import logging
from django.conf import settings
from django.core.management.base import BaseCommand
from telegram import Update
from telegram.ext import (
    CommandHandler,
    Updater,
    Filters,
    CallbackContext,
    ConversationHandler,
    MessageHandler,
    CallbackQueryHandler
)

from ...telegrambot import *


class Command(BaseCommand):
    help = "Run telegram bot in polling mode"
    can_import_settings = True

    
    def handle(self, *args, **options):
        updater = Updater(settings.TOKEN_KEY, use_context=True)

        # updater.dispatcher.add_handler(CommandHandler('start', start))
        # updater.dispatcher.add_handler(CallbackQueryHandler(category))
        # updater.dispatcher.add_handler(CommandHandler('help', help_command))
        # updater.start_polling()
        # updater.idle()
        dispatcher = updater.dispatcher
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', start)],
            states={
                category:[CallbackQueryHandler(category)],
                descriptions:[CallbackQueryHandler(descriptions)],
                3: [CallbackQueryHandler(region)]

            },
            fallbacks=[CommandHandler('help', help)],
        )
        dispatcher.add_handler(conv_handler)
        updater.start_polling()
        updater.idle()
