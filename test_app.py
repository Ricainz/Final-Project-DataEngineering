import unittest
import requests
import app


class TestApp(unittest.TestCase):

    def test_a_base(self):
        response = requests.get('http://localhost:5000')
        self.assertEqual(response.status_code, 200)

    def test_result(self):
        Sentence = "Here is my statement: *Hello*, pic.fghdfger"
        res = app.clean_text(Sentence)
        self.assertEqual(res, ['statement', 'hello'])
    
    def test_response(self):

        params = {
            'Sentence': 'MAGA'
        }
        response = requests.post('http://localhost:5000/result', data=params)
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
	unittest.main()	
