import os

from flask import Flask,render_template
from .route import authCustom,authStd
from .model import db,UserRestCrt


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)
    
    #Load all information for keycloak
    #app.config.from_envvar('KEYCLOAK_FLASK_SETTINGS')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    #load DB
    db.init_app(app)

    app.register_blueprint(authStd.bp)
    app.register_blueprint(authCustom.bp)
    #app.register_blueprint(authKeyCloak.bp)
    app.register_blueprint(UserRestCrt.bp)
    

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.before_request
    def dfn_crypto_content():
        authCustom.init_cryto_content()

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/')
    def start():
        return render_template('auth/login.html')
    return app

# if __name__ == "__main__":
#     create_app()
