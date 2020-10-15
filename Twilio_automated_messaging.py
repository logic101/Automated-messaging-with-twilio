# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 08:35:22 2020

@author: Regan
"""

from twilio.rest import Client
import schedule
import random
import time

messages = ['Hey! Wake up sleepy?', 
            'Good Morning?',
            'How was your night?']

def send_message(quotes = messages):
    account = ''
    token = ''
    quote = quotes[random.randint(0, len(messages)-1)]
    client = Client(account, token)
    client.messages.create(to = '',
                           from_= '',
                           body = quote)


schedule.every().day.at("09:37").do(send_message, messages)

while True:
    schedule.run_pending()
    time.sleep(2)
