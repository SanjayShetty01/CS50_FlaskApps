from flask import Flask, render_template, request, redirect

app = Flask(__name__)

REGISTRANTS = {}

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

    name = request.form.get("name")

    if not name:
        return render_template("error.html", message = "Missing Name")
    
    sport = request.form.get("sport")

    if not sport:
        return render_template("error.html", message = "Missing Sport")
    
    if sport not in SPORTS:
        return render_template("error.html", message = "Invalid Sport")

    # Remember registrants

    REGISTRANTS[name] = sport
     

    return redirect("/registrants")

@app.route("/registrants")
def registerants():
    return render_template("registrants.html", registrants = REGISTRANTS)

if __name__ == "__main__": 
    app.run(debug=True)
