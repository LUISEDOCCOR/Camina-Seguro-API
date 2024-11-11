from peewee import AutoField, CharField, IntegerField, Model, SqliteDatabase

db = SqliteDatabase("./database/database.db")

class Group (Model):
    id = AutoField()
    route = CharField()
    students = IntegerField(default=0)
    parents = IntegerField(default=0)
    schedule = CharField()

    class Meta:
        database = db
