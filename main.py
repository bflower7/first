import streamlit as st

# MBTI 유형과 자세한 설명
mbti_types = {
    "ISTJ": {
        "description": "🔍 **신뢰할 수 있는 현실주의자**  \n"
                       "ISTJ는 주의 깊고 철저한 성향을 가진 사람들입니다.  \n"
                       "안정성과 일관성을 중요시하며, 자신이 하는 일에 대해 큰 책임감을 느낍니다.  \n"
                       "사실과 데이터를 중시하며, 감정을 배제한 합리적인 결정을 선호합니다.  \n"
                       "일이 끝난 후에는 휴식을 취하며, 자신의 공간에서 혼자 시간을 보내는 것을 좋아합니다.",
        "emoji": "🔍🗂️"
    },
    "ISFJ": {
        "description": "🤗 **헌신적인 보호자**  \n"
                       "ISFJ는 다른 사람들을 보살피고 돕는 것을 즐깁니다.  \n"
                       "강한 전통관을 가지고 있으며, 자신의 주변 사람들과의 관계를 중요시합니다.  \n"
                       "최고의 지원자가 되기를 원하며, 사람들을 즐겁고 편안하게 만드는 데 뛰어납니다.  \n"
                       "긴밀한 관계를 맺고, 자신의 책임을 철저히 이행하는 경향이 있습니다.",
        "emoji": "🤗🏡"
    },
    "INFJ": {
        "description": "🌈 **통찰력 있는 조언자**  \n"
                       "INFJ는 깊은 감정적 통찰력과 직관력을 가진 사람들입니다.  \n"
                       "타인의 감정을 잘 이해하고, 자신의 가치관에 따라 행동합니다.  \n"
                       "이상주의자로서, 목표를 세우고 그 목표를 향해 나아가는 것을 중시합니다.  \n"
                       "타인을 도우려는 강한 의지를 가지고 있습니다.",
        "emoji": "🌈💡"
    },
    "INTJ": {
        "description": "📈 **전략적인 계획자**  \n"
                       "INTJ는 분석적이며, 미래를 계획하는 데 능숙한 사람들입니다.  \n"
                       "창의적인 문제 해결자이며, 혁신적인 사고를 통해 목표를 달성합니다.  \n"
                       "가장 높은 효율성과 성과를 위해 시스템과 프로세스를 개선하는 것을 즐깁니다.  \n"
                       "자신의 생각과 이론에 신념을 가지고 있으며, 혼자 있는 것을 선호합니다.",
        "emoji": "📈🔍"
    },
    "ISTP": {
        "description": "⚙️ **유능한 문제 해결사**  \n"
                       "ISTP는 문제를 빠르고 효율적으로 해결하는 데 능한 실용적인 사람들입니다.  \n"
                       "즉각적인 결과를 중시하며, 다양한 경험을 통해 학습합니다.  \n"
                       "손재주가 뛰어나며, 기술적인 과제를 즐깁니다.  \n"
                       "모험을 즐기며, 자율적인 환경에서 잘 지냅니다.",
        "emoji": "⚙️🛠️"
    },
    "ISFP": {
        "description": "🎨 **유연한 예술가**  \n"
                       "ISFP는 감각적이고, 예술적인 것을 중시하는 창의적인 사람들입니다.  \n"
                       "자연에서 영감을 얻으며, 순간의 경험을 소중히 여깁니다.  \n"
                       "자신의 감정이나 경험에 기반한 표현을 중요시하며, 때론 내성적입니다.  \n"
                       "가장 좋아하는 예술적 과정을 통해 자신을 표현하는 것을 즐깁니다.",
        "emoji": "🎨🌿"
    },
    "INFP": {
        "description": "💖 **이상적인 중재자**  \n"
                       "INFP는 깊은 가치관을 가지고 있는 꿈꾸는 사람들입니다.  \n"
                       "자신의 이상이나 철학에 따라 행동하며, 타인에게 공감하는 능력이 뛰어납니다.  \n"
                       "올바른 것을 추구하며, 주변 사람들과의 관계를 중요하게 생각합니다.  \n"
                       "자기 표현을 중요시하며, 예술적인 즉흥세계를 좋아합니다.",
        "emoji": "💖📜"
    },
    "INTP": {
        "description": "🤔 **논리적인 사색가**  \n"
                       "INTP는 깊이 있는 분석과 이론적 사고를 바탕으로 문제를 바라보는 사람들입니다.  \n"
                       "비판적 사고와 창의성을 통해 새로운 가능성을 탐구합니다.  \n"
                       "지식 탐구에 대한 욕구가 강하며, 고립된 상태에서 시간을 보내는 것을 선호합니다.  \n"
                       "다양한 질문을 제기하고 답변을 찾으려는 경향이 있습니다.",
        "emoji": "🤔📘"
    },
    "ESTP": {
        "description": "🚀 **활기찬 해결사**  \n"
                       "ESTP는 즉각적인 결과를 선호하며, 활동적이고 모험을 즐깁니다.  \n"
                       "주변 환경에 쉽게 적응하고, 문제를 해결하기 위해 신속하게 행동합니다.  \n"
                       "사람들을 즐겁게 하고, 즉흥적인 활동을 선호합니다.  \n"
                       "자신의 경험에서 배우는 것을 중시하며, 실용적인 접근을 합니다.",
        "emoji": "🚀🎉"
    },
    "ESFP": {
        "description": "🎉 **사교적인 연예인**  \n"
                       "ESFP는 삶을 즐기고, 사람들과의 사교적인 관계를 중시합니다.  \n"
                       "상황을 즐겁게 만드는 천부적인 재능이 있으며, 순간의 경험을 남다르게 소중히 여깁니다.  \n"
                       "현실적이고 즉흥적인 접근을 통해 주변을 밝혀주며, 다른 사람들을 즐겁게 합니다.",
        "emoji": "🎉❤️"
    },
    "ENFP": {
        "description": "🌟 **창의적인 촉진자**  \n"
                       "ENFP는 새로운 아이디어와 관계에 열정적이며, 창의적인 접근을 선호합니다.  \n"
                       "사람들과의 연결을 중요시하며, 잠재력을 공유하는 것을 좋아합니다.  \n"
                       "자신의 감정을 표현하고, 다양한 가능성을 탐구하는 것을 즐깁니다.",
        "emoji": "🌟💬"
    },
    "ENTP": {
        "description": "💡 **발명가**  \n"
                       "ENTP는 혁신적이고 도전적인 사고를 통해 문제를 해결하는 데 탁월합니다.  \n"
                       "창의적이고 독창적인 아이디어를 제시하며, 새로운 가능성을 열어가는 것을 즐깁니다.  \n"
                       "논쟁을 즐기며, 다양한 관점을 통해 사고를 확장합니다.",
        "emoji": "💡🚀"
    },
    "ESTJ": {
        "description": "🏢 **자신감 있는 관리자**  \n"
                       "ESTJ는 체계적이고 실용적인 사고를 통해 사람들과 상황을 관리합니다.  \n"
                       "자신의 주변을 질서정연하게 유지하며, 안정성과 효율성을 중시합니다.  \n"
                       "강한 리더십을 발휘하며, 목표 달성을 위해 명확한 방향을 추구합니다.",
        "emoji": "🏢📊"
    },
    "ESFJ": {
        "description": "👥 **따뜻한 조정자**  \n"
                       "ESFJ는 사람들과의 관계를 소중히 여기며, 타인에 대한 관심이 매우 큽니다.  \n"
                       "주변 사람들을 돌보고, 조화로운 환경을 만들기 위해 노력합니다.  \n"
                       "팀워크와 소통을 중시하며, 공동체 의식을 깊게 느낍니다.",
        "emoji": "👥❤️"
    },
    "ENFJ": {
        "description": "🌼 **카리스마 있는 리더**  \n"
                       "ENFJ는 타인을 이끌고 격려하는 데 탁월한 능력을 가지고 있습니다.  \n"
                       "강한 공감을 통해 다른 사람의 필요를 인식하고, 협력적인 환경을 조성합니다.  \n"
                       "인간관계를 구축하고, 상호 작용을 통해 긍정적인 영향을 미치기를 원합니다.",
        "emoji": "🌼🤝"
    },
    "ENTJ": {
        "description": "🔥 **결단력 있는 지휘관**  \n"
                       "ENTJ는 강력한 리더십을 바탕으로 목표를 향한 명확한 경로를 설정합니다.  \n"
                       "전략적인 사고를 통해 복잡한 문제를 해결하며, 효율적인 작업을 좋아합니다.  \n"
                       "자신의 비전을 실현하기 위해 강력한 의지를 가지고 있으며, 팀을 이끄는 데 능숙합니다.",
        "emoji": "🔥📈"
    },
}

# Streamlit 애플리케이션 제목
st.title("🌟 MBTI 유형 선택하기")

# MBTI 유형 선택
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", list(mbti_types.keys()))

# 선택한 MBTI 유형 설명
if selected_mbti:
    st.subheader(f"선택한 MBTI 유형: **{selected_mbti}** {mbti_types[selected_mbti]['emoji']}")
    st.write(mbti_types[selected_mbti]["description"])

