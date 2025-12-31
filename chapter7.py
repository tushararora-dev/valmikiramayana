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
    create_image_text_layout("attached_assets/chapter7/chapter7.jpg", layout="full")
    create_image_text_layout("attached_assets/chapter7/banner7.jpg", layout="full")


    text0 = """
    <h2>Chapter 7: Uttara kanda</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")
    
    # =========================
    # Book 7 – Uttara-kanda
    # =========================

    # Chapter 7.1
    with st.expander("Chapter 7.1 – Sages bow to Lord Rama"):
        text1 = """ 
        Jab Rama ne raakshason ko hara kar
apna rajya wapas paaya,
toh sabhi bade-bade Rishi aur Muni
unko naman karne aaye 🙏

🌿 Rishiyon ka Aagman

Purab se aaye Kaushika, Yavakrita, Gargya, Kanva.
Dakshin se Agastya, Atri aur unke shishya aaye.
Paschim se Dhaumya, Kausheya jaise mahan Rishi aaye.
Uttar se Vasishtha, Vishvamitra, Kashyapa, Gautama aur Jamadagni aaye 🌸

Sabhi Rishi
Vedo ke gyata the,
aur tej se aise chamak rahe the
jaise Agni dev 🔥"""
        create_image_text_layout("attached_assets/chapter7/7.1.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        🚪 Rajmahal ke Dwaar par

Rishi Agastya ne dwarpal se kaha,
“Raja Dasharatha ke putra Rama ko
hamare aane ki soochna de do.”

Dwarpal turant andar gaya
aur Shri Rama ko bataya.

👑 Rama ka Vinamra Swagat

Jaise hi Rama ne suna
ki mahan Rishi aaye hain,
unhone kaha—

“Unhe poore samman ke saath andar lao।”

Rama khud uth kar khade hue,
Rishiyon ko jal, arghya diya
aur har ek ko gaay daan mein di 🐄

Phir unke liye
sone se sajje hue aasan laaye gaye,
jin par kusha ghaas aur mrig-charm bicha tha।

🕊️ Rishiyon ka Aashirvaad

Rama ne sab Rishiyon se pucha,
“Bhagwan ki kripa se
aap sab kushal toh hain na?”

Rishiyon ne muskurakar kaha—

“Hey Raghuvansh ke aanand,
hum sab kushal hain.
Aaj tumhe vijayi dekh kar
hamara hriday prasann ho gaya.”

Unhone kaha—

Tumne Ravana jaise maha-bhayankar raakshas ko maara

Kumbhakarna, Atikaya, Mahodara, Prahasta sab ka vinash hua

Indrajit (Ravani) jo Indra ko bhi hara chuka tha,
woh bhi tumhare haathon maara gaya ⚔️

Tum Sita aur Lakshmana ke saath
sukh-shanti mein ho – yahi sabse bada saubhagya hai 🌼

🤔 Rama ka Prashn

Yeh sab sunkar Rama vinamrata se bole—

“O Mahatmaon,
maine toh bahut se shaktishaali raakshason ko maara.
Phir aap Indrajit ki vijay ko itna vishesh kyon keh rahe ho?”

“Usmein aisi kaunsi shakti thi
jo Ravana mein bhi nahi thi?
Usne Indra ko kaise hara diya?
Usne kaunse var aur kaunse tap se
yeh shakti paayi?”

“Yeh koi aadesh nahi,
sirf meri jigyasa hai.
Agar yeh rahasya kehne yogya ho,
toh kripya mujhe batayein.”

Rama ne yeh kehkar
sab Rishiyon ko
haath jodkar pranam kiya 🙏

🌼 Is Adhyay ka Sandesh

Sacha mahaan wahi hota hai jo vinamra ho

Gyaan aur shakti par ghamand nahi, jigyasa honi chahiye

Buzurgon aur Rishiyon ka samman jeevan ko pavitra banata hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.2
    with st.expander("Chapter 7.2 – Birth of Vishravas"):
        text1 = """ 
        Rama ke prashn par
mahan Rishi Agastya (Kumbhayoni)
shaant swar mein bole—

“Hey Rama,
pehle main Ravana ke vansh ki kahani bataunga.
Uske baad tumhe
uske putra ke vishesh var ke baare mein bataunga.”"""
        create_image_text_layout("attached_assets/chapter7/7.2.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        🌸 Purane Yug ki Kahani

Bahut purani baat hai.
Kritayug mein
Prajapati ke putra
Paulastya
naam ke ek mahan Rishi the.

Woh Paramarishi the.
Gyaan, tap aur shanti ka bhandaar.
Devta bhi unka samman karte the.

Tapasya ke liye
woh Meru Parvat ke paas,
Rishi Trinabindu ke ashram ke nikat rahe.

🎶 Tapasya Mein Vighn

Us jungle mein
Rishiyon, Naagon aur Rajarishiyon ki putriyan
aksar khelne aaya karti thi.

Unke saath Apsarayein bhi hoti.
Gaana, nritya aur sangeet hota.
Yeh sab nishkapat tha,
par isse Paulastya ki tapasya bhang hone lagi.

Isse krodhit hokar
Rishi Paulastya bole—

“Jo kanya meri drishti mein aayegi,
woh turant garbhvati ho jaayegi.”

Yeh sunte hi
sab ladkiyaan bhay se wahan se chali gayi.

🌿 Anjaani Bhool

Par Trinabindu Rishi ki putri
yeh shraap sun nahi paayi.

Woh jungle mein ghoomti rahi
aur apni saathiyon se bichhad gayi.

Us samay
Paulastya Rishi
Vedo ka path kar rahe the.

Jaise hi kanya ne
Vedo ka swar suna
aur Rishi ko dekha,
uske sharir mein parivartan aa gaya.

Woh turant garbhvati ho gayi.

Dar aur uljhan mein
woh apne pita ke ashram laut aayi.

👨‍👧 Pita ka Faisla

Trinabindu Rishi ne dhyan lagaya
aur sach jaan liya.

Phir woh apni putri ko lekar
Paulastya Rishi ke paas gaye
aur vinamrata se bole—

“Hey Mahatma,
meri putri ko sweekar kijiye.
Yeh sada aapki seva karegi.”

Paulastya Rishi ne shaant ho kar kaha—
“Tathaastu.”

Trinabindu apne ashram laut gaye
aur kanya Rishi ke saath rehne lagi.

👶 Vishravas ka Janm

Putri ki seva aur gunon se
Paulastya Rishi prasann hue.

Unhone kaha—

“Tumhare gunon se prasann hoon.
Tumhe mere jaisa putra milega.
Woh dono vanshon ka naam roshan karega.
Uska naam Paulastya bhi hoga
aur kyunki tumne Vedo ka shravan kiya,
woh Vishravas bhi kehlaayega.”

Kuch samay baad
Vishravas ka janm hua 🌼

✨ Vishravas ka Swabhav

Bahut vidvaan

Sabko samaan drishti se dekhne wale

Dharma mein sthir

Tapasya-priya, bilkul apne pita jaise

Teenon lokon mein
unka yash fail gaya.

🌼 Is Adhyay ka Sandesh

Tapasya aur gyaan se mahaan santaan hoti hai

Krodh ke shabd bhi bhagya badal dete hain

Achha charitra sabse badi virasat hoti hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.3
    with st.expander("Chapter 7.3 – Vishravas becomes Lord of Wealth"):
        text1 = """ 
        Vishravas
bilkul apne pita Paulastya jaise nikle.
Bahut shaant, pavitra aur gyani.

Unka jeevan bahut simple tha.
Na bhog ki chinta,
na sukh ki lalach.
Bas dharma, tapasya aur Ved ka adhyayan."""
        create_image_text_layout("attached_assets/chapter7/7.3.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        🌼 Vivaah aur Putra ka Janm

Vishravas ke gunon se prasann hokar
mahan Rishi Bharadvaja
ne apni sundar putri unhe vivah mein di.

Vidhivat vivaah hua.
Aur kuch samay baad
unke yahan ek tejassvi putra ka janm hua 👶✨

Woh balak
brahman ke sab gunon se bhara hua tha—
sanyam, shuddhata, tapasya aur daya.

🌟 Naamkaran: Vaishravana

Jab is balak ka janm hua,
toh dada Paulastya Rishi
bahut prasann hue.

Unhone kaha—

“Yeh balak Vishravas jaisa hai.
Isliye iska naam Vaishravana hoga.”

Saare Rishi khush ho gaye.
Sabne ashirvaad diya.

🔥 Kathor Tapasya

Bada hokar Vaishravana
van mein chale gaye.

Unhone socha—

“Mera kartavya hi mera sab kuch hai.”

Unhone hazaar saal tak
kathor tapasya ki.

Kabhi sirf paani,
kabhi hawa par jeevan,
kabhi kuch bhi nahi.

Samay beet-ta gaya,
par unka sankalp aur majboot hota gaya.

🌺 Brahma ka Var

Ant mein
Brahma
Devtaon ke saath wahan aaye.

Brahma bole—

“Main tumhari tapasya se prasann hoon.
Koi var maango, putra!”

Vaishravana ne vinamrata se kaha—

“Mujhe duniya ka rakshak banna hai.
Main sabka bhala chahta hoon.”

Brahma muskuraye 😊
aur bole—

“Tathaastu!
Tum Dhan ke Rakshak banoge.
Tum chaar Lokapalon mein se ek hoge—
Indra, Varuna, Yama aur tum.”

Unhone Vaishravana ko
Pushpak Vimaan bhi diya ✨🚀
jo suraj jaisa chamakta tha.

🏝️ Lanka ka Rajya

Var paakar
Vaishravana ne apne pita Vishravas se poocha—

“Main kahan rahoon, pitaji?”

Vishravas bole—

“Samudra ke paas
Lanka naam ki sundar nagari hai.
Woh ab khaali hai.
Tum wahan raaj karo aur sukhi raho.”

Vaishravana ne
Lanka ko apna nivaas bana liya.

Wahan Nairritas khushi se rehne lage.
Nagari phir se jeevit ho uthi 🌸

✨ Dhan ke Devta

Ab Vaishravana—

Dhan ke Devta bane

Pushpak Vimaan mein yatra karte

Devta aur Gandharva unki stuti karte

Apsaraon ka nritya hota

Suraj jaise tej se chamakte hue
woh apne mata-pita se milne
aate-jaate rehte ☀️

🌼 Is Adhyay ka Sandesh

Tapasya aur dharma se mahaan pad milta hai

Nishkaam seva sabse bada gun hai

Jo sabka bhala chahe,
wahi sachcha rakshak hota hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.4
    with st.expander("Chapter 7.4 – Origin of Rakshasas and their boons"):
        text1 = """ 
        Rama yeh sab sunkar bahut hairaan ho gaye 😮
Unhone Agastya ji ki taraf dekha aur bole—

“Gurudev, aap keh rahe ho ki
pehle Lanka Rakshason ki thi.

Par hum toh jaante hain ki
Rakshas Paulastya ke vansh se hue.

Phir yeh kaun the jo pehle Lanka mein rehte the?
Unka pehla raja kaun tha?
Aur Vishnu ne unhe kyun nikaal diya?

Kripya meri jigyasa door kijiye.”"""
        create_image_text_layout("attached_assets/chapter7/7.4.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        🌊 Prajapati aur Pehla Nirman

Agastya ji shaant muskuraye 😊
aur bole—

“Bahut pehle
Prajapati
ne jal (water) ki rachna ki.

Fir unhone jal ki raksha ke liye
kai prani banaye.

Par yeh sab prani
bhookh aur pyaas se pareshaan ho gaye.

Unhone vinamrata se poocha—

‘Ab hum kya karein?’

Prajapati bole—

‘Jal ki raksha karo!’”

🗣️ Rakshami aur Yakshami

Kuch prani bole—

“Rakshami” (Hum raksha karenge)

Kuch bole—

“Yakshami” (Hum yagya karenge)

Tab Prajapati bole—

Jo bole Rakshami → Rakshas

Jo bole Yakshami → Yaksha

👉 Isi tarah
Rakshas aur Yaksha bane.

⚔️ Heti aur Praheti

Us samay do bhai hue—

Heti – bhayanak, yoddha

Praheti – dharmik aur shaant

Praheti van chale gaye tapasya ke liye 🌲
Par Heti ne vivah kiya.

👹 Vidyutkesha ka Janm

Heti ne Kala ki behen Bhaya se shaadi ki.
Unse ek putra hua—

👉 Vidyutkesha

Woh surya jaisa tejassvi tha ☀️
Jab bada hua,
uski shaadi Sandhya ki beti se hui.

Kuch samay baad
us patni ne ek balak ko janm diya
Mandara Parvat par.

Par maa use chhod kar chali gayi 😢

🔥 Shiva ki Karuna

Balak zor-zor se rone laga 😭
Uski awaaz sunkar aaye—

Shiva
aur Parvati

Parvati ko daya aa gayi 💗
Shiva ne balak ko vardaan diya—

Amar (immortal) bana diya

Maa ke barabar umar de di

Ek vimaan (aerial car) bhi diya 🚀

Parvati ne bhi vardaan diya—

“Rakshason ke bachche
janm lete hi bade ho jaayenge.”

👑 Sukesha – Pehla Maha Rakshas

Yeh balak bada hokar
Sukesha ke naam se prasiddh hua.

Usse itna ghamand ho gaya
ki woh har jagah apne vimaan mein
udta phirta tha ✨

Woh khud ko
Indra jaisa maanne laga."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.5
    with st.expander("Chapter 7.5 – Story of Sukesha’s three sons"):
        text1 = """ 
        Ek Gandharva tha jiska naam Gramani.
Woh aag jaisa tejassvi tha 🔥
Uski ek beti thi—Devavati.
Woh itni sundar thi ki log use
doosri Shri (Lakshmi) kehte the ✨

Gramani ne apni beti
Sukesha ko vivaah mein de di.
Devavati apne pati ke saath
bahut khush thi 😊"""
        create_image_text_layout("attached_assets/chapter7/7.5.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        👶 Teen Maha Putron ka Janm

Samay ke saath
Sukesha ke teen putra hue—

Malyavan

Sumali

Mali

Yeh teenon
teen yajna-agni jaise prachand the 🔥🔥🔥
Shaant hote toh teen lok jaise
Aur yuddh mein toh
teen Vedo jitni shakti rakhte the.

🧘‍♂️ Kathor Tapasya

Apne pita ke vardaan dekhkar
teenon bhaiyon ne socha—

“Hum bhi tapasya karenge!”

Woh Mount Meru par gaye 🏔️
Aur bahut kathor tapasya ki.

Unki tapasya se
teenon lok kaanp uthe 😨
Devta, Asur, sab chintit ho gaye.

🌼 Brahma ka Vardaan

Ant mein
Brahma
khud aaye aur bole—

“Mujhse vardaan maango.”

Teenon bhaiyon ne kaha—

Hume amar banao

Hume aparajit banao

Hume ek-doosre se juda na hone ka vardaan do

Brahma bole—

“Tathastu!” 🙏

😈 Ghamand aur Atyachar

Vardaan milte hi
teenon bhai bahut ghamandi ho gaye 😤

Unhone—

Devtaon ko sataya

Rishiyon ke yagya roke

Sab jagah bhay faila diya

Devta aur Rishi
jaise narak mein jee rahe ho 😞

🏰 Lanka ka Nirman

Teenon bhai gaye
Vishvakarma ke paas.

Bole—

“Hume aisi nagri chahiye
jo Indra ki Amaravati jaisi ho.”

Vishvakarma ne kaha—

“Dakshin samudra ke paas
Trikuta Parvat par
ek nagri hai—Lanka.”

Lanka

sunehri deewaron se ghiri thi

gehri khaaiyon se surakshit thi

aur kabhi na girne wali lagti thi ✨

Teenon bhaiyon ne
Lanka ko apna ghar bana liya 🏰

💍 Teen Vivaah aur Vansh

Ek Gandharvi Narmada thi.
Uski teen sundar betiyan thi 🌸
Unhone teenon bhaiyon se vivaah kiya.

👑 Malyavan ke Vansh

Uski patni Sundari thi.
Unse hue—
Vajramushti, Virupaksha, Durmukha,
Matta, Unmatta…
Aur ek beti—Anala

👑 Sumali ke Vansh

Uski patni Katumati thi 🌕
Unse hue—
Prahasta, Akampana, Vikata, Dhumraksha
aur sabse mahatvapurn—Kaikasi

👉 Kaikasi se aage chal kar Ravana ka janm hua

👑 Mali ke Vansh

Uski patni Vasuda thi.
Unke putra—
Anala, Anila, Hara, Sampati
jo baad mein Vibhishana ke salahkaar bane.

⚠️ Ant mein kya hua?

Apni shakti ke nashe mein
Rakshas—

yagya todte

Rishiyon ko pareshan karte

prakriti ka apmaan karte

👉 Yahin se
vinash ka beej pada 🌑

🌱 Is Adhyay ka Sandesh

Tapasya se shakti milti hai,
par ghamand se vinash

Shakti bina dharma ke
bojh ban jaati hai

Jo prakriti aur sadhuon ko dukh deta hai,
uska ant nishchit hota hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.6
    with st.expander("Chapter 7.6 – Vishnu protects the Gods"):
        text1 = """ 
        Rakshason ke atyachaar se
