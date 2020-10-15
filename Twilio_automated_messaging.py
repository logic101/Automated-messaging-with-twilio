# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 08:35:22 2020

@author: Regan
"""

messages = ['Hey! Wake up sleepy?', 
            'Amka yawa!',
            'Wakie!! wakie!!']
from twilio.rest import Client
import schedule
import random
import time

def send_message(quotes = messages):
    account = 'AC22fc516fe468a4961281c23e434358a9'
    token = 'fbeed57d958a22d57229a287f5156513'
    quote = quotes[random.randint(0, len(messages)-1)]
    client = Client(account, token)
    client.messages.create(to = '+254726232429',
                           from_= '+14159664245',
                           body = quote)


schedule.every().day.at("09:37").do(send_message, messages)

while True:
    schedule.run_pending()
    time.sleep(2)
