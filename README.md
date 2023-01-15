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


