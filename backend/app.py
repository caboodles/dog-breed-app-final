from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from controllers.image_controller import handle_image_upload
import os

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'backend/uploads')

@app.route('/upload', methods=['POST'])
def upload():
    return handle_image_upload(request, app.config['UPLOAD_FOLDER'])

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
