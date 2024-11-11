from flask import Blueprint
from controllers.group import GroupController

bp = Blueprint("group", __name__, url_prefix="/group")

groupController = GroupController()

@bp.get("/")
def getAll ():
    return groupController.getAll()

@bp.post("/")
def create ():
    return groupController.create()


@bp.get("/add/<int:id>/<role>")
def addPerson (id,role):
    return groupController.addPerson(id, role)
