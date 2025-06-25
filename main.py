import streamlit as st
from textblob import TextBlob

# 앱 제목
st.title("😊 간단한 감정 분석기")

# 입력 박스
user_input = st.text_area("문장을 입력해 주세요:", "")

# 분석 버튼
if st.button("감정 분석하기"):
    if user_input.strip() == "":
        st.warning("문장을 입력해 주세요!")
    else:
        # 감정 분석 수행
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity  # -1 ~ 1 사이 값

        # 결과 해석
        if polarity > 0.1:
            sentiment = "긍정 😊"
            color = "green"
        elif polarity < -0.1:
            sentiment = "부정 😞"
            color = "red"
        else:
            sentiment = "중립 😐"
            color = "gray"

        # 결과 출력
        st.markdown(f"**감정 결과**: <span style='color:{color}; font-size:24px'>{sentiment}</span>", unsafe_allow_html=True)
        st.write(f"감정 점수 (Polarity): `{polarity:.2f}`")
