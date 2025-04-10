import requests
from bs4 import BeautifulSoup
import sys

# === Step 1: Scrape quotes ===
def get_quotes():
    url = "https://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('span', class_='text')[:5]
    quote_list = [quote.text for quote in quotes]
    return quote_list

# === Step 2: Send message to Telegram ===
def send_to_telegram(quotes):
    TOKEN = '7929762274:AAHb7rxiif0USqz6i1LmGyRl8tRKBSBXejo'   # Your bot token
    CHAT_ID = '5058786514'                                    # Your chat ID

    message = "📜 Today's Top Quotes:\n\n" + "\n\n".join(quotes)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=payload)

    # Use only ASCII text in print to avoid encoding errors
    print("Message sent to Telegram:", response.status_code)

    # === Output for n8n (UTF-8 safe) ===
    sys.stdout.buffer.write(message.encode('utf-8'))

if __name__ == "__main__":
    quotes = get_quotes()
    send_to_telegram(quotes)
