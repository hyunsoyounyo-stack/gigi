import streamlit as st

# 1. 페이지 설정 및 다크 테마 CSS 주입
st.set_page_config(page_title="포트마피아 연애 시뮬레이션", layout="centered")

# 화면 전체를 검은색 배경, 글자를 흰색/연분홍색으로 강제하는 CSS
st.markdown("""
    <style>
    /* 메인 화면 및 사이드바 배경을 검은색으로 */
    .stApp, [data-testid="stSidebar"] {
        background-color: #0b0b0b !important;
        color: #e0e0e0 !important;
    }
    
    /* 모든 텍스트 기본 색상을 밝은 회색으로 */
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #e0e0e0 !important;
        font-family: 'Noto Sans KR', sans-serif;
    }
    
    /* 대사가 들어가는 안내 상자(st.info)를 마피아 분위기의 어두운 회색조로 커스텀 */
    div[data-testid="stNotification"] {
        background-color: #1a1a1a !important;
        border: 1px solid #FF69B4 !important; /* 분홍색 테두리로 포인트 */
        border-radius: 5px;
    }
    
    /* 구분선 색상 변경 */
    hr {
        border-color: #333333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 분홍색 호감도 텍스트 스타일
pink_style = '<span style="color: #FF69B4; font-weight: bold; font-size: 28px; text-shadow: 0 0 10px #FF69B4;">♥ {}</span>'
pink_sub_text = '<span style="color: #FFBBCC; font-style: italic;">{}</span>'

# 2. 세션 상태(Session State) 변수 초기화
if "stage" not in st.session_state:
    st.session_state.stage = 1
if "love_point" not in st.session_state:
    st.session_state.love_point = 0
if "selected_choice_1" not in st.session_state:
    st.session_state.selected_choice_1 = None

# 3. 사이드바 - 기시 유스케의 호감도 표시 영역
with st.sidebar:
    st.markdown("### 🏢 PORT MAFIA")
    st.write("---")
    st.markdown("#### [ 공략 대상 ]")
    st.subheader("기시 유스케")
    
    # 네온 사인이 빛나는 듯한 분홍색 하트 호감도
    st.markdown(f"**호감도:** {pink_style.format(st.session_state.love_point)}", unsafe_allow_html=True)
    st.write("---")
    
    if st.button("🔄 처음부터 다시 시작"):
        st.session_state.stage = 1
        st.session_state.love_point = 0
        st.session_state.selected_choice_1 = None
        st.rerun()

# 4. 메인 스토리 영역
st.title("💼 문호 스트레이독스: 포트 마피아 내부")
st.write("---")

# ==========================================================
# STAGE 1: 오프닝 씬 (지하 입구 조우)
# ==========================================================
if st.session_state.stage == 1:
    st.subheader("⚠️ 마피아 지하의 조우")
    
    st.write("당신은 포트 마피아 지하의 스산한 입구에 서 있습니다. 처음으로 발을 내딛은 이곳은 낯설기만 합니다.")
    st.write("그때, 당신의 앞으로 천을 뒤집어 쓴 형체가 나타납니다.")
    
    st.write("")
    if st.button("다음 ➡️"):
        st.session_state.stage = 2
        st.rerun()

# ==========================================================
# STAGE 2: 첫 번째 선택지 분기
# ==========================================================
elif st.session_state.stage == 2:
    st.subheader("❓ 당신의 반응은?")
    st.write("당신의 눈앞에 나타난 정체불명의 형체. 일촉즉발의 상황에서 당신은 어떻게 행동하시겠습니까?")
    st.write("")
    
    # 세 가지 선택지 버튼
    if st.button("1. 겁에 질려 팔을 휘적인다"):
        st.session_state.love_point -= 10
        st.session_state.selected_choice_1 = 1
        st.session_state.stage = 3
        st.rerun()
        
    if st.button("2. 깜짝 놀라 몸을 굳힌다"):
        st.session_state.selected_choice_1 = 2
        st.session_state.stage = 3
        st.rerun()
        
    if st.button('3. "안녕?" 태연하게 인사한다.'):
        st.session_state.selected_choice_1 = 3
        st.session_state.stage = 3
        st.rerun()

# ==========================================================
# STAGE 3: 선택지에 따른 유스케의 반응
# ==========================================================
elif st.session_state.stage == 3:
    st.subheader("👁️ 기시 유스케의 반응")
    
    if st.session_state.selected_choice_1 == 1:
        st.write("당신이 겁에 질려 팔을 휘두르자, 천을 쓴 형체가 뒤로 한 발자국 물러납니다.")
        st.markdown(pink_sub_text.format("*(기시 유스케의 호감도가 -10 되었습니다.)*"), unsafe_allow_html=True)
        st.write("")
        # 📝 대사 입력 칸
        st.info("기시 유스케: (대사)")
        
    elif st.session_state.selected_choice_1 == 2:
        st.write("몸이 굳어버린 당신을 향해, 천을 쓴 형체가 가만히 시선을 던집니다.")
        st.markdown(pink_sub_text.format("*(호감도 변동 없음)*"), unsafe_allow_html=True)
        st.write("")
        # 📝 대사 입력 칸
        st.info("기시 유스케: (대사)")
        
    elif st.session_state.selected_choice_1 == 3:
        st.write("스산한 지하 마피아 본부에서 쾌활하게 인사를 던지자, 상대방이 어이없다는 듯 멈칫합니다.")
        st.markdown(pink_sub_text.format("*(호감도 변동 없음)*"), unsafe_allow_html=True)
        st.write("")
        # 📝 대사 입력 칸
        st.info("기시 유스케: (대사)")

    st.write("---")
    if st.button("상황 계속 진행하기 ➡️"):
        st.session_state.stage = 4
        st.rerun()

# ==========================================================
# STAGE 4: 두 번째 상황 (사용자 직접 작성용)
# ==========================================================
elif st.session_state.stage == 4:
    st.subheader("👣 다음 구역으로")
    
    st.write("(다음 포트 마피아 내부 상황 묘사를 이곳에 적어주세요.)")
    
    # 📝 대사 입력 칸
    st.info("기시 유스케: (대사)")
    
    st.write("당신의 선택은?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("(선택지 4)"):
            st.session_state.love_point += 10  # 👈 호감도 수치 수정
            st.session_state.stage = 5
            st.rerun()
            
    with col2:
        if st.button("(선택지 5)"):
            st.session_state.love_point += 5   # 👈 호감도 수치 수정
            st.session_state.stage = 5
            st.rerun()

# ==========================================================
# STAGE 5: 최종 엔딩 확인
# ==========================================================
elif st.session_state.stage == 5:
    st.subheader("치명적인 결과")
    st.write("기시 유스케와의 긴장감 넘치는 만남이 끝났습니다.")
    
    if st.session_state.love_point >= 0:
        st.success("🎉 엔딩: 기시 유스케가 당신에게 깊은 흥미를 보입니다.")
        st.info("기시 유스케: (대사)")
    else:
        st.error("🩸 엔딩: 기시 유스케의 시선이 차갑게 식어 내립니다.")
        st.info("기시 유스케: (대사)")
