from database.config import LocalUser
class LocalUserModel:
    def __init__(self) -> None:
        self.localuser = LocalUser

    def getByUsername (self, username):
        try:
            user = self.localuser.get(self.localuser.username == username)
            return user
        except:
            return False
