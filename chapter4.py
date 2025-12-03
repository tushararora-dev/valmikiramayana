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
    create_image_text_layout("attached_assets/chapter4/chapter4.jpg", layout="full")
    create_image_text_layout("attached_assets/chapter4/banner4.jpg", layout="full")


    text0 = """
    <h2>Chapter 3: kishkindha kanda</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    # Chapter 4.1
    with st.expander("Chapter 4.1 – Rama talks about the beauty of spring and how it makes him feel"):
        text1 = """Rama aur Lakshman
    dheere-dheere Pampa Sarovar ki taraf badh rahe the.

    Jheel lotuses se bhari hui thi—
    laal, neele, safed, sab rangon ke.

    Jheel ka paani saaf, thanda,
    aur ped-paudhon se ghira hua tha.
    Rama ne dekha…
    aur unke dil me ek pal ke liye shanti aayi—
    par bas ek pal ke liye.

    Phir unka dard phir se jaag utha. """

        create_image_text_layout("attached_assets/chapter4/4.1.jpg", text1, layout="side", image_position="left")

        text2 = """🌸 Rama ka Pehla Dard – Basant ka Saundarya

    Rama ne kaha:

    “Lakshman… dekh to, Pampa kitni sundar lag rahi hai.
    Uska paani itna saaf hai jaise sheesha.
    Pedon par phool hi phool hain…
    jaise pahaad ne sheesha pehna ho.

    Par mere andar to dard hi dard hai.
    Bharat ki vyatha (pain)…
    Aur Sita ki yaad… dono mujhe tod rahi hain.”

    Lakshman chup-chap sunte rahe.

    Rama phir bole:

    “Basant aa gaya hai, Lakshman.
    Yeh mausam prem ka mausam hota hai.
    Har ped, har phool,
    har hawaa…
    jaise prem ka geet ga rahi ho.

    Kabhi yeh sab mujhe khush karta tha…
    Sita ke saath.”

    🌺 Basant, Phool, Hawa… Sab Sita ki Yaad Dilaate Hain

    Rama katha jari rakhte hain—

    “Dekh, kaise hawaa phoolon ko hilaa rahi hai.
    Patte udte hain…
    jaise unhe hawa naacha rahi ho.

    Pahaadon ki ghaatiyon me
    pedon se barish ki tarah phool gir rahe hain.

    Aur yeh madhumakkhiyan…
    in ki gunjan (humming)
    jaise prem ka dhun bajaa rahi ho.

    Jab Sita yeh awaaz sunti thi na…
    woh hasti thi, bulati thi mujhe,
    ‘Rama, suno!’

    Aaj woh nahi hai…
    aur yeh sab mujhe dard deta hai.”

    🥀 Rama ki Virah-Agni (Fire of Separation)

    Rama ne dukh se kaha:

    “Lakshman, basant ki yeh breeze (hawa)…
    jo sabko sukoon deti hai,
    mujhe aag jaisi lag rahi hai.

    Ashoka ke phool,
    jo prem jagate hain,
    aaj mere dard ko aur badha rahe hain.

    Peacock dekho…
    kaise prem me nach raha hai!
    Aur uski peahen uske peeche bhaag rahi hai.
    Par meri peahen—Sita…
    to dushman chheen kar le gaya.”

    Unke shabd ruk gaye.
    Aankhon me aansu chamak ne lage.

    Lakshman ka mann bhi bhar aaya,
    par woh chup rahe.

    🌼 Har Cheez Sita ka Chehra Ban Jaati Hai

    Rama ne jheel ki taraf ishara karke kaha:

    “Lakshman…
    lotus ki pankhudiyan dekho…
    yeh Sita ki aankhon jaisi hain.

    Aur yeh hawa…
    jaise Sita ki saans ho.

    Har tree, har phool,
    har awaaz…
    jaise Sita mujhe bula rahi ho.

    Kaise jeeyun main bina uske?
    Kaise?”

    🦢 Pampa Sarovar ki Sundarta bhi Ab Dard Ban Gayi

    Rama ne jheel ka varnan kiya—
    saans ruki hui jaise awaaz me:

    “Yahan swan, karandav (water birds),
    Cakravaka, herons sab hain.

    Jheel me lotuses, lilies…
    aur unki sughandh hawa me.
    Pahaadon par phoolon ki laali,
    jaise sab kuch swarg ka tukda ho.

    Lakshman…
    agar Sita mere saath hoti,
    to main Indra ka swarg bhi na chaahoon.

    Par bina Sita…
    yeh sab paar-paar dard deta hai.”

    😞 Rama ka Sabse Gehraa Dard

    Rama ne phir kaha:

    “Lakshman…
    kaise bataaun Janaka ko ki unki beti kho gayi?
    Kaise mu dikhayun Maa Kaushalya ko?

    Kaise main Ayodhya jaa sakta hoon
    bina Sita ke?

    Tu wapas chale jaa, Lakshman.
    Bharat ke paas.
    Mujh me shakti nahi bachhi.”

    Rama ki awaaz toot gayi.

    🛡️ Lakshman ka Pratigya

    Tab Lakshman ne
    shaant par majboot awaaz me kaha:

    “Rama…
    himmat rakhiye.
    Abhi hamari yatra (journey) poori nahi hui.

    Ravana chahe patal me chhup jaaye…
    ya kisi Devi ke garbh me jaaye…
    main usse cheer daaloonga
    agar woh Sita ko wapas na kare.

    Mehnat se bada koi shastra (weapon) nahi.
    Aur hum dono milkar
    Sita ko laayenge.
    Yeh mera vachan hai.”

    Rama ne ghera saans liya…
    aur dheere-dheere sambhalne lage.

    🦧 Aur Phir—Sugriva ka Darshan

    Dono bhai
    Pampa Sarovar ko paar karte hue
    Rishyamuka parvat ki taraf badhe.

    Wahan, pedon ke peeche,
    ek vanar raja unhe dekh raha tha—

    Sugriva.

    Unki shakal, unka tej,
    unke dhanush teer,
    unke kadam—

    sab dekhkar
    Sugriva ghabra gaya.

    Aur woh
    apne vanar mitron ke saath
    chhup gaya.

    Usne socha:

    “Kaun hain yeh do shoorveer?
    Aur yahan kyun aaye hain?”

    Aur iss tarah
    Rama ki mulaqaat Sugriva se hone ka pal
    bahut kareeb aa gaya. """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.2
    with st.expander("Chapter 4.2 – Sugriva sends Hanuman to meet Rama"):
        text1 = """”
    Rama aur Lakshman
    Pampa ke paas pahunch gaye the—
    dono ke haath me bade talwar aur dhanush-baan.

    Door se
    yeh sab Sugriva ne dekha…
    Aur uska dil zor-zor se dhadakne laga. """

        create_image_text_layout("attached_assets/chapter4/4.2.jpg", text1, layout="side", image_position="left")

        text2 = """ 🐒 Sugriva ka Dar

    Sugriva ne apne chaaron taraf dekha—
    “Kidhar chhupu?
    Kaise bachun?”

    Woh itna ghabra gaya
    ki uske pair kaanpne lage.

    Usne apne mantriyon ko bola:

    “Yeh dono Bali ne bheje honge!
    Zaroor mere dushman bhai Bali ki taraf se aaye hain.
    Bark ke kapde pehenkar
    yahan tak aa gaye?
    Yeh toh mushkil hai!"

    Sugriva ke monkey-mitra bhi dar gaye.
    Sab uchhal-uchhal kar
    ek pahad se doosre par jaakar
    Sugriva ke aas-paas jama ho gaye.

    Unki chalangon se
    ped toot gaye,
    patthar hil gaye,
    aur janwaron me bhagam-bhag mach gayi.

    🐾 Hanuman ka Shaant Awaaz

    Sabke beech
    Hanuman khada hua—
    mastishk thanda,
    awaaz narm,
    par shabd pavitr.

    Usne Sugriva se kaha:

    “Swami, darr ko dil se nikaal dijiye.
    Yahan Bali ka koi nishaan nahi.
    Woh kathor (cruel) Bali
    yahan aas-paas kahin nahi.

    Aapka vanar-swabhav (monkey nature)
    darr me aa kar
    aapko saaf dekhne nahi de raha.

    Aap buddhimaan (wise) ho,
    par jab ek raja ghabra jaaye,
    toh woh sach ko pehchan nahi pata.”

    Sugriva thoda shaant hua.

    👑 Sugriva ka Shak

    Sugriva ne dheere se jawab diya:

    “Hanuman…
    yeh dono apne dhanush-baan ke saath
    dev-putron jaise lagte hain.
    Kaise na darun?

    Mujhe lagta hai
    Bali ne hi inhe bheja hai.
    Wo chalak aur chatur hai.
    Raja hamesha dusman par
    najar rakhte hain.

    Tum jao, Hanuman.
    Ek aam aadmi ki tarah jao.
    Unse milo.
    Unki baat suno.

    Unki chaal, bhaav, sab dekho.
    Unki drishti me imandari hai ya chhal,
    yeh jaancho.

    Pehle inka dil jitna.
    Phir pucho—
    ‘Aap kaun hain?
    Yahan kyun aaye hain?’”

    Sugriva ne aadesh diya.

    🌬️ Hanuman ka Sankalp

    Hanuman ne haath jod kar kaha:

    “Jaise aap ki aagya.”

    Aur phir—
    apni komal chal,
    apne madhur bachan,
    aur apne gyaan ke saath—

    Hanuman Rama aur Lakshmana se milne chala.

    Uska mann bahaadur,
    chehra shaant,
    aur chhati me Rama ke darshan ka anand."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.3
    with st.expander("Chapter 4.3 – Hanuman meets Rama for the first time"):
        text1 = """ 
    Sugriva ne aadesh diya—
    “Hanuman, jao aur un dono ko jaanchkar aao.”

    Aur Hanuman?
    Ek hi chalang me
    Rishyamuka parvat se utre
    aur Rama–Lakshman ke saamne aa khade hue."""

        create_image_text_layout("attached_assets/chapter4/4.3.jpg", text1, layout="side", image_position="left")

        text2 = """🕉️ Hanuman ka Roop-Badalna

    Hanuman ne apna vanar-roop chhod diya.
    Apni maya se
    woh ek sanyasi (wandering monk) ban gaye—
    malamal kapda, jata, kamandalu.

    Unki awaaz bilkul madhur,
    narm,
    aur poori vinamrata se bhari hui:

    “Namaskar, O Mahatmam!
    Aap dono kaun ho?”

    Hanuman ne dono bhaiyon ko namaskar kiya,
    aur fir unki tareef shuru:

    🌞 Hanuman ki Madhur Boli

    “O Tapasviyon!
    Aapka tej, aapka roop,
    aapki chal…
    sab dekh kar lagta hai
    jaise Devta yahan chale aaye hon.

    Aapka rang sona ki tarah chamakta hai,
    bahen-ke hue valkal (bark clothes) pehne ho,
    par aapke kandhe sher jaise mazboot!

    Aap dono ke dhanush-baan
    Indra ke astra jaise lagte hain.
    Aap dono me veerta, tejas,
    aur ek shanti hai—
    jaise Surya aur Chandra
    zamin par utar aaye hon.

    Par aap chup kyun ho?
    Main aapse prashna pooch raha hoon.”

    🐒 Hanuman Apna Parichay Deta Hai

    Thodi der baad Hanuman ne kaha:

    “Sugriva naam hai hamare Raja ka.
    Unhe unke bhai Bali ne vanvaas de diya.
    Woh bahut pareshan hain,
    aur aap jaise veer
    is jungle me kyun aaye—yeh jaanna chahte hain.

    Main Hanuman hoon—
    Pawanputra.
    Koi bhi roop dharan kar sakta hoon.
    Rishyamuka se aaya hoon
    Sugriva ke aadesh par.”

    Aur Hanuman chup ho gaya.

    🌺 Rama ka Prashansa-Bharā Muskaan

    Rama Hanuman ki baat suntay hi
    khil uthte hain.

    Woh Lakshmana se kehte hain:

    “Saumitri…
    yeh koi saadharan vyakti nahi.
    Iski baat se pata chalta hai—
    yeh Vedon ka gyata hai,
    vyakaran me nipun hai,
    aur baat karne me nirdoosh aur sahi.

    Iski boli me
    na ati-shabd hai,
    na kamee.
    Awaaz gehri, madhur,
    aur poori niyantran me hai.

    Jo raja
    aise dhoot (ambassador) bhejta hai,
    woh zaroor safal hota hai.”

    🎯 Lakshmana ka Namra Uttar

    Lakshmana ne Hanuman ko pranam karte hue kaha:

    “O Vidwan!
    Hum Sugriva ke gunon ke baare me sun chuke hain.
    Hum unhi ko dhoond rahe hain.
    Jo unka aadesh,
    so hamara kartavya.

    Hame unse milwao,
    O Mahabali Hanuman!”

    🌟 Hanuman ka Faisla

    Hanuman ka mann khush ho gaya.
    Woh sochta hai:

    “Yahi samay hai—
    Sugriva aur Rama ka milan karwana hoga.”

    Aur Pavanputra
    andar se anandit hokar
    un dono ko
    apne kandhon par bithakar
    Sugriva ke paas le jaane ke liye
    taiyyar ho gaya. """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.4
    with st.expander("Chapter 4.4 – Hanuman brings Rama and Lakshmana to Sugriva"):
        text1 = """ Hanuman ne jab Lakshmana ki vinamr aur pyaari baatein suni,
    toh uska mann khush ho gaya.
    Use pakka ho gaya ki—

    “Sugriva ka rajyapaalan zaroor wapas milega. Rama jaise dost mil gaye—abh jeet nischit hai!”

    🐒 Hanuman ka Prashna

    Hanuman ne muskurate hue Rama se poocha:

    “Prabhu, aap aur aapke bhai is kathin, jungli,
    darawne van me kyun aaye ho?
    Kis kaam ke liye?”

    Rama chup rahe,
    aur Lakshmana ne Rama ke sanket par
    poora iti-haas sunaana shuru kiya."""

        create_image_text_layout("attached_assets/chapter4/4.4.jpg", text1, layout="side", image_position="left")

        text2 = """ 👑 Lakshmana Rama ka Parichay Dete Hain

    Lakshmana ne kaha:

    “Ek samay tha,
    Ayodhya me ek mahan raja rajya karta tha—
    Dasharatha.

    Woh dharm ka rakshak,
    sab jatiyon ka palankarta,
    sabse dayaalu aur nishpaksh…
    jaise dharti par koi dusra Brahma hi ho.

    Unka pehla putra—
    Rama,
    gunon ka sagar,
    raj-dharma me mahir,
    sab logon ka aadhaar.

    Par fate ne kuch aur hi likh rakha tha—
    Kaikeyi ki maang par
    Rama ko vanvaas mila.

    Aur bina ek shabd ki shikayat,
    Rama ne pita ka vachan nibhaaya.”

    Lakshmana ki awaaz yahan nam ho gayi.

    “Unki patni Sita ji,
    sandhya ke laal rang ki sauteli roshni ki tarah,
    unke peeche-peeche van me aa gayi…

    Aur main—main Lakshmana,
    inka chhota bhai,
    inka daas,
    inka sevak,
    inka rakshak—
    inka saaya ban kar saath aaya.

    Par jab hum van me the,
    ek Mayavi rakshasa—
    jo apni ichchha se roop badal sakta tha—
    Sita ko akela paa kar utha le gaya.

    Pata nahi kaun tha,
    kaun le gaya,
    kahan le gaya.”

    Hanuman shant hokar sunte rahe.

    Lakshmana fir bole:

    “Kabandha ne hame ek naam diya—
    Sugriva.
    Usne kaha ke Sugriva hi Sita ka pata lagwane me madad karega.

    Isliye hum yahan aaye hain—
    Sugriva ki sharan me.”

    Aur Lakshmana ke aankhon me aansu aa gaye.

    🌺 Hanuman Ki Karuna

    Hanuman ne madhur awaaz me kaha:

    “Rama jaise gyani,
    sahansi,
    aur dhairyavaan vyakti,
    jo apne gusse aur indriyon par poora niyantran rakhte hain—
    aise log
    sach me sahayog ke haqdar hain!

    Sugriva bhi waise hi dukh me hai,
    jaise aap ho.

    Uska raj chhin gaya,
    uski patni usse cheen li gayi,
    bhai ne use sataya,
    aur woh dar ke maare
    Rishyamuka me chhupa hai.

    Aap dono ka dukh aur uska dukh ek hi hai.
    Woh zaroor aapka mitra banega.
    Mitarta aur vachan-badhata ka pakka hai woh.

    Chaliye,
    main aapko Sugriva ke paas le chalta hoon.”

    🙏 Lakshmana Ka Sammaan

    Lakshmana ne Hanuman ko pranam kiya aur Rama se kaha:

    “Prabhu,
    yeh Hanuman—Pawan putra—sach bol raha hai.
    Iski mukhaakriti,
    iski awaaz,
    iski bhasha…
    sab dayalu aur satya se bhari hai.

    Sugriva jaroor aapki madad karega.”

    🐒 Hanuman Apna Sacha Roop Dharen

    Hanuman ek pal me
    apna sanyasi-roop tyag kar
    apne asli vanar-roop me aa gaye—
    balwan, tejomay,
    pawan ki tarah swatantra.

    Phir kaha:

    “Aao Prabhu,
    aap dono mere kandhon par baith jao.”

    Rama aur Lakshmana
    Hanuman ke kandhon par chadh gaye—
    jaise do devta
    Pawanputra ke upar viraajman ho gaye hon.

    🏔️ Hanuman ki Mahaa-Chalang

    Hanuman ne ek zor se
    “Jai Shri Rama!”
    kahkar
    aakaar-vishal chalang lagayi।

    Ek hi pal me
    woh parvat ki unchaiyon par pahunch gaye,
    aur Sugriva ke paas
    Rama-Lakshmana ko lekar utar pade।"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.5
    with st.expander("Chapter 4.5 – Rama and Sugriva become friends and make an alliance"):
        text1 = """Hanuman Rishyamuka se ek hi chalang me
    Malaya parvat par pahunch gaya,
    aur Rama–Lakshmana ko
    Sugriva ke saamne pesh kiya.

    Hanuman ne shraddha se bola:

    “Maharaj Sugriva,
    yeh Rama hain—
    Ikshvaku vansh ke veer,
    Dasharatha ke putra,
    aur yeh unke bhai Lakshmana.”

    Phir Hanuman ne sab kuch bataaya—
    Rama ka banvaas,
    Sita ka haran,
    aur unki dukh bhari yatra.

    Usne kaha:

    “Sugriva, in dono veeron ko tumhari madad chahiye.
    Inhe apne mitra ke roop me apna lo.” """

        create_image_text_layout("attached_assets/chapter4/4.5.jpg", text1, layout="side", image_position="left")

        text2 = """🤝 Sugriva ka Hari Hua Dil

    Hanuman ki baatein sun kar Sugriva ka mann pighal gaya.
    Use laga jaise achanak
    andhere me roshni aa gayi ho.

    Woh bola:

    “Rama!
    Mere jaise vanar ke saath dosti karne ki ichchha…
    yeh mere liye sabse bada vardaan hai.”

    Phir Sugriva ne apna haath Rama ki or badhaya:

    “Yadi tum chaho,
    to hum dono aaj se mitra ban jayein.”

    Rama ka chehra khil utha.
    Unhone Sugriva ka haath pakad liya—
    mazboot, snehipurn, sachi dosti ka haath.

    Aur dono veer gale lag gaye.

    🔥 Agni Saakshi

    Hanuman ne turant
    do kathiyon ko ghis kar
    agni prajwalit ki.

    Phoolon ki ahuti di gayi,
    agni madham si chamki,
    aur dono uske chaaron or ghoome.

    Agni ko saakshi bana kar
    Rama aur Sugriva ki dosti
    hamesh ke liye band gayi.

    Dono ek-doosre ko dekh kar
    muskurana band hi nahi kar pa rahe the.

    🌿 Van Ki Gadi Par Baithkar Vachan

    Sugriva ne ek bada sa,
    phoolon se bhara sala ka daal toda
    aur use bichha diya.

    Rama ke saath baithkar bola:

    “Aaj se tum mere sukh-dukh ke saathi ho.
    Hum ek hain.”

    Hanuman ne Lakshmana ke liye
    sandal ki sugandhit daali bichhai.

    Wahan baithkar Sugriva apni dard bhari kahani sunane laga…

    💔 Sugriva ka Dard

    “Rama,”
    uski awaaz laraz rahi thi,
    “Bali ne meri patni chheen li…
    mera rajya cheen liya…
    aur mujhe maar daalne ka prayas kiya.

    Main dara hua hoon.
    Bahut dara hua hoon.

    Mujhe bachao.
    Mujhe meri patni aur mera rajya wapas dilao.”

    Uski aankhon me aansu aa gaye.

    ⚔️ Rama ka Vachan: 'Main Bali ko maar doonga'

    Rama ne halka sa muskurate hue kaha:

    **“Sugriva,
    dosti ka phal hota hai—sahayata.
    Aur main apne mitra ka dukh nahi dekh sakta.

    Bali ko
    meri
    ek hi teer se
    zamin par gira doonga.

    Mere baan—
    yeh jo Indra ke vajra jaisi chamak rakhte hain—
    aaj hi us dusht Bali ke seene me utarenge.

    Tayyari karo.
    Aaj Bali marega.”**

    Sugriva ki aankhon me
    aas ki roshni chamak uthi.

    ✨ Teeno Lokon Me Shakun

    Jab Rama–Sugriva ki dosti bani—

    Sita ka baayan ankha (left eye) phadka…
    jaise dukh me ummeed ki ek kiran jaag uthi.

    Sugriva ka baayan ankha bhi phadka—
    jaise rajya wapas milne ka sanket mil gaya.

    Aur door Lanka me
    Ravana ka baayan ankha jerka—
    jaise uske vinaash ka shubh-aarambh ho gaya ho. """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.6
    with st.expander("Chapter 4.6 – Sugriva shows Rama Sita’s clothes and jewelry"):
        text1 = """
    Sugriva, dosti ke is naye bandhan se khush hokar,
    Rama se phir bola:

    “Rama, mujhe tumhari poori kahani
    Hanuman ne bata di hai.
    Tum aur Lakshmana kyon jungle–jungle bhatak rahe ho—
    sab jaanta hoon.”

    Phir uski awaaz dheemi ho gayi:

    “Maithili—tumhari priya Sita—
    use ek raakshas (demon) utha le gaya.
    Bechari roti hui le jaayi gayi,
    aur Jatayu jaise mahan pakshi ko bhi maar diya gaya.”

    Sugriva ne Rama ko dhairya dete hue kaha:

    “Rama, chinta mat karo.
    Sita jahan kahin bhi ho—
    swarg me (heaven) ho ya paataal me (hell)—
    main use dhoondh kar laaunga.
    Yeh mera vachan hai!” """

        create_image_text_layout("attached_assets/chapter4/4.6.jpg", text1, layout="side", image_position="left")

        text2 = """ 
    🌪️ “Maine Sita ko dekha tha…”

    Sugriva yaad karta hai:

    “Ravana jaise dusht raakshas
    Sita ko zor se pakad kar le ja raha tha.
    Woh cheekh rahi thi:
    ‘Rama! Lakshmana!’
    aur poori shakti se chhootne ki koshish kar rahi thi.”

    Phir Sugriva ne ek aur baat kahi jo Rama ke dil ko kaamp gayi:

    “Jab Sita ne mujhe upar pahad par dekha,
    toh usne apni odhani aur gehne neeche gira diye—
    shayad isliye ki koi unko dekhkar tum tak sandesh pahunchaye.”

    “Woh sab maine sambhal kar rakhe hain, Rama.
    Agar chaho to main turant le aaun.”

    Rama ka dil dhadak utha.

    “Sugriva,
    jaldi lao!
    Meri Sita ne jo chhoda…
    main dekhna chahta hoon…”

    🪔 Sita ke Gehno Ka Darshan

    Sugriva turant pahad ki ek gehri gufa me dauda
    aur pyaar se sambhale hue kapde aur gehne laa kar
    Rama ke saamne rakh diye.

    “Yeh lo, Rama…
    yeh wahi hain.”

    Rama ne kapda aur gehne apne haath me liye…
    aur turant hi
    unki aankhon me aansu bhar aaye.

    Unke haath kaanpte rahe.
    Unka dil toot gaya.

    Jaise badal chaand ko dhundhla kar dete hain,
    waise hi
    aansu ne Rama ki drishti dhundla di.

    Rama zameen par gir pade—
    aur sirf ek hi shabd nikla:

    “Sita…”

    💔 Rama ka Vilap

    Sita ki odhani ko apne seene se lagakar
    Rama ne bhari saanson me kaha:

    “Lakshmana,
    dekho…
    yeh Sita ke gehne hain.
    Usne bhaagte hue inhe gira diya hoga.”

    Lakshmana ne gehno ko dekha
    aur dheere se bola:

    “Bhaiya…
    main unke kangans ya jhumke nahi pehchanta…
    par haa…
    in payalon ko pehchanta hoon.
    Main unke charanon ko hi to pranam karta tha.”

    Rama ka dard aur gehra ho gaya.

    ⚔️ Rama ka Pratigya

    Rama ne Sugriva ki or dekha—
    aankhon me agni thi.

    “Sugriva, mujhe batao—
    Sita ko kahan dekha?
    Kaun tha wo raakshas?
    Uska naam kya hai?
    Kahan chhipa hai?”

    Phir Rama garaj uthe:

    “Usne Sita ko chhua bhi kaise?
    Aaj hi uska ant hoga.
    Aaj hi!”

    Jungle ka hawa bhi tharr gayi
    Rama ke iss pratigya se."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.7
    with st.expander("Chapter 4.7 – Sugriva comforts Rama"):
        text1 = """
    Rama ab bhi Sita ke dukh me toot chuke the.
    Unki aankhon me aansu the, awaaz kaap rahi thi.

    Tab Sugriva, jisne abhi-abhi Rama se dosti ki thi,
    haathon ko jod kar, aankhon me aansu lekar bola:

    💬 “Rama, sach kahu… mujhe nahi pata Ravana kahan rehta hai.”

    “Na main jaanta hoon uski shakti,
    na uska vansh,
    na uska bal…
    par ek baat sure hai—

    Main apni poori taaqat se tumhari Sita ko wapas laaunga!”

    Sugriva ki awaaz bharayi hui thi.

    “Ravana aur uske poore vansh ka vinaash kar dunga!
    Par pehle, Rama…
    apne aap ko sambhalo.” """

        create_image_text_layout("attached_assets/chapter4/4.7.jpg", text1, layout="side", image_position="left")

        text2 = """
    💬 “Tum jaise veer purush ko aise tootna shobha nahi deta.”

    Sugriva ne apna dukh yaad kiya, phir dheere se bola:

    “Rama, meri bhi patni mujhse chheen li gayi thi.
    Maine sab kuch khona—
    apni rani, apna raj, apni izzat…
    par phir bhi main gira nahi.

    Main to ek vanar hoon, phir bhi himmat rakhta hoon.
    Tum to dharti ke upar sabse shreshth ho.
    Tum kaise haar maan sakte ho?”

    💬 “Dukh me doobne wale ka haal doobi hui naav jaisa hota hai…”

    Sugriva ne bahut pyaar se samjhaya:

    “Jo aadmi dukh se haar jaye,
    woh samundar me doobti hui naav ki tarah
    nash ho jaata hai.

    Par jo himmat rakhta hai—
    uski har ladaai surakshit hoti hai.”

    Phir haath jodkar bola:

    “Rama, mere dost…
    udhaar mat toot jao.
    Jo dukh me khud ko kho deta hai,
    woh kabhi jeet nahi paata.”

    ✨ Sugriva ke shabdon se Rama phir se majboot hue

    Sugriva ki baaton ne Rama ko andar tak chhoo liya.

    Rama ne apna chehra apni vastra ki koni se poncha,
    aankhon ke aansu bhari saans ke saath ruk gaye.

    Phir Rama ne Sugriva ko gale lagaya aur bola:

    💬 “Sugriva… tum sacche dost ho.”

    “Tumne dosti ka haq nibhaya hai—
    izzat se, pyaar se, himmat se.

    Tumhari baaton ne mujhe phir apna bana diya.
    Jo kuch tumne kaha—
    woh mere dil me utar gaya.”

    Phir Rama ne gambhir ho kar kaha:

    “Sita zinda milegi.
    Ravana marega.
    Mera shabd kabhi jhootha nahi hota.”

    Sugriva ne Rama ki baat suni
    aur uske dil me ek tezz khushi chamak uthi.

    Usse lag gaya—
    “Ab sab theek hoga. Ab hamari jeet nishchit hai.” """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.8
    with st.expander("Chapter 4.8 – Sugriva asks Rama to help him fight Bali"):
        text1 = """
    Sugriva, Rama ki baaton se bahut prasan ho gaya.
    Uske chehre par pehli baar varshon baad aastha ki roshni chamki.

    Woh apne hriday se bol pada:

    💬 “Rama, devta mere upar kripa kar rahe hain…”

    “Mujhe itna uttam, gunon se bhara dost mila—
    yeh meri kismat ka sabse bada vardaan hai!

    Agar tum saath ho, to swarg ka rajya bhi jeet sakta hoon.
    To phir apna khoya hua rajya dobara kyon nahi?”

    Sugriva ne jhuk kar kaha:

    “Aaj jab hamne agni ko sakshi bana kar dosti ki…
    Rama, main garv se kah sakta hoon—
    tum mere mitra ho.” """

        create_image_text_layout("attached_assets/chapter4/4.8.jpg", text1, layout="side", image_position="left")

        text2 = """
    🍃 Sala Par Baithkar Do Dost

    Agli subah, Sugriva ne Rama ko apne paas dekha.
    Jungle ka maahol shaant tha, aur unke paas ek bada sa, phoolon se bhara Sala vriksha khada tha.

    Sugriva ne ek mota, komal patti-patti wala shaakh todkar zameen par bichhaya
    aur Rama ko saath baithne ko kaha.

    Hanuman bhi ek shaakh tod kar Lakshmana ke liye bicha deta hai—
    pura drishya ek parvat ki unchai par dosti ka, vishwas ka varmala jaisa lag raha tha.

    💬 Sugriva ka Ruda Hua Dil

    Shaant baithkar, Sugriva ne halka sa jhuk kar,
    awaz me halka sa kampan lekar bola:

    “Rama… mera bhai Bali mujhe barbaad kar chuka hai.
    Mujhe kisi ka sahara nahi.
    Meri patni chheen li gayi…
    mera rajya chheen liya…
    aur main dar ke saaye me jee raha hoon.
    Mujhe bachao…”

    Uski aankhon me aansu aa gaye.

    💬 Rama ka Vachan

    Rama muskura kar, par dridhata ke saath bole:

    “Dosti ka phal sahayata hota hai.
    Aur dushmani ka phal vinash.

    Aaj hi Bali marega.
    Mere teer — yeh jo sunehre pankhon wale, vajra jaise teer tum dekh rahe ho—
    Bali ko yahin gira denge.

    Woh durjan parvat ki tarah dhool ban jayega.”

    Sugriva ka chehra chamak utha.

    💬 “Rama… main to dukh se toot gaya tha…”

    Sugriva apna seena dabakar roya:

    “Rama, tum mere dukh se kis kadar prem rakhte ho…
    yeh dekhkar meri saansein bhar aati hain.

    Main tumse sachchai se keh raha hoon—
    meri har khushi, mera jeevan,
    sirf tab wapas milega
    jab Bali marega!”

    Phir aansu saaf karke
    woh khud ko sambhalta hai,
    aur kehne lagta hai:

    “Rama, mera dukh mujhe kha raha hai.
    Woh mere dushman hi nahi—
    mere jeevan ki ek zakham ban gaya hai.”

    💬 Rama ka Prashna

    Rama ne gehri shanti me poocha:

    “Sugriva, tumhari aur Bali ki dushmani ka mool kya hai?
    Mujhe batao.
    Poora kasht batao.
    Jab tak main karan na jaan loon,
    main kaise lad sakta hoon?”

    Usne apna dhanush utha kar kaha:

    “Jab main apna baan chhod dunga,
    tab tumhara dushman pehle hi mar chuka hoga.”

    Sugriva aur uske mantri khushi se chamak uthe.
    Sugriva ne phir Rama ko
    apni poori kahani sunani shuru ki—
    apne dukh ka,
    Bali ki kathorta ka,
    aur apne vanvaas ka. """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.9
    with st.expander("Chapter 4.9 – Sugriva tells Rama the story of Bali and Mayavi"):
        text1 = """
    Sugriva ne gehri saans li, jaise purani yaadon ka bojh phir se kandhon par aa gaya ho.
    Usne Rama ki taraf dekha, aur dheere-dheere batane laga—

    💬 “Rama, mera bhai Bali kabhi mera sab kuch tha…”

    “Bali… mera bada bhai.
    Ghor shatruon ko bhi hila dene wala yodha.
    Maa-baap ka laadle, aur mera bhi adhar.

    Pitaji ke swargwas ke baad, usse hi rajya diya gaya.
    Main uske adheen tha—ek sevak ki tarah.
    Aur uske rajme main khushi se hi rehta tha.
    Usse kabhi koi shikayat nahi thi.” """

        create_image_text_layout("attached_assets/chapter4/4.9.jpg", text1, layout="side", image_position="left")

        text2 = """ 
    🔥 Mayavi ka Badla

    “Ek raat,” Sugriva ki awaaz me thodi dehshat thi,
    “jab sab so rahe the, ek daharna raat ke sannate ko cheer kar aayi.

    Woh tha Mayavi—Dundubhi ka putra—
    Bali ka prachand shatru.

    Woh Kishkindha ke dwar par aakar garajne laga:
    ‘Bali! Bahar aa! Mard ho to lad!’”

    Bali ne neend ke andar se hi, gusse se aankhen khol di.
    Hum sab—uski patniyan, main—use rokne aaye.
    Magar uske kroddh ke saamne koi kuch na thaa.
    Woh tufaan ki tarah bahar nikal gaya.

    🐒 “Main bhi uske peeche bhaaga…”

    “Bhai ko akela kaise jaane deta?”
    Sugriva kaha.

    Isliye, chahe Bali mana karta raha,
    phir bhi Sugriva uske peeche bhaag pada.

    Mayavi un dono ko dekh kar khud darte hue bhaag gaya.
    Raat ko chandni raaste par thi,
    beech me ghaas ke neeche ek bada sa andhera gufa-dwar chhupa tha.
    Mayavi seedha usme ghus gaya.

    🌑 Bali ka Aadesh: “Gufa ke darwaze se hilna mat!”

    Gufa ke muh par khade hoke, Bali ne kaha:

    “Sugriva, tu yahin ruka rehna.
    Main andar jaakar us rakshas ko maar kar hi aaoonga.”

    Sugriva ne bahut manaya—

    “Bhai, mat jao… yeh gufa ajeeb lag rahi hai…”

    Par Bali ne gusse me shraap dene ki dhamki di:

    “Ek kadam bhi mat hilna jab tak main na aa jaoon.”

    Phir woh andhere me gayab ho gaya.

    ⏳ Ek Saal… ek poora saal…

    Sugriva ki awaaz bhar aa gayi.

    “Rama… main ek saal tak us gufa ke muh par baitha raha.
    Ek saal!
    Na bhai ki awaz, na koi khabar.
    Mera hriday dar se bhar gaya tha.

    Phir ek din
    gufa se kachcha lahu aur jhaag behkar bahar aaya…”

    Sugriva kanp gaya.

    “Maine Mayavi ka garjan suna…
    Par Bali ki vijay ki garjana kabhi nahi suni.”

    “Tab mujhe laga—
    mera bhai mar gaya.”

    🪨 Gufa ko Pathar Se Bandhkar…

    “Main ro pada, aur socha ki rakshas bahar aa kar sabko maar dalega.
    Isliye maine gufa ke muh par ek pahad jaisa pathar laga diya…
    aur phir Kishkindha chala gaya.

    Wahan jaakar maine Bali ke liye shraaddh kiya,
    jal arpit kiya,
    aur apne dukh ko dil me daba kar chup raha.”

    Par mantriyon ko baat pata chal gayi.

    Rajya ko bina raja ke kaise chalayen?
    Isliye unhone Sugriva ko raja bana diya.

    💥 Par Bali to Zinda Tha…

    Sugriva ki aankhen dard se bhar gayi.

    “Rama… Bali mara nahi tha!
    Usne Mayavi ko maar kar,
    pathar hata kar,
    bahar nikal aaya.

    Aur jab usne dekha ki main rajgaddi par hoon…”

    Sugriva ki awaz toot gayi:

    “…uski aankhen laal ho gayi gusse se.
    Usne mujhe dhoorth kaha…
    vishwasghati kaha…
    aur mere mantriyon ko janjeero me bandh diya.”

    Sugriva ne aage kaha:

    “Main bhai ke charanon me gira—
    ‘sorry bhai, mujhe laga tum mar gaye…!’
    par usne mujhe shama nahi ki.
    Woh mujhe maar-na chahata tha.”

    🤲 Sugriva ka Antim Vachan

    Phir Sugriva ne Rama ki taraf dekh kar kaha:

    **“Rama… dushmani ki jad yahi hai.
    Maine koi paap nahi kiya tha…
    par Bali ne mujhe kabhi nahi samjha.

    Isliye main tumse madad maang raha hoon.”**"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.10
    with st.expander("Chapter 4.10 – Sugriva explains why Bali became angry with him"):
        text1 = """
    Sugriva ne dheere se Rama ki taraf dekha.
    Uski aankhon me dard bhi tha… aur thodi si sharam bhi—
    jaise ek bhai apna ghav phir se khol raha ho.

    🙏 Sugriva ki Antim Koshish: “Bhai, mujhe galat mat samajhna…”

    “Rama,” Sugriva bolna shuru karta hai,
    “jab Bali wapas aaya, woh bahut gusse me tha.
    Par main usse manana chahta tha.

    Main uske aage haath jodkar bola:

    ‘Bhai, tum vijayi ho.
    Mayavi mar chuka hai.
    Tumhare bina main kuch nahi.
    Yeh rajya bhi tumhara tha, tumhara hai.
    Main to bas sambhal raha tha.’”

    Sugriva ki awaaz bhar aati hai.

    “‘Main poore ek saal us gufa ke muh par tumhara intezaar karta raha.
    Fir lahu bahar aata dekha.
    Mujhe laga… tum mar gaye.
    Isliye, darr me, gufa ka muh patthar se bandh diya.
    Aur Kishkindha wapas aaya—bilkul toot kar.’” """

        create_image_text_layout("attached_assets/chapter4/4.10.jpg", text1, layout="side", image_position="left")

        text2 = """
    👑 “Main ne rajya nahi manga tha…”

    Sugriva ne aage kaha:

    “‘Raja banana mera irada nahi tha, Rama.
    Ministers aur praja ne mujhe majboori me gaddi de di—
    kyunki bina raja ke desh dushmano ka nishana ban jata.’”

    “‘Bhai, main tumse mafi maangta hoon.
    Kripya mujhe dushman mat samajhna.’”

    Par…

    Rama chup-chaap sunkar reh gaya,
    kyonki jo Sugriva ne aage bataya, woh aur bhi dardnaak tha.

    🔥 Bali ka Jawab: “Shraap ho tum par!”

    Sugriva ke bol band ho gaye jab usne yaad kiya:

    “Bali ne mujhe dekhte hi kaha—
    ‘Shapth ho tum par!’
    Aur baar-baar wahi kehkar sabke saamne mujhe zaleel kiya.”

    Bali ne praja aur mantriyon ke saamne gusse se ye kahani kahi:

    🔊 Bali ki Uttejit Kahani (Uski Nazar Se)

    “Ek raat Mayavi mujhe lalkar raha tha,”
    Bali garajta hai.

    “Main nikla, aur mere peeche-peeche ye Sugriva bhi aa gaya!
    Mayavi hum dono se dar kar gufa me bhag gaya.
    Maine Sugriva se kaha:
    ‘Main us rakshas ko marte bina wapas nahi aaunga.
    Tu yahan ruk kar mera intezaar kar!’”

    Bali ke chehre par krodh ubhar aata hai:

    “Poora ek saal main gufa me ladta raha.
    Mayavi aur uske parivaar ko maar diya.
    Uske lahu ne gufa bhar di.
    Main bahar aana chahta tha…
    par gufa ka muh to pathar se bandh tha!”

    “Main cheekhta raha—
    ‘Sugriva! Sugriva!’
    par koi jawaab nahi.
    Badi mushkil se pathar ko laat maarke hataaya aur bahar nikla.”

    Aur phir Bali ke shabd Sugriva ka dil cheer dete hain:

    “Sugriva ne mauka dekhkar raj le liya!
    Isi liye main usse nafrat karta hoon.”

    🥀 Sugriva ka Shraap: “Mujhe be-izzat karke nikal diya…”

    Sugriva ki awaaz patli ho jati hai.

    “Rama… usne mujhe sabke saamne apamaanit kiya.
    Ek hi vastra pehnaakar rajya se nikaal diya.
    Meri patni ko cheen liya…”

    “Main akela reh gaya—
    bas yeh Hanuman aur thode se dost mere saath the.”

    “Tabhi maine Rishyamuka par ashraay liya—
    jahan Bali, ek purane shraap ke kaaran, kadam bhi nahi rakh sakta.”

    🤲 Sugriva ka Vinamra Vachan

    **“Rama… yeh meri poori kahani hai.
    Maine kuch galat nahi kiya.
    Phir bhi mujhe yeh dukh mila.

    Aap hi mujhe mere bhai ke dar se bachaa sakte ho.”**

    ⚔️ Rama ka Pratigya

    Rama ne Sugriva ki kahani shant hansi ke saath suni.
    Phir usne apne teer ko dekha, jaise unme agni jag gayi ho.

    “Sugriva,” Rama ne kaha,
    “mere teer kabhi apna nishana nahi chookte.
    Bali ab zinda rahega—
    sirf tab tak jab tak main usse dekh nahi leta.”

    “Tum bhi dukh ke samundar me ho… main bhi.
    Aur main tumhe is dard se nikaal kar hi rahoonga.”

    Sugriva ki aankhon me umeed chamak uthi—
    usne apne jeevan ka sabse bada sahara pa liya tha. """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.11
    with st.expander("Chapter 4.11 – Sugriva tells Rama about Bali’s great strength"):
        text1 = """ 
