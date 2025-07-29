
import requests
import time
import os


def format_result(idx, date, item, last):
    if idx == 0:
        text = f"""
안녕하세요, {date} papers입니다.
<b>{idx+1}. {item["title"]}</b>
{item['response']}
link: {item['link']}
    """
    elif idx == last:
        text = f"""
<b>{idx+1}. {item["title"]}</b>
{item['response']}
link: {item['link']}

감사합니다.
"""
    else:
        text = f"""
<b>{idx+1}. {item["title"]}</b>
{item['response']}
link: {item['link']}
    """
    return text

def prepare_msg(date, summarize):
    body = []
    current_text = ""
    max_length = 4000
    
    last = len(summarize)
    for idx, item in enumerate(summarize):
        text = format_result(idx, date, item, last)
        
        if len(current_text)+len(text) > max_length:
            body.append(current_text)
            current_text=text
        else:
            current_text+=text
    body.append(current_text)
    return body

def send_telegram_msg(date, summarize):
    body = prepare_msg(date, summarize)
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    CHAT_ID = os.environ.get("CHAT_ID")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    for b in body:
        payload = {
            'chat_id' : CHAT_ID,
            'text': b,
            'parse_mode': 'HTML'
        }
        response=requests.post(url, data=payload)
        time.sleep(1)
    