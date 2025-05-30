import streamlit as st

# 각 모듈에서 run 함수 import
from pages.samples.plotting_sample import run as show_plotting
from pages.samples.mapping_sample import run as show_mapping
from pages.samples.dataframe_sample import run as show_dataframe
from pages.samples.kobart_summary_sample import run as kobart_summary
from pages.samples.generate_title_sample import run as generate_title
from pages.demos.generate_and_detect_demo import run as generate_and_detect
from pages.demos.generate_summary_and_title_demo import run as generate_summary_and_title
from pages.demos.show_saved_articles import run as show_saved_articles
from pages.demos.ten_years_ago_demo import run as ten_years_ago_demo

def intro():
    st.title("Welcome to Streamlit! 👋")
    st.sidebar.success("Select a demo above.")
    st.write(
        """
        This app showcases different Streamlit features.
        Choose a demo from the sidebar to begin!
        """
    )

# 메뉴 구성
samples = {
    "Home": intro,
    # "Plotting Demo": show_plotting,
    # "Mapping Demo": show_mapping,
    # "DataFrame Demo": show_dataframe,
    "Kobart News Summary Demo": kobart_summary,
    "Generate Summary Title Demo": generate_title
}
demos = {
    "본문 추출 및 언어 감지 Sample" : generate_and_detect,
    "본문 내용 요약문 및 제목 생성 Sample" : generate_summary_and_title,
    "저장된 기사 요약문 보기 Sample" : show_saved_articles
    "10년 전 오늘 Sample" : ten_years_ago_demo
}


pages = {**samples, **demos}  # 두 dict 병합
page = st.sidebar.selectbox("Choose a page", pages.keys())
pages[page]()