Sugriva ne Rama ke saamne haath jodkar kaha:

“Rama, mujhe aap par pura vishwas hai…
par Bali ki taakat samajhna zaroori hai.”

Uski awaaz me darr bhi tha, aur sachchai bhi.

🌏 Bali ki Asambhav Shaktiyaan

Sugriva bolta gaya:

“Rama… Bali itna shaktishaali (powerful) hai ki…”

Subah hone se pehle poora prithvi chakra ghoom sakta hai—
west ocean se east ocean, north se south ocean tak.

Woh pahaadon ki chotiyan tod kar aasman me uchhal deta hai.

Ek saath kai-kai ped tod deta hai, jaise patle lakdi ho.

Rama chupchap sunte rahe—
Lakshmana ke chehre par bhi halki chinta aa gayi."""

        create_image_text_layout("attached_assets/chapter4/4.11.jpg", text1, layout="side", image_position="left")

        text2 = """ 
🦬 Dundubhi Rakshas (buffalo demon) ka ghamand

Sugriva ne phir Rama aur Lakshmana ki taraf dekhkar kaha:

“Ek baar ek maha-shaktishaali rakshas (demon),
Dundubhi naam ka,
jo pahad ke barabar bada aur
1,000 hathi ki shakti (strength) rakhta tha,
sab par apni taakat jatata phirta tha.”

