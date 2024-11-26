from flask import render_template, request, flash, redirect, url_for, session
#models
from models.localuser import LocalUserModel
#lib
from lib.bcrypt import verify_password

class LocalAuthController:
    def __init__(self):
        self.userModel = LocalUserModel()

    def login (self):
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")

            if (len(username) < 4 or len(password) < 4):
                flash("Todos los campos son necesarios.")
            else:
                user = self.userModel.getByUsername(username)
                if(not user):
                    flash("El usuario no existe")
                else:
                    if not verify_password(password, user.password):
                        flash("Contraseña incorrecta")
                    else:
                        session["id"] = user.id
                        session["username"] = user.username
                        return redirect(url_for("group.dashboard"))

        return render_template("auth.html")
