import os

from flask import Flask, send_file, request, jsonify
from config import UPLOAD_FOLDER

app = Flask(__name__)

@app.route("/health-check")
def hello_world():
    return "<p>server is running</p>"

@app.route("/login", methods=['POST']) # wiht  {username: "user", password: "password"}
def login():
    return "<p>login</p>"

@app.route("/<int:family_id>/time-capsule/<int:time_capsule_id>") # with {Authorization: "Bearer token"}
def time_capsule(family_id, time_capsule_id):
    return "<p>time capsule</p>"

@app.route("/<int:family_id>/time-capsules") # with {Authorization: "Bearer token"}
def time_capsules(family_id):
    return "<p>time capsules</p>"

@app.route("/time-capsule/<int:time_capsule_id>") # with {Authorization: "Bearer token"}
def time_capsule(time_capsule_id):
    return "<p>time capsule</p>"

@app.route('/images/<path:image_name>')
def get_image(image_name):
    try:
        return send_file(os.path.join(UPLOAD_FOLDER, image_name))
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    
@app.route('/upload', methods=['POST'])
def upload_image():
    # POST /upload {image: file}
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({"error": "No selected file"}), 400

    image.save(os.path.join(UPLOAD_FOLDER, image.filename))
    return jsonify({"message": "Image uploaded successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=3000)
