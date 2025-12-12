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
        text1 = """ 
Tara — jiska chehra chand ki tarah shant aur ujla tha —
Bali ko rokte hue boli.
Par Bali ne unki baat ko tarah-tarah ki taanon se taal diya:

⭐ Bali ka Aham

“Sugriva ne mujhe lalkara hai,”
Bali garajte hue bola,
“Main kaise chup reh jaun, Tara?
Veer log be-izzati bardasht nahi karte.
Maut manzoor hai, par apmaan nahi!”

Phir usne Tara ko dilasa diya:

“Raghava (Rama) dharm ko jaante hain,
woh kabhi galat kaam nahi karenge.
Tum wapas jao, mere liye chinta mat karo.”

Bali ne kasam kha kar kaha:

“Main Sugriva ka ghamand tod dunga, par uski jaan nahi loonga.
Bas uski had hoti hui himmat ko dikhana hai.
Tum yahin se laut jao.”"""

        create_image_text_layout("attached_assets/chapter4/4.16.jpg", text1, layout="side", image_position="left")

        text2 = """ 
        ⭐ Tara ka Vishad

Tara ne Bali ko gale lagaya.
Uski aankhon me aansu bhar aaye…
Usne parikrama ki,
mangal-mantra bole,
aur dukh se bhaari dil lekar mahal ke andar laut gayi.

Bali sheher se bahar nikla —
gusse se phat padta hua,
jaise koi vish–bhara naag!

⭐ Do Bhai Jakdte Hue

Kuch hi door, Bali ne Sugriva ko dekh liya —
sona-sa chamakta hua,
kavach pehne,
purane dard aur naye sahas se bhara.

Dono bhai ek dusre ki taraf badhe —
muthiyan kas-ke, aankhen laal,
aur zameen unke kadmon se hilti hui.

Bali garja:

“Is ek muthi se tumhari jaan nikal dunga!”

Sugriva bhi pichhe na hata:

“Meri muthi tumhara mastak tod degi!”

Aur fir…
woh dono pahadon ki tarah takra gaye.
Khoon dharaon ki tarah behne laga,
jaise kisi pahaad se laal jharne phoot pade ho.

⭐ Jung ki Chingariyan

Sugriva ne ek bada sa Sala vriksh ukhaad liya,
aur Bali par patthar jaisa bharaunda gira diya!
Bali dagmagaya —
jaise bojh se dubti hui koi naav.

Do bade devtaon jaise veer yodhaon ki tarah
yeh dono jangal ko kaampte hue lad rahe the.

Par Bali ka bal adhik tha…
Aur Sugriva dheere-dheere kamzor padne laga.
Usne aankhon se Rama ko sanket diya:

“Ab waqt aa gaya hai.”

⭐ Rama ka Faisla

Rama door khade sab dekh rahe the—
Sugriva ka dard,
Bali ka ghamand,
aur dharma ki rekha jo tut‐si rahi thi.

Jab Sugriva ke pair dagmagane lage,
Rama ne apna dhanush uthaya.
Ek teer – zeher bhari sarp ki tarah
unke haath me chamak utha.

Dhanush ki taar ka “TWANG!”
aakash me bijli jaisa gajaa.
Panchi ud gaye…
jangal ke janwar bhag gaye…

Aur phir—

🌩️ “THUNDER!”

Teer aasmaan cheerta hua gaya,
aur Bali ke seene me seedha ghus gaya.

Bali jhatke se peeche gira —
jaise poornima ki raat
Indra ka jhanda toot kar dharti par aa gira ho.

Khoon uske seene se nadiyon ki tarah behne laga.
Uski saanson me ruddh-si ghutan aa gayi…
aur veer Bali
zameen par nirjeev pad gaya.

⭐ Bali ka Patan

Rama ka teer
samay ke chakra jaise tha—
na roka ja sakne wala,
na modha ja sakne wala.

Bali dharti par girte hi
ghargharaane laga,
fir chup ho gaya…

Ek yug ka ant ho chuka tha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.17
    with st.expander("Chapter 4.17 – Bali questions and blames Rama"):
        text1 = """ 
Rama ka teer seene ko cheerta hua gaya,
aur Bali — woh maha–veerta, woh janglon ka raja —
lakdi se kaate hue vriksh ki tarah dharti par gir pada.

Uska sona jaisa ang, Indra ka diya hua haar,
aur uska gira hua deh
mil kar aise chamak rahe the
jaise shaam ke aasman me laalima faili ho.

Par aashcharya ye tha—
Bali mara nahi tha.
Indra ka diya hua divya haar
ab bhi use jeevan de raha tha,
use tej aur shakti se bhar raha tha,
chahe wo zameen par hi kyon na pada ho.

Dharti andhera ho gayi—
jaise chaand bina raat ho gayi ho.

Rama aur Lakshman dheere-dheere,
shraddha se,
usse dekhte hue paas aaye.

Bali ki aankhon me aag thi—
dard bhi, rosh bhi, satya bhi.
Usne zameen par padhe–padhe hi
kadvi par sachchi baatein kahi."""

        create_image_text_layout("attached_assets/chapter4/4.17.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Bali ka Prashna – “Rama, yeh kaisa dharm?”

Bali karwahat bhari awaaz me bola:

“Rama… mujhe pichhe se maar kar
tumne kaunsa punya kamaya?
Tum to veer ho, maryada ke rakhwale.
Pehle mujhe ye lagta tha.”

Usne Rama ke gun ginaaye:

shant,

dayalu,

dharm par chalne wale,

sabka kalyaan karne wale.

Phir bola:

“Par aaj main dekh raha hoon—
tum kuch aur ho.
Bahar se dharm ka chola pehne hue ho,
andar se kisi chhupi hui kuen ki tarah—
dhokebaaz.”

Bali ki saansein bhaari thi,
par shabd bijli ki tarah gir rahe the.

⭐ “Maine tumhara kya bigaada tha?”

Bali bohot dard se par kathor sach me bola:

“Na maine tumhari zameen chhui,
na tumhari nagri ko haani pahunchayi,
na tum par haath uthaya.
Phir kyon?
Kyon mujhe maara
jab main kisi aur se lad raha tha?”

Phir usne dharm ki baat ki:

“Raja ka kaam hota hai nyay.
Tumhara dhanush tumhari awaz ban gaya hai,
aur tumhara gussa tumhari akal ko kha gaya hai.”

Bali ke shabd chubhte the:

“Hum vanvasi hai, phal-mool khane wale.
Humein kya mila hoga jo tumne humse cheen liya?
Tum to manav ho, dharm ke rakhwale!”

⭐ “Mera dosh kya tha?”

Bali ne Rama ko seedhe dekhkar kaha:

“Tum Raghu vansh me janme ho?
Mujhe to vishwas nahi hota.
Ye kaisi maryada?
Kahan gaya tumhara dharm?
Aisa kaarya to
koi chhal karne wala hi karta hai.”

Aur phir—
Bali ne wo baat kahi jo uske dil ka dard thi:

“Agar tum samne aate,
mujhe dhokha na dete,
to Rama… aaj tum yahan khade na hote.
Main hota, tumhe dhool chata kar.”

⭐ “Main tumhare liye Sita ko ek din me laa deta!”

Bali ne karuna aur gham se kaha:

“Agar tum mujhe apna dukh batate,
ek din… sirf ek din me
main Sita ko tumhare paas le aata.
Ravana ko gale me baandh kar laata,
chahe woh samundar ke tal me
ya narak me kyon na chhupa hota!”

Usne fir kaha:

“Sugriva ko gaddi main khushi se de deta.
Par tumne uske liye mujhe chhal se maara.”

Bali ki awaaz dheemi padne lagi…

“Maut to sabko aani hai, Rama.
Par tum apne aap ko kaise samjhaoge?”

Aur itna keh kar
woh maha–vanar
chup ho gaya.
Uska rosh hawa me goonjta reh gaya…"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.18
    with st.expander("Chapter 4.18 – Rama explains his reasons to Bali"):
        text1 = """ 
Bali ka kathin, dard se bhara hua ilzaam Rama par gir chuka tha.
Wo dharti par pada hua tha — sooraj bina roshni,
badal bina barsaat,
aag bina lau jaisa.

Par uski awaaz me ab bhi veerta thi.

Rama aur Lakshman shant nigaahon se uske paas aaye.
Bali ke kathor shabd hawa me goonj rahe the…

⭐ Rama ka shant par teekha jawaab

Rama ne gehri, sthir awaaz me kaha—

“Bali, tum bachchon ki tarah kyun baat kar rahe ho?
Tum dharm, nyay aur maryada ki maryada ko jaante hi nahi.”

Rama ne use jataaya:

“Yeh dharti Ikshvaku vansh ki hai.”

“Bharata is prithvi ke rakshak raja hain.”

“Hum unke pratinidhi hain — hum dharm ko sthapit karte hain.”

Rama ke shabd shaant the, par bijli jaisi satya se bhare.

“Tumne dharm ka ullanghan kiya hai, Bali.”"""

        create_image_text_layout("attached_assets/chapter4/4.18.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Rama ka mukhya aarop – “Tumne Ruma ka apmaan kiya”

Rama ki awaaz kathin ho gayi:

“Sugriva zinda hote hue tumne Ruma ko,
apne chhote bhai ki patni ko,
apni iccha ka vishay bana liya…
Ye dharm ka atyant bhayanak paap hai.”

Rama ne dharm-shastra ka vidhan bataya:

“Jo vyakti apni behen, beti,
ya bhabhi ko ichcha ka vishay banata hai —
uska dand mrityu hai. Yeh raj-dharma hai.”

Bali chup ho gaya…

⭐ “Humne tumhare saath dvesh se nahi, dharm se vyavahar kiya”

Rama ne kaha:

“Yeh dand mera nahi — dharm ka hai.”

Phir kaha:

“Shikar me shikari kab puchhta hai
pashu samne hai ya pichhe?
Vah apna kartavya karta hai.”

“Tum to ek vanar the, ek praja —
aur main raj-dharm ka palankarta.”

Rama ka swaabhavik gyaan Bali ko bechain kar raha tha.

⭐ “Tumne mujhse jo kaha, wo tumhari agyaan se tha”

Rama ne narmi se par gambhir roop me kaha:

“Tumne mujhe alpasamajh se dhoosa.
Par tum kanoon nahi jaante.
Tumhare aas-paas ke mantri bhi andhe the,
aur tum unke peeche chal rahe the.”

“Tumhara dand sahi tha,
sahi samay par, sahi karan se.”

⭐ Bali ka parivartan – satya ka prakaash

Rama ki baatein sunkar,
Bali ka ghamand pighal gaya.
Wo aansuon bhari awaaz me bola:

“Rama… tum sach ke pratirup ho.
Main agyaan me tha.
Jo kuch maine kaha, dukh aur bhranti me kaha.”

Usne haath jod diye:

“Mujhe kshama karo.
Tumhara nyay sahi hai.”

Phir Bali ka dil apne bete ki yaad me dagmagaya.

⭐ “Rama… Angada ka dhyaan rakhna”

Bali ne kampte huye swar me kaha:

“Main apne liye nahi ro raha…
par Angada… mera baccha…
wo toot jaayega.”

Uski awaaz ruk gayi.
Phir bola:

“Sugriva ko sahi raasta dikhana.
Angada ko apne putra jaise sambhalna.”

“Jaisa Bharata aur Lakshmana tumhari raksha karte hain,
waisa hi Sugriva aur Angada ki raksha tum karna.”

Bali ab bilkul narm ho chuka tha.

⭐ Rama ka dukh ko mitaane wala vachan

Rama ne uske maathay par haath rakhkar kaha:

“Bali, chinta mat karo.
Angada mera putra samana rahega.
Sugriva ko main sambhalunga.
Tara ko samman milega.”

Rama ne usse dharm ka antimsatya samjhaya:

“Jo apraadh karta hai aur jo dand deta hai—
dono hi is sansaar ke karan–kaarya chakra ko poora karte hain.”

“Tumhara paap tumhare dand se dhul chuka hai.
Ab tum pavitra ho.”

⭐ Bali ka antimsparsha

Bali, jiski saansein toot rahi thi,
aakhri baar Rama ko dekh kar bola:

“Prabhu, maine tumhe anjaane me dukh pahunchaya.
Ab mujhe kshama karo….”

Uski awaaz dheemi pad gayi…
aur vanar–raj Bali
Rama ki charanon me apni aakhri saans leta gaya."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.19
    with st.expander("Chapter 4.19 – Tara cries in sorrow"):
        text1 = """ 
Bali, vanaron ka mahaan raja, Rama ke teer se ghaayal hokar
dharti par be-hosh pada tha.
Uske shareer par paththaron ke nishaan,
darakhthon ke ghaav,
aur Rama ka teer uske seene me gahra dhansa hua tha.

Wo ab antim saansen le raha tha.

🌕 Tara ko pata chalta hai

Jab Tara ko yeh khabar mili ki Bali ko Rama ka teer lag gaya,
aur ab wo mrityu ke kareeb hai,
toh uska dil toot gaya.

Wo Angada ka haath pakad kar
tez kadam se gufa se bahar nikli.

Par jaise hi wo bahar aayi,
usne dekha — monkeys bhaag rahe the.
Bilkul waise hi jaise hiran apne neta ko marha hua dekh kar bikhar jate hain."""

        create_image_text_layout("attached_assets/chapter4/4.19.jpg", text1, layout="side", image_position="left")

        text2 = """ 
🐒 Monkeys ka dar

Monkeys ne Rama ko dhanush ke saath khada dekha,
toh dar se bhaag utte—

Tara ne pukara:

“O Vanaro! Tum Bali ke sevak ho!
Bhaag kyon rahe ho?
Kya tum sochte ho Sugriva ne usse mara?”

Monkey sainik bole:

“O Devi, hum Rama ke dar se bhaag rahe hain!
Rama ka teer Bali ko gira chuka hai.
Hum kya kar sakte hain?”

Unhone aage kaha:

“Angada ko raja banao!”

“Tum Angada ko bachao!”

“Agar tum nahi manogi, hum dusre jungle chale jayenge.”

Phir unhone ek kathin baat kahi:

“Jungle me kuch vanar bina patni ke rehte hain,
kuch ek patni ko sabke saath baant-te hain…
par sab, patni kho chuke vanaron se darte hain.”
(uncommon: darne ka karan – jealousy/territorial fear)

Tara ne sab sun liya.

🌙 Tara ka tootna

Tara ne unki baatein suni
aur aansu bhar aayi.

Usne kaha:

“Agar Bali hi mar raha hai,
toh na Angada kaam ka hai,
na rajya ka.
Main apne pati ke paas jaungi.”

Apne seene par dono haath maar kar,
roti hui, daudti hui
wo kshetra ki taraf gayi
jahan Bali gira pada tha.

🦁 Bali ka antim drishya

Tara ne dekha:

Bali — veerta ka devta,
jo kabhi piche nahi hataa,
jo pahaad utha leta tha,
jo Indra jaisa shaktishaali tha —
ab ek hi teer se gira hua pada tha.

Bilkul waise jaise:

shikaar hua hiran, sher ke panjon me

ya mandir ka jhanda, tijori, sab kuch tod diya gaya ho

Uska body ab bhi shaurya se chamak raha tha,
par wo bejaan lag raha tha.

🌧️ Tara ki cheekh

Tara ne Rama ko dekha —
woh dhanush par jhuke khade the,
Lakshmana unke saath,
aur Sugriva kuch hi door.

Tara apni saari shakti kho baihti.

Wo dharti par gir padi.
Phir dheere se uth kar
Bali ke pass gayi…

“O Raja…”
usne dard bhari cheekh nikali.

Uski awaaz
bilkul osprey (water-hawk) (a bird with sharp cry) ki cheekh jaisi thi —
tez, tootati hui, dil cheer deti hui.

Sugriva ka dil bhi us dard se hil gaya.
Angada ka chhota sa mann bhi kaap utha.

⚡ Chapter 19 samapt

Yeh tha Tara ka dard…
pati ka virah, bete ka bhavishya,
aur ek nari ka tutta hua sansaar."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.20
    with st.expander("Chapter 4.20 – Tara continues to mourn for Bali"):
        text1 = """ 
Tara ne apne pati Bali ko zameen par pada dekha.
Uske seene me Rama ka mrityu-deta teer tha.
Bali ek bade ghaayal haathi jaisa lag raha tha—
gir gaya, bejaan, par ab bhi shaurya se chamak raha.

Tara daud kar uske paas aayi,
aur use gale laga liya.

Phir Tara ka dil toot gaya.
Aansu ruk hi nahi rahe the.
Usne ro kar kaha:

🌙 Tara ka pehla vilap

**“O Veer Bali!
O mere raja!
O vanaron ke sher!
Tum mujhse baat kyon nahi kar rahe ho?
Utho!
Aise zameen par kyon so gaye?

Kya tumhe dharti mujhse zyada pyari lagti hai?
Marte waqt bhi tum dharti ko gale laga kar lete ho?

Tum jaise bade raja kabhi zameen par nahi sote.
Kya tumne swarg me nayi Kishkindha bana li hai?”**"""

        create_image_text_layout("attached_assets/chapter4/4.20.jpg", text1, layout="side", image_position="left")

        text2 = """ 
🌧 Dard aur yaad

Tara ne aansuon ke saath kaha:

**“Hamare saath-bitaye din…
jungle ki khushboo, hamari baatein…
sab khatam ho gaye.
Aaj main akeli ho gayi.

Tum paanch tattvon me laut rahe ho.
Mera dil paththar ka hona chahiye jo itna dard seh kar bhi toot nahi raha!”**

Phir usne apne hi pati par sach bol diya:

“Tumne Sugriva ki patni chura li.
Tumne usse vanvaas diya.
Aaj tum usi paap ka phal bhugat rahe ho.”

🌪 Tara ke sachche shabd

Tara ne ro kar bola:

**“Main ne hamesha tumhe sahi salah di.
Par tumne meri ek na suni.
Aaj tum Apsaraon ko dikhnay ja rahe ho…
aur main yahan toot rahi hoon.

Tumhe koi hara nahi sakta tha,
par kismat ne tumhe hara diya.”**

⚔️ Rama aur Sugriva ke liye teekhi baat

Tara boli:

**“Rama ne tumhe bina wajah gira diya.
Par wo paap nahi karega,
kyonki usne sirf Sugriva ki baat maani hai.

Sugriva, khush ho jao!
Ruma tumhe wapas mil jayegi.
Rajya tumhara ho gaya.
Tumhara bada bhai yahan mar raha hai.”**

🦁 Tara ka Bali ko antim sandesh

Tara ne Bali ka haath pakad kar kaha:

“Tum mere dard ka jawab kyon nahi dete?
Tumhare itne saari sundar ranian tumhare paas khadi hain.
Ye sab tumhari ek jhalak ka intezar kar rahi hain.”

Uski cheekh dekh kar
saari vanar-ranian rone lagi.
Unhone Angada ko beech me le liya
aur har taraf dard ki aawazein gunjne lagin.

🌑 Angada ka bhavishya

Phir Tara ne fir ro kar kaha:

**“Angada ko kyon chhod ja rahe ho?
Wo tumhari shakal, tumhari veerta,
sab kuch lekar paida hua hai.

Agar maine kabhi galti ki ho,
toh mujhe maaf kar do.
Main tumhare charanon me sar rakhti hoon.”**

🌒 Tara ka nirnay

Tara aur dusri ranian
Bali ke paas hi baithi rahi.

Tara ne faisla kar liya:

“Main yahi rahungi.
Na khaungi, na piyungi.
Main bhi Bali ke saath hi marungi.”

Aur wo Bali ke paas dharti par
be-hosh si gir gayi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.21
    with st.expander("Chapter 4.21 – Hanuman speaks to comfort and guide everyone"):
        text1 = """ 
Tara ke shok ko shaant karne ki ek gambhir, komal, aur dharm-gyan se bhari gatha.

Bali giri pada tha… van ka maha-simha ab nishchal. Tara dharti par bikhri hui thi—jaise aasman se koi taara toot kar zameen par aa gira ho. Uske aanchal me dard hi dard tha.

Tab Hanuman, Vanaron ka mahan neta, bade komal swar me Tara ke paas aata hai. Uska hriday daya se pighal raha tha. Dheere se woh Tara ko sambhalte hue bolta hai—

🕊️ Hanuman ka Dharm-yukt Santvan Vachan

“O Devi,” Hanuman ke swar me karuna thi,
“Yeh shareer ka janm–mrityu ka chakra,
punya–paap ka phal…
sab kuchh iss prani-jagat ka niyam hai.

Jo karte hain, uska fal avashya paate hain—
chahe veer ho ya mrit,
rajya ho ya van.

Tum kisliye shok kar rahi ho?
Kiske liye ro rahi ho?
Jeevan swayam ek bulbule ki tarah hai—
kshan bhangur, asthir, nasht hone ko sada taiyaar."""

        create_image_text_layout("attached_assets/chapter4/4.21.jpg", text1, layout="side", image_position="left")

        text2 = """ 
Par Angada—
woh abhi jeevit hai.
Yuvraj, tumhara putra.
Ab tumhara kartavya uske prati hai.”

Hanuman ne Tara ki aankhon me gehra shok dekha aur dheere se samjhaya—

