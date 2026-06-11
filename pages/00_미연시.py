import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="포트마피아 내부 이야기", page_icon="🍷", layout="centered")

# --- 1. 게임 데이터 설정 (이 부분을 수정하여 이야기를 전개하세요) ---
# [가이드]
# "상황": "보여줄 배경 설명 및 상황 기술"
# "대사": "캐릭터가 할 말 (빈칸으로 수정 가능)"
# "선택지": 각 버튼에 들어갈 문구와 선택 시 이동할 다음 장면(next), 그리고 증가할 호감도(호감도 변수명, 수치)
GAME_DATA = {
    "시작": {
        "상황": "포트마피아 본부 건물의 어두운 복도. 기시 유스케는 상부의 부름을 받고 집무실 앞으로 향하고 있다. 문 너머로 무거운 공기가 흘러나온다.",
        "대사": "(대사)",
        "선택지": [
            {"문구": "(선택지 1)", "next": "장면_A", "호감도_타겟": "다자이", "호감도_증가": 5},
            {"문구": "(선택지 2)", "next": "장면_B", "호감도_타겟": "츄야", "호감도_증가": 10}
        ]
    },
    "장면_A": {
        "상황": "장면 A에 대한 상황을 여기에 적으세요. 다자이와 마주친 상황 등...",
        "대사": "(대사)",
        "선택지": [
            {"문구": "(선택지 A-1)", "next": "시작", "호감도_타겟": "다자이", "호감도_증가": 0}
        ]
    },
    "장면_B": {
        "상황": "장면 B에 대한 상황을 여기에 적으세요. 츄야와 마주친 상황 등...",
        "대사": "(대사)",
        "선택지": [
            {"문구": "(선택지 B-1)", "next": "시작", "호감도_타겟": "츄야", "호감도_증가": 0}
        ]
    }
}

# --- 2. 시스템 초기화 ---
if "current_scene" not in st.session_state:
    st.session_state.current_scene = "시작"

if "love_meters" not in st.session_state:
    # 게임에 등장시킬 캐릭터들의 초기 호감도 설정
    st.session_state.love_meters = {
        "다자이 오사무": 0,
        "나카하라 츄야": 0,
        "아쿠타가와 류노스케": 0
    }

# --- 3. UI 레이아웃 화면 구성 ---
st.title("🍷 문호 스트레이독스: 마피아의 잔영")
st.subheader("주인공: 기시 유스케")
st.markdown("---")

# 현재 장면 데이터 가져오기
current_scene_id = st.session_state.current_scene
scene_data = GAME_DATA.get(current_scene_id, GAME_DATA["시작"])

# 상황 및 대사 출력
st.info(scene_data["상황"])

if scene_data["대사"]:
    st.markdown(f"**💬 대사 :** {scene_data['대as']}")

st.markdown("---")

# 선택지 버튼 출력 및 호감도 로직
st.write("**정해진 운명을 선택하세요:**")
cols = st.columns(len(scene_data["선택지"]))

for idx, option in enumerate(scene_data["선택지"]):
    with cols[idx]:
        # 버튼 생성
        if st.button(option["문구"], key=f"btn_{current_scene_id}_{idx}"):
            # 호감도 상승 시스템 (해당하는 캐릭터가 있고 증가 수치가 있을 때)
            target = option.get("호감도_타겟")
            amount = option.get("호감도_증가", 0)
            
            # 실제 캐릭터 매칭 (데이터 편의성을 위해 포함 여부로 체크)
            for char_name in st.session_state.love_meters.keys():
                if target in char_name:
                    st.session_state.love_meters[char_name] += amount
                    st.toast(f"💖 {char_name}의 호감도가 {amount} 증가했습니다!", icon="💖")

            # 다음 장면으로 이동
            st.session_state.current_scene = option["next"]
            st.rerun()

# --- 4. 호감도 표시 사이드바 (분홍색 강조) ---
st.sidebar.title("💕 캐릭터 호감도")
for char, score in st.session_state.love_meters.items():
    # HTML/CSS를 이용해 핑크색으로 호감도 강조
    st.sidebar.markdown(
        f"""
        <div style="background-color: #FFF0F5; padding: 10px; border-radius: 10px; margin-bottom: 10px; border-left: 5px solid #FF69B4;">
            <b style="color: #DB7093;">{char}</b><br>
            <span style="font-size: 20px;">💗 {score}</span>
        </div>
        """, 
        unsafe_allow_html=True
    )

# 게임 리셋 버튼
if st.sidebar.button("🔄 게임 처음부터 다시 하기"):
    st.session_state.current_scene = "시작"
    for char in st.session_state.love_meters:
        st.session_state.love_meters[char] = 0
    st.rerun()
