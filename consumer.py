import json
from kafka import KafkaConsumer

# Connect to Kafka topic
consumer = KafkaConsumer(
    'stock-prices',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("👂 Consumer listening for stock prices...")

for message in consumer:
    data = message.value
    print(f"📈 {data['timestamp']} | {data['ticker']} | ${data['price']}")