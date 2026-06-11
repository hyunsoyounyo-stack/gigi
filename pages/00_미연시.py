import streamlit as st

# 1. 페이지 설정 및 다크 테마 + DoL 스타일 CSS 주입
st.set_page_config(page_title="포트마피아 내부 상황", layout="centered")

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
    
    /* 대사가 들어가는 안내 상자를 어두운 회색조로 커스텀 */
    div[data-testid="stNotification"] {
        background-color: #1a1a1a !important;
        border: 1px solid #333333 !important;
        border-radius: 5px;
    }
    
    /* [CRITICAL] 스트림릿 버튼을 DoL 스타일의 텍스트 링크로 커스텀 */
    div.stButton > button {
        background-color: transparent !important;
        color: #e0e0e0 !important;
        border: none !important;
        padding: 4px 0px !important;
        font-size: 16px !important;
        text-align: left !important;
        display: block !important;
        box-shadow: none !important;
        transition: color 0.2s ease;
    }
    
    /* 마우스를 올렸을 때 분홍색으로 변하고 밑줄이 생김 (DoL 링크 스타일) */
    div.stButton > button:hover {
        color: #FF69B4 !important;
        background-color: transparent !important;
        text-decoration: underline !important;
    }
    
    /* 버튼 클릭 시 회색 잔상 제거 */
    div.stButton > button:active, div.stButton > button:focus {
        background-color: transparent !important;
        color: #FF69B4 !important;
        box-shadow: none !important;
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
    st.markdown("### PORT MAFIA")
    st.write("---")
    st.markdown("#### 공략 대상")
    st.subheader("기시 유스케")
    
    # 분홍색 하트 호감도
    st.markdown(f"**호감도:** {pink_style.format(st.session_state.love_point)}", unsafe_allow_html=True)
    st.write("---")
    
    if st.button("처음부터 다시 시작"):
        st.session_state.stage = 1
        st.session_state.love_point = 0
        st.session_state.selected_choice_1 = None
        st.rerun()

# 4. 메인 스토리 영역
st.title("문호 스트레이독스: 포트 마피아 내부")
st.write("---")

# ==========================================================
# STAGE 1: 오프닝 씬 (지하 입구 조우)
# ==========================================================
if st.session_state.stage == 1:
    st.write("당신은 포트 마피아 지하의 스산한 입구에 서 있습니다. 처음으로 발을 내딛은 이곳은 낯설기만 합니다.")
    st.write("그때, 당신의 앞으로 천을 뒤집어 쓴 형체가 나타납니다.")
    
    st.write("")
    if st.button("> 다음"):
        st.session_state.stage = 2
        st.rerun()

# ==========================================================
# STAGE 2: 첫 번째 선택지 분기 (DoL 텍스트 스타일)
# ==========================================================
elif st.session_state.stage == 2:
    st.write("당신의 눈앞에 나타난 정체불명의 형체. 일촉즉발의 상황에서 당신은 어떻게 행동하시겠습니까?")
    st.write("")
    
    # DoL 게임처럼 세로로 나열되는 텍스트 링크형 선택지
    if st.button("> 겁에 질려 팔을 휘적인다."):
        st.session_state.love_point -= 10
        st.session_state.selected_choice_1 = 1
        st.session_state.stage = 3
        st.rerun()
        
    if st.button("> 깜짝 놀라 몸을 굳힌다."):
        st.session_state.selected_choice_1 = 2
        st.session_state.stage = 3
        st.rerun()
        
    if st.button('> "안녕?" 태연하게 인사한다.'):
        st.session_state.selected_choice_1 = 3
        st.session_state.stage = 3
        st.rerun()

# ==========================================================
# STAGE 3: 선택지에 따른 유스케의 반응
# ==========================================================
elif st.session_state.stage == 3:
    if st.session_state.selected_choice_1 == 1:
        st.write("당신이 겁에 질려 팔을 휘두르자, 천을 쓴 형체가 뒤로 한 발자국 물러납니다.")
        st.markdown(pink_sub_text.format("(기시 유스케의 호감도가 -10 되었습니다.)"), unsafe_allow_html=True)
        st.write("")
        st.info("기시 유스케: (대사)")
        
    elif st.session_state.selected_choice_1 == 2:
        st.write("몸이 굳어버린 당신을 향해, 천을 쓴 형체가 가만히 시선을 던집니다.")
        st.markdown(pink_sub_text.format("(호감도 변동 없음)"), unsafe_allow_html=True)
        st.write("")
        st.info("기시 유스케: (대사)")
        
    elif st.session_state.selected_choice_1 == 3:
        st.write("스산한 지하 마피아 본부에서 쾌활하게 인사를 던지자, 상대방이 어이없다는 듯 멈칫합니다.")
        st.markdown(pink_sub_text.format("(호감도 변동 없음)"), unsafe_allow_html=True)
        st.write("")
        st.info("기시 유스케: (대사)")

    st.write("---")
    if st.button("> 상황 계속 진행하기"):
        st.session_state.stage = 4
        st.rerun()

# ==========================================================
# STAGE 4: 두 번째 상황 (사용자 직접 작성용)
# ==========================================================
elif st.session_state.stage == 4:
    st.write("(다음 포트 마피아 내부 상황 묘사를 이곳에 적어주세요.)")
    
    st.info("기시 유스케: (대사)")
    st.write("")
    
    # 아래 선택지들도 동일하게 텍스트 링크 스타일로 출력됩니다.
    if st.button("> (선택지 4)"):
        st.session_state.love_point += 10
        st.session_state.stage = 5
        st.rerun()
        
    if st.button("> (선택지 5)"):
        st.session_state.love_point += 5
        st.session_state.stage = 5
        st.rerun()

# ==========================================================
# STAGE 5: 세 번째 상황
# ==========================================================
elif st.session_state.stage == 5:
    st.write("(그 이후의 상황 묘사를 이곳에 적어주세요.)")
    
    st.info("기시 유스케: (대사)")
    st.write("")
    
    if st.button("> 다음 상황으로"):
        st.write("스토리가 준비 중입니다.")
