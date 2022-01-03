from flask import Flask, redirect, url_for, render_template, request
import writingInfo

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def mainPage():
    if request.method != "POST":
        return render_template("index.html", content="")

    actorName, actorJobs, actorBD, actorPhotoPath = writingInfo.DoIt(request.form["actor"])
    return render_template("actorDisplay.html", content=[actorName, actorJobs, actorBD, actorPhotoPath])



if __name__ == "__main__":
    app.run(debug=True)