from pyrogram import Client, filters
from config import BOT_TOKEN, API_HASH, API_ID

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

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

# trail 2 
@app.on_message(filters.private)
def private_chat_handler(client, message):
    stop_words = set(stopwords.words('english'))
    tokenized = sent_tokenize(message)
    for i in tokenized:
    
        # Word tokenizers is used to find the words 
        # and punctuation in a string
        wordsList = nltk.word_tokenize(i)

        # removing stop words from wordList
        wordsList = [w for w in wordsList if not w in stop_words] 

        #  Using a Tagger. Which is part-of-speech 
        # tagger or POS-tagger. 
        tagged = nltk.pos_tag(wordsList)

        message.reply_text(tagged)

      
if __name__ == "__main__":
    app.run()