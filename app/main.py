import streamlit as st 
import numpy as np
import numpy as np
from links import FROH, TRAURIG

st.title("Eisenbahntest")

#hintergrundbild mit url
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://cdn-thumbs.ohmyprints.net/1/a3717c2525dbfcda3f38fa4bc3d735d8/817x600/thumbnail/fit.jpg");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)



wahl = st.selectbox("Wähle deinen beforzugten Test:", ["Bitte wählen" , "Eisenbahnen in der DDR", "Moderne Deutschen Eisenbahnen", "Eisenbahnen in Europa"])
if wahl == "Eisenbahnen in der DDR":
    st.image("https://image.jimcdn.com/app/cms/image/transf/dimension=530x10000:format=jpg/path/s39c9c999a872678e/image/iaa6faff1b0cee4f0/version/1724003276/image.jpg" , width=1000) 
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

if wahl == "Moderne Deutschen Eisenbahnen":
    st.write("Tolle Wahl")
    st.image("https://www.bahnbilder.de/1200/karwendelmassivaus-innsbruck-kommend-rollt-2442-1089108.jpg", width=1000) 
    auswahl7 = st.selectbox("Wähle die Br:", ["Br 2441" , "Br 423", "Br 2442" , "Br 101", "Br 145"])
    if auswahl7 == "Br 2442":
        st.write("Du hast Recht")
        st.image("https://www.modelleisenbahnanlage.com/wp-content/uploads/2009/02/br103-rot.jpg", width=1000)
        auswahl8 = st.selectbox("Wähle die Br:", ["Br 101" , "Br 145", "Br 423", "Br 2441", "Br 103"])
        if auswahl8 == "Br 103":
                st.write("Du hast Recht")
                st.image("https://image.jimcdn.com/app/cms/image/transf/dimension=500x10000:format=jpg/path/s39c9c999a872678e/image/i2794e3dd1d5e995d/version/1725286073/image.jpg" , width=1000)
                auswahl9 = st.selectbox("Wähle die Br:", ["Br 109" , "Br 101", "Br 423", "Br 2441", "Br 201"])
                if auswahl9 == "Br 101":
                    st.write("Super")
                    st.image("https://www.zukunft-mobilitaet.net/wp-content/uploads/2011/05/icx-br412-testfahrten-db-ice4-deutsche-bahn-fernverkehr-siemens-bild.jpg" , width=1000)
                    auswahl10 = st.selectbox("Wähle die Br:", ["Br 201" , "Br 412", "Br 2441", "Br 109", "Br 145"])
                    if auswahl10 == "Br 412":
                        st.write("Genau")
                        st.image("https://www.larsbrueggemann.de/fotos-eb-28-630px/529ewd-098-foto-ice-l-lauenbrueck.jpg")
                        auswahl11 = st.selectbox("Wähle die Br:", ["Br 145" , "Br 2441", "Br 109", "Br V220", "Br 105"])
                        if auswahl11 == "Br 105":
                            st.write("Sehr gut")
                            st.image("https://live.staticflickr.com/65535/48909750751_85a6599766_b.jpg" , width=3000)
                            auswahl12 = st.selectbox("Wähle die Br:", ["Br 145" , "Br 445", "Br 109", "Br V220", "Br V150"])
                            if auswahl12 == "Br 445":
                                st.write("Jawoll")
                                st.image("https://lh3.googleusercontent.com/proxy/ct2XBdFchB-Rse4os65Oncyv3RKrE-BpJSFdmhWOsZJ2C64gQQrd0qS-iS7N9jj3s8NxwucikSzGn6xnRcbaZau78F7_R7I-vcJ4oU0", width=1000)
                                auswahl13 = st.selectbox("Wähle die Br:", ["Br 145" , "Br 109", "Br V220", "Br 218", "Br 110"])
                                if auswahl13 == "Br 218":
                                    st.write("Du hast den Test bestanden")
                                    st.image("https://www.bahnbilder.de/bilder/110-466-mit-einem-ire-karlsruhe-77067.jpg", width=1000)
                                    auswahl14 = st.selectbox("Wähle die Br:", ["Br 145" , "Br 109", "Br V220", "Br 110", "Br 101"])
                                    if auswahl14 == "Br 110":
                                        st.write("Richtig")
                                        st.image("https://www.oehlerfoto.de/bilder/safran.jpg", width=1000)
                                        auswahl15 = st.selectbox("Wähle die Br:", ["Br 145" , "Br 109", "Br V220", "Br 101", "Br 612"])
                                        if auswahl15 == "Br 612":
                                            st.write("Test bestanden")
                                            st.image("https://static.maerklin.de/damcontent/5e/c3/5ec338e601b2ac5516c271cdd356b3d51660629608.jpg" , width=1000)
                                            auswahl16 = st.selectbox("Wähle die Br:", ["Br 145" , "Br 109", "Br 193", "Br 101", "Br V220"])
                                            if auswahl16 == "Br 193":
                                                st.write("Du hast den Test bestanden")
                                                st.image("https://upload.wikimedia.org/wikipedia/commons/4/47/V200_033_F%C3%BCrth.jpg", width=1001)
                                                auswahl17 = st.selectbox("Wähle die Br:", ["Br 145" , "Br V200", "Br V220", "Br 109", "Br 178"])
                                                if auswahl17 == "Br V200":
                                                    st.write("Du hast den Test bestanden")
                                                    st.video("https://youtu.be/2fZVG0AZe2k", autoplay=True)
                                                    auswahl18 = st.selectbox("Wähle den Zug", ["ICE 1" , "ICE X", "Maglev", "Transrapid", "ICE T"])
                                                    if auswahl18 == "Transrapid":
                                                        st.write("Du hast den Test bestanden")
                                                        st.video("https://youtu.be/OJcbBtwnhlY?list=RDOJcbBtwnhlY", autoplay=True)

if wahl == "Eisenbahnen in Europa":
    st.write("Gute Wahl")
    st.image("https://upload.wikimedia.org/wikipedia/commons/c/c5/TGV_Modane-Paris_%C3%A0_St-Jean-de-la-Porte_en_soir%C3%A9e_%28%C3%A9t%C3%A9_2021%29.JPG", width=1000) 
    auswahl19 = st.selectbox("Wähle die Br:", ["" , "TGV" , "ICE", "Eurostar", "Thalys", "Frecciarossa"])