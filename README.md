# Cloud Note Labeler ☁️📝

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-Firestore-orange?logo=firebase&logoColor=white)
![AI/NLP](https://img.shields.io/badge/AI-NLP-lightgrey?logo=googleai&logoColor=white)

A simple **Python CLI application** that lets you input short notes, automatically labels them using basic Natural Language Processing (NLP), and stores them in a **Firebase Firestore database**.  

This project demonstrates cloud integration and basic AI/NLP capabilities in a straightforward, practical way—perfect for portfolios or GitHub showcases.

---

## 🚀 Features

- **Add Notes:** Automatically labels new notes as `AI` or `General`.  
- **List Notes:** Displays all your notes stored in Firestore.  
- **Delete Notes:** Easily remove a note from the database.  
- **Cloud Storage:** Seamlessly stores and retrieves data using Firebase Firestore.  
- **Lightweight CLI:** Simple, user-friendly command-line interface.  

---

## 🛠️ Requirements

- **Python 3.x**  
- **Libraries:** `firebase-admin` and `textblob`
- 
### Firebase Service Account Key

This project requires a Firebase Service Account Key to connect to Firestore.  
**Important:** Do **not** upload your `serviceAccountKey.json` file to GitHub for security reasons.

Install libraries via pip:

```bash
pip install firebase-admin textblob
Firebase Project: Active Firebase project with Firestore enabled.

Firebase Service Account Key: A serviceAccountKey.json file for authentication.

⚡ Setup
Create a Firebase Project
Go to the Firebase console and create a new project.

Enable Firestore
Navigate to the Firestore Database section and create a new database.

Generate Service Account Key

Go to Project settings > Service accounts

Click Generate New Private Key, then confirm

Place the Key
Move the downloaded serviceAccountKey.json into the same directory as cloud_note_labeler.py.

🎯 Usage
Run the application from your terminal:

bash
Kodu kopyala
python cloud_note_labeler.py
CLI Menu options:

Add note: Type a new note. The app automatically labels it and saves it to Firestore.

List notes: View all stored notes and their labels.

Delete note: Enter the ID of the note to remove it.

Exit: Close the application.

📝 Notes
Uses TextBlob for basic sentiment and keyword-based analysis.

A simple yet practical demo of cloud-based storage + AI/NLP functionality.

🌟 Optional Enhancements
Web Interface: Add a web front-end using Flask, FastAPI, or React.

Advanced NLP: Upgrade TextBlob with transformer-based models (Hugging Face) for nuanced labeling.

Real-time Updates: Implement Firebase listeners for live note updates.

Badges: Add more badges or icons for better visual appeal.

📂 License
This project is open-source and free to use.
