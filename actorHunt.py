from flask import Flask, redirect, url_for, render_template
# import writingInfo

app = Flask(__name__)

@app.route("/")
def mainPage():
    return render_template("index.html", content="Hello world")

if __name__ == "__main__":
    app.run(debug=True)