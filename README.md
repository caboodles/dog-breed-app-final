# Dog Breed Identifier

This project allows users to upload an image of a dog, and it identifies the breed using an AI model.

## Setup

1. Clone the repository.
2. Set up a Python virtual environment.
3. Install the dependencies:
    - pip install -r backend/requirements.txt
4. Start the MongoDB server.
    - MONGO_URI=mongodb://localhost:27017/dog_breed_db
5. Seed the database:
    - python database/seed/seed_data.py
6. Run the Flask application:
    - python backend/app.py


## Usage

- Open `frontend/index.html` to start the application.
- Upload a dog image through `frontend/upload.html` to identify the breed.
