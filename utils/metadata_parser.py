import yt_dlp

def extract_metadata(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return {
        'title': info.get('title', 'No title'),
        'author': info.get('uploader', 'No author'),
        'hashtags': ', '.join(info.get('tags', [])) if info.get('tags') else 'No hashtags',
        'video_id': info.get('id', 'No video ID'),
        'video_path': info.get('url', 'No video path')
    }