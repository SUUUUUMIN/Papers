import os
from notion_client import Client

def save_to_notion(date, summarize):
    NOTION_API = os.environ.get("NOTION_API")
    DB_ID = os.environ.get("DB_ID")
    
    notion = Client(auth=NOTION_API)
    total_cnt = len(summarize)
    for idx, summary in enumerate(summarize):
        page = notion.pages.create(
            parent = {"database_id": DB_ID},
            properties = {
                "Title": {"title":[{"text": {"content": summary["title"]}}]},
                "Published_Date": {"date": {"start": date}},
                "Link": {"url": summary["link"]},
                "Domain": {"multi_select": [{"name": summary["keywords"]}]}
            },
            children = [
                {
                    "object": "block",
                    "type": "heading_3",
                    "heading_3": {
                        "rich_text": [{"type": "text", "text": {"content": "Summary"}}]
                    }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph":{
                        "rich_text": [{"type": "text", "text": {"content": summary["response"]}}]
                    }
                },
            ]
        )
        print(f"{idx+1}/{total_cnt} 업로드 완료")