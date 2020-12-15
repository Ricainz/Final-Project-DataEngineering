from flask import Flask, render_template, url_for, request, jsonify
import random
import re
import time
from gensim import models
from nltk.corpus import stopwords
from nltk import word_tokenize, download
from gensim.similarities import WmdSimilarity
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics
import pandas as pd
#download('stopwords')
#download('punkt')


app = Flask(__name__)

app.config['DEBUG'] = True
metrics = GunicornPrometheusMetrics(app)
# MONITORING


stop_words = stopwords.words('english')
model = models.Word2Vec.load('word2vec.model')
df = pd.read_csv('tweets.csv')
df_corpus = pd.DataFrame()
df_corpus['corpus'] = df.text
index_sim = WmdSimilarity(df_corpus['corpus'], model, num_best=20)

def clean_text(text):
    # remove links
    text = re.sub("(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)", '', text)
    text = re.sub("http", '', text)
    # remove retweets
    text = re.sub(r'^RT @.+\:', '', text)
    text = re.sub('@', '', text)
    # remove hastags
    text = text.replace("#","")
    # remove empty lines
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r"\'", "", text)
    # lowering text
    text = text.lower()
    # remove non alhanumerical chars
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    # remove stopwords
    return [word for word in word_tokenize(text) if word not in stop_words]


@app.route('/')
@metrics.counter('page_accesses', 'Main page acces')
def index():
    return render_template('base.html')

@app.route('/result', methods=['POST'])
@metrics.counter('page_results', 'Result page acces')
@metrics.gauge('page_accesses_inprogress', 'Number of visits in progress.')
@metrics.summary('latency_from_main_to_results', 'Time for a request to process',
                 labels={'status': lambda r: r.status_code})
def result():
    if request.method == 'POST':
       
        start = time.time()
        data =  request.form['Sentence']
        cleaned_data = clean_text(data)
        similar = index_sim[cleaned_data]
        print(len(similar))
        res_score = list()
        res_text = list()
        for i in range(len(similar)):
            res_score.append(similar[i][1])
            res_text.append(df_corpus['corpus'][similar[i][0]])
        res_score = ["{:.3f}".format(score) for score in res_score]
     
        return render_template('results.html',res=zip(res_score,res_text),querry=data)
    return render_template('base.html')

if __name__ == "__main__":
  
    app.run(host='0.0.0.0')
