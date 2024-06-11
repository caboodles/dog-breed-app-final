# Dog Breed Identifier

This project allows users to upload an image of a dog, and it identifies the breed using an AI model.

## Setup

### You must use python version : 3.10.5

1. Clone the repository.
2. Add "model.h5" file to dog-breed-app-final(root directory)
3. Set up a Python virtual environment.
4. Install the dependencies:
    - pip install -r backend/requirements.txt
5. Start the MongoDB server.
    - MONGO_URI=mongodb://localhost:27017/dog_breed_db
6. Seed the database:
    - python database/seed/seed_data.py
7. Run the Flask application:
    - python backend/app.py


## Usage

- Upload a dog image through `frontend/upload.html` to identify the breed.
