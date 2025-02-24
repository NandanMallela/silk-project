import cv2
import numpy as np
import os
from flask import Flask , render_template, request, url_for, redirect

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def upload_form():
    return  render_template("register.html")

@app.route("/orders")
def upload_form():
    return  render_template("orders.html")

@app.route("/register")
def upload_form():
    return  render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0") 
