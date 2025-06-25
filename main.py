import streamlit as st

st.set_page_config(page_title="나만의 퀴즈 생성기", layout="centered")

st.title("📚 나만의 퀴즈 생성기")

# 세션에 문제 저장할 리스트 초기화
if "quiz_list" not in st.session_state:
    st.session_state.quiz_list = []

with st.expander("➕ 퀴즈 추가하기"):
    question = st.text_input("문제 입력")
    option1 = st.text_input("보기 1")
    option2 = st.text_input("보기 2")
    option3 = st.text_input("보기 3")
    option4 = st.text_input("보기 4")
    answer = st.selectbox("정답 선택", options=["1", "2", "3", "4"])

    if st.button("퀴즈 추가"):
        if all([question, option1, option2, option3, option4]):
            st.session_state.quiz_list.append({
                "question": question,
                "options": [option1, option2, option3, option4],
                "answer": answer
            })
            st.success("퀴즈가 추가되었습니다!")
        else:
            st.warning("모든 항목을 입력해 주세요.")

# 퀴즈 풀이 시작
if st.session_state.quiz_list:
    st.subheader("📝 퀴즈 풀기")

    user_answers = []
    score = 0

    for idx, quiz in enumerate(st.session_state.quiz_list):
        st.markdown(f"**Q{idx + 1}. {quiz['question']}**")
        choice = st.radio(
            f"선택하세요:",
            quiz["options"],
            key=f"quiz_{idx}"
        )
        user_answers.append(choice)

    if st.button("정답 제출"):
        st.subheader("📊 결과")
        for idx, quiz in enumerate(st.session_state.quiz_list):
            correct = quiz["options"][int(quiz["answer"]) - 1]
            user_choice = user_answers[idx]
            is_correct = user_choice == correct
            if is_correct:
                score += 1
                st.success(f"Q{idx+1} 정답! ✅")
            else:
                st.error(f"Q{idx+1} 오답 ❌ (정답: {correct})")

        st.markdown(f"### 🏁 총 점수: {score} / {len(st.session_state.quiz_list)}")

else:
    st.info("먼저 퀴즈를 하나 이상 추가해 주세요.")
