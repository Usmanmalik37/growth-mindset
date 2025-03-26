import streamlit as st
import random

st.title("🎯 Daily Growth Mindset Challenge Generator")

challenges = [
    "Compliment a stranger today.",
    "Write down one thing you failed at and what you learned.",
    "Do 10 minutes of meditation.",
    "Watch a video on a topic you've never explored before.",
    "Read 10 pages of a new book.",
    "Write tomorrow's one small goal.",
    "Thank someone for being in your life.",
    "Avoid your phone for 1 hour.",
    "Step outside your comfort zone in any way.",
    "Do 20 push-ups or any quick workout."
]

if st.button("Give me today's challenge! 🔥"):
    challenge = random.choice(challenges)
    st.success(f"✅ Your Challenge: {challenge}")
    st.write("Complete it and come back tomorrow for a new challenge! 🚀")