Devta aur Rishi bahut dar gaye 😟
Unke yagya toot rahe the,
unka swarg chhin raha tha.

Darr ke maare
sab Mahadev ke paas gaye 🙏"""
        create_image_text_layout("attached_assets/chapter7/7.6.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        🔱 Devtaon ki Fariyad

Devta bole:

“Prabhu, Sukesha ke putra
Malyavan, Sumali aur Mali
vardaan ke ghamand mein
humein satane lage hain.

Woh kehte hain –
‘Main hi Vishnu hoon,
Main hi Brahma hoon,
Main hi Indra hoon!’

Swarg ab surakshit nahi raha.
Kripya humein bachaiye.”

🌙 Mahadev ka Uttar

Mahadev shaant rahe 🕉️
Aur bole:

“Main khud inhe nahi maar sakta.
Par ek upaay bata sakta hoon.”

“Tum sab
Narayana (Vishnu) ke paas jao.
Wahi inka vinash karenge.”

Devtaon ko naya sahara mila ✨

🐚 Vishnu ke Sharan Mein

Sab Devta
Vishnu ke charnon mein gir gaye 🙏

Bole:

“Prabhu, hum aapki sharan mein hain.
Lanka ke Rakshas
teen bhayankar aag jaise ho gaye hain 🔥🔥🔥
Humein bachaiye!”

🟡 Vishnu ka Vachan

Vishnu bole, garajti awaaz mein:

“Dar mat.
Main Sukesha ke putron ko jaanta hoon.
Unka ghamand ab seema paar kar chuka hai.

Main unka ant karunga.”

Devta shant hue 😌
Aur apne-apne lok laut gaye.

😈 Rakshason ka Ghamand

Lanka mein
Malyavan ne apne bhaiyon se kaha:

“Devta Vishnu ke paas gaye hain.
Hari humein maarna chahte hain.”

Par Sumali aur Mali hans pade 😤

“Humein kisse darr?
Humne Veda padhe, yagya kiye,
koi humein hara nahi sakta!”

Teenon ne yuddh ka nirnay liya ⚔️

🚨 Apashakun (Bure Sanket)

Jaise hi Rakshas yatra par nikle—

Aasmaan se garam khoon gira ☁️🩸

Samundar uchhalne lage 🌊

Pahad kaanp gaye 🏔️

Giddh aur siyaron ki bhayanak awaaz aayi 🐺

Yeh sab
vinash ke sanket the ⚠️

Par Rakshas ruke nahi.

🦅 Vishnu ka Aagman

Tab Vishnu
apna shastra pehne,
Garuda par sawar hue 🦅

Peela vastra,
chakra, shankh, gada, dhanush –
sab tej se chamak rahe the ✨

Aisa lag raha tha
jaise badal par bijli chamak rahi ho ⚡☁️

Dev Rishi aur Gandharva
Vishnu ka stuti gaan karne lage 🎶

⚔️ Yuddh ka Aarambh

Garuda ke pankhon ki hava se
Rakshason ke jhande girne lage 🌪️

Par Rakshas bhi chup nahi rahe.
Unhone hazaaron teer chala diye 🎯

Teer Vishnu par barasne lage,
khoon aur maans se bhare hue.

Yahan se
bhayanak yuddh shuru hua ⚔️🔥

🌱 Is Adhyay ka Sandesh

Ghamand hamesha vinash laata hai

Devta bhi tab jeet paate hain
jab dharma unke saath ho

Jab anyay badhta hai,
tab Narayana swayam aate hain"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.7
    with st.expander("Chapter 7.7 – Battle between Vishnu and Rakshasas"):
        text1 = """ 
        Aasmaan garaj raha tha ☁️⚡
Rakshas baadalon jaise chha gaye.

Hazaaron teer, talwaar, bhale
Vishnu par barasne lage.

Par Vishnu shaant rahe 😌
Bilkul aise jaise
saans ko niyantran mein rakha ho."""
        create_image_text_layout("attached_assets/chapter7/7.7.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        🏹 Vishnu ka Pratikaar

Vishnu ne apna dhanush uthaya.

Teer bijli jaise nikle ⚡
Aur Rakshason par baras pade.

Jis tarah aandhi
baarish ko uda deti hai,
waise hi Rakshas bikhar gaye.

Phir Vishnu ne
apna shankh Panchajanya bajaya 🐚

BOOOOM!

Us dhvani se
teenon lok kaanp gaye 🌍

😱 Rakshason mein Bhay

Shankh ki awaaz se—

Ghode gir gaye 🐎

Haathi shaant ho gaye 🐘

Yoddha rath se neeche gir pade

Rakshas dar gaye 😨
Unka bal toot gaya.

⚔️ Teeron ki Varsha

Vishnu ke teer
hazaaron ki sankhya mein chale.

Rakshas girne lage—
jaise pahad bijli se toot jaate hain ⛰️⚡

Khoon behne laga,
dharti laal ho gayi.

🦁 Rakshas Bhagane Lage

Rakshas aise bhaagne lage
jaise—

Chuha saanp se

Saanp billi se

Billi kutte se

Kutta sher se 🦁

Sab Lanka ki taraf bhaag pade.

😡 Sumali ka Hamla

Rakshas Sumali ne
phir se himmat jutaayi.

Usne Vishnu par
teeron ki baarish kar di.

Kuch Rakshason ko phir hausla mila.

Par Vishnu shaant hi rahe.

💥 Mali ka Ant

Tab Mali aage badha.

Usne gada se
Garuda par zor se vaar kiya.

Garuda ko dard hua
aur woh Vishnu ko door le gaya.

Rakshas khush ho gaye 😈
“Jeet gaye!” chillaye.

🌞 Vishnu ka Chakra

Par Vishnu krodhit ho gaye 🔥

Unhone peechhe mud kar
apna Sudarshan Chakra chhoda.

Woh suraj jaise chamka 🌞
Aur seedha Mali ke sir par laga.

Chak!

Mali ka sir
khoon ki dhaar ke saath gir pada.

🎉 Devtaon ki Jai

Devta khushi se garaj uthe 🙌

“Jai ho! Jai ho Narayana!”

Rakshason ka ghamand toot gaya.

🏃 Ant mein Kya Hua

Sumali aur Malyavan
apni bachi hui sena ke saath
Lanka bhaag gaye.

Garuda phir uthe
aur pankhon ki hava se
Rakshason ko samundar mein gira diya 🌊

Jinke sir kat gaye,
jinke shastra toot gaye,
woh sab girte chale gaye.

🌱 Is Adhyay ka Sandesh

Adharma kitna bhi shaktishaali ho,
ant mein girta hi hai

Dharma aur shaanti sabse bada bal hai

Ghamand andha kar deta hai

Jab duniya ko zarurat hoti hai,
tab Vishnu swayam aate hain"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.8
    with st.expander("Chapter 7.8 – Vishnu fights Malyavan"):
        text1 = """ 
        Jab Vishnu ne
Rakshason ki poori sena ko hara diya,
tab Malyavan ruk gaya.

Woh bhaagte-bhaagte
samundar ki lehar jaise
kinare par thahar gaya 🌊

Uski aankhen laal ho chuki thi 😡
Sir kaanp raha tha."""
        create_image_text_layout("attached_assets/chapter7/7.8.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        🗣️ Malyavan ka Ghamand

Malyavan bola:

“O Narayana!
Tum yoddhon ke niyam nahi jaante.
Bhaagte hue shatru ko maarna paap hai.
Agar yuddh chahte ho,
toh saamne aao.
Main yahin khada hoon!”

Uski awaaz mein
ghamand tha,
par sach kam tha.

🌸 Vishnu ka Uttar

Vishnu shaant rahe 😌
Unki aankhen kamal jaise lal thi.

Vishnu bole:

“Maine devtaon se vachan diya hai
ki main tumhare bhay se
unhe mukt karunga.
Devtaon ka kalyan
mere jeevan se bhi bada hai.
Isliye tumhara ant nischit hai.”

⚔️ Bhala aur Pratikaar

Gusse mein
Malyavan ne bhala uthaya.

Woh bhala
Vishnu ke seene mein laga ⚡
bijli jaise chamak uthi.

Par Vishnu ko
dard ne hilaaya nahi.

Vishnu ne
wahi bhala nikaala
aur zor se Malyavan par phenka.

💥 Malyavan Girte-Girte Bacha

Bhala
Malyavan ke seene par laga.

Uska kavach toot gaya.
Aankhon ke aage andhera chha gaya 😵

Par kuch pal baad
woh phir seedha khada ho gaya,
jaise chattan 🪨

🏏 Gada ka Vaar

Ab Malyavan ne
kaanton wali gada uthayi.

Usne Vishnu ke seene par
zor se vaar kiya.

Devtaon ne aasmaan se kaha:

“Bahut accha! Bahut accha!”

Par sach yeh tha—
Vishnu abhi bhi atal the.

🦅 Garuda ka Prakop

Malyavan ne
Garuda par bhi hamla kiya.

Garuda gusse mein aa gaye 😤
Aur pankhon ki tez hawa chala di.

Jaise aandhi
sookhe patton ko uda deti hai,
waise hi Malyavan pichhe hat gaya.

🏃 Rakshason ki Haar

Yeh dekh kar
Sumali ghabra gaya.

Woh apni sena ke saath
Lanka ki taraf bhaag gaya.

Malyavan bhi
sharm aur haar ke saath
Lanka laut gaya 😔

🌑 Rakshason ka Patan

Bar-bar haar kar
Rakshas Vishnu ka saamna
nahi kar paaye.

Unhone Lanka chhod di
aur Patala chale gaye.

Wahan woh apni patniyon ke saath
chhup kar rehne lage.

✨ Sachchai ka Prakaash

Agastya Rishi bole:

“O Rama!
Yeh sab Rakshas
tumhari hi shakti se hare the.
Tum hi Narayana ho.
Jab dharma kamzor padta hai,
tum swayam aate ho
aur adharm ka naash karte ho.”

🌱 Is Adhyay ka Sandesh

Ghamand yuddh nahi jeetata

Dharma aur vachan sabse bade hote hain

Burai chahe kitni bhi badi ho,
sach aur nyay ke aage haar jaati hai

Jab duniya ko bachane ki zarurat hoti hai,
Bhagwan swayam aate hain"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.9
    with st.expander("Chapter 7.9 – Birth of Ravana and his brothers"):
        text1 = """ 
        Kuch samay baad,
Rakshas Sumali
Patala se upar aaya.

Uske kaan mein sone ke kundal the ✨
Aur saath mein thi uski beti Kaikasi,
jo sundar thi,
bilkul Shri jaisi."""
        create_image_text_layout("attached_assets/chapter7/7.9.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        🤔 Sumali ka Sochna

Sumali ne socha:

“Hum apni shakti kaise badha sakte hain?”

Usne Kaikasi se kaha:

“Beti, tumhara vivah ka samay aa gaya hai.
Tum Vishravas Rishi ko chuno.
Unse tumhe aise putra milenge
jo bahut shaktishaali honge.”

Kaikasi ne
pita ki baat maan li 🙏

🔥 Vishravas ke Aashram Mein

Kaikasi
Vishravas Rishi ke paas pahunchi.

Rishi us samay
agni-yagya mein lage hue the 🔥
Aur chaarth agni jaise chamak rahe the.

Kaikasi
chupchaap khadi rahi,
nazar neeche,
pair se mitti khurachti hui.

🧘 Rishi ka Vachan

Vishravas bole:

“Main jaanta hoon tum kyun aayi ho.
Par tum galat samay par aayi ho.
Isliye tumhare putra
bhayankar aur kroor honge.”

Yeh sunkar
Kaikasi dar gayi 😟
Aur boli:

“Maharaj, mujhe aise putra nahi chahiye.
Kripa kijiye.”

Rishi ne daya dikhayi ❤️
Aur kaha:

“Tumhara aakhri putra
dharmic aur mere jaisa hoga.”

👶 Dashagriva ka Janm

Kuch samay baad,
Kaikasi ne ek bhayanak shishu ko janm diya.

Uske:

10 sir the

20 baahen thi

Rang kaala tha

Daant bade aur bhayanak the 😨

Uske janm par:

giddh aur siyaron ne cheekhna shuru kiya

khoon ki baarish hui

suraj chhup gaya

hawa tez chalne lagi

Rishi Vishravas ne naam diya:

“Dashagriva”
(das gardan wala)

👹 Baaki Santaan

Uske baad paida hue:

Kumbhakarna – bahut bada, bahut bhookha

Shurpanakha – bhayanak roop wali

Bibishana – shaant, dharmic, gyaani 🌼

Bibishana:

Veda padhta

indriyon par niyantran rakhta

sada dharma ke saath khada rehta

😈 vs 😇 Bhaiyon ka Swabhav

Kumbhakarna
– Rishiyon ko bhi kha jaata
– kabhi santusht nahi hota

Dashagriva
– ghamandi
– shakti ka bhookha

Bibishana
– shaant
– satya aur nyay ka pakshdhar

🔥 Jalan aur Pratigya

Ek din Vaishravana (Kubera)
Pushpak Vimaan mein aaya ✨

Woh chamak raha tha,
tej se bhara hua.

Kaikasi ne Dashagriva se kaha:

“Dekho tumhara bhai Kubera
kitna mahaan ban gaya hai.
Tum bhi uske jaise bano.”

Dashagriva ke mann mein
jalan bhar gayi 😠

Usne pratigya li:

“Main Kubera se bhi
zyada shaktishaali banunga!”

🕉️ Kathor Tapasya

Dashagriva aur Kumbhakarna
Gokarna gaye.

Wahan unhone:

kathor tapasya ki

bhookh, dard, kasht jhela

Dashagriva ne socha:

“Tapasya se
main sab kuch paa sakta hoon.”

Unki tapasya se
Brahma ji prasann hue ✨
Aur unhe
mahavar dene aaye.

(Yahin se shuru hoti hai
Ravana ki shakti ka yug…)

🌱 Is Adhyay ka Sandesh

Galat ichha se paayi shakti,
vinash laati hai

Ghamand bhai-bhai ko dushman bana deta hai

Dharma hamesha shaant aur sthir hota hai

Sab ek hi ghar mein paida hote hain,
par karm hi bhavishya banate hain"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.10
    with st.expander("Chapter 7.10 – Ravana’s severe penance"):
        text1 = """ 
        Rama ne Agastya Rishi se poocha 🙏
