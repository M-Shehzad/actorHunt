from flask import Flask, json, redirect, url_for, render_template, request, jsonify, make_response
import writingInfo
import requests

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def mainPage():
    return render_template("index.html", content="")

    # actorName, actorJobs, actorBD, actorPhotoPath = writingInfo.DoIt(request.form["actor"])
    # return render_template("actorDisplay.html", content=[actorName, actorJobs, actorBD, actorPhotoPath])
    # print(request.form["actor"])
    

@app.route("/search", methods = ["POST", "GET"])
def getJson():
    if request.method == "POST":
        # print(request)
        req = request.get_json()
        print(req)
        actorName, actorJobs, actorBD, actorPhotoPath = writingInfo.DoIt(req["name"])
        res = make_response(jsonify({"name":actorName,
                                        "job": actorJobs,
                                        "dob":actorBD,
                                        "pic":actorPhotoPath}), 200)
        print(res.data)
        return "post request working"
    return "get request"

@app.route("/result", methods=["POST"])
def resultPage(par):
    # print(par)
    return "helloworld"


if __name__ == "__main__":
    app.run(debug=True)