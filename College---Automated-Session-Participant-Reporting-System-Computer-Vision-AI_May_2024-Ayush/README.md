# College---Automated-Session-Participant-Reporting-System-Computer-Vision-AI-

This project aims to automate the attendance marking process using facial recognition 
technology. The system captures images of students in a classroom, identifies them, and 
marks their attendance in a database. The project leverages Python, PostgreSQL, and various 
machine learning libraries.  
The project focuses on automating attendance marking for educational institutions. It 
includes: 
• Capturing images using a camera 
• Identifying students using facial recognition 
• Storing attendance records in a database 
• Generating and sending attendance reports 
Exclusions: 
• Integrating with other existing attendance systems 
• Real-time attendance monitoring 
• Extensive testing in varied lighting conditions 
Requirements 
Functional Requirements: 
• Capture and process images to identify students. 
• Store attendance records in a PostgreSQL database. 
• Generate daily and monthly attendance reports. 
• Send reports to faculty, students and director via email. 
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
