from flask import Flask, render_template, url_for, flash, get_flashed_messages, request
from .config.variables import SECRET_KEY

def create_app():
    app = Flask(__name__)


    #CONFIGS
    app.config["SECRET_KEY"] = SECRET_KEY


    # BLUEPRINTS
    from .views.admin_auth import admin
    app.register_blueprint(admin, url_prefix="/owner")


    @app.errorhandler(404)
    def errorhandler(error):
        return render_template("admin/error-404.html")
    
    @app.errorhandler(Exception)
    def errorhandler(error):
        print("500 ERROR", str(error))
        return render_template("admin/error-500.html")

    return app