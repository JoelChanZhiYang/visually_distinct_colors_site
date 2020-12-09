from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@app.route("/json")
def respond():
    response = {}
    response["text"] = "Hello World!"
    return jsonify(response)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)