“Maharaj, Dashagriva aur uske bhaiyon ne kaisi tapasya ki?”

Agastya shaant swar mein bole—"""
        create_image_text_layout("attached_assets/chapter7/7.10.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        🔥 Kumbhakarna ki Tapasya

Kumbhakarna ne bhi
bahut kathin tapasya ki.

Garmiyon mein
paanch aag ke beech khada rehta 🔥

Barsaat mein
veer-asana mein baithta 🌧️

Sardi mein
thande paani mein khada rehta ❄️

Aise hi 2000 saal beet gaye.
Woh bhi apne tareeke se
dharma ka raasta follow kar raha tha.

🌸 Bibishana ki Shuddh Tapasya

Bibishana to
dharma ka jeevan roop tha 😇

5000 saal
ek pair par khada raha

Uske baad
5000 saal
suraj ki taraf muh karke,
haath upar uthaye,
Veda ka dhyaan karta raha ☀️

Jab uski tapasya poori hui:

apsaraon ne nritya kiya 💃

phoolon ki baarish hui 🌸

devtaon ne uski stuti ki

Bibishana ne
10,000 saal
bilkul swarg jaise jeevan mein tapasya ki.

😈 Dashagriva ki Bhayanak Tapasya

Dashagriva ki tapasya
sabse bhayanak thi.

10,000 saal
bina bhojan ke raha

Har 1000 saal
apna ek sir
agni mein balidaan karta 🔥

Aise hi:

9000 saal mein
9 sir agni ko chadha diye

Jab woh
10va sir kaatne ja raha tha,
tab Brahma ji
devtaon ke saath prakat hue ✨

🌟 Brahma ji ka Var

Brahma ji bole:

“Main prasann hoon.
Jo maango, maango.”

Dashagriva khushi se kaanp utha 😈
Aur bola:

“Mujhe amar bana do!”

Brahma ji ne kaha:

“Amaratva dena sambhav nahi.
Kuch aur maango.”

Dashagriva ne kaha:

“Mujhe devta, daitya, danav,
nag, yaksha, rakshas—
koi bhi na maar sake.
Manushya se mujhe koi bhay nahi.”

Brahma ji bole:

“Tathaastu!”

Aur saath hi kaha:

jo sir tune agni ko diye the,
woh sab wapas ug aayenge

tum koi bhi roop
apni ichha se dharan kar sakoge

Dashagriva ke
sab sir wapas aa gaye 😨

🌼 Bibishana ko Mila Maha-var

Phir Brahma ji ne
Bibishana se poocha:

“Tum kya chahte ho?”

Bibishana ne vinamrata se kaha 🙏

“Mera mann hamesha dharma mein rahe.
Sankat mein bhi main galat na karoon.
Bina sikhaye mujhe
Brahma-astra ka gyaan ho.
Mere vichaar hamesha satya ke saath ho.”

Brahma ji prasann ho gaye 😊
Aur bole:

“Tum rakshas kul mein paida hue,
par tumhara hriday pavitra hai.
Main tumhe amaratva deta hoon.”

😴 Kumbhakarna ke Saath Chaal

Jab Brahma ji
Kumbhakarna ko var dene lage,
to sab devta dar gaye 😱

Devta bole:

“Isse var mat do!
Yeh teenon lok kha jayega!”

Brahma ji ne
Sarasvati Devi ko yaad kiya.

Unse kaha:

“Iske muh se
wahi bulwao
jo devta chahte hain.”

Sarasvati Devi
Kumbhakarna ke muh mein pravesh hui.

Kumbhakarna bola:

“Mujhe
anant kaal ki neend chahiye!”

Brahma ji bole:

“Tathaastu!”

Jaise hi Sarasvati Devi gayi,
Kumbhakarna hosh mein aaya 😵
Aur socha:

“Yeh maine kya maang li?”

Par ab kuch nahi ho sakta tha.

🌳 Tapasya ke Baad

Teeno bhai:

Dashagriva 😈

Kumbhakarna 😴

Bibishana 😇

Sleshmataka van mein gaye
Aur kuch samay
sukh se rahe.

🌱 Is Adhyay ka Sandesh

Shakti bina dharma vinash laati hai

Ahankar insaan ko andha kar deta hai

Dharma aur vivek hi sabse bada var hai

Bibishana jaise log
andhere mein bhi roshni ban jaate hain ✨"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.11
    with st.expander("Chapter 7.11 – Kubera gives Lanka to Ravana"):
        text1 = """ 
        Sumali ko jab pata chala
ki Dashagriva aur uske bhaiyon ko
bahut bade var mil gaye hain,
to uska darr khatam ho gaya 😈

Woh Paatal se bahar aaya.
Uske saath Marica, Prahasta, Virupaksha aur Mahodara
bhi gusse aur josh mein aa gaye."""
        create_image_text_layout("attached_assets/chapter7/7.11.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        🐍 Sumali ka Sapna

Sumali ne Dashagriva ko gale lagaya
aur bola:

“Beta, aaj mera sapna poora ho gaya.
Vishnu ke darr se hum
Lanka chhodkar bhag gaye the.
Ab tum shaktishaali ho gaye ho.
Lanka wapas le aao.
Chahe baat se, tohfe se,
ya phir shakti se!”

Usne kaha:

“Agar tum Lanka ke raja bane,
to Rakshas vansh phir se uth khada hoga.”

🤔 Dashagriva ka Pehla Vichaar

Dashagriva ne shaant swar mein kaha:

“Dhanada mera bada bhai hai.
Uske khilaaf jaana
theek nahi lagta.”

Sumali ne baat aage nahi badhayi.
Par uske mann mein beej pad chuka tha 🌱

🔥 Prahasta ki Bhadkaane Wali Baat

Kuch samay baad Prahasta bola:

“Veeron ke liye bhai–bhai
ka rishta zyada maayne nahi rakhta.
Devta aur daitya bhi
ek dusre ke khilaaf lade hain.”

Usne purani kahani sunayi
aur bola:

“Isliye tum bhi
apna adhikar lo.”

Dashagriva ne thoda socha…
aur phir bola:

“Theek hai!” 😈

🏔️ Lanka ke Paas Aagman

Dashagriva apni sena ke saath
Trikuta Parvat par pahucha.

Usne Prahasta ko
doot bana kar bheja.

Sandesh yeh tha:

“Lanka Rakshason ki nagri hai.
Agar tum ise wapas kar do,
to shanti bani rahegi.”

💰 Dhanada ka Uttam Uttar

Prahasta ne yeh sandesh
Dhanada (Kubera) ko diya.

Dhanada shaant tha 😊
Usne kaha:

“Lanka mujhe mere pita ne di thi.
Par main yeh rajya
apne bhai ke saath
baantne ko taiyaar hoon.”

Phir bhi Dhanada
apne pita Vishravas ke paas gaya
aur poocha:

“Pitaji, mujhe kya karna chahiye?”

👴 Pita Vishravas ka Nirdesh

Vishravas ne gambhir swar mein kaha:

“Dashagriva ka mann
varon ke ghamand se andha ho gaya hai.
Usse ladna theek nahi.
Tum Lanka chhod do
aur Kailash Parvat par jao.”

Unhone kaha:

“Wahan Mandakini nadi behti hai.
Devta, gandharva aur apsara
wahan anand se rehte hain.”

🚶‍♂️ Tyag aur Maryada

Pita ki baat maan kar
Dhanada ne:

Lanka chhod di

apna parivaar, dhan
aur sevak saath le gaya

Usne yuddh nahi chuna,
maryada chuni 🌼

👑 Dashagriva ka Rajyabhishek

Prahasta khushi se Dashagriva ke paas gaya
aur bola:

“Lanka khaali ho chuki hai!”

Dashagriva apni sena ke saath
Lanka mein pravesh karta hai.
Rakshas use raja bana dete hain 👑

Lanka phir se
andhere aur ahankar se bhar jaati hai ☁️

🌕 Dhanada ka Naya Nagar

Dhanada ne Kailash Parvat par
ek nayi, pavitra nagri basayi ✨
Jo chamakti thi
jaise chandrama.

🌱 Is Adhyay ka Sandesh

Ahankar rajya dila sakta hai,
par shanti cheen leta hai

Tyag hamesha haar nahi hota

Maryada aur dharma
sabse badi shakti hain
Dhanada ne rajya chhoda,
par imaan nahi chhoda 🙏"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.12
    with st.expander("Chapter 7.12 – Marriages of the Rakshasas"):
        text1 = """ 
        Dashagriva ab Lanka ka raja ban chuka tha 👑
Rajyabhishek ke baad
usne apne bhaiyon ke saath
parivaar ke kaam sochne shuru kiye.

Sabse pehle baat aayi
behen Shurpanakha ke vivaah ki."""
        create_image_text_layout("attached_assets/chapter7/7.12.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        💍 Shurpanakha ka Vivaah

Dashagriva ne
apni behen Shurpanakha
ko Kalaka vansh ke raja Vidyujjihva
se vivaah karwa diya.

Vivaah shaan se hua,
par Rakshasiyon ke tareeke se 😈

🌲 Jungle mein Maya se Mulakaat

Iske baad Dashagriva
shikaar par nikla.

Wahan jungle mein
uski mulaqat hui
Danava Maya se.

Maya ek yuvati ladki ke saath tha.
Dashagriva ne poocha:

“Tum kaun ho?
Aur is sunsaan jungle mein
is sundar ladki ke saath
kyun ghoom rahe ho?”

🧙‍♂️ Maya ki Kahani

Maya ne shaant swar mein kaha:

“Meri patni apsara Hema thi.
Devta use mujhse le gaye.
Main akela reh gaya.”

Usne bataya:

Usne sone ka shehar banaya

Par dukh door nahi hua

Ab woh apni beti ke liye pati dhoondh raha tha

Usne kaha:

“Beti pita ke liye
chinta ka kaaran hoti hai.”

Phir Maya ne apna parichay diya
aur poocha:

“Ab tum batao, tum kaun ho?”

🧬 Dashagriva ka Parichay

Dashagriva ne garv se kaha:

“Main Paulastya vansh ka hoon.
Mera naam Dashagriva hai.
Mere pita rishi Vishravas hain.”

Yeh sunte hi
Maya bahut prabhavit hua ✨

👰 Mandodari ka Vivaah

Maya ne turant kaha:

“Main apni beti
Mandodari
tumhe vivaah mein deta hoon.”

Dashagriva ne kaha:

“Theek hai!”

Jungle mein hi
agni jala kar vivaah hua 🔥

Maya jaanta tha
ki Dashagriva ke pita ka shraap hai,
phir bhi usne yeh vivaah kiya.

Shaadi ke saath Maya ne
Dashagriva ko ek divya bhala (spear)
bhi diya.
Isi bhale se baad mein
Lakshmana ghaayal hue.

👩‍❤️‍👨 Bhaiyon ke Vivaah

Lanka laut kar
Dashagriva ne
apne dono bhaiyon ka bhi vivaah karwaya:

Kumbhakarna ki shaadi
Vajravala se hui

Bibishana ne vivaah kiya
Sarama se

Sarama ek gandharva rajkanya thi.
Uska janm Manasa sarovar ke paas hua tha.
Isliye uska naam Sarama pada.

🎉 Sukh aur Vilas

Sab rakshas apni–apni patniyon ke saath
sukh aur vilas mein jeene lage.
Jaise gandharva
Nandana van mein rehte hain 🌸

⚡ Indrajit ka Janm

Mandodari ne
ek shaktishaali putra ko janm diya.

Bachcha paida hote hi
garaj utha,
jaise baadal ⚡

Puri Lanka ghoonj uthi.

Isliye Dashagriva ne kaha:

“Iska naam Meghanada hoga.”

Wahi Meghanada
baad mein Indrajit ke naam se
prasiddh hua.

Woh apne mahal mein
aise bada hua
jaise raakh ke neeche
aag 🔥

🌱 Is Adhyay ka Sandesh

Shaadi sirf sukh nahi,
bhavishya bhi banati hai

Ghamand aur shakti ke saath
zimmedaari bhi aati hai

Indrajit ka janm
aane wale mahavinash ka sanket tha"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.13
    with st.expander("Chapter 7.13 – Crimes committed by Ravana"):
        text1 = """ 
        😴 Kumbhakarna ki Gehri Neend

Kuch samay baad,
Bhagwan ne Nidra (neend) ko bheja
Kumbhakarna ke paas.

Neend itni bhaari thi
ki Kumbhakarna ne Ravana se kaha:

“Bhai,
mujhe bahut neend aa rahi hai.
Mere liye ek surakshit jagah banao.”"""
        create_image_text_layout("attached_assets/chapter7/7.13.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        Ravana ne
shreshth shilpiyon ko bulaya.

Unhone ek vishal mahal banaya:

bahut lamba–chauda

heere aur sphaṭik ke farsh

sone ke stambh

shaant aur alag jagah

Wahin Kumbhakarna so gaya
aur hazaaron saalon tak nahi jaga 😴

😈 Ravana ka Andha Ghamand

Jab Kumbhakarna so raha tha,
tab Ravana ka ghamand badhne laga.

Usne:

Devtaon ko pareshaan kiya

Rishiyon ke tapasya-sthal tod diye

Yaksh aur Gandharvon ke udyan barbaad kar diye

Nadiyon ko uthaala,
ped giraye,
pahadon ko maara

Woh pagal haathi ki tarah
sab kuch ujaad raha tha.

✉️ Kubera ka Sandesh

Ravana ke bade bhai
Kubera (Dhanada)
yeh sab sun kar chintit hue.

Socha:

“Yeh mera bhai hai.
Main ise sambhalne ki koshish karoon.”

Kubera ne
ek doot (messenger) ko Lanka bheja.

🤝 Bibishana ka Achha Vyavhaar

Doot sabse pehle
Bibishana ke paas gaya.

Bibishana ne:

aadar se swagat kiya

bhai Kubera ka haal poocha

phir use Ravana ke darbar le gaya

👑 Darbar mein Sandesh

Ravana apne raaj-sinhāsan par tha.

Doot ne vinamrata se kaha:

“Yeh sandesh aapke bade bhai Kubera ka hai.”

Sandesh ka saar:

“Ravana, apne paapon ko roko”

“Dharma ka raasta apnao”

“Devta aur Rishi tumhare khilaaf yojna bana rahe hain”

“Main bhi kathor tapasya karke
Shiv ji ka mitra bana hoon”

“Apne vansh ko badnaam mat karo”

🔥 Ravana ka Krodh

Yeh sunte hi
Ravana ki aankhen laal ho gayi 😡

Usne daant pees kar kaha:

“Na tu mera bhai hai,
na woh jo tujhe bhejne wala hai!”

“Mujhe gyaan dene wala kaun hota hai Kubera?”

“Main apni shakti se
Teenon Lok jeet loonga!”

Aur phir…
sabse bhayanak paap hua 😢

🗡️ Doot ki Hatya

Ravana ne
ek hi vaar mein doot ko maar diya.

Aur uska sharir
dusht rakshason ko de diya.

Yeh rajdharma ka poora apmaan tha.

🌍 Teen Lok jeetne ka Ahankaar

Khoon se haath rang kar
Ravana apne rath par chadha.

Usne ghoshna ki:

“Ab main Kubera se bhi yuddh karunga!
Main sab Lok ka swami banunga!”

Aur ghamand mein
woh Teen Lok jeetne nikal pada.

🌱 Is Adhyay ka Sandesh (Moral)

Ghamand insaan ko andha bana deta hai

Achhi salah ko thukrana vinash laata hai

Doot ko maarna maha-paap hai

Ravana ka patan
yahin se shuru ho chuka tha"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.14
    with st.expander("Chapter 7.14 – Ravana fights the Yakshas"):
        text1 = """ 
        😈 Ravana ka Yuddh ke liye Nikalna

