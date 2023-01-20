import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_disconnect(client, userdata, rc):
    print("Disconnected with result code "+str(rc))
    failed_attempts = 0
    for address in addresses:
        try:
            client.connect(address)
        except:
            print(f"Failed to connect to {address}")
            failed_attempts += 1
            if failed_attempts >= 10:
                print("Exceeded maximum number of failed attempts.")
                return
        else:
            print(f"Connected to {address}")
            break
    client.loop_forever()


addresses = ["test.mosquitto.org", "iot.eclipse.org"]

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect


for address in addresses:
    try:
        client.connect(address)
    except:
        print(f"Failed to connect to {address}")
    else:
        print(f"Connected to {address}")
        break


client.loop_forever()