"""
App file
"""
from flask import Flask


app = Flask(__name__)
app.config.from_object('simplestorymaker.config.Configuration')
