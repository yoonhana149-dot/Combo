# Telegram Card Checker Bot

A Telegram bot for checking card validity using Stripe API.

## Setup

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the bot: `python main.py`

## Deployment on Render

1. Fork this repository to your GitHub account
2. Connect your GitHub to Render
3. Create a new Web Service on Render
4. Select your repository
5. Use the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`

## Important Notes

- This bot is restricted to specific chat ID (1753137498)
- Make sure to handle sensitive information properly
- Use environment variables for production tokens
