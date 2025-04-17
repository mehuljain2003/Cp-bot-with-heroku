# CPFree Telegram Bot

A Python Telegram bot deployed on Heroku to execute custom commands from Telegram.

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/cpfree-bot.git
   cd cpfree-bot
   ```

2. Set your Telegram bot token inside `cpfree.py`.

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Deploy to Heroku:
   ```bash
   heroku create
   git push heroku main
   ```

5. Scale the worker:
   ```bash
   heroku ps:scale worker=1
   ```

## Usage

Send commands to your Telegram bot to run the script remotely.
