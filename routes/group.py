from flask import Blueprint, render_template
from controllers.group import GroupController

bp = Blueprint("group", __name__, url_prefix="/group")

groupController = GroupController()

@bp.get("/")
def getAll ():
    return groupController.getAll()

@bp.post("/")
def create ():
    return groupController.create()

@bp.get("/dashboard")
def dashboard():
    return groupController.dashboard()

@bp.get("/add/<int:id>/<role>")
def addPerson (id,role):
    return groupController.addPerson(id, role)

@bp.get("/changevisibility/<int:id>")
def changeVisibility(id):
    return groupController.changeVisibility(id)

@bp.get("/delete/<int:id>")
def delete(id):
    return groupController.delete(id)
