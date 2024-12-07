from database.config import Group

class GroupModel:
    def __init__(self):
        self.group = Group

    def getAll(self):
        try:
            return  [record for record in self.group.select().dicts()]
        except:
            return []

    def getAllPublic(self):
        try:
            return  [record for record in self.group.select().where(self.group.isPublic == True).dicts()]
        except:
           return []

    def getByUserId(self, user_id):
        try:
            return  [record for record in self.group.select().where(self.group.user == user_id).dicts()]
        except:
           return []

    def create(self, route, schedule, user):
        try:
            data = self.group(route=route, schedule=schedule, user=user)
            data.save()
            dataDict = data.__data__
            return dataDict
        except:
            return False

    def getDataById(self, group_id):
        group = self.group.get(self.group.id == group_id)
        return group

    def getById(self, group_id):
        return self.group.select().where(self.group.id == group_id).exists()

    def addPerson(self, group_id, role):
        data = self.getDataById(group_id)
        if role == "student":
            newStudentsCount = data.students + 1
            query = self.group.update(students=newStudentsCount).where(self.group.id == group_id)
        else:
            newParentsCount = data.parents + 1
            query = self.group.update(parents=newParentsCount).where(self.group.id == group_id)
        query.execute()

    def changeVisibility (self, id):
        data = self.getDataById(id)
        query = self.group.update(isPublic=(not data.isPublic)).where(self.group.id == id)
        query.execute()

    def delete (self, id):
        query = self.group.delete().where(self.group.id == id)
        query.execute()
