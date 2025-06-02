import streamlit as st
from components.ten_years_ago_component import get_10years_ago_news, con, sidebarCon
from components.related_news_component import suggest_related_news

def run():
    st.title("📝 관련 기사 제안 Demo")

    if st.button("Generate", key="related button"):
        suggest_related_news()

