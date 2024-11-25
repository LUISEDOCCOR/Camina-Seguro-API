from flask import Flask, jsonify
from database.config import db, Group
#blueprints
from routes.group import bp as bpGroup

app = Flask(__name__)
app.secret_key = "1234"

app.register_blueprint(bpGroup)

@app.get("/")
def root ():
    return jsonify({"msg": "Is Live"})

@app.before_request
def init_database():
    db.connect()

@app.after_request
def close_database(response):
    db.close()
    return response

with db:
    db.create_tables([Group])
