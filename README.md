# ChatGPT-telegram
Simple working telegram bot written in python
1. pip3 install python-telegram-bot openai
2. edit chatgpt.py
- TELEGRAM_TOKEN #from https://t.me/BotFather
- openai.api_key #from https://beta.openai.com/account/api-keys
- enige (optional):
    text-davinci-002
    text-babbage-001
    text-ada-001
    text-gpt-002
- temperature (optional):
    If you are looking for more deterministic responses, you may want to use a lower temperature, such as 0.1 or 0.2. On the other hand, if you want more varied responses, you may want to use a higher temperature, such as 0.7 or 0.8.
3. run it: python3 chatgpt.py
