import os

import pyrebase
from flask import *




app = Flask(__name__)
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

db = firebase.database()

@app.route('/')
def hello():
    return 'Hello, World!' 



if __name__ == '__main__':
	app.run()