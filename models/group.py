from database.config import Group

class GroupModel:
    def __init__(self):
        self.group = Group

    def getAll(self):
        try:
            return  [record for record in self.group.select().dicts()]
        except:
           return []

    def create(self, route, schedule):
        try:
            data = self.group(route=route, schedule=schedule)
            data.save()
            dataDict = data.__data__
            return dataDict
        except:
            return False

    def getById(self, group_id):
        try:
            group = self.group.get(self.group.id == group_id)
            return group
        except:
            return False

    def addPerson(self, group_id, role):
        try:
            data = self.getById(group_id)
            if not data:
                return False
            if role == "student":
                newStudentsCount = data.students + 1
                query = self.group.update(students=newStudentsCount).where(self.group.id == group_id)
            else:
                newParentsCount = data.parents + 1
                query = self.group.update(parents=newParentsCount).where(self.group.id == group_id)
            query.execute()
            return True
        except:
            return False

    def changeVisibility (self, id):
        try:
            data = self.getById(id)
            if not data:
                return False
            query = self.group.update(isPublic=(not data.isPublic)).where(self.group.id == id)
            query.execute()
        except:
            return False

