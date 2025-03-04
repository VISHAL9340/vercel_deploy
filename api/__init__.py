from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return {"message": "Instagram Reel Downloader API Running!"}

    @app.route("/download", methods=["GET"])
    def download_reel():
        return {"message": "Download function will be implemented here"}

    return app