⚔️ Dundubhi ka pehla challenge — Samudra Dev

Dundubhi garaj kar bolta hai:

“Aao Samudra, mujhse yuddh karo!”

Par Samudra Dev (Ocean God) shanti se jawab dete:

“Main lad nahi sakta.
Par ek aadmi hai—
Himavat (Himalaya)—
voh tum jaisa parakrami (valiant) se lad sakta hai.”

Dundubhi samajh gaya—Samudra ladna nahi chahta.
Toh woh seedha Himalaya ki taraf bhaag pada.

🏔️ Himavat se bhi haar

Himalaya ne bhi haath jodkar kaha:

“Main yoddha nahi, tapasiyon ka rakshak (protector) hoon.
Par agar ladne ka shauk hai—
Bali ko dhoondo!
Voh tumhare jaisa hi hai.”

Yeh sunkar Dundubhi bhaaga Kishkindha ki taraf…
Rage se bhar kar!

🐃 Dundubhi ka Kishkindha par prahar

Woh gaayab se ek bhayankar bhais (buffalo) ban gaya—
kale badal jaisa bhayanak aur bada!

Darwaze tod diye

Ped ukhaad diye

Poora shehar hila diya

Tab Bali apne mahal se bahar aaya—
Tara aur anya patniyon ke saath.

