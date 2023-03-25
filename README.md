# Kafka-Streaming

This project aims to demonstrate a simple implementation of Kafka message streaming using Python. The project includes a producer, which sends messages to Kafka, and a consumer, which consumes these messages. The messages in this project are generated using Python's fake user information data. With this project, you can learn the basics of Kafka messaging and how to use Python to generate and consume messages.

Prerequisite:
----
   - Docker 
   - docker-compose 
   - Python3.11


Installation:
----
1. We need to up the Kafka server along with zookeeper & Kafdrop Admin Frontend type the below command

    ```
    docker-compose up 
    ``` 
    in case of run demon mode: 
    ```
    docker-compose up -d 
    ``` 
2. After  executing the step (1) we will visit: 
    ```
    http://127.0.0.1:9002/
    ```
3. After exectuting (1) & (2) now we are ready to create topic using this admin dashboard. The steps along with screenshot given below: 

   ![alt text](https://raw.githubusercontent.com/Tarequzzaman/Kafka-Streaming/main/asset/Dashboard.png)
  
   As in our code we will added `user-registration` as Kafka topic, we need to create new topic from the topic section of the dashbaord 

   ![alt text](https://raw.githubusercontent.com/Tarequzzaman/Kafka-Streaming/main/asset/TopicSection.png)

   Now we will put the topic name and partition and replication factor. As we have use only one kafka server as standlone. In our case we need to keep replication factor 1 

   ![alt text](https://raw.githubusercontent.com/Tarequzzaman/Kafka-Streaming/main/asset/TopicName.png)

   We have done with created our topic. Now we are allowing to send and receive message through this topic. 

   ![alt text](https://raw.githubusercontent.com/Tarequzzaman/Kafka-Streaming/main/asset/created-topic.png)
  

4. In this step we will do all python related task
    - Create a virtual-environment & activate it 

        ```
        python3.11 -m venv env 
        ```

        ```
        source env/bin/activate
        ```

    - Receive meeage via consumer.
 
        ```
        python consumer.py
        ```

   


    - Send message through producer. After environment activation we need to type 
        ```
        python producer.py
        ```

Reference:
---
1. https://github.com/obsidiandynamics/kafdrop
2. https://kafka-python.readthedocs.io/en/master/
