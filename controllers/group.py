from flask import jsonify, request, render_template, flash, redirect, url_for
from models.group import GroupModel

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

        if len(data["route"]) < 5 or len(data["schedule"]) < 5:
            return {"msg": "No se permiten datos tan cortos."}, 400

        group = self.groupModel.create(data["route"], data["schedule"])
        if group:
            return jsonify({"msg": "Fue creado exitosamente, y ahora sera aprobado.", "group": group})
        else:
            return {"msg": "Algo paso al crearlo."}, 500

    def addPerson (self, id,role):
        roles = ["student", "parent"]
        if not role in roles:
            return {"msg": "Rol invalido."}, 400
        isDone = self.groupModel.addPerson(id, role)
        if not isDone:
            return {"msg": f"Error al añadir el rol de {role}."}, 400

        return jsonify({"msg": f"Se ha agregado correctamente el rol de {role}."})

    def dashboard(self):
        groups = self.groupModel.getAll()
        return render_template("index.html", groups=groups)

    def changeVisibility (self, id):
        self.groupModel.changeVisibility(id)
        return redirect(url_for("group.dashboard"))

    def delete (self, id):
        self.groupModel.delete(id)
        return redirect(url_for("group.dashboard"))