Ravana apni taakat par ghamand karke
apne 6 mantriyon ke saath nikla:

Mahodara

Prahasta

Marica

Shuka

Sarana

Dhumraksha

Sab ke mann mein sirf yuddh tha.
Aisa lag raha tha jaise Ravana
poori duniya jala dega 🔥"""
        create_image_text_layout("attached_assets/chapter7/7.14.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        🏔️ Mount Kailasha par Aagman

Ravana:

shehron se guzra

nadiyon ko paar kiya

jungle aur pahaad laanghe

Aur aakhir mein
Mount Kailasha pahunch gaya.

Wahan rehne wale Yaksha
use dekh kar dar gaye 😨

Unhone kaha:

“Yeh to hamare Raja ka bhai hai.”

Phir woh apne Raja
Kubera (Dhanada) ke paas gaye
aur Ravana ke iraadon ki khabar di.

⚔️ Yakshon ka Pratikar

Kubera ne anumati di.
Yaksha khushi aur veerta ke saath
yuddh ke liye nikal pade.

Jab dono senaayein takrayin,

pahaad kaanp uthe

zameen hil gayi

bhayankar yuddh chhid gaya

🔥 Ravana aur Uske Mantri

Ravana ne garaj kar sena ko utsaahit kiya.

Uske mantriyon ne:

har ek ne 1000 Yakshon ka saamna kiya

Hathiyaar chale:

gada

talwaar

lohe ke danda

barchhi

Yakshaon ke vaar
baarish ki tarah gir rahe the ☔

🪨 Marica ka Girna

Ek bhayanak Yaksha
Samyodhakantaka
tez gati se aaya.

Usne Marica par aisa vaar kiya
ki Marica gir pada,
jaise taara Kailasha se toot kar gir jaaye 🌠

Par Marica:

thodi der mein sambhal gaya

phir se yuddh mein kood pada

Yaksha haar kar bhaag gaya.

🚪 Ravana ka Dwaar Todna

Ravana khud
Yaksha nagar ke dwaar tak pahunch gaya.

Dwaar-rakshak ne use roka,
par Ravana ruka nahi 😤

Usne:

dwaar todna shuru kiya

Yaksha ne dwaar ka danda uthakar maara

Khoon behne laga,
par Ravana amar vardaan ke kaaran gira nahi.

Ulta Ravana ne:

wahi danda uthaya

Yaksha par zor se maara

Yaksha mitti ban kar gaayab ho gaya.

😱 Yakshon ki Haar

Yeh dekh kar
Yaksh sena mein bhagdad mach gayi.

Yaksha:

nadiyon mein kood gaye

gufaon mein chhup gaye

hathiyaar phenk diye

Dar se:

chehre bigad gaye

saans phool gayi

Yuddh ka maidaan
poori tarah shant ho gaya.

🌱 Is Adhyay ka Sandesh (Moral)

Ghamand se jeet mil sakti hai,
par shanti nahi

Shakti bina dharma ke
sirf bhay paida karti hai

Ravana jeeta zaroor,
par uska paap aur badh gaya"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.15
    with st.expander("Chapter 7.15 – Battle between Ravana and Kubera"):
        text1 = """ 
        👑 Dhanada ka Aadesh

Jab hazaaron Yaksha bhaagte hue dikhai diye,
to Dhanada (Kubera) ka mann dukhi ho gaya.

Unhone Manibhadra se kaha:

“O Yaksha Rajkumar,
iss paapi Ravana ko roko.
Hamare veer Yakshon ko bachao!”"""
        create_image_text_layout("attached_assets/chapter7/7.15.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        ⚔️ Manibhadra ka Pravesh

Manibhadra:

4000 Yakshon ke saath

poori shakti se yuddh mein kooda

Yaksha:

gada

bhala

talwar

lathi

chillaate hue bole:

“Aage badho!”
“Peeche mat hato!”
“Lado!”

Yuddh bahut bhayanak ho gaya 😨

🔥 Ravana ke Mantriyon ka Tandav

Prahasta ne 1000 Yaksh maar giraye

Mahodara ne aur 1000

Marica ne pal bhar mein 2000 Yaksh

Devta, Rishi, Gandharva
sab dekh kar hairaan reh gaye.

💥 Manibhadra vs Dhumraksha

Manibhadra aur Dhumraksha
aamne–saamne aaye.

Dhumraksha ne seene par bhala maara

Manibhadra hila tak nahi

Phir Manibhadra ne:

zor se vaar kiya

Dhumraksha behōsh hokar gir pada

😈 Ravana ka Seedha Hamla

Dhumraksha ko gira dekh
Ravana khud yuddh mein kood pada.

Manibhadra ne:

Ravana par 3 teer chalaaye

Ravana ne:

gada se vaar kiya

Manibhadra ka mukut tedha ho gaya

Isliye Manibhadra ka naam pada
“Parshvamauli” 👑➡️↘️

Aakhir Manibhadra bhi
yuddh se peeche hat gaya.

🗣️ Kubera ka Updesh

Ab Dhanada khud yuddh ke maidan mein aaye.

Unhone Ravana ko kaha:

“Tu meri baat nahi maanta.
Iska phal tujhe bhavishya mein milega.
Jo maa–baap, guru aur dharma ka
apmaan karta hai,
woh vinaash paata hai.”

“Paap se shakti mil sakti hai,
par sukh nahi.
Jaise beej boya jaata hai,
waisa hi phal milta hai.”

Phir Dhanada bole:

“Main aur baat nahi karunga.
Paapi se bas itna hi kehna kaafi hai.”

Yeh sun kar
Ravana ke kai mantri bhaag gaye.

🌪️ Antim Yuddh – Ravana vs Kubera

Ab sirf Ravana aur Dhanada.

Kubera ne Agni-astra chalaaya 🔥

Ravana ne Varuna-astra se roka 💧

Phir Ravana ne maya ka sahara liya:

kabhi sher bana

kabhi badal

kabhi pahad

kabhi samundar

Aakhir Ravana ne:

bhaari gada ghumayi

Kubera ke sir par zor se maari

Kubera behosh hokar gir pade,
jaise jad se kata hua ped 🌳💥

🌿 Kubera ka Bachav

Rishi Padma aur anya Rishi:

Kubera ko utha kar

Nandana van le gaye

🚀 Pushpaka Vimaan par Kabza

Ravana jeet gaya 😈

Usne:

Pushpaka Vimaan chheen liya

sunehre stambh

mani–moti

phal dene wale ped

har mausam mein sukh

Yeh Vimaan:

mann ke vichaar se tez

Vishvakarma ki rachna

devtaon ka vaahan

Ravana us par chadh kar sochne laga:

“Maine teenon lok jeet liye!”

🔥 Adhyay ka Sandesh (Moral)

Ghamand se jeet mil sakti hai,
par woh jeet tikti nahi

Dharma ke bina shakti vinaash laati hai

Ravana upar se jeeta,
par andar se aur andhera ho gaya"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.16
    with st.expander("Chapter 7.16 – How Ravana got his name"):
        text1 = """ 
        🚀 Pushpaka Vimaan ka Rukna

O Rama,
apne bhai Kubera ko haraane ke baad,
Rakshason ka raja Dashagriva
Pushpaka Vimaan par ghoom raha tha.

Ek din woh
sunehri ghaas se bhare ek vishaal jungle ke upar aaya.
Beech mein ek unchha pahad tha.

Jaise hi Vimaan pahad ke paas pahuncha,
achanak ruk gaya 😮

Ravana hairaan ho gaya."""
        create_image_text_layout("attached_assets/chapter7/7.16.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        Usne socha:

“Yeh kaise ho sakta hai?
Pushpaka to meri iccha se chalta hai!
Kya koi pahad ka vaasi ise rok raha hai?”

🗣️ Marica ka Uttar

Tab Marica bola:

“O Raja,
yeh Vimaan sirf Kubera ki seva karta hai.
Usse alag hone par
yeh apni shakti kho deta hai.”

🐒 Nandi ka Pravesh

Tab ek chhota, majboot, peela–kaala bauna prakat hua.
Uska naam tha Nandi —
Bhagwan Shiva ka sevak.

Nandi ne bina dare kaha:

“O Dashagriva, yahan se laut jao.
Is pahad par Mahadev vihar kar rahe hain.
Yahan Devta, Yaksha, Gandharva,
ya Rakshas kisi ko aana mana hai!”

😈 Ravana ka Ahankaar

Ravana gusse se hans pada 😤
Uski aankhen laal ho gayi.

Usne bola:

“Yeh Shankara kaun hai?
Main is pahad ko hi ukhaad dunga!”

Nandi ko
bandar-mukh dekh kar
Ravana zor se hasa.

🔮 Nandi ka Shaap

Nandi ka chehra kathor ho gaya.

Usne kaha:

“O Dashanana,
tumne mere roop ka mazaak udaaya.
Isliye bandar jaise veer janmenge,
jo tumhe aur tumhari jaati ko
nasht kar denge!”

“Main abhi tumhe maar sakta hoon,
par tumhara vinaash pehle hi likha ja chuka hai.”

Aasmaan se
phool barse 🌸
aur dev-vadya baj uthe.

🏔️ Ravana ka Ghor Apmaan

Ravana shaap ki parwah na karke
pahad ke paas gaya.

Ghamand mein bola:

“Main is pahad ko hi ukhaad dunga!”

Usne pahad ko baahon mein pakadkar
zor se hila diya.

Pahad kaanp utha 😱
Parvati dar ke maare
Shiva se chipak gayi.

👣 Mahadev ka Ek Angutha

Mahadev muskuraye 😊
aur sirf apna angutha
pahad par rakh diya.

Bas.

Ravana ki:

baahen pis gayi

haddiyan chubhne lagi

Woh dard se
bhayanak cheekh utha 😫

Us cheekh se:

teenon lok kaanp gaye

samundar uchhal pade

pahad hilne lage

🙏 Ravana ka Pashchatap

Devta aur mantri chillaye:

“Mahadev ko shaant karo!
Unke bina koi sharan nahi!”

Tab Ravana ne:

sir jhukaya

hazaar saal tak stuti ki

bhajan aur mantra gaye

🕉️ Ravana Naam ka Janm

Mahadev prasann ho gaye.

Unhone Ravana se kaha:

“Tumne dard mein jo cheekh maari,
usse teenon lok ro pade.”

“Isliye aaj se
tumhara naam hoga —
RAVANA
yani jo duniya ko rula de.”

Mahadev ne use:

ek divya talwar di
Chandrahasa ⚔️

aur lambi aayu ka vardaan diya

Par chetavani bhi di:

“Is talwar ka apmaan mat karna.
Varna yeh mere paas laut aayegi.”

🌍 Ravana ka Andha Safar

Naam aur vardaan paakar
Ravana aur bhi ghamandi ho gaya.

Pushpaka Vimaan par baith kar
woh poori duniya ghoomne laga.

Jo jhuk gaye — bach gaye.
Jo nahi jhuke —
nasht ho gaye.

📜 Is Adhyay ka Sandesh (Moral)

Ahankaar se shakti badhti lagti hai,
par ant kareeb aa jaata hai

Devta daya dete hain,
par ghamand kabhi maaf nahi hota

Ravana ka naam shaktishaali bana,
par uska vinaash bhi usi mein chhupa tha"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.17
    with st.expander("Chapter 7.17 – Story of Vedavati"):
        text1 = """ 
        🌲 Himalaya ke Van mein

O Raja,
jab Ravana duniya bhar mein ghoom raha tha,
woh Himalaya ke ghane jungle mein pahuncha.

Wahan usne ek yuva ladki dekhi.
Woh devta si chamak wali thi ✨

kaale hiran ki khal pehne

jataa (bikhre baal)

aur tapasya ka jeevan jee rahi thi."""
        create_image_text_layout("attached_assets/chapter7/7.17.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        😈 Ravana ka Ghamand

Us sundar ladki ko dekh kar
Ravana ka mann bigad gaya.

Hans kar bola:

“O Sundari,
itni chhoti umar mein yeh kathor jeevan kyun?
Tumhari sundarta tapasya mein kyun chhupi rahe?”

“Tum kaun ho?
Kis ki beti ho?
Tumhara pati kaun hai?”

🕊️ Vedavati ka Sach

Ladki ne shant swar mein kaha:

“Mera naam Vedavati hai.”

“Mere pita Kushadhwaja the,
ek mahaan Brahmarishi.
Unhone Vishnu ko mera pati chuna tha.”

“Kai Devta, Gandharva,
aur Rakshas mere liye aaye,
par pita ne mana kar diya.”

“Is par Shumbha naam ke Daitya ne
mere pita ko raat mein maar diya 😔
Maa ne unke saath agni mein pravesh kar liya.”

“Ab main sirf Narayana (Vishnu) ke liye tapasya kar rahi hoon.
Woh hi mere swami hain.”

“Ravana, tum mujhe jaante nahi.
Main apni tapasya se
teenon lok ka gyaan rakhti hoon.”

🔥 Ravana ka Apmaan

Ravana ne phir bhi kaha:

“Vishnu kaun hai?
Main Lanka ka Raja hoon!
Mujhse shaadi karo,
saare sukh milenge!”

Vedavati gusse se boli:

“Sharam karo!
Vishnu teenon lok ke swami hain.
Unka apmaan sirf tum jaise ghamandi karte ho!”

⚔️ Antim Apmaan

Ravana ne
Vedavati ke baal pakad liye 😡

Vedavati ne:

apna haath talwar bana liya

apne baal khud kaat diye

Aag jalakar boli:

“Tumhare sparsh se main ashuddh ho gayi hoon.
Main jeevit nahi rahungi!”

“Main tumhe shraap nahi dungi,
kyunki meri tapasya nasht ho jaayegi.”

“Par agar meri tapasya sachchi hai,
toh main phir janm loongi,
aur tumhara vinaash karungi!”

🔥 Agni mein Pravesh

Yeh kehkar
Vedavati ne agni mein kood kar praan tyag diye 🔥

Turant:

phoolon ki baarish hui 🌸

devta prasann hue

🌸 Punarm Janm ka Rahasya

O Rama,
Vedavati hi baad mein:

Janak ke ghar janmi

Sita ke roop mein 🌼

Woh:

pehle Satya Yug mein Vedavati thi

phir Treta Yug mein Sita bani

Aur tum, Rama,
khud Vishnu ho.

Vedavati ka balidaan
hi Ravana ke ant ka kaaran bana.

📜 Is Kahani ka Sandesh (Moral)

Pavitrata aur bhakti kabhi nasht nahi hoti

Ahankaar aur kaam ant mein vinaash laate hain

Nari ka apmaan hi Ravana ke patan ki jad bana

Sachchi tapasya anyaay ka ant karti hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.18
    with st.expander("Chapter 7.18 – Gods hide in fear of Ravana"):
        text1 = """ 
        🔥 Vedavati ke balidaan ke baad

Vedavati ke agni mein pravesh karne ke baad,
Ravana phir se apne Pushpaka Vimaan par chadh kar
poori dharti par ghoomne laga.

Ek din woh Ushirabija naam ke sthal par pahuncha,
jahaan Raja Marutta ek maha-yagya kar rahe the.

Is yagya mein:

Devta khud upasthit the

