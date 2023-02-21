import paho.mqtt.client as mqtt
import serial
from xbee import XBee

# Set up the serial port for the XBee module
ser = serial.Serial('COM1', 9600)  # Replace with the correct serial port and baud rate for your setup

# Set up the XBee module
xbee = XBee(ser, escaped=True)

# Set up the MQTT client
client = mqtt.Client()
client.connect("broker.hivemq.com", 1883)  # Replace with the address and port of your MQTT broker

# Define the callback function for when a message is received
def on_message(client, userdata, msg):
    with open('xbee_data.txt', 'a') as f:
        f.write(msg.payload.decode() + '\n')
        print("Message written to file")

# Subscribe to a topic
client.subscribe("example/topic")

# Set the callback function for incoming messages
client.on_message = on_message

# Start the MQTT loop
client.loop_start()

# Wait for incoming messages
while True:
    try:
        # Wait for a message from the XBee module
        response = xbee.wait_read_frame()
        
        # Convert the payload to a string
        payload ="D0"
        
        # Publish the payload to the MQTT broker
        client.publish("example/topic", response)
    except KeyboardInterrupt:
        break

# Stop the MQTT loop
client.loop_stop()
