
import streamlit as st
import time

# 1. 페이지 설정
st.set_page_config(
    page_title="러브 시그널: 방과 후의 기적",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. 게임 데이터 및 스토리 시나리오 정의
SCENARIOS = {
    "start": {
        "title": "🌸 만남의 시작, 벚꽃길",
        "bg_image": "https://images.unsplash.com/photo-1524413840807-0c3cb6fa808d?auto=format&fit=crop&w=1200&q=80", # 벚꽃길 배경
        "char_image": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=500&q=80", # 소희 (미소/자연스러운 포트레이트)
        "character": "소희",
        "dialogue": "안녕! 오늘 마침 딱 맞춰 만났네? 같이 등교할까?",
        "choices": [
            {"text": "🌸 가방을 대신 들어주며 같이 가자고 한다.", "next": "classroom_together", "love_change": 15},
            {"text": "✨ 장난치며 볼을 살짝 꼬집는다.", "next": "classroom_playful", "love_change": 5},
            {"text": "💦 부끄러워서 헛기침을 하며 앞서 걸어간다.", "next": "classroom_awkward", "love_change": -5}
        ]
    },
    "classroom_together": {
        "title": "🏫 설레는 교실 안",
        "bg_image": "https://images.unsplash.com/photo-1580582932707-520aed937b7b?auto=format&fit=crop&w=1200&q=80", # 교실 배경
        "char_image": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=500&q=80", # 기분 좋은 웃음 소희
        "character": "소희",
        "dialogue": "히히, 고마워. 너 오늘 왜 이렇게 친절해? 꼭 딴 사람 같잖아~ 점심시간에 내 옥상 비밀 아지트로 올래?",
        "choices": [
            {"text": "🍱 당연히 가야지! 수제 도시락을 기대할게.", "next": "rooftop_happy", "love_change": 20},
            {"text": "🥖 매점에서 피자빵 사서 가겠다고 한다.", "next": "rooftop_normal", "love_change": 10},
            {"text": "✍️ 졸려서 교실에서 낮잠 자겠다고 거절한다.", "next": "ending_bad", "love_change": -20}
        ]
    },
    "classroom_playful": {
        "title": "🏫 교실 복도에서의 투닥거림",
        "bg_image": "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?auto=format&fit=crop&w=1200&q=80", # 복도 배경
        "char_image": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=500&q=80", # 삐진 표정 느낌의 소희
        "character": "소희",
        "dialogue": "아얏! 아침부터 또 장난이야? 진짜 초등학생도 아니고... 그래도 밉지 않네. 방과 후에 시간 비어?",
        "choices": [
            {"text": "☕ 카페에 가서 새로 나온 신메뉴를 사주겠다고 한다.", "next": "cafe_date", "love_change": 15},
            {"text": "🏃 오락실에 가서 대결을 신청한다.", "next": "arcade_date", "love_change": 5}
        ]
    },
    "classroom_awkward": {
        "title": "🏫 서먹서먹해진 오전 수업",
        "bg_image": "https://images.unsplash.com/photo-1507842217343-583bb7270b66?auto=format&fit=crop&w=1200&q=80", # 도서실 느낌 배경
        "char_image": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=500&q=80", # 무덤덤한 표정
        "character": "소희",
        "dialogue": "너 요새 사춘기야? 왜 나랑 눈도 안 마주치려고 해? 나 뭐 잘못한 거라도 있어...?",
        "choices": [
            {"text": "💌 사실 부끄러워서 그랬다고 솔직하게 털어놓는다.", "next": "classroom_together", "love_change": 15},
            {"text": "💼 아무것도 아니라고 둘러대며 자리를 피한다.", "next": "ending_bad", "love_change": -15}
        ]
    },
    "rooftop_happy": {
        "title": "🌅 노을빛 옥상 아지트",
        "bg_image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80", # 노을 풍경
        "char_image": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=500&q=80", # 수줍게 웃는 모습
        "character": "소희",
        "dialogue": "짜잔! 내가 아침 일찍 만든 사랑의 3단 도시락이야! ...흠, '사랑'은 빼고 그냥 3단 도시락! 얼른 먹어봐!",
        "choices": [
            {"text": "💝 눈을 감고 너와 늘 함께하고 싶다고 고백한다.", "next": "ending_good_check", "love_change": 25},
            {"text": "👍 진짜 맛있다며 다음에도 또 해달라고 약속한다.", "next": "ending_normal_check", "love_change": 10}
        ]
    },
    "rooftop_normal": {
        "title": "🌅 바람 부는 옥상",
        "bg_image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "char_image": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=500&q=80",
        "character": "소희",
        "dialogue": "음~ 피자빵 냄새 좋다! 한 입만 줘! 맨날 투닥거려도 너랑 옥상에 있을 때가 제일 마음 편해.",
        "choices": [
            {"text": "💕 나 사실 네가 여자로 보이기 시작했어.", "next": "ending_good_check", "love_change": 20},
            {"text": "👬 우리 우정 변치 말자, 평생 단짝친구야!", "next": "ending_friend", "love_change": 0}
        ]
    },
    "cafe_date": {
        "title": "☕ 분위기 좋은 카페",
        "bg_image": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=1200&q=80", # 따뜻한 카페
        "char_image": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=500&q=80",
        "character": "소희",
        "dialogue": "우와, 여기 인스타 감성 뿜뿜한다! 달콤한 조각 케이크 보니까 오늘 피로가 싹 가시는 느낌이야. 너 센스 늘었다?",
        "choices": [
            {"text": "🌹 네가 좋아할 것 같아서 미리 알아봤어.", "next": "ending_good_check", "love_change": 20},
            {"text": "🍰 사실 그냥 가까운 곳 온 건데 개이득이네!", "next": "ending_normal_check", "love_change": 5}
        ]
    },
    "arcade_date": {
        "title": "🎮 반짝이는 오락실",
        "bg_image": "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=1200&q=80", # 네온사인 오락실
        "char_image": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=500&q=80",
        "character": "소희",
        "dialogue": "앗싸! 내가 리듬게임 1등 먹었다! 넌 손가락이 왜 그렇게 굼뜨냐? 딱 대, 딱 밤 한 대 예약이야!",
        "choices": [
            {"text": "🤕 내 머리가 아픈 만큼 네가 즐거웠다면 좋아.", "next": "ending_normal_check", "love_change": 15},
            {"text": "🔥 한 판 더 해! 이번엔 내 인생을 걸겠어!", "next": "ending_friend", "love_change": 5}
        ]
    },
    "ending_friend": {
        "title": "👬 우정 엔딩: 최고의 단짝",
        "bg_image": "https://images.unsplash.com/photo-1491438590914-bc09fcaaf77a?auto=format&fit=crop&w=1200&q=80", # 편안한 골목길
        "char_image": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=500&q=80",
        "character": "소희",
        "dialogue": "헤헤, 역시 내 마음을 제일 잘 아는 건 너뿐이야! 평생 내 1호 단짝친구가 되어줘!",
        "is_ending": True,
        "type": "friend"
    },
    "ending_bad": {
        "title": "😢 배드 엔딩: 어색해진 사이",
        "bg_image": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?auto=format&fit=crop&w=1200&q=80", # 쓸쓸한 버스 정류장
        "char_image": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=500&q=80",
        "character": "소희",
        "dialogue": "응... 바쁘면 어쩔 수 없지. 가볼게... (소희의 눈빛이 무덤덤해진 채 뒤돌아섭니다.)",
        "is_ending": True,
        "type": "bad"
    },
    "ending_happy": {
        "title": "💖 트루 해피엔딩: 수줍은 고백",
        "bg_image": "https://images.unsplash.com/photo-1524413840807-0c3cb6fa808d?auto=format&fit=crop&w=1200&q=80",
        "char_image": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=500&q=80",
        "character": "소희",
        "dialogue": "어... 정말? 나 사실 아주 오랫동안 이 날만을 기다려왔어. 앞으로 매일 너랑 함께하고 싶어... 좋아해!",
        "is_ending": True,
        "type": "happy"
    }
}

# 3. 세션 상태(Session State) 초기화
if "scene" not in st.session_state:
    st.session_state.scene = "start"
if "love_meter" not in st.session_state:
    st.session_state.love_meter = 30 # 시작 호감도 30%
if "log" not in st.session_state:
    st.session_state.log = []

current_scene = SCENARIOS[st.session_state.scene]

# 분기 체크용 더미 씬 처리 (호감도 수치에 따른 진정한 엔딩 판정)
if st.session_state.scene in ["ending_good_check", "ending_normal_check"]:
    if st.session_state.love_meter >= 60:
        st.session_state.scene = "ending_happy"
    elif st.session_state.love_meter >= 40:
        st.session_state.scene = "ending_friend"
    else:
        st.session_state.scene = "ending_bad"
    st.rerun()

current_scene = SCENARIOS[st.session_state.scene]

# 4. 사이드바 - 실시간 호감도 & 기록 대시보드
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #ff6b81;'>🌸 미연시 상태 정보</h2>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=300&q=80", caption="소꿉친구 '소희' (18)", use_container_width=True)
    
    # 호감도 게이지바 구현
    love = st.session_state.love_meter
    love = max(0, min(100, love)) # 0 ~ 100 제한
    
    st.markdown(f"#### ❤️ 소희와의 호감도: **{love}%**")
    st.progress(love / 100)
    
    # 성향 분석 텍스트
    if love >= 80:
        st.success("💖 심장이 터질 것 같은 운명적 상태!")
    elif love >= 50:
        st.info("😊 단순한 친구 이상으로 의식하는 중!")
    elif love >= 30:
        st.warning("🤝 아직은 소꿉친구 단계예요.")
    else:
        st.error("💔 서먹해지고 있어 위험해요!")
        
    st.divider()
    st.markdown("### 📜 지금까지 선택한 역사")
    if st.session_state.log:
        for item in st.session_state.log:
            st.caption(item)
    else:
        st.caption("선택을 통해 추억을 쌓아보세요.")

# 5. 메인 게임 화면 디자인용 커스텀 CSS 주입
st.markdown("""
<style>
    /* 전체 배경을 비주얼 노벨풍으로 감싸는 컨테이너 */
    .game-box {
        background-color: #121212;
        border-radius: 15px;
        padding: 10px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        color: white;
        margin-bottom: 20px;
    }
    /* 비주얼 노벨 특유의 반투명 텍스트 대사창 */
    .text-box {
        background-color: rgba(20, 20, 20, 0.85);
        border: 2px solid #ff6b81;
        border-radius: 10px;
        padding: 18px;
        margin-top: 15px;
        font-size: 1.15rem;
        line-height: 1.6;
        color: #f1f1f1;
        box-shadow: inset 0 0 10px rgba(255,107,129,0.3);
    }
    .char-name {
        color: #ff6b81;
        font-weight: bold;
        font-size: 1.25rem;
        margin-bottom: 5px;
        text-shadow: 1px 1px 2px black;
    }
</style>
""", unsafe_allow_html=True)

# 6. 메인 화면 헤더 및 배경 아트 구현
st.title("💖 러브 시그널: 방과 후의 기적")
st.caption("방과 후, 노을 아래에서 소꿉친구와의 로맨스가 피어납니다. 당신의 선택은?")

# 게임 가상 윈도우 레이아웃 구현 (상단 배경화면 / 캐릭터 배치)
with st.container():
    # 2단 컬럼 구조로 왼쪽은 캐릭터 초상화, 오른쪽은 감성적 배경 이미지
    col1, col2 = st.columns([1.1, 2], gap="small")
    
    with col1:
        # 소희의 포트레이트
        st.image(current_scene["char_image"], use_container_width=True, caption=current_scene.get("character", ""))
        
    with col2:
        # 진행 중인 상황의 넓은 감성 배경
        st.image(current_scene["bg_image"], use_container_width=True, caption=f"현재 장소: {current_scene['title']}")

# 7. 비주얼 노벨형 대사 출력부
st.markdown(f"""
<div class="text-box">
    <div class="char-name">🎙️ {current_scene.get('character', '시스템')}</div>
    <div>"{current_scene['dialogue']}"</div>
</div>
""", unsafe_allow_html=True)

st.write("") # 간격 띄우기

# 8. 선택지 인터페이스 구현 (버튼 클릭 시 분기 전개 및 상태 관리)
if not current_scene.get("is_ending", False):
    st.markdown("### 👈 다음 중 당신의 선택은?")
    
    # 3가지 버튼 세로 배열 또는 가로 배치 (여기서는 직관적인 세로 배치 이용)
    for idx, choice in enumerate(current_scene["choices"]):
        # 버튼 스타일 다양화를 위해 이모지와 텍스트 적용
        if st.button(choice["text"], key=f"choice_{idx}", use_container_width=True):
            # 1. 호감도 반영
            st.session_state.love_meter += choice["love_change"]
            # 2. 히스토리 기록
            st.session_state.log.append(f"📍 {current_scene['title']} → {choice['text'].split(' ')[0]} 선택 (호감도 {choice['love_change']}%p)")
            # 3. 화면 지연 애니메이션 효과 연출
            with st.spinner("소희의 마음이 바뀌는 중..."):
                time.sleep(0.5)
            # 4. 다음 신(Scene)으로 교체 및 강제 렌더링
            st.session_state.scene = choice["next"]
            st.rerun()
else:
    # 게임 클리어 엔딩 씬일 경우 결과 요약문 제공
    st.markdown("### 🎉 에필로그 결과")
    
    end_type = current_scene.get("type", "friend")
    if end_type == "happy":
        st.balloons()
        st.success(f"💖 축하합니다! 성공적으로 소희의 마음을 열어 트루 해피엔딩에 도달했습니다! (최종 호감도: {st.session_state.love_meter}%)")
    elif end_type == "friend":
        st.info(f"🤝 둘도 없는 단짝 친구로서 평생의 파트너가 되었습니다. (최종 호감도: {st.session_state.love_meter}%)")
    else:
        st.error(f"😢 아쉽게도 소희와의 거리가 너무 멀어졌습니다. 다시 도전해 보세요... (최종 호감도: {st.session_state.love_meter}%)")

    # 9. 다시하기 리셋 기능
    if st.button("🔄 처음부터 다시 도전하기", type="primary", use_container_width=True):
        st.session_state.scene = "start"
        st.session_state.love_meter = 30
        st.session_state.log = []
        st.rerun()
