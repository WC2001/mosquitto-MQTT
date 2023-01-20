# Project outlining the basics of connecting several instances of the broker using Mosquitto MQTT

### Mosquitto on Docker Contrainer

The `docker-compose.yml`  file includes a basic installation of Mosquitto on a Docker container.

### How to start

1. Start container: 

```bash
docker-compose up -d
```

2. If you want you can change the authentication , to do this you must:
- Get into the relevant container: `docker exec -it mqtt sh`
- Generate authentication file: `mosquitto_passwd -c /mosquitto/config/auth admin`. Replece the `admin` with your own username.
- Enter the password once prompt
- Restart Docker container: `docker compose restart`

3. Test the connection
- use MQTTX or your preferred MQTT client.
- Fill up the username, password (By default username: **admin** password: **admin**), and use `localhost` as the host with `mqtt://` prefix.
- Crete a new subscription on the client and send a message to relevant topic to test.

### Bridge setup

To connect MQTT brokers, you need to set several properties in mosquitto.conf file for respective brokers.

### Mosquitto.conf file for broker1

```conf
listener 1883
listener 9001
protocol websockets

allow_anonymous false
password_file /mosquitto/config/auth

persistence true
persistence_location /mosquitto/data/
 
log_dest file /mosquitto/log/mosquitto.log
allow_anonymous false

connection bridge1
address 172.20.0.11:1884, 172.20.0.12:1885

round_robin true

remote_username admin
remote_password admin

topic # out 0
topic # in 0
```

You can specify the connection by setting the name and address.
In this case there are two addresses given, which will cause broker 1 use second address if the first one's connection fails.
Option **round_robin** determines the behaviour after the primary connection comes back. If set to true second broker remains in use, otherwise broker 1 changes back to first address.

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


