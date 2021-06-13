from flask import Blueprint, request
from api.users_api import UsersApi

bp = Blueprint(
    "users", __name__, url_prefix="/users"
)


@bp.route("/signup", methods=["POST"])
def signup():
    return UsersApi(request).signup()



@bp.route("/signout", methods=["GET"])
def signout():
    return UsersApi(request).signout()



@bp.route("/login", methods=["POST"])
def login():
    return UsersApi(request).login()



@bp.route("/save_user", methods=["POST"])
def save_user():
    return UsersApi(request).save_user()


@bp.route("/get_users", methods=["GET"])
def get_users():
    return UsersApi(request).get_users()





