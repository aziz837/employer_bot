from telegram.ext import CommandHandler, MessageHandler, Filters
from django_telegrambot.apps import DjangoTelegramBot

import logging
logger = logging.getLogger(__name__)

def start(update, context):
    print('salom')
    update.message.reply_text('Hi!')


def help_command(update, context):
    update.message.reply_text('Help!')



def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

