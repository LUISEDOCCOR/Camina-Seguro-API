from peewee import AutoField, CharField, IntegerField, Model, SqliteDatabase, BooleanField, ForeignKeyField

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
