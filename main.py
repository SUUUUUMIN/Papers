from Crawling import crawling_data
from Summary import summarize_with_llm
from Sending import send_automated_email

papers, date = crawling_data()
body = summarize_with_llm(papers)
send_automated_email(date, body)