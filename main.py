from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import telebot
import time
import re

# Telegram Bot Token & Channel ID
BOT_TOKEN = "7403870709:AAHrQzyQkyetO9rHJvgV7Mh8TMhb3XQnWdE"
CHANNEL_ID = "@ff_id_unban"  # Replace with your channel's username or ID
 # Replace with your channel's username or ID
bot = telebot.TeleBot(7403870709:AAHrQzyQkyetO9rHJvgV7Mh8TMhb3XQnWdE)

# Function to check UID on the website
def check_uid(uid):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get("https://freefireinfo.in/unban-your-free-fire-account-in-2025-100-working-trick-step-by-step-guide/")
        time.sleep(3)  # Wait for the page to load
        
        input_box = driver.find_element(By.XPATH, "//input[@type='text']")
        input_box.send_keys(uid)
        input_box.send_keys(Keys.RETURN)
        
        time.sleep(5)  # Wait for results to load
        
        result_text = driver.find_element(By.CLASS_NAME, "result-class").text  # Update selector as per the site
        driver.quit()
        return result_text
    except Exception as e:
        driver.quit()
        return f"Error fetching details: {str(e)}"

# Handling messages in group
@bot.message_handler(func=lambda message: message.text and message.text.startswith("gat "))
def fetch_uid(message):
    chat_id = message.chat.id
    text = message.text.strip()
    
    uid_match = re.search(r"gat (\d+)", text)
    if uid_match:
        uid = uid_match.group(1)
        bot.send_message(chat_id, f"Checking UID: {uid}... Please wait!")
        result = check_uid(uid)
        bot.send_message(CHANNEL_ID, f"✅ UID Check Result:\n{result}")
    else:
        bot.send_message(chat_id, "Invalid UID format! Use: gat 12345678")

# Start bot
print("Bot is running...")
bot.polling(none_stop=True)
