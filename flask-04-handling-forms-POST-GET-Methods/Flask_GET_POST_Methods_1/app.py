# Import Flask modules
from flask import Flask, render_template, request

# Create an object named app
app = Flask(__name__)

# Create a function named `index` which uses template file named `index.html` 
# sent three numbers as template variable to the app.py and assign route of no path ('/') 
@app.route("/")
def index():
    return render_template("index.html")


# calculate sum of them using inline function in app.py, then sent the result to the 
# "number.hmtl" file and assign route of path ('/total'). 
# When the user comes directly "/total" path, "Since this is GET 
# request, Total hasn't been calculated" string returns to them with "number.html" file
@app.route("/total", methods = ["GET", "POST"])
def total():
    if request.method == "POST":
        # can use this syntax to get the values from the form
        # value1 = request.form['value1']
        # or use the methods below
        # the form is on the index.html page - the values are come from that form
        num1 = request.form.get("value1") # value1 = request.form['value1']
        num2 = request.form.get("value2")
        num3 = request.form.get("value3")
        #the return is sending the values to the number.html
        return render_template("number.html", total= int(num1)+int(num2)+int(num3))
    else:
        return render_template("number.html")





# Add a statement to run the Flask application which can be debugged.
if __name__== "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=80)