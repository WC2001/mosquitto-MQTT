# Project outlining the basics of connecting several instances of the broker using Mosquitto MQTT

### To run use command

docker-compose up --build

### Bridge setup

To connect MQTT brokers, you need to set several properties in mosquitto.conf file for respective brokers.

### Mosquitto.conf file for broker1

<div align="center">
<img src="/assets/mosquitto_conf.png" alt="mosquitto_conf">
</div>

You can specify the connection by setting the name and address.
In this case there are two addresses given, which will cause broker 1 use second address if the first one's connection fails.
Option round_robin determines the behaviour after the primary connection comes back. If set to true second broker remains in use, otherwise broker 1 changes back to first address.

### Diagram

<div align="center">
<img src="/assets/diagram.png" alt="diagram">
</div>

### Shared Subscriptions visualisation using paho.mqtt

Open mosquitto server on your local machine and use the command:

python3 shared_subscription.py

The script creates six subscribers, two of them subscribe on shared topic *$share/group1/test*, other two on *$share/group2/test* and remaining two on *test*. After that there is a message published on topic *test*.

As subscribers 1 and 2 are in the same share-group only one of them is going to receive the message, the same applies to subscribers 3 and 4.
All subscribers subscribing to topic *test* will receive the message.
As a result there are 4 clients that received a message.

This mechanism might be usefull for load balancing MQTT-clients and 'hot topics' that could overload one mqtt client.


### Schared subscription

<div align="center">
<img src="/assets/shared_subscription.png" alt="shared_subscription">
</div>


