from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello! I am Muhammad Yasir . I study in Virtual Federal University of Pakistan'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

