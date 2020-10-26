import ssd1306
i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 60)
oled.fill(0)
oled.text("   dvaroboti.cz", 0, 0)
oled.show()

gc.collect()
esp.osdebug(None)

led = machine.Pin(16, machine.Pin.OUT)
cas_konec = 0
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
  blink_ms(0, False)
  try:
    client.check_msg()
    
  except OSError as e:
    restart_and_reconnect()
    