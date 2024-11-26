from flask import request
from models.user import UserModel
from lib.bcrypt import hash_password, verify_password
from flask_jwt_extended import create_access_token

class UserController:
    def __init__ (self):
        self.userModel = UserModel()

    def signup(self):
        data = request.get_json()
        if ("email" not in data or "name" not in data or "password" not in data):
            return {"msg": "Todos los campos son necesarios."}, 400

        email = data["email"]
        password = data["password"]
        name = data["name"]

        if (len(email) < 4 or len(password) < 4 or len(name) < 4):
            return {"msg": "Los datos son muy cortos, mínimo 4 caracteres"}

        if(self.userModel.getByEmail(email)):
            return {"msg": "El correo ya está registrado"}

        user = self.userModel.create(name=name, email=email, password=hash_password(password))

        if(not user):
            return {"msg": "Hubo un error al crear el usuario "}, 500

        token = create_access_token(identity=str(user["id"]))

        return {"token": token, "name": name}

    def login(self):
        data = request.get_json()
        if ("email" not in data or "password" not in data):
            return {"msg": "Todos los campos son necesarios."}, 400

        email = data["email"]
        password = data["password"]

        if (len(email) < 4 or len(password) < 4):
            return {"msg": "Los datos son muy cortos, mínimo 4 caracteres"}

        if(not self.userModel.getByEmail(email)):
            return {"msg": "El correo no está registrado"}

        user = self.userModel.getDataByEmail(email)

        print(user)

        if(not verify_password(userPassword=password, password=user.password)):
            return {"msg": "La contraseña es incorrecta."}

        token = create_access_token(identity=str(user.id))

        return {"token": token, "name": user.name}


        return {}
