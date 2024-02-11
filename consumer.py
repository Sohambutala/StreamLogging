from kafka import KafkaConsumer
import json

# Kafka topic you want to consume
topic_name = 'echoflow_logs'

# Kafka server address
bootstrap_servers = ['localhost:9092']

# Create a Kafka consumer
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',  # Start reading at the earliest message
    group_id=None,  # Do not commit offsets
    enable_auto_commit=False,  # Manual offset management
    value_deserializer=lambda x: json.loads(x.decode('utf-8')) if x else None  # Adjust deserializer as per your message format
)

# Consume messages
for message in consumer:
    print(f"Received message: {message.value} from topic: {message.topic}, partition: {message.partition}, offset: {message.offset}")

# Close the consumer connection
consumer.close()
