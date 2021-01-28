from telegram.ext import CommandHandler, MessageHandler, Filters

from .models import Category, Region, User

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
    InlineKeyboardMarkup,
    KeyboardButton
)


import logging
logger = logging.getLogger(__name__)

# def start()
db = Category()

def start(update: Update, context: CallbackContext) -> None:
    tg_user = update.message.from_user
    try:
        user = User.objects.get(tg_id=tg_user.id)
    except Exception as e:
        print('error: ', str(e))
        user = None

    if not user:
        user = User(tg_id=tg_user.id, first_name=tg_user.first_name, last_name=tg_user.last_name)
        user.save()
    tell = user.phone

    jobs = [
        [

            InlineKeyboardButton("Ish beruvchi", callback_data='1'),
            InlineKeyboardButton("Ish Oluvchi", callback_data='2'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(jobs)

    update.message.reply_text('KIMSIZ UZI ? :', reply_markup=reply_markup)

    next = ''
    if tell:
        next = 5
    else:
        next = 2

    return next

def get_phone_number(update: Update, context: CallbackContext):
    query = update.callback_query
    datas = query.data.split('_')
    text = 'Telefon nomeringizni kiriting: '
    # query.message.reply_text(text)
    contact_number = KeyboardButton(text="Contact", request_contact=True)
    query.message.reply_text(text, reply_markup=ReplyKeyboardMarkup([[contact_number]]))
    return 4


def descriptions(update: Update, context: CallbackContext):
    tg_user = update.message.from_user
    phone_user = update.message.text
    try:
        user = User.objects.get(tg_id=tg_user.id)
    except Exception:
        user = None

    print('user_id: ', tg_user.id)
    print('user: ', user)
    user.phone=phone_user
    user.save()

    text = 'Ish xaqida qisqacha malumot yozing'
    update.message.reply_text(text)
    return 8

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
    else:
        disct = Region.objects.raw('SELECT * FROM bot_region')
        print(disct)
        buttons = generateButtons(disct)
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


