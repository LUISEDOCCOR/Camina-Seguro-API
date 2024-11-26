from flask import jsonify, request, render_template, redirect, url_for, flash
from models.group import GroupModel
from flask_jwt_extended import get_jwt_identity

class GroupController:
    def __init__(self):
        self.groupModel = GroupModel()

    def getAll (self):
        groups = self.groupModel.getAllPublic()
        return jsonify(groups)

    def create (self):
        data = request.get_json()
        if  "route" not in data or "schedule" not in data:
             return {"msg": "Todos los campos son necesarios."}, 400

        route = data["route"]
        schedule = data["schedule"]

        if len(route) < 5 or len(schedule) < 5:
            return {"msg": "No se permiten datos tan cortos."}, 400

        user_id = get_jwt_identity()

        group = self.groupModel.create(route=route, schedule=schedule, user_id=user_id)

        if not group:
            return {"msg": "Algo paso al crearlo."}, 500

        return jsonify({"msg": "Fue creado exitosamente, y ahora sera aprobado.", "group": group})

    def addPerson (self, id, role):
        roles = ["student", "parent"]

        if not role in roles:
            return {"msg": "Rol invalido."}, 400

        if(not self.groupModel.getById(id)):
            return {"msg": "No existe ese grupo"}

        self.groupModel.addPerson(id, role)

        return {"msg": "Se ha agregado correctamente el rol"}

    def dashboard(self):
        groups = self.groupModel.getAll()
        return render_template("index.html", groups=groups)

    def changeVisibility (self, id):
        if(not self.groupModel.getById(id)):
            flash("No existe ese grupo")
        else:
            self.groupModel.changeVisibility(id)

        return redirect(url_for("group.dashboard"))

    def delete (self, id):
        if(not self.groupModel.getById(id)):
            flash("No existe ese grupo")
        else:
            self.groupModel.delete(id)

        return redirect(url_for("group.dashboard"))
