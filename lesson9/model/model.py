import random
import logging

from telegram import Update
from telegram.ext import CallbackContext


HELP_TEXT = """Commands:
/help - show this text
/hello - say hello
/rps <rock, paper, scissors> - play rock paper scissors"""

logger = logging.getLogger("my_logger")

def show_help(update: Update, context: CallbackContext):
    logger.debug("Help command")
    update.message.reply_text(HELP_TEXT)


def hello_name(update: Update, context: CallbackContext):
    logger.debug("Hello command")
    update.message.reply_text(f"Hello, {update.effective_user.first_name}")


def play_rps(update: Update, context: CallbackContext):
    logger.debug("RPS command")
    
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    user_action = context.args[0]
    if user_action not in possible_actions:
        update.message.reply_text("Wrong choise")    
    reply_text = ""
    update.message.reply_text(f"Computer chose {computer_action}")
    if user_action == computer_action:
        reply_text = f"Both players selected {user_action}. It's a tie!"
    elif user_action == "rock":
        if computer_action == "scissors":
            reply_text = "Rock smashes scissors! You win!"
        else:
            reply_text = "Paper covers rock! You lose."
    elif user_action == "paper":
        if computer_action == "rock":
            reply_text = "Paper covers rock! You win!"
        else:
            reply_text = "Scissors cuts paper! You lose."
    elif user_action == "scissors":
        if computer_action == "paper":
            reply_text = "Scissors cuts paper! You win!"
        else:
            reply_text = "Rock smashes scissors! You lose."
    update.message.reply_text(reply_text)
