import os
import pyrebase
from flask import *
from ChatAI import chat
import tempfile
import time





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
store = firebase.storage()


app = Flask(__name__)

app.secret_key = 'secret'

@app.route("/login", methods=["GET", "POST"])
def login():
  print(request.form)
  if request.method == "POST":
    email = request.form["email"]
    print(email)
    password = request.form["password"]
    try:
      user = auth.sign_in_with_email_and_password(email, password)
      user_id = user['idToken']
      user_email = email
      session['usr'] = user_id
      session["email"] = user_email
      return redirect("/")
    except:
      return render_template('login.html')  
  return render_template('login.html')


@app.route("/logout")
def logout():
  session.clear()
  return redirect("/login")

@app.route('/', methods=["GET","POST"])
def query():
  print(request.form)
  if request.method == "POST" and "query" in request.form:
    query = request.form["query"]
    answer = chat.get_answer(query)
    return render_template('home.html', answer=answer)
  return render_template('home.html')

@app.route('/advising', methods=["GET","POST"])
def advising():
  print(request.form)
  if request.method == "POST" and "query" in request.form:
    query = request.form["query"]
    answer = chat.get_answer(query)
    return render_template('advising.html', answer=answer)
  return render_template('advising.html')

@app.route('/messaging', methods=["GET","POST"])
def messaging():
  print(request.form)
  if request.method == "POST" and "query" in request.form:
    query = request.form["query"]
    answer = chat.get_answer(query)
    return render_template('messaging.html', answer=answer)
  return render_template('messaging.html')

@app.route('/register', methods=["GET","POST"])
def register():
  print(request.form)
  if request.method == "POST" and "query" in request.form:
    query = request.form["query"]
    answer = chat.get_answer(query)
    return render_template('register.html', answer=answer)
  return render_template('register.html')

@app.route('/search', methods=["GET","POST"])
def search():
  print(request.form)
  if request.method == "POST" and "query" in request.form:
    query = request.form["query"]
    answer = chat.get_answer(query)
    return render_template('search.html', answer=answer)
  return render_template('search.html')

@app.route('/records', methods=["GET","POST"])
def upload():
  print(request.files)
  if request.method == "POST" and "query" in request.form:
    query = request.form["query"]
    answer = chat.get_answer(query)
    return render_template('records.html',answer=answer)
  if request.method == "POST" and "upload" in request.files:
    print(request.form)
    file = request.files['upload']
    temp = tempfile.NamedTemporaryFile(delete=False)
    file.save(temp.name)
    store.child(temp.name).put(temp.name)
    
    return render_template('records.html')
  print("L")
  return render_template('records.html')



if __name__ == '__main__':
	app.run()
