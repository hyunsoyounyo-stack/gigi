import streamlit as st

# 1. 페이지 설정 및 다크 테마 + DoL 블루 링크 스타일 CSS 주입
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
    
    /* 선택지 버튼을 DoL 스타일의 기본 파란색 글씨로 강력 고정 */
    div.stButton > button {
        background-color: transparent !important;
        color: #4a90e2 !important;
        border: none !important;
        padding: 4px 0px !important;
        font-size: 16px !important;
        text-align: left !important;
        display: block !important;
        box-shadow: none !important;
        transition: color 0.2s ease;
    }
    
    /* 마우스를 올렸을 때 (더 밝은 파란색 + 밑줄) */
    div.stButton > button:hover {
        color: #70a1ff !important;
        background-color: transparent !important;
        text-decoration: underline !important;
    }
    
    /* 버튼 클릭 시 또는 포커스 시 잔상 방지 및 색상 유지 */
    div.stButton > button:active, div.stButton > button:focus {
        background-color: transparent !important;
        color: #4a90e2 !important;
        box-shadow: none !important;
    }
    
    /* 구분선 색상 변경 */
    hr {
        border-color: #333333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 세션 상태(Session State) 변수 초기화
if "stage" not in st.session_state:
    st.session_state.stage = 1
if "love_point" not in st.session_state:
    st.session_state.love_point = 0
if "selected_choice_1" not in st.session_state:
    st.session_state.selected_choice_1 = None

# 3. 사이드바 - 기시 유스케의 호감도 표시 영역 (가로 막대바 커스텀)
with st.sidebar:
    st.markdown("### PORT MAFIA")
    st.write("---")
    st.markdown("#### 공략 대상")
    st.subheader("기시 유스케")
    
    # --- 가로형 양방향 호감도 막대바 연출 ---
    lp = st.session_state.love_point
    # 값 제한 (-100 ~ 100)
    lp = max(-100, min(100, lp))
    
    # HTML/CSS 기반 양방향 게이지 바 생성
    if lp >= 0:
        left_space = 50
        bar_width = (lp / 100) * 50
        bar_color = "#FF69B4"
        shadow_color = "#FF69B4"
    else:
        bar_width = (abs(lp) / 100) * 50
        left_space = 50 - bar_width
        bar_color = "#4a90e2"
        shadow_color = "#4a90e2"

    gauge_html = f"""
    <div style="margin-bottom: 5px; font-size: 14px; font-weight: bold; color: #e0e0e0;">
        호감도: <span style="color: {bar_color}; text-shadow: 0 0 5px {shadow_color};">{st.session_state.love_point}</span>
    </div>
    <div style="width: 100%; background-color: #222; height: 12px; border-radius: 6px; position: relative; overflow: hidden; border: 1px solid #444;">
        <div style="position: absolute; left: 50%; top: 0; width: 2px; height: 100%; background-color: #555; z-index: 2;"></div>
        <div style="position: absolute; left: {left_space}%; width: {bar_width}%; height: 100%; background-color: {bar_color}; box-shadow: 0 0 8px {shadow_color}; transition: all 0.5s ease; z-index: 1;"></div>
    </div>
    """
    st.markdown(gauge_html, unsafe_allow_html=True)
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
# STAGE 1: 오프닝 서술
# ==========================================================
if st.session_state.stage == 1:
    st.write("당신은 요코하마의 밤을 지배하는 잔혹한 조직, 포트 마피아의 말단 신입입니다.")
    st.write("조직에 들어온 지 얼마 되지 않아 업무가 서툴고 기가 약하다는 이유로, 당신은 악질적인 선배들의 표적이 되었습니다. 그들은 킥킥거리며 아무도 가기 꺼려하는 본부 건물의 가장 깊숙한 지하 통로로 당신을 떠밀었습니다. 제대로 된 손전등 하나 쥐어주지 않은 채로 말입니다.")
    st.write("포트 마피아의 지하는 소문대로 차갑고 스산한 공기로 가득 차 있습니다. 웅웅거리는 낡은 환풍기 소리만이 불길하게 울려 퍼지고, 사방의 콘크리트 벽에서는 원인 모를 습기와 곰팡이 냄새, 그리고 어딘지 모르게 비릿한 피비린내가 배어 나오는 것만 같습니다.")
    st.write("발을 내딛을 때마다 구두 굽 소리가 기괴하게 메아리치고, 발목을 타고 올라오는 오한에 당신은 저절로 옷깃을 여미며 몸을 웅크립니다. 뒤를 돌아보아도 이미 빛은 사라진 지 오래, 칠흑 같은 어둠만이 삼킬 듯이 도사리고 있습니다.")
    st.write("심장이 터질 것처럼 쿵쾅거리던 바로 그때, 저 멀리 짙은 어둠 속에서 무언가가 이쪽을 향해 소리도 없이, 급작스럽고 빠르게 다가오기 시작합니다!")
    
    st.write("")
    if st.button("> 다음"):
        st.session_state.stage = 2
        st.rerun()

# ==========================================================
# STAGE 2: 이어지는 연출 (귀신 조우)
# ==========================================================
elif st.session_state.stage == 2:
    st.write("숨이 턱 막히는 공포 속에서 흐릿한 시야를 간신히 넓혀봅니다. 눈앞까지 다가온 것은 다름 아닌 허공을 일렁이는 거대한 하얀 천이었습니다.")
    st.write("귀신? 아니면 악명 높은 포트 마피아의 잔혹한 이능력자일까요? 이 어두운 지하에서 마주친 이질적인 존재에 온몸의 털이 곤두섭니다.")
    st.write("")
    
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
        st.write("당신이 겁에 질려 비명을 지르며 마구 팔을 휘두르자, 하얀 천을 쓴 형체가 예상치 못한 움직임에 멈칫하더니 뒤로 한 발자국 물러납니다. 천 너머에서 작은 한숨소리가 들려오는 것만 같습니다. 사람?")
        st.write("")
        st.write('"하아...... 신입? 멋대로 움직이지마, 진짜 귀신이라도 나올지 모르잖아?"')
        st.write("")
        st.write("상대를 귀신으로 착각한 속내를 들킨 것만 같아 심장이 콩닥콩닥해졌습니다.")
        
    elif st.session_state.selected_choice_1 == 2:
        st.write("공포에 질려 손가락 하나 움직이지 못하고 몸이 완전히 굳어버린 당신. 천을 쓴 수수께끼의 형체는 그런 당신의 앞에 우뚝 서서 가만히 시선을 던집니다.")
        st.write("")
        st.write('"(여기에 2번 대사를 입력하세요)"')
        
    elif st.session_state.selected_choice_1 == 3:
        st.write("공포를 이겨내고, 스산한 마피아 지하 통로에 어울리지 않는 태연하고 쾌활한 인사를 건넵니다. 그러자 백색의 형체가 어이없다는 듯 그 자리에 뚝 멈춰 섭니다.")
        st.write("")
        st.write('"(여기에 3번 대사를 입력하세요)"')

    st.write("---")
    # 🛠️ 이 부분 끝에 콜론(:)을 넣어 정상적으로 수정했습니다.
    if st.button("> 상황 계속 진행하기"):
        st.session_state.stage = 4
        st.rerun()

# ==========================================================
# STAGE 4: 두 번째 상황 (사용자 직접 작성용)
# ==========================================================
elif st.session_state.stage == 4:
    st.write("(다음 포트 마피아 내부 상황 묘사를 이곳에 적어주세요.)")
    st.write("")
    st.write('"(대사)"')
    st.write("")
    
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
# =
