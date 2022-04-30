import random
from kafka import KafkaConsumer

consumer = KafkaConsumer('pageview',
                         auto_offset_reset='latest',
                         group_id=f'pageview-group-{random.randrange(99999)}',
                         bootstrap_servers='localhost:9092')
for message in consumer:
    print(f"""
        {message.topic}:{message.partition}:{message.offset}
        key={message.key} value={message.value}
    """)
