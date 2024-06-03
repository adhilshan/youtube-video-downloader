# YouTube Video Downloader API
##Description
This API allows you to download YouTube videos in various formats and qualities. It provides a simple and efficient way to retrieve video metadata and download videos.

## Features
- Download YouTube videos in MP4, WebM, and other formats
- Choose from various video qualities, including 1080p, 720p, 480p, and more
- Retrieve video metadata, including title, views, and thumbnail URL
- Supports audio-only downloads
## API Endpoints
GET /api/video-info
- Retrieve video metadata and download links
Parameters:
- package-name: com.example.myapp (required)
- video-id: YouTube video ID (required)
Response:
- Video metadata (title, views, thumbnail URL)
- Array of download links with format, quality, and file size information
Example Response

```json
{
  "title": "Never Gonna Give You Up",
  "views": 1540966843,
  "thumbnail_url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/hq720.jpg?sqp=-oaymwEXCNUGEOADIAQqCwjVARCqCBh4INgESFo&rs=AOn4CLBX-HcaMSEAucUr5J0qD5nEyiPAoQ",
  "downloads": [
    {
      "file_size": 5680516,
      "quality": "1080p",
      "url": "https://rr3---sn-ab5sznly.googlevideo.com/videoplayback?expire=1717438970&ei=mrVdZpLiOK6ykucPn4OXuAg&ip=3.236.93.234&id=o-ALRfAmUibhHDG9QK2uEeAdJm-Fbqg1vusIPcrffMFcqN&itag=248&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=7c&mm=31%2C26&mn=sn-ab5sznly%2Csn-t0a7sn7d&ms=au%2Conr&mv=m&mvi=3&pl=22&initcwndbps=2188750&vprv=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=5680516&dur=212.040&lmt=1717051809076575&mt=1717417002&fvip=1&keepalive=yes&c=ANDROID_MUSIC&txp=4535434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRgIhANJaFf6i1oiJ4fiXxudlTafBcriJoKcVSe9Imd6gpwNIAiEAnPY38wG9j4S-0hD5vNIVqYIx2ezr9H9Nlf-5MCflmp4%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHlkHjAwRQIhAMI-nvSjU7goKCf2CmQDa0MvII-iQPqiDmxkMqCwfqaQAiAq9DhMpyryHjpA5it6c6A_bvKlEvLdtLkgNEsHWJ17jQ%3D%3D"
    },
   ...
  ]
}
```
## Make your demo GET request to
http://barcode-ytdownloader.vercel.app/api/video-info
### Params
Header Name : package-name <br>
Header Value : com.example.myapp<br>

Header Name : video-id <br>
Header Value : dQw4w9WgXcQ <br>

## Deploy To Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fflask3&demo-title=Flask%203%20%2B%20Vercel&demo-description=Use%20Flask%203%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fflask3-python-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)

# Flask + Vercel

This example shows how to use Flask 3 on Vercel with Serverless Functions using the [Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python).

## Demo

https://flask-python-template.vercel.app/

## How it Works

This example uses the Web Server Gateway Interface (WSGI) with Flask to enable handling requests on Vercel with Serverless Functions.

## Running Locally

```bash
npm i -g vercel
vercel dev
```

Your Flask application is now available at `http://localhost:3000`.

## One-Click Deploy

Deploy the example using [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fflask3&demo-title=Flask%203%20%2B%20Vercel&demo-description=Use%20Flask%203%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fflask3-python-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)
