from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.connection import getCorrectTime, selectDB
import numpy as np
def step1(title):
    # ✅ 예시 기사 리스트 (딕셔너리 리스트)
    sql = "SELECT * FROM related_news where DATE = '" + getCorrectTime() + "'"
    articles = selectDB(sql)

    # ✅ 기사 본문 리스트 만들기 (content 기준)
    article_contents = [article['content'] for article in articles]

    # ✅ TF-IDF 벡터화
    vectorizer = TfidfVectorizer(max_features=5000)
    article_vectors = vectorizer.fit_transform(article_contents)

    # ✅ 사용자 쿼리
    query_text = title
    query_vector = vectorizer.transform([query_text])

    # ✅ 유사도 계산
    similarities = cosine_similarity(query_vector, article_vectors)[0]
    top_n_idx = np.argsort(similarities)[::-1][:5]

    # ✅ 결과 출력
    print(f"\n✅ 기준 문장: {query_text}\n")
    print("추천 기사 Top 5:")

    result = []
    for rank, idx in enumerate(top_n_idx, start=1):
        article = articles[idx]
        result.append(article)
        print(f"{rank}. {article['title']} (유사도: {similarities[idx]:.2f})")
        print(article['content'][:300] + "...")
        print(article['url'] + "...")
        print("---")
    return result
