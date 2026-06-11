import streamlit as st

# 1. 페이지 기본 설정 및 분홍색 호감도 스타일 적용
st.set_page_config(page_title="포트마피아 연애 시뮬레이션", layout="centered")

# 분홍색 텍스트를 위한 CSS 스타일 선언
pink_text = '<span style="color: #FF69B4; font-weight: bold;">{}</span>'

# 2. 게임 시스템 데이터 초기화 (새로고침해도 유지되도록 세션 스테이트 사용)
if "stage" not in st.session_state:
    st.session_state.stage = 1
if "love_point" not in st.session_state:
    st.session_state.love_point = 0

# 3. 사이드바 - 호감도 표시 영역 (분홍색 강조)
with st.sidebar:
    st.header("💘 공략 대상 정보")
    st.subheader("이름: 기시 유스케")
    # 분홍색으로 호감도 표시
    st.markdown(f"**현재 호감도:** {pink_text.format(f'♥ {st.session_state.love_point}')}", unsafe_allow_html=True)
    
    # 테스트용 초기화 버튼
    if st.button("게임 처음부터 다시 하기"):
        st.session_state.stage = 1
        st.session_state.love_point = 0
        st.rerun()

# 4. 메인 스토리 전개 영역
st.title("💼 문호 스트레이독스: 포트 마피아 내부")
st.write("---")

# --- [STAGE 1: 게임의 시작] ---
if st.session_state.stage == 1:
    st.subheader("마피아 본부의 어느 날")
    
    # 📝 상황 묘사를 적어주세요
    st.write("포트 마피아 본부의 어두운 복도. 저 멀리서 기시 유스케가 걸어온다.")
    
    # 📝 유스케의 대사를 적어주세요
    st.info("기시 유스케: (여기에 유스케의 대사를 입력하세요.)")
    
    st.write("당신의 선택은?")
    
    # 📝 선택지와 호감도 상승 수치를 수정하세요
    col1, col2 = st.columns(2)
    with col1:
        if st.button("(선택지 1을 입력하세요)"):
            st.session_state.love_point += 10  # 👈 늘어날 호감도 수치 수정 (예: +10)
            st.session_state.stage = 2
            st.rerun()
            
    with col2:
        if st.button("(선택지 2를 입력하세요)"):
            st.session_state.love_point += 5   # 👈 늘어날 호감도 수치 수정 (예: +5)
            st.session_state.stage = 2
            st.rerun()

# --- [STAGE 2: 다음 상황] ---
elif st.session_state.stage == 2:
    st.subheader("깊어지는 대화")
    
    # 📝 상황 묘사를 적어주세요
    st.write("당신의 반응에 기시 유스케는 잠시 눈을 가늘게 뜨더니, 이내 옅은 미소를 지었다.")
    
    # 📝 유스케의 대사를 적어주세요
    st.info("기시 유스케: (여기에 두 번째 유스케의 대사를 입력하세요.)")
    
    st.write("당신의 선택은?")
    
    # 📝 선택지와 호감도 상승 수치를 수정하세요
    col1, col2 = st.columns(2)
    with col1:
        if st.button("(선택지 3을 입력하세요)"):
            st.session_state.love_point += 20  # 👈 호감도 수치 수정
            st.session_state.stage = 3
            st.rerun()
            
    with col2:
        if st.button("(선택지 4을 입력하세요)"):
            st.session_state.love_point += 0   # 👈 호감도 수치 수정
            st.session_state.stage = 3
            st.rerun()

# --- [STAGE 3: 엔딩 조건 체크] ---
elif st.session_state.stage == 3:
    st.subheader("결과")
    st.write("기시 유스케와의 짧은 만남이 끝났다.")
    
    # 호감도 기준에 따른 엔딩 분기 (기준 점수는 마음대로 수정 가능)
    if st.session_state.love_point >= 25:
        st.success("🎉 엔딩: 기시 유스케의 호감을 얻는 데 성공했습니다!")
        st.write("기시 유스케: (해피엔딩 대사 입력)")
    else:
        st.error("😢 엔딩: 기시 유스케는 차가운 시선을 남긴 채 돌아섰습니다.")
        st.write("기시 유스케: (노말/배드엔딩 대사 입력)")
