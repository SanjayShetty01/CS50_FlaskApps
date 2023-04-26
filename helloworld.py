from flask import Flask

# initializing the application
app = Flask(__name__)

#route handling 
@app.route("/")
# the below function gets called whenever the above route in called
def index():
    return "Hello World"

    

if __name__ == "__main__": 
    #run the application if the it called
    app.run(debug=True)