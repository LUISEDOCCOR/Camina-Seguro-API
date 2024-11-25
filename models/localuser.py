from database.config import LocalUser
class LocalUserModel:
    def __init__(self) -> None:
        self.user = LocalUser 
    
    def getByUsername (self, username):
        try:
            user = self.user.get(self.user.username == username)
            return user 
        except:
            return False