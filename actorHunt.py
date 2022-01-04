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
        # print(request)
        req = request.get_json()
        print(req)

# --------------------------DATABASE-------------------------------------------------------------------------------
        conn = sqlite3.connect("database.sqlite")
        cur = conn.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS ACTORHUNT (NAME TEXT, DOB TEXT, JOB TEXT, PICTURE TEXT)")
        cur.execute("SELECT * FROM ACTORHUNT WHERE NAME = ?",(req["name"].lower(),))
        data = cur.fetchone()
        if data is None:
            actorName, actorJobs, actorBD, actorPhotoPath = writingInfo.DoIt(req["name"])
            cur.execute("INSERT INTO ACTORHUNT (NAME, DOB, JOB, PICTURE) VALUES (?, ?, ?, ?)",(str(actorName).lower(), str(actorBD), str(actorJobs), str(actorPhotoPath)))

        else:
            actorName, actorBD, actorJobs, actorPhotoPath = data
        cur.close()
        conn.close()
# -----------------------------------------------------------------------------------------------------------------

        res = make_response(
            jsonify(
                {
                    "name": actorName,
                    "job": actorJobs,
                    "dob": actorBD,
                    "pic": actorPhotoPath,
                }
            ),
            200,
        )
        print(res.data)
        return res
    return "get request received, something wrong"





if __name__ == "__main__":
    app.run(debug=True)
