import os
import json
import logging

from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,      
)
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    ConversationHandler,
    CallbackQueryHandler,
)

import state_constants as sc
import worker_menu as wm

CREDENTIALS_FILE = "credentials.txt"
TOKEN_FIELD = "auth-token"

logger = logging.getLogger("my_logger")


def init_bot() -> Update:
    logger.debug("%s Checking credentials file", __name__)
    if not os.path.isfile(CREDENTIALS_FILE):
        raise FileNotFoundError(__name__, "No credentials file")
    logger.debug("%s Reading credentials file", __name__)
    with open(CREDENTIALS_FILE, 'r', encoding='utf-8') as f:
        cred_data = json.load(f)
    logger.debug("%s Registering credentials", __name__)
    updater = Updater(cred_data[TOKEN_FIELD])
    logger.debug("%s Registering command handlers", __name__)

    
    #main menu
    select_menu_handlers = [
        wm.conv_handler,
        # dep_conv_handler,
        # jobs_conv_handler,
        CallbackQueryHandler(end, pattern='^'+sc.END+'$'),
    ]
    # main menu conversationHandler    
    main_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            sc.SELECTING_MENU: select_menu_handlers,
            sc.STOPPING: [CommandHandler('start', start)],
            sc.END: [CommandHandler('start', start)],
        },
        fallbacks=[CommandHandler("stop", stop)]
    )
    updater.dispatcher.add_handler(main_conv_handler)
    return updater


def start(update: Update, context: CallbackContext):
    
    text = "Нажмите на кнопку для перехода в подменю"
    buttons = [
        [InlineKeyboardButton(text='операции с работниками', callback_data=wm.START_MENU)],
        # [InlineKeyboardButton(text='операции с департаментами', callback_data=DEP_MENU)],
        # [InlineKeyboardButton(text='операции с должностями', callback_data=JOBS_MENU)],
        [InlineKeyboardButton(text='Закончить работу', callback_data=sc.END)],
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    if context.user_data.get(sc.START_OVER):
        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    else:
        user = update.message.from_user
        update.message.reply_text(f"Бот для работы с кадрами ООО Морж\nДобрый день {user.first_name}")
        update.message.reply_text(text=text, reply_markup=keyboard)
    context.user_data[sc.START_OVER] = False
    context.user_data[sc.MAIN_MENU_FUNCTION] = start
    return sc.SELECTING_MENU


def stop(update: Update, context: CallbackContext):
    # определяем пользователя
    user = update.effective_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("User %s typed stop", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text("stop")
    # Заканчиваем разговор.
    return sc.END

def end(update: Update, context: CallbackContext):
    """End conversation from InlineKeyboardButton."""
    update.callback_query.answer()

    text = 'end'
    update.callback_query.edit_message_text(text=text)
    return sc.END