Bali ne thande sur me poocha:

“Dundubhi, kyun chilla raha hai?”

Dundubhi cheekha:

“Akele lad!
Main ek raat ruk sakta hoon…
Tu apni patniyon se vidai le le!
Kal subah teri maut nishchit hai.”

⚔️ Bali vs Dundubhi — Mahadangal

Bali ne hansi se kaha:

“Sharab (intoxication) yoddhaon ka bal hota hai!
Chalo, ladte hain!”

Aur yuddh shuru ho gaya.

Bali ne uske sing pakad liye

Usse zameen par patak diya

Ped, pathar, ghutne, mukke—sab se maara

Dundubhi ki taakat ghatti gayi

Bali ki shakti badhti gayi

Phir—

Bali ne uska pura badan utha kar 4 mile door pheka!

Dundubhi mar chuka tha.

🌧️ Khoon ki Boondein aur Matanga Rishi ka Shraap (curse)

Dundubhi ke moonh se nikla khoon hawa me udata hua
Matanga Rishi ke ashram par gira.

Rishi bahut krodhit hue.

“Kaun hai yeh paapi?
Isne mere van ko kalaankit kar diya!
Agar yeh bandar phir yahaan aaya…
Toh woh mar jayega!
Aur yahan aane wale sare vanar pathar ban jayenge (turn to stone).”

