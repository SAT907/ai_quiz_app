import streamlit as st
import json
import random
import base64
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="AI Master Quiz Game", layout="centered", initial_sidebar_state="collapsed")

# --- CONVERT LOCAL MP4 TO BASE64 URI ---
video_file_name = "534F4982-2476-4D8E-A282-E090326CCD15.mp4"

@st.cache_data
def load_video_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return None

video_b64 = load_video_base64(video_file_name)

# --- COMPLETE INJECTED CSS, VIDEO & AUDIO SYNC ENGINE ---
if video_b64:
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

    /* HIDE STREAMLIT DEFAULT HEADER & FOOTER TO PREVENT BUTTON OVERLAP */
    header[data-testid="stHeader"] {{
        display: none !important;
    }}
    #MainMenu {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}

    /* Clean Container Sizing */
    .block-container {{
        max-width: 780px !important;
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }}

    /* Global Typography */
    html, body, [class*="css"], label, p, span {{
        font-family: 'VT323', monospace !important;
        color: #FFFFFF !important;
        font-size: 22px !important;
    }}

    .stApp {{
        background-color: transparent !important;
    }}

    /* Fullscreen Background Video */
    #bg-video {{
        position: fixed;
        top: 50%;
        left: 50%;
        min-width: 100vw;
        min-height: 100vh;
        width: auto;
        height: auto;
        transform: translate(-50%, -50%);
        object-fit: cover;
        z-index: -9999;
        opacity: 0.45;
        pointer-events: none;
    }}

    /* Translucent Quiz Card */
    .quiz-card {{
        background: rgba(10, 15, 25, 0.92);
        padding: 24px;
        border-radius: 12px;
        border: 2px solid #00FF41;
        box-shadow: 0 0 18px #00FF41;
        margin-bottom: 15px;
        text-align: center;
    }}

    /* Radio Choice Custom Styling */
    .stRadio > div {{
        background: rgba(0, 0, 0, 0.75);
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #00FF41;
        text-align: left;
    }}

    /* Custom Streamlit Buttons */
    div.stButton > button:first-child {{
        background-color: #00FF41;
        color: #000000 !important;
        font-family: 'VT323', monospace !important;
        border: none;
        padding: 10px 20px;
        border-radius: 6px;
        font-size: 22px !important;
        width: 100%;
        cursor: pointer;
        margin-top: 10px;
    }}
    div.stButton > button:first-child:hover {{
        background-color: #00B32C;
        color: #FFFFFF !important;
        box-shadow: 0 0 12px #00FF41;
    }}

    /* Prominent Audio Toggle Button */
    .audio-btn-style {{
        background-color: #FF0033;
        color: #FFFFFF !important;
        border: 2px solid #00FF41;
        padding: 10px 24px;
        font-family: 'VT323', monospace !important;
        font-size: 22px !important;
        font-weight: bold;
        border-radius: 8px;
        cursor: pointer;
        box-shadow: 0 0 15px #FF0033;
        transition: 0.2s;
        margin-bottom: 15px;
        display: inline-block;
    }}

    h1 {{
        font-size: 38px !important;
        color: #00FF41 !important;
        text-align: center;
        margin-bottom: 0px !important;
        text-shadow: 2px 2px #000;
    }}
    </style>

    <!-- HTML5 Video Background -->
    <video id="bg-video" autoplay loop muted playsinline>
        <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
    </video>

    <!-- PROMINENT TOP AUDIO TOGGLE -->
    <div style="text-align: center; margin-top: 10px;">
        <button id="audio-control-btn" onclick="toggleVideoAudio()" class="audio-btn-style">
            🔇 AUDIO: OFF (CLICK TO TURN ON)
        </button>
    </div>

    <script>
    function updateBtnUI(isMuted) {{
        var btn = document.getElementById('audio-control-btn');
        if (btn) {{
            if (!isMuted) {{
                btn.innerHTML = "🔊 AUDIO: ON";
                btn.style.backgroundColor = "#00FF41";
                btn.style.color = "#000000";
                btn.style.boxShadow = "0 0 15px #00FF41";
            }} else {{
                btn.innerHTML = "🔇 AUDIO: OFF (CLICK TO TURN ON)";
                btn.style.backgroundColor = "#FF0033";
                btn.style.color = "#FFFFFF";
                btn.style.boxShadow = "0 0 15px #FF0033";
            }}
        }}
    }}

    function toggleVideoAudio() {{
        var v = document.getElementById('bg-video');
        if (v) {{
            if (v.muted) {{
                v.muted = false;
                v.play().catch(e => console.log(e));
                localStorage.setItem('quiz_audio_pref', 'on');
                updateBtnUI(false);
            }} else {{
                v.muted = true;
                localStorage.setItem('quiz_audio_pref', 'off');
                updateBtnUI(true);
            }}
        }}
    }}

    // Auto-restore audio state across Streamlit re-renders
    (function syncAudioOnRender() {{
        var v = document.getElementById('bg-video');
        var pref = localStorage.getItem('quiz_audio_pref');
        if (v) {{
            if (pref === 'on') {{
                v.muted = false;
                v.play().catch(e => console.log(e));
                updateBtnUI(false);
            }} else {{
                v.muted = true;
                updateBtnUI(true);
            }}
        }}
    }})();

    // Global listener: clicking anywhere on page turns sound on automatically if not explicitly turned off
    document.addEventListener('click', function(e) {{
        if (e.target && e.target.id === 'audio-control-btn') return;
        var v = document.getElementById('bg-video');
        var pref = localStorage.getItem('quiz_audio_pref');
        if (v && v.muted && pref !== 'off') {{
            v.muted = false;
            v.play().catch(err => console.log(err));
            localStorage.setItem('quiz_audio_pref', 'on');
            updateBtnUI(false);
        }}
    }});
    </script>
    """, unsafe_allow_html=True)
else:
    st.error(f"Missing video file: '{video_file_name}' in directory.")

# --- LOAD QUESTION BANK ---
@st.cache_data
def load_questions():
    try:
        with open('questions.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("Error: 'questions.json' not found. Run 'python build_json.py' first.")
        return []

question_bank = load_questions()

# --- SESSION STATE INITIALIZATION ---
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'current_idx' not in st.session_state:
    st.session_state.current_idx = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'shuffled_questions' not in st.session_state:
    st.session_state.shuffled_questions = []

# --- APP UI ---
st.title("🤖 AI MASTER QUIZ")
st.markdown("<p style='text-align: center; color: #00FF41; margin-bottom: 15px;'>UNITS I & II ASSESSMENT</p>", unsafe_allow_html=True)

if not st.session_state.quiz_started:
    st.markdown(
        "<div class='quiz-card'>"
        "SELECT GAME MODE TO BEGIN:<br><br>"
        "<small style='color: #00FF41;'>(Click button above or anywhere on screen to enable sound)</small>"
        "</div>", 
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔥 ALL 50 QUESTIONS"):
            st.session_state.shuffled_questions = random.sample(question_bank, len(question_bank))
            st.session_state.quiz_started = True
            st.session_state.current_idx = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.rerun()

    with col2:
        if st.button("⚡ 10 RANDOM QUESTIONS"):
            st.session_state.shuffled_questions = random.sample(question_bank, min(10, len(question_bank)))
            st.session_state.quiz_started = True
            st.session_state.current_idx = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.rerun()

else:
    q_list = st.session_state.shuffled_questions
    idx = st.session_state.current_idx

    if idx < len(q_list):
        q = q_list[idx]

        st.markdown("<div class='quiz-card'>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #00FF41; text-align: left;'>QUESTION {idx + 1} OF {len(q_list)} | SCORE: {st.session_state.score}</p>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: left;'>{q['question']}</h3>", unsafe_allow_html=True)

        # Multiple-Choice Radio Selector
        user_choice = st.radio(
            "Select your answer:",
            q['options'],
            key=f"q_choice_{idx}",
            disabled=st.session_state.answered
        )

        st.markdown("</div>", unsafe_allow_html=True)

        if not st.session_state.answered:
            if st.button("SUBMIT ANSWER"):
                st.session_state.answered = True
                if user_choice == q['answer']:
                    st.session_state.score += 1
                st.rerun()
        else:
            if user_choice == q['answer']:
                st.success("✅ CORRECT!")
            else:
                st.error(f"❌ INCORRECT! Correct answer: {q['answer']}")
            
            st.info(f"💡 Explanation: {q['explanation']}")

            if st.button("NEXT QUESTION ➡️"):
                st.session_state.current_idx += 1
                st.session_state.answered = False
                st.rerun()

    else:
        # Final Score Screen
        st.markdown("<div class='quiz-card'>", unsafe_allow_html=True)
        st.markdown("## 🏆 QUIZ COMPLETED")
        st.markdown(f"### FINAL SCORE: {st.session_state.score} / {len(q_list)}")

        pct = (st.session_state.score / len(q_list)) * 100
        if pct == 100:
            st.success("FLAWLESS VICTORY! 100%")
        elif pct >= 60:
            st.info(f"PASSING SCORE: {pct}%")
        else:
            st.error(f"NEEDS IMPROVEMENT: {pct}%")

        if st.button("🔄 RESTART QUIZ"):
            st.session_state.quiz_started = False
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
