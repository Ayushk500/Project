import psycopg2
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Fetch attendance data from the database
def fetch_attendance_data():
    conn = psycopg2.connect(
        dbname="x", 
        user="x", 
        password="x", 
        host="127.0.0.1"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM attendance")
    records = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()
    return pd.DataFrame(records, columns=colnames)

# Map subject ID to subject name
def map_subject_id(subject_id):
    subject_map = {1: 'maths', 2: 'chemistry', 3: 'english', 4: 'physics', 5: 'computers'}
    return subject_map.get(subject_id, 'Unknown')

# Organize data into two columns: student name and subject
def organize_data(attendance_data):
    attendance_data['subject'] = attendance_data['subject_id'].apply(map_subject_id)
    attendance_data['student'] = attendance_data['student_id'].apply(lambda x: f'Student {x}')
    organized_data = attendance_data[['student', 'subject']]
    return organized_data

# Save image from the database to a file
def save_image(image_data, filename):
    with open(filename, 'wb') as f:
        f.write(image_data)

# Send email with the CSV and image attachments
def send_email(subject, body, to_email, csv_attachment, image_attachment):
    from_email = "support@aptpath.in"
    password = "btpdcnfkgjyzdndh"
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach CSV file
    with open(csv_attachment, "rb") as attachment_file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment_file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(csv_attachment)}")
        msg.attach(part)
    
    # Attach Image file
    with open(image_attachment, "rb") as attachment_file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment_file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(image_attachment)}")
        msg.attach(part)
    
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

# Main function to generate and send the report
def generate_and_send_report():
    # Fetch and organize data
    attendance_data = fetch_attendance_data()
    organized_data = organize_data(attendance_data)
    
    # Convert to CSV
    csv_filename = "attendance_report.csv"
    organized_data.to_csv(csv_filename, index=False)
    
    # Save the first image (you can modify to handle multiple images as needed)
    image_data = attendance_data.loc[0, 'image']
    image_filename = "attendance_image.png"
    save_image(image_data, image_filename)
    
    # Send email
    subject = "Daily Attendance Report"
    body = "Please find the attached daily attendance report and image."
    to_email = "exmp@gmail.com"
    
    send_email(subject, body, to_email, csv_filename, image_filename)

# Call the function
generate_and_send_report()
