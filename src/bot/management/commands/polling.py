import logging
from django.conf import settings
from django.core.management.base import BaseCommand
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from ...telegrambot import start, help_command


class Command(BaseCommand):
    help = "Run telegram bot in polling mode"
    can_import_settings = True

    
    def handle(self, *args, **options):
        updater = Updater(settings.TOKEN_KEY, use_context=True)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("help", help_command))
        updater.start_polling()
        updater.idle()
