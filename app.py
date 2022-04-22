from flask import Flask
from random import randint, random

app = Flask(__name__)

@app.route('/')
def hello_world():
    value = random()
    return str(int(value * 1000))

if __name__ == '__main__':
   app.run()