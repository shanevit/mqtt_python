last_message = 0
message_interval = 10
counter = 0
topic_sub = b'esp32/temp'
station = network.WLAN(network.STA_IF)
station.active(True)
client_id = ubinascii.hexlify(machine.unique_id())


try:
  mqtt_server = pripoj_se_scan(station) # pripoji se k wifi a vrati adresu MQTT serveru
  client = connect()
  subscribe()
  
except OSError as e:
  restart_and_reconnect()
  
while True:
  try:
    client.check_msg()
    
  except OSError as e:
    restart_and_reconnect()
    