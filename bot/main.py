import nltk

from pyrogram import Client, filters
from config import BOT_TOKEN, API_HASH, API_ID

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from backend.db import dbInitialization, dbPing


app = Client("Cuss-o-meter", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.private & filters.command("start"))
def private_chat_handler(client, message):
    message.reply_text("Hello! I'm Cuss-o-meter. The greatest cussing meter bot.")
    
@app.on_message(filters.command("start") & filters.group)
def group_start_handle(client, message):
    message.reply_text("Hello! I'm Cuss-o-meter. The greatest cussing meter bot.")

# trial 
@app.on_message(filters.private & filters.command("cuss"))
def private_chat_handler(client, message):
    message.reply_text("that aint funny cuhh")


# bad words list, trial
bW = {
    "fuck",
    "damn",
    "shit",
    "bitch",
    "mf"
}

# trial 2 
@app.on_message(filters.private)
def private_chat_handler(client, message):
    
    nltk.download('punkt_tab')
    nltk.download('averaged_perceptron_tagger_eng')
    
    # porter turns every word into its base form
    porter = PorterStemmer()    
   
    # changes the sentence into a 
    tokenized = word_tokenize(message.text)

    #turns each word into its base form and checks if it exists in the bad word list
    wordsList = len([w for w in tokenized if porter.stem(w) in bW]) 

    
    
    message.reply_text("Cuss Counter: "+str(wordsList))

      
if __name__ == "__main__":
    app.run()