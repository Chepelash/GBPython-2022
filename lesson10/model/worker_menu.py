
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

#states
(
    START_MENU, 
    SHOW_DATA,
    SELECT_ACTION,
    RETURN_TO_MAIN, 
    BACK
) = map(lambda x: __name__ + x, map(str, range(5)))

# functions
def show_all_workers(update: Update, context: CallbackContext):
    text = "Works"
    buttons = [[InlineKeyboardButton("Назад", callback_data=BACK)]]
    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.answer()    
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    return SHOW_DATA

def start_menu(update: Update, context: CallbackContext):
    text = "Меню работников"
    buttons = [
        [InlineKeyboardButton("Показать всех", callback_data=SHOW_DATA)],
        [InlineKeyboardButton("В главное меню", callback_data=RETURN_TO_MAIN)]
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.answer()    
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    return SELECT_ACTION

def return_upper(update: Update, context: CallbackContext):
    context.user_data[sc.START_OVER] = True
    context.user_data[sc.MAIN_MENU_FUNCTION](update, context)
    return sc.END

def stop_submenu(update: Update, context: CallbackContext):
    update.message.reply_text("Bye")
    return sc.STOPPING
#worker CH
menu_handlers = [
    CallbackQueryHandler(show_all_workers, pattern='^'+SHOW_DATA+'$'),
    # CallbackQueryHandler(add_worker, pattern='^'+ADD_WORKER+'$'),
    # CallbackQueryHandler(edit_worker, pattern='^'+EDIT_WORKER+'$'),
    # CallbackQueryHandler(return_upper, pattern='^' + RETURN_TO_MAIN + '$'),
]
conv_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(start_menu, pattern='^'+START_MENU+'$')],
    states={
        SELECT_ACTION: menu_handlers,
        SHOW_DATA: [CallbackQueryHandler(start_menu, pattern='^'+BACK+'$')]
    },
    fallbacks=[ 
        CommandHandler('stop', stop_submenu),
        CallbackQueryHandler(return_upper, pattern='^' + RETURN_TO_MAIN + '$'),
    ],
    map_to_parent={
        sc.END: sc.SELECTING_MENU,
        sc.STOPPING: sc.STOPPING
    }
)

