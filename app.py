import streamlit as st

# 각 모듈에서 run 함수 import
from pages.samples.kobart_summary_sample import run as kobart_summary
from pages.samples.generate_title_sample import run as generate_title
from pages.demos.generate_and_detect_demo import run as generate_and_detect
from pages.demos.generate_summary_and_title_demo import run as generate_summary_and_title
from pages.demos.show_saved_articles import run as show_saved_articles
from pages.demos.ten_years_ago_demo import run as ten_years_ago_demo
from pages.demos.related_news_demo import run as related_news_demo
from pages.samples.main import run as main

# 메뉴 구성
samples = {
    "Home": main,
    # "Kobart News Summary Sample": kobart_summary,
    # "Generate Summary Title Sample": generate_title
}
demos = {
    # "본문 추출 및 언어 감지 Demo" : generate_and_detect,
    # "본문 내용 요약문 및 제목 생성 Demo" : generate_summary_and_title,
    "저장된 기사 요약문 보기 Demo" : show_saved_articles,
    "10년 전 오늘 Demo" : ten_years_ago_demo,
    "관련 기사 제안 Demo" : related_news_demo
}

st.set_page_config(
    page_title="뉴스 요약 앱",
    layout="wide",  # 👉 여백 줄이고 넓게 보기
    initial_sidebar_state="expanded"
)

pages = {**samples, **demos}  # 두 dict 병합
page = st.sidebar.selectbox("Choose a page", pages.keys())
pages[page]()