Samvarta Rishi (Brihaspati ke bhai) yagya karwa rahe the"""
        create_image_text_layout("attached_assets/chapter7/7.18.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        😨 Devtaon ka Bhay

Ravana ko dekhte hi devta kaanp uthe.

Unhe pata tha:

Ravana ko boon mil chuke hain

Woh apavitra aur nirdayi hai

Yagya bigaad sakta hai

👉 Isliye devtaon ne apni raksha ke liye jaanwaron ke roop le liye:

Devta	Roop
Indra	🦚 Mor (Peacock)
Yama (Dharmaraja)	🐦 Kauwa (Crow)
Kuvera	🦎 Girgit (Chameleon)
Varuna	🦢 Hans (Swan)

Baaki devta bhi kisi na kisi roop mein chhup gaye.

🐕 Ravana ka Apmaan

Devta bhag gaye,
aur Ravana yagya-sthal mein gande kutte ki tarah ghus gaya.

Usne Raja Marutta se kaha:

“Lado ya mere aage jhuk jao!”

Raja Marutta bole:

“Tum kaun ho?”

Ravana hans kar bola:

“Main Ravana hoon!
Kuvera ka chhota bhai!
Jisne apne bhai ko hara kar
Pushpaka Vimaan chheen liya!”

⚔️ Raja Marutta ka Dharm

Raja Marutta gusse mein bole:

“Apne bhai ko hara kar ghamand karta hai?
Yeh koi veerta nahi!”

“Main abhi tumhe apne teeron se maar dunga!”

Raja ne dhanush utha liya,
par Guru Samvarta Rishi ne roka:

“Yagya adhoora reh gaya toh
tumhari vansh ka naash ho jayega.”

“Yagya karte samay
krodh aur yuddh mana hai.”

Raja Marutta ne:

dhanush chhod diya

shant ho gaye

yagya poora kiya

🩸 Ravana ka Paap

Ravana ne isse:

apni jeet maana

aur ghoshna karwa di

“Ravana vijayi hai!”

Uske baad:

usne wahan maujood Rishiyon ko maar diya

unka rakht peeya

aur phir dharti par ghoomne chala gaya 😔

🌈 Devtaon ke Vardaan (Boons)

Ravana ke jaane ke baad
devta apne-apne roop se bahar aaye.

Khushi mein unhone un jaanwaron ko vardaan diye:

🦚 Indra → Mor

Mor ke pankhon mein 1000 aankhen aayi 👁️

Saanp mor ko nuksaan nahi pahuncha sakte

Baarish mein mor nachta hai ☔

👉 Isi wajah se mor ke pankh itne rang-birange hote hain.

🐦 Yama → Kauwa

Kauwa:

lambi aayu paata hai

rog kam hote hain

Kauwa jab khata hai,
pitar (purvaj) bhi tript hote hain

🦢 Varuna → Hans

Hans:

poora shwet (white) ho gaya 🤍

pehle pankhon ke kinare kaale hote the

Paani mein rehkar usse anand milta hai

🦎 Kuvera → Girgit

Girgit ke sir par sona jaisa rang aa gaya ✨

Yeh Kuvera ki kripa ka chihn hai

📜 Is Adhyay ka Sandesh (Moral)

Adharm se prapt shakti bhay paida karti hai

Devta bhi adharmi se bachne ke liye chhup jaate hain

Yagya aur dharm krodh se bade hote hain

Prakriti ke rang aur gun bhi dharm ka phal hain

Ravana ka har kadam uske ant ko aur paas la raha tha"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.19
    with st.expander("Chapter 7.19 – Ravana fights King Anaranya"):
        text1 = """ 
        🌪️ Ravana ka Ghamand

Marutta ko hara kar,
Ravana aur zyada ghamandi ho gaya.

Woh shehron-shehron ghoomta raha.
Har raja se ek hi baat bolta:

“Ya to mujhse lado,
ya haar maan lo.”

Bahut se samajhdaar raja the.
Unhone socha, samjha,
aur Ravana ki shakti dekh kar bole:

“Hum haar gaye.”

Ravana aur zyada ghamand mein aa gaya."""
        create_image_text_layout("attached_assets/chapter7/7.19.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        🏰 Ayodhya mein Chunauti

Phir Ravana pahuncha Ayodhya.
Wahan ke raja the Anaranya.
Bahut veer. Bahut dharmic.

Ayodhya utni hi majboot thi
jitni Amaravati devtaon ki nagri.

Ravana bola:

“Mujhse yuddh karo
ya haar maan lo!”

Raja Anaranya ko gussa aaya.
Unhone shant par dridh awaaz mein kaha:

“Main yuddh sweekar karta hoon.
Tum bhi taiyaar ho jao.”

⚔️ Bhayankar Yuddh

Raja Anaranya apni poori sena ke saath nikle:

hazaaron rath

lakhon ghode

das hazaar haathi

aur anek sainik

Zameen kaanp uthi.
Yuddh shuru ho gaya.

Lambe samay tak ladaai hui.
Par Ravana ki sena aag jaise thi.
Anaranya ki sena
jalti hui agni mein ghee jaise sama gayi.

Dheere-dheere
poori sena nasht ho gayi 😔

🏹 Raja Anaranya ka Antim Sangharsh

Apni sena ko khoya dekh kar,
Raja Anaranya ne dhanush uthaya.

Unhone 800 teer chhode.
Par Ravana par
ek bhi ghaav nahi laga.

Phir Ravana ne ek bhaari prahar kiya.
Raja Anaranya rath se gir pade.
Zameen par gir kar
saans mushkil ho gayi.

Ravana hans kar bola:

“Mujhse lad kar kya mila?
Teenon lokon mein
koi mujhe hara nahi sakta!”

🕯️ Dharmic Raja ke Antim Vachan

Raja Anaranya ne dheere se kaha:

“Mujhe tumne nahi haraya.
Samay (Time) ne mujhe haraya.”

“Par ek baat yaad rakhna, Ravana.”

Unki awaaz kamzor thi,
par vachan majboot tha:

“Ikshvaku vansh mein
ek balak janm lega.”

“Uska naam hoga – Rama.”

“Wahi tumhara ant karega.”

Jaise hi yeh vachan bole gaye,

aakash se phool barse 🌸

dev dundubhi baj uthi

Raja Anaranya
swarg lok chale gaye.

🌱 Kahani ka Sandesh (Moral)

Ghamand se shakti andhi ho jaati hai

Adharm jeet sakta hai, par bach nahi sakta

Dharmic vachan kabhi vyarth nahi jaate

Ravana ka ant likha ja chuka tha

Ram ka janm pehle hi nirdharit tha"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.20
    with st.expander("Chapter 7.20 – Ravana meets Sage Narada"):
        text1 = """ 
        ☁️ Achanak Mulakaat

Ravana prithvi par ghoom raha tha.
Har jagah darr faila raha tha.

Tab usne dekha —
Rishi Narada,
baadal par sawar,
akash mein chamakte hue ✨

Ravana ne turant vinamrata dikhayi.
Pranam kiya.
Aur poocha:

“Maharshi, aap yahan kaise?”"""
        create_image_text_layout("attached_assets/chapter7/7.20.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        🪶 Narada ka Shant Updesh

Narada muskuraaye.
Unki awaaz shaant thi,
par gehri.

Unhone kaha:

“O Dashagriva,
tumhare parakram se
devta bhi hile hue hain.”

“Tumne Gandharvon,
Nagas aur auron ko haraya.
Yeh sab mujhe pata hai.”

Phir Narada ne dheere se kaha:

“Par ek baat socho.”

🌍 Narada ka Prashn

Narada bole:

“Is manushya lok ko
kyun sata rahe ho?”

“Yeh duniya pehle hi
dukh se bhari hai.”

“Log budhaape,
bhookh, pyaas,
rog aur shokh se peedit hain.”

“Kahin naach–gaana hai,
kahin aansu aur cheekh.”

“Koi maa ke moh mein bandha,
koi patni aur bachchon ke.”

“Jo duniya pehle hi kamzor hai,
usey satana
kis veerata ka kaam hai?”

⚖️ Maha Salah

Narada ne gehri baat kahi:

“Agar sach mein
sab par vijay chahte ho…”

“Toh Yama ko harao.”

“Mrityu ko jeet lo.”

“Jab maut jeet li,
tab samjho
poora sansaar jeet liya.”

😈 Ravana ka Ghamandi Hasna

Narada ki baat sun kar,
Ravana zor se hansa 😈
Jaise badal garaj uthe.

Usne kaha:

“Maharshi!
Main Rasatal jaunga.”

“Devta, Nag,
sab ko jhukaa dunga.”

“Phir amrit ke liye
samudra manthan bhi karunga!”

Phir aur aage badh kar bola:

“Main Yama se ladne ja raha hoon.”

“Dakshin disha mein,
Surya putra Yama ke nagar tak.”

“Main chaaron
Lokpalon ko bhi haraunga!”

🌑 Yama se Yuddh ka Sankalp

Ravana ne garaj kar kaha:

“Mrityu ka ant kar dunga!”

“Sabko rulaane wale Yama ko
khud rone par majboor karunga!”

Yeh kehkar Ravana
apne mantriyon ke saath
dakshin disha ki taraf nikal gaya.

🔥 Narada ka Manan

Narada wahi ruk gaye.
Gehri soch mein doob gaye.

Unka tej
dhuaan rahit agni jaise tha 🔥

Unhone socha:

“Mrityu ko kaun hara sakta hai?”

“Jo devtaon ko bhi
niyam mein rakhta hai.”

“Jo har jeev ke karm ka
hisaab karta hai.”

“Agar Yama hara diya gaya,
toh sansaar ka niyam
kaise chalega?”

Narada ke mann mein jigyaasa jaagi:

“Main khud Yama lok jaa kar
yeh yuddh dekhunga.”

🌱 Kahani ka Sandesh (Moral)

Ghamand buddhi ko andha kar deta hai

Jo mrityu ko chunauti de,
woh apne ant ko nazdeek laata hai

Narada jaise gyaani
shant hote hain,
par sach bolte hain

Adharm jitna bhi upar uthe,
girna uska niyam hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.21
    with st.expander("Chapter 7.21 – Ravana challenges Yama"):
        text1 = """ 
        Narada ji ne mann mein socha—
“Yeh baat Yama Dev ko batani zaroori hai.”
Aur woh halka kadam rakhte hue
Yama ke lok ki taraf chale gaye.

Wahan Yama
agni ke paas baithe the.
Woh har jeev ko
uske karm ke hisaab se
nyay de rahe the.

Yama Dev ne Narada ji ko dekha.
Unhe aasan diya.
Arghya diya.
Aur pyaar se poocha—"""
        create_image_text_layout("attached_assets/chapter7/7.21.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        “Hey Devarishi,
sab kushal toh hai?
Dharma theek chal raha hai na?
Tum yahan kyun aaye ho?”

Narada ji ne shaant swar mein kaha—

“Yama Dev,
main ek chinta ki baat lekar aaya hoon.
Dashagriva, jise log Ravana kehte hain,
yahaan aa raha hai.
Woh apni ichchha ki shakti se
tumhe chunauti dena chahta hai.”

Itna sunte hi,
door se ek chamak dikhai di.
Suraj jaise tej wala
Pushpak Vimaan aage badh raha tha.

Woh tha Ravana.

Uska tej
mrityu-lok ke andhkaar ko bhi
hata raha tha.

Ravana ne charon taraf dekha.
Usne dekha—
kuch log apne achhe karm ka phal pa rahe hain.
Aur kuch log
apni galtiyon ka bojh mehsoos kar rahe hain.

Kahin shaanti thi.
Kahin peeda.
Har jagah ek hi niyam tha—
jaise karm, waisa phal.

Ravana ne ghamand mein aakar
kuch peedit atmaon ko
bandhan se mukt kar diya.

Isse Yama ke sainik
chaukannay ho gaye.
Unhone nyay ki raksha ke liye
aage badhna shuru kiya.

Yama ki sena aur Ravana ke saathi
aamne-saamne aa gaye.
Aakash goonj utha.
Par Pushpak Vimaan
Brahma ji ke vardaan se
phir se surakshit ho gaya.

Yuddh tez hota gaya.
Ravana akela hi
kaiyon ka saamna kar raha tha.
Uske sharir par chot thi,
par uska ahankaar aur bhi bada tha.

Aakhir Ravana
zameen par aa khada hua.
Uski aankhon mein krodh tha.
Usne ek divya astra uthaya
aur zor se bola—

“Ruko! Sab ruko!”

Astra chhodte hi
aag aur roshni phail gayi.
Yama ki sena
peeche hatne lagi.

Ravana aur uske saathi
garjana karne lage.
Prithvi kaanp uthi.

Moral (Soft Message):
Har lok mein ek niyam hota hai—
karma ka niyam.
Ghamand aur shakti
agar dharma se alag ho jaaye,
to woh sirf vinaash ka raasta dikhati hai.
Sachchi mahaanta
nyay, maryada aur santulan mein hoti hai 🌼"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.22
    with st.expander("Chapter 7.22 – Duel between Ravana and Yama"):
        text1 = """ 
        Zor-zor ki awaaz sunkar
Yama samajh gaye—
unki sena haar chuki hai.

Unki aankhen laal ho gayin.
Gussa saaf dikh raha tha.

Yama ne apne saarathi se kaha—
“Jaldi rath le chalo.
Mujhe khud aage jaana hoga.”

Divya rath taiyaar hua.
Yama us par chadh gaye.
Unke saath Mrityu aur Kaal bhi the.
Unke hathiyaar aag jaise chamak rahe the."""
        create_image_text_layout("attached_assets/chapter7/7.22.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        Teenon lok kaanp uthe.
Devta bhi darr gaye.
Aisa lag raha tha
jaise samay khud chal pada ho.

Jab Yama ka bhayanak rath
yuddh-sthal ke paas aaya,
to Ravana ke saathi
darr ke maare bhaag gaye.

Par Ravana
bilkul nahi hila.
Uske mann mein
na darr tha,
na sankoch.

Yama ne paas aakar
apne astra chhode.
Ravana par kai baan lage.
Par Ravana bhi chup nahi raha.

Usne bhi
teer-par-teer chala diye.
Aakash bhar gaya
teekhi chamak se.

Saat din tak
yeh sangharsh chalta raha.
Na koi peeche hataa,
na koi jhuka.

Sab devta,
gandharva,
rishi—
sab dekh rahe the.
Unhe laga
jaise duniya ka ant ho raha ho.

Ravana ne
apne dhanush ko kheench kar
poore aakash ko
teeron se bhar diya.

Yama bhi
krodh se bhar gaye.
Unke mukh se
aag aur dhuan nikla.

Mrityu ne kaha—
“Is Rakshasa ko
ab ant milna hi chahiye.
Meri drishti se
koi bhi jeev
zinda nahi reh sakta.”

Yama ne bhi
apna maha-dand utha liya.
Woh dand
kabhi nishana nahi chookta.

Par tabhi—
achanak—
Brahma
wahan prakat hue.

Brahma ji ne shaant swar mein kaha—

“Yama,
ruk jao.
Is par maine vardaan diya hai.
Mera vachan
jhootha nahi hona chahiye.”

“Ye dand agar gira,
to sirf Ravana hi nahi,
poora jagat nash ho jaayega.”

“Isliye isse hata lo.
Dharma ka rakshan karo.”

Yama ne
Brahma ji ki baat maani.
Unhone kaha—

“Main apna dand rok leta hoon.
Par phir
main is yuddh se
adrishya ho jaata hoon.”

Yeh keh kar
Yama apne rath ke saath
gaayab ho gaye.

Ravana ne
apna naam zor se pukara.
Pushpak Vimaan par chadha
aur Yama-lok se
bahar nikal gaya.

Devta,
Brahma ji aur Narada ji
shanti se
swarg lok laut gaye.

Moral (Soft Message):

Kabhi-kabhi
bohot zyada shakti bhi
niyam ke aage ruk jaati hai.
Vardaan, vachan aur dharma
sabse upar hote hain.
Aur bina dharma ke
jeet bhi
poori nahi hoti 🌼"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.23
    with st.expander("Chapter 7.23 – Ravana fights Varuna’s sons"):
        text1 = """ 
        Yama se saamna karne ke baad
