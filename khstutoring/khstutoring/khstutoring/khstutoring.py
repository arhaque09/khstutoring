from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
app1 = Flask("app", static_folder='static', template_folder="templates")

@app.route('/')
def home(): 
    return render_template("home.html")

@app.route('/about/')
def about(): 
    return render_template("about.html")

@app.route('/scheduling/')
def scheduling(): 
    return render_template("scheduling.html")

@app.route('/contact_us/')
def contact_us(): 
    return render_template("contact_us.html")


if __name__=="__main__":
    app.run(debug=True)