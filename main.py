from Crawling import crawling_data
from Summary import llm_summarize
from Sending import send_automated_email

papers, date = crawling_data()
body = llm_summarize(papers)
send_automated_email(date, body)