import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):
    @task
    def base_test(self):
        self.client.get("/")
        

    @task
    def stress_test_post(self):
        self.client.post("/result", {"Sentence":"I WON"})

    def on_start(self):
        self.client.get("/")

# run using locust -f locust_m.py --host=http://0.0.0.0:5000
