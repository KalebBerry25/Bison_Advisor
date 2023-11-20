import pyrebase
from flask import *

config = {
"apiKey": "AIzaSyBurNMdpk2CxK8fo6Q4HDrEkE3liRy85H4",
"authDomain": "bison-advisor-group-n.firebaseapp.com",
"projectId": "bison-advisor-group-n",
"storageBucket": "bison-advisor-group-n.appspot.com",
"messagingSenderId": "69696678672",
"appId": "1:69696678672:web:eec07336c9c210d45d9395",
"measurementId": "G-SLY1NJN3JX",
"databaseURL": "https://console.firebase.google.com/u/0/project/bison-advisor-group-n/database/bison-advisor-group-n-default-rtdb/data/~2F"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__)

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if request.method == "POST":
    email = request.form["email"]
    password = request.form["password"]
    try:
      auth.create_user_with_email_and_password(email, password)
      user = auth.sign_in_with_email_and_password(email, password)   
      user_id = user['idToken']
      user_email = email
      session['usr'] = user_id
      session["email"] = user_email
      return redirect("/") 
    except:
      return render_template()  
  return render_template()

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    email = request.form["email"]
    password = request.form["password"]
    try:
      user = auth.sign_in_with_email_and_password(email, password)
      user_id = user['idToken']
      user_email = email
      session['usr'] = user_id
      session["email"] = user_email
      return redirect("/")  
    except:
      return render_template()  
  return render_template()


@app.route("/logout")
def logout():
  auth.current_user = None
  session.clear()
  return redirect("/")


