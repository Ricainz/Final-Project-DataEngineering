FROM python:3.6 
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip install -r requirements.txt
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt

ADD . /app
RUN chmod +x ./entrypoint.sh
EXPOSE 5000
EXPOSE 8080
ENV prometheus_multiproc_dir /tmp
