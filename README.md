# Kafka Consumer на Python

Этот скрипт реализует Kafka-клиент, который подключается к серверу Kafka, подписывается на указанный топик и выводит полученные сообщения на экран в реальном времени.

## Требования

- Python 3.7 или выше
- Установленный и настроенный сервер Kafka
- Библиотека `kafka-python`

## Установка

1. Клонируйте или скопируйте данный скрипт в ваш проект.
2. Установите зависимости:
   ```bash
   pip install kafka-python
Использование

Убедитесь, что сервер Kafka запущен и топик, из которого вы хотите читать сообщения, существует.
Запустите скрипт:
python kafka_consumer.py
Введите параметры подключения:
IP-адрес сервера Kafka
Порт Kafka (обычно 9092)
Название топика, из которого нужно читать сообщения
Скрипт начнет отображать сообщения, которые поступают в указанный топик. Для завершения работы нажмите Ctrl+C.
Поведение скрипта

Скрипт читает сообщения с начала топика, если ранее подключение не выполнялось (auto_offset_reset='earliest').
Если в топике нет сообщений, скрипт ждет поступления новых.
Пример вывода

При успешной работе скрипт отображает полученные сообщения в реальном времени:

Введите IP адрес сервера Kafka: 127.0.0.1
Введите порт Kafka: 9092
Введите название топика: test_topic
Подключено к Kafka, подписка на топик 'test_topic'
Чтение сообщений из топика 'test_topic'...
Получено сообщение: {'id': 123, 'message': 'Random message 456', 'timestamp': 1699887601.123456}
Получено сообщение: {'id': 789, 'message': 'Random message 987', 'timestamp': 1699887602.987654}
Заметки

Убедитесь, что Kafka работает, а топик содержит сообщения. Если сообщений в топике нет, скрипт будет ждать их поступления.
Сообщения предполагаются в формате JSON, чтобы корректно десериализовать их в объект Python.
Вы можете настроить скрипт для чтения сообщений в режиме реального времени или управления смещением (offset) в зависимости от потребностей.
Поддержка

Если у вас возникли вопросы или проблемы, открывайте Issue в репозитории или создайте Pull Request для улучшений.

Лицензия

Этот проект распространяется под MIT License.