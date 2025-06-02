import feedparser
import time, datetime
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from utils.connection import updateDB
from newspaper import Article
from sqlalchemy import text

# 📌 예시: 네이버 뉴스 RSS (IT/과학)
rss_url = "	http://www.khan.co.kr/rss/rssdata/total_news.xml"  # 예시 (전자신문)

# 1️⃣ RSS 피드에서 기사 URL 가져오기
feed = feedparser.parse(rss_url)
print("RSS URL:", rss_url)

print("Feed keys:", feed.keys())  # feed.entries 외에 어떤 키가 있는지 보기
print("Entries 개수:", len(feed.entries))

print(f"RSS에서 {len(feed.entries)}개의 기사 발견!")

# 2️⃣ 각 기사 크롤링
sqlList = []
paramList = []
for entry in feed.entries:
    url = entry.link
    print(f"\n[기사 URL] {url}")

    try:
        # newspaper3k 사용
        article = Article(url, language='ko')
        article.download()
        article.parse()


        print(f"제목: {article.title}")
        print(f"날짜: {str(article.publish_date)[:10]}")
        print(f"본문 (10자): {article.text[:10]}...")

        # ✅ 여기서 DB 저장 or 파일 저장 가능 (예: CSV, SQLite 등)
        sql = text("""
        INSERT INTO related_news (url, title, date, content)
        VALUES (:url, :title, :date, :content)
        """)

        params = {
            "url": entry.link,
            "title": article.title,
            "date": str(article.publish_date)[:10],
            "content": article.text
        }

       # 금일 기사만 크롤링하도록 필터링
        if str(article.publish_date)[:10] == str(datetime.datetime.now())[:10]:
            print('this is today news')
            sqlList.append(sql)
            aramList.append(params)

    except Exception as e:
        print(f"크롤링 실패: {e}")

    time.sleep(1)  # polite crawling (1초 대기)
result = updateDB(sqlList, paramList)
if result['status'] == "success":
    print("done!")