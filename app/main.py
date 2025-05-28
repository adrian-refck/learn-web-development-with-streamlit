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
            st.image("https://image.jimcdn.com/app/cms/image/transf/none/path/seeb3ec9c7b1770c5/backgroundarea/i2e088bbd57b9304f/version/1580588491/image.jpg", width=1000)
            auswahl3 = st.selectbox("Wähle die Br:", ["Br 624" , "Br 442", "Br 642" , "Br 118" , "Br 103"])
            if auswahl3 == "Br 118":
                st.write("Du hast Recht")
                st.image("https://www.bahnbilder.de/bilder/vt-115-tee-trans-120349.jpg" , width=1000)
                auswahl4 = st.selectbox("Wähle die Br:", ["Br 699" , "Br 513", "Br 601" , "Br 99" , "Br 120"])
                if auswahl4 == "Br 601":
                    st.write("Du hast recht")
                    st.image("https://www.eriksmail.de/Templates/100502GummibahnAltona/143211Altona020510.jpg", width=1000)
                    auswahl5 = st.selectbox("Wähle die Br:", ["Br 103" , "Br 143", "Br 401" , "Br1442" , "Br 52" ])
                    if auswahl5 == "Br 143":
                        st.write("Du hast recht")
                        st.image("https://img.fotocommunity.com/dr-v100-in-mecklenburg-1-219818a9-7615-47a1-9555-8b7c86cf7eb5.jpg?width=1000", width=1000)
                        auswahl6 = st.selectbox("Wähle die Br:", ["Br V150" , "Br V220", "Br 121", "Br V100", "Br 442"])
                        if auswahl6 == "Br V100":
                            st.header("Du hast den Test bestanden")
                            st.video("https://youtu.be/WQYN2P3E06s", autoplay=True)

else:
    st.write("Tolle Wahl")
    st.image("https://www.bahnbilder.de/1200/karwendelmassivaus-innsbruck-kommend-rollt-2442-1089108.jpg", width=1000) 
    auswahl7 = st.selectbox("Wähle die Br:", ["Br 2442" , "Br 423", "Br 146" , "Br 101", "Br 145"])
    if auswahl7 == "Br 2442":
        st.write("Du hast Recht")
        st.image("https://www.modelleisenbahnanlage.com/wp-content/uploads/2009/02/br103-rot.jpg", width=1000)