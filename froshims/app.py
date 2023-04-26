from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = ["Football", 
          "Cricket", 
          "Formula 1"
]


@app.route("/")
def index():
    return render_template("index.html", sports = SPORTS)

@app.route("/register", methods = ["POST"])
def register():

    #validate submission

    if not request.form.get("name") or request.form.get("sports") not in SPORTS:
        return render_template("failure.html")
     
    return render_template("success.html")


if __name__ == "__main__": 
    app.run(debug=True)
