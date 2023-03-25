import json
import time
from kafka import KafkaProducer
from faker import Faker


TOPIC_NAME = "user-registration"
SERVER_ADDRESS = '127.0.0.1:9092'



producer = KafkaProducer(
    bootstrap_servers=SERVER_ADDRESS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


def get_user_information() -> dict:
    """Generate Fake User Data from Python Faker Library"""

    fake = Faker()
    return {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "country": fake.country(),
    }


if __name__ == "__main__":
    """
       1. Get Fake User Data 
       2. Send the fake data to the consumer topic 
       3. Sleep 10 seconds and repeat the process utill press Crontrol C
    """

    try:
        while(True):
            registered_user_data = get_user_information()
            print(registered_user_data)
            producer.send(TOPIC_NAME, registered_user_data)
            time.sleep(10)
    except KeyboardInterrupt:
       print("Quit")