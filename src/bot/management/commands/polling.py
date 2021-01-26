import logging

from django.core.management.base import BaseCommand
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from ...telegrambot import start, help_command

class Command(BaseCommand):
    help = "Run telegram bot in polling mode"
    can_import_settings = True

    
    def handle(self, *args, **options):
        updater = Updater("1547973611:AAE3E5orFqkqw_9csRaK2Rqyt9pdCJH1Fh8", use_context=True)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("help", help_command))
        updater.start_polling()
        updater.idle()