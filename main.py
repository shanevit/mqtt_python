import paho.mqtt.client as mqtt #import the client1
import pandas_datareader.data as web
from pandas_datareader.data import get_quote_yahoo
import time
#import time
############
def burza():
    czg = web.DataReader("CZG.PR", 'yahoo')
    posledni = czg.iloc[[-1]]
    cena = get_quote_yahoo('CZG.PR').price[0]
    print(' ')
    return(str(cena) + ' Kc ')


def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################

old_zprava = ''

broker_address="192.168.1.21"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
#client.loop_start() #start the loop
print("Subscribing to topic","esp32/temp")
client.subscribe("esp32/temp")

client.loop_start()

while True:
    zprava = burza()
    if zprava != old_zprava:
        print("Publishing message to topic", "esp32/temp")
        client.publish("esp32/temp", zprava)
    else:
        print('nic')
    time.sleep(5)
    old_zprava = zprava

client.loop_stop()

# TODO: uhladit
# TODO: Threading