import os
import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TELEGRAM_TOKEN = "input telegram bot token here"
openai.api_key = "input openai api key here"

def chatgpt_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
       stop=None,
        temperature=0.8,
    )

    message = completions.choices[0].text
    return message.strip()

def echo(update, context):
    user_input = update.message.text
    response = chatgpt_response(user_input)
    if not response:
        response = "I'm sorry, I am unable to generate a response based on your input."

    while response:
        if len(response) > 4096:
            chunk = response[:4096]
            response = response[4096:]
        else:
            chunk = response
            response = ""
        update.message.reply_text(chunk)
    
def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
