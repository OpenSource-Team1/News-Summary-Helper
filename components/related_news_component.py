import streamlit as st
from utils.related_news import step1

def suggest_related_news():
    result = step1("핸드폰 충전")

    for article in result:
        with st.container():
            st.write(article['url'])
