from twilio.rest import Client 
import requests 
from datetime import datetime
from threading import Timer

try:
    from console_thrift import KeyboardInterruptException as KeyboardInterrupt
except ImportError:
    pass
"""Twilio Account SID and Auth Token"""
client = Client("ACxxxxxxxxxxxxxx", "zzzzzzzzzzzzz")

r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR%27')
r = r.json()
usd = r['USD']

number = input("Enter your phone number (e.g. +1 212-359-4029): ")

def SMS():

    message = client.messages.create(  
                                      messaging_service_sid='zzzzzzzzzzzzz', # service sid
                                      body=f'{str(usd)}$',      
                                      to='number' 
                                  ) 
         
    print(message.sid)

x=datetime.today()
y=x.replace(day=x.day+1, hour=8, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

t = Timer(secs, SMS)
t.start()

