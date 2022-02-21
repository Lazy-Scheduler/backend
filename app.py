import os
import json
from flask import Flask
import requests

# blueprints
from src.views.policy_render import policy
from src.views.posta import posta

app = Flask(__name__)

#register blueprints
app.register_blueprint(policy)
app.register_blueprint(posta)

@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)