Yeh shraap sunkar Sare vanar bhaag gaye.

😨 Bali ka dar — Rishyamuka se doori

Bali Rishi se maafi maangne gaya,
par Rishi ne ek shabd bhi nahi suna.

Tab se Bali ne kasam kha li—

“Main Rishyamuka pahad ke 4 kos paas bhi nahi jaaunga.”

Isi liye Sugriva kehta hai:

“Rama, main yahaan Rishyamuka par isliye reh sakta hoon—
kyunki Bali ka shraap usse yahan aane nahi deta.”

🦴 Dundubhi ki Haddi aur Sala ke Ped — Bali ki Shakti ka Saboot

Sugriva Rama ko ek pahaad jaise dher par le gaya:

“Yeh Dundubhi ki haddi hai.
Aur Bali ne yeh 7 Sala ke ped—
ek ke baad ek—
apni ungli se bhida kar ched daale the.”

Sugriva ki awaaz dar se kaanp rahi thi:

“Rama… mujhe nahi lagta koi insaan Bali ko hara sakta hai.”

Lakshmana muskura diye:

“Sugriva, tumhe Rama ki shakti ka saboot chahiye?”

Sugriva ne faint si awaaz me kaha:

“Haan… agar Rama ek teer me
yeh 7 ped ched de,
toh main maan jaaunga ki woh Bali ko hara sakta hai.”

