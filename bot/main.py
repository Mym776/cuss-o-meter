from pyrogram import Client, filters
from config import BOT_TOKEN, API_HASH, API_ID


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
      
if __name__ == "__main__":
    app.run()