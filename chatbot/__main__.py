"""This module contains the command line interface to the chatbot package."""

import sys

from chatbot import __version__ as version
from chatbot.chatbot_lib import chat_with_gpt


def main():
    """
    The main routine.
    :return: None
    """

    print(f"Running version {version} from {__file__}.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)


if __name__ == "__main__":
    sys.exit(main())