🌬️ Rama ka Shant Muskaan — “Tum par bharosa paida karunga”

Rama ne mithaas bhari muskaan ke saath kaha:

“Sugriva, tumhara vishwas zaroori hai.
Main usse jagaaunga.”

Rama ne dheere se apna paon uthaya
aur Dundubhi ki sookhi haddi ko aise uchaala
jaise ek patta hawa me lehrata ho.

Sugriva ne turant kaha:

“Rama, jab Bali ne pheka tha,
tab Dundubhi ka sharir taaza tha—bhaari tha.
Ab to yeh sookhi haddi hai!
Isse main kaise Tulna (comparison) karoon?”

“Aap ek baar Sala ke ped me teer chalaiye…
tab main poora vishwas karloonga.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.12
    with st.expander("Chapter 4.12 – Sugriva and Bali fight"):
        text1 = """
Sugriva ki baat sunte hi Rama muskura diye.
Unke chehre par woh shant par atoot vishwas tha.

🎯 Rama ne apni shakti dikhayi — 7 Sala Ped ek teer me!

Rama ne apna dhanush uthaya,
ek chamakta hua sunehra laathe wala teer nikaala,
aur nishana liya.

Phir TWAANG!!!

Teer aisi gati se chala
ki hawa bhi kaanp uthi.

Pehle ped ko cheda

Phir doosra

Teesra

Chautha…

Saathva tak ek hi teer guzar gaya

Phir pahaad ko bhi ched diya

Aur zameen me ghus kar phir wapas Rama ke tarquiver me aa gaya.

Sugriva aankh phaad kar dekhte reh gaye.

Unke muh se bas ek hi baat nikli:

“Rama… aap Bhagwan ho!”

Khushi se bhar kar woh Rama ke pairon me gir pade. """

        create_image_text_layout("attached_assets/chapter4/4.12.jpg", text1, layout="side", image_position="left")

        text2 = """
💛 Sugriva ka naya vishwas

Sugriva ne kandhe jhuka kar kaha:

“Aap to devtaon ko bhi hara sakte ho.
Bali to phir kya cheez hai?
Rama, ab main poori tarah nishchint hoon.
Mere dushman ko maar dijiye!”

Rama ne Sugriva ko gale laga liya,
jaise Lakshmana ko lagate the.

⚔️ Chalo, ab Bali ko aawaaz dete hain

Rama ne kaha:

“Chalo Kishkindha.
Tum Bali ko challenge do.
Main peeche se sab dekh raha hoon.”

Phir Rama, Lakshmana aur Sugriva Kishkindha ke paas pahad ke peeche chhup gaye.

Sugriva ne zor se garaj kar Bali ko lalkara:

“BAALIII!
Bahaar aa!”

Uski garaj se pura van kaanp utha.

😡 Bali nikla — Sooraj ki tarah bhayankar

Bali ne apne mahal se nikalte hi Sugriva ko dekha
aur uska khoon khaulta gaya.

Phir jo hua, woh apni aankhon se dekhne layak tha—

Dono bhai ek dusre par toot pade

Haath, mukke, pair, dharti—sab hila diya

Unki takkar aisi thi jaise Mangal aur Brihaspati grah takra rahe ho

Rama teer tayyar karke dekh rahe the.

Par ek samasya thi…

❗ Rama ne teer kyun nahi chalaaya?

Bali aur Sugriva dono bilkul ek jaise dikhe:

Ek hi rang

Ek hi aavaaz

Ek hi shakti

Ek hi kapde

Ek hi chal

Rama soch rahe the:

“Agar galti se Sugriva ko maar diya toh?
Yeh paap hoga.”

Isliye woh teer nahi chala sake.

🩸 Sugriva pit kar bhaaga

Bali ki taakat Sugriva par bhaari padi.
Usne Sugriva ko zor se patka,
uski chhati par ghamand se vaar kiya,
aur Sugriva khoon se latpat bhaag gaya,
seedha Rishyamuka parvat ki taraf.

Bali peecha kar sakta tha,
par shraap ki wajah se wahan nahi jaa sakta tha.

उसने चिल्लाकर कहा:

“Jaa! Aaj chhod diya!”

😢 Sugriva ki shikayat

Rama aur Lakshmana, Hanuman ke saath Sugriva ke paas pahunche.
Sugriva rote hue bola:

“Rama… aapne mujhe marne ke liye kyun chhod diya?
Aap ne kaha tha ‘Challenge karo’,
par aapne mujhe bachaya nahi.
Agar aap nahi maarna chahte the Bali ko…
toh mujhse pehle hi keh dete.”

Sugriva ka dil toot gaya tha.

🤲 Rama ka sachcha jawaab

Rama ne Sugriva ka haath pakadkar kaha:

“Mere dost…
tum dono ek jaise lag rahe the.
Main tumhe pehchaan hi nahi sakta tha!
Main kaise teer chalata?
Agar tum galti se mar jaate
toh mera dharm, meri kshatriyata, sab nasht ho jaata.”

Lakshmana ne turant Gajapushpi mala tod kar Sugriva ke gale me pehna di.

Rama ne kaha:

“Ab jab tum Bali se ladne jaoge,
main door se tumhari mala dekh kar pehchaan jaaunga.
Is baar Bali bach nahi payega.”

Sugriva ka chehra phir chamak utha.

Woh phir se Bali ko lalkarne ke liye tayyar ho gaya. """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.13
    with st.expander("Chapter 4.13 – Rama visits the hermitage of the seven sages"):
        text1 = """
Rama, Lakshmana aur Sugriva Rishyamuka se nikal pade.
Rama ke haath me sona jaisa chamakta dhanush,
peeche Lakshmana,
aur unke piche Hanuman, Nala, Neela, aur senapati Taara jaise veer vanar chal rahe the.

Sugriva ke gale me Gajapushpi ki mala chamak rahi thi—
jo ab Rama ki pehchaan ka nishaan banne wali thi.

🌺 Jungle ka saundarya — ek chalti hui painting

Raaste me:

Ped phoolon ke bhaar se jhuk gaye the

Nadiyan shaanti se samundar ki taraf beh rahi thi

Ghatiyan aur pahaadiyon me gehre ched, chasmey aur anokhe paudhe

Neel-jal ke jhilmil sarovar

Unme khilte kamal

Hans, bagle, jal-kukkut aur baaki pankhi madhur swar bhar rahe the

Hiran bina kisi dar ke doobte-soobte ghaas kha rahe the.

Mada-rasa me matwaale, bade-bade haathi
pahaadon par sir takraate hue chal rahe the—
poore deodar van ko hila dene wale.

Vanar-dal un sabhi drishyon ko dekh kar hairan tha. """

        create_image_text_layout("attached_assets/chapter4/4.13.jpg", text1, layout="side", image_position="left")

        text2 = """
🌳 Rama ka prashna — “Yeh kaise anokhe ped hain?”

Kuch hi door chal kar Rama ne ek ajeeb sa jhund dekha.

Unhone Sugriva se pucha:

“Sugriva, yeh ped badalon jaise kyun lag rahe hain?
Unpar dhuaan kyun chadha hua hai?
Unka rang itna ajeeb hara aur sunehra kyun lag raha hai?”

Sugriva ne dheere se kaha:

🕉️ “Rama… yeh Saptajanon ka Ashram hai.”

Sugriva ne chal-te chal-te us paavan jagah ka rahasya sunaaya:

“Yeh woh ashram hai jaha 7 mahan rishi — Saptajana — rehte the.
Ve 700 saal tak tapasya karte rahe.
Saath din paani me kandhe tak doobe rehte…
Aur sirf hawaa ko bhojan banate.”

Rama aur Lakshmana chok gaye.

Sugriva bolte gaye:

“Inki tapasya itni bhayankar thi ki ve shareer samet swarg gaye.”

“Unki shakti se yeh ashram devtaon aur asuron tak ke liye apraveshya ban gaya.”

“Pakshi, jangli jaanwar — koi iske andar nahi jaata.”

“Jo bhool se jaaye… wapas nahi aata.”

Kabhi-kabhi andar se:

veena jaise sangeet

swargiya geet

ek uncha dhuaan

aur divya sugandh nikalti

Sugriva ne zor se bola:

“Rama, Lakshmana — haath jod kar pranaam karo.
In Rishiyon ka samman karne wale ko kabhi kasht nahi hota.”

🙏 Rama–Lakshmana ka pranam aur pavitra sankalp

Rama aur Lakshmana ne dono haathon se pranaam kiya.
Ek shanti ki lehar un par chhaa gayi.

Phir teeno — Rama, Lakshmana, Sugriva —
aur pura vanar sena
aage badh gayi.

🏰 Kishkindha saamne thi — aur Bali ka ant bhi

Ashram piche reh gaya.
Ab saamne khadi thi Bali ki rajdhani — Kishkindha.

Rama ne apna dhanush kas liya.
Lakshmana ne teer nikaale.
Sugriva ki saanse tez ho gayi.

Vanar sena garaj uthi.

Yahi jagah thi jahan Bali ka ant likha jaana tha. """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.14
    with st.expander("Chapter 4.14 – Sugriva challenges Bali again"):
        text1 = """
Kishkindha ke paas pahunchte hi
Rama, Lakshmana, Sugriva aur sab vanar
ghane pedon ke peeche chup gaye.

Hawa me tanav tha.
Jungle khamosh tha.
Bas Sugriva ki saanse tez ho rahi thi—
gusse, apmaan aur badle ke saath.

🦁 Sugriva ki dahad — jo aasman ko cheer gayi

Rama ke taraf dekhkar Sugriva bol utha:

“Yeh hai Kishkindha!
Yeh Bali ka rajya, sunehre deewaron se ghira hua.
Aaj… aaj tu apne vaada poora karega, Rama!”

Yeh keh kar Sugriva ne
apna seena phulaaya
aur ek bhayankar garaj maari.

Uski dahad:

badalon se bharpur tufaan jaisi

ek sher ki chaal jaisi

suraj ke udte hue prakaash jaisi

Pura aakash usi se goonj utha. """

        create_image_text_layout("attached_assets/chapter4/4.14.jpg", text1, layout="side", image_position="left")

        text2 = """ 
🎯 Rama ka vachan — “Aaj Bali marega”

Rama ne shant swar me kaha:

“Sugriva, tumhare gale me jo Gajapushpi ki mala hai,
us se main tumhe pehchan loonga.
Aaj tumhara dushman, jo bhai hone ke kaabil nahi,
zaroor gir jayega.”

Phir Rama ne gambihta se add kiya:

“Maine tumhare saamne 7 Sala vriksh ek teer se cheer diye.”

“Bali ka pata bhi nahi chalega jab mera baan usse chhoo lega.”

“Main apna vachan kabhi nahi todta— na sukh me, na kasht me.”

“Toh Sugriva, garaj…
vo garaj jo Bali ko nikaal laayega.”

Sugriva ki aankhen chamak uthi.
Rama ka vachan— kisi bhi jeev ke liye
amogh astra ki tarah hota hai.

🌪️ Sugriva ki pratidhwani— jisme dard, gussa aur badla tha

Sugriva ne phir ek bhoom-phaad garaj maari—
itni tez, itni bhayankar,
ki:

gaayen dara kar bhaag gayi

hiran teer ki tarah jungle ki taraf udd gaye

pankhiyon ka santulan bigad gaya, vo zameen par gir pade

hawa tak hil gayi

Yeh dahad sirf awaz nahi thi…
yeh saalon ke dard ki cheekh thi,
apmaan ka badla tha,
apne chheen liye parivaar ki pukaar thi.

Aur sabse zyada—
yeh Rama ko di gayi apni aakhri aas thi.

Sugriva— Surya ka putra—
ek baar phir is tarah garja
jaise doobte hue samundar me se
dhoop phatkar bahar aa rahi ho.

Bali ne is dahad ko suna.
Aur yeh dahad…
uske ant ki shuruaat thi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.15
    with st.expander("Chapter 4.15 – Tara gives advice to Bali"):
        text1 = """ 
