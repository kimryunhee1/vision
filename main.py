import streamlit as st

st.set_page_config(page_title="미리 준비된 퀴즈", layout="centered")
st.title("🎯 나를 맞춰봐!")

# 미리 준비된 퀴즈 리스트 (질문, 보기, 정답 인덱스)
quiz_list = [
    {
        "question": "내가 가장 좋아하는 색깔은 무엇일까요?",
        "options": ["파란색", "분홍색", "초록색", "검은색"],
        "answer": 1  # 0-based 인덱스 (파란색)
    },
    {
        "question": "내 취미는?",
        "options": ["노래 듣기", "독서", "쇼핑하기", "춤추기"],
        "answer": 0  # 쇼핑하기
    },
    {
        "question": "내가 스트레스를 받을 때 주로 하는 행동은?",
        "options": ["혼자 누워있기", "친구와 대화하기", "혼자 음악 듣기", "아무것도 안 하기"],
        "answer": 2  # 혼자 음악 듣기 (예시)
    },
    {
        "question": "륜희님이 가장 좋아하는 동물은?",
        "options": ["고양이", "강아지", "토끼", "햄스터"],
        "answer": 0  # 토끼
    },
    {
        "question": "륜희님이 가장 좋아하는 계절은?",
        "options": ["봄", "여름", "가을", "겨울"],
        "answer": 3  # 겨울
    }
]

user_answers = []

st.write("각 문제에 대해 보기 중 하나를 선택하세요:")

for idx, quiz in enumerate(quiz_list):
    st.markdown(f"**Q{idx+1}. {quiz['question']}**")
    choice = st.radio(
        "",
        quiz["options"],
        key=f"quiz_{idx}"
    )
    user_answers.append(choice)

if st.button("정답 제출"):
    score = 0
    st.subheader("결과")
    for idx, quiz in enumerate(quiz_list):
        correct_answer = quiz["options"][quiz["answer"]]
        user_answer = user_answers[idx]
        if user_answer == correct_answer:
            score += 1
            st.success(f"Q{idx+1}: 정답! ✅ ({user_answer})")
        else:
            st.error(f"Q{idx+1}: 오답 ❌ (당신: {user_answer} / 정답: {correct_answer})")
    st.markdown(f"### 🏆 총 점수: {score} / {len(quiz_list)}")
