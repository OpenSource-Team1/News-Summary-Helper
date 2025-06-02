import streamlit as st
from components.news_summary_process import select_options, show_input_news, show_summary_title
from components.ten_years_ago_component import get_10years_ago_news, con, sidebarCon


def run():
    
    st.title("📝 ")
    df = get_10years_ago_news() # 10년 전 기사 데이터 불러오기 (/components/ten_years_ago_component)
    
    col1, col2 = st.columns([4, 1])

    with col1.container():
        
        text, lang, length_option = select_options()
        show_input_news(text, lang, length_option)

        if st.button("Generate"):
            if not text.strip():
                st.warning("텍스트를 입력해주세요.")
            else:
                show_summary_title(text, lang)
    sidebarCon(df)

