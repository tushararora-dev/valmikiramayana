import streamlit as st
from app import create_image_text_layout   # reuse function from main.py

def display_content():

    st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bungee+Spice:wght@700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Beth+Ellen&display=swap');
    h2 {
        font-family: 'Bungee Spice', cursive !important;
        font-size: 45px;
        text-align: center;
        color: #e7b66c !important;
    }
    .stMainBlockContainer{
        padding-top: 0rem; !important}
    p, li { 
        font-size: 18px !important;
        # line-height: 1.6 !important;
        text-align: justify !important;
        color: oldlace;
    }

    .st-emotion-cache-1gcegfv h2 {
    font-size: 1.5rem;
    }
    table {
        border-collapse: collapse;
        width: 100%;
    }

    td {
        border: 2px solid #444 !important;
        padding: 5px;
        font-size: 16px !important;
        line-height: 1.2 !important;
        text-align: justify !important;
        color: oldlace;
        background-color: #6969691f; /* dark background to contrast oldlace */
    }


    .beth1 {
            font-family: 'Beth Ellen', cursive !important; /* <-- use Beth Ellen (imported) */
            font-size: 22px;
            color: oldlace !important;
            text-align: center !important;
            margin-top: 0.2em;
            color: dimgray !important;
        }

    </style>
    """,
    unsafe_allow_html=True
    )
    create_image_text_layout("attached_assets/chapter3/chapter3.jpg", layout="full")
    create_image_text_layout("attached_assets/chapter3/banner3.jpg", layout="full")


    text0 = """
    <h2>Chapter 3: Aranya kanda</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