“Samay ka niyam anivarya hai.
Bali ne dharm-nishta se raj kiya,
daanon me mahaan tha,
samdrishti, kripa aur tyaag se bhara hua.

Aise punyatma veer ab devon ke loka me virajmaan honge.
Unke liye kyun shok?

Devi, ab tum vansh ki rakshika ho.
Angada ka sahara tum ho.
Aur Sugriva, tumhare pati ka bhai—
rajya usi ka adhikaarik haq hai.

Tum shant ho jao.
Angada ko sambhalo.
Usse dhairya do.
Uske bhavishya ki raksha karo.
Rajya ka bhavishya tumhare haath me hai.”

Hanuman ki nishtha aur maryada bhare vachan
swayam van ko bhi shant kar dene saksham the.

🌑 Tara ka Shokbharit Uttaar

Par Tara ke hriday me ek hi baat dhadak rahi thi: Bali.
Uska praan, uska sukh, uska sehara.

Aansuon me bheegi hui,
Hanuman ko uttar deti hai—

“Hanuman…
Mere liye Angada jaisa sau putra bhi ho,
to bhi main un sabse pehle
iss veer ke sharir se lipat kar jeena–marna chahungi.

Mujhme rajya chalane ki shakti nahi.
Angada bhi abhi kishor hai—
rajya sambhalne yogya nahi.

Rajya ka adhikaar
putra ke pita ke bhai, yane Sugriva ko milta hai.
Waris ka sachcha sanrakshak maata nahi— chacha hota hai.
Ye vansh-ka-dharma hai, raja-dharma hai.

Mere liye iss sansaar me,
ya parlok me,
koi shrey ya sukh nahi—
bas apne pati ke paas rehna hi meri gati hai.

Main to usi shayya par marna chahti hoon
jahan mera swami,
yudh me shatru se mukh morh kar
veer-gati paaya hai.”

Tara apne shok ki seema par khadi thi—
uska praan Bali ke tatpraya me hi basa hua tha.

Hanuman chup ho jaata hai—
kshatriya-dharma aur pativrat-dharma ka
ye karuna-mishrit sangam
uske hriday ko bhi chhed deta hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.22
    with st.expander("Chapter 4.22 – Bali says his final words"):
        text1 = """ 
Bali—mahaveer, vanar-raj, Sugriva ka jyeshth bhai—
ab antim saans le raha tha.
Uski saans halki thi, uska ur gahari peeda se uth-baith raha tha,
par uski drishti—ab bhi teekhi, saaf, aur prem se bhari hui.

Usne dheere se aankhein ghumayi
aur apne saamne Sugriva ko khada dekha.

Antim shakti jodkar, Bali ne
apne chhote bhai ko sneh aur karuna se bhare shabdon me sambodhit kiya—

🕊️ Bali ka Sugriva se Antim Sambodhan

“Sugriva…
Mere kareeb aa,
par dvesh lekar nahi.

Main bhrant ho gaya tha…
moha ne, krodh ne, ahankaar ne
mujhe andha kar diya.
Ham dono bhai the—
par humare bhagya ne hume kabhi ek hone nahi diya.

Aaj tum vanar-rajya ka adhikaar
phir se praapt karoge.
Aur main…
iss mrityu-lok ko chhod kar jaa raha hoon.

Main jeevan, rajya, yash, sab ek pal me
tyaag raha hoon.
Par ek cheez hai jo
mai tumhare bina nahi chhod sakta…”

Bali ki aankhen Angada par ja tikti hain—
jo zameen par baitha, aansuon se bheega hua,
pita ko tak raha tha."""

        create_image_text_layout("attached_assets/chapter4/4.22.jpg", text1, layout="side", image_position="left")

        text2 = """ 
“Angada…
Mera putra.
Meri aanch.
Meri dhadkan.

Sugriva—
uski raksha karna.
Uska pita, uska mitra, uska sharan ban jaana—
jaise main tha.
Woh abhi nirbal hai, jawaan hai,
par veerta uske lahu me hai.

Use kabhi akela mat chhodna.
Woh tumhara putra jaisa hi hai.”

Bali ruk kar phir dheere se bolta hai—

“Tara—Sushena ki putri—
samay ko pehchanti hai,
bhavishya ko jaanti hai.
Jab woh tumse kahe ‘Yeh karo, yeh uchit hai,’
to bina hichkichaye karo.
Uske drishti ka bhram kabhi nahi hota.

Aur ek baat…
Rama jo kahe, wahi karna.
Uska avagya tumhe dukh aur dand donon dega.”

Phir Bali apni suvarna-mala ko pakad kar Sugriva ki aur badhata hai—

“Yeh raj-rekha…
Shri ka aabha isme hai.
Mere mrityu ke baad yeh mujhe chhod degi—
isliye tum ise le lo, Sugriva.”

Sugriva,
jisne yuddh jeeta tha,
par mann se poora haar chuka tha—
royi hui aankhon se yeh suvarn-mala le leta hai.

Woh apne bhai ke charanon me gir padta hai.

🌿 Bali ka Angada se Antim Updesh

Ab Bali apne putra Angada ke paas bulata hai.
Uski awaaz halka sa kamp rahi thi—

“Putra…
Samay, sthiti, aur maryada ko pehchanna seekho.

Sukh-dukh ko samaan samajhkar jeena.
Sugriva ko apna swami,
apna raja,
apna pita mankar chalna.

Uske mitron se mitrata,
uske shatruon se doori—
yeh tumhari raksha karegi.

Adhik sneha bhi nahi,
adhik virakti bhi nahi—
dono adharm ke raaste hain.
Madhyam marg pakadna, Angada…”

Bali ki saans tej ho jaati hai.
Uski aankhen phail jaati hain.
Dant bhedte hain,
aur ek gambhir, dirgha peeda ke saath—

mahaveer Bali antar-dhan ho jaata hai.

🌑 Vanaron ka Vilap

Jaise hi Bali ne praan tyaage,
van ki praja par ek aandhi si chha gayi.

“Hamare raja chale gaye!”
“Hamari shaan, hamara sahara—sab chala gaya!”
“Hamara rakshak, hamara Indra-tulya simha—
kaise gir gaya?”

Unhone Bali ki paraakrama bhari yuddh katha yaad ki—
Golaba Gandharva ke saath solah saal tak yuddh;
jitne bhi rakshas, yatudhan, daitya aaye—
sab usne dhool chataayi.

Par aaj woh simha,
woh parvata-sam Bali,
ek teer me bhu-tal par so raha tha.

🌘 Tara ka Mahaa-Shok

Tara—
jo apne shok me samudra ho chuki thi—
apne pati ke nishpran deh ko dekhkar
phir se zameen par gir padti hai.

Jaise koi laata, jhada hua vriksha ho
aur us par latakti koi bali hui bel.

Uske karuna-bhare chil-laah
poore van ko kaamp dete hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.23
    with st.expander("Chapter 4.23 – Tara cries over Bali’s body"):
        text1 = """ 
Bali—vanaron ka raja, apar shakti ka dhani—
ab nishchala pada tha,
mrityu ke sukh-shaant sparsh me lepta hua.

Uska chehra—jo kabhi garv, tej aur veerta se chamakta tha—
ab shaant, sthir, aur gungunati mrityu-jyoti se bhara tha.

Tara,
jiski pratishtha teenon lokon me phaili thi,
jiski buddhimatta aur saundarya dono prasiddh the—
apne patidev ke mukh ko
komal haath se chhoote hue
rukhi saans ke saath boli:"""

        create_image_text_layout("attached_assets/chapter4/4.23.jpg", text1, layout="side", image_position="left")

        text2 = """ 
🌘 Tara ka Bali se Vilap

“He Veer!
Meri baat na maankar
dekho kis kathor, patharili zameen par aaj pade ho tum…

Kya tumne dharti ko apni priya chuni,
mujhse zyada?
Main yahi hoon—tumhare paas—
par tum ek shabd bhi nahi bolte…

Haay!
Vidhata ne Sugriva ka saath diya—
aaj woh veer kehlayega,
kathin yuddh ka vijeta ban kar.

Vanar aur Rishabha-neta
sab tumhari veerta ko yaad kar rahae hain…
Unki pukaar,
Angada ka dard,
aur mera shok—
kya yeh sab bhi tumhe jagaa nahi pa rahe?

O Maharathi,
jiske liye yuddh ek khel tha—
aaj mujhe be-sahara chhod kar
paanch tattvon me vilin ho gaye tum…

Kaun si patni sukh paati hai,
jab uska pati yuddh me gir jaaye?
Chahe putra ho, dhan ho—
widwa toh widwa hi kehlati hai,
yeh ved-vyawahaar ka vidhan hai.

Tumhara shareer,
jo kabhi rakta-rangi silk se saja rehta tha,
aaj tumhare apne lohu se lipta hua pada hai…

Tumhare shaurya ke dhwaj patak rahe hain—
par main tumhe gale tak nahi laga sakti,
kyunki Rama ka teer
ab bhi tumhare hriday me virajmaan hai…”

🩸 Teer ka Nikalna

Tab Nala, vanaron ka sena-nayak,
aage badha
aur Bali ke ango se
Rama ka teer nikaala—

Woh teer, jo pahad ki gufa se nikalti
krodhit sarp-jaisi jwala sa lag raha tha,
suryakirnon ki tarah chamak raha tha.

Jaise hi teer nikla,
Bali ke ghaavon se
nadi ki tarah laal dhaara behne lagi—
jaise kisi parvat se chhootkar
lal-chandan se rangin jal
niche aa raha ho.

💧 Tara apne Aansuon se Bali ko Dhoti Hai

Tara ne
yuddh ki mitti aur khoon
jo Bali ke shareer par laga tha—
apne aansuon se dhona shuru kiya.

Woh aansu—
jo prem, shok, samarpan aur pativrat dharm
ka sangam the—
Bali ke shareer par moti ki taal ki tarah girte ja rahe the.

Phir usne Angada se kaha:

💔 Tara ka Angada se Sambodhan

“Beta…
Dekho apne pita ka yeh kathin ant…

Yeh vahin bali ka phal hai
jo kapat se janma tha…
Tumhare pita ka deh,
jo kabhi udit surya ki tarah chamakta tha,
aaj mrityu-lok me lete hue
panch-bhuto me sama raha hai.

Jaao…
jaakar unhe gale lagao.”

🧒 Angada ka Vilap

Angada—jiski aankhen lal ho chuki thi
aur hriday toote hue shankh ki tarah dard se bhar gaya tha—
pita ke pairon se lipat kar rota hua bola:

“**Pitashri!
Main hoon, Angada!
Pehle jab main aapko gale lagata tha,
aap hamesha kehte the—
‘Jeete raho, mere beta…’

Aaj kyun nahi keh rahe?
Kyun nahi bol rahe…?”

🌙 Tara ka Antim Dukh

Tara,
apne shok se dubbti hui,
phir se Bali ke sharir par jhuk gayi—

“Main yahin hoon—
tumhari mrityu-deh ke paas—
bilkul us gaay ki tarah
jo apne saand ki mrityu par khadi roti hai…

Tumhari suvarna-mala—
jo Indra ne tumhe asur vijay ke baad di thi—
woh kahan gayi?

Par nahi—
rajya ke alankaar
mrityu ke baad bhi raja ka saath nahi chhodte.
Parvat ka raj-tattva
suryast ke baad bhi chamakta hai…

Tumne meri salah nahi maani—
aur main tumhe rok nahi pai…

Tumhari mrityu ne
mujhe bhi maar diya—
aur Angada ko bhi.

Lakshmi ne
aaj tumhe bhi chhod diya,
aur mujhe bhi…”

Iske baad
Tara ka shok poorn roop se phoot padta hai,
jaise ek nadi apne bandhan tod kar behne lage."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.24
    with st.expander("Chapter 4.24 – Sugriva feels guilty and sad"):
        text1 = """ 
Tara ko
shok ke gehre, behad, doobte hue sagar me vilin dekhkar,
Sugriva ka hriday phat gaya.

Apne hi bhai ke mrityu ka drishya—
aur us par Tara ka dard—
uske mann ko dagmagane laga.
Uska mukh aansuon se bhig gaya,
aur bhare saans ke saath
woh dheere-dheere Rama ke paas pahuncha,
jo apni sena aur parivaar se ghiray hue
ab bhi rajatva ke sabhi lakshan dharan kiye khade the—
dhanush haath me,
teer uske kandhe par sarpon ki jaise lakate hue."""

        create_image_text_layout("attached_assets/chapter4/4.24.jpg", text1, layout="side", image_position="left")

        text2 = """ 
🌘 Sugriva ka Rama se Vilap

“He Purushottam!
Aapne jo vachan diya tha—
aapne woh pura kiya…
Aur dekhiye—yeh uska phal hai…

Meri jeet ke beech mein,
Iss laashe ke saamne
mera hriday shant ho hi nahi pa raha.

Tara vilap kar rahi hai,
Angada ka jeevan toot gaya hai,
aur poori Kishkindha ro rahi hai.
Aise rajya ka kya sukh,
jiska mool hi khoon aur dard ban gaya ho?

Pehle—
krodh, rosh aur dvesh ne
mujhe hansne diya tha mere bhai ki mrityu par…

Par jaise hi Maine uska sharir dekha—
mere andar ka maanas ro pada.
Aaj samajh aata hai—
ki Rishyamuka par vanvaasi rehna hi behtar tha
bhai-hatya kar raj milne se…”

💔 Sugriva ka Apraadhi-hriday

“Woh bolta tha,
‘Main tumhe maarna nahi chahta, jao yahan se…’
Kitni udaar, kitni shresth vaani thi woh!

Aur main?
Maine kya kiya, Rama?
Maine uska khoon baha diya.

Yeh paap…
vishwa me kaun baant sakta hai?
Meri jaati ka rakshak main hi uska naash karne wala ban gaya!

Indra ne bhi jab Vishwarupa ko maara tha,
toh paap dharti, vrikshon, paani aur striyon me vibhakt ho gaya…
Par mera paap?
Kaun sa jeev mere saath is bojh ko baantega?

Main rajya ke layak nahi hoon,
na hi samman ka adhikari.
Aaj main paap se jal gaya hoon—
jaise sona aag me jhulas kar bas bhasm reh jaata hai.

Angada—
woh ek anmol ratan hai,
par beta toh har ghar me janma le sakta hai.
Par bhai?
Bali jaisa bhai
kis yug me, kis lok me mil sakta hai?

Uske bina main jee nahi sakta.
Main agni me pravesh kar
apne bhai ka prem dobara paaunga…”

🌑 Sugriva ki Antim Vinati

“Jab chaaho hum vanar sena ko Sita ki khoj me bhejenge…
par main—
jo apne vansh ka shatru ban gaya hoon—
main aapko pranaam kar ke
apne paap ka prayashchit karne jaa raha hoon, Rama…”

🌕 Rama ka Shok

Sugriva ke shabd—
dard se pade,
tukdo me toote—
sun kar Rama ke chakshu bhi aansuon se bhar gaye.

Raghuvansh ka woh shreshtha putra
ro pada,
kyunki uska hriday bhi
Tara ke shok aur Sugriva ke pashchattapa se bhaari ho gaya tha.

Jab usne idhar-udhar drishti ghumayi,
usne dekha—
Tara apne pyaare Bali ke sharir ko
bahon me bandh kar vilap kar rahi hai.

Mantriyon ne usse halka sa piche kiya,
aur woh, kaampti hui,
tevar me dukh ka sagar liye
Rama ke paas aa pahunchi.

🌙 Tara ka Rama se Antim Aagrah

“He Kakutstha…
Aap apar shaurya ke swami,
aprameya bal ke adhikari…
Aapne mere pati ko apne teer se chir diya—
toh ab yeh teer mujhe bhi de dijiye.

Woh akele swarg nahi jayega—
main bhi uske bina ek pal nahi jeeungi.

Agar aap sochte ho ki ‘stree-hatya paap hai’—
toh mujhe uska ardhang hi samajhiye.
Aap mere pati ko hi wapas unka ardhang de rahe honge.

Unke bina
main na iss lok me rah sakti hoon,
na uss lok me jahan apsarayein unhe gherengi—
woh wahan bhi mere bina sukhi nahi honge.”

🌄 Rama ka Adhyatmik Uttar

Rama,
dayaal aur vivek ka roop,
us dukhit rani se mradul swar me bole:

“Devi, shok mat karo…
Jo kuchh hota hai—
Narayan ki ichha se hota hai.
Karm, phal, janma aur mrityu—
sab ek anant niyam me bandhe hain.

Angada rajya ka yuvaraj banega.
Tumhara kalyan nishchit hai.
Aur veer ke sanginiyon ka dharm hai—
dharna, sahana, aur dheeraj.”

Rama ke vachan,
amrit ki boondon ki tarah
Tara ke dard se tapte hriday par tapak padey—
aur dheere-dheere
uska vilap shaant hone laga."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.25
    with st.expander("Chapter 4.25 – Bali’s funeral is performed"):
        text1 = """ 
Sugriva, Tara, aur Angada ke dukh ko dekhkar
Kakutstha—daya ka saagar,
Lakshmana ke saath
aage badhe
aur mṛidu madhur vaani me bole—

🌕 Rama ka Dharma-sankalp

“Viyog se kisi ka kalyān nahi hota, Sugriva!
Jo hona tha—ho chuka.
Ab tumhara kartavya tumhari aankhon ke saamne khada hai.

Rona, shok—yeh sab lokaachaar ka ek ang hai—
par adhik aakranth hokar
koi mrityu ko rok nahi sakta.

Samay—hi sab kuchch chalata hai—
samay hee janm deta hai,
samay hee sangharsh banata hai,
samay hee visraam karwata hai."""

        create_image_text_layout("attached_assets/chapter4/4.25.jpg", text1, layout="side", image_position="left")

        text2 = """ 
Na koi karta hai,
na koi karwata hai—
prakriti apne niyam se chalti hai.

Bali—apne punya se
apne uchch sthaan par pahunch chuka hai.
Usne raj dharm nibhaya,
daana, udarta, aur nyaya ka palan kiya—
isliye woh devalok ka adhikari hua.

Ab shok tyago.
Aur apne bhai ke antim sanskaar shuru karo.”

🌘 Lakshmana ka Aadesh

Rama ke shant hone par,
Sumitra-nandan Lakshmana,
veerta ka agni-shikha,
Sugriva se bole—

“Sugriva!
Antyeshti me vilamb uchit nahi.
Tara aur Angada ke saath
turant prarambh karo.

Vrikshon ka sukha lakda,
chandan ki lakdi,
ghrita, tel, sugandh,
aur shobha ke vastra—
sab ikattha karvao.

Tara!
jaldi se ek vaahan—palki—le aaon.
Jo log yatra-sewa me nipun aur balvan hain,
unhe taiyaar rakho.”

Lakshmana ke shabdon ka prabhav
taar ki tarah sidha Tara ke hriday me utar gaya.
Dhadakte mann se
woh tezi se andheri guhā me gayi—
aur kuchh hi kshanon me
majboot vanaron dwara uthayi ja rahi
shobha-yukt divya palki lekar laut aayi.

🌄 Divya Palki ka Darshan

Palki—
jaise kisi Siddha ka vimaan,
mrigasaar wood se nirmit,
kanthas, chitrankit stambhon,
moti ki malaon,
rajabhoomi ke pushpon aur gandhon se yukt.

Rama ne usse dekh kar Lakshmana se kaha—
“Bali ka sharir isme stith karo. Sanskaar prarambh ho.”

Sugriva, aansuon se bhara,
Angada ke saath milkar
Bali ka sharir utha kar
palki par rakhta hai.

Pushp, vastra, kaanchan alankar—
sab Bali ke sharir par sajaye gaye—
jaise veer ko divya yatra ke liye su-shobhita rakha jaye.

🌒 Vanara Sena ka Maharaja ko Antim Samman

Vanar-senapati
palki ke aage-aage
ratnon ki varsha karte chale.

Aaj—
Bali ne bhale hi sharir chhod diya,
par vanaron ne usse Rajyapurush ki
poori maryada di.

Stree-yon ke “He Veer! He Veer!”
vilap ki dhvani
ghane vanon ke vistar me
garaj kar gunj uthi.

🌘 Shok ki Ragini — Tara aur Angada

Nadi ke kinare—
jahan pahadon se girta jal
koomltā hua ek ret ka dweep banata hai—
wahan
ek vishal chita sajayi gayi.

Bali ka sharir jab us par rakha gaya,
Tara, uska mastak apni god me rakhkar
vilap karne lagi—

🌹 Tara ka Vilap

“He Prān-nāth!
Ab toh ek nazar bhi nahi karoge?
Hum sab ro rahe hain—
par tumhari simti hui muskaan,
mrityu me bhi suryoday si chamak rahi hai…

Rama ke ek teer ne
tumhe humse cheen liya—
hum sab ko vidhava bana diya.

Tumhare bina
yeh junglee raaste,
yeh parvat,
yeh rashtra—kis ka sahara lenge?

Tumhare mantri yahan hain,
Sugriva bhi yahan hai—
sab tumhari ek jhalak ko tars rahe hain.

Utho, he Pawan-putr ke saman balwaan!
Jaise pehle hum sabko van me le jaate the—
vaise hi ab hume
antim yatra me saath le chalo…”

