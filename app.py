import os
from flask import Flask, request, jsonify
from utils.metadata_parser import extract_metadata
from flask_cors import CORS

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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)