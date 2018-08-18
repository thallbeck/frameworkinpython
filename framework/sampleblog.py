from selenium import webdriver
from flask import Flask
app = Flask(__name__)

@app.route("/")
def test():
    return "First page"
