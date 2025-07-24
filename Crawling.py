import requests
from bs4 import BeautifulSoup

# 허깅페이스 url
def crawling_data():
    
    base_url = "https://huggingface.co"
    paper_url = "https://huggingface.co/papers/" # 페이퍼 메인 페이지


    paper_page = requests.get(paper_url)
    paper_soup = BeautifulSoup(paper_page.text, "html.parser")

    date = paper_soup.find("meta", property="og:url").get("content").split("/")[-1]
    today_papers_list = paper_soup.find_all("article")
    print(f"{date} 페이퍼 개수 : {len(today_papers_list)}개")

    papers = {}
    for paper in today_papers_list:
        link = paper.a.get("href")
        full_url = base_url+link
        
        content = requests.get(full_url)
        soup = BeautifulSoup(content.text, "html.parser")
        
        # 내용 추출
        title = soup.find("h1", class_="mb-2 text-2xl font-semibold sm:text-3xl lg:pr-6 lg:text-3xl xl:pr-10 2xl:text-4xl").text.replace("\n ","")
        abstract = soup.find("p", class_="text-gray-600").text
        papers[(title, full_url)] = abstract
    print(papers, len(papers))
    
    return papers, date