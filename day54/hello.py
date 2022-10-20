from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_code():
    return "Hello 100 days of code"

@app.route('/dupa')
def hello_dupa():
    return "Hello dupa"

if __name__ == "__main__":
    app.run()
