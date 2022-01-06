from flask import (
    Flask,
    json,
    redirect,
    url_for,
    render_template,
    request,
    jsonify,
    make_response,
)
import writingInfo
import requests
import sqlite3
import json

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def mainPage():
    return render_template("index.html", content="")

    # actorName, actorJobs, actorBD, actorPhotoPath = writingInfo.DoIt(request.form["actor"])
    # return render_template("actorDisplay.html", content=[actorName, actorJobs, actorBD, actorPhotoPath])
    # print(request.form["actor"])


@app.route("/search", methods=["POST", "GET"])
def getJson():
    if request.method == "POST":
        req = request.get_json()

        actorName, actorBD, actorJobs, actorPhotoPath, _ = writingInfo.DoIt(req["name"])
        
        res = make_response(
            json.dumps(
                {
                    "name": actorName,
                    "job": actorJobs[1:-1],
                    "dob": actorBD[5:],
                    "pic": actorPhotoPath,
                }
            ),
            200,
        )
        return res
    return "get request received, something wrong"





if __name__ == "__main__":
    app.run(debug=True)
