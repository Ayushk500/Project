import os
import cv2
import numpy as np
from deepface import DeepFace
import psycopg2
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import io


def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="x",
            user="x",
            password="x",
            host="127.0.0.1",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None



def extract_datetime_from_filename(filename):
    try:
        datetime_str = filename.split('.')[0]  # Assuming filename format is yyyymmdd_hhmm.ext
        date_time = datetime.strptime(datetime_str, "%Y%m%d_%H%M")
        return date_time
    except Exception as e:
        print(f"Error extracting datetime from filename: {e}")
        return None


def get_subject_id(date_time):
    hour = date_time.hour
    if 10 <= hour < 11:
        return 1  # Maths
    elif 11 <= hour < 12:
        return 2  # Chemistry
    elif 12 <= hour < 13 or 13 <= hour < 14:
        return 3  # English
    elif 14 <= hour < 15:
        return 4  # Computer
    return None




def recognize_faces(image_path, conn):
    try:
        # Load image
        img = cv2.imread(image_path)
        
        # Recognize faces
        result = DeepFace.find(img_path=image_path, db_path="/media/ayush/New Volume/Infosys Springboard/infosys springboard iamges/traindata", enforce_detection=False)
        
        recognized_students = []
        for face in result:
            student_name = face['identity'].split(os.sep)[-2]  # Extract student name from the result
            
            # Query the student table to get the student ID
            cur = conn.cursor()
            cur.execute("SELECT id FROM student WHERE name = %s", (student_name,))
            student_id = cur.fetchone()
            if student_id:
                recognized_students.append((student_id[0], student_name))
            cur.close()
        
        return recognized_students
    except Exception as e:
        print(f"Error recognizing faces: {e}")
        return []




def label_faces(image_path, recognized_students):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 20)
    
    for (student_id, student_name), face in zip(recognized_students, faces):
        box = face['region']
        draw.rectangle([box['x'], box['y'], box['x']+box['w'], box['y']+box['h']], outline="red", width=3)
        draw.text((box['x'], box['y']-20), student_name, fill="red", font=font)
    
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()




def insert_into_attendance(conn, date_time, subject_id, student_id, img_bytes):
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO attendance (date, subject_id, student_id, image) 
            VALUES (%s, %s, %s, %s)
        """, (date_time, subject_id, student_id, psycopg2.Binary(img_bytes)))
        conn.commit()
        cur.close()
    except Exception as e:
        print(f"Error inserting into attendance: {e}")


def main(image_path):
    conn = connect_to_db()
    if conn is None:
        return
    
    date_time = extract_datetime_from_filename(os.path.basename(image_path))
    if date_time is None:
        return
    
    subject_id = get_subject_id(date_time)
    if subject_id is None:
        print("No subject found for the given time")
        return
    
    recognized_students = recognize_faces(image_path, conn)
    for student_id, student_name in recognized_students:
        img_bytes = label_faces(image_path, recognized_students)
        insert_into_attendance(conn, date_time, subject_id, student_id, img_bytes)
    
    conn.close()




# Provide the path to your test image
main("/media/ayush/New Volume/Infosys Springboard/infosys springboard iamges/test_data/group/20240705_1100.jpg")


