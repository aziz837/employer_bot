from telegram.ext import CommandHandler, MessageHandler, Filters
from django_telegrambot.apps import DjangoTelegramBot
from telegram.ext import (
    Updater,
    CallbackContext,
)
from telegram import(
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove, 
    Update,  
    InlineKeyboardButton, 
    InlineKeyboardMarkup
) 

import logging
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Ish beruvchi", callback_data='1'),
            InlineKeyboardButton("Ish Oluvchi", callback_data='2'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Categoryadan birini Tanlang:', reply_markup=reply_markup)
    return 

def help_command(update, context):
    update.message.reply_text('Help!')



def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