Bali apne raj mahal ke andar,
apni ranion se ghira baitha tha—
shaant, sukh me, jeet ke guman me…

Tabhi—
Sugriva ki dahad ne
poori Kishkindha hila di.

Ek dahad…
jisme saal-on ka dard, beizzati aur badla tha.

Jis pal Bali ne woh garaj suni,
uski aankhen laal ho gayi,
tan gusse se kaap utha,
aur jo pehle sone jaisa chamak raha tha,
vah sooraj grahan jaise dhundhla pad gaya.

Usne zameen par pair patka jaise dharti ko tod dalega.

👑 Tara — jiski sune to raaj bache, par Bali ne na suna

Bali gusse me aage badhne hi wala tha
ki Tara ne use baahon me rok liya.

Uski awaaz me pyar tha, par dar bhi.
Uski aankhon me vishwas tha, par shanka bhi.

Tara boli—
“Mere Veer, yeh gussa mat karo.
Yeh aaj tumhe behakar le jayega.”

Phir bohot shaant, bohot dheere,
par bilkul saaf shabdon me kaha:"""

        create_image_text_layout("attached_assets/chapter4/4.15.jpg", text1, layout="side", image_position="left")

        text2 = """
🔱 “Sugriva ka dusra aahvaan… kuch to gadbad hai.”

