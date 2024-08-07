# -*- coding: utf-8 -*-
"""monofaced.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d_24zucdq40XcOdl60u5-GnINQzSmPgX
"""

!pip install deepface

from deepface import DeepFace
import os

import cv2

# Path to the folder containing the monofaced images
folder_path = '/content/sample_data/train_data'

# List all subfolders (each corresponding to a person)
person_folders = os.listdir(folder_path)

# Iterate through each person's folder
for person_folder in person_folders:
    image_folder_path = os.path.join(folder_path, person_folder)
    # List all image files in the person's folder
    image_files = os.listdir(image_folder_path)

    # Iterate through each image file
    for image_file in image_files:
        image_path = os.path.join(image_folder_path, image_file)

        # Use DeepFace for face detection
        detected_faces = DeepFace.detectFace(image_path)

        # Process detected_faces as needed (e.g., save or display results)
        print(f"Detected {len(detected_faces)} face(s) in {image_file}")

import os
import cv2
from deepface import DeepFace
from google.colab.patches import cv2_imshow  # Import cv2_imshow for Colab

# Path to the folder containing the monofaced images
folder_path = '/content/sample_data/train_data'

# List all subfolders (each corresponding to a person)
person_folders = os.listdir(folder_path)

# Iterate through each person's folder
for person_folder in person_folders:
    image_folder_path = os.path.join(folder_path, person_folder)

    # List all image files in the person's folder
    image_files = os.listdir(image_folder_path)

    # Iterate through each image file
    for image_file in image_files:
        image_path = os.path.join(image_folder_path, image_file)

        try:
            # Check if the path is a file and ends with an image extension
            if os.path.isfile(image_path) and any(image_path.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']):
                # Load the image using OpenCV
                img = cv2.imread(image_path)

                if img is not None:
                    # Convert image to grayscale for face detection (optional)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                    # Perform face detection using OpenCV's Haar cascades or deep learning-based models
                    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                    detected_faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

                    if len(detected_faces) > 0:
                        print(f"Detected {len(detected_faces)} face(s) in {image_file}")

                        # Process detected_faces as needed (e.g., draw bounding boxes)
                        for (x, y, w, h) in detected_faces:
                            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

                        # Display the image with bounding boxes using cv2_imshow for Colab
                        cv2_imshow(img)
                    else:
                        print(f"No faces detected in {image_file}")
                else:
                    print(f"Error loading image: {image_file}")
            else:
                print(f"Skipping non-image file: {image_file}")

        except Exception as e:
            print(f"Error processing {image_file}: {str(e)}")

import os
import cv2
from deepface import DeepFace
from google.colab.patches import cv2_imshow  # Import cv2_imshow for Colab

# Path to the folder containing the training data
train_folder_path = '/content/sample_data/train_data'

# Path to the folder containing the testing data
test_folder_path = '/content/sample_data/test_data'

# List of persons (each corresponding to a subfolder in train_folder_path)
persons = os.listdir(train_folder_path)

# Load known face embeddings or models for recognition (example)
# Replace with your own logic or database for face recognition
known_faces = {
    'P1': 'path_to_embedding_or_model_for_P1',
    'P2': 'path_to_embedding_or_model_for_P2',
    'P3': 'path_to_embedding_or_model_for_P3',
    'P4': 'path_to_embedding_or_model_for_P4',
    'P5': 'path_to_embedding_or_model_for_P5',
    # Add more as needed
}

# Function to perform face detection and recognition
def detect_and_recognize_faces(image_path):
    try:
        # Use DeepFace to detect faces in the image
        detected_faces = DeepFace.detectFace(image_path, enforce_detection=False)

        if len(detected_faces) > 0:
            print(f"Detected {len(detected_faces)} face(s) in {image_path}")

            # Process each detected face for recognition
            for face in detected_faces:
                # Perform face recognition using DeepFace
                result = DeepFace.find(img_path = image_path, db_path = train_folder_path, enforce_detection=False)

                # Example of result
                print(f"Recognized person: {result}")

                # Draw bounding box around the face
                (x, y, w, h) = face['box']
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Display the image with bounding boxes using cv2_imshow for Colab
            cv2_imshow(img)
        else:
            print(f"No faces detected in {image_path}")

    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")

# Process training data (persons)
for person in persons:
    person_folder_path = os.path.join(train_folder_path, person)
    if os.path.isdir(person_folder_path):
        images = os.listdir(person_folder_path)
        for image in images:
            image_path = os.path.join(person_folder_path, image)
            detect_and_recognize_faces(image_path)

# Process testing data (groups and monofaced)
test_groups_folder = os.path.join(test_folder_path, 'group')
if os.path.isdir(test_groups_folder):
    test_groups_images = os.listdir(test_groups_folder)
    for image in test_groups_images:
        image_path = os.path.join(test_groups_folder, image)
        detect_and_recognize_faces(image_path)

test_monofaced_folder = os.path.join(test_folder_path, 'monofaced')
if os.path.isdir(test_monofaced_folder):
    test_monofaced_images = os.listdir(test_monofaced_folder)
    for image in test_monofaced_images:
        image_path = os.path.join(test_monofaced_folder, image)
        detect_and_recognize_faces(image_path)

import os
import cv2
from deepface import DeepFace
from google.colab.patches import cv2_imshow  # Import cv2_imshow for Colab

# Path to the folder containing the monofaced images
monofaced_folder_path = '/content/sample_data/test_data/monofaced'

# Load known face embeddings or models for recognition (example)
# Replace with your own logic or database for face recognition
known_faces = {
    'P1': 'path_to_embedding_or_model_for_P1',
    'P2': 'path_to_embedding_or_model_for_P2',
    'P3': 'path_to_embedding_or_model_for_P3',
    'P4': 'path_to_embedding_or_model_for_P4',
    'P5': 'path_to_embedding_or_model_for_P5',
    # Add more as needed
}

# Function to detect and recognize faces in monofaced images
def detect_and_recognize_monofaced(image_path):
    try:
        # Use DeepFace to detect faces in the image
        detected_faces = DeepFace.detectFace(image_path, enforce_detection=True)

        if len(detected_faces) == 1:
            print(f"Detected 1 face in {image_path}")

            # Perform face analysis using DeepFace
            analyzed_info = DeepFace.analyze(image_path, actions=['emotion', 'age', 'gender', 'race'])

            # Extract the dominant emotion from analyzed_info
            dominant_emotion = analyzed_info['dominant_emotion']

            # Example of recognized information
            print(f"Analyzed information: {analyzed_info}")

            # Display the image with bounding box and recognized information
            img = cv2.imread(image_path)
            (x, y, w, h) = detected_faces[0]['box']
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(img, f"Age: {analyzed_info['age']}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
            cv2.putText(img, f"Gender: {analyzed_info['gender']}", (x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
            cv2.putText(img, f"Dominant Emotion: {dominant_emotion}", (x, y+50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
            cv2_imshow(img)

        elif len(detected_faces) > 1:
            print(f"Detected {len(detected_faces)} faces in {image_path}. Skipping because it's a multifaced image.")

        else:
            print(f"No faces detected in {image_path}")

    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")

# Process monofaced images
if os.path.isdir(monofaced_folder_path):
    monofaced_images = os.listdir(monofaced_folder_path)
    for image in monofaced_images:
        image_path = os.path.join(monofaced_folder_path, image)
        detect_and_recognize_monofaced(image_path)