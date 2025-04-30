import streamlit as st
import pydub 
import numpy as np
import numpy as np
from links import FROH, TRAURIG

# Emojis: 😎 💻 🚀 😢 😁
# mehr Emojis gibt es hier: https://apps.timwhitlock.info/emoji/tables/unicode
st.title("Frage runde ")

st.write("Wilkommen, ich bin ein Streamlit-Web-App ")

wahl = st.selectbox("Wähle deine beforzugte Marke:", ["Amd", "Nvdia"])

if wahl == "Amd":
    st.write("Du hast ein Verständnis von Technik.")
    st.image("https://www.appdisqus.com/wp-content/uploads/2025/03/AMD.webp" , width=2000)
    st.audio("/workspaces/learn-web-development-with-streamlit/app/sound/ahhhh-37191.mp3", format="audio/mpeg", loop=False, autoplay=True)
else:
    st.write("Du hast zu viel Geld.")
    st.image("https://i.ytimg.com/vi/FSElza2KVWg/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBgLWC0aqAcN8rVZD-UpVRRGcKIrg" , width=2000)
    col1, col2 = st.columns(2)
    with col1:
        st.audio("/workspaces/learn-web-development-with-streamlit/app/sound/lawnmower-2-57599.mp3", format="audio/mpeg", loop=False, autoplay=True )
    
    with col2:
        st.audio("/workspaces/learn-web-development-with-streamlit/app/sound/explosion-42132.mp3", format="audio/mpeg", loop=True, autoplay=True) 
    

wahl_os = st.selectbox("Wähle dein bevorzugtes Betriebssystem:", ["Windows", "Linux"])


if wahl_os == "Windows":
    st.write("Du solltest Linux ausprobieren.")
    st.image("https://images.moneycontrol.com/static-mcnews/2024/07/20240719093902_WhatsApp-Image-2024-07-19-at-15.02.58.jpeg?impolicy=website&width=770&height=431" , width=2000)
    st.audio("/workspaces/learn-web-development-with-streamlit/app/sound/mid-nights-sound-291477.mp3", format="audio/mpeg", loop=True, autoplay=True)
    st.video("https://youtu.be/D3-vBBQKOYU" , loop=True , autoplay=True)
else:
    st.write("Du bist ein richtiger Macher.")
    st.image("https://w7.pngwing.com/pngs/140/585/png-transparent-penguin-tux-of-math-command-linux-from-scratch-linux-kernel-penguin-animals-bird-printed-circuit-board.png" , width=2000)
    st.audio("/workspaces/learn-web-development-with-streamlit/app/sound/future-bass_feeling-162598.mp3", format="audio/mpeg", loop=False, autoplay=True )

#st.audio(data, format="audio/wav", start_time=0, *, sample_rate=None, end_time=None, loop=False, autoplay=False)



sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 16  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)

#audio mpeg formatieren zu numby array


def read(f, normalized=False):
    """MP3 to numpy array"""
    a = pydub.AudioSegment.from_mp3(f)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
    if normalized:
        return a.frame_rate, np.float32(y) / 2**15
    else:
        return a.frame_rate, y

def write(f, sr, x, normalized=False):
    """numpy array to MP3"""
    channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
    if normalized:  # normalized array - each item should be a float in [-1, 1)
        y = np.int16(x * 2 ** 15)
    else:
        y = np.int16(x)
    song = pydub.AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)
    song.export(f, format="mp3", bitrate="320k")

sampel_rate, arr = read("/workspaces/learn-web-development-with-streamlit/app/sound/ahhhh-37191.mp3", normalized=True)

st.write(arr.max(), arr.shape, sampel_rate)
st.audio(arr[:, 0], sample_rate=10000*sampel_rate)