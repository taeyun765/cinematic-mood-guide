import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="Cinematic Mood Guide", page_icon="🎬", layout="centered"
)

# 타이틀 및 소개
st.title("🎬 시네마틱 무드 가이드 (Cinematic Mood Guide)")
st.markdown(
    "원하는 **시대, 장르, 감정적 분위기**를 입력하시면, AI 큐레이터가 깊이 있는 3가지 명작을 추천해 드립니다."
)
st.markdown("---")

# 사용자 입력 섹션
st.subheader("🎞️ 어떤 영화를 찾고 계신가요?")

col1, col2 = st.columns(2)
with col1:
    movie_era = st.text_input("1. 시대 (예: 1940~50년대 이탈리아, 1990년대 홍콩)")
with col2:
    movie_genre = st.text_input("2. 장르 (예: 느와르, 네오레알리즘, SF 드라마)")

movie_mood = st.text_area(
    "3. 원하는 분위기 및 키워드",
    placeholder="예: 전쟁 직후의 황량함 속에서 피어나는 인간적인 연민과 쓸쓸함",
)

# 추천 실행 버튼
if st.button("✨ 맞춤형 영화 큐레이션 받기", type="primary"):
  if not movie_era or not movie_genre or not movie_mood:
    st.warning("⚠️ 시대, 장르, 분위기를 모두 입력해 주세요!")
  else:
    with st.spinner("영화 데이터베이스를 탐색하고 무드를 분석하는 중입니다..."):
      # (데모 모드: 실제 AI API 대신 과제 시연용으로 미리 구성된 시뮬레이션 결과 출력)
      import time

      time.sleep(2)  # 로딩 연출

      st.success("큐레이션이 완료되었습니다! 🎥")
      st.markdown("---")

      # 결과 카드 1
      st.markdown("### 🏆 1. 자전거 도둑 (Bicycle Thieves, 1948)")
      st.markdown(
          f"- **매칭 포인트:** 입력하신 *'{movie_era}'*, *'{movie_genre}'*, 그리고 *'{movie_mood}'* 결에 가장 완벽하게 부합합니다."
      )
      st.markdown(
          "- **큐레이터 코멘트:** 전쟁 직후 로마의 거친 풍경을 배경으로, 아버지와"
          " 아들의 하루를 통해 사회적 비극을 건조하면서도 깊은 울림으로"
          " 전달합니다."
      )
      st.markdown("")

      # 결과 카드 2
      st.markdown("### 🥈 2. 로마, 오픈 시티 (Rome, Open City, 1945)")
      st.markdown(
          "- **매칭 포인트:** 시대적 아픔 속에서 피어나는 처절한 연대의"
          " 감정을 담고 있습니다."
      )
      st.markdown(
          "- **큐레이터 코멘트:** 카메라가 포착한 현장의 생생함이 관객에게"
          " 그 시절의 공기를 고스란히 전달해 줍니다."
      )
      st.markdown("")

      # 결과 카드 3
      st.markdown("### 🥉 3. 400번의 구타 (The 400 Blows, 1959)")
      st.markdown(
          "- **매칭 포인트:** 차가운 현실을 마주한 소년의 시선을 통해 서늘한"
          " 고독과 자유에 대한 갈망을 그립니다."
      )
      st.markdown(
          "- **큐레이터 코멘트:** 질감 있는 흑백 화면이 선사하는 특유의"
          " 쓸쓸하고 아름다운 미학이 돋보입니다."
      )

# 사이드바 (과제 정보 안내)
with st.sidebar:
  st.header("📌 Project Info")
  st.info(
      "이 앱은 데이터 기반 AI 어플리케이션 디자인 스펙 과제를 위해 제작된"
      " 데모 프로토타입입니다."
  )
  st.markdown("**· 활용 도구:** Python, Streamlit, GitHub")
  st.markdown("**· 시스템 구조:** Serverless Cloud Deploy")
