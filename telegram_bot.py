import telegram.ext
from dotenv import load_dotenv
import os
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
load_dotenv()
TOKEN = os.getenv("TOKEN")
# print(TOKEN)

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    update.message.reply_text("Hello! Welcome Nandini's bot... ")

def helps(update, context):
    help_message = """
    Hi there, This Bot is Created By Nandini Jambhulkar.
    How can I help you?...

    /start - To start the conversation
    /content - Information about This Bot and Owner.
    /contact - Information about contact of Nandini.
    /help - To get this help Menu.

    I hope this helps you :)
    """

    update.message.reply_text(help_message)

def content(update, context): 
    content_message = """
    This Bot is Created By Nandini Jambhulkar. During the Vacation of Diwali...

    Being a first-generation immigrant in India has significantly influenced my distinct viewpoints and ambitions. I possess a natural curiosity for acquiring new knowledge and enjoy the process of learning.

    Life has instilled in me the value of pursuing opportunities, regardless of their level of risk. My professional journey commenced with a Bachelor's degree in Computer Science. I have a passion for exploring the world and capturing moments through photography.

    Please feel free to contact me via LinkedIn. I'm always looking forward to an insightful conversation over tea!
    """
    update.message.reply_text(content_message)
     
def contact(update, context):
    contact_message = """
    You can connect with me on: 
    Portfolio: https://nandinijambhulkar12.github.io/responsive-portfolio-website/
    LinkedIn: https://www.linkedin.com/in/nandini-jambhulkar-11978125b
    GitHub: https://github.com/nandiniJambhulkar12
    """
     update.message.reply_text(contact_message)
     
def handle_message(update, context):
     update.message.reply_text(f"You said: {update.message.text}")

# # Create the Updater and pass it the bot's token
updater = telegram.ext.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# # Register command handlers
dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', helps))
dispatcher.add_handler(telegram.ext.CommandHandler('content', content))
dispatcher.add_handler(telegram.ext.CommandHandler('contact', contact))

# # # Register a message handler to reply to any text messages
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.TEXT & telegram.ext.Filters.MENTION, handle_message))



try:
    
    
# #     # Start the Bot
   updater.start_polling()

# #     # Run the bot until you press Ctrl-C
   updater.idle()
except Exception as e:
    
    logging.error(f"Error: {e}")