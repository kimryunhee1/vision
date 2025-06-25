import streamlit as st

# 감정 단어 리스트 (예시)
positive_words = ["좋다", "사랑", "기쁨", "감사", "행복", "최고", "멋지다"]
negative_words = ["싫다", "짜증", "화남", "슬픔", "우울", "불쾌", "최악"]

def analyze_sentiment(text):
    pos = sum(word in text for word in positive_words)
    neg = sum(word in text for word in negative_words)

    if pos > neg:
        return "긍정 😊"
    elif neg > pos:
        return "부정 😞"
    else:
        return "중립 😐"

# Streamlit 인터페이스
st.title("간단한 감정 분석기 (TextBlob 없이)")

text = st.text_area("문장을 입력하세요:")

if st.button("감정 분석하기"):
    if text.strip() == "":
        st.warning("문장을 입력해 주세요!")
    else:
        result = analyze_sentiment(text)
        st.markdown(f"**감정 결과**: <span style='font-size:24px'>{result}</span>", unsafe_allow_html=True)
