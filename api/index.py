import json
from flask import Flask, render_template, request, jsonify
from pytube import YouTube

app = Flask(__name__)

# Load API keys from apis.json
with open('data.json') as f:
    api_keys = json.load(f)['api_keys']

@app.route("/api/video-info", methods=["GET"])
def get_video_info():
    video_id = request.headers.get("VIDEO_ID")
    api_key = request.headers.get("API_KEY")

    # Validate the API key
    if api_key not in api_keys:
        return jsonify({"error": "Invalid API Key"}), 401
    
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
