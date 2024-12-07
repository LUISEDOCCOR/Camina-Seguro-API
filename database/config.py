from peewee import AutoField, CharField, IntegerField, Model, SqliteDatabase, BooleanField, ForeignKeyField, PostgresqlDatabase
from dotenv import load_dotenv
import os

load_dotenv(".env.local")

if(os.getenv("environment") == "production"):
    DB_NAME = os.getenv('DB_NAME')
    USER = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASSWORD')
    HOST = os.getenv('DB_HOST')
    PORT = os.getenv('DB_PORT')
    db = PostgresqlDatabase(
        DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
else:
    db = SqliteDatabase("./database/database.db")

class User (Model):
    id = AutoField()
    password = CharField()
    email = CharField(unique=True)

    class Meta:
        database = db

class Group (Model):
    id = AutoField()
    route = CharField()
    students = IntegerField(default=0)
    parents = IntegerField(default=0)
    schedule = CharField()
    isPublic = BooleanField(default=False)
    user =  ForeignKeyField(User, backref="groups")

    class Meta:
        database = db

class LocalUser (Model):
    id = AutoField()
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db
