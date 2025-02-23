from machine import Pin, ADC
import ujson
import network
import utime as time
import dht
import urequests as requests

LDR_PIN = Pin(34)
DHT_PIN = Pin(15)
DEVICE_ID = "esp32-monitoring"
WIFI_SSID = ""
WIFI_PASSWORD = ""
TOKEN = "BBUS-qtusJBMGHKfz4bRZE9wlo8W2YVx8zl"

def send_data(temperature, humidity, light):
    url_ubidots = "http://industrial.api.ubidots.com/api/v1.6/devices/" + DEVICE_ID
    url_mongodb = "https://4c97-103-125-43-188.ngrok-free.app/sensor"  # using ngrok
    # url_mongodb = "http://localhost:8000/sensor"  # api in localhost:8000
    # url_mongodb = "http://192.168.1.3:8000/sensor"  # if failed, use this to connect API which hosted Flask global ip based on the laptop
    
    headers = {"Content-Type": "application/json", "X-Auth-Token": TOKEN}
    data = {
        "temp": temperature,
        "humidity": humidity,
        "ldr_value": light
    }
    print(data)
    
    response_ubidots = requests.post(url_ubidots, json=data, headers=headers)
    response_mongodb = requests.post(url_mongodb, json=data, headers={"ngrok-skip-browser-warning": "true"})
    
    print("Done Sending Data To Ubidots and MongoDB!")
    print("Response Ubidots:", response_ubidots.text)
    print("Response MongoDB:", response_ubidots.text)
    
    response_ubidots.close()
    response_mongodb.close()
    print("\n")

wifi_client = network.WLAN(network.STA_IF)
wifi_client.active(True)
print("Connecting to WiFi...")
wifi_client.connect(WIFI_SSID, WIFI_PASSWORD)

while not wifi_client.isconnected():
    print("Connecting...")
    time.sleep(0.1)
print("WiFi Connected!")
print(wifi_client.ifconfig())

dht_sensor = dht.DHT11(DHT_PIN)
ldr_sensor = ADC(Pin(34))
ldr_sensor.atten(ADC.ATTN_11DB)

while True:
    ldr_value = -1
    
    try:
        dht_sensor.measure()
        ldr_value = ldr_sensor.read()
    except:
        pass

    time.sleep(0.5) 
    
    if ldr_value != -1:
        send_data(dht_sensor.temperature(), dht_sensor.humidity(), ldr_value)
    else:
        print("Sensor Error")
    
    time.sleep(5)
