from locust import HttpUser, task, between

class Product(HttpUser):
    wait_time = between(1, 5)
    @task
    def get_products(self):
        self.client.get("")
        self.client.post(
            "",
            data={"title":"some title", "content": "some content"}
        )