Ravana
apne saathiyon ko dhoondhne nikla.

Uska sharir ghayal tha.
Khoon laga hua tha.
Par uski aankhon mein
abhi bhi ghamand chamak raha tha.

Marich aur baaki saathi
use dekh kar hairaan reh gaye.
Unhone Ravana ko badhai di
aur sab Pushpak Vimaan mein baith gaye."""
        create_image_text_layout("attached_assets/chapter7/7.23.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        Ravana ab
jal-lok ki taraf gaya.
Yeh wo jagah thi
jo Varuna
ke rakshan mein thi.

Wahan Naag aur Daitya rehte the.
Ravana Bhogavati nagari pahuncha,
jahan Naagraj Vasuki ka raj tha.

Usne Naagon ko jeet liya
aur ratnon se bani nagari mein
ghamand se ghus gaya.

Aage
Nivatakavacha Daitya rehte the.
Unhe Brahma ka vardaan mila hua tha.

Ravana ne unhe yuddh ki chunauti di.
Daitya khush ho kar
hathiyaar utha laaye.

Rakshas aur Daitya
saal bhar tak ladte rahe.
Na koi jeeta,
na koi haara.

Aakhir
Brahma
khud prakat hue.

Brahma ji ne shaant swar mein kaha—

“Tum dono ko
koi poori tarah nahi hara sakta.
Isliye shatru nahi,
mitra bano.”

Ravana aur Nivatakavacha
aag ke saamne
mitrata mein bandhe.

Ravana kuch samay
wahi raha.
Usne maya aur vidya seekhi
aur phir aage badha.

Ab Ravana
Rasatala gaya.
Wahan Varuna ki rajdhani
Ashma nagari thi.

Ravana ne wahan yuddh kiya.
Phir usne
Varuna ke lok ki taraf badhna shuru kiya.

Usne Surabhi Gau ko dekha—
jisse amrit aur doodh ka sagar banta hai.
Ravana ne uska chakkar lagaya
aur aage badh gaya.

Usne Varuna ke sainikon ko
sandesh bheja—

“Apne raja ko batao,
Ravana aaya hai.
Yuddh sweekaar karo,
ya haar maan lo.”

Yeh sunkar
Varuna ke putra aur pautra
rath le kar aa gaye.

Aakash mein
bhayankar yuddh hua.
Kabhi Ravana bhaari padta,
kabhi Varuna ke putra.

Kuch der ke liye
Ravana peeche hat gaya.
Par uske saathi
Mahodara ne
Varuna ke putron ke rath gira diye.

Fir se ghor yuddh hua.
Aakhir Varuna ke putra
thak gaye aur gir pade.

Ravana zor se bola—

“Yeh sandesh Varuna tak pahuncha do!”

Tab Varuna ke mantri Prahasta ne kaha—

“Varuna dev yahan nahi hain.
Woh Brahmalok gaye hain
Gandharva sangeet sunne.”

Yeh sunkar
Ravana ne apna naam ghoshit kiya.
Ghamand bhari hasi hasi.
Aur Pushpak Vimaan mein baith kar
Lanka ki taraf laut gaya.

Moral (Soft Message):

Jeet agar sirf ghamand se ho,
to woh jeet poori nahi hoti.
Sachchi mahaanta
sanyam, maryada aur samajh se aati hai.
Aur jo har jagah yuddh dhoondhta hai,
use ant mein
sirf thakaan milti hai 🌼"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.23b
    with st.expander("Chapter 7.23b – Ravana meets Bali"):
        text1 = """ 
        Yuddh ke nashe mein doobe hue
Ravana ke sainik
Ashma nagari mein ghoomne lage.

Ravana ne wahan
ek adbhut mahal dekha.
Hare-bhare panna,
motiyon ke jaal,
sunehre stambh,
aur heere-jare seedhiyan.
Woh mahal
Indra ke lok jaisa lag raha tha.

Ravana ne socha—
“Yeh itna sundar mahal
kis ka ho sakta hai?”

Usne Prahasta ko bheja—
“Jaakar pata lagao.”"""
        create_image_text_layout("attached_assets/chapter7/7.23b.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        Prahasta andar gaya.
Ek ke baad ek
saath kamre paar kiye.
Aakhir ek aag jalti hui dikhi.

Us aag ke beech
ek vyakti baitha tha.
Woh zor-zor se hans raha tha.
Uska tej suraj jaisa tha.

Prahasta darr gaya
aur turant laut aaya.
Usne sab Ravana ko bata diya.

Ravana khud andar jaane laga.
Tab darwaaze par
ek bhayanak roop wala vyakti khada tha.
Uski aankhen laal,
jeebh aag jaisi,
aur haath mein gada thi.

Ravana ka dil tez dhadakne laga.
Uska sharir kaanp gaya.

Us vyakti ne kaha—
“Ruk kyun gaye, Rakshasa?
Batao, kya chahte ho?”

Phir usne poocha—
“Kya tum Bali se yuddh karna chahte ho?”

Ravana sambhal kar bola—
“Is mahal ka swami kaun hai?”

Vyakti ne kaha—

“Yahan Bali rehta hai.
Woh mahaan hai.
Veer hai.
Satya par chalne wala hai.
Usse koi hara nahi sakta.”

“Agar yuddh chahte ho,
to andar jao.”

Ravana andar gaya.
Bali ko dekha.
Bali aag jaise chamak rahe the.

Bali ne hans kar
Ravana ko apni godi mein bithaya
aur kaha—

“Batayo, Lanka ke raja,
yahaan kyun aaye ho?”

Ravana bola—
“Maine suna hai
tum kabhi bandhan mein the.
Main tumhe chhuda sakta hoon.”

Bali zor se hansa.
Aur bola—

“Ravana,
jisne mujhe bandha,
use koi nahi hara sakta.”

“Darwaaze par jo khada hai,
wahi sab ka malik hai.”

“Woh samay hai.
Woh srishti hai.
Woh vinaash bhi hai.”

“Devta, Daitya,
sab uske adheen hain.”

Bali ne kaha—

“Bahut se mahaan veer
ghamand mein aa kar
uske saamne gire hain.”

Phir Bali ne ek
chamakta hua chakra dikhaya.

“Kya tum ise utha sakte ho?”
usne poocha.

Ravana ne socha—
“Yeh toh aasaan hai.”

Par jaise hi usne uthaya,
woh chakra hila tak nahi.

Ravana ne poori taakat lagayi.
Par agle hi pal
woh zameen par gir pada.
Behosh ho gaya.

Thodi der baad
Ravana hosh mein aaya.
Sharm se uska sir jhuk gaya.

Bali ne pyaar se kaha—

“Yeh chakra
us bhagwan ka hai
jo Hiranyakashipu ko bhi
hara chuka hai.”

“Wahi
darwaaze par khada tha.”

Tab Bali ne us bhagwan ka naam liya—

Vishnu
Hari, Narayana, Nrsingha.

“Wahi
srishti karta hai,
palta hai,
aur samay par vinaash bhi.”

“Jo use jaanta hai,
woh paap se mukt hota hai.”

Yeh sab sunkar
Ravana aur bhi gusse mein aa gaya.
Usne hathiyaar utha liye.

Par bhagwan Hari ne socha—
“Brahma ke vachan ke kaaran
main ise abhi nahi maarunga.”

Aur woh adrishya ho gaye.

Ravana ne dekha
ki koi saamne nahi hai.
Usne khushi mein naara lagaya
aur Lanka ki taraf
laut gaya.

Moral (Soft Message):

Sirf shakti aur ghamand
sab kuch nahi hota.
Kuch shaktiyan
samajh aur vinamrata se pehchaani jaati hain.

Jo apni seema samajh leta hai,
wahi sach mein mahaan hota hai 🌼"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.23c
    with st.expander("Chapter 7.23c – Ravana challenges the Sun"):
        text1 = """ 
        Thoda sochne ke baad
Ravana
Surya-lok ki taraf chal pada.

Raat usne
Sumeru Parvat ki choti par bitayi.
Subah hote hi
Pushpak Vimaan mein baith kar
aage badha.

Vimaan
suraj ke ghodon jitni tezi se
chal raha tha."""
        create_image_text_layout("attached_assets/chapter7/7.23c.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        Tab Ravana ne
chamakte hue Surya ko dekha.
Hazaar kirnon se chamakta hua.
Sone ke gehne,
laal kamal ki mala,
aur laal chandan se
shobhit sharir.

Surya Dev
poore jagat ko
pavitra kar rahe the.

Surya ki roshni
itni tez thi
ki Ravana bhi
kuch pal ke liye
dab sa gaya.

Usne Prahasta se kaha—

“Jaakar Surya Dev ko batao—
Ravana yahan aaya hai.
Ya to yuddh karein,
ya haar sweekaar karein.”

Prahasta aage badha.
Surya ke dwaar par
do dwarpaal the—
Pingala aur Dandi.

Sandesh sun kar
Dandi ne Surya Dev ko bataya.

Surya Dev shaant rahe.
Unhone sirf itna kaha—

“Dandi,
jaakar Ravana se keh do—
ya to mujhe jeeto,
ya keh do ki main haar gaya.
Jo theek lage, karo.”

Dandi ne
yeh sandesh Ravana tak pahuncha diya.

Surya ki kirnen
abhi bhi tez thi.
Ravana unke saamne
aur aage badh nahi paaya.

Usne door se hi
nagaade bajwa diye.
Aur apni jeet ka
elan kar diya.

Phir woh
Pushpak Vimaan mein baitha
aur wahan se
laut gaya.

Moral (Soft Message):

Kabhi-kabhi
insaan apni shakti se
prakriti ko bhi chunauti de deta hai.
Par asli tej
shor se nahi,
shaanti aur niyam se pehchaana jaata hai 🌼"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.23d
    with st.expander("Chapter 7.23d – Ravana meets King Mandhata"):
        text1 = """ 
        Raat Sumeru Parvat par bitakar
Ravana
chandralok ki taraf badha.
Uske mann mein
ab bhi yuddh ka josh tha.

Wahan usne
ek chamakta hua rath dekha.
Apsaraon se ghira hua.
Sangeet aur nritya se bhara hua.

Ravana ko jigyasa hui.
Usne paas khade rishi Parvata se poocha—

“Yeh kaun hai
jo bina darr ke
aise aage badh raha hai?”

Rishi Parvata ne shaant swar mein kaha—"""
        create_image_text_layout("attached_assets/chapter7/7.23d.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        “Putra,
yeh sab raja hain
jo apne karm ke phal bhogne
swarg ki yatra par ja rahe hain.

Jaise tumne tapasya se
shakti paayi hai,
waise hi inhone bhi
dharm aur daan se
apna sthaan kamaya hai.”

Ravana ne phir poocha—

“Kya inmein se koi
mujhe yuddh ka sukh dega?”

Rishi bole—

“Yeh sab swarg chahte hain,
yuddh nahi.
Par ek raja hai
jo tumhara saamna karega.”

“Uska naam hai
Mandhata.
Saat dweep ka swami.
Ayodhya ka mahaan raja.”

Thodi hi der mein
Ravana ne Mandhata ko dekha.
Sunehra rath.
Divya tej.
Shaant par veer chehra.

Ravana ne garv se kaha—

“Raja Mandhata,
mujhse yuddh karo!”

Mandhata hans pade.
Aur bole—

“Agar jeevan pyaara nahi,
to saamne aao, Rakshasa.”

Ravana ne ghamand se kaha—

“Main Varuna, Yama aur Kuvera se nahi dara.
Phir ek manushya se kyun darun?”

Aur yuddh shuru ho gaya.

Mandhata ne
apne teeron se
Rakshaso ki sena ko
rok diya.
Jaise aag
sookhi ghaas ko jala deti hai.

Unhone Ravana ke rath par
gada se prahaar kiya.
Ravana gir pada.
Behosh ho gaya.

Rakshas darr gaye.

Par thodi der mein
Ravana sambhal gaya.
Usne phir se yuddh chhed diya.

Mandhata bhi uth khade hue.
Unka tej
suraj jaisa chamak utha.

Dono taraf se
divya astron ka prayog hone laga.
Puri srishti
kaamp uthi.

Tab do mahaan rishi—
Paulastya aur Galava—
wahan prakat hue.

Unhone prem se kaha—

“Bas karo.
Yeh yuddh
sirf vinaash laayega.”

Unki baat sunkar
Ravana aur Mandhata
shaant hue.

Dono ne
yuddh rok diya.
Aur apne-apne raaste
laut gaye.

Moral (Soft Message):

Shakti aur veerata
tabhi sundar hoti hai
jab uske saath
sanyam aur vivek ho.

Jo samay par
talwar rakh de,
wahi sach mein
mahaan veer hota hai 🌼"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.23e
    with st.expander("Chapter 7.23e – Ravana visits the Moon world"):
        text1 = """ 
        Do rishiyon ke jaane ke baad,
Ravana
aakash ke aur upar badhne laga.

Woh hazaaron yojan door
alag-alag divya lokon se guzra.
Kahin hans rehte the,
kahin Siddha aur Charan,
kahin Ganga ka pavitra jal
aakash se beh raha tha.

Har lok shant tha.
Har jagah niyam aur maryada thi."""
        create_image_text_layout("attached_assets/chapter7/7.23e.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        Aakhir Ravana
us lok mein pahuncha
jahan Chandra
virajmaan the.

Chandra Dev
taaron se ghire hue the.
Unki shital roshni
sab jeevon ko sukh deti thi.

Par jaise hi Ravana wahan aaya,
chandramā ki thandi kirnein
aag jaisi lagne lagi.

Ravana ke saathi
kampne lage.
Prahasta ne kaha—

“Rajaji,
yeh thandi roshni
jalane wali hai.
Humein yahan se nikalna chahiye.”

Par Ravana
krodh se bhar gaya.
Usne dhanush uthaya
aur Chandra Dev par
baan chalaane laga.

Tab achanak
Brahma
wahan prakat hue.

Brahma ji ne
shaant aur gambhir swar mein kaha—

“Ravana,
bas karo.
Chandra sabka kalyan chahte hain.
Unhe peeda mat do.”

“Main tumhe
ek divya vardaan deta hoon.
Ek pavitra mantra.”

“Is mantra ko
roz nahi,
sirf tab japna
jab tumhari jaan khatre mein ho.”

“Rudraksha mala haath mein lekar
iska smaran karna.
Tab tumhe koi hara nahi paayega.
Par bina smaran ke
safalta nahi milegi.”

Ravana ne
haath jod kar kaha—

“Prabhu,
agar main aapko priya hoon,
to mujhe yeh mantra de dijiye.
Isse main
devon ke bhay se
mukt ho jaunga.”

Brahma ji ne
us pavitra mantra ke
108 naam sunaye—
jo Ishwar ke
anek roopon ka varnan karte the.

Unhone kaha—

“Jo in naamon ka
shraddha se smaran karega,
uske paap nasht honge.
Use sharan milegi.
Aur jeevan ke yuddh mein
sahi disha milegi.”

Ravana ne
mantra suna.
Uska ghamand
thoda shaant hua.

Woh wahan se
laut gaya.
Par uske haath mein
ab shakti ke saath
ek yaad bhi thi—
ki shakti ke upar bhi
niyam hota hai.

Moral (Soft Message):

Sirf taakat se
sab kuch nahi jeeta jaata.
Kabhi-kabhi
kripa aur niyam
shakti se bhi bade hote hain.

Aur jo shakti ko
maryada ke saath rakhe,
wahi sach mein
surakshit rehta hai 🌙"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.23f
    with st.expander("Chapter 7.23f – Ravana meets the Maha-Purusha"):
        text1 = """ 
        Brahma ji se vardaan paakar
