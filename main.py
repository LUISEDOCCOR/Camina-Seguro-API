from flask import Flask, jsonify
from database.config import db, Group, LocalUser
#blueprints
from routes.group import bp as bpGroup
from routes.localauth import bp as bpLocalAuth
#lib
from lib.bcrypt import hash_password
from dotenv import load_dotenv
import os
from datetime import timedelta

load_dotenv(".env.local")

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_PASSWORD")
app.permanent_session_lifetime = timedelta(minutes=5)

app.register_blueprint(bpGroup)
app.register_blueprint(bpLocalAuth)

@app.get("/")
def root ():
    return "ok"

@app.before_request
def init_database():
    db.connect()

@app.after_request
def close_database(response):
    db.close()
    return response

with db:
    db.create_tables([Group, LocalUser])
    if not LocalUser.select().where(LocalUser.username == "admin").exists():
        user = LocalUser(username="admin", password=hash_password(os.getenv("ADMIN_USER_PASSWORD")))
        user.save() 