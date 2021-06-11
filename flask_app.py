from flask import Flask, render_template, redirect, url_for, request
from overheal.readers import read_heals

app = Flask(__name__)
app.config["DEBUG"] = True

warcraftlog = ""

@app.route('/', methods=["GET", "POST"])
def index():
    global warcraftlog

    if request.method == "GET":
        # process the link
        heals = None
        error = None

        if warcraftlog:
            heals, error = read_heals(warcraftlog)

        return render_template("overheal.html", warcraftlog=warcraftlog, info=heals, error=error)

    warcraftlog = request.form["warcraftlog_url"]
    return redirect(url_for("index"))

