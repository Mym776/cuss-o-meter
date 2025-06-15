import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore

from pyrogram import Client, filters
from config import BOT_TOKEN, API_HASH, API_ID, FIREBASE_KEY

def dbConnect():
    if not FIREBASE_KEY:
        print("Error: FIREBASE_KEY environment variable not set!")
        exit()
    try:
        cred = credentials.Certificate(FIREBASE_KEY)
        firebase_admin.initialize_app(cred)
        print("Firebase Admin SDK initialized successfully!")
        #db = firestore.client()



    except Exception as e:

        print(f"Error initializing Firebase Admin SDK: {e}")
        
        exit()
