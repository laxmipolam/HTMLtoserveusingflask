#!flask/bin/python
from flask import Flask, jsonify
from flask import abort, render_template
from flask_cors import CORS

application = Flask(__name__)
CORS(application)


@application.route('/')
def index():
   return render_template('weather.html')

if __name__ == '__main__':
    application.run(host='ec2-3-16-181-53.us-east-2.compute.amazonaws.com',port=8002)