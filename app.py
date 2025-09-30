import os
from flask import Flask, request, jsonify, send_file, make_response
from utils.metadata_parser import extract_metadata
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app)

@app.route('/extract', methods=['POST'])
def extract():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'Missing URL'}), 400

    metadata = extract_metadata(url)
    return jsonify({'metadata': metadata})

@app.route('/download', methods=['POST'])
def download_video():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'Missing URL'}), 400

    ydl_opts = {
        'outtmpl': 'downloads/%(id)s.%(ext)s',
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        video_id = info.get('id')
        ext = info.get('ext')

    # Return a direct link to download the video
    return jsonify({
        'download_url': f'https://{os.environ.get("RENDER_EXTERNAL_HOSTNAME")}/serve/{video_id}.{ext}'
    })

@app.route('/serve/<filename>')
def serve_video(filename):
    path = f'downloads/{filename}'
    if not os.path.exists(path):
        return jsonify({'error': 'File not found'}), 404
    return send_file(path, mimetype='video/mp4')
    
    response = make_response(send_file(path, mimetype='video/mp4'))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)