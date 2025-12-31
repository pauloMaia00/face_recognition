# Face Recognition Project

The Face Recognition Attendance System is a Python-based computer vision application designed to automate attendance tracking using facial recognition. Instead of relying on manual roll calls or sign-in sheets, the system identifies individuals through a live camera feed and records their attendance automatically.

This project demonstrates how computer vision, image processing, and machine learning concepts can be applied to solve a real-world problem efficiently. The system is capable of detecting faces in real time, recognizing known individuals by comparing facial features, and logging attendance with timestamps for record-keeping and analysis.

---

## Motivation & Problem Statement
Traditional attendance systems suffer from several drawbacks:
-They are time-consuming, especially in large classrooms or workplaces.
- They are prone to human error and proxy attendance.
- They require manual effort and constant supervision.

This project addresses those issues by:
- Eliminating manual intervention
- Increasing accuracy using biometric identification
- Providing a scalable and reusable automated solution

---

## Key Features
- Real-Time Face Detection
  Uses OpenCV to continuously scan video frames and locate human faces.

- Face Recognition
  Identifies individuals by comparing live facial encodings against a stored dataset of known faces.

- Automated Attendance Logging
  When a known face is detected, the system records the person’s name along with the current date and time.

- Persistent Attendance Records
  Attendance is saved to a CSV file, making it easy to analyze, export, or integrate with other systems.

- Expandable Dataset
  New users can be added simply by adding images to the dataset folder.

---

## Tech Stack

- **Python** - chosen for its strong ecosystem in data science and computer vision.
- **OpenCV (cv2)** – Handles image processing, webcam access, and face detection.
- **face_recognition** – Extracts facial embeddings and performs face matching using deep learning techniques.
- **numpy** - Efficient numerical operations on image arrays.
- **Pandas/CSV Handling** - Used for managing attendance records in a structured format. 

---

## Project Structure

---

## Folder & File Explanation
- ImgBasic and ImgAttendences
  Contains labeled images of known individuals. Each folder contains files and the file names corresponds to a person’s identity.
- Attendances.csv
  Stores attendance logs with name, date, and time.
- basics.py
  Loads images from the dataset and computes facial encodings.
- AttendencesProject.py
  Runs real-time face detection and recognition using a webcam.
- requirements.txt
  Lists all Python dependencies required to run the project.

---

## System Workflow
This system follows a structured pipeline to automate attendance using facial recognition:
- Image Collection - Images of known individuals are collected and stored in the dataset/ directory. Each person has a dedicated folder containing multiple facial images to improve recognition accuracy.
- Face Encoding - The system processes each image and extracts unique facial features (encodings). These encodings act as numerical representations of faces and are stored for comparison.
- Real-Time Face Detection - A live video stream is captured using a webcam. OpenCV detects faces in each frame.
- Face Recognition - Detected faces are encoded and compared against the stored encodings of known individuals.
- Attendance Recording - When a match is found, the system logs the person’s name along with the current date and time into an attendance file. Duplicate entries for the same session are prevented.

---

## Installation & Setup
Prerequisites
- Python 3.8 or higher
- Webcam or external camera
- Supported operating system (Windows, macOS, or Linux)

## Clone the Repository
`git clone https://github.com/pauloMaia00/face_recognition`
`cd face-recognition-attendance`

## Install Required Dependencies
`pip install -r requirements.txt`


The required packages include:
- opencv-python
- face-recognition
- numpy
- pandas


## How to Run the Project
Step 1: Train Face Encodings
Run the training script to process all images and generate face encodings:

`python basics.py`

Step 2: Start the Attendance System
Launch the real-time face recognition and attendance capture:

`python AttendencesProject.py`

Step 3: View Attendance Records
Attendance will be automatically recorded in:

`Attendances.csv`

