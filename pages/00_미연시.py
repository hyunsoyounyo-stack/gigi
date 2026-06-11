import streamlit as st

# 1. 페이지 기본 설정 및 분홍색 호감도 스타일 정의
st.set_page_config(page_title="포트마피아 연애 시뮬레이션", layout="centered")

# 분홍색 텍스트를 표현하기 위한 HTML 스타일 (사이드바용)
pink_style = '<span style="color: #FF1493; font-weight: bold; font-size: 26px;">♥ {}</span>'

# 2. 세션 상태(Session State) 변수 초기화
if "stage" not in st.session_state:
    st.session_state.stage = 1
if "love_point" not in st.session_state:
    st.session_state.love_point = 0
if "selected_choice_1" not in st.session_state:
    st.session_state.selected_choice_1 = None  # 첫 번째 선택지 저장용

# 3. 사이드바 - 기시 유스케의 호감도 표시 영역
with st.sidebar:
    st.header("💖 공략 대상")
    st.subheader("이름: 기시 유스케")
    # 분홍색 하트와 함께 호감도 수치 출력
    st.markdown(f"**호감도:** {pink_style.format(st.session_state.love_point)}", unsafe_allow_html=True)
    st.write("---")
    
    # 디버깅/재시작 버튼
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
    st.subheader("마피아 지하의 조우")
    
    # 요청하신 첫 번째 대사(상황 묘사)
    st.write("당신은 포트 마피아 지하의 스산한 입구에 서 있습니다. 처음으로 발을 내딛은 이곳은 낯설기만 합니다.")
    st.write("그때, 당신의 앞으로 천을 뒤집어 쓴 형체가 나타납니다.")
    
    # 다음 버튼을 누르면 선택지가 있는 STAGE 2로 이동합니다.
    if st.button("다음 ➡️"):
        st.session_state.stage = 2
        st.rerun()

# ==========================================================
# STAGE 2: 첫 번째 선택지 분기
# ==========================================================
elif st.session_state.stage == 2:
    st.subheader("당신의 반응은?")
    st.write("당신의 눈앞에 나타난 정체불명의 형체. 일촉즉발의 상황에서 당신은 어떻게 행동하시겠습니까?")
    
    # 세 가지 선택지 버튼 생성
    if st.button("1. 겁에 질려 팔을 휘적인다"):
        st.session_state.love_point -= 10  # 첫 번째 선택지만 호감도 -10
        st.session_state.selected_choice_1 = 1
        st.session_state.stage = 3
        st.rerun()
        
    if st.button("2. 깜짝 놀라 몸을 굳힌다"):
        # 호감도 변동 없음 (+0)
        st.session_state.selected_choice_1 = 2
        st.session_state.stage = 3
        st.rerun()
        
    if st.button('3. "안녕?" 태연하게 인사한다.'):
        # 호감도 변동 없음 (+0)
        st.session_state.selected_choice_1 = 3
        st.session_state.stage = 3
        st.rerun()

# ==========================================================
# STAGE 3: 선택지에 따른 유스케의 반응 및 대사 작성 칸
# ==========================================================
elif st.session_state.stage == 3:
    st.subheader("기시 유스케의 반응")
    
    if st.session_state.selected_choice_1 == 1:
        st.write("당신이 겁에 질려 팔을 휘두르자, 천을 쓴 형체가 뒤로 한 발자국 물러납니다.")
        st.write("*(기시 유스케의 호감도가 <span style='color:red;'>-10</span> 되었습니다.)*", unsafe_allow_html=True)
        
        # 📝 1번 선택지를 골랐을 때 유스케의 대사를 적어주세요
        st.info("기시 유스케: (대사)")
        
    elif st.session_state.selected_choice_1 == 2:
        st.write("몸이 굳어버린 당신을 향해, 천을 쓴 형체가 가만히 시선을 던집니다.")
        st.write("*(호감도 변동 없음)*")
        
        # 📝 2번 선택지를 골랐을 때 유스케의 대사를 적어주세요
        st.info("기시 유스케: (대사)")
        
    elif st.session_state.selected_choice_1 == 3:
        st.write("스산한 지하 마피아 본부에서 쾌활하게 인사를 던지자, 상대방이 어이없다는 듯 멈칫합니다.")
        st.write("*(호감도 변동 없음)*")
        
        # 📝 3번 선택지를 골랐을 때 유스케의 대사를 적어주세요
        st.info("기시 유스케: (대사)")

    st.write("---")
    if st.button("상황 계속 진행하기 ➡️"):
        st.session_state.stage = 4
        st.rerun()

# ==========================================================
# STAGE 4: 두 번째 상황 (사용자 직접 작성용)
# ==========================================================
elif st.session_state.stage == 4:
    st.subheader("다음 구역으로")
    
    # 📝 다음 상황에 대한 묘사를 적어주세요
    st.write("(다음 포트 마피아 내부 상황 묘사를 이곳에 적어주세요.)")
    
    # 📝 기시 유스케의 다음 대사를 적어주세요
    st.info("기시 유스케: (대사)")
    
    st.write("당신의 선택은?")
    
    col1, col2 = st.columns(2)
    with col1:
        # 📝 선택지 제목과 늘릴 호감도 수치(+10 등)를 직접 수정하실 수 있습니다.
        if st.button("(선택지 4)"):
            st.session_state.love_point += 10  # 👈 호감도 조절
            st.session_state.stage = 5
            st.rerun()
            
    with col2:
        if st.button("(선택지 5)"):
            st.session_state.love_point += 5   # 👈 호감도 조절
            st.session_state.stage = 5
            st.rerun()

# ==========================================================
# STAGE 5: 최종 엔딩 확인 및 정산
# ==========================================================
elif st.session_state.stage == 5:
    st.subheader("결과 확인")
    st.write("기시 유스케와의 오늘의 만남이 마무리되었습니다.")
    
    # 성공 기준선 설정 (예: 0점 이상 시 성공, 마이너스 시 실패)
    if st.session_state.love_point >= 0:
        st.success("🎉 성공 엔딩: 기시 유스케가 당신에게 흥미를 보입니다.")
        st.write("기시 유스케: (대사)")
    else:
        st.error("😢 실패 엔딩: 기시 유스케가 깊은 한숨을 쉬며 멀어집니다.")
        st.write("기시 유스케: (대사)")
