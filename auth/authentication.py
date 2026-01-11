from flask import Blueprint, jsonify, request

from closet_db.closet_db import get_closet_db
from closet_db.queries import register_user, verify_login_creds

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/register', methods=["POST"])
def register():
    if request.is_json:
        try:
            user_data = request.get_json()
            # Entry of the data needs to be made to the DB
            username,password = user_data["Records"][0]["username"],user_data["Records"][0]["password"] 
            db = get_closet_db()
            error = register_user(db,username,password)

            if error:
                return jsonify({"status_code":"409", "message":f"{error}"})
            return jsonify({"status_code":"201", "message":f"User '{username}' created successfully!"})
        except Exception as exc:
            return jsonify({"status_code":"500", "message":f"Error encountered : {exc}"})
        
    return jsonify({"status_code":"400", "message":"Data sent in not JSON. Try again!"})

@auth.route('/login', methods=["POST"])
def login():
    if request.is_json:
        try:
            user_data = request.get_json()
            # Entry of the data needs to be made to the DB
            username,password = user_data["Records"][0]["username"],user_data["Records"][0]["password"] 
            db = get_closet_db()
            error = verify_login_creds(db,username,password)

            if error:
                return jsonify({"status_code":"400", "message":f"{error}"})
            return jsonify({"status_code":"201", "message":f"Successfully logged-in as '{username}'"})
        except Exception as exc:
            return jsonify({"status_code":"500", "message":f"Error encountered : {exc}"})
        
    return jsonify({"status_code":"400", "message":"Data sent in not JSON. Try again!"})