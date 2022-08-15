from telegram.ext import ConversationHandler

(
    START_OVER,
    SELECTING_MENU,
    STOPPING,
    MAIN_MENU_FUNCTION
) = map(lambda x: __name__ + x, map(str, range(4)))

END = str(ConversationHandler.END)