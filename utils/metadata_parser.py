import yt_dlp
import logging

def extract_metadata(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        logging.info(info)  # View this in CloudWatch or Render logs

        return {
            'title': info.get('title', 'No title'),
            'uploader': info.get('uploader', 'No uploader'),
            'description': info.get('description', 'No description'),
            'hashtags': [tag for tag in info.get('tags', []) if tag.startswith('#')],
            'video_path': info.get('url', 'No video path')
        }