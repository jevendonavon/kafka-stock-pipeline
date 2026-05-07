# Kafka Stock Price Streaming Pipeline

A real-time data streaming pipeline using Apache Kafka that simulates 
live stock price feeds and processes them as they arrive.

## What it does

A producer simulates stock price changes every 2 seconds for AAPL, MSFT, 
GOOGL, and AMZN, sending each price update to a Kafka topic. A consumer 
reads and displays the prices in real-time as they stream in.

## Architecture

```
Producer (simulates prices)
↓
Kafka Topic: "stock-prices"
↓
Consumer (reads prices in real-time)
```

## Stack

- Apache Kafka 4.2.0 (KRaft mode — no Zookeeper needed)
- Python 3.12
- kafka-python
- Java 17 (OpenJDK)

## Setup

```bash
# Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install kafka-python pandas
```

## How to run

**Step 1 — Start Kafka:**
```bash
cd ~/kafka_2.13-4.2.0
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties
bin/kafka-server-start.sh config/server.properties
```

**Step 2 — Create topic (new terminal):**
```bash
cd ~/kafka_2.13-4.2.0
bin/kafka-topics.sh --create --topic stock-prices --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

**Step 3 — Start consumer (new terminal):**
```bash
source venv/bin/activate
python consumer.py
```

**Step 4 — Start producer (new terminal):**
```bash
source venv/bin/activate
python producer.py
```

## Sample output

Producer:

Sent: {'ticker': 'AAPL', 'price': 264.74, 'timestamp': '2026-05-07 10:35:39'}
Sent: {'ticker': 'MSFT', 'price': 442.88, 'timestamp': '2026-05-07 10:35:39'}

Consumer:

2026-05-07 10:35:58 | AAPL | $265.29
2026-05-07 10:35:58 | MSFT | $443.87

## What I learned

- How Kafka producers and consumers work
- The difference between batch and streaming data
- Setting up Kafka in KRaft mode (no Zookeeper)
- Why streaming matters for real-time analytics
