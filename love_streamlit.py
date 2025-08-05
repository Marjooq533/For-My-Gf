import streamlit as st
import base64

# --- Set background image and overlay ---
def set_bg(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');
        .stApp {{
            background: linear-gradient(rgba(255, 192, 203, 0.3), rgba(255, 182, 193, 0.3)),
                        url("data:image/jpg;base64,{encoded}") no-repeat center center fixed;
            background-size: cover;
            font-family: 'Dancing Script', cursive;
            font-weight: 700;  /* Make all text bold */
        }}
        .title-text {{
            text-align: center;
            color: #e75480;
            font-size: 60px;  /* Bigger */
            font-weight: 700;
            text-shadow: 1px 1px 5px white;
        }}
        .subtitle-text {{
            text-align: center;
            color: #8b0000;
            font-size: 32px;  /* Bigger */
            font-weight: 700;
            margin-bottom: 40px;
            text-shadow: 1px 1px 3px white;
        }}
        .love-box {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 30px;
            border-radius: 25px;
            box-shadow: 3px 3px 15px rgba(0,0,0,0.25);
            font-size: 26px;  /* Bigger */
            font-weight: 700;
            color: #4b0082;
            text-align: center;
            margin: 0 auto 40px auto;
            max-width: 900px;
        }}
        .stButton > button {{
            background-color: #ffb6c1;
            color: #8b0000;
            border-radius: 15px;
            font-size: 26px;  /* Bigger */
            font-weight: 700;
            padding: 15px 40px;
            border: none;
            transition: 0.3s;
            width: 100%;
            max-width: 300px;
            cursor: pointer;
        }}
        .stButton > button:hover {{
            background-color: #ff69b4;
            color: white;
        }}
        .footer {{
            color: #4b0082;
            text-align: center;
            font-size: 20px;  /* Bigger */
            font-weight: 700;
            margin-top: 50px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Romantic paragraphs ---
love_paragraphs = [
    "I know I can be clingy sometimes, but it’s only because the thought of losing you scares the life out of me. You’re not just someone I love — you’re the person I can’t imagine existing without. You’re mine, and I feel safe when I say that, because every second with you feels like home.",
    "Every moment you're away, it feels like something is missing. My heart doesn't beat the same when you’re not near. I miss you in ways words can’t explain — not just your voice or your face, but the energy you bring into my soul. Without you, I feel half-alive.",
    "I don’t want to share you with the world. I want to keep you all to myself — your laughs, your sleepy eyes, the way you breathe when you're close to me. You're mine in every way, and I cherish you like the rarest thing in the universe.",
    "Loving you isn’t something I chose — it’s something my heart decided on its own. You became my addiction, my obsession, my peace, and my chaos. I crave your touch, your smell, your voice. I need you more than I’ve ever needed anything.",
    "Sometimes I just stare at our chats or your photos, smiling like an idiot, because my heart still can’t believe you're real. I miss you even when you’re just a message away. I want to wrap myself in your presence and never let go.",
    "I’m not good with words, but I hope you can feel how insanely, deeply, stupidly in love with you I am. It’s overwhelming — the way you make me feel. Like I was made just to love you, protect you, and never let anything hurt you.",
    "You’re not just the love of my life — you’re the part of me I never knew was missing. I need you like I need air. And I’m not afraid to say it — I get jealous, scared, and overly attached, because I love you that much. And I never want to let you go."
]

# --- Streamlit app setup ---
st.set_page_config(page_title="A Piece of My Heart 💌", page_icon="💘", layout="centered")

# Set background
set_bg("background.jpg")

# Title and intro
st.markdown("<div class='title-text'>FOR THE LOVE OF MY HEART 💖</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle-text'>CLICK BELOW EVERYTIME TO KNOW HOW I FEEL WHEN YOU R NEAR ME CHELLAMEY😚</div>", unsafe_allow_html=True)

# Paragraph logic
if 'index' not in st.session_state:
    st.session_state.index = 0

# Center the button using columns
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("MY HEART 🌹"):
        if st.session_state.index < len(love_paragraphs):
            st.markdown(
                f"<div class='love-box'>{love_paragraphs[st.session_state.index]}</div>",
                unsafe_allow_html=True)
            st.session_state.index += 1
        else:
            st.markdown("<div class='love-box' style='color:#ff1493;'>That’s all for now… but my heart still overflows with love for you--MY KANMANI💗</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Made with love — your 🐒</div>", unsafe_allow_html=True)
