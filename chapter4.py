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

Jab Sita yeh awaaz sunती thi na…
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
    text1 = """⭐ Hinglish Kahani: “Sugriva ka Dar Aur Hanuman ka Kaam”

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
    text1 = """ ⭐ Hinglish Kahani: “Hanuman aur Rama ka Pehla Milan”

Sugriva ne आदेश diya—
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

