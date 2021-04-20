import os
from os.path import join, dirname
from dotenv import load_dotenv
import paho.mqtt.client as paho
import paho.mqtt.publish as publish
from time import sleep
import serial

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


with serial.Serial(os.environ.get("PORT"), 9600) as ser:
    while(True):
        try:
            line = ser.readline().decode('utf-8')
            if line.find('No card') == -1:
                start = line.find('[')
                ending = line.find(']')
                card_id = line[start+1:ending]
                print("Card ID:", card_id)
                publish.single(os.environ.get("TOPIC"), card_id, hostname=os.environ.get("HOST"), client_id=os.environ.get("ID"), keepalive=3)
        except KeyboardInterrupt:
            break


