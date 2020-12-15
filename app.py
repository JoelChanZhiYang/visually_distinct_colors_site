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


@app.route("timetable/all/<int:userID>")
def getUserTimetable(userID):
    try:
        data = db.User-Lesson.find({"userID": userID}).pretty()
    except Exception as e:
        return {err: e}, 400
    return data, 200


@app.rote("/user_CA/<int:ccaID>")
def getCcaMembers(ccaID):
    try:
        data = db.userHasCCA.find({"ccaID": ccaID})
    except Exception as e:
        return {err: e}, 400
    return data, 200


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
