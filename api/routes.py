from flask import Blueprint, request, jsonify
import yt_dlp
import os

download_bp = Blueprint("download", __name__)

DOWNLOAD_FOLDER = "downloads"

@download_bp.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Instagram Reel Downloader API Running!"})

@download_bp.route("/download", methods=["POST"])
def download():
    try:
        data = request.json
        url = data.get("url")

        if not url:
            return jsonify({"error": "URL is required"}), 400

        ydl_opts = {
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return jsonify({"message": "Download Successful!", "file": "Check downloads folder"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

