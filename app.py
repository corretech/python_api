from flask import Flask
from dotenv import load_dotenv
import os
import openai
import requests
import urllib.request
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from twilio.rest import Client
account_sid = os.getenv('ACCOUNT_SID') # Your Account SID from www.twilio.com/console
auth_token  = os.getenv('AUTH_TOKEN')  # Your Auth Token from www.twilio.com/console

app = Flask(__name__)
load_dotenv(override=True)


@app.route('/')
def index():
  return "hello word"

@app.route('/key')
def key():
   return account_sid

@app.route("/world/<country>")
def hello_world(country):
    return f"<p>Hello, {country}!</p>"

@app.route("/twilio/<string:phone_number>/<string:token>/")
def twilio(phone_number, token):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f'コレテクの認証コード：{token}',
        to=f"+81{phone_number}",
        from_="+19897188878",
    )
    return f"<p>{message.sid}</p>"