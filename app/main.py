import streamlit as st 
import numpy as np
import numpy as np
from links import FROH, TRAURIG

st.title("Eisenbahntest")

wahl = st.selectbox("Wähle deinen beforzugten Test:", ["Bitte wählen" , "Eisenbahnen in der DDR", "Moderne Deutschen Eisenbahnen"])
if wahl == "Eisenbahnen in der DDR":
    st.image("https://y7b2e7b4.delivery.rocketcdn.me/wp-content/uploads//2019/09/6-Triebwagen-VT172-2.jpg" , width=1000) 
    auswahl = st.selectbox("Wähle die Br:", ["Br 601" , "Br 172", "Br 7"])
    if auswahl == "Br 172":
        st.write("Du hast Recht")
        st.image("https://www.bahnbilder.de/1200/20012023-idagroden-db-br-1323260.jpg", width=1000)
        auswahl2 = st.selectbox("Wähle die Br:", ["Br 669" , "Br 2 ", "Br 232"])
        if auswahl2 == "Br 232":
            st.write("Du hast Recht")
            st.image("https://hellertal.startbilder.de//1024/desiro-br-642-vogtlandbahn-vt-202616.jpg", width=1000)
            auswahl3 = st.selectbox("Wähle die Br:", ["Br 642" , "Br 172", "Br 7"])