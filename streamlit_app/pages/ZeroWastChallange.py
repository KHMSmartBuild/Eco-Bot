

import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
import streamlit.components.v1 as components

# Streamlit App Configuration
st.set_page_config(
    page_title="Eco-Bot",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Page Title
st.title("The Big Clean APP")

# Page Description
st.write("Welcome to the Eco-Bot's Zero-Waste Challenge")

# Intro Contents
with st.container():
    st.write("The Challenge")
   
    col1, col2, col3 = st.columns(3)
    with col1:
        st.video("https://www.youtube.com/watch?v=veXEBFmqfj0")
    with col2:
        st.video("https://www.youtube.com/watch?v=4GtWGHvX-rk&pp=ygUPd2FzdGUgcmVjeWNsaW5n")
    with col3:
        st.video("https://www.youtube.com/watch?v=3PYYadvwkOo&pp=ygUYd2FzdGUgbWFuYWdlbWVudCBpc3N1ZXMg")
    with col1:
        st.video("https://www.youtube.com/watch?v=ccR2zK6yn8o&pp=ygUYd2FzdGUgbWFuYWdlbWVudCBpc3N1ZXMg")
    with col2:
        st.video("https://www.youtube.com/watch?v=Cti5HQZnTrQ&pp=ygUYd2FzdGUgbWFuYWdlbWVudCBpc3N1ZXMg")
    with col3:
        st.image(f"assets/images/eco-botLF.png", caption="Eco-Bot", use_column_width=True)
st.write("Litter is one of the biggest challenges we face today. How can we ensure that we are using as much as possible of our waste?")
st.chat_input("Ask Eco-Bot a question: ")
# How To Solve The Challenge with Eco-Bot
# Page Contents
with st.container():
    st.write("How To Solve The Challenge with Eco-Bot")
    st.write("""
    Eco-Bot is a chatbot that helps you find the best way to recycle your waste. 
    """)
    if st.checkbox("Show Video", False):
        class ImageProcessor(VideoTransformerBase):
            def transform(self, frame):
                img = frame.to_ndarray(format="bgr24")
                
                # Add your image processing logic here
                
                return img

        webrtc_streamer(key="example", video_transformer_factory=ImageProcessor)
components.html("""<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>""")
