import streamlit as st

# 확장된 긍정 단어 목록
positive_words = [
    "좋다", "행복", "기쁘다", "사랑", "감사", "즐겁다", "신난다", "만족", "멋지다", "최고다",
    "훌륭하다", "예쁘다", "잘했다", "성공", "행운", "기분 좋다", "추천", "반가워", "든든하다", "대박"
]

# 확장된 부정 단어 목록 + 아프거나 힘든 감정 표현
negative_words = [
    "싫다", "짜증", "화나다", "슬프다", "우울", "지치다", "힘들다", "나쁘다", "최악", "불만",
    "실망", "지겹다", "짜증난다", "외롭다", "지옥", "무섭다", "불쾌", "지루하다",
    "아프다", "두통", "열", "기침", "피곤", "컨디션", "속이 안좋다", "병원", "몸살", "토할 것 같다",
    "눈물", "스트레스", "정신적", "무기력", "아무것도 하기 싫다"
]

# 감정 분석 함수
def analyze_sentiment(text):
    text = text.lower()
    words = text.split()

    pos_count = sum(any(pos_word in word for pos_word in positive_words) for word in words)
    neg_count = sum(any(neg_word in word for neg_word in negative_words) for word in words)

    if pos_count > neg_count:
        return "긍정 😊", pos_count, neg_count
    elif neg_count > pos_count:
        return "부정 😞", pos_count, neg_count
    else:
        return "중립 😐", pos_count, neg_count

# Streamlit UI 구성
st.title("💬 감정 분석기 (TextBlob 없이 작동)")

user_input = st.text_area("문장을 입력하세요:")

if st.button("감정 분석하기"):
    if user_input.strip() == "":
        st.warning("문장을 입력해 주세요!")
    else:
        result, pos_score, neg_score = analyze_sentiment(user_input)

        st.markdown(f"### 감정 결과: **{result}**")
        st.write(f"👍 긍정 단어 수: `{pos_score}`")
        st.write(f"👎 부정 단어 수: `{neg_score}`")

        # 공감 메시지
        if result == "부정 😞":
            st.info("💙 힘든 마음이 느껴져요. 잠깐 쉬어가도 괜찮아요. 필요한 건 당신의 회복입니다.")
