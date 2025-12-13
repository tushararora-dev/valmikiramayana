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
    create_image_text_layout("attached_assets/chapter5/chapter5.jpg", layout="full")
    create_image_text_layout("attached_assets/chapter5/banner5.jpg", layout="full")


    text0 = """
    <h2>Chapter 5: Sundara kanda</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")
    # Chapter 5.1
    with st.expander("Chapter 5.1 – Hanuman starts his journey to Lanka"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.1.jpg", text1,  layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.2
    with st.expander("Chapter 5.2 – Hanuman reaches the city of Lanka"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.2.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.3
    with st.expander("Chapter 5.3 – Hanuman enters Lanka quietly"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.3.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.4
    with st.expander("Chapter 5.4 – Hanuman looks at the city and its people"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.4.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.5
    with st.expander("Chapter 5.5 – Hanuman searches the city but cannot find Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.5.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.6
    with st.expander("Chapter 5.6 – Hanuman explores Ravana’s palace"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.6.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.7
    with st.expander("Chapter 5.7 – Hanuman sees the flying chariot Pushpaka"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.7.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.8
    with st.expander("Chapter 5.8 – More details about the Pushpaka chariot"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.8.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.9
    with st.expander("Chapter 5.9 – Hanuman searches the women’s palace"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.9.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.10
    with st.expander("Chapter 5.10 – Hanuman sees Ravana with his wives"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.10.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.11
    with st.expander("Chapter 5.11 – Hanuman sees the grand dining hall"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.11.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.12
    with st.expander("Chapter 5.12 – Hanuman feels sad and worried"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.12.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.13
    with st.expander("Chapter 5.13 – Hanuman feels confused and troubled"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.13.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.14
    with st.expander("Chapter 5.14 – Hanuman reaches the Ashoka garden"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.14.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.15
    with st.expander("Chapter 5.15 – Hanuman sees Sita for the first time"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.15.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.16
    with st.expander("Chapter 5.16 – Hanuman thinks deeply after seeing Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.16.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.17
    with st.expander("Chapter 5.17 – Hanuman sees the demon women guarding Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.17.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.18
    with st.expander("Chapter 5.18 – Ravana comes to the Ashoka garden"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.18.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.19
    with st.expander("Chapter 5.19 – Sita feels great sorrow"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.19.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.20
    with st.expander("Chapter 5.20 – Ravana asks Sita to marry him"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.20.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.21
    with st.expander("Chapter 5.21 – Sita strongly refuses Ravana"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.21.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.22
    with st.expander("Chapter 5.22 – Ravana threatens Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.22.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.23
    with st.expander("Chapter 5.23 – The demon women try to convince Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.23.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.24
    with st.expander("Chapter 5.24 – The demon women scare and threaten Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.24.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.25
    with st.expander("Chapter 5.25 – Sita feels hopeless"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.25.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.26
    with st.expander("Chapter 5.26 – Sita predicts the destruction of the demons"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.26.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.27
    with st.expander("Chapter 5.27 – Trijata tells her dream"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.27.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.28
    with st.expander("Chapter 5.28 – Sita cries and laments"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.28.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.29
    with st.expander("Chapter 5.29 – Sita notices good signs of hope"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.29.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.30
    with st.expander("Chapter 5.30 – Hanuman thinks about what to do next"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.30.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.31
    with st.expander("Chapter 5.31 – Hanuman praises Lord Rama"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.31.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.32
    with st.expander("Chapter 5.32 – Sita notices Hanuman"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.32.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.33
    with st.expander("Chapter 5.33 – Hanuman talks with Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.33.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.34
    with st.expander("Chapter 5.34 – Sita feels unsure and afraid of Hanuman"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.34.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.35
    with st.expander("Chapter 5.35 – Hanuman proves he is Rama’s messenger"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.35.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.36
    with st.expander("Chapter 5.36 – Sita asks Hanuman many questions"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.36.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.37
    with st.expander("Chapter 5.37 – Sita refuses to go with Hanuman alone"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.37.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.38
    with st.expander("Chapter 5.38 – Sita gives Hanuman her jewel"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.38.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.39
    with st.expander("Chapter 5.39 – Hanuman comforts and calms Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.39.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.40
    with st.expander("Chapter 5.40 – Hanuman says goodbye to Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.40.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.41
    with st.expander("Chapter 5.41 – Hanuman destroys the Ashoka garden"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.41.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.42
    with st.expander("Chapter 5.42 – Hanuman kills Ravana’s guards"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.42.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.43
    with st.expander("Chapter 5.43 – Hanuman destroys temples and buildings"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.43.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.44
    with st.expander("Chapter 5.44 – Hanuman kills the warrior Jambumalin"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.44.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.45
    with st.expander("Chapter 5.45 – Hanuman kills the sons of Ravana’s ministers"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.45.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.46
    with st.expander("Chapter 5.46 – Hanuman kills five generals and their armies"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.46.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.47
    with st.expander("Chapter 5.47 – Hanuman kills Aksha"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.47.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.48
    with st.expander("Chapter 5.48 – Hanuman allows himself to be captured"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.48.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.49
    with st.expander("Chapter 5.49 – Hanuman sees Ravana and is surprised"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.49.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.50
    with st.expander("Chapter 5.50 – Hanuman is questioned by the demons"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.50.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.51
    with st.expander("Chapter 5.51 – Hanuman speaks bravely and fearlessly"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.51.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.52
    with st.expander("Chapter 5.52 – Vibhishana asks Ravana to spare Hanuman"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.52.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.53
    with st.expander("Chapter 5.53 – Hanuman is taken through the city as a prisoner"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.53.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.54
    with st.expander("Chapter 5.54 – Hanuman burns the city of Lanka"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.54.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.55
    with st.expander("Chapter 5.55 – Hanuman worries about Sita’s safety"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.55.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.56
    with st.expander("Chapter 5.56 – Hanuman meets Sita again and takes leave"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.56.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.57
    with st.expander("Chapter 5.57 – Hanuman returns from Lanka"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.57.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.58
    with st.expander("Chapter 5.58 – Hanuman tells everyone about his journey"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.58.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.59
    with st.expander("Chapter 5.59 – Hanuman urges the monkeys to rescue Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.59.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.60
    with st.expander("Chapter 5.60 – Jambavan rejects Angada’s plan"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.60.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.61
    with st.expander("Chapter 5.61 – The monkeys destroy Madhuvana garden"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.61.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.62
    with st.expander("Chapter 5.62 – Dadhimukha fights the monkeys"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.62.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.63
    with st.expander("Chapter 5.63 – Dadhimukha tells Sugriva about the destruction"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.63.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.64
    with st.expander("Chapter 5.64 – Sugriva comforts Rama"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.64.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.65
    with st.expander("Chapter 5.65 – Hanuman tells Rama about meeting Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.65.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.66
    with st.expander("Chapter 5.66 – Rama feels deep sadness"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.66.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.67
    with st.expander("Chapter 5.67 – Hanuman describes his meeting with Sita in detail"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.67.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.68
    with st.expander("Chapter 5.68 – Hanuman repeats his comforting message to Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter5/5.68.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")