Ravana
apne raaste par aage badh gaya.

Kuch din baad
woh pashchim samudra ke kinaare pahuncha.
Ek tapu par
ek adbhut purush baitha hua tha.
Uska tej aag jaisa tha.
Naam tha Mahajambunada.

Us purush ka roop
itna vishaal aur prabhavshaali tha
jaise devon ka raja
ya suraj sab grahon mein."""
        create_image_text_layout("attached_assets/chapter7/7.23f.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        Ravana ne garjana ki—
“Mujhse yuddh karo!”

Usne teer aur hathiyaar chalaye.
Par woh Mahapurush
bilkul shaant raha.
Jaise sher ko
kamzor jaanwar ka darr nahi hota.

Usne shaant swar mein kaha—
“Ravana,
main tumhari yuddh ki ichchha
abhi shant kar deta hoon.”

Us Mahapurush ki shakti
Ravana se hazaar guna zyada thi.
Uske sharir mein
poora jagat basa hua tha—
devta, rishi, parvat, samudra,
veda, kaal, dharma sab kuch.

Us Mahapurush ne
sirf khel-khel mein
Ravana ko haath se chhua.
Aur Ravana
zameen par gir pada.
Jaise ped jad se ukhad jaaye.

Phir woh Mahapurush
prithvi ke neeche ke lok mein
antardhaan ho gaya.

Ravana hosh mein aaya
aur apne mantriyon se bola—
“Woh kaun tha?
Kahan chala gaya?”

Mantriyon ne kaha—
“Woh purush
devon aur daityon ke
ghamand ko tod deta hai.”

Ghamand mein andha Ravana
gufa ke andar ghus gaya.
Wahan usne dekha—
bahut se divya purush
nrittya kar rahe the.
Sab usi Mahapurush jaise lag rahe the.

Tab Ravana ka
rom-rom kaanp utha.
Par Brahma ke vardaan ke kaaran
woh zinda bahar aa gaya.

Usne dekha—
ek shwet shayya par
Mahapurush shant so rahe the.
Unke paas
Lakshmi
seva kar rahi thi.

Ravana ke mann mein
galat ichchha jaagi.
Woh Lakshmi ji ki taraf badha.

Tab Mahapurush hans pade.
Unki aag jaisi shakti se
Ravana jalne laga
aur phir gir pada.

Mahapurush ne kaha—
“Utho Ravana.
Aaj tumhari mrityu nishchit nahi.
Brahma ka vardaan tumhari raksha karta hai.”

Ravana ka darr
ab poori tarah jag chuka tha.
Usne poocha—
“Tum kaun ho?”

Mahapurush muskuraye—
“Tumhara ant nikat hai.”

Ravana ne ghamand se kaha—
“Main amar hoon.
Mujhe koi maar nahi sakta.”

Tab Ravana ne
Mahapurush ke sharir mein
poora brahmand dekha—
dev, rishi, grah,
samudra, parvat,
jeev aur nirjeev sab kuch.

Yeh sun kar
Rama
Rishi Agastya se bole—
“Yeh Mahapurush kaun the?”

Agastya ji ne kaha—

“Woh Mahapurush
Kapila the.
Aur jo sab nrittya kar rahe the,
woh unke saman hi divya the.”

“Ravana turant nash nahi hua
kyunki Kapila ji ne
use krodh se nahi dekha.”

“Unke shabdon ne hi
Ravana ka ghamand tod diya.”

Kuch samay baad
Ravana sambhla
aur apne mantriyon ke paas
laut gaya.

Moral (Soft Message):

Kabhi-kabhi
sabse bada yuddh
bahar nahi,
andar hota hai.

Aur jo apne ghamand ko
nahi pehchaan pata,
use sachchi shakti
sirf ek jhalak dikha kar
jhuka deti hai 🌼"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 7.24
    with st.expander("Chapter 7.24 – Ravana abducts women and gets cursed"):
        text1 = """ 
        Safar ke dauran
Ravana
ghamand aur jeet ke nashe mein aage badhta gaya.
Par uske kaamon ka raasta
ab andhera hota ja raha tha.

Usne kai rajao, rishiyon aur devtaon ki
betiyon ko zabardasti
Pushpak Vimaan mein baitha liya.
Dar aur dukh se bhari
un aankhon se aansu girte rahe.
Vimaan ke andar
sirf siskiyon ki awaaz thi."""
        create_image_text_layout("attached_assets/chapter7/7.24.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        Un bechariyon ko
apne maa-baap,
apne pati,
apne ghar yaad aa rahe the.
Koi roti hui boli—
“Ab mere bachche ka kya hoga?”
Koi dukhi mann se keh uthi—
“Kya maine pehle kabhi
koi galti ki thi?”

Sabne milkar kaha—

“Yeh anyay hai.
Dusron ke sukh ko cheenna
bahut bada paap hai.
Is paap ka phal
use avashya milega.”

Un pavitra aur nirdosh
mahilaon ke shabdon se
aakash goonj utha.
Phoolon ki varsha hui.
Aur Ravana ka tej
pal bhar ke liye
kam sa lagne laga.

Yeh ek shraap tha—
anyay ke khilaaf sach ka shraap.

Kuch hi samay baad
Ravana Lanka pahuncha.
Rakshas khushiyaan mana rahe the.

Tab uski behen
Shurpanakha
roti hui uske saamne gir padi.

Aankhon mein gussa aur dukh tha.

Woh boli—

“Bhai,
tumhari talwar se
mera suhaag chhin gaya.
Mere pati ko tumne
yuddh ke junoon mein
maar diya.”

“Ab main
jeete-jeete vidhwa ho gayi.”

Ravana thoda hila.
Usne narm swar mein kaha—

“Behen,
yuddh ke shor mein
galti ho gayi.
Mujhe pehchaan nahi rahi.”

“Main tumhe samman aur suraksha doonga.”

Usne kaha—

“Tum apne cousin
Khara
ke paas jao.
Main uske saath
14,000 veer Rakshas bhejta hoon.”

“Khara
Dandaka Van ki raksha karega.
Tum wahan
nirbhay raho.”

Ravana ne
Rakshaso ki sena
Khara ko saunp di.
Khara turant
Dandaka Van ki taraf
chal pada.

Shurpanakha
ussi van mein rehne lagi.

Moral (Soft Message):

Shakti jab daya aur maryada ke bina ho,
to woh shraap ban jaati hai.
Aur jab nirdosh log anyay ke khilaaf bolte hain,
to unke shabd
bhavishya ka raasta badal dete hain 🌼"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.25
    with st.expander("Chapter 7.25 – Ravana allies with Madhu"):
        text1 = """ 
        Apni behen ko samjha-bujha kar
Ravana
ka mann thoda shaant hua.
Uska gussa kuch kam hua
aur chinta bhi door ho gayi.

Phir woh Nikumbhila Van gaya.
Wahan yagya-sthal chamak raha tha.
Havan-kund, stambh aur ved-mantra
sab kuch pavitra lag raha tha.

Wahin Ravana ne apne putra
Meghanada (Indrajit)
ko dekha.
Woh tapasya aur yagya mein lage hue the."""
        create_image_text_layout("attached_assets/chapter7/7.25.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        Ravana ne pyaar se poocha—
“Beta, yahan kya kar rahe ho?”

Tab Guru Shukracharya ne kaha—
“Meghanada ne bahut kathin yagya kiye hain.
Isse use divya rath, maya-shakti,
akshay baan aur adbhut dhanush mile hain.”

Ravana ne suna aur kaha—
“Achha hai.
Par ab ghar chalo.”

Lanka laut kar
Ravana ne bandi banayi hui
sab mahilaon ko bulaya.
Yeh dekh kar
Vibhishana
dukh se bole—

“Bhai,
yeh kaam tumhare liye achha nahi.
Isse tumhara naam, vansh aur bhavishya
sab ko nuksaan hoga.”

Vibhishana ne ek aur baat batayi—
“Madhu naam ka Rakshasa
Kumbhinasi ko le gaya hai.
Woh hamari rishtedaar hai.”

Ravana ko gussa aa gaya.
Usne turant yatra ki tayyari karne ko kaha.

Badi sena nikli—
aage Meghanada,
beech mein Ravana,
peeche Kumbhakarna.

Vibhishana Lanka mein hi rahe,
kyunki unka mann dharm ke saath tha.

Jab Ravana
Madhu ke nagar pahuncha,
Madhu wahan nahi mila.
Par Kumbhinasi
darr ke maare
Ravana ke charanon mein gir padi.

Usne vinamrata se kaha—
“Bhai,
mere pati ko mat maarna.
Ek stri ke liye vidhwa hona
sabse bada dukh hota hai.”

Ravana ka mann pighla.
Usne kaha—
“Daro mat.
Main Madhu ko nahi maarunga.”

Phir Madhu ko jagaya gaya.
Usse kaha gaya—

“Ravana dev-lok jeetna chahte hain.
Tum unke mitra bano.”

Madhu ne sammaan se
Ravana ka swaagat kiya.
Aur mitrata sweekaar kar li.

Ravana ne raat
Madhu ke ghar bitayi.
Subah apni sena ke saath
Kailasha Parvat ki taraf
prasthaan kiya.

Moral (Soft Message):

Jab gussa shaant hota hai,
to samajh paida hoti hai.
Aur jab samjhauta aur mitrata hoti hai,
to bina yuddh ke bhi
raaste nikal aate hain 🌼"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.26
    with st.expander("Chapter 7.26 – Nalakuvara curses Ravana"):
        text1 = """ 
        Raat ke samay
Ravana
Kailasha Parvat par apni sena ke saath
vishram kar raha tha.
Chandni raat thi.
Phool, hawa aur sangeet
parvat ko aur bhi sundar bana rahe the.

Is sundarta ko dekh kar
Ravana ka mann bhatak gaya.
Uske vichaaron mein
sanyam kam ho gaya."""
        create_image_text_layout("attached_assets/chapter7/7.26.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        Usi samay
ek apsara Rambha
wahan se guzar rahi thi.
Woh pavitra utsav ke liye
ja rahi thi.
Uske mann mein
koi galat bhaav nahi tha.

Ravana ne use roka.
Rambha darr gayi.
Usne vinamrata se kaha—

“Rajan,
aap mere rakshak ho.
Main aapke putra-samaan
Nalakuvara
ki patni hoon.
Mujhe jaane dein.”

Par Ravana ne
uski baat nahi suni.
Apne ahankaar aur ichchha ke vash mein
usne maryada ka ullanghan kiya.

Rambha rote hue
Nalakuvara ke paas pahunchi
aur saari ghatna batai.

Nalakuvara ka mann
dukh aur krodh se bhar gaya.
Usne dhyaan kiya
aur satya jaan liya.

Phir usne
Ravana ko shraap diya—

“Jo bal aur pad ka ghamand karke
kisi stri ki icchha ke bina
uski maryada todega,
woh kabhi sukh nahi paayega.
Aisi galti dobara hui
to uska vinash nishchit hoga.”

Yeh shraap sunte hi
akash se phool barse.
Devta prasann hue.

Jab Ravana ko
is shraap ka pata chala,
toh uska ghamand
toot gaya.
Usne samjha
ki shakti bina maryada
sirf vinash laati hai.

Is ghatna ke baad
jo striyaan pehle darr mein thi,
unke mann mein
thodi shanti aayi.

Moral (Soft Message):

Sachchi shakti wahi hoti hai
jo maryada aur samman ke saath ho.
Bal ya pad ka ghamand
jab niyantran kho deta hai,
toh uska parinaam
hamesha dukh deta hai 🌼"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.27
    with st.expander("Chapter 7.27 – War between Gods and Rakshasas"):
        text1 = """ 
        Bahut samay pehle,
Ravana
apni badi sena ke saath
Kailasha Parvat paar karke
Indraloka pahunch gaya.

Jab Rakshason ki sena aayi,
toh Devaloka hil gaya.
Awaazon se aakash goonj utha."""
        create_image_text_layout("attached_assets/chapter7/7.27.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        Indra
apne singhasan par ghabra gaye.
Unhone sab Devtaon ko bulaya.

“Taiyaar ho jao,”
Indra bole,
“Ravana se yuddh ka samay aa gaya hai.”

Sab Devta
– Aditya, Vasu, Rudra, Marut –
apne shastra le kar
maidan mein utar aaye.

Par Indra ka mann abhi bhi
chinta se bhara tha.
Woh seedhe
Vishnu
ke paas gaye.

“Hey Narayana,”
Indra ne kaha,
“Ravana ko Brahma ka vardaan mila hai.
Hum kaise jeetenge?”

Vishnu shaant the.
Unhone kaha—

“Dar mat, Indra.
Aaj Ravana ko koi nahi maar sakta.
Par uska ant zaroor hoga.
Main khud uske vinash ka kaaran banunga.
Abhi Devta milkar yuddh karo.”

Indra ko thoda sahas mila.

Yuddh shuru hua.
Devta aur Rakshas
aamne–saamne aa gaye.

Aakash mein teer ude.
Zameen par shor tha.
Har taraf yudh ka kohra tha.

Ravana ke saath
uske bahut saare yoddha the.
Unmein ek tha
Sumali,
Ravana ka nana.

Sumali bahut shaktishaali tha.
Usne Devtaon ko
peeche dhakel diya.
Kai Devta thak gaye.

Tab ek Devta aage aaye—
Vasu Savitra.

Savitra ne
poori himmat se
Sumali ka saamna kiya.

Dono ke beech
bhayanak yuddh hua.
Aakhir Savitra ne
apni gada uthayi.

Ek zor daar prahar hua.
Sumali gir pada.
Uski shakti wahin samaapt ho gayi.

Jab Rakshason ne
Sumali ko girte dekha,
unke mann mein darr aa gaya.
Woh sab yuddh chhod kar
bhaag gaye.

Devtaon ko rahat mili.

Moral (Soft Message):

Ahankaar aur anyaay
kitni bhi shakti ke saath ho,
ant mein haar jaata hai.
Aur dharma ke saath khadi himmat
kabhi vyarth nahi jaati 🌼"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.28
    with st.expander("Chapter 7.28 – Indra fights Ravana"):
        text1 = """ 
        Sumali ke vinash ke baad jab Rakshas sena bhagne lagi, tab Indrajit (Ravani) ne apni garajti hui awaaz se Rakshason ko phir se sambhala.
Woh apne divya rath par chadhkar Devtaon par toot pada — jaise jungle mein aag lag jaaye 🔥

Devta ghabra gaye, par tab Indra ne unhe roka:

