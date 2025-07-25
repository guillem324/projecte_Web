from flask import Flask,render_template, url_for, redirect, request
import os
app = Flask(__name__)




#inicialització db 
import firebase_admin
from firebase_admin import firestore, credentials
try:
    cred = credentials.Certificate('secure/proyecto1-56aab-198e37058f99.json')
except:
    cred = credentials.Certificate(os.environ["FIREBASE_SERVICE_ACCOUNT"])
# Application Default credentials are automatically created.
firebase_app = firebase_admin.initialize_app(cred)
db = firestore.client()













@app.route("/")
def hello_world():
    return render_template("index.html")

@app.post("/login")
def login():
    print(request)
    client_username = request.args.get('username')
    client_password = request.args.get('password')

    llista_usuaris = db.collection("users").stream()

    for usuari in llista_usuaris:
        print(usuari)
        print(usuari.id)
        dades_usuari= usuari.to_dict()
        print(dades_usuari)
        if client_username == dades_usuari['username'] and client_password == dades_usuari['password']:
            return "", 200
    return "", 400 
@app.route("/contingut")
def contingut ():
    return render_template("contingut.html")


