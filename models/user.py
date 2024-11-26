from database.config import User

class UserModel:
    def __init__(self):
        self.user = User

    def getByEmail(self, email):
        return self.user.select().where(self.user.email == email).exists()

    def create(self, name, email, password):
        try:
            data = self.user(name=name, email=email, password=password)
            data.save()
            return data.__data__
        except:
            return False

    def getDataByEmail(self, email):
        user = self.user.get(self.user.email == email)
        return user
