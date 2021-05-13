from flask import Flask

app = Flask(__name__)

def create_app(settings_module='config.dev'):

@app.route('/')
def hello_world():
    return 'Hello, World!'