# Chapter 4.1
with st.expander("Chapter 4.1 – Rama talks about the beauty of spring and how it makes him feel"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.1.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.2
with st.expander("Chapter 4.2 – Sugriva sends Hanuman to meet Rama"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.2.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.3
with st.expander("Chapter 4.3 – Hanuman meets Rama for the first time"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.3.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.4
with st.expander("Chapter 4.4 – Hanuman brings Rama and Lakshmana to Sugriva"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.4.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.5
with st.expander("Chapter 4.5 – Rama and Sugriva become friends and make an alliance"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.5.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.6
with st.expander("Chapter 4.6 – Sugriva shows Rama Sita’s clothes and jewelry"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.6.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.7
with st.expander("Chapter 4.7 – Sugriva comforts Rama"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.7.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.8
with st.expander("Chapter 4.8 – Sugriva asks Rama to help him fight Bali"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.8.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.9
with st.expander("Chapter 4.9 – Sugriva tells Rama the story of Bali and Mayavi"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.9.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.10
with st.expander("Chapter 4.10 – Sugriva explains why Bali became angry with him"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.10.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.11
with st.expander("Chapter 4.11 – Sugriva tells Rama about Bali’s great strength"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.11.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.12
with st.expander("Chapter 4.12 – Sugriva and Bali fight"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.12.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.13
with st.expander("Chapter 4.13 – Rama visits the hermitage of the seven sages"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.13.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.14
with st.expander("Chapter 4.14 – Sugriva challenges Bali again"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.14.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.15
with st.expander("Chapter 4.15 – Tara gives advice to Bali"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.15.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.16
with st.expander("Chapter 4.16 – Rama fatally wounds Bali"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.16.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.17
with st.expander("Chapter 4.17 – Bali questions and blames Rama"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.17.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.18
with st.expander("Chapter 4.18 – Rama explains his reasons to Bali"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.18.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.19
with st.expander("Chapter 4.19 – Tara cries in sorrow"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.19.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.20
with st.expander("Chapter 4.20 – Tara continues to mourn for Bali"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.20.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.21
with st.expander("Chapter 4.21 – Hanuman speaks to comfort and guide everyone"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.21.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.22
with st.expander("Chapter 4.22 – Bali says his final words"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.22.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.23
with st.expander("Chapter 4.23 – Tara cries over Bali’s body"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.23.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.24
with st.expander("Chapter 4.24 – Sugriva feels guilty and sad"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.24.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.25
with st.expander("Chapter 4.25 – Bali’s funeral is performed"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.25.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.26
with st.expander("Chapter 4.26 – Sugriva is crowned as king"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.26.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.27
with st.expander("Chapter 4.27 – Rama describes the Prasravana mountain"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.27.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.28
with st.expander("Chapter 4.28 – Rama talks about the rainy season"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.28.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.29
with st.expander("Chapter 4.29 – Hanuman reminds Sugriva of his promise to help find Sita"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.29.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.30
with st.expander("Chapter 4.30 – The autumn season is described"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.30.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.31
with st.expander("Chapter 4.31 – Lakshmana goes to Kishkindha"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.31.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.32
with st.expander("Chapter 4.32 – Hanuman speaks to calm Lakshmana"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.32.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.33
with st.expander("Chapter 4.33 – Tara gently stops Lakshmana from getting angry"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.33.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.34
with st.expander("Chapter 4.34 – Lakshmana scolds Sugriva"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.34.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.35
with st.expander("Chapter 4.35 – Tara explains and defends Sugriva"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.35.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.36
with st.expander("Chapter 4.36 – Lakshmana forgives Sugriva"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.36.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.37
with st.expander("Chapter 4.37 – Sugriva gathers his monkey army"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.37.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.38
with st.expander("Chapter 4.38 – Sugriva goes to meet Rama"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.38.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.39
with st.expander("Chapter 4.39 – Sugriva’s huge monkey forces arrive"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.39.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.40
with st.expander("Chapter 4.40 – Sugriva sends monkeys to search for Sita in the East"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.40.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.41
with st.expander("Chapter 4.41 – Sugriva sends another team to search in the South"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.41.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.42
with st.expander("Chapter 4.42 – More monkeys are sent to the West"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.42.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.43
with st.expander("Chapter 4.43 – A group is sent to search in the North"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.43.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.44
with st.expander("Chapter 4.44 – Rama gives his ring to Hanuman"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.44.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.45
with st.expander("Chapter 4.45 – The monkey search teams leave"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.45.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.46
with st.expander("Chapter 4.46 – Sugriva tells about his travels around the world"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.46.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.47
with st.expander("Chapter 4.47 – The monkeys return from their search"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.47.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.48
with st.expander("Chapter 4.48 – Angada kills an Asura"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.48.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.49
with st.expander("Chapter 4.49 – The monkeys searching in the South do not find Sita"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.49.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.50
with st.expander("Chapter 4.50 – Hanuman and friends enter the dark Rikshabilā cave"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.50.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.51
with st.expander("Chapter 4.51 – They hear the story of an old ascetic"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.51.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.52
with st.expander("Chapter 4.52 – Swayamprabha frees the monkeys from the cave"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.52.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.53
with st.expander("Chapter 4.53 – Angada and his friends discuss what to do next"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.53.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.54
with st.expander("Chapter 4.54 – Hanuman tries to stop Angada’s hopeless plans"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.54.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.55
with st.expander("Chapter 4.55 – The monkeys think of giving up and starving"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.55.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.56
with st.expander("Chapter 4.56 – Sampati suddenly appears"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.56.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.57
with st.expander("Chapter 4.57 – Angada tells his story to Sampati"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.57.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.58
with st.expander("Chapter 4.58 – Sampati tells the monkeys where Sita is hidden"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.58.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.59
with st.expander("Chapter 4.59 – Sampati encourages them to continue their mission"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.59.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.60
with st.expander("Chapter 4.60 – The story of the ascetic Nishakara"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.60.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.61
with st.expander("Chapter 4.61 – Sampati tells his story to Sage Nishakara"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.61.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.62
with st.expander("Chapter 4.62 – The sage tells Sampati where Sita is"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.62.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.63
with st.expander("Chapter 4.63 – Sampati’s wings grow back"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.63.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.64
with st.expander("Chapter 4.64 – The monkeys feel scared when they see the huge ocean"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.64.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.65
with st.expander("Chapter 4.65 – The leaders of the monkey army discuss their plan"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.65.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.66
with st.expander("Chapter 4.66 – Jambavan reminds Hanuman of his great powers"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.66.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")


# Chapter 4.67
with st.expander("Chapter 4.67 – Hanuman gets ready to leap to Lanka"):
    text1 = """ """

    create_image_text_layout("attached_assets/chapter4/4.67.jpg", text1, layout="side", image_position="left")

    text2 = """ """
    create_image_text_layout(text_content=text2, layout="full")

