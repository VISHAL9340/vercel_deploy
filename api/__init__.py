from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    
    # Create downloads folder if not exists
    os.makedirs("downloads", exist_ok=True)

    # Import routes
    from api.routes import download_bp
    app.register_blueprint(download_bp)

    return app

