import os
from flask import Flask

def create_app():
    app = Flask("the-closet", instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'closet-users-db.sqlite'),
    )
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from .routes import bp
    app.register_blueprint(bp)

    from closet_db import closet_db
    closet_db.init_app(app)
    
    return app