Tara ne kaha:

“Pehli baar Sugriva aaya tha—
usse tune hara kar bhaga diya.
Aaj woh phir garaj raha hai,
khuli chunauti de raha hai…
aur bina kisi wajah ke koi aise lautkar nahi aata.

Isme koi raaz hai.”

Phir Tara ne apna andesha bataya:

“Sugriva akela nahi aaya.
Uske peeche koi shaktishaali aashray hai.”

“Woh kisi ki shakti par bharosa karke hi
fir yeh dahad laa sakta hai.”

“Main ispar Bharosa karti hoon…
ki yeh kisi mahaveer ka saath lekar aaya hai.”

Aur phir Tara ne sach bata diya—
wo sach jise Bali sun hi nahi raha tha.

🌘 Rama ka ullekh — jo Bali ke vinaash ka sanket bana

Tara aage boli:

“Suna hai Sugriva ne dosti ki hai do rajkumar se—
Ayodhya ke putron se—
Rama aur Lakshmana se.

Woh Rama…
jiska naam hi dand hai, shastra hai, dharma hai.
Jisne asuron ko jala diya,
jo pralay agni jaisa hai.

Uska saath Sugriva ko mila hai.
Woh van me reheta hai,
par uske teer me pura brahmand base hain.”

Tara ne Bali ki aankhon me aankhen daal kar kaha:

“Rama se dushmani mat lo.
Yeh tumhare hit me nahi.
Aaj shanti hi jeet hai.”

❤️ Tara ka antim vinamra prarthna

Gadgad swar me Tara boli:

“Bali…
Sugriva tumhara bhai hai.
Use gale laga lo.
Dushmani chhod do.
Rama se bhi dosti kar lo.
Yehi tumhara surakshit raasta hai.

Agar tum mujhse prem karte ho…
to meri baat mano.”

Tara ke shabdon me patni ka pyar tha,
samajhdaar rani ki drishti thi,
aur ek tapasvini ka satya bhi.

⚔️ Par Bali… apni kismat ki taraf chal pada

Usne ek shabd bhi na maana.
Uski aankhon me sirf gussa tha,
uske kaano me sirf Sugriva ki dahad.

Aur Bali apne antim yudh ki taraf badh gaya—
jahaan uska saamna Rama se hone wala tha.
Jahaan se wapas lautna…
kisi bhi roop me sambhav nahi tha. """
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

