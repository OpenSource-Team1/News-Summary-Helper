import streamlit as st
import numpy as np
from utils.connection import connectDB
from components.news_summary_process import run as news_summary_process
import time
import datetime
from dateutil.relativedelta import relativedelta

def run():
    st.title("📝 10년 전 오늘 Demo")
    df = getSql()
    


    col1, col2 = st.columns([3, 2])
    data = np.random.randn(10, 1)

    with col1.container():
        news_summary_process(st)
    with col2.container():
        con(df)
    sidebarCon(df) # Sidebar에 출력

def getSql():
    correct_time = datetime.datetime.now() - relativedelta(years=10)
    # st.write(correct_time.strftime('%Y-%m-%d'))

    df = connectDB("select * from news_summary WHERE article_date =\"" + "2015-05-27" + "\"" ) #  correct_time.strftime('%Y-%m-%d')
    return df



def con(df):
    for i in df:
        # st.caption(str(i['id']) + ":" + i['category'])
        with st.expander(i['title_summary']):
            st.markdown("[" + i['body_summary'] + "](" + i['url'] + ")")


def sidebarCon(df):
    with st.sidebar:
        with st.container(border=True):
            st.info("✅ 10년 전 오늘")
            for i in df:
                st.markdown(str(i['id']) + " : [" + i['title_summary'][:20] + "..." + "](" + i['url'] + ")")
                # st.metric(str(i['id']), i['title_summary'][:20], i['category'])
            # st.caption("This is a string that explains something above.")