# Import Flask modules
#render_template is needed to send variables to HTML file
from flask import Flask, render_template

# Create an object named app 
app = Flask(__name__)

# Create a function named head which shows the massage as "This is my first conditions experience" in `index.html` 
# and assign to the route of ('/')
@app.route("/")
def head():
    first = "This is my first conditions"
    return render_template("index.html", message=False)

# Create a function named header which prints numbers from 1 to 10 one by one in `body.html` 
# and assign to the route of ('/tony')
@app.route("/tony")
def header():
    numbers = range(1,11)
    names = ["Serdar", "Matt", "Anu", "Elif", "Tony", "Bill", "Callhan"]
    #the HTML file receiving and the variable you're sending
    return render_template("body.html", object=names)

# run this app in debug mode on your local.
if __name__=="__main__":
    app.run(debug=True)