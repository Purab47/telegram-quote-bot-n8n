# 📜 Telegram Quote Bot with n8n Integration

This project is a mini automation that scrapes top quotes from [quotes.toscrape.com](https://quotes.toscrape.com), and sends them to a Telegram bot using a combination of Python and the automation tool [n8n](https://n8n.io/).

## 🚀 Features

- Scrapes top 5 quotes from a public quote website.
- Sends the quotes to a Telegram bot chat automatically.
- Integrates Python with n8n using the **Execute Command** node.
- UTF-8 safe handling for emojis and special characters.
- Easily customizable and extendable (schedule, store, notify, etc.).

---

## 🧰 Tech Stack

- Python (with `requests` and `BeautifulSoup`)
- Telegram Bot API
- n8n (open-source workflow automation)

---

## 📁 File Structure

```bash
.
├── job_scraper.py          # Python script that scrapes and sends quotes
├── Send_Quotes_to_Telegram.json       # (Optional) Exported n8n workflow file
└── README.md               # Project overview and documentation
