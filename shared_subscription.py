import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes 
import time,logging,sys

client_id="test"
mqttv=mqtt.MQTTv5
messages=[]

host = '127.0.0.1'
port = 1883

pub_topic = "test"
clients = []

def on_publish(client, userdata, mid):
    print("published")

def on_connect(client, userdata, flags, reasonCode,properties=None):
    print('Connected ',reasonCode)


def on_message(client, userdata, message):
    msg=str(message.payload.decode("utf-8"))
    messages.append(msg)
    print(client, end=": ")
    print('RECV Topic = ',message.topic, end=", ")
    print('RECV MSG =', msg)


def on_disconnect(client, userdata, rc):
    print('Received Disconnect ',rc)

def on_subscribe(client, userdata, mid, granted_qos,properties=None):
    print('SUBSCRIBED')

def on_unsubscribe(client, userdata, mid, properties, reasonCodes):
    print('UNSUBSCRIBED') 


print("creating client")
client = mqtt.Client("client1",protocol=mqttv)

def assign_callbacks(client):
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe
    client.on_publish = on_publish
    client.loop_start()
    clients.append(client)


client1 = mqtt.Client("client1")
client2 = mqtt.Client("client2")
client3 = mqtt.Client("client3")
client4 = mqtt.Client("client4")
client5 = mqtt.Client("client5")
client6 = mqtt.Client("client6")
pub_client = mqtt.Client("pub_client")
assign_callbacks(client1)
assign_callbacks(client2)
assign_callbacks(client3)
assign_callbacks(client4)
assign_callbacks(client5)
assign_callbacks(client6)
properties=None
client1.connect(host,port,properties=properties)
client2.connect(host,port,properties=properties)
client3.connect(host,port,properties=properties)
client4.connect(host,port,properties=properties)
client5.connect(host,port,properties=properties)
client6.connect(host,port,properties=properties)

time.sleep(10)
print("client 1 and 2 subscribe to shared topic $share/group1/test")
client1.subscribe('$share/group1/test')
client2.subscribe('$share/group1/test')
print("client 3 and 4 subscribe to shared topic $share/group2/test")
client3.subscribe('$share/group2/test')
client4.subscribe('$share/group2/test')
print("client 5 and 6 subscribe to topic test")
client5.subscribe('test')
client6.subscribe('test')

assign_callbacks(pub_client)
pub_client.connect(host,port,properties=properties)
time.sleep(5)
print("publishing message to topic test")
pub_client.publish('test',"test message")


time.sleep(5)

client.disconnect()
for client in clients:
    client.loop_stop()
    client.disconnect()
time.sleep(5)  

