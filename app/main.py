import streamlit as st
import numpy as np
from links import FROH, TRAURIG

# Emojis: 😎 💻 🚀 😢 😁
# mehr Emojis gibt es hier: https://apps.timwhitlock.info/emoji/tables/unicode
st.title("Frage runde ")

st.write("Wilkommen, ich bin ein Streamlit-Web-App ")

wahl = st.selectbox("Wähle deine beforzugte Marke:", ["Amd", "Nvdia"])

if wahl == "Amd":
    st.write("Du hast ein Verständnis von Technik.")
    st.image("https://www.appdisqus.com/wp-content/uploads/2025/03/AMD.webp" , width=1000)
    st.audio("/workspaces/learn-web-development-with-streamlit/app/sound/ahhhh-37191.mp3", format="audio/mpeg", loop=False, autoplay=True)
else:
    st.write("Du hast zu viel Geld.")
    st.image("https://i.ytimg.com/vi/FSElza2KVWg/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBgLWC0aqAcN8rVZD-UpVRRGcKIrg" , width=1000)
    col1, col2 = st.columns(2)
    with col1:
        st.audio("/workspaces/learn-web-development-with-streamlit/app/sound/lawnmower-2-57599.mp3", format="audio/mpeg", loop=False, autoplay=True )
    
    with col2:
        st.audio("/workspaces/learn-web-development-with-streamlit/app/sound/explosion-42132.mp3", format="audio/mpeg", loop=True, autoplay=True) 
    

wahl_os = st.selectbox("Wähle dein bevorzugtes Betriebssystem:", ["Windows", "Linux"])


if wahl_os == "Windows":
    st.write("Du solltest Linux ausprobieren.")
    st.image("https://images.moneycontrol.com/static-mcnews/2024/07/20240719093902_WhatsApp-Image-2024-07-19-at-15.02.58.jpeg?impolicy=website&width=770&height=431" , width=1000)
    st.audio("/workspaces/learn-web-development-with-streamlit/app/sound/mid-nights-sound-291477.mp3", format="audio/mpeg", loop=True, autoplay=True)
    st.video("https://youtu.be/D3-vBBQKOYU" , loop=True , autoplay=True)
else:
    st.write("Du bist ein richtiger Macher.")
    st.image("https://w7.pngwing.com/pngs/140/585/png-transparent-penguin-tux-of-math-command-linux-from-scratch-linux-kernel-penguin-animals-bird-printed-circuit-board.png" , width=1000)
    st.audio("/workspaces/learn-web-development-with-streamlit/app/sound/future-bass_feeling-162598.mp3", format="audio/mpeg", loop=False, autoplay=True)




#sample_rate = 40000 # 44100 samples per second
#seconds = 2  # Note duration of 2 seconds
#frequency_la = 20000  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
#t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
#note_la = np.sin(frequency_la * t * 2 * np.pi) + np.sin(2 * frequency_la * t * 2 * np.pi) 

#st.audio(note_la, sample_rate=sample_rate)







