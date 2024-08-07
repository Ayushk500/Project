Infosys Internship 4.0 Project 

Documentation 

Project Documentation: College - Automated Session Participant Reporting 
System (Computer Vision AI). 

Introduction 
The objective of this project is to streamline the attendance tracking procedure through the 
implementation of facial recognition technology. The system functions by taking 
photographs of students within a classroom setting, accurately identifying them, and then 
recording their attendance in a centralized database. Key technologies utilized in this 
initiative include Python, PostgreSQL, and a range of machine learning libraries. 

Specifically designed for educational institutions, the project addresses the following 
functionalities: 
• Image capture using a camera 
• Student identification through facial recognition algorithms 
• Storage of attendance data in a database 
• Automated generation and distribution of attendance reports 
Exclusions: 
• Integration with pre-existing attendance systems 
• Real-time monitoring of attendance 
• Rigorous testing across diverse lighting environments 
 
 
Requirements 
Functional Requirements: 
• Image capture and processing for student identification. 
• Storage of attendance records in a PostgreSQL database. 
• Generation of daily and monthly attendance reports. 
• Distribution of reports via email to faculty, students, and the director. 
 
Non-Functional Requirements: 
• The system should be able to handle images with multiple faces. 
• The system should be robust against variations in lighting and image quality. 
• The system should ensure data security and privacy.

User Stories: 
• As a teacher, I want to receive daily attendance reports via email. 
• As an administrator, I want to be able to view and download attendance records. 
Technical Stack 
• Programming Languages: Python 
• Frameworks/Libraries: OpenCV, DeepFace, Pandas, NumPy, Psycopg2, OS , MIME  
• Databases: PostgreSQL 
• Tools/Platforms: Email (SMTP), Schedule, SQLAlchemy 
 
Architecture/Design 
System Architecture: 
• Image Capture: Captures images at scheduled intervals. 
• Face Recognition: Uses DeepFace module to detect and identify students. 
• Database: Stores attendance records. 
• Report Generation: Generates and sends reports via email. 
Design Decisions: 
• Model: Used VGG-Face for face recognition due to its high accuracy. 
• Database: Chose PostgreSQL for its robustness, ease of integration and open-source 
nature with Python. 
• Email Service: Utilized SMTP with Office365 for sending emails. 
 
Development 
Technologies and Frameworks: 
• Python for scripting and development. 
• OpenCV for image processing. 
• DeepFace for facial recognition. 
• Pandas and NumPy for data manipulation. 
• SQLAlchemy for database operations.
• Schedule for task scheduling. 
• SMTP for email notifications. 
Coding Standards and Best Practices: 
• Followed PEP8 for Python coding standards. 
• Modularized the code for maintainability. 
• Implemented error handling and logging. 
Challenges: 
• Handling images with multiple faces: Addressed by adjusting the face detection 
thresholds. 
• Ensuring accurate face recognition: Improved by training on a larger dataset of 
student images. 
 
Testing 
Testing Approach: 
• Unit Tests: Tested individual functions for face detection and recognition. 
• Integration Tests: Tested the integration between image capture, recognition, and 
database storage. 
• System Tests: End-to-end testing of the entire workflow from image capture to 
report generation. 
Results: 
• Successfully identified and marked attendance for over 90% of the test images. 
• Detected and resolved minor bugs related to image processing and database 
connectivity. 
 
Deployment 
Deployment Process: 
• Set up the PostgreSQL database on a local server. 
• Configured the Python environment with necessary libraries. 
• Scheduled the image capture and processing script using the Schedule library.
• Automated the report generation and email sending process. 
Deployment Instructions: 
1. Install PostgreSQL and create the necessary database and tables. 
2. Set up the Python environment and install required libraries. 
3. Configure the email settings in config.py. 
4. Run the scheduling script to start the daily, weekly, and monthly tasks. 
 
User Guide 
Using the Application: 
1. Place the camera in the classroom to capture images. 
2. Ensure the image file names follow the HH-MM-SS.jpg format. 
3. The system will automatically process the images and mark attendance. 
4. Reports will be generated and sent to the configured email addresses. 
Troubleshooting Tips: 
• If the system fails to recognize faces, check the image quality and lighting conditions. 
• Ensure the database is running and accessible. 
• Check the email configuration if reports are not being sent. 
 
Conclusion 
The Auto Attendance System effectively automates the process of marking attendance, 
offering a dependable and efficient solution tailored for educational institutions. Noteworthy 
accomplishments include excellent accuracy in facial recognition and smooth integration 
with email services for distributing reports. 
 
Lessons Learned: 
• The significance of high-quality images in ensuring accurate face recognition. 
• The necessity for comprehensive testing across diverse environments to guarantee 
robust performance.  
• The importance of modular code design to facilitate maintenance and scalability.

Future Improvements: 
• Incorporation with real-time attendance monitoring systems. 
• Improvement of face recognition accuracy across varying lighting conditions. 
• Scaling the system to accommodate multiple classes and subjects.
