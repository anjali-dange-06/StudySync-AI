from __future__ import annotations

import streamlit as st

from core.config import get_settings
from database.db import init_db
from pages import chat, coding_tutor, daily_goals, dashboard, documents, knowledge_gap, mindmap_page, planner, progress, quiz, summarize, voice_professor, weak_topics
from components.theme import load_theme

st.set_page_config(
    page_title="StudyPilot AI | Learn Smarter, Prepare Better",
    page_icon="📘",
    layout="wide", 
    initial_sidebar_state="expanded",
)

load_theme()

settings = get_settings()
init_db(settings.database_path)

with st.sidebar:
    st.markdown(
        '<div class="sp-brand"><div class="sp-brand-row"><div class="sp-logo">SP</div>'
        '<div><strong>StudyPilot AI</strong><br><span class="muted">Learning workspace</span></div></div>'
        '<div class="sp-profile"><strong>Student workspace</strong>'
        '<span><span class="status-dot"></span>Private data · local</span></div></div>',
        unsafe_allow_html=True,
    )
    st.caption("LEARN")
    st.markdown("---")
    section = st.radio(
        "Workspace",
        [
            "Dashboard",
            "My Daily Goals",
            "My documents",
            "AI study chat",
            "Smart summaries",
            "AI Mind Map Generator",
            "Quiz practice",
            "AI Coding Tutor",
            "Weak Topic Detection",
            "Knowledge Gap Detection",
            "AI Voice Professor",
            "Study planner",
            "My progress",
        ],
        label_visibility="collapsed",
        key="workspace_navigation",
    )
    st.markdown("---")
    st.caption("Your notes stay on this device.")
    if settings.api_key:
        st.success(f"Gemini configured · {settings.model}", icon="🔐")
    else:
        st.warning("Add GEMINI_API_KEY to .env to enable AI features.", icon="🔑")

pages_by_name = {
    "Dashboard": dashboard,
    "My Daily Goals": daily_goals,
    "My documents": documents,
    "AI study chat": chat,
    "Smart summaries": summarize,
    "AI Mind Map Generator": mindmap_page,
    "Quiz practice": quiz,
    "AI Coding Tutor": coding_tutor,
    "Weak Topic Detection": weak_topics,
    "Knowledge Gap Detection": knowledge_gap,
    "AI Voice Professor": voice_professor,
    "Study planner": planner,
    "My progress": progress,
}
app_page = st.Page(
    lambda: pages_by_name[section].render(settings),
    title="StudyPilot AI",
    default=True,
)
st.navigation([app_page], position="hidden").run()
