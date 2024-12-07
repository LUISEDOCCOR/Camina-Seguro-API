from flask import Flask
from flask_cors import CORS
from database.config import db, Group, LocalUser, User
from dotenv import load_dotenv
import os
from datetime import timedelta
#blueprints
from routes.group import bp as bpGroup
from routes.localauth import bp as bpLocalAuth
from routes.user import bp as bpUser
#lib
from lib.bcrypt import hash_password
#jwt
from flask_jwt_extended import JWTManager

load_dotenv(".env.local")

app = Flask(__name__)
CORS(app)
JWTManager(app)

app.secret_key = os.getenv("FLASK_PASSWORD")
app.permanent_session_lifetime = timedelta(minutes=5)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)

app.register_blueprint(bpGroup)
app.register_blueprint(bpLocalAuth)
app.register_blueprint(bpUser)

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
    db.create_tables([Group, LocalUser, User])
    if not LocalUser.select().where(LocalUser.username == "admin").exists():
        user = LocalUser(username="admin", password=hash_password(os.getenv("ADMIN_USER_PASSWORD")))
        user.save()
