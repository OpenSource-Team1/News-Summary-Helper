from transformers import pipeline
import streamlit as st


@st.cache_resource
def load_classifier():
    try:
        classifier = pipeline("text-classification",
                              model="classla/multilingual-IPTC-news-topic-classifier",
                              device=-1, max_length=512, truncation=True)
    except Exception as e:
        raise RuntimeError(f"분류 모델 로딩에 실패했습니다 : {e}")

    return classifier


def detect_topic(text):
    classifier = load_classifier()
    result = classifier(text)[0]["label"]
    return result


def get_topic():
    topic = ['education', 'human interest', 'society', 'sport', 'crime, law and justice',
             'disaster, accident and emergency incident', 'arts, culture, entertainment and media',
             'politics', 'economy, business and finance', 'lifestyle and leisure', 'science and technology',
             'health', 'labour', 'religion', 'weather', 'environment', 'conflict, war and peace']

    return topic

def topic_to_category(topic):
    socialCondition = (topic == 'human interest' or topic == 'society' or topic == 'crime, law and justice' or topic == 'disaster, accident and emergency incident' or topic == 'labour'
                    or topic == 'religion')
    cultureCondition = (topic == 'arts, culture, entertainment and media' or topic == 'lifestyle and leisure')
    scienceCondition = (topic == 'education' or topic == 'science and technology' or topic == 'health' or topic == 'weather' or topic == 'environment')

    if topic == 'economy, business and finance':
        return "경제"
    elif topic == 'politics':
        return "정치"
    elif socialCondition:
        return "사회"
    elif topic == 'conflict, war and peace':
        return "국제"
    elif cultureCondition:
        return "문화"
    elif topic == 'sport':
        return "스포츠"
    elif scienceCondition:
        return "과학"