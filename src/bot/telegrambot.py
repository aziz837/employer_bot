from telegram.ext import CommandHandler, MessageHandler, Filters
from django_telegrambot.apps import DjangoTelegramBot
from .services import *
from .models import Category, Region

from telegram.ext import (
    CommandHandler,
    Updater,
    Filters,
    CallbackContext,
    ConversationHandler,
    MessageHandler,
    CallbackQueryHandler
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

# def start()
db = Category()

def start(update: Update, context: CallbackContext) -> None:
    jobs = [
        [
            InlineKeyboardButton("Ish beruvchi", callback_data='1'),
            InlineKeyboardButton("Ish Oluvchi", callback_data='2'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(jobs)

    update.message.reply_text('Categorydan birini kiriting :', reply_markup=reply_markup)
    return category
   


def category(update: Update, context: CallbackContext) :
    query = update.callback_query
    datas = query.data.split('_')
    childs= Category.objects.all()
    buttons = generateButtons(childs)

    query.message.delete()
    query.message.reply_text(
        'Qanday ish qilish kere: ',
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    return descriptions

def descriptions(update: Update, context: CallbackContext):
    query = update.callback_query
    datas = query.data.split('_')
    print(datas)
    query = update.callback_query
    query.message.delete()
    query.message.reply_text(
        'Ish Xaqida qisqacha malumot yozing : ',
    )
    return 3
def region(update: Update, context: CallbackContext):
    query = update.callback_query
    datas = query.data.split('_')
    regions = Region.objects.get(parend_id=null)
    buttons= generateButtons(regions)
    query.message.reply_text(
        'Ish Xaqida qisqacha malumot yozing : ', 
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    return 5
    
def help_command(update, context):
    query = update.callback_query
    datas = query.data.split('_')
    update.message.reply_text('Help!')

def generateButtons(categories):
    buttons = []
    tmp_buttons = []
    for category in categories:
        tmp_buttons.append(
            InlineKeyboardButton(category.title,
            callback_data=f'category_{category.id}')
        )
        if len(tmp_buttons) == 2:
            buttons.append(tmp_buttons)
            tmp_buttons = []
    if len(tmp_buttons) > 0:
        buttons.append(tmp_buttons)

    return buttons

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


