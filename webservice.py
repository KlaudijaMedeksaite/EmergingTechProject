# flask to create web app
import flask 
import numpy as np
from flask import render_template, request
import tensorflow as tf
from tensorflow import keras

# Create a new web app.
app = flask.Flask(__name__)

# home route
@app.route("/")
def home():
  return render_template('index.html')

# clicking predict button
@app.route("/send",  methods=['POST'])
def send(sum=sum):
  if request.method == 'POST':
    # gets the speed
    speed = request.form['speedNum'] 


    sum = float(speed)*3 
    return render_template('index.html', sum=sum)
