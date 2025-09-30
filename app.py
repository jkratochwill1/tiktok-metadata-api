from flask import Flask, request, jsonify
from utils.metadata_parser import extract_metadata

app = Flask(__name__)

@app.route('/extract', methods=['POST'])
def extract():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'Missing URL'}), 400

    metadata = extract_metadata(url)
    return jsonify({'metadata': metadata})

if __name__ == '__main__':
    app.run(debug=True)