import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore

from pyrogram import Client, filters
from config import BOT_TOKEN, API_HASH, API_ID, FIREBASE_KEY

# connects with the db and gets the firestore client
def dbInitialization():
    if not FIREBASE_KEY:
        print("Error: FIREBASE_KEY environment variable not set!")
        exit()
    try:
        cred = credentials.Certificate(FIREBASE_KEY)
        firebase_admin.initialize_app(cred)
        print("Firebase Admin SDK initialized successfully!")
        db = firestore.client()
        return db



    except Exception as e:

        print(f"Error initializing Firebase Admin SDK: {e}")
        
        exit()


# pings with db by trying to get a nonexistent collection
def dbPing(firestore_client):
    try:
       
        doc_ref = firestore_client.collection("health_checks").document("ping_test_document")
        doc = doc_ref.get()

        print("Firestore 'ping' successful: Connection established.")
        return True
    except Exception as e:
        print(f"Firestore 'ping' failed: {e}")
        return False