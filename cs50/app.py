from flask import Flask, render_template, request

app = Flask(__name__) # tells python to convert this files to consider this as a flask application

@app.route("/") # default page
def index():
    # name = request.args.get("name") #pulls the data after ? in the url
    return render_template("index.html")
                          # , name_of_person = name) # render this template to the user 
    # name is passed to html file from app.py file to index.html


@app.route("/greet", methods = ["POST"])
def greet():
    # name = request.args.get("name")
    name = request.form.get("name")
    return render_template("greet.html", name_of_person = name)

# request.args.get for get method
# request.form,get for post method


if __name__ == "__main__": 
    #run the application if the it called
    app.run(debug=True)

