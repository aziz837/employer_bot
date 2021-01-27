from telegram.ext import CommandHandler, MessageHandler, Filters
from django_telegrambot.apps import DjangoTelegramBot

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

    update.message.reply_text('KIMSIZ UZI ? :', reply_markup=reply_markup)
    return 2
   
def descriptions(update: Update, context: CallbackContext):
    query = update.callback_query
    datas = query.data.split('_')
    print(query)
    text = 'Ish xaqida qisqacha malumot yozing'
    query.message.reply_text(text)
    return 4

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
    return 3


def region(update: Update, context: CallbackContext):
    
    regions = Region.objects.filter(parend_id=0)
    buttons= generateButtons(regions)
    
    update.message.reply_text(
        'Qaysi Viloyatdansz: ', 
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    return 5

def district(update: Update, context: CallbackContext):

    query = update.callback_query
    datas = query.data.split('_')
    if datas[0] == 'category':
        cat_id = int(datas[1])
        print(cat_id)
        disct = Region.objects.raw('SELECT * FROM bot_region where parend_id=%s',[cat_id])
        print(disct)
        buttons= generateButtons(disct)
    query.message.delete()
    query.message.reply_text(
        'Qaysi tumandansz: ', 
        reply_markup=InlineKeyboardMarkup(buttons)
    )

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


