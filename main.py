from flask import Flask,render_template, url_for, redirect, request
import os
app = Flask(__name__)

from google.cloud import secretmanager
from google.oauth2 import service_account

os.makedirs("secure", exist_ok=True)
os.environ["FIREBASE_CREDENTIALS"] = "secure/firebase_service_account_info.json"
try:
    secret_client = secretmanager.SecretManagerServiceClient()
    with open("secure/firebase_service_account_info.json", "w") as f:
        f.write(secret_client.access_secret_version(request={"name": "projects/774024863265/secrets/FIREBASE_SERVICE_ACCOUNT"}).payload.data.decode("UTF-8"))
except:
    pass
#inicialització db 
import firebase_admin
from firebase_admin import firestore, credentials
cred = credentials.Certificate(os.environ["FIREBASE_CREDENTIALS"])
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


