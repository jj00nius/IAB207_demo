from flask import Flask
from flask_bootstrap import Bootstrap4

def create_app():
    app = Flask(__name__)

    # Utility module used to display forms quickly
    Bootstrap4(app)

    # Secret key for the session object
    app.config.update(dict(
        SECRET_KEY="shaegill",
        WTF_CSRF_SECRET_KEY="a csrf secret key"
    ))

    # Add blueprints
    from . import views
    app.register_blueprint(views.mainbp)

    return app