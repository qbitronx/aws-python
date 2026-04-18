from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')

    from app.controllers.developer_controller import developer_bp
    app.register_blueprint(developer_bp)

    return app
