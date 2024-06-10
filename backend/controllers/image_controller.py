import os
from werkzeug.utils import secure_filename
from flask import jsonify
from services.ai_model_service import predict_breed
from models.breed import Breed

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def handle_image_upload(request, upload_folder):
    if 'file' not in request.files:
        return jsonify(error="No file part"), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify(error="No selected file"), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)
        
        # Get the breed prediction from the AI model
        breed_name = predict_breed(filepath)
        
        # Retrieve breed information from the database
        breed_info = Breed.get_breed_info(breed_name)
        if breed_info:
            return jsonify(
                breed=breed_info.get("name", breed_name),
                info=breed_info.get("info", "No additional information available.")
            )
        else:
            return jsonify(
                breed=breed_name,
                info="Breed information not found in the database."
            )
    else:
        return jsonify(error="Invalid file type"), 400
