import json
import random
from kafka import KafkaProducer

class PageView:

    def __init__(self, url: str):
        self._url = url

    @property
    def url(self):
        return self._url

    def to_json(self):
        return json.dumps({"pageview": {"url": self.url}})


class PageViewKafkaLogger:

    def __init__(self, broker: str = ['localhost:9092']):
        self.producer = KafkaProducer(bootstrap_servers=broker)

    def produce(self, pageview: PageView):
        try:
            future = self.producer.send(topic='pageview', key=f"{random.randrange(999999)}".encode(), value=pageview.to_json().encode())
            record_metadata = future.get(timeout=10)
            print(pageview.to_json().encode())
        except Exception as e:
            print(e)


if __name__ == "__main__":
    producer = PageViewKafkaLogger()
    while True:
        pv = PageView(f"URL{random.randrange(9999)}")
        producer.produce(pv)
