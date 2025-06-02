import streamlit as st
from utils.related_news import step1
from utils.classify_topic import topic_to_category

def suggest_related_news():
    articles = st.session_state.get("generated_articles", [])

    if not articles:
        st.info("아직 저장된 기사가 없습니다.")
    else:
        # print("ARTICLES : ", articles)
        result = step1(articles[0]['title'], topic_to_category(articles[0]['topic']))
   
        if not result:
            st.info("관련된 기사가 업데이트 되지 않았습니다.")
        else:
            # print(result)
            for article in result:
                with st.expander(f"**{article['title']}, {article['category']}**"):
                    st.write(article["content"])