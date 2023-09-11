from flask import *


# start 
app = Flask(__name__)

@app.route('/test')
def test():
    return "HELLO THERE!!!!"

# replace message "welcome to login screen" with a login screen

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

# add '/signup' route and return the message "This is the signup page"
@app.route('/signup')
def signup():
    return "This is the signup page"

@app.route('/saysomething')
def saysomething():
    return "Hi there"


app.run(debug=True)
# end