from flask import Flask, render_template, request, redirect, url_for
import os
import shutil
import numpy as np
from PIL import Image
import cv2
import threading
import time

app = Flask(__name__)

UPLOAD_FOLDER = 'input'
WORKING_DIRECTORY = 'working_directory'
ALLOWED_EXTENSIONS = {'png'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['WORKING_DIRECTORY'] = WORKING_DIRECTORY

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def clear_input_folder():
    folder = app.config['UPLOAD_FOLDER']
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

def copy_and_rename_image():
    input_folder = app.config['UPLOAD_FOLDER']
    working_folder = app.config['WORKING_DIRECTORY']
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            source_path = os.path.join(input_folder, filename)
            destination_path = os.path.join(working_folder, 'main.png')
            try:
                shutil.copy(source_path, destination_path)
                print(f"Image copied and renamed successfully to {destination_path}")
            except Exception as e:
                print(f"Failed to copy and rename image. Reason: {e}")

# Function to import pipeline from transformers after a delay
def import_pipeline_with_delay():
    global pipe
    # Wait for 10 seconds
    time.sleep(10)
    # Import pipeline from transformers
    from transformers import pipeline
    # Initialize depth estimation pipeline
    pipe = pipeline(task="depth-estimation", model="Intel/dpt-large")

# Start the function in a separate thread to avoid blocking the main thread
threading.Thread(target=import_pipeline_with_delay).start()

focus_option = None  # Initialize the focus option variable

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    clear_input_folder()  # Clear the input folder before uploading a new file
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Copy and rename the PNG image to the working directory
        copy_and_rename_image()
        return "File uploaded successfully"  # Return a success message
    return "Upload failed"  # Return an error message if file upload fails

@app.route('/update_focus', methods=['POST'])
def update_focus():
    global focus_option  # Access the global variable
    focus_option = request.form.get('focus_option')
    return "Focus option updated successfully: {}".format(focus_option)

if __name__ == '__main__':
    app.run(debug=True)
