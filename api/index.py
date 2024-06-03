from flask import Flask, request, jsonify
from pytube import YouTube

app = Flask(__name__)

PACKAGE_NAME = "com.example.myapp"

@app.route("/api/video-info", methods=["GET"])
def get_video_info():
    package_name = request.headers.get("package-name")
    video_id = request.headers.get("video-id")
    if package_name!= PACKAGE_NAME:
        return jsonify({"error": "Unauthorized Access"}), 401
    else:
        downloadUrls = []
        video_url = "https://www.youtube.com/watch?v=" + video_id
        yt = YouTube(video_url)
        
        streams = yt.streams

        for stream in streams:
            JSONObj = {
                "quality" : stream.resolution,
                "file-size" : stream.filesize,
                "url" : stream.url
            }
            downloadUrls.append(JSONObj)

        video_info = {
            "title": yt.title,
            "author": yt.author,
            "description": yt.description,
            "views": yt.views,
            "length": yt.length,
            "thumbnail_url": yt.thumbnail_url,
            "streams": downloadUrls
        }

    return jsonify(video_info)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
