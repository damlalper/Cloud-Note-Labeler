import firebase_admin
from firebase_admin import credentials, firestore
from textblob import TextBlob

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
notes_ref = db.collection("notes")

# Function to auto-label notes
def auto_label(note):
    analysis = TextBlob(note)
    if "AI" in note.upper() or "ML" in note.upper() or analysis.sentiment.polarity > 0:
        return "AI"
    else:
        return "General"

# Add a note
def add_note():
    note = input("Enter note: ")
    label = auto_label(note)
    notes_ref.add({"note": note, "label": label})
    print(f"Note added! Label: {label}")

# List all notes
def list_notes():
    notes = notes_ref.stream()
    print("\nNotes:")
    for i, n in enumerate(notes, 1):
        data = n.to_dict()
        print(f"{i}. {data['note']} [{data['label']}]")

# Delete a note
def delete_note():
    list_notes()
    notes = list(notes_ref.stream())
    if notes:
        idx = int(input("Enter note number to delete: ")) - 1
        if 0 <= idx < len(notes):
            notes[idx].reference.delete()
            print("Note deleted!")

# CLI menu
while True:
    print("\n1. Add Note\n2. List Notes\n3. Delete Note\n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_note()
    elif choice == "2":
        list_notes()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
