from kafka import KafkaConsumer
import json

def get_kafka_config():
    kafka_ip = input("Введите IP адрес сервера Kafka: ")
    kafka_port = input("Введите порт Kafka: ")
    topic = input("Введите название топика: ")
    return kafka_ip, kafka_port, topic

def create_kafka_consumer(kafka_ip, kafka_port, topic):
    try:
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=f"{kafka_ip}:{kafka_port}",
            value_deserializer=lambda v: json.loads(v.decode('utf-8')),
            auto_offset_reset='earliest',  # Начинаем читать с самого начала, если ранее не подключались
            enable_auto_commit=True
        )
        print(f"Подключено к Kafka, подписка на топик '{topic}'")
        return consumer
    except Exception as e:
        print(f"Ошибка подключения к Kafka: {e}")
        exit(1)

def main():
    kafka_ip, kafka_port, topic = get_kafka_config()
    consumer = create_kafka_consumer(kafka_ip, kafka_port, topic)

    print(f"Чтение сообщений из топика '{topic}'...")
    try:
        for message in consumer:
            print(f"Получено сообщение: {message.value}")
    except KeyboardInterrupt:
        print("\nОстановка клиента Kafka")
    finally:
        consumer.close()

if __name__ == "__main__":
    main()
