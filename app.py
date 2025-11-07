import streamlit as st
import time

st.title("AI Referee Demo")
st.write("Upload a play → Get instant AI call + confidence!")

video = st.file_uploader("Upload video", type=["mp4", "mov"])

if video:
    st.video(video)
    if st.button("Run AI Review"):
        with st.spinner("Analyzing..."):
            time.sleep(2)
        st.success("Call: **Traveling**")
        st.info("Confidence: 96% → High")
        st.write("AI: **1.8 sec** | Human: **45 sec**")
        st.balloons()