Striyon ne usse pakda,
usse sambhala—
par Tara girti hi ja rahi thi.

🌑 Angada ka Agni-pradip

Angada—
hriday me peda ka pahad liye—
apne pita ke sharir ko
chaaron or parikrama karta hua
aag lagata hai.

Aankhon se aag jaisi lahu-jaisi dhara beh rahi thi—
par dharm ke anusaar
usne pita ko mukhagni di.

Chita ki tezi se bhasm hoti lauon ke beech
Bali—
veeron ka veer—
divya lok ki disha me chal diya.

🌄 Antim Sanskaar ki Poorti

Sugriva, Tara, aur Angada
snan karke
Rama ke paas aaye.

Raghunandan—
jinhe devon ne bhi maryada ka devata kaha—
Sugriva ke shok me saath khade rahe,
aur Bali ko antim dharm se sambodhit kiya."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.26
    with st.expander("Chapter 4.26 – Sugriva is crowned as king"):
        text1 = """ 
⭐ Sugriva Ka Rajyabhishek — Hinglish Kahani

Bali ki maut ke baad,
Sugriva bahut udaas tha.
Uske kapde bheege the,
aur dil dard se bhara hua tha.

Tab uske mantriyon ne use gher liya
aur sab milkar Rama ke paas le gaye.
Sugriva haath jodkar
Rama ke saamne khada ho gaya—
bilkul waise hi jaise Rishis Brahma ke saamne khade hote hain."""

        create_image_text_layout("attached_assets/chapter4/4.26.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Hanuman Ki Vinati

Hanuman, jiska chehra suraj ki tarah chamak raha tha,
bohot vinamr awaaz me bola:

“Prabhu, kripya karke Sugriva ko
uska rajn ki gaddi wapas de dijiye.
Woh apne logon ke saath milkar
apne rajya ko sambhal lega.

Aap iss pahaad ke andar bani
sundar cave me aaram se reh sakte hain,
aur monkeys ko bhi ek naya raja mil jayega.”

⭐ Rama Ka Shant Jawab

Rama pyaar se bole:

“Hanuman, main 14 saal tak
kisi shehar ya gaon me nahi ja sakta,
yeh mera pita ka vachan hai.

Isliye Sugriva hi Kishkindha jaaye
aur raja bane.

Aur yaad rakhna,
Angad ko rajya ka yuvaraj banana—
wo Bali ka beta hai,
bahadur aur imaandar bhi.”

Rama ne Sugriva se kaha:

“Ab barsaat ka mausam aa gaya hai,
yudh ka samay nahi hai.
Kartik ka mahina aate hi
hum Ravana ko maarne niklenge.

Tab tak tum raja ban kar
apne rajya ko sambhalo.”

⭐ Sugriva Ka Raj Tilak

Rama ki baat sunkar
Sugriva apni rajdhani Kishkindha laut gaya,
jahaan sab monkeys ne zameen ko chho kar
apne raja ka swagat kiya.

Phir Sugriva apne bhai Bali ke
androni mahal me gaya
aur wahan uska rajyabhishek hua.

Monkeys ne ek safed chhatra,
yak ke pankhe,
sunehri saaman,
phool,
chandan,
kapde,
sona,
madhu,
aur sugandhit jal laya.

Vidhiyon ke anusaar
Rishi, pandit aur veer monkeys
sona ke kalashon me shuddh jal bhar kar
Sugriva ke sir par chhidakte gaye.

Poora mahal
“Jai! Jai!” ki awaazon se goonj utha.

⭐ Angad Banaye Gaye Yuvaraj

Rajyabhishek ke turant baad
Sugriva ne Angad ko gale lagaya
aur use yuvaraj bana diya.

Monkeys khush ho kar bole:

“Bahut accha! Bahut accha!”

Poora Kishkindha jhandaon se bhar gaya—
har gali khushi se chamak rahi thi.

⭐ Sugriva Ka Naya Adhyay

Rama ko khabar bhejne ke baad
Sugriva apni patni Ruma se mila
aur dono ne apne rajya ko dobaara sambhala.

Sugriva ab asli arth me
Vaanaron ka Maharaja ban chuka tha—
bilkul waise hi jaise Indra devon ka raja hota hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.27
    with st.expander("Chapter 4.27 – Rama describes the Prasravana mountain"):
        text1 = """ 
⭐ Prasravana Par Rama Aur Lakshman — Hinglish Kahani

Sugriva ka rajyabhishek ho chuka tha,
aur woh Kishkindha laut gaya.
Rama aur Lakshman ek sundar pahaad, Prasravana, par rehne aa gaye.

Yeh pahaad sheron ki dahad,
hiran ki cheekh,
aur jangli awaazon se bharpura tha.
Har taraf bade-bade peedh, belen aur ghani jhadiaan thi.
Pahaad aisa lagta tha jaise badalon ka ek chamakta hua pahaad ho.

Choti par ek badi si gufa thi—
Rama aur Lakshman ne wahi apna ghar banaya."""

        create_image_text_layout("attached_assets/chapter4/4.27.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Rama Ka Prasravana Ka Sundar Varnan

Ek din Rama ne halka sa muskura kar
Lakshman se kaha:

“Saumitri, yeh jagah barsaat ke mausam me rehne ke liye perfect hai.
Dekho, yeh pahaad kitna sundar hai—
kale, safed aur bhure pathar,
nadiyon me uchhalte medhak,
aur har taraf rang-birangi belen aur phool.

Idhar ek pyara sa talaab bhi hai—
lotus se bharahua.
Aur gufa ke paas hawa bhi tez nahi chalti.
Yeh jagah humare liye bohot sukoon wali rahegi.”

Rama ne Lakshman ko nadi ka sundar nazara bhi dikhaya:

“Is nadi ka paani bilkul saaf hai,
aur iske kinare par
sandal, bakula, ketaki, ashoka aur kitne hi peedh hain.

Hans, bagule aur jal-chidiyaan
yahan masti kar rahi hain.
Kabhi neele kamal chamak rahe hain,
kabhi laal, kabhi safed.

Yeh sab dekhkar mann khush ho jata hai.”

Phir Rama muskura kar bole:

“Kishkindha bhi yahin paas me hai.
Aajkal Sugriva aur monkeys
nagare baja kar khushiya mana rahe honge.”

⭐ Par Rama Ka Dil Udaas

Par jitni sundar jagah thi,
Rama utne hi udaas the.

Sita ki yaad unhe sone nahi deti thi.
Raat ko woh bas aasman ki taraf dekhkar
ghehri saanse bharte rehte.

Lakshman apne bhai ko dukh me dekhkar
bohot pareshaan hua.

⭐ Lakshman Ki Dilasa Deti Baatein

Lakshman pyaar se bole:

“Bhaiya, aap yun gham me dubkar
apni shakti kam mat karo.

Jo vyakti hamesha roye,
uska kaam kabhi safal nahi hota.

Aapko dharm, himmat aur bhagwan par vishwas rakhna hoga.
Ravana chalak hai—
agar mann kamzor hua
to hum Sita Mata ko kaise bachayenge?

Barsaat khatam hote hi
aap poori duniya hila doge.
Bas thoda intezaar karo
aur apna junoon jagao.”

⭐ Rama Ka Sankalp Wapas Jaga

Rama ne Lakshman ki baat suni
aur dheere-dheere unke chehre par
phir se veerta chamakne lagi.

Rama बोले:

“Tumne theek kaha, Lakshman.
Ab main apna dukh pee jaunga
aur Ravana ko dhoond kar hi rahunga.

Sugriva barsaat ke baad zaroor madad karega.
Aur main uska upkar kabhi nahi bhoolunga.”

Lakshman ne haath jodkar kaha:

“Bhaiya, hum dono yeh chaar mahine
yahin shanti se guzaarenge.
Phir hum Ravana ka anth karenge.”

Aur is tarah,
Rama aur Lakshman ne Prasravana par
apna intezaar ka samay shuru kiya—
par Rama ke dil me
Sita ki yaad hamesha dard ki tarah ane lagi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.28
    with st.expander("Chapter 4.28 – Rama talks about the rainy season"):
        text1 = """ 
⭐ Chapter 28 – Barish Ka Mausam Aur Rama Ka Dard (Hinglish Kahani)

Bali ki maut aur Sugriva ka rajyabhishek ho chuka tha.
Ab Rama, Lakshman ke saath Malyavat parvat par reh rahe the.
Barish ka mausam aa gaya tha.

Rama aasman ki taraf dekh kar Lakshman se bole:

“Lakshman, dekho… badal pahaadon jaisa lag raha hai.
Nau mahine samundar ka paani sooraj ne sukha liya,
ab aasman fir se us paani ko barsa raha hai.

Aasman pe laal, peele, kaale rang ek saath milkar
bilkul chot khaaye hue insaan jaisa lagta hai.
Thandi hawa me ketaki aur mitti ki khushboo ghul rahi hai.

Zameen garmi se jal gayi thi,
ab barish me aankhon ki tarah aansu baha rahi hai—
bilkul Sita ki tarah.”"""

        create_image_text_layout("attached_assets/chapter4/4.28.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Pahaad Aur Jungle Ka Sundar Roop

Rama ne aas-paas ki khoobsurti ko dekhkar kaha:

“Yeh pahaad dekho Lakshman—
barish se chamak raha hai.
Arjuna ke peedh phoolon se bhare hain.
Gufaaon me hawa gusar rahi hai,
aur awaaz nikal rahi hai jaise brahmin Ved gunguna rahe ho.

Bijli ko dekho—
jaise aasman ko peeli chabuk se maara ja raha ho.”

Rama ko bijli ki chamak me
Sita ki jhulti tasveer nazar aayi.

Phir Rama bole:

“Yeh badal pehadiyon jaise jambooke phal ban gaye hain.
Hans, bagule aur mor yahan wapas aa gaye hain.
Peacocks khushi me nach rahe hain.”

⭐ Barish Ke Mausam Ki Badalti Duniya

Rama barish ke nazare dekh kar bolte ja rahe the:

“Raste dube hue hain,
gaadiyaan chal nahi sakti.
Nadiyan tez bhaav le kar peedh ke phool utha rahi hain.

Jambu ka phal pak gaya hai—
mitha aur rangin.
Aam neeche gir rahe hain.

Badal girte paani se moti jaisi boondein gira rahe hain.
Hawa me madhumakhiyon ki gunjan,
maine-mand peeli bijli,
aur jangal me mor ka naach—
yeh sab ek bada sangeet jaisa lag raha hai.

Hawaa thandi ho gayi hai.
Mitti me laal bindi jaise ladybirds chamak rahi hain.
Jungle me jangli hathi,
mor aur bees sab apni apni masti me hain.”

⭐ Rama Ka Dard Gehraa Hota Gaya

Par jitna hi jangal sundar hota gaya,
Rama utne hi udaas hote gaye.

Rama ne dukhi awaaz me kaha:

“Lakshman… Sugriva shayad iss barish ka maza le raha hoga—
usey sab wapas mil gaya:
patni, rajya, shanti.

Par main?
Main to Sita ke bina us nadi ke kinaare jaisa hoon
jiska kinara toot kar beh gaya ho.
Barish me raaste band ho gaye hain.
Main kuch kar bhi nahi sakta.

Aur Ravana…
vo mujhe ab aur bhi bhayanak lagta hai.”

Rama ki awaaz bhar aayi.

⭐ Lakshman Ka Dharam, Himmat Aur Dilasa

Lakshman haath jod kar bole:

“Bhaiya, aapka dukh main samajh sakta hoon…
par barish me kuch nahi ho sakta.

Sugriva apna vaada nibhayega—
aapne uske liye sab kuch kiya hai.
Aap bas sharad ritu ka intezaar karo.

Jaise hi barsaat khatam hogi,
hum dono milkar Ravana ka anth kar denge.”

Rama ne dheere se sir hila kar kaha:

“Tum theek kehte ho, Lakshman.
Main intezaar karunga—
barish, Sugriva aur samay
sab mere paksh me aayenge.”

Aur is tarah,
Rama rainy season me bhi
Sita ki yaad me jalte rahe,
lekin Lakshman ki baaton ne
unka sankalp phir se majboot kar diya."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.29
    with st.expander("Chapter 4.29 – Hanuman reminds Sugriva of his promise to help find Sita"):
        text1 = """ 
⭐ Chapter 29 – Hanuman Ne Sugriva Ko Yaad Dilaya Apna Vaada

Barsaat khatam ho chuki thi.
Aasman saaf tha—na bijli, na badal.
Sirf chaand ki roshni aur saras ke panchhiyon ki awaaz.

Par Sugriva…
jo kabhi apne dukh me dooba hua tha…
ab apne rajya, apni patni Ruma aur Tara ke saath sukh-masti me dooba hua tha.

Rajya ka kaam mantriyon ke hawale,
aur din-raat bas manoranjan.
Rama ka vaada?
Jaise use yaad hi na raha ho."""

        create_image_text_layout("attached_assets/chapter4/4.29.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Hanuman Ne Sab Samajh Liya

Hanuman, jo hamesha samay aur kartavya ko samajhta tha,
usey pata chal gaya ki Sugriva raaste se hat raha hai.

Woh shaant lekin majboot awaaz me Sugriva ke paas gaya
aur bola:

“Sugriva, tumne apna rajya wapas le liya, apni patni ko bhi.
Ab tumhara agla kartavya hai—
apne dost Rama ka kaam poora karna.
Jo dost hum par badi kripa karta hai,
uska upkaar chukana hi sabse bada dharm hota hai.”

⭐ Hanuman Ki Seekh (Simple Aur Seedhi)

Hanuman ne pyar aur samajhdaari se samjhaya:

“Jo raja apne doston ko bhool jaata hai, uska dushman jaldi badh jaata hai.”

“Jo dost ki mushkil me saath nahi deta, vo kabhi sachha veer nahi hota.”

“Rama ne tumhare liye apni jaan tak daav pe laga di.
Ab tumhari baari hai, Sugriva.”

Phir Hanuman ne gahri baat kahi:

“Rama ne tumhe abhi tak yaad nahi dilaya…
kyunki Rama vinamra hai.
Par iska matlab yeh nahi ki tumhe bhool jana chahiye!
Agar hum der kar denge, to sharmindagi bhi hogi
aur paap bhi lagega.

Chalo, turant Sita ki talaash shuru karte hain!”

⭐ Sugriva Ko Baat Samajh Aayi

Hanuman ki baatein seedhi dil me utar gayi.

Sugriva ne turant faisla kiya.

Vo Nila ko bulakar bola:

“Nila, turant pura vanar sena ikatthi karo!
Pahaad, jungle, samundar—
jahaan bhi vanar tainat hain, sabko bulao.

Jo vanar 15 din ke andar nahi aaya,
uski sazah sakht hogi.
Angada ke saath jaakar
har ek veer ko yudh ke liye tayaar karo!”

Aise kehkar Sugriva
wapas apne mahal ki taraf chala gaya—
par iss baar zimmedaari samajh kar."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.30
    with st.expander("Chapter 4.30 – The autumn season is described"):
        text1 = """ 
⭐ Chapter 30 – Sharad Ritu Aur Rama Ka Dukh

Barsaat khatam ho gayi thi.
Aasman bilkul saaf, badal bilkul gayab.
Chaand ki roshni itni nirmal thi ki dil ko shanti milti…
par Rama ke dil ko nahi.

Rama ne dekha ki Sugriva to palace me apni nayi khushi me mast hai—
par Sita abhi bhi durr, akeli, dukhi.

Is soch ne Rama ka dil phir se bhaari kar diya."""

        create_image_text_layout("attached_assets/chapter4/4.30.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Rama Ka Dard

Rama pahad ki choti par baitha tha.
Neeche chamakte jungle, aasman me udte hans,
aur hawa me thandi thandak…

Phir bhi woh udaas tha.

Woh dheere se bola:

“Autumn itna sundar lag raha hai…
par Sita ke bina mujhe kuch acha nahi lagta.

Vo cranes ki awaaz pasand karti thi…
ab jab ye awaaz sunegi… to kitna roegi?

Vo kamal jaise phoolon ko pasand karti thi…
aur ab vo akeli kaise muskuraayegi?”

Rama ka dil toot gaya.
Usse Sita ki yaad ruk hi nahi rahi thi.

⭐ Lakshmana Ka Samjhana

Isi waqt Lakshmana fruits lekar wapas aaya.
Usne Rama ko itna udaas dekha to bola:

“Bhaiya, aap himmat kyu haar rahe ho?
Yeh samay ro-ne ka nahi,
sochne ka hai.

Sita jaise agni ko dushman choo bhi nahi sakta.
Hum usey wapas laayenge.”

⭐ Rama Ka Naya Sankalp

Rama ne gehri saans li aur bola:

“Lakshmana, tum theek kehte ho.
Jab shakti ho, himmat ho,
to darr ki koi jagah nahi.

Ab sharad ritu aa chuki hai.
Aasman saaf hai.
Yeh hi ladayi ki shuruaat ka samay hota hai.”

Lekin phir Rama ka mann phir Sita ki yaad me bhar gaya.

⭐ Rama Autumn Ka Varnan Karte Hain

Rama aasman ki aur dekhte hue bola:

“Dekho Lakshmana—

Badal chala gaye

pahaad fir chamak rahe hain

nadiyaan shaant beh rahi hain

hans aur crane wapas aa gaye

hathi aaraam se jal me chal rahe hain

jungle me ful phir se khil gaye

teekhi dhoop me mitti sookh rahi hai

Ye sharad ritu sabke liye khushi laati hai…

Par mere liye nahi, Sita ke bina nahi.”

⭐ Rama Ka Krodh Badhta Hai

Fir Rama ne gahri udaasi me kaha:

“Lakshmana… 4 mahine beet gaye.
Saara samay to Raghuvanshi ne dhairya se intezaar kiya.

Par Sugriva?
Woh to apni masti me hi laga hai.
Usne apna vaada bhool gaya.”

Rama ki awaaz sakht ho gayi:

“Jab maine Bali ko maara,
Sugriva ne vaada kiya tha
ki barsaat khatam होते hi woh Sita ki talaash karega.

Par aaj vo rajya me mast hai—
Na koi taiyari, na koi sena ka bulawa…”

Rama ne Lakshmana ki taraf dekha aur bola:

⭐ Rama Ka Sandesh Lakshmana Ke Liye

“Lakshmana, tum Kishkindha jao.

Sugriva se kehna:

‘Jo aadmi upkaar ka badla nahi deta,
vo sabse nichla aadmi hota hai.’

‘Rama ne tumhari jaan bachai, tumhara rajya diya.
Ab tumhara kartavya hai apna vaada nibhaana.’

‘Agar tumne apna vachan tod diya,
to Bali jaise anjaam se tum bhi nahi bachoge.’”

Lakshmana ne bhai ke krodh ko dekha
aur uska khoon bhi garam ho gaya.

Usne socha:
“Ab Sugriva ko jagana hi hoga.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.31
    with st.expander("Chapter 4.31 – Lakshmana goes to Kishkindha"):
        text1 = """ 
⭐ Lakshmana Ka Gussa Aur Kishkindha Ka Dar

(Hinglish Kahani — Chapter 31)

Rama ka dil dukh se bhaar ho gaya tha.
Sita ki yaad, Sugriva ki be-parwahi… sab kuchh unhe chubh raha tha.

Ye dekh kar Lakshmana, jo sher jaise shaktishaali aur dil se komal tha,
gusse se kaamp uthaa.

⭐ Lakshmana Ka Gussa

Lakshmana bola:

“Bhaiya, Sugriva ne to hadd kar di!
Aapne uska rajy wapas dilaya, aur woh…
bas dosti ka karz bhool kar maze le raha hai!

Aisi bewafaayi bardasht nahi hoti.
Main abhi jaake usse sabak sikha deta hoon!”

Lakshmana ka gussa bijli ki tarah chamak raha tha."""

        create_image_text_layout("attached_assets/chapter4/4.31.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Rama Ka Shaant Updesh

Par Rama ne haath pakad kar kaha:

“Lakshmana, shant ho jao.
Bada veer wahi hota hai jo gusse ko rok sake.

Sugriva ne galti ki hai,
par tum usse pyar se samjhana.
Kathor shabd mat kehna.
Bas yaad dilana ke waqt nikal raha hai.”

Rama ke shabd thande paani jaise the.
Lakshmana ne unhe maana, par dil me aag ab bhi jal rahi thi.

⭐ Lakshmana Kishkindha Me

Apna dhanush pakde, Lakshmana aandhi ki tarah Kishkindha ki taraf badhe.
Raaste ke ped—Sala, Tala, Saral—
sab unke zor se hil rahe the.

Monkeys unki aahat sun kar dar gaye.
Kuchh ne pahad ke tukde utha liye,
kuchh ne bade-bade ped jad se ukhaad liye,
par Lakshmana ki aag dekh kar
sab idhar-udhar bhaag gaye.

Lakshmana sach me krodh-kaal jaise dikh rahe the.

⭐ Angada Ka Dar

Angada, jo Bali ka beta tha,
himmat jutaa kar aage aaya.

Lakshmana garajte hue बोले:

“Beta, jao Sugriva ko bolo—
Lakshmana, Rama ka chhota bhai,
darwaaze par khada hai.
Woh gusse se dahak raha hai.
Usse turant bulao!”

Angada ghabra kar andar bhaaga.

⭐ Sugriva Behosh Si Neend Me

Sugriva tab tak
daaru aur manoranjan me dooba hua so raha tha.
Tara uske paas thi,
aur woh sab kuchh bhool chuka tha—
dosti, vaada, Sita ki dhoondh… sab.

Angada ne paon chhu kar bola:
“Maama… Lakshmana aaye hain!”

Par Sugriva ne aankh bhi nahi kholi.

⭐ Monkeys Ka Shor Aur Dar

Baahar, monkeys Lakshmana ko dekh kar
dar ke maare zor zor se cheekhne lage—
jaise bijli garaj rahi ho!

Iss shor se Sugriva ki neend toot gayi.
Aankhen laal, sharab ka nasha,
aur ghabrahat sab ek saath aa gaye.

Uske do buddhimaan mantri—Yaksha aur Prabhava—
aur Angada uske paas aaye.

⭐ Mantriyon Ka Seedha Sandesh

Unhone kaha:

“Raja, Rama aur Lakshmana dono dev-samaan veer hain.
Lakshmana bahar aag ki tarah khaRa hai.
Monkeys uski ek jhalak se darr rahe hain!

Woh tumse baat karne aaye hain.
Unka gussa shant karo—
sir jhuka kar unke charanon me pranaam karo.
Aur Rama ka kaam turant poora karo.
Vaada nibhana hi sachchi shaurya hai, Rajan.”

Sugriva ab poori tarah hosh me aa gaya.
Use samajh aa gaya ki uski badi galti ho chuki hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.32
    with st.expander("Chapter 4.32 – Hanuman speaks to calm Lakshmana"):
        text1 = """ 
⭐ Hanuman Ka Samajhdari Bhara Updesh

(Hinglish Kahani — Chapter 32)

Angada aur mantriyon ki baat sunkar
Sugriva ki neend aur nasha dono utar gaye.
Ab use mehsoos hua ki baat bahut bigad gayi hai.

Sugriva ghabra kar bola:

“Main ne kya galat kiya?
Lakshmana mujhse itna kyon gussa hai?
Kahin koi dushman hum dono ke beech fasad to nahi kar raha?

Rama ne mere liye itna kuchh kiya…
Aur main unka udhaar abhi tak chuka nahi paaya.
Dosti nibhaana aasaan nahi hota…
Bas, isi baat ka darr hai.”

Sugriva ki awaaz me pachtawa tha."""

        create_image_text_layout("attached_assets/chapter4/4.32.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Tab Hanuman Utha — Buddhi Ka Sagar

Hanuman, jo sabse buddhimaan, sabse wafadaar aur sabse shaktishaali
vanaron me pramukh tha,
shant aur saaf man se bola:

“Rajan, ye bilkul sahi hai ki Rama ne tumhara kabhi na bhoolne wala upkaar kiya.
Unhone Bali jaise shaktishaali vir ko tumhare liye maar giraya.
Aisa kaun karta hai?

Par dekho, ab mausam badal chuka hai.
Sharad ritu aa gayi hai—
aasmaan saaf hai, sitaare chamak rahe hain,
nadia shant hain…
Ye hi woh samay hai jab hum Sita ki talaash shuru karne wale the.

Lekin tum to manoranjan me doob gaye, Rajan…
Tumne waqt ki pukaar sun hi nahi paayi.

Issi liye
Rama ne apne bijli-jaise bhai Lakshmana ko bheja hai.
Jab bada veer naram shabd ke bajay kathor shabd bheje…
To samajh lo uske dil me chot pahunchi hai.

Isliye ye gussa swabhavik hai.”

⭐ Hanuman Ki Sachchi Salah

Hanuman phir jhuk kar par honsle se bola:

“Rama ko naraz karna samajhdari nahi.
Woh dhanush utha le to devtaon, asuron aur gandharvon ko bhi hila de.

Rajan, humne unka ehsaan liya hai.
Ab unki madad karna humara kartavya hai.
Aise veer se dosti todna… ya unki baat ko nazarandaz karna…
Bahut badi chook hogi.

To mera vichaar ye hai—
Lakshmana ke saamne jhuk kar unse kshama maango.
Angada aur poori sena ke saath jao.
Dosti me vinamrata hi shobha deti hai.

Aur sabse zaroori—
Apna vaada nibhao, Rajan.
Sita ki talaash abhi shuru honi chahiye!”

Hanuman ki baat
sach, seedhi aur sahi thi.
Sugriva ne unhe dhyan se suna—
Uska mann ab sharm aur samajh dono se bhar chuka tha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.33
    with st.expander("Chapter 4.33 – Tara gently stops Lakshmana from getting angry"):
        text1 = """ 
⭐ Tara Ne Kaise Shant Kiya Lakshmana

(Hinglish Kahani — Chapter 33)

Lakshmana, Rama ka wafadaar bhai,
Kishkindha ki chamakdar nagri me ghusse ja raha tha.
Uske chehre par gussa saaf dikhta tha—
jaise aandhi apna rasta banati hai.

Darwaze par bade-bade vanar pehredaar
haath jod kar khade ho gaye.
Lakshmana ki bhari saanson aur tej nazron se
woh dare hue the, par uska rasta rokne ki himmat nahi kar paye."""

        create_image_text_layout("attached_assets/chapter4/4.33.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Kishkindha Ki Chamak

Lakshmana ne shehar dekha—
hara-bhara, phoolon se saja,
mehenge pattharon aur sona-chandi se chamak raha.
Har taraf bade mahal, unme gaana, veena ki dhun,
khush vanaron ki chal-phir.
Sab kuchh itna sundar, par
Lakshmana ke mann me bas ek hi cheez thi—Rama ka dukh.

Jab woh andar badha,
usne Sugriva ke mahal se
nupur ki jhankar aur hasta-khelta geet suna.
Ye sab dekh kar Lakshmana ka gussa
phir se bhadak utha—
aur usne apna dhanush ka taar khinch kar
ek zor ka tan-tan! kiya.

Pura mahal kaanp uthaa.
Sugriva, jo madh-seen tha,
turant hosh me aaya aur dar gaya.

⭐ Sugriva Ka Pachtawa

Sugriva ne Tara se ghabra kar kaha:

“Lakshmana gussa kyon hai?
Rama jaise mitra ko main kaise naraaz kar sakta hoon?
Agar koi galti mujhse ho gayi ho…
to tum jaakar uska gussa thanda karo, Tara.
Veer purush auraton se kathor nahi bolte.”

⭐ Tara — Buddhi aur Komalta Ka Sangam

Tara, jise sab sundar aur samajhdar jaante the,
halke ladkhadate kadmon se Lakshmana ke paas aayi.
Lakshmana ne ek pativrata aurat ko dekh kar
apna gussa turant rok liya
aur sir jhukakar samman dikhaya.

Tara ne naram awaaz me poocha:

“Hey Rajputra, ye itna gussa kyon?
Kisne tumhari baat nahi mani?
Kaun aag lekar sookhe jungle me ghus gaya?”

⭐ Lakshmana Ka Dard

Tara ki komal baaton se Lakshmana ka gussa halka hua,
par dard abhi bhi tha.

Lakshmana ne shant par kathor shabdon me kaha:

“Sugriva apni zimmedari bhool gaya hai, Tara.
Usne Rama se vaada kiya tha.
4 mahine beet gaye…
Par woh prem, nasha aur manoranjan me dooba hua hai.

Aise kaise chalega?
Dosti ka matlab hota hai—vaada nibhaana.
Aur samay par madad dena.

Tum hi batao,
ab kya kiya jaye?”

⭐ Tara Ka Samjhaav

Tara ne pyaar aur samajh se bola:

“Hey Lakshmana,
gussa chhodo.
Sugriva ne galti ki hai, par jaan-boojh kar nahi.
Kabhi-kabhi manushya bhi vasana me beh jate hain—
to ye to vanar hai, prakriti se chanchal.

Par suno—
Sugriva ne tumhare kaam ki tayari kar rakhi hai.
Duniya bhar ke vanar—
hazaron, laakhon, karodon—
sab pahunch chuke hain.

Tum andar aao,
hamara ghar tumhare liye pavitra hai.”

⭐ Lakshmana Ka Andar Jana

Tara ki baat sunkar Lakshmana ne
apna gussa ek taraf rakha
aur andar gaya.

Wahan Sugriva sona jaise chamakta,
rajasi pehnawa, sugandhit pushp,
aur sundar mahal me ruma ko gale lagaye baitha tha.

Par jaise hi usne Lakshmana ko dekha,
uski aankhon ki neend aur madira sab gaayab ho gayi.

Ab samay aa gaya tha—
Sugriva ko apni galti sudhaarni thi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.34
    with st.expander("Chapter 4.34 – Lakshmana scolds Sugriva"):
        text1 = """ 
⭐ Lakshmana Ki Sakht Daant – Sugriva Ko Yaad Dilayi Zimmedari

(Hinglish Kahani — Chapter 34)

Sugriva ne jaise hi Lakshmana ko andar aate dekha—
aankhen laal, saans tez, gussa agni ki tarah,
uska dil ghabra gaya.

Woh turant apne sone ke singhasan se uth kar
Lakshmana ke saamne khada ho gaya,
aur uske peeche Ruma aur anya vanar-stree jaise
chaand ke aas-paas taaron ki tarah khadi ho gayin.

Lakshmana ne Sugriva ko dekha—
raat ke aasman me chaand jaise,
par aas-paas vasana aur aalas ka badal.
Tab Lakshmana ka gussa aur bhadak gaya."""

        create_image_text_layout("attached_assets/chapter4/4.34.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Lakshmana Ki Teekhi Par Sachchi Baatein

Lakshmana ne kadak awaaz me kaha:

“Sugriva!
Sacha raja woh hota hai
jo daya-bhara ho,
jo apne vaade nibhaaye,
jo doston ka ehsaan yaad rakhe.

Par jis raja me
na wafadari ho, na shukrana,
woh duniya me badnaam hota hai."

Lakshmana ne ek ek shabd
tez talwar ki tarah chalaya:

"Jo aadmi jhooth bolkar
ghodon ka nuksaan karta hai,
woh sau ghodon ka papi hota hai.
Jo jhooth gai ke baare me bole,
woh hazaar gaayon ka papi hota hai.
Par jo insaan ke baare me jhooth bole—
woh apni aur apne khandaan ki barbaadi bulaata hai.

Par sabse bada paap kya hai?
Ahankaar aur ahsaan-faramoshi.
Iska koi prayashchit nahi!”

Sugriva ka chehra nichla pad gaya.

⭐ Lakshmana Ki Krodh-Vaaniyon Ka Bijli Jaisa Prabhav

Lakshmana ne sakht shabdon me kaha:

“Rama ne tera sab kuchh lautaya—
tera rajya, tera maan,
tera jeevan tak bachaya!

Aur tu?
Tu to vaada nibhaana hi bhool gaya.
Tu sukh-bhogon me dooba hua,
jabki Rama dukh se jal raha hai.

Tu un logon me se hai
jo saap to hote hain,
par awaaz mazedaar mendhak jaise nikaalte hain—
dhokebaaz.

Yad rakh…
Bali ka raasta abhi band nahi hua.
Agar tu apna vaada nahi nibhaaya,
to Rama ke teer tujhe bhi wahi le jayenge!”

Sugriva ka kaleja dahal gaya.
Usne apni aankhen neeche kar li.

Lakshmana ne aakhri baar sakhti se kaha:

“Abhi samay hai, Sugriva.
Apna vaada nibhao.
Rama ka dukh khatam karo.
Varna tumhari raah bhi Bali ki raah ban jayegi.”

Yeh sunte hi, Sugriva ki aankhon se nasha aur madh-matra ka rang udd gaya.
Usse samajh aa gaya—
ab kaam karne ka samay aa chuka hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.35
    with st.expander("Chapter 4.35 – Tara explains and defends Sugriva"):
        text1 = """ 
⭐ Tara Ka Bachav — Sugriva Ki Taraf Se Prem aur Buddhi Ki Baat

(Hinglish Kahani — Chapter 35)

Lakshmana gusse se bhara hua tha—
jaise garajta hua baadal,
jaise agni ki laal-lal jaan se nikli chamak.

Tabhi Tara, jiska chehra poornima ke chaand jaise komal aur shant tha,
aage badh kar dheemi, par drit, awaaz me boli:"""

        create_image_text_layout("attached_assets/chapter4/4.35.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ “Lakshmana, Sugriva itna bura nahi!”

“O Lakshmana,” Tara ne kaha,
“Yeh kathor shabd Sugriva ke laayak nahi…
aur woh bhi tumhare muh se!

Sugriva na bewafa hai, na jhootha,
na ehsaan-faramosh!
Woh dhokebaaz bhi nahi,
aur na hi koi kapati!”

Tara ki awaaz me sachchai thi.
Woh jaanti thi ke Lakshmana ka gussa dukh se paida hua hai,
isliye usne pyar aur buddhi dono se baat rakhi.

⭐ “Sugriva ne Rama ka ehsaan kabhi nahi bhoola.”

Tara ne shant hoke samjhaya:

“Rama ne uske liye woh kiya
jo koi aur nahi kar sakta tha.
Rama ne use phir se rajya diya,
phir se samman diya,
aur phir se Ruma aur mujhe uski zindagi me laaya.

Par Lakshmana…
bahut saalo tak dukh jhelne ke baad,
jab kisi ko achanak sukh mile—
toh kabhi kabhi woh waqt ka andaza kho deta hai.”

⭐ “Vishvamitra jaise maha-rishi bhi kabhi bhatak gaye the.”

“Ek baar Vishvamitra rishi bhi,” Tara boli,
“10 saal tak Apsara Ghritachi ki sangati me
samay hi bhool gaye the!
Woh bhi waqt pehchaanne me maahir the—
phir bhi bhatak gaye.

Sugriva ne itne dino baad
thodi si khushi paayi hai,
isliye thoda bhatak gaya hai.
Rama ko use maaf kar dena chahiye.”

⭐ “Sugriva sab kuchh chhod sakta hai—Rama ke liye.”

Tara ne sacche mann se kaha:

“Mujhe poora yakeen hai—
Sugriva Rama ke liye
Ruma, Angada, main khud, rajya, dhan,
gaaye-bhaise—sab kuchh tyaag dega!
Bas ek baar Sita ko dhoondhne ka kaam shuru ho jaaye.”

⭐ “Lanka me rakshas hazaaron me hain—Sugriva akela nahi lad sakta.”

Tara ne Lakshmana ko sach bataya:

“Lanka me to ajeeb-shakal wale,
bhayankar balwale rakshas
hazaaron, lakhi aur milioni sankhya me rehte hain.

Unka saamna bina taiyyari ke—
aasan hi nahi, namumkin hai.

Isliye Sugriva ne
saare vanar sena,
saare shaktishaali sainiko—
bears, golangulas, aur kotiyon vanaron ko
bulaaya hai.

Woh sab aaj hi aa rahe hain.”

⭐ “Lakshmana, apna gussa shaant karo.”

Ant me Tara ne nivedan kiya:

“O Lakshmana,
tumhara chehra gusse se laal ho gaya hai.
Tumhari aankhen bijli ki tarah chamak rahi hain.

Yeh dekh kar vanaron ki patniyaan
phir se dara hui hain—
jaise pehle Bali ke samay dar gayi thi.

Kripya apna krodh shaant karo.
Sab taiyyar hai—
Sugriva ne kuchh bhi nahi bhoola.”

Tara ki meethi, buddhi-bhari baatein
Lakshmana ke dil tak pahunchne lagi.
Aandhi jaisa uska krodh
ab halki si hawa me badalne laga…"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.36
    with st.expander("Chapter 4.36 – Lakshmana forgives Sugriva"):
        text1 = """ 
⭐ Lakshmana aur Sugriva ka Milap

(Hinglish Kahani — Chapter 36)

Tara ki pyari, samajhdaari bhari baatein
Lakshmana ke dil me utar gayin.
Saumitri, jo apne swabhaav se hi komal aur vinamra tha,
ab dheere dheere shant ho gaya.

Usne dekha ki Tara imaandari se
Sugriva ka paksh rakh rahi hai—
aur uski baaton me sachchai hai.
Lakshmana ka gussa pighalne laga
jaise dhoop me barf."""

        create_image_text_layout("attached_assets/chapter4/4.36.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Sugriva ne apna dar utaar phenka

Lakshmana ke shant hote hi
Sugriva ka dar bhi mit gaya—
jaise koi bheega kapda utaar kar fek deta hai.

Usne apne gale se
woh rang-biranga, shandar haar bhi utaar diya
jo uski rasiya zindagi ka prateek tha.

Ab woh bilkul hosh me tha.
Aankhon me satarkta,
dil me vinamrata.

Woh Lakshmana ke aage jhuk kar bola:

⭐ “Rama ne mujhe sab kuchh diya hai…”

“O Saumitri,” Sugriva ne gahri awaaz me kaha,
“Rama ne mujhe sab lauta diya—
mera rajya,
mera maan,
meri izzat…
aur meri parivaar tak.

Kaun hai jo Rama ka ehsaan chuka sakta hai?
Main toh unka udhaar kabhi nahi utaar sakta!

Rama to apni hi shakti se
Sita ko wapas layenge,
aur Ravana ko maar girayenge.
Main?
Main toh bas unke saath chalunga.”

Sugriva ne yaad kiya—
kaise Rama ne ek teer se
saat saal ke drakshya vriksha,
ek pahaad,
aur zameen ko chhed diya tha!

“Jis veer ka dhanush tanne se hi
duniya kaanp uthe—
use meri madad ki kya zaroorat?”

Phir Sugriva ne haath jod kar kaha:

“Par agar main kisi baat me galat pada hoon,
kisi farz me dheela pada hoon,
toh Rama mujhe maaf karen—
kyonki kaun sa insaan bina galti ke hota hai?”

⭐ Lakshmana ka dil pighal gaya

Lakshmana ne Sugriva ki baatein suni…
aur unke chehre par naram si muskaan aa gayi.

Woh bola:

“O Sugriva,
agar tum saath ho
toh Rama ko kisi sahayata ki kami nahi.

Tumhara vinamr swabhaav,
tumhari bahaduri,
aur tumhari wafadaari—
ye sab tumhe monkey-rajya ka
sabse yogya raja banati hain.

Tumne galti maani—
aur jo apni galti maanta hai,
woh asli veer hota hai.
Tum aur Rama—
dono ek jaise ho—
bal me bhi,
veerata me bhi.”

Phir Lakshmana ne haath badha kar kaha:

“Chalo, Sugriva!
Rama dukhi hain—
unhe hamari zaroorat hai.
Chalo unke paas chalein.”

Aur phir halka sa jhuk kar bola:

“Jo kathor shabd maine gusse me kahe…
unhe maaf kar dena, Sugriva.”

Lakshmana aur Sugriva—
dono ke dil ka bojh halka ho gaya.
Dosti fir se phool jaisi khil gayi.
Aur ab—
Sita ki talaash ka yuddha
sach much shuru hone wala tha…"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.37
    with st.expander("Chapter 4.37 – Sugriva gathers his monkey army"):
        text1 = """ 
⭐ Sugriva Bulata Hai Duniya Bhar Ke Vanaron Ko

(Hinglish Kahani — Chapter 37)

Lakshmana ke madhur aur samajhdaari bhare shabdon ko sun kar
Sugriva ka hausla badh gaya.
Ab woh poori taiyaari se Rama ka saath nibhane ke liye khada tha.

Woh Hanuman ki taraf mudkar bola—

⭐ “Hanuman, poori duniya ke vanaron ko bulao!”

“Hanuman!
Mahendra parvat ki chotiyon par jo rehte hain…
Himavat ke kathor pahaadon par jo tap karte hain…
Vindhya, Kailash, Mandara aur Pandu parvat ke veer…
Aur Panch-parvat ke vanar…

Sea ke pashchimi kinaare,
Suryadev ke nikat pahadon,
Padmachalu ke ghane vanon,
Aur Anjana parvat ke veer—
jinme hathi jaisi shakti hai—
sab ko bulao!"""

        create_image_text_layout("attached_assets/chapter4/4.37.jpg", text1, layout="side", image_position="left")

        text2 = """ 
Jo vanar sona jaisi chamak rakhte hain,
jo guhaon me rehte hain,
jo Meru, Dhoomra aur Maharuna parvaton me baste hain…

Jahan jahan ho sakta hai—
sab ko ek saath jama karo!

Agar koi aaram kare,
ya mazaa lete hue mere aadesh ko bhool jaye,
to use kaha do—
das din ke andar na aaye, to dand milega.”

Sugriva ki awaaz aadesh se bhari thi—
raja hone ka garaj usme mehsoos ho raha tha.

⭐ Hanuman jaise hawa ki tarah daud pade

Vaayuputra ne jhuk kar aadesh svikaar kiya,
aur turant
team by team, toliyaan toliyaan
vanaron ko chaaro dishaon me bhej diya.

Woh aasman ki un ungliyon se guzre
jin par pakshi bhi kabhi kabhi hi jaate —
Rahu, Ketu, Surya aur Chandrama ke margon se bhi pare.

Hawa, pahaad, dariya, samundar—
sab ko paar kar ke
monkey-messengers
Sugriva ka sandesh pohcha rahe the:

“Rama ke liye jama ho jao!”

⭐ Duniya bhar se Vanaron ka maha-saagar umad pada

● Anjana parvat se —
teen koti ka kaala, kajal jaisa sena-dal!

● Pashchim ke din dhalne wale pahaad se —
das koti sona-jaisey chamakdar vanar!

● Kailash se —
sher ke ghar ke rang ke hazaar vanar!

● Himavat se —
aulaukik tapasvi vanar—das-das million tak!

● Vindhya ke laal-coal jaisey bhayanak vanar—
sau sau million ki tezi se daudte hue!

● Samundar ke safed kinaaron se,
● Tamala van se,
● Nariyal ke vanon se—
itne vanar aaye ki ginti ka bhi pata nahi chal sakta tha!

Poori prithvi ka har vanar lag raha tha
jaise Rama ke liye tayaar ho kar nikla ho.

⭐ Himavat ke shikhar par paaya gaya divya vriksha

Jab kuchh vanar dusron ko bulane gaye,
to unhe Himavat ke shikhar par
ek prakritik, divya vriksha mila.

Kehte hain ki purva kal me
Mahadeva ke samman me wahan yagya hua tha—
aur us yagya se
amrit jaise phal, jadibootiyan aur beej
janm le liye the.

Unhe kha kar
ek mahine tak bhookh nahi lagti thi.

Vanaron ne woh sab divya phal, jadibootiyan,
sugandhit pushp ikattha kiye
aur Sugriva ko arpan karne laut padey.

⭐ “Maharaj, poori duniya ke vanar aa gaye!”

Jab sab messenger laut aaye,
to Sugriva ke raj-dwar par
laakhon-croadh vanar
samudra ki tarah umad rahe the.

Unhone kaha—

“Hum ne pahaad, dariya, jungle sab khoj liye—
duniya ka koi bhi vanar baaki nahi.
Sab aapke aadesh par aa gaye hain.”

Sugriva ka chehra chamak utha.
Usne saare phal, jadibootiyan aur pushp
khushi se accept kiye—

Kyunki ab—
Rama ki sena tayaar thi.
Sita ki talaash ka asli mahasangram
shuru hone wala tha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.38
    with st.expander("Chapter 4.38 – Sugriva goes to meet Rama"):
        text1 = """ 
⭐ Sugriva Rama Se Milne Chalta Hai

(Hinglish Kahani — Chapter 38)

Sugriva ne jab sab monkeys ke laaye hue phal, phool aur jadibootiyan accept ki,
to woh bade khush hua.
Usse lag raha tha—
Rama ka kaam ab sach-much shuru ho chuka hai.

Jab sab vanar apna kaam karke chale gaye,
tab Lakshmana ne namrata se kaha—

“Mitra, ab Kishkindha se nikalne ka samay aa gaya hai.”

Sugriva ne turant kaha—

“Theek hai Lakshmana, chalo. Main poori tarah tumhare adhesh me hoon.”

Usne Tara aur sab mahilaon ko wapas bhej diya
aur zor se apne senapatiyon ko bulaya—"""

        create_image_text_layout("attached_assets/chapter4/4.38.jpg", text1, layout="side", image_position="left")

        text2 = """ 
“Idhar aao!”

Jitne bhi vanar raj-mahal ke andar the,
sab daud kar aa gaye, haath jod kar.

Sugriva ne kaha—

“Jaldi jao, ek shandar palki lao!”

Vanar bijli ki tarah bhaage
aur thodi der me ek sunahari palki,
prabha se chamakti hui, le aaye.

Sugriva ne Lakshmana se kaha—

“Saumitri, pehle aap palki par baithiye.”

Lakshmana bete ho gaye.
Phir Sugriva bhi baith gaya.

Vanaron ne palki utha li—
upar safed chhatra tha,
aur yak-ke-poonchh ke pankhe hil rahe the.
Shankh aur nagade baj rahe the,
aur Sugriva poore rajsi andaaz me
Rama se milne chala.

⭐ Rama apne mitra ko aate dekh kar khush ho gaya

Jab vanaron ki badee sena keechindha se bahar nikli
to woh ek kamal se bhare sarovar jaisi lag rahi thi.

Rama ne Sugriva ko dekhkar muskura diya.
Sugriva palki se utar kar
Rama ke charanon me gir gaya.

Rama ne use utha kar gale laga liya—
dosti ki garamjoshi se bhara ek aalingan.

Phir Rama ne pyaar se kaha—

⭐ Rama ka updesh

“Sugriva, sachcha raja woh hota hai
jo apna samay theek se baant kar chalata ho—
kartavya, sukh aur dharma ke beech.
Jo in sab ko bhool jata hai,
woh us aadmi jaisa hota hai
jo ped ki choti par so jaye
aur neeche girne par hi jaage.”

“Ab kaam karne ka waqt aa chuka hai.
Apne mantriyon se salah karo,
O Vanar-Raj!”

⭐ Sugriva ka vinamr jawab

Sugriva ne haath jod kar kaha—

“Rama, mere paas kuch bhi nahi tha—
na rajya, na samman, na parivaar.
Aapki kripa se sab wapas aaya.

Aise upkaar ka badla kaun chuka sakta hai?
Main kabhi bhi nakara nahi ho sakta.

Mere duta chaaro dishaon me gaye hain.
Sankhya me hazaaron, laakhon, croreon—
vanar, bhalu, kapis—
sab aa rahe hain.

Yeh sab veer,
jo devtaon aur gandharvon ke vansh se janme hain,
jo ichha se roop badal sakte hain,
Ravana ke viruddh aapka saath dene ke liye
tezi se aa rahe hain.

Jab yeh sab sena ikatthi ho jayegi,
hum sab milkar Ravana ko hara denge
aur Sita ko wapas laayege.”

Rama ne Sugriva ki taiyaari dekhkar
neele kamal jaisa khil utha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.39
    with st.expander("Chapter 4.39 – Sugriva’s huge monkey forces arrive"):
        text1 = """ 
⭐ Sugriva ki Sena Rama ke Paas Pahunchti Hai

(Hinglish Kahani — Chapter 39)

Sugriva haath jod kar Rama ke saamne khada tha.
Rama ne pyaar se usse gale laga kar kaha—

“Sugriva, tumhare jaise nishtha-waan mitra ka pavitra charitra dekhkar mujhe bilkul haarani nahi hoti.
Jaise Indra barsaat karta hai,
jaise Surya andhera mita deta hai,
waise hi tum apne doston ko khushi dete ho.”

Rama muskuraya aur bola—

“Tum mere saath ho, Sugriva.
Ab main apne sabhi dushmanon ko hara sakta hoon.
Ravana ne Sita ko chura kar apni hi barbaadi bulaayi hai.”"""

        create_image_text_layout("attached_assets/chapter4/4.39.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Achanak Aasmaan Andhera Ho Gaya…

Rama ke shabdon ke turant baad,
aasmaan me ek ajeeb sa andhera chhaa gaya.
Dhool hawa me ghoomne lagi,
dharti hilne lagi—
jaise pahaad, jungles sab kamp rahe hon.

Aur tab…
poori dharti monkeys se bhar gayi!

Unki sankhya itni zyada thi
ki lagta tha jaise pahaadon ki fasal chal padi ho.
Vanar sena ek second me
aasmaan, samundar aur pahaadon se nikal kar
Sugriva ke charon taraf ikatthi ho gayi.

⭐ Har Taraf se Nayak aa Rahe The!
🌄 Shatavali ki sena

Surya jaise laal,
chand jaise safed,
kamal ke dhaagon jaise peele vanar—
hazaaron ki sankhya me Shatavali ke saath aaye.

🏔️ Tara ke pita

Sunehre pahaad jaise bade aur tej.
Hazaaron koti vanar lekar aaye.

🌸 Ruma ke pita

Udit Surya jaise chamakte hue,
woh bhi hazaaron koti vanar sang laaye.

🐾 Hanuman ke pita Kesharin

Tez aur veer monkeys ke sath.

🐻 Dhumra – bhaalu senapati

Do hazaar bhaaluon ki gajab sena.

🐒 Nila

Kaajal jaise kaale,
10 koti monkeys ke maalik.

🌙 Gavaya

Sunehre pahaad jaise tej.
5 kotis ke saath.

🦁 Mainda aur Dvivida – Ashwini Kumaron ke putra

Ek hazaar million vanaron ka netritva!

🐘 Gaja

3 kotis ki sena ke saath.

🐻 Jambavan – Reechhon ka raja

10 kotis ke maha-veer bhalu.

🐒 Angada – Bali ka putra

Anant sankhya me sena—
jaise ant na ho, aakhri ginti hi na mile!

⭐ Hanuman

Apne hazaaron vanar-veeron ke saath
Rama ke charanon me jaakar khade ho gaye.

Aur phir—
Sharabha, Kumuda, Vahni, Rambha, Durmukha…
aise hazaaron neta apni-apni senaon ko lekar aaye
jinhe gin paana namumkin tha!

Poora jagat
pahaad, nadi, jangal—
sab monkeys se bhar gaya.

Jaise badalon ki bheed Surya ko gher leti hai,
waise hi ye Bhutan, Vanar aur Bhalu Sugriva ko gher kar
garaj garaj kar Rama ka swagat kar rahe the.

⭐ Sugriva ka Adesh

Sab neta aage badhe,
haath jod kar Raja Sugriva ke paas aaye.

Sugriva ne Rama ki or dekh kar kaha—

“Prabhu, sab vanar aa gaye hain.
Duniya bhar ki sena aapke aadesh ki prateeksha kar rahi hai.”

Phir Sugriva apne senapatiyon se bola—

“O Vanar-Veeron!
Apni-apni sena ko pahaadon, nadion aur jangal ke paas theek se tainaat karo.
Aur apni sena ki theek-theek ginti bhi pata karo.”

Aur is tarah
Rama ki sabse vishal, adbhut aur tej se bhari sena
Ravana ke khilaaf yuddh ke liye tayyar ho gayi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.40
    with st.expander("Chapter 4.40 – Sugriva sends monkeys to search for Sita in the East"):
        text1 = """ 
⭐ Sugriva Apne Vanaron Ko Poorab (East) Mein Bhejata Hai

(Hinglish Kahani — Chapter 40)

Rama ke saamne khade Sugriva ne kaha—

“Prabhu, meri poori vanar sena taiyaar hai.
Ye sab Mahendra jaise shaktishaali, tej aur buddhimaan hain.
Aapka ek ishara mile, toh ye duniya ke kisi kone tak pahunch sakte hain.”

Rama ne use gale lagaya aur pyaar se bola—

“Mere priya mitra, pehle ye pata karna zaroori hai ki Sita maa zinda hain ya nahi…
Aur Ravana kis jagah chhupa hua hai.
Tum hi is yatra ke neta ho.
Tum waqt aur paristhiti ko sabse achchi tarah samajhte ho.”

Sugriva ne haath jod kar kaha—

“Aadesh dijiye, Prabhu.”

Phir usne apne praabal senapati Vinata ko bulaya—
jo pahaad jaise bade the, aur jinki garaj bijli ki tarah lagti thi."""

        create_image_text_layout("attached_assets/chapter4/4.40.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Vanaron Ka Poorab Ki Taraf Safar

Sugriva ne Vinata se kaha—

**“Vinata! Tum hazaaron vanaron ko saath lekar Poorab ki aur jaao…

Sita aur Ravana ko dhoondo.”**

Fir Sugriva ne unhe ek ek jagah ka naam bataya, jahan tak unhe dhoondhna tha.

⭐ 🗺️ Yeh Sab Jagah Dhoondhni Hain:
🌊 Bade Nadi aur Pahaad

Bhagirathi

Sarayu

Kaushiki

Kalindi

Yamuna

Sarasvati

Sindhu

Shona (laal paani wali nadi)

Mahi aur Kalamahi

🏞️ Desh aur Shehar

Brahmamala

Videha

Malavana

Kashi-Koshala

Magadh

Pundra

Anga

Ye sab van-sampann aur kai khoj se bhare hue desh the.

⭐ 🐾 Ajeeb Aur Anokhe Logon Ka Desh

Sugriva ne kaha—

“Vinata, tum un logon ke beech bhi dhoondhna…
Jinke kaan zameen tak latakte hain,
jo ek pair par bhaagte hain,
jo kala rang aur bhayanak roop rakhte hain,
aur kuch jo manushya-maans khaate hain.”

Fir bola—

“Kirata jaisi jaatein bhi milengi—
sunehre rang wale, lambe baal baandhne wale,
macheli khaane wale shikari.
Unke beech bhi Sita ko dhoondhna.”

⭐ 🌏 Doop, Tapu Aur Gehri Gufaayein

Sugriva ne unhe anek islands (tapus) ki or jaane ko kaha—

Suvama Tapu (sona)

Rupayaka Tapu (chaandi)

Yava ka Tapu

Tez laharon wale samudron ka kinaara

Bhayanak praantar jahan Asura rehte hain

Woh Asura jo upar se guzarti cheez ki parchai tak pakad lete hain!

⭐ Garuda ka Tej Mahal Jaise Ghar

Fir Sugriva ne unhe ek vishesh jagah ke baare mein bataya—

“Aage tumhe ek vishal Shaalmali ka vriksh milega.
Uske paas Vishwakarma ka banaya hua
Garuda ka chamakta mahal hoga—parvat jaisa uncha.”

Wahan ek dushman jaati bhi rehti thi—Mandeha Rakshas,
jo roz suraj ugte hi suraj ki garmahat se gir jaate the,
phir dubara pahado par latak jaate the.

⭐ Samudron Ke Paar – Doodh Jaisa Samundar

Sugriva ne kaha—

“Phir tum Doodh-sa Kshiroda Samudra aayega, jisme Rishabha Pahaad hai.
Wahan Sone jaise kamal, Chaandi jaisi pankhudiyaan milengi.
Yaksha, Kinner, Apsara—sab wahan khelte mil sakte hain.”

Uske baad bhi unhe anek samudron aur pahaadon ka naam bataya—
Jahan tak ek mahina mein dhoondhna sambhav ho.

⭐ Udaya Parvat – Suraj Ugaane Ki Jagah

Ant mein Sugriva ne kaha—

“Poorab ka antim seema Udaya Parvat hai—
jahaan se Suraj ugta hai.
Uske aage andhera hi andhera hai.
Wahan tak hi tum jaa sakte ho.”

⭐ ⏳ Kash Pehle Lautna Zaroori Hai

Sugriva ne sakht chetavani di—

“Ek poora mahina tumhare paas hai.
Udaya Parvat tak dhoondho,
par ek mahine se zyada mat lagana.
Wapas nahi aaye toh dand—mrityu hogi.”

Phir pyaar se bola—

“Maithili ko paakar mere paas badhiya samachar lekar aana.
Mahendra parvat aur uske aas-paas ka poora kshetra dhyaan se dhoondhna.”

Aur is tarah—
Vinata aur hazaaron vanar Poorab ki or udd chale,
Rama ki priya Sita mata ki talaash mein."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.41
    with st.expander("Chapter 4.41 – Sugriva sends another team to search in the South"):
        text1 = """ 
⭐ Chapter 41 – Dakshin Ki Ore Talash

(Hinglish Retelling)

Sugriva ne jab apni pehli badi sena ko poorab ki taraf bhej diya,
to ab usne doosri shaktishaali sena ko dakshin disha mein bhejna shuru kiya.

Is baar sena ka neta Angad tha—Bahut veer, bahut hoshiyaar.

Uske saath chale:

Hanuman, tej, samajhdaar, diler;

Nila, Agni ka putra;

Jambavan, buddhi aur shakti ka khazana;

Suhotra, Sharari, Sharagulma, Gaja, Gavaksha,
Gavaya, Sushena, Vrishabha;

Mainda, Dvivida, Gandhamadana;

Ulkamukha aur Ananga,
aur kai aur mahan vanar-nayak.

Sab taiyaar the — Sita Maa ki talash ke liye."""

        create_image_text_layout("attached_assets/chapter4/4.41.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Sugriva Ka Map-Samjhaana

Sugriva ne unhe dhyaan se kaha:

“Pehle tumhe Vindhya parvat dikhai dega—
hazaaron chotiyon wala, ped-paudhon se bhara hua.”

Woh aage bole:

Narmada ka saaf nadi-jal, jahan bade-bade saanp rehte hain.

Godavari, jiska kaala-naal ghaas se bharpoor kinara.

Krishnaveni, khoobsurat aur shant.

Phir:

Mekhala aur Utkal ki bhoomi,

Dasharna nagri,

Avanti, Vidarbha, Nishtika,

Mahishaka,

Matsya, Kalinga, Kaushika —
sab jagah Sita ji ko dhoondhna.

Aur phir:

Dandakaranya ka gahan jungle, pahaad, nadiyan, aur guhaayein.

⭐ Dakshin Ki Gehraaiyon Mein…

Sugriva ne unhe aage ke raaste bataye:

Andhra, Paundra, Chola, Pandya, Kerala —
har jagah khoj karna.

Phir aata hai:

Ayomukha Parvat – lohe jaise chamakdar pattharon se bhara,
sundar sandalwood ke jungle ke saath.

Wahan se aage:

Kaveri nadi, jahan Apsarayein khelti hain.

Malaya Parvat jahan Rishi Agastya rehte hain.
Unki ijazat se hi tum Tamraparni nadi ko paar kar paoge.

Phir Sugriva ne unhe ek sundar drishya bataya:

“Tamraparni ki beech-beech mein jo chhote-tatte islands hain,
wahan sandalwood ke forests hain…
jaise koi naveli dulhan apne var ki taraf ja rahi ho.”

⭐ Samudra aur Pariyojanayein

Sugriva ne kaha:

“Pandya rajya ke motiyon se sajjey hue sone ke dwar dekhoge.
Phir samudra ke kinare pohonch kar yeh dekhna hoga
ki tum samudra paar kar sakte ho ya nahi.”

Samudra ke beech:

Mahendra Parvat — poora sunehra,
devon aur Rishiyon ka ghar,
jahan Indra har amavas ko aata hai.

Uske paar:

“Ek lambi si 400-mile wali island hai—
jahaan Ravana rehta hai.
Vahin Sita ho sakti hain.
Bahut dhyaan se khojna.”

Samudra mein ek raaz bhi tha:

Angaraka Rakshasi –
jo upar uddne walon ki parchai pakad leti hai!

⭐ Aage Ki Duniya: Jahan Khauf Bhi Hai, Roop Bhi

Sugriva ne aur aage bataya:

Pushpitaka Parvat – sooraj jaise chamakdar.

Uske baad Suryavan – mushkil pahaad.

Phir Vaidyuta Parvat – hamesha hare pedon se bhara,
saalon tak phal deta hua.

Aage:

Kunjara Parvat – jahan Vishvakarma ne
Rishi Agastya ke liye ek sundar,
sunehra, uncha mahal banaya.

Aur phir:

Bhogavati – saapon ki rajdhani,
jahan Vasuki Raja rehta hai.
Bahut khatarnak, par zaroori khoj.

Aur aage:

Rishabha Parvat,

aur ek saatvik sandalwood ka jungle
jahan Rohita Gandharva aur uske paanch tej-saathis
hifazat rakhte hain —
yeh jungle enter nahi karna.

Aur sabse aakhir:

“Wahan Rishiyon ka aashram hai,
phir Pitron ka pranta —
jahan jeevit log kabhi nahi jaate.”

⭐ Mission Ki Shart

Sugriva ne un sab ko siddhe shabdon mein kaha:

“Ek mahine ke andar
jisne bhi ‘Sita mil gayi!’ bol diya,
woh mera sabse pyaara dost hoga.
Uske saare dukh door kar doonga.
Chahe usmein kitni bhi kamiyaan kyon na ho,
woh mera apna ban jayega.”

Aur ant mein kaha:

“Tum sab bahadur ho.
Tumhari shakti apar hai.
Ab jao —
aur apni veerta sabit karo.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.42
    with st.expander("Chapter 4.42 – More monkeys are sent to the West"):
        text1 = """ 
⭐ Chapter 42 – Vanaron Ko Pashchim Ki Ore Bheja Gaya

(Hinglish Retelling)

Dakshin ki sena ko bhejne ke baad,
ab Sugriva ne pashchim disha ke liye ek aur bada mission shuru kiya.

Is baar unhone bulaaya:

Sushena, unka sasur, bahut buddhi aur shakti wale;

Marica aur uske veer putra;

Archismat aur Archirmalayas—
sab hi mahaan vanar-nayak.

Sugriva ne kaha:

“Aap sab milkar 2 lakh vanaron ko le jao.
Sita Mata ko dhoondhna hai—
jahan-jahan zarurat pade.”"""

        create_image_text_layout("attached_assets/chapter4/4.42.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Pashchim Ka Lamba Safar

Sugriva ne samjhana shuru kiya:

“Saurashtra, Bahlikas, Chandrachitra—
sab shetron ko achchhe se dekhna.
Jungle, ped, nadiyan, sab jagah khojna.”

Vanaron ko kaha gaya:

Punnaga pedon wale ghane van,

Bakula aur Uddalaka se bhare jungle,

Ketaka ke jhund,

aur thandi hawaaon wali paschimi nadian.

Sabhi shetron ko dhoondhna tha.

Phir:

“Jahan jahan tapasviyon ke ashram hain,
pahadi jharne hain, kathin ghatiyaan hain—
wahan bhi jao.
Kabhi kabhi raaste registan jaise sukhhe honge.”

Aur jab aur aage jaoge:

“Tumhe samudra dikhega—
jisme bade-bade whales aur crocodiles rehte hain.”

⭐ Samudra ke Kinare Aur Rahasya-Jagahen

Sugriva ne kaha:

Tamala aur coconuts se bhare bade-bade van,

Murachipattana,

Jatapura, Avanti, Angalapa,

aur Alakshita ka van.

Ye sab jagah khojni thi Sita ji ke liye.

Phir:

“Jahan Sindhu nadi samudra se milti hai,
wahan Somagiri Parvat hai—
sau chotiyon wala.”

Wahan rehte:

Sher jaise Sinhas,
jo whales aur elephants ko utha le jaate hain!

Sugriva ne kaha:

“Wahan jaakar har ek choti aur ghaati ko khojna.”

⭐ Samudra Ke Beech Ke Chamatkari Parvat

Sugriva ne bataya:

1. Pariyatra Parvat

Pure sunehre chamak wala,

beeson yojan tak vishal,

jahan Gandharva rehte hain—
bohot shaktishaali, kabhi kabhi shaitani bhi.

“Unke khaas fal mat khana,
par Sita ko dhoondhna zaroor!”

2. Vajra Parvat

Emerald jaise hara,

heere ki tarah chamakdar.

Sau yojan ka pahaad,

jismein gehri-gehri guhaayein.

3. Charavat Parvat

Jahan Vishvakarma ne
Sudarshan Chakra ka roop banaya tha!

Boht sundar gufaayein aur jharne yahan hain.

Sita ko wahan bhi khojna.

⭐ Aage Aur Bhayanak-Sundar Duniya
Varaha Parvat

64 yojan ka sunehra parvat.

Yahan hai Pragjyotisha,
jahaan rakshas Naraka rehta hai.

Sarvasauvarna Parvat

Chaaron taraf sunehre jharne aur ped.

Sher, hathi, jangli suar, sab jor se garajte honge.

Megha Parvat

Jahan Devtaon ne Indra ka rajyabhishek kiya tha.

Uske baad:

60,000 sunehre pahadon ki shreni!

Poore aasman ko roshan karte hue.

Aur beech mein:

Meru Parvat

Sugriva ne kaha:

“Ye sabse mahan parvat hai.
Surya Dev ne isse ashirvaad diya tha
ki yahan ke parvat aur devta
hamesha sunehre chamkenge.”

Wahan Varuna ka ek bada sunehra mahal bhi hai.

⭐ Andheri Seema: Aage Mat Jaana

Meru ke aage:

Ek bada sunehra Tala ped,

Aur phir Astachala Parvat —
jahan Surya ast hota hai.

Usse aage:

“Andhera hi andhera hai.
Wahan koi nahi jaata.
Wahan se lautna mushkil hai.”

Sugriva ne sabko chetavani di.

⭐ Antim Nirdesh

Sugriva ne pyaar aur kathorata dono ke saath kaha:

“Pashchim mein jitna maine bataya hai,
utna hi khojna.
Ek mahine ke andar wapas aa jaana.
Jo der karega… woh mar jayega.”

Aur aakhri baat:

“Sushena tumhare neta honge.
Unki baat sunna.
Woh buddhi, shakti, sab mein sabse aage hain.”

Vanar sab Jhukkar bole:

“Aapka aadesh sarakhon par!”

Aur fir woh sab Varuna Dev ke disha ki taraf
vega se nikal pade."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.43
    with st.expander("Chapter 4.43 – A group is sent to search in the North"):
        text1 = """ 
⭐ Chapter 43 – Vanaron Ko Uttar Disha Ki Ore Bheja Gaya

(Hinglish Retelling)

Sugriva ne jab pashchim ki sena ko bhej diya,
to ab unhone uttar disha ke liye taiyari shuru ki.

Unhone Shatavali, ek bahadur aur buddhimaan vanar, ko bulaya.

Sugriva ne kaha:

“Shatavali, tum 1 lakh vanaron ke saath
Himalaya ki taraf jao.
Har pahad, har ghati, har jungle mein
Sita Mata ko dhoondhna.”"""

        create_image_text_layout("attached_assets/chapter4/4.43.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Dayitva aur Krtagyata

Sugriva ne sab ko yaad dilaya:

“Rama ne humare liye bahut bada upkaar kiya hai.
Agar hum unki sahayata karein,
to hamari zindagi safal ban jayegi.
Jo humein bhala chahte hain,
unhe is kaam mein poora man lagana hoga.”

Vanaron ne Rama ke prati apna vachan pakka kiya
aur mission shuru hua.

⭐ Uttari Deshon Ka Safar

Sugriva ne kaha:

“Mleccha, Pulinda, Shurasena, Bharata, Kuru,
Madra, Kamboja, Yavana—
in sab deshon mein khojna.”

Jahan shehre the, wahan khojna.
Jahan pahad the, wahan khojna.
Har nadi, har jungle mein khojna.

Phir:

Himavat ke gahre van

Lodhra aur Padmaka ke ped

Devadaru ka jungle

Saare gupt raste aur gufaayein

“Ravana aur Sita ko wahan dhoondhna.”

⭐ Himalaya ke Pavitra Sthaan

Shatavali ki sena ko jaana tha:

Soma Ashram — jahan Devta aur Gandharva aate hain

Kala Parvat — bade plateaus aur gehri ghatiyon wala

Sudarshana aur Devasakha Parvat —
jahan har tarah ke pakshi rehte hain

Sugriva ne kaha:

“Har gufa, har chattan, har chhota kone-ko khojna.
Ho sakta hai Sita wahi kahin ho.”

⭐ Vishal Registan Aur Kailash Ki Khoj

Vanaron ko bataya gaya:

400 mile lamba sukha registan,
jahan na ped, na nadi, na jeev.

Uske baad:

⭐ Kailash Parvat

Chand jaisa safed, sundar aur shant.

Wahan:

Kuvera ka sunehra rajmahal

Phoolon se bhare sarovar

Hans, bagule aur apsarayein

Guhyakaon ki bhoomi

“Is poore shetra ko achchhi tarah khojna.”

⭐ Krauncha Aur Manasa Parvat

Phir vanaron ko jaana tha:

Krauncha Parvat

Boht mushkil gufaayein

Bade rishi jo apna roop badal sakte hain

Manasa Shikhar

Jahan Kaamdev ne tapasya ki

Jahan koi devta ya rakshas bhi aasani se nahi ja sakta

Sugriva:

“Phir bhi, jitna ho sake utna khojna.”

⭐ Mainaka, Siddhaon Ki Bhoomi Aur Vaikhanasa Sarovar

Vanaron ko fir jaana tha:

Mainaka Parvat

Jahan daanav Maya ka mahal hai

Jahan ghodon jaise chehre wali स्त्रियाँ rehti hain

Siddhaon ki jagah

Bahut shuddh tapasviyon ka sthaan

Wahan jaake vinamrta se Sita ke baare mein poochhna

Aur:

Vaikhanasa Sarovar

Sunehri kamal

Hans aur sundar panchhi

Kuvera ka hathi Sarvabhauma yahan ghoomta hai

⭐ Uttara Kuru Aur Aage Ka Andhera

Sugriva ne kaha:

“Uttara Kuru tak jaa sakte ho.
Par uske aage mat jaana.
Wahan sada raat hoti hai,
koi raasta nahi, na hi wapas aana sambhav.”

Aur:

“Somagiri Parvat bhi aayega—
usse bas dekhna, chadhna nahi.”

⭐ Antim Sandesh

Sugriva ne pyaar aur majbooti saath kaha:

“Maine jitne sthaan ginaaye hain aur jinhe bhool gaya hoon,
sab jagahon par khojna.
Tum hawa aur agni jaise shaktishaali ho.
Sita ko dhoondkar Rama ko sukh do—
isi mein tum sab ki veerta aur samman hai.”

Phir:

“Jab tum successful ho kar aaoge,
to main tum sab ko samman, sukh aur aadar dunga.
Tumhara dushman khatam hoga
aur tum poori duniya mein izzat paoge.”

Vanar-nayakon ne sir jhukaya.
Purvaas ki hawa chal rahi thi.
Aur veer vanar uttar disha ki taraf nikal pade—
mission poora karne ke liye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.44
    with st.expander("Chapter 4.44 – Rama gives his ring to Hanuman"):
        text1 = """ 
⭐ Chapter 44 – Rama Apna Anguthi Hanuman Ko Dete Hain

(Hinglish Retelling)

Sugriva ko sabse zyada bharosa Hanuman par tha.
Isliye unhone sabse pehle Hanuman ko apna poora yojana batayi.

Sugriva ne Hanuman se kaha:

“Hanuman, tumhare raste mein
dharti ho, asmaan ho, samundar ho
ya dev–danav—
koi tumhe rok nahi sakta!

Tumhara gyaan, tumhari tezi, tumhari urja—
sab tumhe kisi bhi jeev se alag banati hai.
Tum bilkul apne pita, Pawan Dev, ki tarah ho.

Sita Maa ko dhoondh kar lana tumhare hi bas ki baat hai.”

Hanuman chup chaap sunte rahe,
aur Sugriva ki baaton se unmein aur himmat bhar gayi."""

        create_image_text_layout("attached_assets/chapter4/4.44.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Rama ka Vishwas

Rama ne ye sab dekha aur socha:

“Sugriva ko pura vishwas hai Hanuman par…
aur Hanuman ko bhi apni shakti par bharosa hai.
Jis ko uska swami parakh chuka ho,
woh kaam zaroor poora karta hai.”

Rama ke mann mein ek shanti chaa gayi—
jaise unko pehle hi pata chal gaya ho
ki ab Sita mil jayengi.

⭐ Rama ki Anguthi – Sita ke liye Nishani

Phir Rama ne apne haath se ek anguthi nikali.
Uspar Rama ka naam khoda hua tha.

Rama ne Hanuman ke haath mein woh anguthi rakhte hue kaha:

“Hanuman, yeh anguthi Sita Maa ko sabit karegi
ki tum mere dhoota ho.

Tumhari buddhi, himmat aur anubhav—
sab tumhari safalta ka sanket de rahe hain.”

Hanuman ne anguthi ko apne maathe se lagakar pranam kiya.
Unki aankhon mein himmat chamak uthi.

⭐ Yatra ki Shuruaat

Phir Hanuman,
taaron se ghire chand jaise chamak rahe the—
apni poori vaanar sena ke saath nikal pade.

Rama ne unhe ruk kar ek baar aur bulaya:

“Hanuman, tum sher ki shakti rakhte ho.

Main poori tarah tum par nirbhar hoon.

Apni poori taakat, buddhi aur saahas se
Sita Maa ko wapas lekar aao.”

Hanuman ne apne dono haath jod kar pranam kiya
aur shabdhin nikal pade—
ek aise kaam ke liye
jo unke naam ko amar kar dega."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.45
    with st.expander("Chapter 4.45 – The monkey search teams leave"):
        text1 = """ 
⭐ Chapter 45 – Vaanaron ka Maha-Prasthaan

(Hinglish Retelling)

Sugriva ne ek bada sa sabha bulaayi.
Jitne bhi vanar-senapati the—sabke sab ek saath aa gaye.

Sugriva ne unhe Rama ke kaam ki yaad dilaai aur bola:

“O Vanar Veeron,
jo disha maine batayi hai,
usi taraf jao
aur Sita Maa ko dhoondh kar lao!”

Jaise hi aadesh mila,
poori vanar sena zameen par tiddi jaisi fail gayi—
har taraf hil-jul, shor, gajab utsaah!"""

        create_image_text_layout("attached_assets/chapter4/4.45.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Chaar Dishaon Mein Chaar Maha-Senayen

🟦 Uttar – Shatavali lightning ki speed se nikal pada,
jahaan barfili pahaadiyon ka raja, Himalaya, khada hai.

🟧 Poorab – Vinata apne balwaan vanaron ke saath aage badha.

🟥 Dakshin – Tara, Angada aur Pawan-putra Hanuman
Agastya Muni ki bhoomi ki taraf nikal pade.

🟩 Pashchim – Sushena, sher jaisa shaktishaali vanar,
Varuna Dev ke rakshit shetra ki ore chal diya.

Sugriva ne charon taraf apni sena bhej kar
gehri saans li—
ab yeh yatra sach* mein shuru ho chuki thi.

⭐ Vanaron ka Josh!

Jab vanar nikal pade,
toh dharti unke kolahal se goonj uthi—
cheeche, cheekh, josh bhare naray,
jaise prakriti bhi unki himmat badha rahi ho.

Sab bol rahe the:

“Hum Sita Maa ko wapas layenge!”
“Hum Ravana ko maar girayenge!”

Kuch apni shakti ka danka baja rahe the:

🐒 “Main akela Ravana ko hara kar Sita Maa ko launga!”
🐒 “Main jahan bhi ho—paataal ho ya samundar—usse dhoondh nikalunga!”
🐒 “Main ped ukhaad dunga!”
🐒 “Main pahaad tod dunga!”
🐒 “Main samundar ko churn kar daalunga!”

Aur fir shaurya ka mukhya daava:

🐒 “Main ek hi chhalang mein 4 kos paar kar sakta hoon!”
🐒 “Main 100 kos tak kud sakta hoon!”
🐒 “Main to us se bhi zyada ud sakta hoon!
Na zameen mujhe rok sakti hai, na asmaan, na samundar!”

Poora jungle unki garjanon se goonj raha tha.
Har vanar apne aap ko sabse shaktishaali samajh raha tha—
aur sabka ek hi sankalp tha:

“Sita Maa ko khoj kar lana hai!”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.46
    with st.expander("Chapter 4.46 – Sugriva tells about his travels around the world"):
        text1 = """ 
⭐ Chapter 46 – Sugriva tells Rama about his Journey around the World

(Hinglish Story Rewrite)

Jab saare vanar-sena ke nayak apne-apne dishaon mein nikal gaye,
Rama ne pyaar se Sugriva se poochha:

“Sugriva, tumhe dharti ke itne saare kona-kaunsa kaise pata hai? Tum ne sab kuch kaise dekha?”

Sugriva ne Vinamrata se pranam kiya aur bola:"""

        create_image_text_layout("attached_assets/chapter4/4.46.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Bali, Dundubhi aur Ek Darawani Gufa

“Prabhu, ek baar Bali ek maha-atikrami asur Dundubhi ka peecha kar raha tha.
Dundubhi ne mahisa (bhains) ka roop le liya aur Malaya parvat ke paas ek gufa me ghus gaya.

Bali uske peeche gufa ke andar chala gaya.

Main gufa ke darwaze par rukkar pratiksha karta raha…
Ek din… do din… ek mahina… ek saal!

Par Bali wapas na aaya.

Phir achanak gufa se jhag waala khoon bahar behta dikha.
Main ghabra gaya!
Maine socha, ‘Bali toh ab nahi raha…’”

Dukhi Sugriva ne gufa ka muh pahad jitne bade pathar se band kar diya,
sochte hue —
“Ab Dundubhi bhi yahin mar jaayega.”

Phir woh dil toot kar Kishkindha laut gaya.

⭐ Prabhutva, Phir Dar, Phir Bhaagna

“Kishkindha jaakar maine rajya sambhala,
Tara aur Ruma mere saath the,
sab kushal chalta raha…

Tabhi ek din, Bali wapas aa gaya—
jeevit aur gussay se dehla dene wala!

Main turant uske charon taraf se bachkar nikalne laga,
par Bali ne mujhe maar dene ka sankalp kar liya tha.

Main bhaagta gaya, vah peechhe aata gaya.”

⭐ Dharti ka Pradakshina – Poora Vishva ki Yatra

Sugriva aage bola:

“Bali se bachne ke liye main itna dauda,
itna dauda…
ki poori duniya dekh daali!

Dharti mujhe lag rahi thi
jaise aag ka gola ghoom raha ho.”

⭐ Purv (East) ki Yatra

“Main purv ki disha gaya—
wahan sundar pahaad, gehri gufaayein,
jheel, nadiyaan aur Udaya parvat jiska sona chamakta hai…

Aur maine dekha Safed Samudra,
jahan apsaraayein rehti hain.”

⭐ Dakshin (South) ki Yatra

“Phir main dakshin ki taraf bhaaga—
Vindhya vanon se guzra
jahaan chandan ke pedon ki khushboo hamesha bashti hai.”

⭐ Pashchim (West) ki Yatra

“Bali phir bhi mere peeche tha—
main paschim ki taraf mud gaya.”

⭐ Uttar (North) ki Yatra

“Aage chalkar main Astachala parvat pahunch gaya.
Phir uttar ki taraf bhaaga,
Himavat, Meru aur Uttar Samudra tak pahunch gaya.”

⭐ Rishyamuka – Ek Surakshit Sthaan

“Ab main poori duniya ghoom chuka tha…
par Bali se bachne ka ek lauta sthan mila—

Rishyamuka Parvat.

Hanuman ne mujhe bataya:

‘Rajaa, yahin rishi Matanga ka aashram hai.
Bali ko ek shraap mila hai—
agar woh yahan aaya, uska sir sau tukdon mein phoot jaayega.’

Isliye Bali kabhi hamaare paas nahi aaya.”

⭐ Ant mein Sugriva ne kaha—

“Is tarah, he Raghava,
poori prithvi par bhaagte-bhaagte
maine har disha ko apni aankhon se dekha
aur aakhirkar yahin sharan lee.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.47
    with st.expander("Chapter 4.47 – The monkeys return from their search"):
        text1 = """ 
⭐ Chapter 47 – Vanaron ka Wapasi Yatra

(Hinglish Story Rewrite)

Vaidehi ko dhundhne ke liye, Sugriva ke saare vanar-nayak
tej gati se apni–apni dishaon me nikal pade.

Woh jheelon, nadiyon, gaon, shehron,
aur baarish se ajeeb bane jungleon tak pahunch gaye—
har woh jagah jahaan Sita mili ho sakti thi.

Din bhar woh vanar simh-hardayi se khoj karte,
aur raat ko thak kar pedon ke neeche su jaate,
jahaan hamesha har mausam ke phal lage rehte the."""

        create_image_text_layout("attached_assets/chapter4/4.47.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Ek Mahine Ki Khoj… Par Koi Sita Nahi

Ek mahine ki seema Sugriva ne rakhi thi.
Din pehla jise woh apne ravana-se samay maante the—
lagataar dhundte rahe… par kuch na mila.

Mahina poora hotey hi,
thake-haare vanaron ki toliyan
Prasravana parvat ki ore
wapas lautne lagi.

⭐ Purv se Vinata Ka Wapasi

Sabse pehle shaktishaali Vinata apni sena ke saath aaya.

Usne kaha—

“Humne poora purv khoj dala…
par Sita ka koi pata nahi chala.”

⭐ Uttari Disha se Shatabali

Phir maha-vanar Shatabali
puri uttari disha ko chhanne ke baad
hath jode khada hua—

“Prabhu, humne pahaad, ghatiyan,
barfili bhoomi—sab dekh li…
par Janaki ji ka koi nishan nahi.”

⭐ Pashchim se Sushena

Teesre aaye Sushena,
lion-like warrior and Tara ke pita.

Unhone bhi pair padte hi pranam kiya
aur bola:

“He Sugriva, he Raghava,
humne saare pashchimi parvat,
gehre van, ghaatiyan,
samudra-tat tak ki bhoomiyan
sab-sab baar-baar talashi hain.

Bade-bade janwar mile,
kuch humne maara,
kuch hame talaash ke liye dar dar bhatakna pada…
par Sita mil nahi paayi.”

⭐ Sabki Nazar Ek Hi Vanar Par

Phir Sushena ne muskurate hue,
par asha bhari awaaz me kaha:

“Prabhu…
Hanuman milenge.
Wo hi Vaidehi ka pata lagayega.
Pavana-putra maha-balvaan hai.
Aur nishchit roop se woh wahin gaya hai
jahan Sita ko le jaya gaya tha.”

Rama ne ye shabd sun kar
andar hi andar santosh ka saans li—
kyonki unke hriday me bhi
Hanuman par sabse adhik vishwas tha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.48
    with st.expander("Chapter 4.48 – Angada kills an Asura"):
        text1 = """ 
⭐ Chapter 48 – Angada ne Asur ko Maara

(Hinglish Story Rewrite)

Hanuman, Tara aur yuvaraj Angada
tez hawa ki tarah
apni dakšin disha ki yatra par nikal pade,
waisi hi jaise Sugriva ne unhe aadesh diya tha.

Unke saath vanaron ke pramukh senapati bhi the,
sabhi ek man se Sita ki talaash mein.

Un sab ne Vindhya parvat-mala ke janglon,
gufāon, nadiyon, jheelon,
aur gahri ghaatiyon ko chhan maara…
par Janaki ka koi nishaan nahi."""

        create_image_text_layout("attached_assets/chapter4/4.48.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Sunsaan, Kathor Bhoomi

Janglon ke beech woh sirf
jadon, kand-mool aur kuch berries khakar
apna jeevan chalate rahe.

Fir unhe ek aisi bhoomi mili
jahan na pedh the, na phool, na patte,
na hi janwar ki koi aahat…

Na hiran, na gajraj, na shyen pakshi—
sab kuch sookh-chuka,
jaise prakriti par kisi ne abhishaap de diya ho.

Yeh wo hi bhoomi thi
jise mahān tapasvi Rishi Kandu
apne putra ki mrityu se shok-grast ho kar
shraapit kar chuke the.

Unki tapasya ki agni se
yeh pura jangl bejaan ho gaya tha.

Vanaron ne is bhayanak sthal ko bhi
koni-koni chhan dala…
par Sita ya Ravana ka koi pata nahi.

⭐ Ek Daravna Asur saamne!

Fir vanar ek aise van mein ghuse
jo kaanton aur baelon se bhara hua tha—
aur tab saamne aya ek bhayankar Asur!

Uchchai khada hua,
jaise koi jeevit pahaad,
akhand roop se bhayanak,
devtaon tak se na darne wala.

Usne garaj kar kaha:

“Tum sab to nishchay hi mar gaye!”

Aur apni muṭṭhiyan kas kar
vanaron par jhapta.

Saare vanar ek saath ho gaye—
par sabse aage badhe Angada,
Bali putra, veerta ka roop.

⭐ Angada ka Ek Pralay-Jaisa Prahar!

Angada ne socha ki shayad
yeh Ravana hi ho…

To bina ek pal gavaaye
apni khuli hui haath ki talwar jaise talhī
us Asur ki chhati par maari—

Ek hi prahar mein
Asur jhaad ki tarah jhulta hua gira
aur lahu ugalte-ugalte
zamin par nishchesth ho gaya.

Vanaron ne vijay ke nara lagaye!
Angada ki shakti dekh kar sab romanchit ho uthe.

⭐ Khoj jaari… par Dil Bhaari

Us Asur ki guha ko vanaron ne
chhor-chhor kar talashi li.

Jab kuch na mila,
woh ek aur andheri guha mein ghuse—
jahan unki thakan
jaise haddi tak utar gayi ho.

Bahut der khojne ke baad
jab wahan bhi Sita ka koi pata na mila,
toh sabhi vanar veer
thak kar, udaas ho kar,
ek akela sa pedh tha,
uske neeche jaakar
shaant ho kar baith gaye…

Unke hriday bhar aa rahe the—
“Kahin hum Maithili ko kabhi dhoond hi na paaye?”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.49
    with st.expander("Chapter 4.49 – The monkeys searching in the South do not find Sita"):
        text1 = """ 
⭐ Chapter 49 – Vanaron ki Vyarth Khoj Dakshin Disha Mein

(Hinglish Story Rewrite)

Angada — prajnāvan, buddhimān aur veerta ka roop —
apni thaki-hāri vanar sena ke beech khade hue.

Khud bhi thak chuke the, par unki awaaz mein
ab bhi utsāh ki bijli chamak rahi thi."""

        create_image_text_layout("attached_assets/chapter4/4.49.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Angada ka Utsaah Badhane Wala Sandesh

Angada boli:

“Humne har jangal, pahad, nadi, gufa, ghaati aur
van ke kathin se kathin hisson mein khoj ki…
par na Janaki mili, na Ravana ka koi nishaan.

Sugriva ne jo ek mahina diya tha—
uska bada hissa beet chuka hai.

Ab thakan, neend, udaasi—
sabko dil se nikaal do!

Aao, aaj hi aaj, phir se sab jagah khoj daalein!

Yahi samay hai apna shaurya dikhane ka.
Safalta hamesha milti hai
lagan, buddhi aur hausle se.

Aur tum jaante ho—
Sugriva ka prakop bahut bhayanak hota hai…
aur Rama ka dukh humse dekha nahi jaata.

Main tumhare hi hit ki baat kar raha hoon.
Agar tum sahmat ho, to chalo,
varna koi behtar sujhaav ho to batao.”*

Angada ke shabdon mein
sachchai aur chinta dono thi.

⭐ Gandhamadana ki Sahmati

Sabhi vanar thake hue the—
kuchh to pyaas se behaal…

Par tahzeeb se, dridh awaaz mein
Gandhamadana bole:

“Angada bilkul sahi keh raha hai!
Aao, hum phir se pahadon, guhon,
jharnon, pathron aur junglon ko
Sugriva ke aadesh ke mutabik chhan maaren!”

Unke shabdon se
vanaron mein nayi jaan aa gayi.

⭐ Phir Shuru Hui Khoj Dakshin Ki

Saare vanar ek saath
utsāh aur veerta se bhar kar
Vindhya ki ghaatiyon aur janglon mein daud pade.

Unhone pahadon ko chadha,
jo sharad ritu ke baadal ki tarah
chandi si chamak rahe the.

Inke shikhar, ghaatiyan,
Saptaparna ke van, Lodhra ke janglat—
koi jagah chhodi nahi…

Par phir bhi Sita ka koi pata nahi.

Pahadon ke choti tak chadhkar
vanar veeron ke pair laraz rahe the—
thakan hadh se zyada ho chuki thi.

Neeche utarte waqt
sab ek pedh ke neeche thodi der
thahar gaye,
jahaan thandi hawa se
unke shareer ko aaraam mila.

Jab thodi taqat laut aayi,
tab Angada, Hanuman aur anya pramukh vanar
phir se uthkar bole:

“Chalo! Dakshin ki khoj phir se shuru karte hain!”

Aur is prakar
Sita ki talaash mein,
wo dusri baar Vindhya parvat-mala ki or
naye hausle ke saath badhe."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.50
    with st.expander("Chapter 4.50 – Hanuman and friends enter the dark Rikshabilā cave"):
        text1 = """ 
⭐ Chapter 50 – Hanuman aur Vanaron ka Rikshabila Gufā Mein Pravesh

(Hinglish Story Rewrite)

Hanuman — Pavanputra, parvat-samaan, dridh-sankalp —
Tara aur Angada ke saath phir ek baar
Vindhya parvat ke gehre janglon aur
darārun ghaatiyon ki khoj mein nikal pade.

Un vanaron ne un guhon ko bhi chhān daala
jahan sher aur bāgh ki dahāḍ ghoonjti thi,
aur un teevra pravāhon ko bhi jahan
kadam rakhna mushkil ho jaata tha.

Khojte-Khojte ve dakshin-pashchim ki unchaiyon tak aa pahunche,
jahaan kuch der ke arāam ne unhe samay ka ehsaas hi na hone diya."""

        create_image_text_layout("attached_assets/chapter4/4.50.jpg", text1, layout="side", image_position="left")

        text2 = """ 
⭐ Kabhi-Na-Khattam Hone Wale Jungle

Vindhya ka woh hissa—
ghane van, gehri ghaatiyan,
aur andheri guhayen—
jaise antheen paheli ho.

Par Hanuman ne, apni tej buddhí aur
anant urja se, sab kuchh khoj daala.

Thodi-thodi door par the:
Gaja, Gavaksha, Gavaya, Sharabha, Gandhamadana,
Mainda, Dvivida, Jambavan, Angada, Tara,
aur swayam Hanuman.

Sab ek hi lakshya lekar—
Sita ki talaash mein—dakshin ki aur barhte gaye.

⭐ Rahasyamay Gufā ka Darshan

Tabhi unhone dekha—
ped-paudhon aur bel-latas se ghiri
ek vishal, bhayanak, rahasyamay gufa: Rikshabila.

Uska dwar kisi danav ne jaise raksha ki ho,
par andar se aa rahe the:
bagule, hans, jal-pakshi—
sabke pankhon se tapakta paani,
aur un par kamal ke parāg ki chamak.

Pyaas aur bhook se pareśān vanaron ke liye
ye drishya ek asha ki kiran bana.

Hanuman bole:

“Dekho! Yahan se jo pakshi nikal rahe hain,
zaroor andar paani hoga.

Hume itna dhoondhte ek mahina ho gaya—
thak gaye hain hum sab.

Aao, iss gufa mein chalte hain.
Yahan jeevan ke chinhn nazar aa rahe hain.”

Vanar khushi se bhar uthe.
Sab ne ek saath gufa ka dwar paar kiya,
jahan na suraj ka prakash tha, na chand ki roshni.

⭐ Andhere ka Samandar

Andhera itna gehra
ki ret ka kan, hawa ki resham—
sab bas ek saaya-sa lag raha tha.

Gufa ke andar sher ki dahad,
hiranon ki halchal,
pakshiyon ki awaaz goonj rahi thi.
Aur un veer vanaron ka
dil pehli baar halka sa kaamp utha.

Par unki aankhen—
vanar-jaati ki var-datta tej drishti—
andhere ko chhedti chali gayi.

Chaar kos andar,
anakher, unhe laga jaise sharir saara
thakawat se toot jaye.
Paani ki talaash mein
wo neeche-hi-neeche utarte gaye.

Tab hi—
ek prakash ka bindu
andhere mein chamka.

⭐ Ek Anokhi, Adbhut Jagah

Wahan pahunch kar vanar stambhit reh gaye.

Ped—jaise sone ke bane,
phool—jaise aag ke angaare,
tan—jaise emerald,
chhaal—jaise jalti roshni.

Kamal ke talāon mein
sona jaise machhliyan,
vishal neele kamal,
shant jal,
aur har taraf prakash ki laali.

Mahal—
sone aur chandi ke,
khidkiyon par motiyon ki jhallar.
Farsh—heere-moti se jada hua.
Aalas ki jagah nahi—
ye to Indra ka swarg lagta tha!

Khan-peen, phal-mool,
madhur peene yogya ras,
bahumulya kapde,
sone-chandi ke bartan,
aur sugandhit lakdi ke dher—
sab yahan bhare pade the.

⭐ Ek Rahasyamay Vrudhha Tapasvini

Par sabse adbhut drishya to tab dikha—
ek vrudhha tapasvini,
mriga-charma aur valkala pehne,
bahut hi prakashmay aur gambhir.

Vanar thithak gaye.
Hanuman aage badhe,
sir jhukaakar bole:

“Hey Mata, aap kaun hain?
Yeh gufa kiski hai?

Yeh divya van, yeh dhan-daulat,
yeh prabha—
sabka swami kaun hai?

Kripya batayiye,
hum pathik hain,
Sita ki talaash mein bhatak rahe hain.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.51
    with st.expander("Chapter 4.51 – They hear the story of an old ascetic"):
        text1 = """ 
Chapter 51: 
🌟 Gufa Mein Ek Rahasyamayi Tapasvini

Hanuman aur saare vanar bahut thake hue the.
Bhookh, pyaas aur andhera unhe bilkul thaka chuka tha.

Jab woh gufa ke andar ghus gaye,
to unki aankhen khulī ki khulī reh gayin—

sunehre ped

hira-moti se sajhe mahal

sona-chandi ke bartan

sunehri machhliyaan aur kamal

khushboo se bhare phool

Sab kuch itna chamak raha tha jaise suraj ugne wala ho."""

        create_image_text_layout("attached_assets/chapter4/4.51.jpg", text1, layout="side", image_position="left")

        text2 = """ 
Hanuman hairaan hokar bole:

“Mata, yeh sab kis ka hai?
Yeh sunehre ped, yeh mithai jaisi roots aur fruits…
Yeh sona-chandi ke mahal…
Yeh sab kiska kamaal hai?
Aapka, ya kisi aur ka?”

🌺 Tapasvini Swayamprabha Ka Jawaab

Woh tapasvini—bark ke kapde aur mriga-charm pehne—
pyaar se muskurayi aur boli:

“Hey Vanar-shreshtha, suno.”

Unhone bataya:

Maya naam ka ek maha-jaadugar yeh sab banaya tha.

Maya pehle Daityon ka maha-architect tha.

Usne hazaar saal tapasya ki, aur Brahma ji se vardaan mila.

Is vardaan se usne yeh poora sone ka van aur mahal bana dala.

Phir ek din Maya ko apsara Hema se prem ho gaya.
Lekin Indra ko yeh pasand nahi aaya,
aur vajra se Maya ko maar diya.

Brahma ji ne phir yeh poora sone ka van,
aur sundar mahal,
Hema ko gift kar diya.

Tapasvini ne kaha:

“Mera naam Swayamprabha hai.
Main Merusavarni ki beti hoon.
Hema meri priya sakhī hai.
Uski kripa se main is sone ke van ki raksha karti hoon.”

🐒 Vanaron Se Sawal

Phir Swayamprabha pyaar se puchti hai:

“Ab tum batao, kis kaam se yahan aaye ho?
Itne kathin jangalon me kyun bhatak rahe ho?
Pehle kuch phal kha lo, paani pee lo…
phir mujhe sab sach-sach batao.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.52
    with st.expander("Chapter 4.52 – Swayamprabha frees the monkeys from the cave"):
        text1 = """ 
Chapter 52: 🌟 Swayamprabha Ne Vanaron Ki Madad Ki

Vanar ab thode shaant ho chuke the.
Tab tapasvini Swayamprabha ne pyaar se poocha:

“O Vanaro, agar tum log thakawat se thode theek ho gaye ho,
to mujhe batao tum yahan kaise aaye?”

Hanuman ne haath jodkar sab sach-sach bataya:

🐒 Hanuman Ka Sachha Vrittant

“Hum Raja Rama ke sevak hain.
Rama ki patni Sita ko Ravana chheen kar le gaya.
Unki talaash hum sabka farz hai.

Sugriva ne humein south direction mein bheja.
Hum ne pahaadon, samudron, jangalon—sab jagah dhoondha.
Phir bhookh-pyaas se thak kar hum ped ke neeche baith gaye.
Umeed tootne lagi thi."""

        create_image_text_layout("attached_assets/chapter4/4.52.jpg", text1, layout="side", image_position="left")

        text2 = """ 
Tab humein ek badi si gufa dikhi.
Andhera tha, lekin andhar se
paani se bhige huye pankh waale pakshi bahar aa rahe the.
Humne socha—shayad andar paani ya phal mil jaaye.
Isliye hum sab haath pakad kar gufa mein chale gaye.

Andar andhera aur bhayanak tha,
lekin phir humein woh sunehra van dekhne ko mila
aur aapne humein phal, jhad, sab kuch diya.
Aapne humein bacha liya.
Ab bataiye, hum aapke liye kya kar sakte hain?”**

🌺 Swayamprabha Ka Nirmal Uttar

Swayamprabha muskurai aur boli:

“Mujhe tum se kuch nahi chahiye,
main to bas apna kartavya nibha rahi hoon.”

😟 Vanaron Ki Chinta

Par Hanuman ne vinamrta se fir kaha:

“Mata, ek badi mushkil hai.
Hum bahut din yahan gufa mein ruk gaye.
Sugriva ne ek niyat time diya tha.
Agar hum der kar gaye… to humein dand milega.
Kripya humein bahar nikaal dijiye.”

✨ Tapasya Ki Shakti

Swayamprabha boli:

“Beta, is gufa se zinda bahar nikalna mushkil hota hai.
Lekin meri tapasya ki shakti se main tum sab ko bahar le jaa sakti hoon.
Ek baat yaad rakhna—
Jab tak main kuch na kahoon, apni aankhen mat kholna.”

Sab vanaron ne turant apni aankhen
haathon se dhak li.

Aur ek pal mein—
jaise jadoo ho gaya ho—
wo saare vanar gufa ke bahar aa gaye!

🌄 Bahaar Ka Drishya

Swayamprabha boli:

“Dekho, yeh Vindhya Mountain hai.
Wahan Prasravana parvat dikhta hai.
Aur samne bada sa sagar bhi hai.
Tumhari yatra mangalmay ho!
Ab main apne ghar laut rahi hoon.”

Aur itna keh kar
Swayamprabha wapas andheri gufa mein sama gayi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.53
    with st.expander("Chapter 4.53 – Angada and his friends discuss what to do next"):
        text1 = """ 
Chapter 53: 🌊 Samundar Ke Kinare Vanaron Ki Chinta

Vanar log aage badhe aur saamne dekha—
bahut bada, daraavna samundar, jismein bade-bade leher uth rahe the.
Yeh Varuna ka samundar tha.

Gufa mein ek poora mahina beet chuka tha.
Sugriva ne jo time diya tha… woh khatam ho gaya tha.
Sab vanar Vindhya parvat ke neeche baith kar pareshaan ho gaye.

Phoolon se bhare ped, belon se latpat jhadiyan—
sab kuch sundar tha,
par vanaron ke mann mein sirf dar tha."""

        create_image_text_layout("attached_assets/chapter4/4.53.jpg", text1, layout="side", image_position="left")

        text2 = """ 
🐒 Angada Ka Dukh

Angada, jo sher jaise kandhe aur lambe baahu wala yuva rajkumar tha,
buzurg vanaron ko samman dekar bola:

“Hum sab Sugriva ke hukum par nikle the.
Par gufa mein waqt zyada lag gaya…
Mahina beet gaya.
Humne Sita ko nahi dhoonda.
Ab kya hoga?”

Woh udaas hokar bola:

“Sugriva hamari galti kabhi maaf nahi karega.
Raja ka aadesh todna—yeh badi saza deta hai.
Hum yahan se khaali haath laut gaye, to hum zinda nahi bachenge.
Isse achha yahi samundar ke paas upwaas karke mar jaana behtar hai.”

Angada ne apna kasht bhi bataya:

“Mujhe Sugriva nahi, Rama ne rajkumar banaya tha.
Sugriva mujhe pasand nahi karta.
Galti yahan hui hai… aur wo mauka pakad kar mujhe maar dalega.”

Yeh sunkar saare vanar rote hue bole:

“Haan! Sugriva kathor hai…
Aur Rama Sita ji ke bina dukhi hain.
Hum apna kaam nahi kar paaye—
wo humein marwa denge.
Isse behtar yahi hai ki hum yahin mar jaayein.”

🦁 Tara Ka Samajhdaar Salah

Tab General Tara ne shant swar mein kaha:

“Darne se kya hoga?
Chalo hum sab wapas us gufa mein jaate hain.
Wahan phool, paani, phal sab kuch hai.
Aur koi humein wahan dhoond bhi nahi sakta—
na Indra, na Sugriva, na Rama.”

Angada ko bhi yeh baat sahi lagi.

⭐ Vanaron Ka Nirnay

Sab vanar zor se bole:

“Haan!
Hum wahi karte hain jo humein zinda rakh sake.
Chalo wapas gufa mein chalte hain!”

Aur is tarah,
darte-par-girte,
vanaron ne tay kiya ki
pehle apni jaan bachana zaroori hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.54
    with st.expander("Chapter 4.54 – Hanuman tries to stop Angada’s hopeless plans"):
        text1 = """ 
Chapter 54: 🐒 Hanuman Aur Angada Ki Baat

Tara ne jab gufa mein chhupne ka idea diya,
Hanuman ne dekha ki Angada ka mann hil chuka hai.
Woh soch raha tha ki shayad Angada ab apne aap ko raja jaisa samajh raha hai.

Hanuman jaanta tha ki Angada
— bahut buddhimaan,
— bahadur,
— aur apne pita Bali jaisa shaktishaali tha.
Isliye agar uska mann bhatak gaya,
to poori vanar sena mushkil mein pad sakti thi."""

        create_image_text_layout("attached_assets/chapter4/4.54.jpg", text1, layout="side", image_position="left")

        text2 = """ 
Hanuman ne socha:
"Angada ko right path par lana hoga."
Aur isliye usne ek chal sochi—
pehle vanaron mein halka sa doubt paida kare,
phir Angada ko sachchi aur kadvi baat bataye.

⚠️ Hanuman Ki Kadvi Par Sachchi Salah

Hanuman Angada ke paas gaya aur bola:

“Angada, tum bahut shaktishaali ho,
shayad Bali se bhi zyada.
Par vanar log… woh hamesha bechain hote hain.
Apne ghar, apni patni, apne bachche—
unhe sab yaad aayega.
Woh kabhi tumhari nai sarkar nahi manenge.”

Phir Hanuman ne seedha sach keh diya:

“Jambavan, Nila, Suhotra… aur main—
hum tumhari taraf nahi aa sakte.
Aur tum yeh jaante ho—
takatwar hamesha kamzor ko hara deta hai.
Isliye strong logon se dushmani mat karo.”

Hanuman ne gufa ka bhi sach bataya:

“Tum jis gufa ko surakshit samajh rahe ho,
Lakshman apne teer se use patte ki tarah ched denge.
Unke teer bijli ki tarah tez hain—
parvat tak tod sakte hain.”

🐾 “Vanar Tumhe Chhod Denge”

Hanuman ne Angada ko samjhaya:

“Vanar apne parivaar ko yaad karenge,
aur tumhara saath chhod denge.
Phir tum akela pad jaoge.
Aur jab aadmi ya vanar akela hota hai,
to chhoti si awaaz bhi darr paida karti hai.”

Hanuman ne ek aur kadvi baat kahi:

“Lakshman tumhein chhodenge nahi.
Chahe tum gufa mein chup jao,
unke teer tumhein dhoondh hi lenge.”

🌿 “Sahi Raasta Yeh Hai…”

Phir Hanuman ne narm swar mein kaha:

“Agar tum vinamr hokar humare saath Sugriva ke paas chalo,
to woh tumhein maaf kar dega.
Woh ek achha raja hai—
vachan ka pakka,
dil ka saaf.
Tumhare maata se pyar karta hai,
aur tum uske bhatije ho.
Woh kabhi tumhein nahi marega.
Tum wapas rajkumar ban sakte ho.”

Hanuman ne haath jodkar kaha:

“Chalo Angada…
humein Sita ji ko dhoondhna hai.
Galti ho gayi, par rasta abhi bhi khula hai.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.55
    with st.expander("Chapter 4.55 – The monkeys think of giving up and starving"):
        text1 = """ 
Chapter 55: 🌊 Angada Ka Dukh Aur Vanaron Ka Faisla

Hanuman ki baat seedhi, samajhdaar aur pyaar se bhari thi.
Par Angada ka mann ab bhi toot chuka tha.
Usne dard bhari awaaz mein jawab diya:

💔 “Main Sugriva Par Bharosa Nahi Kar Sakta”

Angada bola:

“Sugriva na to stable hai, na daya rakhta hai.
Usne apne bhai ki patni ke saath rehna chun liya…
apne bhai ko gufa mein chhod diya…
aur Rama ji ka upkaar bhi bhool gaya.”"""

        create_image_text_layout("attached_assets/chapter4/4.55.jpg", text1, layout="side", image_position="left")

        text2 = """ 
Angada ka dard aur bada tha:

“Agar main wapas gaya, to Sugriva mujhe kabhi zinda nahi chhodega.
Woh mujhe Bali ka beta samajhkar dushman maanta hai.
Bandhva dega… saza dega…
Iss se achha hai ki main yahin mar jaoon.”

Angada ne zor se saans li aur bola:

“Main gufa ya rajya nahi jaunga.
Yahin samundar ke paas upwaas karke apni jaan de dunga.”

Phir usne apni aankhen nam karke kaha:

“Hanuman… mere pranam Sugriva aur Rama ji ko keh dena.
Aur meri maa Tara ko bata dena…
woh bahut dukh mein mar jayegi.”

🐒 Vanaron Ka Dil Toot Gaya

Angada kusha grass par baith gaya—
thaka hua, ro raha tha, bilkul akela.
Usse dekh kar saare vanar bhi ro pade.

Unhone socha:

“Agar Angada marne ja raha hai,
to hum bhi usse akela nahi chhod sakte.”

Sab vanar Angada ke paas baith gaye.
Samundar kinaare, darbha ghaas par,
poora toli ek saath bol uthi:

“Hum bhi yahin upwaas karke mar jayenge.”

Unki aankhon se aansu beh rahe the.
Woh Raghav ki kahani yaad karte ja rahe the:

— Rama ka vanvaas
— Raja Dashrath ki mrityu
— Janasthan ka yudh
— Jatayu ki shahadat
— Sita ji ka apaharan
— Bali ka vinaash
— Aur ab Raghav ka gussa…

Yeh sab soch kar vanaron ka dil dar se bhar gaya.
Poora pahaadi ilaqa unke rote hue swaron se goonj utha—
jaise aasman mein bijli garaj rahi ho."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.56
    with st.expander("Chapter 4.56 – Sampati suddenly appears"):
        text1 = """ 
Monkeys ek bade pahad ke plateau par baithe the.
Woh sab thak gaye the.
Sita ko dhoondhte-dhoondhte unki ummeed toot rahi thi.
Sab ne socha:
“Agar hum Sita ko nahi dhoond paaye…
to hum yahin bina khaaye-piye praan tyag kar denge.”

Tabhi achanak, ek bada sa vulture wahan aaya.
Woh tha Sampati, Jatayu ka bhai.
Bahut purana, bahut samajhdaar, aur shaktishaali pakshi.

Woh apni gufa se bahar nikla aur monkeys ko dekha.
Usne khush hoke kaha:"""

        create_image_text_layout("attached_assets/chapter4/4.56.jpg", text1, layout="side", image_position="left")

        text2 = """ 
“Ah, lagta hai mere purane karmon ka phal mil gaya.
Aaj mujhe tyaar khaana mil raha hai!
Jab yeh bandar ek-ek karke mar jayenge,
main sabko kha jaaunga.”

Uski baat sunkar sab monkeys ghabra gaye.
Angad ne halki si awaaz mein Hanuman se kaha:

“Dekho, lagta hai hamare jeevan ka anth aa gaya…
Sita ke liye humne sab kuch kiya,
phir bhi unka pata nahi mila.
Aur ab mrityu — Vivasvat ke vanshaj —
jaise yahan hamara intezaar kar rahi ho.

Hanuman, tumhe yaad hai Jatayu?
Woh bhi Sita ke liye ladte-ladte shaheed ho gaya.
Kitne praani, janwar tak,
Rama ke liye apni jaan dene ko taiyyar ho jaate hain.

Jatayu kitna bhaagyashaali hua.
Woh Ravana se ladte hue veergati ko prapt hua,
aur ab hume Sugriva ka dar bhi nahi hai.
Hum bechare, bina Sita ke, yahan marne wale hain.”

Angad dukhi tha.
Monkeys zameen par lete the.
Koi aas nahi bachi thi.

🦅 Sampati ko sachai sunai deti hai

Sampati ne unki baatein suni.
Uska dil kaanp gaya.
Usne zor se pukara:

“Yeh kaun hai jo mere bhai Jatayu ki maut ka zikr kar raha hai?
Woh mera laadle bhai tha.
Mujhe batao —
uski Ravana se ladaai kaise hui?
Woh kaise shaheed hua?

Aur yeh bhi batao,
Rama — Dasaratha ka beta —
uska dost kaise bana?”

Sampati ab uda nahi sakta tha.
Kabhi woh suraj ke kareeb gaya tha
aur uske pankh jal gaye the.

Isliye usne vinamrta se kaha:

“Hey veer bandaron,
mera uddhar karo.
Mujhe is pahad se neeche utarne mein madad do.
Main tumse sab kuch sunna chahta hoon.
Main Jatayu ki kahani poori sunna chahta hoon.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.57
    with st.expander("Chapter 4.57 – Angada tells his story to Sampati"):
        text1 = """ 
Sampati ka awaaz dukh se kaanp raha tha…
par monkeys abhi bhi us par bharosa nahi kar rahe the.
Unhe laga —
“Pata nahi yeh pakshi kya chahta hai…”

Sab bandar fasting par baithe the,
marne ka sankalp lekar.
Unhone baithke ek faisla kiya:

“Chalo is vulture ko neeche utaar dete hain.
Phir yeh chahe toh hume kha le.
Hum toh waise bhi yahin marne wale hain.
Agar yeh hume kha kar apna pet bhar le,
toh hamara prayas bhi safal ho jaayega.”

Is tarah sochkar, monkeys ne Sampati ko pahad se neeche utarne mein madad ki."""

        create_image_text_layout("attached_assets/chapter4/4.57.jpg", text1, layout="side", image_position="left")

        text2 = """ 
🐒 Angad bolna shuru karta hai

Phir Angad ne pyaar se Sampati se kaha:

“Hey Pakshi-raaj,
Hamare vansh ke praarambhik raja the Riksharajas —
meri par-dadaji.

Unke do putr the: Bali aur Sugriva.
Dono bahut shaktishaali aur dharmic the.
Mere pitashri Bali to poori duniya mein prasiddh the.”

Angad ne thoda saans li, phir kahani aage badhai…

🌲 Ram, Lakshman, aur Sita ka vanvaas

“Ek din,
Ayodhya ke veer raja Rama,
jo King Dasaratha ke putr aur Ikshvaku vansh ke deepak the,
apne pita ki aagya se vanvaas gaye.

Sita aur Lakshmana unke saath the.
Dandaka van mein shanti se jee rahe the…”

Phir Angad ki awaaz udaas ho gayi:

“Par ek din,
Ravana Sita mata ko utha le gaya.
Us samay tumhare bhai Jatayu ne unhe dekha.
Jatayu ne himmat se Ravana ka rath toda,
Sita ko chhudaya…

Par woh budha aur thaka hua tha.
Ravana ne use maar dala.

Rama ne apne haathon se
Jatayu ki antimsanskaar kiya.
Woh swarg ko prapt hua.”

⚔️ Sugriva aur Rama ki mitrata

“Iske baad Rama ne mere chacha Sugriva se dosti ki.
Sugriva ne unki madad maangi…

Aur phir Rama ne mere pita Bali ko maar diya.
Bali ne Sugriva ko raajya se nikala tha,
isliye Rama ne nyay ki taraf se uska saath diya.

Bali ki mrityu ke baad
Sugriva raaja bane.”

🔍 Sita ki talaash… aur monkeys ka dukh

“Rama ne hum sab monkeys ko
chaaron dishaon mein bheja
taaki hum Sita mata ko dhoondh sakein.

Par hum nahi dhoondh paaye.

Dandaka van se nikle,
phir ek badi si gufa mein chhale gaye
jo Maya ne banayi thi.

Wahan humne poora ek mahina guzaar diya.
Isse hum Sugriva ke dwara diye gaye samay se
bahut zyada der ho gaye.

Ab agar hum khali haath laut jaate,
toh Sugriva, Lakshmana, aur Rama ka krodh
hum bardasht nahi kar paate.

Isliye humne faisla kiya…
ki hum yahin upwas karke
pran tyag kar denge.”

Angad ne apni baat sambhaal kar puri ki.
Uski aankhon mein udaasi thi.
Par uske shabdon mein sachchai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.58
    with st.expander("Chapter 4.58 – Sampati tells the monkeys where Sita is hidden"):
        text1 = """ 
Monkeys ki dukhi kahani sunkar
Sampati, Jatayu ka bada bhai,
aankhon mein aansu bhar kar bola:

“Hey vanaro…
Tumne bataya ki mera pyaara bhai Jatayu
Ravana se ladte-ladte shaheed ho gaya.
Main budha ho chuka hoon,
aur mere pankh bhi jal gaye the…
Isliye main uska badla nahi le sakta.”

Uska dil toot gaya tha."""

        create_image_text_layout("attached_assets/chapter4/4.58.jpg", text1, layout="side", image_position="left")

        text2 = """ 
🌞 Sampati ki purani kahani

Sampati ne yaad kiya:

“Pehle, jab Indra ne Vritra-asur ko maara tha,
main aur Jatayu soch rahe the
kaun zyada shaktishaali hai.

Dono aasman mein suraj ki taraf udd gaye.
Par jab suraj bilkul upar aa gaya,
Jatayu ki shakti kam hone lagi.
Woh jalne laga.

Maine usse bachane ke liye
apne pankhon se use dhak diya…
par usse bachate-bachate
mere hi pankh jal gaye!

Main Vindhya par gir gaya
aur usse alag ho gaya.
Tab se mujhe nahi pata tha
uske saath kya hua.”

Sampati ro pada.

🐒 Angad ka sawaal

Angad ne aadab se poocha:

“Hey Sampati,
Agar tum Jatayu ke sachmuch bhai ho
aur tumne hamari kahani sun li,
toh batao —
kya tum jante ho Ravana kahan rehta hai?
Sita mata kahan chhupakar rakhi gayi hai?”

🦅 Sampati ka bada rahasya

Sampati ne gehri, shant awaaz me kaha:

“Vanaro,
Mere pankh nahi rahe,
par meri drishti aur buddhi ab bhi shaktishaali hai.
Main Ram ka kaam karunga —
sirf apne shabdon se.”

Usne bataya:

“Maine Devtaon aur Asuron ke yudh dekhe hain.
Samudra manthan bhi dekha hai.
Vishnu ke teen bade kadam bhi janta hoon.
Par sabse zaroori baat yeh hai—

Maine Sita ko dekha tha.

Ravana ek sundar, jawan aur roti hui stree ko
aasman mein le ja raha tha.
Woh baar-baar pukaar rahi thi:
‘Hey Rama!’
‘Hey Lakshmana!’

Uske gehne neeche gir rahe the…
uska peela, chamakta hua vastra
Ravana ki kaali deh par
bijli ki tarah chamak raha tha.

Main samajh gaya —
woh Sita hi thi.”

Monkeys ka saans ruk gaya.

🌴 Lanka ka varnan

Sampati ne kaha:

“Ravana, Vishravas ka putra aur Kuber ka bhai,
Lanka naam ki nagri mein rehta hai.
Yeh nagri Vishvakarma ne banayi hai.

Yeh samundar ke beech ek island par hai.
Yahan se 100 yojan door —
lagbhag 400 miles.

Sone ke dwar, sone ki deeware,
ucch mahal, tej se chamakti kalakritiyan—
Lanka bahut shandaar hai.

Aur wahi,
Ravana ke andar-ke mahal mein,
rakshasiyon ki pehredari mein,
Sita mata bandi hai.”

Monkeys ke chehre par umeed chamak uthi.

🕊️ Pakshiyon ka gyaan aur Sampati ki drishti

Sampati ne bataya:

“Hum bade pakshi
janam se hi door-dar tak dekh sakte hain.
Hum 400 miles door bhi sapasht dekh lete hain.
Isliye main aaj bhi
Ravana aur Sita ko dekh sakta hoon.”

Phir usne monkeys ko salah di:

“Tumhe samundar paar karna hoga.
Sita ko dhundna hoga.
Aur phir Rama ke paas lautna hoga.

Ab mujhe tum Varuna ke teer le chalo —
main wahan apne bhai Jatayu ke liye
jal-anjali dena chahta hoon.”

🌊 Monkeys ki madad — aur khushi ka pal

Vanaro ne bada prem dikhaya.
Unhone be-pankh Sampati ko
sambhaal kar samundar kinaare le gaye.

Phir use wapas Vindhya par chhod diya.

Aur jab unhe Sita ke baare mein
puri jankari mil gayi…

toh unke dil khushi se bhar gaye.
Aasha phir jaag uthi.
Sita ko dhundhna ab sambhav tha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.59
    with st.expander("Chapter 4.59 – Sampati encourages them to continue their mission"):
        text1 = """ 
Sampati ne jo meethi—amrit jaisi—baatein batayi,
unhe sun kar sab monkeys ki umeed wapas aa gayi.
Sab ke dil halka ho gaye.

Tab Jambavan, sabse purane aur gyaani vanar,
zameen se uthkar bole:

“Hey Vulture King,
Sita kahan hai?
Kisne use dekha?
Kisne use chhupaya?
Mithila ki beti kaun le gaya?

Humein sab batao—
taaki hum jungle ke sab praaniyon ko bachaa sakein.
Aur humein yaad hai—
Dasaratha ji ke teeron ki shakti koi nahi bhool sakta!
Aur Lakshmana ke bijli-jaisi baan to sabko hila kar rakh dete hain!”"""

        create_image_text_layout("attached_assets/chapter4/4.59.jpg", text1, layout="side", image_position="left")

        text2 = """ 
🦅 Sampati phir kahani batata hai

Monkeys ab fasting chhod chuke the.
Sampati unhe tasalli deta hua bola:

“Suno, vanaro…
Main tumhe batata hoon
ki maine Sita ke baare mein kaise jaana,
aur kisne mujhe uska pata diya.

Bahut saal pehle,
jab main is kathin Vindhya par gira tha—
tab se main yahin chala aaya.
Ab main bohot budha ho gaya hoon.
Par mera beta Suparshva,
jo sabse accha pakshi hai,
roze mujhe khana laata tha.”

Sampati thodi der rukkar bola:

“Hum pakshiyon ka swabhaav hi kuch alag hai—
Gandharv log manoranjan pasand karte hain,
Saanp log gusse wale hote hain,
Hiran bahut sharmile hote hain…
Aur hum—hum bahut bhookhe-sookhe prakriti ke hain!”

🍃 Suparshva ka anokha drishya

Ek din Sampati bhookh se pareshaan tha.
Suparshva subah-subah uda aur shaam tak wapas aaya—
par bina khane ke.

Woh dukhi hoke bola:

“Pitaji,
Aaj main Mahendra Parvat ke paas
samay kaat raha tha.
Wahan main un praaniyon ko rok raha tha
jo samundar paar aate-jate hain.

Tabhi maine dekha—
aankhon ke saamne jaise kaali megh ka tukda chal raha ho.
Woh Ravana tha.
Aur uske haath mein ek sundar stree thi—
jo subah ki roshni jaise chamak rahi thi.

Main socha,
‘In dono ko pakad loon toh pitaji ka bhojan ho jaaye.’
Par Ravana ne vinamrta se kaha:
‘Mujhe jaane do.’

Aur hum shaant praaniyon ko
shaant logon ko thoda toh daya deni hi chahiye…”

Suparshva aage bola:

“Phir aasman ke praaniyon—
Siddha, Rishi, aur Devtayein—
mere paas aaye.

Unhone kaha:

‘Bhale hi Sita dukh mein hai,
par woh zinda hai!
Aur tumhare liye accha hua
ki Ravana tumhare saamne se nikal gaya.’

Phir Siddhayein boli:

‘Woh jo stree tumne dekhi,
woh Rama ki patni Sita hai.
Uska vastra phata hua tha,
baal bikhar gaye the,
aur woh roti hui
“Rama!” “Lakshmana!” pukaar rahi thi.’”

🦅 Sampati ka sankalp

Sampati fir monkeys ki taraf mudkar bola:

“Sito ki gati sunkar mera dil toot gaya tha.
Par bina pankhon ke main kuch nahi kar sakta tha.
Lekin main apne gyan se tumhari madad karunga.
Main Rama ke kaam ko apna kaam maan chuka hoon.”

Usne monkeys ki taraf gaur se dekha:

“Tum sab itne shaktishaali ho
ki devta bhi tumhe rok nahi sakte.
Rama aur Lakshmana ke teer
teenon lokon ko hila sakte hain.
Aur tum sab milkar—
Ravana ko puri tarah hara sakte ho!

Isliye der kis baat ki?
Jis kaam ko karna sahi ho—
usme tezi dikhani chahiye.
Aage badho, vanaro!
Tumhara lakshya tumhari pratishtha banega.”"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 4.60
    with st.expander("Chapter 4.60 – The story of the ascetic Nishakara"):
        text1 = """ 
Jab Sampati ne apne bhai Jatayu ke liye
jal-anjali aur snan kar liya,
toh sab monkey chiefs us adbhut pahad par baith gaye.
Sampati ko beech mein rakha gaya,
jaise veer praja apne buzurg ko gher leti hai.

Tab Sampati ne Angad se muskurate hue kaha:

“Hey vanaro,
Shant ho kar meri baat suno.
Main tumhe sach-sach bataunga
ki maine Maithili (Sita) ke baare mein kaise jaana.”"""

        create_image_text_layout("attached_assets/chapter4/4.60.jpg", text1, layout="side", image_position="left")

        text2 = """ 
☀️ Sampati ka gira hua din

Sampati ne yaad kiya:

“Bohot saal pehle,
main Vindhya par gir gaya tha.
Mere pankh suraj ki garmi se jal gaye the.
Main be-hosh tha.

Chhe din baad jab mujhe hosh aaya,
main kamzor tha, bhooka tha,
aur aas-paas kuch samajh nahi pa raha tha.

Phir dheere-dheere
jab maine jheelon, pattharon, nadiyon,
ghane jangal aur pahaadon ko dekha—
toh mujhe yaad aaya:

‘Haan! Yeh to Vindhya parvat hi hai!
Yeh wahi jagah hai jahan devta bhi aate hain.’”

🧘‍♂️ Sant Nishakara ka aashram

Sampati bole:

“Yahin ek pavitra ashram tha
jahan Rishi Nishakara rehte the.
Woh bahut kathor tapasvi the.
Devta bhi unka samman karte the.

Main iss parvat par 8,000 saal tak pada raha.
Phir jab maine rishi ko kahin nahi dekha,
toh main bohot mushkil se—
ghas aur kaante chalte hue—
pahaad se neeche utara.

Main unse milna chahta tha.
Pehle main aur Jatayu
bahut baar un sant ke paas ja chuke the.”

🌺 Vrikshon se bhara sundar tapovan

Sampati ne kaha:

“Us aas-paas ki hawa meethi lagti thi.
Har ped phool aur phal se bhara hota tha.

Main ashram ke paas ek ped ke niche ruk gaya.
Thodi door maine rishi ko dekha—
unke sharir se tej nikal raha tha,
jaise suraj ki chamak ho.

Woh snan karke aa rahe the.
Unke aas-paas janwar saath chal rahe the—
bhale bhalu, sher, hiran,
aur rang-birange saanp.

Jab rishi ashram mein ghus gaye,
sab janwar chupchaap chale gaye—
jaise raja andar jaaye
toh mantri bahar ruk jaate hain.”

🙏 Nishakara aur Sampati ki mulaqat

Rishi ne jab Sampati ko dekha,
toh unke chehre par dayaa aa gayi.
Woh andar gaye,
phir wapas aaye
aur puchha:

“Hey mitra,
tumhari paron ka rang kyun badal gaya?
Tumhari chaal kamzor kyun ho gayi?
Tumhari saansein itni tez kyun chal rahi hain?

Pehle do vulture hote the—
bijli ki tarah tej,
mann ke mutabik roop badal lene wale.
Ek tum Sampati…
aur doosre tumhare bhai Jatayu!

Tum dono human-roop lekar
mere pair dabate the.
Aaj tum itne badhal gaye ho…
kaise?

Kaunsi chot lagi?
Kaun sa rog aaya?
Tumhare pankh kisne jala diye?

Sab batao, hey veer!”"""
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

