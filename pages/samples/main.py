import streamlit as st
from components.news_summary_process import run as news_summary_process
from components.ten_years_ago_component import get_10years_ago_news, con, sidebarCon


def run():
    
    st.title("📝 ")
    df = get_10years_ago_news() # 10년 전 기사 데이터 불러오기 (/components/ten_years_ago_component)
    
    col1, col2 = st.columns([4, 1])

    with col1.container():
        news_summary_process()  # generate_summary_and_title_demo 활용
    sidebarCon(df)

