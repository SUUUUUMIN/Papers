from Crawling import crawling_data
from Summary import summarize_with_llm
from Sending import send_automated_email
from Telegram import send_telegram_msg

papers, date = crawling_data()
body = summarize_with_llm(papers)
send_telegram_msg(date, body) #Telegram
#send_automated_email(date, body) #Email