import json
import time
import random
from kafka import KafkaProducer
from datetime import datetime

# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Stock tickers with base prices
stocks = {
    'AAPL': 265.0,
    'MSFT': 443.0,
    'GOOGL': 310.0,
    'AMZN': 226.0
}

print("🚀 Producer started — sending stock prices...")

while True:
    for ticker, base_price in stocks.items():
        # Simulate small price change
        change = random.uniform(-2.0, 2.0)
        price = round(base_price + change, 2)
        
        message = {
            'ticker': ticker,
            'price': price,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        producer.send('stock-prices', value=message)
        print(f"Sent: {message}")
    
    time.sleep(2)  # send every 2 seconds