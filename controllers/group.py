from flask import jsonify, request

from models.group import GroupModel

class GroupController:
    def __init__(self):
        self.groupModel = GroupModel()

    def getAll (self):
        groups = self.groupModel.getAll()
        return jsonify(groups)

    def create (self):
        data = request.get_json()
        if  "route" not in data or "schedule" not in data:
             return {"msg": "All fields are required"}, 400

        group = self.groupModel.create(data["route"], data["schedule"])
        if group:
            return jsonify({"msg": "Created successfully", "group": group})
        else:
            return {"msg": "Something happened when creating it"}, 500

    def addPerson (self, id,role):
        roles = ["student", "parent"]
        if not role in roles:
            return {"msg": "Invalid Role"}, 400
        isDone = self.groupModel.addPerson(id, role)
        if not isDone:
            return {"msg": f"Error adding {role} role"}, 400

        return jsonify({"msg": f"has been successfully completed with the role of {role}"})
