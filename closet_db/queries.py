from werkzeug.security import generate_password_hash, check_password_hash

def register_user(db_instance, username, password):
    error = None
    try:
        db_instance.execute(
            "INSERT INTO user (username, password) VALUES (?, ?)",
            (username, generate_password_hash(password)),
        )
        db_instance.commit()
    except db_instance.IntegrityError:
        error = f"User '{username}' already exists. Try again!"
    return error

def verify_login_creds(db_instance, username, password):
    error = None
    user = db_instance.execute(
        "SELECT * FROM user WHERE username=?", (username,)
    ).fetchone()
    
    if user is None:
        error=f"User '{username}' doesn't exist!"
    elif not check_password_hash(user['password'], password):
        error="Incorrect password!"
    
    return error