“Bhago mat! Dekho, mera putra Jayanta bhi yuddh ke liye aa raha hai!”"""
        create_image_text_layout("attached_assets/chapter7/7.28.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        Jayanta vs Indrajit

Jayanta, apne rath par aakar Indrajit se bhid gaya.
Dono taraf se teer, shaktiyan aur astr-shastr barsne lage.

Indrajit ne maya-yuddh ka prayog kiya —
poori dishaon mein andhkaar chha gaya 🌑
Devta aur Rakshas ek-dusre ko pehchaan bhi nahi paa rahe the.

Isi andhkaar mein Puloman (Jayanta ka nana) Jayanta ko utha kar samudra mein le gaya.
Jayanta ke gaayab hote hi Devtaon ka sahas toot gaya aur ve idhar-udhar bikhar gaye.

Indra ka Pravesh

Putra ke lapata hone par Indra swayam yuddh ke liye nikle.
Unka divya rath, Matali ne taiyaar kiya.
Aakash mein bijli, aandhi aur apsaraon ka nritya —
yeh sab Indra ke prayan ke sanket the ⚡

Isi samay Ravana bhi apne Pushpaka Vimana par chadh gaya.
Saanp-jute rath, bhayankar gati, aur pralaya-jaisi shakti ke saath woh maidan mein kooda.

Indrajit ne yuddh chhod diya —
ab pita aur Devraj aamne-saamne the.

Devta vs Rakshas – Antariksh Yuddh

Rudra, Vasu, Marut, Aditya — sab Devta ek saath lade.
Rakshas sena chithar-bithar ho gayi.
Yuddh-kshetra khoon ki nadi jaisa lagne laga,
jahaan shastra magarmachh the aur pakshi mandra rahe the 🩸

Phir Ravana, krodh se bhara hua,
seedha Indra ko chunauti dene aaya.

Indra vs Ravana

Indra ne apna maha-dhanush chadhaaya —
uski tankaar se dishaen kaanp uthi.

Indra ke agni-teer Ravana par barsne lage ☀️
Aur Ravana bhi hazaaron teeron se Indra ko dhakne laga.

Aakash poori tarah andhkaar se bhar gaya.
Devta aur Rakshas — dono apni poori shakti se lade.

👉 Yeh yuddh ab apne charam par tha…
aur iska nateeja aane wala tha agle adhyay mein.

Dharmik Arth (Moral Insight)

Ahankaar + Vardaan = Bhayankar Vinash ka Marg

Maya aur bal se kuch samay jeet mil sakti hai,
par Dharma ka niyam atal hota hai 🌿

Devta bhi tab haarte hain jab ve ekjut nahi hote."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.29
    with st.expander("Chapter 7.29 – Indra is captured by Ravana’s son"):
        text1 = """ 
        Yuddh ka maidan ghor andhkaar se bhar gaya tha 🌑
Devta aur Rakshas ek-dusre ko pehchaan nahi paa rahe the.
Par teen log aise the jo bilkul bhatke nahi —
Indra, Ravana
aur Ravana ka putra Indrajit (Meghnad)."""
        create_image_text_layout("attached_assets/chapter7/7.29.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        Ravana ka Ahankaar

Apni sena ko nasht hota dekh kar Ravana ka krodh bhadak utha 🔥
Usne apne saarathi se kaha:

“Aaj main sab Devtaon ko Yama-lok bhej dunga!
Indra, Varuna, Yama — sab mere pairon tale honge!”

Uska rath bijli ki gati se Devtaon ki panktiyon ko kaatne laga.

Indra ki Yojana

Indra samajh gaye ki Ravana ko maara nahi ja sakta
(kyonki Brahma ka vardaan uski raksha karta tha).

Isliye Indra ne Devtaon se kaha:

“Ravana ko maaro mat, zinda pakad lo!
Jaise Bali ko bandhi bana kar maine teenon lok paaye the.”

Yeh kehkar Indra doosri disha mein chale gaye.

Indrajit ka Maya-Yuddh

Tab Indrajit ne apni maya-shakti ka prayog kiya ✨
Usne Devtaon ki sena ko ghabra diya.

Phir woh chupke se Indra par toot pada.
Devta Indrajit ko dekh hi nahi paaye.

Indra thak chuke the…
Aur usi pal Indrajit ne maya ke bandhan se
Devraj Indra ko baandh liya ⛓️

👉 Devtaon ke Raja ko bandhi bana liya gaya!

Devtaon ka Hausla Toot Gaya

Jab Devtaon ne dekha ki Indra bandhi ban chuke hain,
unka sahas toot gaya 😔
Aur ve yuddh chhod kar peeche hat gaye.

Putra ka Gaurav

Indrajit ne apne pita Ravana se kaha:

“Pitaji, vijay mil chuki hai.
Devraj bandhi ban chuke hain.
Ab aur yuddh ki zarurat nahi.”

Ravana ne garv se kaha:

“Putra, aaj tumne apne vansh ka maan badha diya.
Indra par vijay paana koi sadharan baat nahi.”

Phir Ravana ne Indrajit ko Indra ke rath par
bandhi bane Devraj ke saath Lanka jaane ko kaha.

Is Adhyay ka Moral 🌿

Ahankaar se jeet mil sakti hai, par shaanti nahi

Maya aur bal se Devta bhi bandhe ja sakte hain

Par yeh jeet asthaayi hoti hai ⏳

Dharma ka uday abhi baaki tha…
"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.30
    with st.expander("Chapter 7.30 – Gautama curses Indra"):
        text1 = """ 
        Jab Indra
Ravana ke putra Indrajit ke haathon bandhi ban gaye,
tab Devta chintit ho gaye 😔

Sab Devta Brahma ke saath
Lanka pahuche aur Ravana se shanti se baat ki."""
        create_image_text_layout("attached_assets/chapter7/7.30.jpg", text1, layout="side", image_position="left")
        text2 = """ 
        Indrajit ko vardaan

Brahma ne kaha:

“Tumhare putra ka veerata adbhut hai.
Uska naam Indrajit hoga —
jo Indra par vijay paane wala hai.”

Devtaon ne kaha:
“Indra ko chhod do, jo chaho vardaan le lo.”

Indrajit ne kaha:

“Mujhe amar bana do!”

Brahma bole:

“Amar koi nahi hota.”

Tab Indrajit ne doosra vardaan maanga:

“Jab tak main yuddh se pehle
Agni-dev ki pooja karun,
main ajay rahun.
Aur bina pooja ke yuddh karun,
to meri mrityu ho jaaye.”

Brahma ne kaha:
“Tathaastu.” ✨

Aur Indra ko chhod diya gaya.

Indra ka dukh

Indra ki shaan toot chuki thi.
Woh udaas ho gaye 😞

Tab Brahma ne kaha:

“Indra, kya tumhe apna paap yaad hai?”

Ahalya ka prasang

Brahma ne Indra ko uski bhool yaad dilayi…

Ek samay Ahalya
ko Gautama ke saath vivaah mein diya gaya tha.

Indra ne Gautama ka roop dharan karke
Ahalya ko bhramit kiya 😔

Gautama Rishi ne yeh dekh liya.
Aur krodh mein Indra ko shraap diya:

“Tum yuddh mein apne shatru ke haath
bandhi banoge!”

Isi shraap ka phal tha
jo Indra ko Indrajit ke haathon mila.

Ahalya ko bhi shraap

Gautama ne Ahalya se kaha:

“Tum tapasya karogi.
Ikshvaku vansh mein janme
Rama
tumhe shuddh karenge.”

Aur wahi hua 🌸
Vanvaas ke dauran
Rama ke sparsh se
Ahalya ka uddhaar hua.

Indra ka prashchit

Brahma ne Indra se kaha:

“Vishnu ki pooja karo.
Apni indriyon par niyantran rakho.”

Indra ne yagya kiya 🙏
Aur phir se Swarg ke Raja bane.

Is Adhyay ka Moral 🌿

Pad aur shakti galtiyon se nahi bachati

Paap ka phal der se sahi, par milta zaroor hai

Prashchit aur bhakti se hi uddhaar hota hai

Rama dharma ka prateek hain — jo giron ko bhi utha dete hain

Agla adhyay batayega
Ravana ke ant ka raasta kaise tay hua…
Agar chaho, main next chapter ko
chibi-style moral story ya simple children’s kahani mein likh sakta hoon 🌼"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.31
    with st.expander("Chapter 7.31 – Ravana at Narmada river"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.31.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.32
    with st.expander("Chapter 7.32 – Arjuna defeats Ravana"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.32.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.33
    with st.expander("Chapter 7.33 – Ravana is released"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.33.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.34
    with st.expander("Chapter 7.34 – Bali humiliates Ravana"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.34.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.35
    with st.expander("Chapter 7.35 – Story of Hanuman’s childhood"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.35.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.36
    with st.expander("Chapter 7.36 – Hanuman is cursed by sages"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.36.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.37
    with st.expander("Chapter 7.37 – Praise of Lord Rama"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.37.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.37b
    with st.expander("Chapter 7.37b – Supplement"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.37b.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.37c
    with st.expander("Chapter 7.37c – Supplement"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.37c.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.37d
    with st.expander("Chapter 7.37d – Supplement"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.37d.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.37e
    with st.expander("Chapter 7.37e – Supplement"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.37e.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.37f
    with st.expander("Chapter 7.37f – Supplement"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.37f.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.38
    with st.expander("Chapter 7.38 – Rama bids farewell to allies"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.38.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 7.39
    with st.expander("Chapter 7.39 – Rama gives gifts to allies"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.39.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.40
    with st.expander("Chapter 7.40 – Rama sends away Vanaras and others"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.40.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.41
    with st.expander("Chapter 7.41 – Pushpaka chariot is dismissed"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.41.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.42
    with st.expander("Chapter 7.42 – Happy life of Rama and Sita"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.42.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.43
    with st.expander("Chapter 7.43 – Rama hears public rumours"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.43.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.44
    with st.expander("Chapter 7.44 – Rama calls his brothers"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.44.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.45
    with st.expander("Chapter 7.45 – Rama orders Lakshmana to leave Sita"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.45.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.46
    with st.expander("Chapter 7.46 – Lakshmana takes Sita away"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.46.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.47
    with st.expander("Chapter 7.47 – Sita is told the truth"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.47.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.48
    with st.expander("Chapter 7.48 – Sita is left near the Ganga"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.48.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.49
    with st.expander("Chapter 7.49 – Valmiki shelters Sita"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.49.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.50
    with st.expander("Chapter 7.50 – Sumantra consoles Lakshmana"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.50.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.51
    with st.expander("Chapter 7.51 – Bhrigu curses Vishnu"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.51.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.52
    with st.expander("Chapter 7.52 – Lakshmana meets Rama"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.52.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.53
    with st.expander("Chapter 7.53 – Story of King Nriga"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.53.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.54
    with st.expander("Chapter 7.54 – End of Nriga’s story"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.54.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.55
    with st.expander("Chapter 7.55 – Story of King Nimi"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.55.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.56
    with st.expander("Chapter 7.56 – Urvashi is cursed"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.56.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.57
    with st.expander("Chapter 7.57 – End of Nimi and Vasishtha story"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.57.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.57b
    with st.expander("Chapter 7.57b – Supplement"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.57b.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.57c
    with st.expander("Chapter 7.57c – Supplement"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.57c.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.57d
    with st.expander("Chapter 7.57d – Supplement"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.57d.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.58
    with st.expander("Chapter 7.58 – Shukra curses Yayati"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.58.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.59
    with st.expander("Chapter 7.59 – Puru accepts his father’s curse"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.59.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.59b
    with st.expander("Chapter 7.59b – Supplement"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.59b.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.59c
    with st.expander("Chapter 7.59c – Supplement"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.59c.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.59d
    with st.expander("Chapter 7.59d – Supplement"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.59d.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.60
    with st.expander("Chapter 7.60 – Sages approach Rama"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.60.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 7.61
    with st.expander("Chapter 7.61 – Story of Madhu"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.61.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.62
    with st.expander("Chapter 7.62 – Shatrughna asks to fight Lavana"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.62.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.63
    with st.expander("Chapter 7.63 – Shatrughna is crowned"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.63.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.64
    with st.expander("Chapter 7.64 – Shatrughna marches to battle"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.64.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.65
    with st.expander("Chapter 7.65 – Story of King Saudasa"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.65.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.66
    with st.expander("Chapter 7.66 – Birth of Lava and Kusha"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.66.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.67
    with st.expander("Chapter 7.67 – Story of Mandhata"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.67.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.68
    with st.expander("Chapter 7.68 – Shatrughna meets Lavana"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.68.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.69
    with st.expander("Chapter 7.69 – Lavana is killed"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.69.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.70
    with st.expander("Chapter 7.70 – Shatrughna rules Madhu city"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.70.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.71
    with st.expander("Chapter 7.71 – Shatrughna meets Valmiki"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.71.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.72
    with st.expander("Chapter 7.72 – Shatrughna returns to Rama"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.72.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.73
    with st.expander("Chapter 7.73 – Death of a Brahmin’s son"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.73.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.74
    with st.expander("Chapter 7.74 – Narada explains the reason"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.74.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.75
    with st.expander("Chapter 7.75 – Rama inspects his kingdom"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.75.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.76
    with st.expander("Chapter 7.76 – Shambuka is killed"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.76.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.77
    with st.expander("Chapter 7.77 – Story of Svargin"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.77.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.78
    with st.expander("Chapter 7.78 – Story of Shveta"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.78.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.79
    with st.expander("Chapter 7.79 – Hundred sons of Ikshvaku"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.79.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.80
    with st.expander("Chapter 7.80 – Danda insults Aruja"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.80.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.81
    with st.expander("Chapter 7.81 – Danda’s kingdom destroyed"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.81.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.82
    with st.expander("Chapter 7.82 – Rama bids farewell to Agastya"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.82.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.83
    with st.expander("Chapter 7.83 – Bharata stops Rajasuya sacrifice"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.83.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.84
    with st.expander("Chapter 7.84 – Story of Vritra"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.84.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.85
    with st.expander("Chapter 7.85 – Vritra is slain"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.85.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.86
    with st.expander("Chapter 7.86 – Indra is freed"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.86.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.87
    with st.expander("Chapter 7.87 – Story of Ila"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.87.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.88
    with st.expander("Chapter 7.88 – Budha meets Ila"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.88.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.89
    with st.expander("Chapter 7.89 – Birth of Pururavas"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.89.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.90
    with st.expander("Chapter 7.90 – Ila regains her form"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.90.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")
    # Chapter 7.91
    with st.expander("Chapter 7.91 – Ashvamedha sacrifice planned"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.91.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.92
    with st.expander("Chapter 7.92 – Ashvamedha described"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.92.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.93
    with st.expander("Chapter 7.93 – Valmiki asks Lava-Kusha to sing Ramayana"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.93.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.94
    with st.expander("Chapter 7.94 – Lava-Kusha recite Ramayana"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.94.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.95
    with st.expander("Chapter 7.95 – Rama calls Sita"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.95.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.96
    with st.expander("Chapter 7.96 – Sita appears before Rama"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.96.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.97
    with st.expander("Chapter 7.97 – Sita enters the Earth"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.97.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.98
    with st.expander("Chapter 7.98 – Rama’s grief and Brahma’s words"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.98.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.99
    with st.expander("Chapter 7.99 – Death of the queens"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.99.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.100
    with st.expander("Chapter 7.100 – Bharata sent to conquer Gandharvas"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.100.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.101
    with st.expander("Chapter 7.101 – Gandharvas defeated"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.101.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.102
    with st.expander("Chapter 7.102 – Kingdoms given to Lakshmana’s sons"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.102.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.103
    with st.expander("Chapter 7.103 – Death comes for Rama"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.103.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.104
    with st.expander("Chapter 7.104 – Message of Death"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.104.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.105
    with st.expander("Chapter 7.105 – Visit of Sage Durvasa"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.105.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.106
    with st.expander("Chapter 7.106 – Lakshmana is banished"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.106.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.107
    with st.expander("Chapter 7.107 – Lava-Kusha crowned"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.107.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.108
    with st.expander("Chapter 7.108 – Rama’s final orders"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.108.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.109
    with st.expander("Chapter 7.109 – Rama’s Mahaprasthana"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.109.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.110
    with st.expander("Chapter 7.110 – Rama ascends to heaven"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.110.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 7.111
    with st.expander("Chapter 7.111 – Supreme message of Ramayana"):
        text1 = """ """
        create_image_text_layout("attached_assets/chapter7/7.111.jpg", text1, layout="side", image_position="left")
        text2 = """ """
        create_image_text_layout(text_content=text2, layout="full")
