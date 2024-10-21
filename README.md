# FACE_DETECTION_FACE_RECOGNIZATION_USING_OPENCV
A simple face detection and recognition project using OpenCV, Haar cascades, and LBPH recognizer. It detects faces, trains on images, and identifies people with confidence scores.


# Face Recognition System Using OpenCV & Haar Cascades 🚀
Overview 💻
This project implements Face Detection and Recognition using OpenCV's Haar cascades and Local Binary Patterns Histograms (LBPH) for face recognition. It processes images by detecting faces, grayscaling them, and training a face recognizer to identify people.

Features 🌟
Face Detection using Haar cascades.
Face Recognition through LBPH, trained on specific images of people.
Multi-face detection across several input images.
Confidence Scoring for recognized faces.
Libraries Used 📚
OpenCV
Numpy
Pytesseract (optional for OCR tasks)
Steps 🛠️
Face Detection: Detects faces in input images and highlights them using green rectangles.
Training Model: Loads images, detects faces, and trains the LBPH face recognizer.
Face Recognition: The trained model predicts the person’s name and provides confidence scores.
Usage 🚀
Place your images for training in separate folders under the Faces directory.
Modify the people list to match folder names.
Run the training script to create the recognizer model.
Test the model by running the recognition script on test images.
Enjoy face recognition magic! 🎉
