# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np
from flask import render_template

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return render_template('index.html')
