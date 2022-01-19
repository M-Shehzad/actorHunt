from flask import (
    Flask,
    json,
    render_template,
    request,
    make_response,
)
import writingInfo
import json

# Defining a FLASK web app
app = Flask(__name__)

# Route to the main page and rendering main page html
@app.route("/", methods=["POST", "GET"])
def mainPage():
    return render_template("index.html", content="")


@app.route("/search", methods=["POST", "GET"])
def getJson():
    if request.method == "POST":
        req = request.get_json() # getting the request data from client

        actorName, actorBD, actorJobs, actorPhotoPath, _ = writingInfo.DoIt(req["name"])
        
        res = make_response(
            json.dumps( # Converting the data received into an JSON Format
                {
                    "name": actorName,
                    "job": actorJobs,
                    "dob": actorBD[5:],
                    "pic": actorPhotoPath,
                }
            ),
            200, 
        )
        return res # returning the JSON data to client with STATUS 200 OK 
    return "get request received, something wrong"





if __name__ == "__main__":
    app.run(debug=True) # debug is set True to refresh the server whenever the changes are made
