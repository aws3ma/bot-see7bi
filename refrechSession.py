from flask import Flask
from threading import Thread , Timer
from datetime import datetime

app = Flask('')

@app.route('/')
def home():
  return '<h1>bot see7bi</h1>'
def run():
  app.run(host='0.0.0.0',port=8080)

def keepAlive():
  t = Thread(target=run)
  t.start()



