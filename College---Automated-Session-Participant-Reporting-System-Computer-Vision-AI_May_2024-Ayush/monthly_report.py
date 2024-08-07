import psycopg2
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Fetch attendance data from the database
def fetch_attendance_data():
    try:
        conn = psycopg2.connect(
            dbname="x", 
            user="x", 
            password="x", 
            host="127.0.0.1",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM attendance")
        records = cur.fetchall()
        colnames = [desc[0] for desc in cur.description]
        cur.close()
        conn.close()
        return pd.DataFrame(records, columns=colnames)
    except Exception as e:
        logging.error(f"Error fetching data from database: {e}")
        return pd.DataFrame()

# Map subject ID to subject name
def map_subject_id(subject_id):
    subject_map = {1: 'maths', 2: 'chemistry', 3: 'english', 4: 'physics', 5: 'computers'}
    return subject_map.get(subject_id, 'Unknown')

# Organize data into monthly attendance report
def organize_data(attendance_data):
    attendance_data['subject'] = attendance_data['subject_id'].apply(map_subject_id)
    attendance_data['student'] = attendance_data['student_id'].apply(lambda x: f'Student {x}')
    
    # Calculate monthly statistics
    attendance_summary = attendance_data.groupby(['student', 'subject']).agg(
        total_classes=('id', 'count')
    ).reset_index()
    
    attendance_summary['present'] = attendance_summary['total_classes']
    attendance_summary['absent'] = 0
    attendance_summary['attendance_percentage'] = 100
    
    # Rename columns for final output
    attendance_summary.columns = ['Student Name', 'Subject', 'Total Classes', 'Present', 'Absent', 'Attendance %']
    
    return attendance_summary

# Send email with the CSV attachment
def send_email(subject, body, to_email, csv_attachment):
    from_email = "support@aptpath.in"
    password = "btpdcnfkgjyzdndh"
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach CSV file
    try:
        with open(csv_attachment, "rb") as attachment_file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment_file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(csv_attachment)}")
            msg.attach(part)
    except Exception as e:
        logging.error(f"Error attaching CSV file: {e}")
    
    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        logging.info("Email sent successfully")
    except Exception as e:
        logging.error(f"Error sending email: {e}")

# Main function to generate and send the report
def generate_and_send_report(to_email):
    # Fetch and organize data
    attendance_data = fetch_attendance_data()
    if attendance_data.empty:
        logging.error("No attendance data fetched, aborting report generation")
        return
    
    organized_data = organize_data(attendance_data)
    
    # Convert to CSV
    csv_filename = "monthly_attendance_report.csv"
    organized_data.to_csv(csv_filename, index=False)
    
    # Send email
    subject = "Monthly Attendance Report"
    body = "Please find the attached monthly attendance report."
    
    send_email(subject, body, to_email, csv_filename)

# Call the function with the recipient email
recipient_email = "exmp@gmail.com"
generate_and_send_report(recipient_email)
