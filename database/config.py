from peewee import AutoField, CharField, IntegerField, Model, SqliteDatabase, BooleanField

db = SqliteDatabase("./database/database.db")

class Group (Model):
    id = AutoField()
    route = CharField()
    students = IntegerField(default=0)
    parents = IntegerField(default=0)
    schedule = CharField()
    isPublic = BooleanField(default=False)

    class Meta:
        database = db
