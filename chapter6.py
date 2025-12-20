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
    create_image_text_layout("attached_assets/chapter6/chapter6.jpg", layout="full")
    create_image_text_layout("attached_assets/chapter6/banner6.jpg", layout="full")


    text0 = """
    <h2>Chapter 6: Yuddha kanda</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")
    # Chapter 6.1
    with st.expander("Chapter 6.1 – Rama praises Hanuman and feels worried"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.1.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.2
    with st.expander("Chapter 6.2 – Sugriva comforts Rama"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.2.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.3
    with st.expander("Chapter 6.3 – Hanuman tells Rama about Lanka’s strength"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.3.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.4
    with st.expander("Chapter 6.4 – The army reaches the sea shore"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.4.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.5
    with st.expander("Chapter 6.5 – Rama feels sad thinking about Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.5.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.6
    with st.expander("Chapter 6.6 – Ravana asks advice from his people"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.6.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.7
    with st.expander("Chapter 6.7 – The demons encourage Ravana"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.7.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.8
    with st.expander("Chapter 6.8 – Ravana’s generals boast proudly"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.8.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.9
    with st.expander("Chapter 6.9 – Vibhishana advises Ravana to return Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.9.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.10
    with st.expander("Chapter 6.10 – Vibhishana strongly repeats his advice"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.10.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.11
    with st.expander("Chapter 6.11 – Ravana calls a meeting of his court"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.11.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.12
    with st.expander("Chapter 6.12 – Ravana talks with Kumbhakarna"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.12.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.13
    with st.expander("Chapter 6.13 – Ravana tells an old story"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.13.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.14
    with st.expander("Chapter 6.14 – Vibhishana criticizes Ravana’s courtiers"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.14.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.15
    with st.expander("Chapter 6.15 – Vibhishana scolds Indrajit for boasting"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.15.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.16
    with st.expander("Chapter 6.16 – Ravana insults Vibhishana and sends him away"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.16.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.17
    with st.expander("Chapter 6.17 – The monkeys discuss Vibhishana"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.17.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.18
    with st.expander("Chapter 6.18 – Rama listens to the monkeys’ advice"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.18.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")
    # Chapter 6.19
    with st.expander("Chapter 6.19 – Vibhishana is brought before Rama"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.19.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.20
    with st.expander("Chapter 6.20 – Ravana sends Shuka to Sugriva"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.20.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.21
    with st.expander("Chapter 6.21 – Rama becomes angry at the sea god"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.21.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.22
    with st.expander("Chapter 6.22 – The army crosses the sea"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.22.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.23
    with st.expander("Chapter 6.23 – Rama sees good and bad signs"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.23.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.24
    with st.expander("Chapter 6.24 – Shuka tells Ravana how monkeys treated him"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.24.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.25
    with st.expander("Chapter 6.25 – Ravana sends spies Shuka and Sarana"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.25.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.26
    with st.expander("Chapter 6.26 – Sarana describes the monkey leaders"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.26.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.27
    with st.expander("Chapter 6.27 – Sarana continues his report"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.27.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.28
    with st.expander("Chapter 6.28 – Shuka also lists the enemy warriors"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.28.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.29
    with st.expander("Chapter 6.29 – Ravana sends more spies"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.29.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.30
    with st.expander("Chapter 6.30 – Shardula reports back to Ravana"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.30.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.31
    with st.expander("Chapter 6.31 – Ravana lies to Sita about Rama’s death"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.31.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.32
    with st.expander("Chapter 6.32 – Sita feels hopeless and sad"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.32.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.33
    with st.expander("Chapter 6.33 – Sarama comforts Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.33.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.34
    with st.expander("Chapter 6.34 – Sarama secretly watches Ravana’s plans"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.34.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.35
    with st.expander("Chapter 6.35 – Malyavan advises Ravana to make peace"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.35.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.36
    with st.expander("Chapter 6.36 – Ravana strengthens Lanka’s defenses"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.36.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.37
    with st.expander("Chapter 6.37 – Rama plans the attack"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.37.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.38
    with st.expander("Chapter 6.38 – The army climbs Mount Suvela"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.38.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.39
    with st.expander("Chapter 6.39 – Lanka is described in detail"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.39.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.40
    with st.expander("Chapter 6.40 – Sugriva and Ravana fight fiercely"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.40.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.41
    with st.expander("Chapter 6.41 – Rama sends Angada as a messenger"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.41.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.42
    with st.expander("Chapter 6.42 – The demons attack suddenly"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.42.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.43
    with st.expander("Chapter 6.43 – Monkeys and demons fight"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.43.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.44
    with st.expander("Chapter 6.44 – Angada shows great bravery"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.44.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.45
    with st.expander("Chapter 6.45 – Indrajit wounds Rama and Lakshmana"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.45.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.46
    with st.expander("Chapter 6.46 – The monkey army feels hopeless"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.46.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.47
    with st.expander("Chapter 6.47 – Sita sees Rama and Lakshmana fallen"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.47.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.48
    with st.expander("Chapter 6.48 – Sita cries in sorrow"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.48.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.49
    with st.expander("Chapter 6.49 – Rama wakes up and cries for Lakshmana"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.49.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.50
    with st.expander("Chapter 6.50 – Garuda frees Rama and Lakshmana"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.50.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.51
    with st.expander("Chapter 6.51 – Dhumraksha comes to fight"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.51.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.52
    with st.expander("Chapter 6.52 – Hanuman kills Dhumraksha"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.52.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.53
    with st.expander("Chapter 6.53 – Vajradamshtra enters the battle"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.53.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.54
    with st.expander("Chapter 6.54 – Angada kills Vajradamshtra"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.54.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.55
    with st.expander("Chapter 6.55 – Akampana attacks the monkeys"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.55.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.56
    with st.expander("Chapter 6.56 – Hanuman kills Akampana"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.56.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.57
    with st.expander("Chapter 6.57 – Prahasta comes to fight"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.57.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.58
    with st.expander("Chapter 6.58 – Prahasta is killed"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.58.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.59
    with st.expander("Chapter 6.59 – Ravana shows his power in battle"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.59.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.60
    with st.expander("Chapter 6.60 – The demons wake Kumbhakarna"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.60.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")
    # Chapter 6.61
    with st.expander("Chapter 6.61 – The story of Kumbhakarna is told"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.61.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.62
    with st.expander("Chapter 6.62 – Kumbhakarna meets Ravana"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.62.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.63
    with st.expander("Chapter 6.63 – Kumbhakarna comforts Ravana"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.63.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.64
    with st.expander("Chapter 6.64 – Mahodara gives advice"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.64.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.65
    with st.expander("Chapter 6.65 – Kumbhakarna joins the battle"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.65.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.66
    with st.expander("Chapter 6.66 – Angada scolds the fleeing monkeys"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.66.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.67
    with st.expander("Chapter 6.67 – Kumbhakarna fights fiercely"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.67.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.68
    with st.expander("Chapter 6.68 – Ravana mourns Kumbhakarna’s death"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.68.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.69
    with st.expander("Chapter 6.69 – Angada kills Narantaka"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.69.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.70
    with st.expander("Chapter 6.70 – Many demon warriors are killed"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.70.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.71
    with st.expander("Chapter 6.71 – Lakshmana kills Atikaya"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.71.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.72
    with st.expander("Chapter 6.72 – Ravana makes new battle plans"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.72.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.73
    with st.expander("Chapter 6.73 – Invisible Indrajit defeats the monkeys"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.73.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.74
    with st.expander("Chapter 6.74 – Hanuman brings the healing mountain"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.74.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.75
    with st.expander("Chapter 6.75 – Monkeys set Lanka on fire"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.75.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.76
    with st.expander("Chapter 6.76 – Angada kills Kumbha"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.76.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.77
    with st.expander("Chapter 6.77 – Hanuman fights Nikumbha"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.77.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.78
    with st.expander("Chapter 6.78 – Maharaksha attacks Rama and Lakshmana"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.78.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.79
    with st.expander("Chapter 6.79 – Rama kills Maharaksha"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.79.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.80
    with st.expander("Chapter 6.80 – Indrajit returns to battle"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.80.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.81
    with st.expander("Chapter 6.81 – Indrajit tricks the army with illusion"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.81.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.82
    with st.expander("Chapter 6.82 – Hanuman rallies the monkeys"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.82.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.83
    with st.expander("Chapter 6.83 – Lakshmana speaks bravely"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.83.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.84
    with st.expander("Chapter 6.84 – Vibhishana comforts Rama"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.84.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.85
    with st.expander("Chapter 6.85 – Lakshmana goes to fight Indrajit"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.85.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.86
    with st.expander("Chapter 6.86 – Indrajit stops his ritual to fight"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.86.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.87
    with st.expander("Chapter 6.87 – Indrajit and Vibhishana argue"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.87.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.88
    with st.expander("Chapter 6.88 – Lakshmana and Indrajit fight"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.88.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.89
    with st.expander("Chapter 6.89 – The fierce battle continues"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.89.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.90
    with st.expander("Chapter 6.90 – Indrajit loses his chariot and horses"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.90.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.91
    with st.expander("Chapter 6.91 – Indrajit is killed"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.91.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.92
    with st.expander("Chapter 6.92 – Lakshmana is healed"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.92.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.93
    with st.expander("Chapter 6.93 – Ravana mourns his son’s death"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.93.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.94
    with st.expander("Chapter 6.94 – Rama fights bravely"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.94.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.95
    with st.expander("Chapter 6.95 – Demon women cry in grief"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.95.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.96
    with st.expander("Chapter 6.96 – Ravana goes to fight and sees bad signs"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.96.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.97
    with st.expander("Chapter 6.97 – Sugriva fights Virupaksha"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.97.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.98
    with st.expander("Chapter 6.98 – Sugriva kills Mahodara"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.98.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.99
    with st.expander("Chapter 6.99 – Angada fights Mahaparshva"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.99.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.100
    with st.expander("Chapter 6.100 – Rama and Ravana fight with magic weapons"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.100.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.101
    with st.expander("Chapter 6.101 – Ravana runs away from battle"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.101.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.102
    with st.expander("Chapter 6.102 – Lakshmana recovers fully"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.102.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.103
    with st.expander("Chapter 6.103 – Rama and Ravana fight again"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.103.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.104
    with st.expander("Chapter 6.104 – The battle continues"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.104.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.105
    with st.expander("Chapter 6.105 – Rama scolds Ravana for his sins"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.105.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.106
    with st.expander("Chapter 6.106 – Ravana scolds his charioteer"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.106.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.107
    with st.expander("Chapter 6.107 – Rama prays to the Sun God"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.107.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.108
    with st.expander("Chapter 6.108 – Bad signs appear"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.108.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.109
    with st.expander("Chapter 6.109 – The battle rises and falls"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.109.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.110
    with st.expander("Chapter 6.110 – The duel continues"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.110.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.111
    with st.expander("Chapter 6.111 – Rama kills Ravana"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.111.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.112
    with st.expander("Chapter 6.112 – Vibhishana mourns Ravana"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.112.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.113
    with st.expander("Chapter 6.113 – Ravana’s wives cry"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.113.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.114
    with st.expander("Chapter 6.114 – Mandodari mourns and Ravana’s funeral is done"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.114.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.115
    with st.expander("Chapter 6.115 – Vibhishana becomes king of Lanka"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.115.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.116
    with st.expander("Chapter 6.116 – Hanuman carries Rama’s message to Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.116.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.117
    with st.expander("Chapter 6.117 – Rama sends Sita away"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.117.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.118
    with st.expander("Chapter 6.118 – Rama rejects Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.118.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.119
    with st.expander("Chapter 6.119 – Sita passes the fire test"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.119.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.120
    with st.expander("Chapter 6.120 – Brahma praises Rama"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.120.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.121
    with st.expander("Chapter 6.121 – Sita is reunited with Rama"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.121.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.122
    with st.expander("Chapter 6.122 – Dasharatha appears and blesses Rama"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.122.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.123
    with st.expander("Chapter 6.123 – Indra brings back the fallen army"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.123.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.124
    with st.expander("Chapter 6.124 – Vibhishana gives Pushpaka chariot to Rama"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.124.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.125
    with st.expander("Chapter 6.125 – Rama starts the journey to Ayodhya"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.125.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.126
    with st.expander("Chapter 6.126 – Rama shows places to Sita on the way"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.126.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.127
    with st.expander("Chapter 6.127 – Rama meets Sage Bharadvaja"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.127.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.128
    with st.expander("Chapter 6.128 – Rama sends Hanuman to Bharata"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.128.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.129
    with st.expander("Chapter 6.129 – Hanuman tells Bharata the full story"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.129.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.130
    with st.expander("Chapter 6.130 – Bharata goes to meet Rama"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.130.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.131
    with st.expander("Chapter 6.131 – Rama is crowned king of Ayodhya"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.131.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")
