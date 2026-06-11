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
    
    /* 입력창 및 선택 상자(Selectbox) 배경 다크톤 조절 */
    div[data-testid="stTextInput"] input, div[data-testid="stSelectbox"] div[data-baseweb="select"] {
        background-color: #1a1a1a !important;
        color: #e0e0e0 !important;
        border: 1px solid #444 !important;
    }
    
    /* 구분선 색상 변경 */
    hr {
        border-color: #333333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 세션 상태(Session State) 변수 초기화
if "stage" not in st.session_state:
    st.session_state.stage = 0  # 0번 스테이지: 캐릭터 설정 화면
if "player_name" not in st.session_state:
    st.session_state.player_name = "신입"

# 외형 관련 세션 변수
if "hair_color" not in st.session_state:
    st.session_state.hair_color = "흑발"
if "hair_length" not in st.session_state:
    st.session_state.hair_length = "단발"
if "eye_color" not in st.session_state:
    st.session_state.eye_color = "흑안"

if "love_point" not in st.session_state:
    st.session_state.love_point = 0
if "selected_choice_1" not in st.session_state:
    st.session_state.selected_choice_1 = None

# RPG 시스템 변수 초기화
if "stats" not in st.session_state:
    st.session_state.stats = {"외모": 50, "정신력": 50, "체력": 50, "입담": 50, "전투": 50}
if "inventory" not in st.session_state:
    st.session_state.inventory = ["조직원 배지", "동전 몇 개"]


# 3. 사이드바 - 캐릭터 프로필 / 호감도 / 스탯 / 인벤토리 영역
with st.sidebar:
    st.markdown("### PLAYER STATUS")
    st.markdown(f"**이름:** {st.session_state.player_name}")
    st.markdown(f"**외형:** {st.session_state.hair_color} / {st.session_state.hair_length} / {st.session_state.eye_color}")
    st.write("---")
    
    # 공략 대상 및 호감도 막대바
    st.markdown("#### 공략 대상: 기시 유스케")
    lp = st.session_state.love_point
    lp = max(-100, min(100, lp))
    
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
    <div style="margin-bottom: 5px; font-size: 13px; font-weight: bold; color: #e0e0e0;">
        호감도: <span style="color: {bar_color}; text-shadow: 0 0 5px {shadow_color};">{st.session_state.love_point}</span>
    </div>
    <div style="width: 100%; background-color: #222; height: 10px; border-radius: 5px; position: relative; overflow: hidden; border: 1px solid #444; margin-bottom: 20px;">
        <div style="position: absolute; left: 50%; top: 0; width: 2px; height: 100%; background-color: #555; z-index: 2;"></div>
        <div style="position: absolute; left: {left_space}%; width: {bar_width}%; height: 100%; background-color: {bar_color}; box-shadow: 0 0 8px {shadow_color}; z-index: 1;"></div>
    </div>
    """
    st.markdown(gauge_html, unsafe_allow_html=True)
    st.write("---")
    
    # 5대 스탯창 구현
    st.markdown("#### 보유 스탯")
    
    def render_stat_bar(stat_name, value, color):
        val = max(0, min(100, value))
        stat_html = f"""
        <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 2px; color: #ccc;">
            <span>{stat_name}</span>
            <span style="font-weight: bold; color: {color};">{val} / 100</span>
        </div>
        <div style="width: 100%; background-color: #1a1a1a; height: 6px; border-radius: 3px; border: 1px solid #333; margin-bottom: 10px; overflow: hidden;">
            <div style="width: {val}%; height: 100%; background-color: {color};"></div>
        </div>
        """
        st.markdown(stat_html, unsafe_allow_html=True)

    render_stat_bar("외모", st.session_state.stats["외모"], "#da70d6")
    render_stat_bar("정신력", st.session_state.stats["정신력"], "#00bfff")
    render_stat_bar("체력", st.session_state.stats["체력"], "#32cd32")
    render_stat_bar("입담", st.session_state.stats["입담"], "#ffd700")
    render_stat_bar("전투", st.session_state.stats["전투"], "#ff4500")
    
    st.write("---")
    
    # 인벤토리 창
    st.markdown("#### 인벤토리")
    if st.session_state.inventory:
        inv_html = '<div style="display: flex; flex-wrap: wrap; gap: 5px;">'
        for item in st.session_state.inventory:
            inv_html += f'<span style="background-color: #222; color: #aaa; border: 1px solid #444; padding: 3px 8px; border-radius: 12px; font-size: 12px;">{item}</span>'
        inv_html += '</div>'
        st.markdown(inv_html, unsafe_allow_html=True)
    else:
        st.caption("비어 있음")
        
    st.write("---")
    
    # 리셋 버튼
    if st.button("처음부터 다시 시작"):
        st.session_state.stage = 0
        st.session_state.player_name = "신입"
        st.session_state.hair_color = "흑발"
        st.session_state.hair_length = "단발"
        st.session_state.eye_color = "흑안"
        st.session_state.love_point = 0
        st.session_state.selected_choice_1 = None
        st.session_state.stats = {"외모": 50, "정신력": 50, "체력": 50, "입담": 50, "전투": 50}
        st.session_state.inventory = ["조직원 배지", "동전 몇 개"]
        st.rerun()


# 4. 메인 디자인 및 스테이지 제어 영역
# ==========================================================
# STAGE 0: 시작 전 캐릭터 외형 설정창
# ==========================================================
if st.session_state.stage == 0:
    st.markdown("<h1 style='text-align: center; color: #FF69B4 !important; text-shadow: 0 0 15px rgba(255,105,180,0.5); font-size: 36px;'>문호 스트레이독스 기반 자캐 연애 시뮬레이션</h1>", unsafe_allow_html=True)
    st.write("---")
    
    st.write("포트 마피아에 입사하신 것을 환영합니다! 본 웹사이트는 포트마피아의 드림주, 기시 유스케와 연관된 미연시 게임입니다. 잘 부탁드립니다!")
    st.write("")
    
    # 캐릭터 커스텀 UI
    input_name = st.text_input("당신의 이름을 입력해 주세요", value="신입", max_chars=10)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        select_hair_color = st.selectbox(
            "머리 색", 
            ["흑발", "백발", "금발", "갈발", "은발", "적발", "청발"]
        )
    with col2:
        select_hair_length = st.selectbox(
            "머리 길이", 
            ["단발", "숏컷", "중단발", "장발", "세미롱"]
        )
    with col3:
        select_eye_color = st.selectbox(
            "눈 색", 
            ["흑안", "적안", "벽안", "자안", "녹안", "금안", "역안"]
        )
    
    st.write("")
    st.write("---")
    
    # 시작 버튼 연출
    if st.button("▶ 스토리 시작하기"):
        st.session_state.player_name = input_name
        st.session_state.hair_color = select_hair_color
        st.session_state.hair_length = select_hair_length
        st.session_state.eye_color = select_eye_color
        
        st.session_state.stats = {"외모": 50, "정신력": 50, "체력": 50, "입담": 50, "전투": 50}
        st.session_state.inventory = ["조직원 배지", "동전 몇 개"]
        st.session_state.stage = 1
        st.rerun()

# ==========================================================
# STAGE 1: 오프닝 서술
# ==========================================================
elif st.session_state.stage == 1:
    st.markdown("### 포트 마피아 내부")
    st.write("---")
    st.write(f"당신({st.session_state.player_name})은 요코하마의 밤을 지배하는 잔혹한 조직, 포트 마피아의 말단 신입입니다.")
    st.write("조직에 들어온 지 얼마 되지 않아 업무가 서툴고 기가 약하다는 이유로, 당신은 악질적인 선배들의 표적이 되었습니다. 그들은 킥킥거리며 아무도 가기 꺼려하는 본부 건물의 가장 깊숙한 지하 통로로 당신을 떠밀었습니다. 제대로 된 손전등 하나 쥐어주지 않은 채로 말입니다.")
    st.write("포트 마피아의 지하는 소문대로 차갑고 스산한 공기로 가득 차 있습니다. 웅웅거리는 낡은 환풍기 소리만이 불길하게 울려 퍼지고, 사방의 콘크리트 벽에서는 원인 모를 습기와 곰팡이 냄새, 그리고 어딘지 모르게 비릿한 피비린내가 배어 나오는 것만 같습니다.")
    
    hair_color_map = {
        "흑발": "칠흑 같은", "백발": "하얀색의", "금발": "금색의", 
        "갈발": "갈색의", "은발": "은색의", "적발": "붉은색의", "청발": "청색의"
    }
    
    h_adj = hair_color_map.get(st.session_state.hair_color, "")
    h_length = st.session_state.hair_length
    
    if h_length in ["장발", "세미롱", "중단발"]:
        hair_desc = f"어디선가 갑작스레 불어닥친 밤바람에 당신의 {h_adj} 긴 머리칼이 세차게 휘날리며 어두운 시야를 가립니다."
    else:
        hair_desc = f"어디선가 갑작스레 불어닥친 밤바람에 당신의 {h_adj} 짧은 머리끝이 거칠게 흩날립니다."
        
    st.write(f"발을 내딛을 때마다 구두 굽 소리가 기괴하게 메아리치고, 발목을 타고 올라오는 오한에 당신은 저절로 옷깃을 여미며 몸을 웅크립니다. {hair_desc} 뒤를 돌아보아도 이미 빛은 사라진 지 오래, 칠흑 같은 어둠만이 삼킬 듯이 도사리고 있습니다.")
    st.write("심장이 터질 것처럼 쿵쾅거리던 바로 그때, 저 멀리 짙은 어둠 속에서 무언가가 이쪽을 향해 소리도 없이, 급작스럽고 빠르게 다가오기 시작합니다!")
    
    st.write("")
    if st.button("> 다음"):
        st.session_state.stage = 2
        st.rerun()

# ==========================================================
# STAGE 2: 이어지는 연출 (★백발+장발+적안 이스터에그 반영★)
# ==========================================================
elif st.session_state.stage == 2:
    st.markdown("### 포트 마피아 내부")
    st.write("---")
    
    # 이스터에그 조건 판별 (백발, 장발, 적안을 모두 갖췄는가)
    is_easter_egg = (
        st.session_state.hair_color == "백발" and 
        st.session_state.hair_length == "장발" and 
        st.session_state.eye_color == "적안"
    )
    
    if is_easter_egg:
        # 이스터에그 전용 특수 서술
        st.write("순간의 당황 속에서 흐릿한 시야를 겨우 넓혀봅니다. 의문으로 잘게 떨리는 당신의 눈동자가 허공의 백색 형체를 똑바로 담아냅니다. 눈앞까지 다가온 것은 다름 아닌 허공을 일렁이는 거대한 하얀 천이었습니다. 아니, 다리가 있는 것을 보니 사람에 가까운가요? 그리고는 쿵! 눈 앞에 천과 몸을 부딪칩니다.")
        st.write("갑자기 나타난 존재에 공포보다는 당황이 밀려옵니다. 그러나, 당신은 피하지 않았고 천을 뚫어져라 바라보았습니다. 어쩐지 부딪친 쪽이 더 놀란 느낌입니다.")
    else:
        # 일반 조건용 서술
        eye_color_map = {
            "흑안": "검은색", "적안": "붉은색", "벽안": "푸른색", 
            "자안": "자색", "녹안": "녹색", "금안": "금색", 
            "역안": "기이하게 뒤틀린"
        }
        e_adj = eye_color_map.get(st.session_state.eye_color, "")
        eye_desc = f"{e_adj} 눈동자"
            
        st.write(f"숨이 턱 막히는 공포 속에서 흐릿한 시야를 간신히 넓혀봅니다. 두려움 혹은 경계심으로 잘게 떨리는 당신의 {eye_desc}가 허공의 백색 형체를 똑바로 담아냅니다. 눈앞까지 다가온 것은 다름 아닌 허공을 일렁이는 거대한 하얀 천이었습니다.")
        st.write("귀신? 아니면 악명 높은 포트 마피아의 잔혹한 이능력자일까요? 이 어두운 지하에서 마주친 이질적인 존재에 온몸의 털이 곤두섭니다.")
    
    st.write("") 
    
    if st.button("> 겁에 질려 팔을 휘적인다."):
        st.session_state.love_point -= 10
        st.session_state.stats["정신력"] -= 5
        st.session_state.selected_choice_1 = 1
        st.session_state.stage = 3
        st.rerun()
        
    if st.button("> 깜짝 놀라 몸을 굳힌다."):
        st.session_state.stats["정신력"] -= 2
        st.session_state.selected_choice_1 = 2
        st.session_state.stage = 3
        st.rerun()
        
    if st.button('> "안녕하세요." 태연하게 말 건넨다.'):
        st.session_state.stats["입담"] += 5
        st.session_state.selected_choice_1 = 3
        st.session_state.stage = 3
        st.rerun()

# ==========================================================
# STAGE 3: 선택지에 따른 유스케의 반응
# ==========================================================
elif st.session_state.stage == 3:
    st.markdown("### 포트 마피아 내부")
    st.write("---")
    if st.session_state.selected_choice_1 == 1:
        st.write("당신이 겁에 질려 팔을 마구 휘두르자, 하얀 천을 쓴 형체가 예상치 못한 움직임에 멈칫하더니 뒤로 한 발자국 물러납니다. 천 너머에서 작은 한숨소리가 들려오는 것만 같습니다. 사람?")
        st.write("")
        st.write('"하아...... 신입? 멋대로 움직이지마, 진짜 귀신이라도 나올지 모르잖아?"')
        st.write("")
        st.write("성별을 알 수 없는 목소리가 천 너머로 새어나옵니다. 상대를 귀신으로 착각한 속내를 들킨 것만 같아 당신의 심장이 심장이 콩닥콩닥해졌습니다.")
        st.session_state.stats["정신력"] -= 5
        
    elif st.session_state.selected_choice_1 == 2:
        st.write("갑작스런 상황에 반응도 못하고 멈췄습니다. 큭, 기분 나쁘게 웃는 소리가 들립니다.")
        st.write("")
        st.write("한참의 대치가 계속됩니다. 자세히 보니 사람......? 사람인 것 같습니다. 정장을 입은 멀끔한 두 다리가 땅을 딛고 서 있는 모습이 똑똑히 망막에 맺힙니다.")
        st.write("")
        st.write('"놀랐어? 처음보네, 신입인가봐?"')
        st.write("")
        st.write("성별을 알 수 없는 목소리가 천 너머로 새어나옵니다. 목소리에는 즐거움이 잔뜩 묻어있는 것 같습니다. 이 사람은 사람을 놀래키는 게 재미있는 걸까요?")
        
    elif st.session_state.selected_choice_1 == 3:
        st.write("딱히 놀라지도 않았습니다. 아니, 그저 별 생각이 없었다는 것에 가까웠던 것 같습니다. 사람을 보면 인사를 해야하기 때문에, 어색한 상황에서 먼저 입을 열어 말을 건네었습니다")
        st.write("")
        st.write('"안녕하세요."')
        st.write("허? 어이없다는 듯한 작은 숨소리가 천 너머로 새어나옵니다.")
        st.write("")
        st.write('"......넌 무슨, 놀라지도 않아?"')
        st.write("")
        st.write("성별을 알 수 없는 목소리가 천 너머로 새어나왔습니다. 그런데, 그게 중요한가요?")

    st.write("---")
    if st.button("> 상황 계속 진행하기"):
        st.session_state.stage = 4
        st.rerun()

# ==========================================================
# STAGE 4: 두 번째 상황 (사용자 직접 작성용)
# ==========================================================
elif st.session_state.stage == 4:
    st.markdown("### 포트 마피아 내부")
    st.write("---")
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
# ==========================================================
elif st.session_state.stage == 5:
    st.markdown("### 포트 마피아 내부")
    st.write("---")
    st.write("(그 이후의 상황 묘사를 이곳에 적어주세요.)")
    st.write("")
    st.write('"(대사)"')
    st.write("")
    
    if st.button("> 다음 상황으로"):
        st.write("스토리가 준비 중입니다.")
