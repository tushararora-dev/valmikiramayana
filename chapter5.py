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
        🐒 Hanuman ka sankalp

Hanuman ne mann mein nishchay kiya.
“Main Sita Maa ko dhoondh kar hi rahunga.”

Yeh kaam bahut mushkil tha.
Par Hanuman ke liye kuch bhi asambhav nahi tha.

Woh pahaad par khade hue.
Unki aankhon mein tej tha.
Dil mein sirf Shri Ram ka kaam tha."""
        create_image_text_layout("attached_assets/chapter5/5.1.jpg", text1,  layout="side", image_position="left")

        text2 = """
        🙏 Devtaon ko pranam

Hanuman ne
Surya Dev ko pranam kiya.
Vayu Dev ko yaad kiya.
Brahma aur sab jeevon ko naman kiya.

Phir unhone apne pita Vayu ko yaad karke kaha:
“Pitaji, mujhe shakti dena.”

⛰️ Pahaad ka kaanpna

Hanuman ne apna sharir bada kar liya.
Jaise poornima ki raat mein samundar badhta hai.

Unhone pahaad ko zor se pakda.
Pahaad kaanp utha.
Pedon se phool girne lage.

Paani baha,
sona–chandi jhalakne laga,
chattanen toot gayin.

Sab jeev dar gaye.
Rishi aur Vidyadhar aakash mein udd gaye.

Sab bole:
“Yeh Vayu ka putra Hanuman hai.
Yeh Ram ke kaam ke liye samundar paar ja raha hai.”

🦁 Maha-chhalaang

Hanuman ne zor se garaj kar kaha:
“Ya toh main safal ho kar lautunga,
ya Lanka ko hi utha launga!”

Aur phir—
DHAAD!

Hanuman ne maha-chhalaang lagayi.
Ped bhi unke saath udd gaye.
Jaise dost bidaai dene aaye ho.

Phool hawa mein udte gaye.
Samundar sitaron sa chamak utha.

Hanuman aakash mein
bijli jaise chamak rahe the.

🌊 Samundar ka samman

Devta phool barsa rahe the.
Surya ne apni garmi kam kar di.
Vayu Hanuman ki madad kar raha tha.

Samundar ne socha:
“Yeh Ikshvaku vansh ka kaam hai.
Mujhe sahayata karni chahiye.”

Usne Mainak parvat ko upar bulaya.

🏔️ Mainak parvat ka nimantran

Mainak parvat samundar se nikla.
Sone jaisa chamak raha tha.

Usne kaha:
“Hanuman, thoda aaram kar lo.
Phal khao, shakti lo.”

Par Hanuman muskuraye.
“Main vachan de chuka hoon.
Main ruka nahi sakta.”

Bas haath se sparsh kiya.
Aur aage badh gaye.

🐍 Surasa ki pareeksha

Devta chahte the
Hanuman ki buddhi ki pareeksha ho.

Surasa, naagon ki maa,
rakshasi ka roop lekar aayi.

Usne kaha:
“Tum mera bhojan ho.”

Hanuman bole:
“Kaam poora karke wapas aakar
tumhara vachan poora karunga.”

Surasa ne muh bada kiya.
Hanuman ne sharir bada kiya.
Surasa aur bada muh kholti gayi.

Achaanak—
Hanuman chhota ho gaye.
Ungli jitne size ke ban kar
uske muh mein gaye
aur turant bahar aa gaye.

“Pranam Maa,” Hanuman bole.
Surasa prasann hui.
“Jao beta, vijayi bano.”

👹 Singhika ka ant

Aage Singhika aayi.
Woh chhaaya pakad kar shikaar karti thi.

Usne Hanuman ki chhaaya pakad li.

Hanuman samajh gaye.
Sharir bada kiya.
Phir achaanak chhota ho kar
rakshasi ke muh mein ghus gaye.

Andar se hi
uska ant kar diya.

Sab devta bole:
“Shabash Hanuman!
Tumhara dhairya aur buddhi mahaan hai.”

🌴 Lanka ke paas

Hanuman ne socha:
“Agar main itna bada raha,
rakshas mujhe pehchaan lenge.”

Unhone apna asli roop le liya.
Shaant. Chhota. Tez.

Phir woh
Lanka ke paas pahunche.

Samundar ke kinare utar kar
unhone Lanka ko dekha—
sone si chamakti nagri.

Hanuman ne mann mein kaha:
“Ab asli kaam shuru hota hai.”"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.2
    with st.expander("Chapter 5.2 – Hanuman reaches the city of Lanka"):
        text1 = """
        🌊 Samundar ke paar

Samundar paar karke
Hanuman Trikuta Parvat par aa gaye.

Pedon se phool gir rahe the.
Jaise prakriti unka swagat kar rahi ho 🌸

Itna lamba safar karne ke baad bhi
Hanuman bilkul thake hue nahi the.

Woh muskura kar bole:
“Main hazaaron yojan ja sakta hoon,
yeh 400 yojan ka samundar kya cheez hai?”"""
        create_image_text_layout("attached_assets/chapter5/5.2.jpg", text1, layout="side", image_position="left")

        text2 = """
        🌳 Lanka ka pehla darshan

Hanuman ne aage dekha.
Hare khet, ghane jungle,
aur sugandhit ped-paudhe.

Sarala, Priyala, Ketaka,
aur rang-birange phoolon wale ped.

Talab the,
jinmein hans aur kamal khil rahe the 🦢🌸
Sundar bagiche aur fountains chamak rahe the.

Aur upar—
Sone jaisi chamakti Lanka ✨

🏰 Sone ki nagri

Lanka ek pahad par basi thi.
Charon taraf gehri khaai (moat) thi.

Safed aur neele kamal pani mein khil rahe the.
Har jagah rakshas pehredaari kar rahe the.

Sheher ke charon taraf
sunehri deewaar thi.

Unchi-unchi imaratein,
jaise badal zameen par utar aaye ho.

Safed mahal,
sone ke darwaze,
aur jhandon se saji sadkein.

Hanuman ko laga:
“Yeh to devtaon ki nagri jaisi hai.”

🤔 Hanuman ka vichaar

Hanuman thode gambhir ho gaye.

Woh bole:
“Yeh nagri bahut bhayanak hai.
Ravana yahan raj karta hai.”

Phir unhone socha:
“Sirf kuch hi vanar yahan aa sakte hain—
Sugriva, Nila, Bali ka putra… aur main.”

Par sabse pehle ek baat zaroori thi.

Hanuman ne mann mein kaha:
“Pehle mujhe Sita Maa zinda hain ya nahi,
yeh pata lagana hoga.”

🧠 Buddhi ka nirnay

Hanuman ne apne sharir ko dekha.
Woh bole:
“Is roop mein main sheher mein nahi ja sakta.”

Rakshas bahut chaukanna the.
Hawa tak ko pehchaan lete the.

Hanuman ne socha:
“Agar main pakda gaya,
to Ram ji ka kaam barbaad ho jayega.”

Unki aankhon mein chinta thi 😔
par buddhi tez thi.

Phir unhone nishchay kiya:
“Main raat ko,
chhote se roop mein,
chupke se Lanka mein jaunga.”

🌆 Raat ka intezaar

Hanuman surya ke doobne ka intezaar karne lage.

Jab suraj Asta Parvat ke peeche chhup gaya,
andhera chha gaya 🌒

Tab Hanuman ne apna sharir
billi jitna chhota kar liya 🐾

Aur ek chhalaang mein—
Lanka ke andar pravesh kiya!

🌙 Chamakti raat

Sheher ki sadkein chaudi thi.
Ghar sone ke khambon se sajey the.

7–8 manzil ke mahal,
sangmarmar ke farsh,
aur sunehri naqsh.

Hanuman ko yeh sab dekh kar
thoda aanand hua,
aur thoda dukh bhi.

Unhone socha:
“Kaash Sita Maa bhi
Ram ji ke saath aise sukh mein hoti.”

🌕 Chandra Dev ka saath

Aasmaan mein poornima ka chand tha 🌕
Taare uske saath chamak rahe the.

Chand ki roshni
jaise Hanuman ka raasta dikha rahi ho.

Hanuman ne chand ko dekha aur mann mein kaha:
“Hey Chandra Dev,
meri madad karna.”

Aur phir—
chupchaap,
hoshiyaari se,
Hanuman Lanka ke gharon mein
Sita Maa ko dhoondhne ke liye badhne lage…"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.3
    with st.expander("Chapter 5.3 – Hanuman enters Lanka quietly"):
        text1 = """
        🌌 Raat ka safar

Mount Samva par thoda aaram karke,
Pavan-putra Hanuman raat ke andhere mein
Lanka sheher ki taraf badhe.

Yeh sheher Ravana ka tha.
Bagiche sundar the.
Jheel aur pani chamak raha tha.
Samundar ki halki awaaz aa rahi thi 🌊

Hanuman ka mann utsah se bhara tha."""
        create_image_text_layout("attached_assets/chapter5/5.3.jpg", text1, layout="side", image_position="left")

        text2 = """
        🏰 Chamakti Lanka

Lanka bahut hi samriddh thi.
Sunehri deewarein.
Safed darwaze.
Jhande hawa mein lehra rahe the 🚩

Ghanti aur ghunghroo ki awaaz har taraf thi.
Ratnon se sajey farsh.
Moti, panna, heera, sab jagmagaa rahe the ✨

Seedhiyaan kristal ki thi.
Kamre aise lag rahe the
jaise hawa mein bane ho.

Mor aur koyalein bol rahi thi.
Hans aur rajhans talab mein tair rahe the 🦢
Dhol aur nagade baj rahe the.

Hanuman yeh sab dekh kar
thode hairaan,
thode khush ho gaye.

🤔 Hanuman ka vichaar

Hanuman ne mann mein socha:

“Yeh sheher bahut majboot hai.
Ravana ke sainik har jagah hain.

Sirf kuch hi vanar
yahan aa sakte hain—
Angad, Kumud, Mainda, Dvivida…
aur main.”

Phir unhone
Ram ji aur Lakshman ki veerta yaad ki.

Unka hausla aur badh gaya 💪

🌆 Lanka – ek nagri jaise stree

Hanuman ko laga
Lanka ek sajji hui stree jaisi hai.

Samundar uska vastra.
Astabal aur gaushala uske gehne.
Hathiyaar-grih uska bal.

Mashaalon aur taaron ki roshni
andhera mita rahi thi.

👹 Lanka Devi ka pravesh

Jaise hi Hanuman sheher mein ghuse,
Lanka Devi saamne aa gayi.

Woh bhayanak thi.
Awaaz garajti hui thi ⚡

Woh boli:
“Kaun ho tum, vanar?
Yahan kyun aaye ho?
Sach batao,
varna jeevan khatre mein hai!”

🐒 Hanuman ka shaant uttar

Hanuman shant rahe.
Unhone poocha:

“Pehle yeh batao,
tum kaun ho
aur mujhe kyun rok rahi ho?”

Lanka Devi gusse mein boli:

“Main Lanka ki rakshak hoon.
Ravana ke aadesh par yahan khadi hoon.
Mujhe haraaye bina
koi sheher mein nahi ja sakta!”

⚔️ Takraar

Hanuman bole:
“Main sirf sheher dekhna chahta hoon.
Uske bagiche aur mahal.”

Lanka Devi aur gussa ho gayi 😡
Aur boli:
“Mujhe haraaye bina
tum ek kadam bhi aage nahi ja sakte!”

Phir usne zor se
Hanuman par haath mara 👊

💥 Ek hi prahar

Hanuman garaj uthe.
Par unhone socha:
“Yeh ek stree hai.”

Isliye poori shakti nahi lagayi.
Bas apni mutthi se
usey door dhakel diya.

Lanka Devi zameen par gir gayi.

Hanuman ne usey dekha.
Unke mann mein daya aa gayi ❤️

🌺 Bhavishyavani

Zameen par padi Lanka Devi
kamzor awaaz mein boli:

“Hey Veer Vanar,
mujhe maaf karo 🙏

Tumne mujhe hara diya.
Aur iske saath
ek bhavishyavani sach ho gayi.”

Phir usne kaha:

“Brahma ji ne kaha tha—
jis din ek vanar mujhe haraayega,
us din Rakshason ka ant shuru ho jayega.”

“Tumhara yahan aana
is baat ka sanket hai
ki Ravana ka vinash nikat hai.”

🚪 Rasta khul gaya

Lanka Devi ne namrata se kaha:

“Ab tum bina roke
sheher mein ja sakte ho.

Jahan chaho jao.
Sita Maa ko dhoondho.

Tumhara kaam safal hoga.”

Hanuman ne aage kadam badhaya.
Lanka ke darwaze unke liye khul chuke the 🌟

Aur is tarah,
Hanuman ka asli mission shuru hua…"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.4
    with st.expander("Chapter 5.4 – Hanuman looks at the city and its people"):
        text1 = """
        🐒 Raat mein entry

Apni veerta se
Hanuman ne Lanka Devi ko hara diya tha.

Ab bina dar ke,
woh gate se nahi,
seedha deewar ke upar se kood gaye.

Raat ka samay tha 🌌
Aur Hanuman
Lanka ke beechon-beech pahunch gaye."""
        create_image_text_layout("attached_assets/chapter5/5.4.jpg", text1, layout="side", image_position="left")

        text2 = """
        👣 Rajmarg par chalna

Hanuman rajmarg par chalne lage.
Sadak phoolon se bhari thi 🌸
Har taraf hasi,
gaane aur sangeet ki awaaz thi 🎶

Unhone mann mein socha:
“Main Sugriva aur Ram ji ke kaam ke liye yahan hoon.”

🏙️ Chamakti nagri

Lanka ke ghar
bahut sundar the.

Heeron jaise jharokhe.
Safed badalon jaise mahal ☁️
Diwaron par kamal aur shubh chinh bane the.

Hanuman sab kuch
dhyaan se dekh rahe the.

💃 Mahal ke andar ki awaazein

Hanuman ghar-ghar jaakar
sun rahe the—

• Prem mein doobi auratein ga rahi thi
• Payal aur kangan ki awaaz aa rahi thi
• Taali aur manjiron ki chhan-chhan ho rahi thi

Kuch gharon mein
Vedo ka path ho raha tha 📜
Mantron ki madhur dhvani gunj rahi thi.

👹 Rakshason ka sheher

Kahin Rakshas
Ravana ki stuti kar rahe the.

Kahin jaasoos khade the 🕵️‍♂️
Alag-alag roop mein—

• Jata wale
• Mundan kiye hue
• Mrigcharm pehne
• Kuch toh ajeeb dikhne wale

Kisi ke ek hi aankh.
Kisi ka kaan hilta hua.
Kuch baune.
Kuch bhayanak.

Sab haathiyon jaise majboot nahi the.
Par sab savdhaan the ⚠️

⚔️ Sena aur suraksha

Hanuman ne dekha—

• Talwar wale
• Bhale aur gade uthaye hue
• Dand aur lohe ki salakhein
• Jhande aur nishan le jaate sainik 🚩

Hazaron Rakshas
raja ke aadesh par
mahal ki raksha kar rahe the.

🏯 Ravana ka mahal

Phir Hanuman ne dekha
Ravana ka mahal.

Woh pahad ke upar tha ⛰️
Sunehri darwaze.
Chaaron taraf gehri khaai.
Safed kamal se bhari.

Mahal se
ghodon ki hinhinahat,
rathon ki awaaz,
aur haathiyon ki garaj sunai de rahi thi 🐘

Chaar-dant wale haathi
badalon jaise lag rahe the.

🌸 Andar ka saundarya

Hanuman dheere se
mahal ke andar chale gaye.

Diwaarein
sone ki thi ✨
Chhat par
moti aur ratn jade the.

Har taraf
chandan aur agar ki khushboo thi 🌿

Yeh sab dekh kar bhi
Hanuman ka mann ek hi baat par tha—

👉 “Mujhe Sita Maa ko dhoondhna hai.”

Unki aankhen jagti thi.
Unka mann shaant tha.
Aur unka sankalp atoot 💛"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.5
    with st.expander("Chapter 5.5 – Hanuman searches the city but cannot find Sita"):
        text1 = """
        🌕 Chandrama ki roshni

Us raat poora chaand aasmaan mein chamak raha tha 🌕
Taaron ke beech woh aise lag raha tha
jaise safed kamal ya shankh ka tukda.

Uski thandi roshni
• andhere ko mita rahi thi
• samundar mein jwar utha rahi thi
• aur logon ke mann mein prem jaga rahi thi

Hanuman ne us chaand ko dekha
aur poori Lanka uski roshni mein naha rahi thi."""
        create_image_text_layout("attached_assets/chapter5/5.5.jpg", text1, layout="side", image_position="left")

        text2 = """
        🌃 Raat ka Lanka

Raat gehri ho chuki thi.

• Striyan apne patiyon ke saath so rahi thi
• Kuch Rakshas loot-paath ke liye nikal chuke the
• Kahin madira, kahin jua, kahin halla

Hanuman ne dekha—

🏛️ Bade-bade mahal
🐎 Raths, ghode, sunehri singhasan
🐘 Haathi garaj rahe the

Poora sheher
shor, bhog aur ghamand se bhara hua tha.

👹 Rakshason ke vyavhaar

Kahin Rakshas
• aapas mein jhagad rahe the
• apni chhaati peet rahe the
• dhanush utha kar dhamki de rahe the

Kahin koi kapde theek kar raha tha
kahin koi apni patni ko gale laga raha tha.

Sheher
jaise zehrele saanpon se bhari jheel ho 🐍

💃 Striyan aur bhog-vilas

Hanuman ne dekha—

• Courtesans shringar kar rahi thi
• Kuch hans rahi thi
• Kuch gusse mein thi
• Kuch gehri neend mein thi

Kuch striyan
apne premiyon ke saath aanand mein doobi thi.

Kuch
bina vastron ke
akeli padi thi,
sone jaise chamakti hui ✨

Sab kuch sundar tha,
par Hanuman ka mann shaant nahi tha.

👑 Sab kuch hone ke baad bhi…

Hanuman ne har ghar dekha.
Har mahal.
Har antahpur.

Sundar striyan thi,
gunvaan thi,
shobhavan thi.

Par…

❌ Sita Maa kahin nahi thi.

😔 Sita Maa ki yaad

Hanuman ke mann mein
Sita Maa ki tasveer ubhar aayi—

• Pavitra
• Pativrata
• Ram ji mein leen
• Aankhon mein aansu
• Hriday mein Ram ka naam

Woh Sita
jo pehle ratnon se sajti thi,
ab shok mein doobi hogi.

Jaise—
• dhool se dhaka sone ka tukda
• ghaav ka nishaan
• toota hua sunehra teer

Par woh kahin nazar nahi aayi.

💔 Hanuman ka dukh

Poora sheher chaan maarne ke baad bhi
Hanuman Sita Maa ko nahi dhoondh paaye.

Us veer ke mann mein pehli baar
nirasha aur shok aa gaya.

Unka hriday bhar aaya 💔
Unki himmat dagmaga gayi."""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.6
    with st.expander("Chapter 5.6 – Hanuman explores Ravana’s palace"):
        text1 = """
        🐒 Rooftops par ghoomta Hanuman

Raat ke sannate mein,
Hanuman apni ichchha ke anusar roop badalte hue
kabhi chhaton par, kabhi minaron par
poori Lanka mein vicharan kar rahe the.

Aakhir unki nazar padi
👉 Ravana ke raj-mahal par —
jo chamakte hue suraj jaisa tha ☀️
aur bhayankar rakshason se ghira hua.

Woh mahal
aise surakshit tha
jaise sheron se bhara hua ghana jungle 🦁"""
        create_image_text_layout("attached_assets/chapter5/5.6.jpg", text1, layout="side", image_position="left")

        text2 = """
        🏰 Ravana ka bhavya mahal

Hanuman ne dekha—

• Chandi aur sone se jade hue darwaze
• Bade-bade aangan aur sabha-sthal
• Ghantiyaan latakti hui rath
• Tez ghode aur yuddh-ke-liye taiyaar haathi 🐘

Rath aur wahan
sher aur baagh ki khaal se dhake hue the
jin par sone–chandi ki naqashi thi.

Yeh jagah
maharathiyon ki baithak thi —
yahan veer yojna banate the.

💎 Aishwarya aur raksha

Mahal mein har jagah—

✨ Ratn bikhre hue
✨ Mehnge singhasan
✨ Sugandhit chandan ki khushboo

Rakshakon ki kadi pehra
aur har taraf
straiyon ke gehno ki chhan-chhan 🔔

Kabhi yeh mahal
samundar ki tarah shaant lagta
(kyonki sab Ravana se darte the)
aur kabhi
lehron ki tarah goonj uthta
— shankh, nagade aur mridang ke swar se.

Hanuman ne socha:
🗣️ “Yeh sach mein Lanka ka ratna hai.”

🏠 Rakshas netaon ke mahal

Hanuman ruke nahi.

Ek-ek karke unhone dekhe—

• Prahasta ka mahal
• Mahaparshva ka nivas
• Kumbhakarna ka bhavya ghar (baadal jaise vishal ☁️)
• Vibhishan ka ghar
• Indrajit, Jambumali, Mahodara, Virupaksha
• Aur anek anya rakshas veeron ke mahal

Sabhi ghar
dhan–daulat aur shakti se bhare hue the.

Par Sita Maa kahin nahi.

👹 Antahpur ke bahar ka drishya

Aakhir Hanuman pahuche
👉 Ravana ke shayan-kaksh ke nikat.

Wahan—

• Bhayanak rakshasiyaan
• Haathon mein gadaa, bhala, talwar
• Aankhon mein kroorata 🔥

Bade-bade rakshas
har prakaar ke astr-shastr liye
chauksi se pehra de rahe the.

🐘 Sena aur sampatti

Hanuman ne dekha—

🐘 Aise haathi
jo shatru sena ko kuchal sakte the
— Airavata ke saman balshali

🐎 Tez ghode
⚔️ Sone ke rath
🛡️ Chamakte kavach

🎭 Rangshala
🎶 Manoranjan kaksh
🏋️ Vyayamshala

Har jagah
daulat ke dher lage hue the —
jaise Kubera ka khazana ho.

👑 Ravana ka tej

Ratnon ki chamak
aur Ravana ke apne tej se
poora mahal
suraj ki tarah jagmaga raha tha ☀️

Sone ke palang
motiyon se jade bartan
madira se bhare patra 🍷

Sangeet, nupur, manjira
har taraf goonj rahe the.

Sundar striyan
motiyon ke saman chamakti hui
mahal ko ghire hue thi.

😔 Par ek baat…

Itni bhavyata ke beech bhi—

❌ Sita Maa ka kahin pata nahi chala

Hanuman ka mann
aur bhaari ho gaya.

Unhone socha—
🗣️ “Itni khoj ke baad bhi
Janak-nandini yahan nahi…
toh woh kahaan hogi?”"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.7
    with st.expander("Chapter 5.7 – Hanuman sees the flying chariot Pushpaka"):
        text1 = """
        🐒 Hanuman ki talaash jaari rehti hai…

Hanuman, jo thakte nahi,
ab bhi Lanka ke bhavya mahalon ko
ek-ek karke dekh rahe the.

Yeh mahal—

✨ sone ki khidkiyon se sajje hue
✨ pannā (emerald) se jade hue
✨ baadalon ke jaise lagte the
jinmein bijli chamak rahi ho ⚡
aur safed bagule ud rahe hon 🕊️

Un mahalon ke andar—"""
        create_image_text_layout("attached_assets/chapter5/5.7.jpg", text1, layout="side", image_position="left")

        text2 = """
        • shankh
• dhanush
• talwarein
• yuddh ke astr–shastr

turret (minarein)
itni unchi
jaise pahad ⛰️

Yeh sab
Ravana ne apni tapasya aur shakti se banwaya tha —
itne sundar
ki devta aur rakshas dono inhe maan dete the.

👑 Ravana ka mukhya mahal

Aakhir Hanuman pahuche
👉 Ravana ke sabse vishal aur shreshth mahal par.

Woh mahal—

☁️ baadalon ke pahaad jaisa tha
💎 ratnon se bhara
🌸 har taraf phoolon se dhaka hua

Aisa lagta tha
jaise swarg khud dharti par utar aaya ho.

Sundar striyan
us mahal ki shobha badha rahi thi,
bilkul
jaise bijli baadal ko aur chamak de ⚡☁️

Hanuman ko laga—
🗣️ “Yeh koi mahal nahi,
yeh toh aakash mein chalne wala rath lagta hai.”

🌈 Maya se bhi aage ka kaam

Is mahal mein—

• nakli pahaad (mitti se bane)
• banavati ped jin par phool lage the
• safed imaaratein jo chamak rahi thi
• sarovar, jinmein kamal khile the 🌸
• bagiche aur fawware
jo mann ko moh lete the

Sab kuch
itna adbhut
jaise Maya ne bhi apni poori kala dikha di ho.

🚀 Pushpaka Vimaan ka darshan

Aur tab—

Hanuman ki nazar padi
👉 Pushpaka Vimaan par ✨

🔹 moti jaisa chamakta
🔹 sabse unchi imaaraton se upar tairta hua
🔹 devtaon ka vikhyat vimaan

Ismein—

• pannā, chandi aur moongā se bane pakshi
• dhatuon se bane naag
• jeevit jaise ghode aur pakshi
jin ke pankh
kabhi sikudte
kabhi phailte

Phool
sone aur moongā ke bane hue
aur un par yeh pakshi baithe the 🌺

Aur ek drishya—

🐘 haathi, kamal ke patte pakde hue
jo Mahalakshmi par jal chhidak rahe the
Lakshmi ji
kamal ke sarovar mein baithi
haath mein kamal liye hue 🌸

Hanuman
hairaan reh gaye 😮

Unhone socha—
🗣️ “Yeh toh pahaad ke gufaon se bhi adhik sundar hai,
ya phir
basant mein sugandh chhodte ped jaisa.”

😔 Par dukh ki baat…

Itni khoj ke baad bhi—

❌ Sita Maa ka kahin pata nahi

Na mahalon mein
Na Pushpaka ke aas-paas
Na kisi shobha mein

Hanuman ka hriday
jal utha 💔

Unhone socha—
🗣️ “Janak-nandini,
jo apne pati ke dharm aur prem se jeeti hain,
kahin aur hi rakhi gayi hongi…
shayad kisi udyan mein…
shayad kisi nirjan sthal par…”

Unke mann mein
jalti hui vedna utpann ho gayi."""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.8
    with st.expander("Chapter 5.8 – More details about the Pushpaka chariot"):
        text1 = """
        🐒 Hanuman ruk gaye.
Unki nazar
ab bhi Pushpaka Vimaan par tiki hui thi.

Woh vimaan
sona aur ratnon se saja hua tha ✨
itna chamakdar
ki aankhen khud-b-khud us par ruk jaati thi.

Yeh koi normal rath nahi tha.
🛠️ Vishvakarma khud
ise apni sabse shreshth kala maanta tha.

Har chhoti cheez
perfect thi.
Kahin bhi
koi kami nahi.

Hanuman ne socha—
🗣️ “Devtaon ke rathon se bhi
yeh vimaan kam nahi lagta.”"""
        create_image_text_layout("attached_assets/chapter5/5.8.jpg", text1, layout="side", image_position="left")

        text2 = """
        🚀 Soch se chalne wala vimaan

Yeh vimaan
Ravana ne tapasya se paaya tha 🙏
Sirf mann mein socho
aur vimaan
wahi pahunch jaata.

💨 Hawa se tez
🌌 aakash mein ghoomne wala
🎨 andar anek kamre aur kala ke adbhut namoone

Yeh vimaan
sirf shakti ka nahi,
sukh aur samriddhi ka prateek bhi tha.

🌕 Sundar aur pavitra

Pushpaka—

🌕 sharad poornima ke chand jaisa nirmal
⛰️ chamakdar chotiyon wale pahaad jaisa bhavya
🌸 phoolon se dhaka hua
aur basant se bhi zyada sundar

Isse uthti
ek alag hi roshni thi ✨

👹 Kaun uthaata tha ise?

Is vimaan ko
hazaaron rakshas uthaye hue the.

Un rakshason ke—

• bade-bade khule hue aankh
• kaanon mein kundal
• din-raat udaan bharne ki shakti

Woh vimaan
din aur raat
aakash mein
tez gati se ghoomta rehta tha 🌌

💭 Hanuman ka mann

Hanuman
is vimaan ko dekh kar
kuch pal ke liye
hairaan reh gaye 😮

Par phir
unka mann bhaari ho gaya.

Unhone socha—
🗣️ “Itni shaan,
itni shakti,
itni sundarta…
phir bhi Sita Maa yahan nahi hain.”

Unki aankhon mein
chinta thi
par mann mein
sankalp bhi 🔥"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.9
    with st.expander("Chapter 5.9 – Hanuman searches the women’s palace"):
        text1 = """
        🐒 Hanuman aage badhe.
Unki nazar
ek bahut bade mahal par padi.

Yeh mahal
Ravana ka antahpur tha.
Bahut hi vishal aur shandaar.

Hanuman dheere-dheere
andar gaye.
Unka mann sirf ek baat soch raha tha—

🗣️ “Kahin yahin Sita Maa to nahi?”"""
        create_image_text_layout("attached_assets/chapter5/5.9.jpg", text1, layout="side", image_position="left")

        text2 = """
        🏰 Mahal ka drishya

Mahal ke charo taraf—
🐘 bade-bade haathi
⚔️ hathiyaar uthaye rakshak
👹 rakshasiyon ki bheed

Yeh jagah
samundar jaisi lag rahi thi,
jahan khatarnaak jeev bhare pade ho.

Yahan
Ravana ki raniyan bhi thi
aur woh rajkumariyan bhi
jinhe usne zabardasti utha liya tha.

Hanuman ka mann
aur zyada bhaari ho gaya 😔

✨ Pushpaka Vimaan phir dikha

Mahal ke beech mein
Pushpaka Vimaan bhi tha 🚀

Woh itna sundar tha
jaise surya khud chamak raha ho.

Sone ki seedhiyaan
ratnon se bhari chhat
aur sugandh se bhara hua mahal 🌺

Par Hanuman ne
dil ko roka.
Unka kaam tha—
Sita Maa ko dhoondhna.

🌙 Andar ka drishya

Andar ek bada hall tha.
Sab jagah—
🪔 sunehre deepak
💎 chamakdar farsh
🎶 halki khushboo aur shanti

Wahan
bahut si sundar striyan so rahi thi.

Koi phoolon ke haar mein,
koi gehno mein,
koi apni saheliyon se lipti hui.

Sab
sharab ke nash mein soyi hui thi.

Hanuman ne
sabke chehre dekhe.

💔 Hanuman ka dukh

Unhone dhyaan se dekha…
par—

😢 Sita Maa kahin nahi thi.

Hanuman ka dil
toot sa gaya.

Unhone socha—

🗣️ “Agar Sita Maa in mein hoti,
to Ravana sach mein bhaagyashaali hota.”

Par phir
unhone khud hi jawab diya—

🗣️ “Nahi…
Sita Maa in sabse
bahut zyada pavitra aur mahaan hain.”

🌼 Ant mein Hanuman ka vichaar

Hanuman bole—

🗣️ “Isi Sita Maa ke liye
Ravana ne itna bada paap kiya hai.”

Unka mann
aur bhi majboot ho gaya 💪
par aankhon mein
abhi bhi chinta thi 😢"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.10
    with st.expander("Chapter 5.10 – Hanuman sees Ravana with his wives"):
        text1 = """
        🐒 Hanuman ne aage dekha…

Ek bahut hi shandaar manch (dais) tha—
💎 crystal ka bana
💍 motiyon se saja
🛏️ hara-emarald ke palang
🪵 sone aur haathi-dant se joda hua

Upar
🌕 chand jaisi chamak wala chhatra laga tha
jo devtaon ke yogya lag raha tha."""
        create_image_text_layout("attached_assets/chapter5/5.10.jpg", text1, layout="side", image_position="left")

        text2 = """
        👑 Ravana ka shayan-sthal

Us jagah par
🔥 sone ka palang tha
jo aag ki tarah chamak raha tha.

Us par
🌸 Ashok ke phoolon ki mala
🌬️ pankhe jhulte hue
🌺 sugandh charo taraf faili hui

Aur wahi…

😈 Ravana so raha tha.

😱 Hanuman ka bhay

Ravana ko dekhkar
Hanuman thoda peeche hat gaye.

Woh
deewar se chipak kar
seedhiyon ke paas khade ho gaye.

Unhone dekha—

🗣️ “Yahi hai Rakshason ka Raja…”

👹 Ravana ka bhayanak roop

Ravana
☁️ garajte badal jaisa lag raha tha
⚡ bijli ki tarah chamakte gehne
👁️ laal aankhen
👑 ratnon se bhara mukut

Uska sharir
🌼 kesar aur chandan se lipta hua
🟡 peela vastra pehne hua

Uski do badi-badi baahen
🐍 paanch-mukh wale saanpon jaisi lag rahi thi
jo palang par faili hui thi.

Wahi baahen
jinse devta, yaksha, gandharva sab kaamp jaate the.

🍷 Sugandh aur nasha

Ravana ki saanson se
🥭 aam
🌼 bakul
🍷 madira
🍛 bhojan
sabki mili-juli sugandh
poore mahal ko bhar rahi thi.

Woh
🛢️ gehri neend mein
🐍 saanp ki tarah saans le raha tha.

👩‍🎤 Ravana ki patniyan

Ravana ke charo taraf—

💃 uski patniyan so rahi thi
🎶 gaayika
🪕 veena, mridang, manjira pakde hue

Koi
veena se lipti
koi mridang se
koi saheli ko gale lagaye

Sab
🍷 nasha aur nritya se thaki hui
🌙 gehri neend mein thi.

Yeh drishya
aasman ke taaron jaisa lag raha tha ✨

🌸 Mandodari ka darshan

Phir Hanuman ki nazar padi—

👑 Mandodari par
Ravana ki mukhya patni

Woh
✨ bahut sundar
🌕 chand jaisi roshan
💎 ratnon aur motiyon se saji hui

Usse dekhkar
Hanuman ka mann uchhal pada 😮

🗣️ “Kahin yehi Sita Maa to nahi?”

🐒 Hanuman ki khushi (thodi der ke liye)

Is soch mein
Hanuman bahut khush ho gaye 😄

Unhone
🔁 uchhalna
🎵 gaana
🌀 dum hilana
🏛️ khambon par chadhna
⬇️ neeche koodna

Sab kuch
bandar jaisi masti mein kar diya.

⚠️ Lekin sach abhi baaki hai…

Yeh khushi
sirf ek pal ki thi.

Aage Hanuman samjhenge—

❌ Ye Sita Maa nahi hai
❌ Ye Mandodari hai

Aur phir
unhe milegi—

🌳 Ashoka Vatika
😢 dukhi Sita Maa"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.11
    with st.expander("Chapter 5.11 – Hanuman sees the grand dining hall"):
        text1 = """
        Chapter 11: Bhoj–Sabhā (Banqueting Hall) ka Varṇan

🕉️ Hanumān ji ka vichār-parivartan

Sītā ke baare mein pehle jo bhram aaya tha, use chhodkar Mahābalī Hanumān ne socha—

“Rām se bichhudi hui wo pavitra nārī
na to sukh se soyegi,
na bhojan karegi,
na shṛṅgār;
aur Indra jaise Devon ke rājā ko bhi svīkār na karegi.
Rām ka tulya koi Dev-lok mein bhi nahin.
Isliye yeh Sītā nahi ho sakti—yeh koi aur hai.”

Is nishchay ke saath, Sītā ko dhoondhne ke liye Hanumān fir se Bhoj–Sabhā ki talāsh mein lage."""
        create_image_text_layout("attached_assets/chapter5/5.11.jpg", text1, layout="side", image_position="left")

        text2 = """
        🍷 Bhoj–Sabhā ka drishya

Vahān—

ḍhol, mṛdaṅg, celikā par tik kar

ya komal palangon par letī hui

gānā–vādan, nṛtya aur madirā se thakī hui
hazāron sundar striyān gahrī nidrā mein so rahi thīn।

Kuch—

apni–apni sundartā par charchā karte hue so gayīn,

kuch gāyan–kalā par tark karte hue,

kuch samay–sthān ki samajh rakhne wali, avsar-vivek par baat karte hue,

aur kuch keval hās–vinod mein magn hokar nidrā ko prāpt ho chukī thīn।

In sab ke beech Rāvaṇ,
jaise gāyon se ghirā hua ek balvān bail,
ya van mein māda hāthiniyon ke madhya ek mahā-gaj,
shobhā pā raha tha.

🍖 Bhojan aur Vilās

Hanumān ne dekha—

bhains, hiran, bhalū ka māṁs alag-alag thālon mein,

mor, murghā sone ke patraon par,

suar, machhli, bakrī, khargosh, dahi aur namak ke saath pakāye hue,

kuch bhojan adha khāya hua, kuch bilkul chhua bhi nahi gaya.

🍶

uttam madirā,

phalon–phoolon se bani madhur pey,

sugandhit dravyaon se taiyār ki hui sharāb.

💎

sone ke pyāle, ratnon se jadit madirā–kalash,

kahin poore bhare, kahin aadhe, kahin bilkul khaali.

🌸

phal chhote patraon mein sajāe gaye,

phool bikhre hue,

gehne aur payal idhar–udhar pade hue,

aur poori sabhā agni ke saman chamak rahi thi।

😴 Sundar striyon ka nidrā–drishya

Kahin—

khali palang,

kahin ati-sundar yuvatiyān ek–dusre ko baahon mein bhare hue so rahi thīn।

Ek yuvati ne—

doosri ki razāī chheen kar

usi mein lipat kar nidrā le li thi।

Unki shwās itni komal thi
ki vastron ya mālāon ko keval sparsh kar rahi thi—
jaise hawa unhein sneh se chhoo rahi ho.

Sugandhit chandan,
madhur sidhu,
phool–mālā,
dhūp aur lepan—
sab milkar Pushpak Viman aur poore bhavan ko mahkā rahe the।

Striyān—

kuch śyām varṇ,

kuch kanchan–svarṇ jaise rang ki,

sab vilās se thak kar soye hue kamalon si lag rahi thīn।

❌ Sītā ka abhaav aur Hanumān ka dharm–chintan

Parantu—

👉 Janak–nandini Sītā kahin bhi nahin milī.

Sab ke chehron ko dekh lene ke baad Hanumān ke man mein chintā hui—

“Kya main apne kārya mein asafal to nahi ho gaya?”

Fir ek aur vichār aaya—

“Doosre ki patnī ko sote hue dekhna
nishchit hi dharm–viruddh hai.
Yeh mera uddeshya kabhi nahi tha.
Par yeh sab to Rāvaṇ ki patniyān hain—
jisne swayam par–striyon par drishti dali hai.”

🧠 Antim Vivek aur Atma–shuddhi

Tab buddhimān Hanumān ne apne man ko parakhā—

“Main in sab ko bina unke gyaan ke dekh aaya,
par mere man mein ratti bhar bhi vikār nahi aaya.
Man hi indriyon ka mool hai—
aur mera man sthir aur pavitra hai।

Sītā ko dhoondhne ka aur koi upāy bhi nahi tha.
Nārī ko nāriyon mein hi khoja jātā hai—
jaise hiran ko hiranon mein,
nārī ko mṛgon mein nahi.

Isliye pavitra hriday se
main Rāvaṇ ke antahpur tak gaya,
par Sītā yahān nahi hai.”

Dev, Dānav aur Nāg–kanyāon ke chehre dekh kar bhi
jab Sītā nahi milī,
to Hanumān Bhoj–Sabhā chhod kar
anya disha mein talāsh karne lage।

🌼 Adhyāy 11 ki Seekh

Kartavya ke liye shuddh drishti avashyak hai

Sharīrik drishya se adhik man ki shuddhata mahatvapurn hai

Dharm aur uddeshya pavitra ho to kārya bhi pavitra hota hai

Satya ki khoj mein dridhta aur vivek hi margdarshak hain

🌙 Chapter 11 yahin samāpt hota hai 🌙"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.12
    with st.expander("Chapter 5.12 – Hanuman feels sad and worried"):
        text1 = """
        Chapter 12: Hanumān ka Udaas ho jana

🏰 Antahpur mein antim talāsh

Rāvaṇ ke mahal ke andar hi ruk kar
Hanumān ji ne fir se khoj shuru ki.

bagīche dekhe

galleries dekhi

sone ke kamre dekhe

Par Sītā kahin bhi nazar nahi aayi.
Na wo sundar, shaant aur pavitra nārī.

Tab Hanumān ke man mein bhārī vichār aaye।"""
        create_image_text_layout("attached_assets/chapter5/5.12.jpg", text1, layout="side", image_position="left")

        text2 = """
        😔 Man ke andheron mein uthte vichār

Hanumān ne socha:

“Itni mehnat ke baad bhi
agar main Mithilā ki betī ko nahi paaya,
to shayad Sītā ab jeevit hi nahi hai.

Shayad usne apni maryādā bachāne ke liye
Rāvaṇ ke haathon prāṇ tyāg diye.
Ya phir us bhayānak rākshasiyon ko dekh kar
uska hriday toot gaya ho.

Meri saari shakti, meri saari veerta
vyarth chali gayi.”

Uska man aur bhi bhārī ho gaya.

⚖️ Sugrīva aur vānar–senā ka bhay

Hanumān ne aage socha:

“Main Sugrīva ke saamne
kaise jaaun?
Jo kathor dand deta hai.

Sab vānar mujhse poochhenge—
‘Samudra paar jaakar
kya laakar diye tum?’

Main kya uttar dunga?
‘Main Sītā ko nahi dhoondh paaya’?”

Yeh soch kar
Hanumān ka hriday kamp utha.

🔥 Tyāg ka vichār, par dhairya ki yaad

Ek pal ke liye
unhone socha:

“Shayad upvaas karke
prāṇ tyāg dena hi uchit hai.”

Par turant hi
ek aur shuddh vichār aaya—

“Parishram hi safalta ki jad hai.
Dhairya hi samriddhi ki jad hai.
Aur lagan se hi param sukh milta hai.

Jab tak saans hai,
tab tak prayās chhodna paap hai.”

🔍 Antim aur poori talāsh ka sankalp

Hanumān ne nishchay kiya:

jo sthaan chhoot gaye hain, unhe dekhunga

jo pehle dekhe the, unhe dobāra dekhunga

Unhone talāsh ki:

bhoj–sabhā

udyān

khel–mandap

aangan

ghar

sadak

gali

rath

Ek–ek kona.
Chaar ungli jitni jagah bhi nahi chhodi.

👹 Darāwani drishya, par Sītā nahi

Hanumān ne dekhi—

bhayānak rākshasiyan

vikrit sharīr

bhayanak chehre

Unhone dekhi—

Vidyādharon ki patniyan

Nāg–kanyāyen,
jinke mukh poorn chandrama jaise chamak rahe the

Par Sītā kahin nahi thi.

Na Rāghav ki priya.
Na Janak–nandini.

🌧️ Gehri niraasha

Itni sundar striyon ke beech bhi
jab Sītā nahi mili,
to Hanumān ka hriday toot sa gaya.

Unhe laga—

“Sab vānar–veeron ka parishram
aur mera samudra laanghna
sab vyarth ho gaya.”

Is bhār ke saath
Hanumān Pushpak Viman se neeche utar aaye.

🌑 Udaasi ka andhera

Ab—

chehra gambhir tha

man bhaari tha

aatma udaas thi

Pavan–putra Hanumān
gehri soch mein doob gaye.

🌙
Is adhyāy ke saath
Hanumān ki sabse badi parīkshā shuru hoti hai—
jab sab kuch andhera lagta hai,
tab bhi ummeed ko zinda rakhna।

✨ Is Adhyāy ki Seekh

Asafalta ke baad bhi prayās chhodna nahi chahiye

Dhairya hi veerta ka sachcha roop hai

Andhere ke baad hi ujaala aata hai

Jo rukta nahi, wahi jeetta hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.13
    with st.expander("Chapter 5.13 – Hanuman feels confused and troubled"):
        text1 = """
        Chapter 13: Hanumān ka Mahā-Dwand (Dilemma)

🌩️ Diwāron par utarte hue Hanumān

Pushpak Vimaan se ramparts par utarte hue
Hanumān ji bijli ki chamak jaise lag rahe the.

Par unka mann…
andhere se ghira hua tha.

Unhone socha:

“Main ne poori Lankā ko baar-baar chhaan maara,
par Janak-nandini Sītā kahin nahi mili.

Jatayu ke bhai Sampāti ne kaha tha
ki Sītā Rāvaṇ ke mahal mein hai,
par main use dekh nahi paaya—
yeh kaise ho sakta hai?”"""
        create_image_text_layout("attached_assets/chapter5/5.13.jpg", text1, layout="side", image_position="left")

        text2 = """
        😟 Bhayānak sambhāvanāyen

Hanumān ke mann mein ek-ek kar
bhayānak vichār ubharne lage:

Kahin Sītā ne Rāvaṇ ke bhay se prāṇ to nahi tyāg diye?

Kahin samudra ke upar le jaate samay
Rāvaṇ ke pakad se chhoot kar jal mein gir to nahi gayi?

Kahin us dusht ne Sītā ko maar diya ho?

Ya phir kisi andhere kaid-khaane mein band kar diya ho?

Par ek baat par unka vishwās atal tha:

“Rāma ki patnī
kabhi Rāvaṇ ko sweekār nahi kar sakti.”

⚖️ Satya bolun ya chhupāun?

Tab sabse kathin prashn saamne aaya:

“Agar main Rāma se kahun
ki maine Sītā ko nahi paaya—
to yeh unke liye prāṇ-ghātak hoga.

Par agar main satya chhupaun—
to woh bhi adharma hai.

Main kya karun?”

Hanumān uljhan mein pad gaye.

💔 Ek samachar jo sab kuch tod de

Unhone kalpanā ki:

Rāma Sītā ka naam sunkar prāṇ tyāg denge

Lakshmaṇ bhai ke bina jee nahi paayenge

Bharata aur Shatrughna bhi jeevan chhod denge

Teenon raniyaan—Kaushalyā, Sumitrā, Kaikeyī—
apne putron ke shok mein mar jaayengi

Sugrīva apne mitra ke dukh mein prāṇ de dega

Ruma, Tārā, Angad—sab vināsh ki ore badh jaayenge

Puri vānar-senā nashṭ ho jaayegi

“Meri ek asafal yātrā
poori srishti ka vināsh ban jaayegi.”

🔥 Maut ya Asha?

Hanumān ne socha:

“Agar main laut jaaun bina Sītā ke,
sab mar jaayenge.

Agar main yahin ruk jaun,
toh kam se kam asha zinda rahegi.”

Unhone apne mann mein do raaste dekhe:

Aatma-tyāg

Antim prayās

Par turant hi buddhi boli:

“Jab tak jeevan hai,
safalta sambhav hai.

Jeevit rehne mein hi
Rāma–Sītā ke milan ki sambhāvanā hai.”

⚔️ Veerta ka sankalp

Hanumān ne dridh nishchay kiya:

“Ya toh main
Rāvaṇ ko maar dunga,
ya use ghaseet kar Rāma ke saamne laaunga.

Par bina Sītā ko paaye
main Lankā chhod kar nahi jaaunga.”

🌳 Ashok Vatika ka smaran

Tab unhe yaad aaya:

“Ek sthaan abhi baaki hai—
Ashok Vatika.

Woh pavitra van
jahan dukh ko bhi shanti milti hai.

Shayad wahin
Rāma ki priya ho.”

🙏 Devtaon se prārthanā

Hanumān ne sab devtaon ko pranām kiya:

Rāma aur Lakshmaṇ

Pavan Dev

Agni, Chandra, Surya

Indra, Varuṇ, Marut

Rishiyon aur sab adrisht shaktiyon ko

“Mujhe safalta do,
mujhe Sītā tak pahunchāo.”

🐒 Laghu roop aur gupt yātrā

Hanumān ne apna roop bahut chhota kar liya:

“Ashok Vatika mein
kathor rākshas pahre par honge.

Gupt rehna hi
Rāma ki seva hai.”

🌸 Antim prashn, jo hriday se nikla

Aur unke mann se nikla ek hi sawāl:

“Kab main us pavitra rani ko dekhunga—
jinke daant motiyon jaise,
jinki muskaan chandrama jaisi,
aur jinki aankhen kamal-patra si hain?

Woh komal, pavitra nari
mujhe kaise milegi?”

🌿 Adhyāy ka Saar

Dharm aur kartavya ke beech ka dwand

Asha ka diya jo andhere mein bhi jalta hai

Hanumān ka sachcha veer roop—
jo toot kar bhi haar nahi maanta

🌙 Chapter 13 yahin samāpt hota hai 🌙"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.14
    with st.expander("Chapter 5.14 – Hanuman reaches the Ashoka garden"):
        text1 = """
        Chapter 14: Ashok Vatika

🧘‍♂️ Thoda ruk kar, mann ko shant karke…

Thodi der dhyān karke,
Hanumān ji ka mann phir Sītā ji ke khayal mein jud gaya.

Aur phir—
ek zordaar chhalaang!

Woh rampart se kood kar
Ashok Vatika ki deewar par aa khade hue.
Unka hriday khushi se kaanp raha tha."""
        create_image_text_layout("attached_assets/chapter5/5.14.jpg", text1, layout="side", image_position="left")

        text2 = """
        🌼 Basanti bahaar ka adbhut drishya

Wahan basant ritu thi.
Har taraf ped, phool aur khushboo thi।

Hanumān ji ne dekha:

Ashok, Champa, Aam, Kadamb, Nagkesar jaise ped

Lataon mein lipte hue sau-sau bel

Rang-birange phool jo hawa mein jhoom rahe the

Phir woh teer ki tarah
seedhe Ashok Vatika ke andar utar gaye.

Yeh bagicha
ugte hue suraj jaisa chamak raha tha।

🐦 Pakshiyon ka sangeet, prakriti ki muskaan

Har taraf:

Pakshiyon ki madhur awaaz

Madhumakhiyon ki gunjan

Moron ki pukaar

Hiran aur pakshi shanti se ghoom rahe the

Sab jeev khush lag rahe the.

Yeh dekh kar
dekhne wale ka dil bhi khil jaata tha 🌷

🌺 Phoolon ki baarish

Hanumān ji jab aage badhe,
toh sote hue pakshi ud gaye.

Unke pankhon ki hawa se
phoolon ki baarish hone lagi 🌸🌸

Rang-birange phool
Hanumān ji par girne lage.

Aisa lag raha tha jaise
phoolon se dhaka hua ek parvat chal raha ho.

Sab jeev sochne lage:

“Yeh to Basant Dev khud aa gaye hain!”

🌳 Haste hue ped, jhoomti dharti

Ped hil rahe the,
phool, patte aur phal gir rahe the.

Kuch ped aise lag rahe the
jaise sab kuch haar chuke hon 😄

Ashok Vatika ka drishya
aisa tha jaise—

“Ek yuva nari,
jiske baal bikhre ho gaye ho,
par phir bhi sundar ho.”

💎 Sone–chandi ke talab

Aage badhte hue
Hanumān ji ne dekha:

Sone aur chandi se bane raaste

Sheeshe jaise saaf talab

Kinare par motiyon, moongon aur ratnon ki seedhiyaan

Kamal aur kumud se bhare jalashay

Hans, batakh aur pakshi
un talabon ki shobha badha rahe the।

🏞️ Pahaad aur behte jharne

Phir unhone dekha
ek sundar pahaad—
badalon jaisa chamakta hua ☁️

Us pahaad se
ek nadi beh rahi thi।

Woh nadi aisi lag rahi thi
jaise koi yuva kanya
apne priya se rooth kar ja rahi ho…
aur phir thodi door jaakar
maan kar wapas aa rahi ho 💞

🌳 Shingshapa vriksh — vishesh drishya

Sabse aakhir mein
Hanumān ji ne dekha—

ek akela, sunehra Shingshapa ped 🌳✨
Uske chaaron taraf
sone ka chabutra tha।

Ped ke patte aur phool
hawa mein hil rahe the,
aur aisi awaaz aa rahi thi
jaise gehne khanak rahe ho।

Hanumān ji hairaan reh gaye।

🐒 Ped par chadh kar, aas lagaye hue

Hanumān ji turant
us Shingshapa ped par chadh gaye
aur mann mein socha:

“Yahin se shayad
main Vaidehi Sītā ko dekh paun.

Woh dukhi nari
jo Rāma ke bina ro rahi hogi.

Yeh Ashok Vatika
unke rehne ke yogya hai.

Jo van mein ghoomne ki aadat wali thi,
woh yahin zaroor aayegi.

Jo jeevon se prem karti thi,
woh is nadi ke paas pooja ke liye aayegi.”

🌙 Antim vishwas

Hanumān ji ne socha:

“Agar Sītā ji zinda hain,
toh woh yahin aayengi.

Is shant, pavitra jagah par.”

Yeh soch kar
Hanumān ji ped ke patton aur phoolon mein chhup gaye
aur poori Vatika ko
chupchaap dekhne lage 👀🌸

🌿 Adhyāy ka Saar

Ashok Vatika = asha aur shanti ka sthal

Prakriti bhi Sītā ji ke dukh ko mehsoos karti hai

Hanumān ka dhairya aur vishwas ab aur majboot ho chuka hai

🌼 Chapter 14 yahin samāpt hota hai 🌼"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.15
    with st.expander("Chapter 5.15 – Hanuman sees Sita for the first time"):
        text1 = """
        Chapter 15: Hanumān ne Sītā ko dekha

🐒 Ped par baithe Hanumān

Shingshapa ped par baithe hue,
Hanumān ji chaaron taraf dhyaan se dekh rahe the.

Unki aankhen
sirf Sītā ko dhoondh rahi thi 👀

Poora Ashok Vatika
swarg jaise lag raha tha—

Lataon se lipte ped

Phoolon ki sugandh

Koyal ki madhur awaaz

Sone jaise kamal, chandi jaise kumud

Sab kuch Nandan Van jaisa sundar tha 🌿✨"""
        create_image_text_layout("attached_assets/chapter5/5.15.jpg", text1, layout="side", image_position="left")

        text2 = """
        🌳 Ashok Vatika ki adbhut shobha

Ashok ke ped phoolon ke bojh se jhuk rahe the.
Aisa lag raha tha
jaise jad tak phool hi phool ho 🌸

Kimshuk, Karnikar, Champa, Punnag—
sab ped aag jaise chamak rahe the.

Pura vatika
jaise doosra swarg ho.

🏛️ Ek divya mandir

Tab Hanumān ji ki nazar padi
ek safed mandir par.

Kailash parvat jaisa safed

Hazaar stambhon par tika hua

Moonga jaise seedhiyaan

Sone jaise farsh

Mandir itna uncha tha
jaise aasmaan ko choo raha ho 🌕

😔 Aur tab… woh drishya

Achaanak…

Hanumān ji ne dekha
ek stri.

Woh—

Maili si peeli saadi mein thi

Bahut dubli ho chuki thi

Aas-paas rakshasiyan khadi thi

Baar-baar gehri saansein le rahi thi

Uski chamak
ab dhuaan mein ghiri lau jaisi lag rahi thi 🔥💨

🌙 Dukh mein doobi sundarta

Woh bina gehno ke thi.
Bilkul aise
jaise kamal bina phool ke.

Aankhon se aansu beh rahe the 😢
Chehra udaas tha.

Woh aisi lag rahi thi
jaise hirni shikariyon ke beech phans gayi ho.

Uske lambe kaale baal
peeche latak rahe the—
jaise baarish ke mausam ki kaali dharti 🌧️

💔 Hanumān ka hriday kaanp utha

Hanumān ji ne use dekha
aur mann mein socha:

“Yeh wahi hai…
yeh hi Sītā hai.”

Uska chehra
ab bhi poornima ke chaand jaisa tha 🌕

Bhale hi dukh ne use kamzor kar diya ho,
par garima aur pavitrata ab bhi saaf dikh rahi thi।

🌺 Sītā ki pehchaan

Hanumān ji ne dhyaan diya—

Kamal jaise netra

Bimba jaise honth

Patli kamar

Shant aur maryada bhari baithak

Woh dharti par baithi thi,
jaise tapasyā kar rahi ho 🙏

Uska dukh
jaal ki tarah uski sundarta ko dhak raha tha।

🧠 Nishchay

Hanumān ji ne mann hi mann kaha:

“Rāma ne jaisa varnan kiya tha,
yeh wahi nishaniyaan hain.

Jo gehne raste mein gira diye the,
woh yahan nahi.

Par jo bachaye the,
woh ab bhi uske sharir par hain.”

Uski saadi purani thi,
par rang ab bhi chamak raha tha—
bilkul uski apni roshni jaisa ✨

❤️ Rāma–Sītā ka bandhan

Hanumān ji ne socha:

“Yahi woh hai
jiske liye Rāma dukh mein jee rahe hain.

Prem, daya, shok aur virah—
sab isi ke liye.”

Dono ek-doosre ke sahare jee rahe the.
Ek ke bina doosra
shayad zinda na reh paata 💞

🙏 Mann hi mann pranām

Sītā ko dekh kar
Hanumān ji ka hriday bhar aaya 😌

Unhone mann hi mann:

Rāma ko pranām kiya

Sītā ko pranām kiya

Aur kaha:

“Mera kaam safal ho gaya.”

🌼 Chapter 15 ka Saar
Hanumān ne akhirkaar Sītā ko dekh liya

Dukh mein bhi Sītā ki pavitrata aur gaurav chamak raha tha

Hanumān ka vishwas aur kartavya aur majboot ho gaya"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.16
    with st.expander("Chapter 5.16 – Hanuman thinks deeply after seeing Sita"):
        text1 = """
        Chapter 16: Sītā ko dekhkar Hanumān ke vichār

🙏 Mann hi mann pranām

Sītā ko dekhkar
aur man hi man Rāma ko pranām karke,
vanaron mein shreshṭh Hanumān
fir se gehre vichār mein doob gaye।

Unki aankhon mein aansu the 😢
aur hriday karunā se bhar aaya tha।"""
        create_image_text_layout("attached_assets/chapter5/5.16.jpg", text1, layout="side", image_position="left")

        text2 = """
        🕊️ Bhāgya ke aage kaun jeet sakta hai?

Hanumān ji ne socha:

“Bhāgya ke bal ko kaun taal sakta hai?
Dekho, Lakṣmaṇ ke bade bhai,
maryādā puruṣ Rāma ki patnī Sītā
aaj is dukh ko jhel rahi hain.”

Phir unhone mann hi mann kaha:

“Rāma aur Lakṣmaṇ ke parākram ko jaankar bhi
yeh devī bilkul vyākul nahi hain—
jaise varṣā ke aane par
Ganga kabhi ghabrāti nahi.”

👑 Rāma aur Sītā — ek-doosre ke yogya

Hanumān ji ne nishchay kiya:

“Kul, svabhāv, ācharaṇ aur āyu—
har roop se Rāma aur Sītā barābar hain।
Rāghava hi Vaidehī ke yogya hain
aur Vaidehī hi Rāma ke.”

Sītā ki chamak
ab bhi naye sone jaisi thi ✨
bilkul Lakṣmī devī ke samaan.

🔥 Sītā ke liye hue maha-yuddh

Hanumān ji ne Rāma ke saare parākram yaad kiye:

Sītā ke liye Bāli ka vadh hua

Kabandh maara gaya

Vīrādha van mein gira

Janasthān mein 14,000 rākṣas jale

Khara, Dūṣaṇa, Triśirā— sab ka ant

Sugrīv ko Bāli ka rajya mila

Aur samudra bhi paar kiya gaya 🌊

Hanumān bole:

“Agar Rāma Sītā ke liye
poori dharti ko ulat dete,
toh bhi woh uchit hota!”

🌍 Teen lok vs. Sītā

Hanumān ka vichār aur gehra ho gaya:

“Agar ek taraf teenon lok ka raj ho
aur doosri taraf Janak-nandini Sītā—
toh teenon lok
Sītā ke ek ansh ke bhi barābar nahi!”

Woh dharti se utpann hui thi—
hal ki rekha se
kamal ke parāg jaisi dhool se nikli hui 🌾🌸

Woh Dasharath ki badi bahu,
veer aur dhairya se bhari,
kabhi peechhe na hatne wali.

🌲 Van ko mahal samajhne wali patnī

Hanumān bole:

“Rāma ke prem mein
Sītā ne sab sukh tyāg diye।

Mahal chhodkar
phal-mool par jeena
unhe kisi rajya se kam na laga।

Pati-sevā hi unka sukh tha।”

Par aaj—

Kanaka jaise ang wale

sada muskurane wali

wahi Sītā
akalpaniya dukh jhel rahi hai 💔

💧 Virah ka dard

Hanumān ne socha:

“Rāma unke darshan ke liye
pyāse vyakti jaise tadap rahe hain।

Sītā mil jaaye
toh Rāma ka sukh
gire hue rajya ke wapas milne jaisa hoga.”

Sītā—

Sab se door

Sab sukh se vanchit

Sirf Rāma ki āsha mein jee rahi thi

🌙 Rāma ke bina shobha bhi feeki

Hanumān bole:

“Stri ka sabse bada gehna
uska pati hota hai।

Rāma ke bina
itni sundar hote hue bhi
Sītā ki shobha feeki pad gayi hai।”

Aur Rāma—

“Sirf apni veertā ke bal par
jeevit hain,
varna virah ka dukh
kisi aur ko jeene na deta।”

🌧️ Karun drishya

Sītā—

Prithvi jaisi sahanśīl

Kamal netron wali

Kabhi Rāma–Lakṣmaṇ se surakshit

Aaj ped ke neeche baithi

bhayānak rākṣasiyon se ghirī hui 😔

Hanumān bole:

“Jaise palaa se kata kamal,
waise hi Sītā
vipattiyon ki varṣā mein murjha rahi hain।

Jaise jhund se bichhdi hirni,
waise hi woh akeli pad gayi hain।”

Ashok ke phool,
basant ka chand—
sab kuch unke dukh ko
aur badha raha tha 🌸🌕

🧠 Antim nishchay

Yeh sab soch kar
veer Hanumān poori tarah nishchit ho gaye—

“Yeh Sītā hi hain.”

Aur woh
Shingshapa ped par chupchaap
sthir ho kar baith gaye 🌳
— sahi samay ka intezaar karte hue।

🌼 Chapter 16 ka Saar

Hanumān ne Sītā ke dukh ko gehra mehsoos kiya

Sītā ke liye Rāma ke sab parākram yaad aaye

Rāma–Sītā ke prem aur maryādā par unka vishwas aur pakka ho gaya

Ab Hanumān agla kadam sochenge…"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.17
    with st.expander("Chapter 5.17 – Hanuman sees the demon women guarding Sita"):
        text1 = """
        Chapter 17: Sītā ki Rakṣā karne wālī Rākṣasiyān ka Bhayānak Varnan

🌕 Chandramā ka uday

Us samay nirmal, shvet kamal jaisa chandramā
nirdosh aakash mein uday hua।
Woh neele jal par tairte hue hans ke samaan
aakash-mandal mein vicharan kar raha tha।

Jaise Hanumān ki sahāyata ke liye hi,
us shītल chandrika ne
Pavan-putra Hanumān ko
apni thandi roshni se dhak liya ✨"""
        create_image_text_layout("attached_assets/chapter5/5.17.jpg", text1, layout="side", image_position="left")

        text2 = """
        💔 Dukh se jhuki hui Sītā

Chandni mein Hanumān ne dekha—

Sītā, jinka mukh chandramā ke samaan tha,
aaj dukh ke bojh se dabi hui
us naav jaisi lag rahi thi
jo lehron mein doobne wali ho।

Unhe dekhkar
Maruti ka hriday aur bhi karun ho utha।

👹 Bhayanak Rākṣasiyān ka darśan

Hanumān ne dekha ki
Sītā se thodi door
kai bhayanak rākṣasiyān pahra de rahi hain—

Kisi ki ek hi aankh ya ek hi kaan

Kisi ke kaan hi chehre ko dhak rahe the

Kisi ke maathe par naak

Kisi ke bahut bade sir aur lambe gale

Kisi ke baal itne kam, kisi ke itne zyada
jaise kambal lapeta ho

Kuchh—

Tedhi–medhi

Kubdi

Buni

Baune

Gande baalon wali

Aankhen laal, chehra bhayankar 😨

🐗 Pashu-sadrish roop

Kuch rākṣasiyān—

Bhalu ki naak, hirni ka muh

Sher, oont, bhains, bakri, giddh jaise chehre

Kisi ke hathi, ghode, oont ke pair

Kisi ke sir seene mein dhanse hue

Kisi ke—

Ek hi haath ya ek hi pair

Gadhe, ghode, gai, bandar jaise kaan

Hathi jaisi soondh-nāk

Ya naak hi nahi

Sach mein,
unko dekhkar ronte khade ho jaane wale the 😖

⚔️ Khoon aur madira se bhari rakṣā

Woh sab—

Bhale, gadaa, hathode pakde hue

Jhagda-priya, krodhi

Hamesha madira aur maans ka sevan karne wali

Unke sharir khoon se sane hue

Woh sab
us bahu-shakhā wale ped ke chaaron or
ghera banaye baithi thi
jiske neeche Janak-nandini Sītā thi।

🌸 Sītā ka karun saundarya

Hanumān ne dekha—

Sītā—

Apni tej se rahit

Dukh se jali hui

Dhool se bhare hue baalon wali

Jaise punya-kshaya ke baad gira hua tara ✨➡️🌍

Vishv-vikhyāt pativrata hone par bhi
unke milan ki aasha bahut kam lag rahi thi।

🌑 Upamāon se bhara drishya

Hanumān ke man mein upamāen utri—

Jhund se bichhdi hathini, jis par sher ne aakraman kiya ho

Varsha ke ant mein badalon se dhaki chandni

Bina chhede rakha hua veena

Keechad se lipta kamal 🌸

Ashok Vatika ke beech,
rākṣasiyon se ghiri hui Sītā
Rohini nakshatra jaise lag rahi thi
jise Rahu nigalne ko tatpar ho।

🪷 Sundarta ke pare pavitrata

Haan—
unke vastra phate hue the,
saundarya dhundhla gaya tha—

Par—

🔥 Unki aatma ab bhi divya thi

Kyoki—

Unka man Rāma ke yash mein sthir tha

Unki rakṣā unke apne charitra ne ki

Yahi unki asli shakti thi 💎

😭 Hanumān ka anand aur aansu

Sītā ko jeevit dekhkar
Maruti ke hriday mein
apaar anand bhar aaya।

Unhone—

Khushi ke aansu bahaye 😭

Mann hi mann Rāma ko pranām kiya 🙏

🙇 Gupt avasthā

Rāma aur Lakṣmaṇ ko pranām kar
veer Hanumān—

🌳 Poorn roop se chhupe hue
usi vriksh par sthir rahe
— sahi samay ka intezaar karte hue।

🌺 Chapter 17 ka Saar

Chandramā ke prakāsh mein Sītā aur unki rakṣak rākṣasiyān ka darśan

Rākṣasiyān ka atyant bhayanak aur vikrit varnan

Dukh se jali hui, par charitra se divya Sītā

Hanumān ka anand, aansu aur gupt sthiti"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.18
    with st.expander("Chapter 5.18 – Ravana comes to the Ashoka garden"):
        text1 = """
        Chapter 18: Rāvaṇ ka Aśoka Vāṭikā mein āgaman

🌌 Rātri ka ant aur prabhāt ki aahat

Phoolon se lade hue van ko nihārte hue,
Sītā ko nikat se dekhne ki icchā se bhare Hanumān ne
mehsoos kiya ki rātri apne ant ki or badh rahi hai।

Us samay, titanon mein jo Vedoṅ, Śāstroṅ aur unke chhah aṅgoṅ ke gyaata the,
unke mukh se Vaidik mantraon ka uchchāran sunāi dene laga।
Woh dhvani pavitra thi, shubh thi—
aur prabhāt ka sanket de rahi thi 🔔"""
        create_image_text_layout("attached_assets/chapter5/5.18.jpg", text1, layout="side", image_position="left")

        text2 = """
        👑 Daśagrīv Rāvaṇ ka jagna

Isi shubh dhvani ke saath
das siron wala Mahābali Rāvaṇ nidrā se jagā।

Sangeet madhur tha, manohar tha—
jaise kisi rājā ko jagāne ke liye devatā svayam ga rahe hon।

Jagte hi—

uske haar aur vastra vyavasthit na the

man turant Vaidehī Sītā ki or chala gaya 💔

Sītā ke prati ati-vyāmoha mein dooba hua
woh ghamandi rākṣas
apni icchāon par niyantran na rakh saka।

🌺 Aśoka Vāṭikā mein praveś

Apne sharir ko—

anek prakār ke ābhūṣaṇon se sajā kar

ati bhavya vastron mein dharan kar

Rāvaṇ ne Aśoka Vāṭikā mein praveś kiya 🌸

Woh van—

anant vrikṣon se bhara tha

har prakār ke phal–phool se ladā hua

kamal aur kumud se sajjit sarovaron se yukt

prem mein magna sundar pakshiyon se gungunata

aur adbhut shilp-kala se bane hue bhaiyon (wolves) se sajā hua tha

👸 Sang mein sau sau sundar striyān

Rāvaṇ ke pichhe—

sau sundar striyān chal rahi thi

jo Dev aur Gandharvon ki putriyan thi

Bilkul waise hi
jaise Indra ke pichhe apsarāyen chalti hain ✨

Unmein se—

kuchh sone ke deep uthaaye hue thi

kuchh chanvar aur pankhe

kuchh sone ke kalash mein jal liye aage chal rahi thi

kuchh sone ka sinhaasan aur gaddiyan

ek uske daahine taraf ratn-jadit madira-pātra

aur ek hans jaisa chhatra,
sone ki dandi aur chandrama jaisi chamak wala ☂️

🍷 Rāvaṇ ki patniyon ka varnan

Rāvaṇ ki patniyan—

neend aur madira ke prabhāv mein

ladkhadati hui chal rahi thi

Unke—

motiyon ke haar aur chūḍiyan jhool rahi thi

chandan lep mit chuka tha

baal bikhre hue the

maathe par paseene ki boondein thi

phool murjha gaye the

gajron ke tukde baalon mein atke the

Fir bhi—

unmein garv tha

saundarya tha

aur apne pati ke prati ākarṣaṇ aur anurāg bhi

Is tarah woh komal striyān
Rākṣas-rāj ke pichhe chal rahi thi।

🐘 Icchā ka gulām Rāvaṇ

Rāvaṇ—

apni kāmanāon ka dās ban chuka tha

man poori tarah Sītā par sthir tha

Isliye—

👉 woh dheere–dheere
👉 ghamand ke saath
👉 Aśoka Vāṭikā mein aage badh raha tha

🔔 Hanumān ka darśan

Hanumān ne—

striyon ke kamarbandh aur nupuron ki ghantiyon ki dhvani suni

aur dekha—

🔥 Rāvaṇ, jiska bal aur parākram
akalpanīya tha।

Chāroṅ or—

sugandhit tel se jalte anek deep

unki roshni mein Rāvaṇ chamak raha tha

Madira, ghamand aur kāmanā se matwala
uski laal-tāmbey jaisi aankhen
use Manmatha (Kāmdev) jaisa bana rahi thi
— lekin binā dhanush ke 🎯

🧥 Rāvaṇ ka rūp

Usne apna—

phoolon se sajā hua

amrit-manthan ke jhaag jaisa nirmal

bhavya uttarīya (cloak)

theek kiya
jo ek sundar clasps se bandha hua tha।

🌿 Hanumān ka gupt darśan

Patton aur shaakhāon ke parde ke peeche chhupe hue
Mahābalī Hanumān ne
us rākṣas-rāj ko dhyān se dekha।

Unhone pehchān liya—

“Yahi hai woh lambe bhujāon wala Rāvaṇ,
jo pehle nagar ke madhya bhavya mahal mein so raha tha.”

🌑 Rāvaṇ ke tej ke saamne Hanumān

Yadyapi Hanumān—

atyant veer the

tej se bhare hue the

Phir bhi—

⚡ Rāvaṇ ka prabhāv itna prachand tha
ki Hanumān ne apne aap ko
aur adhik patton mein chhupa liya।

🔥 Rāvaṇ ka lakṣya

Rāvaṇ—

nirdosh, sundar, shyām-keshī Sītā ko dekhne ke liye

jinki stan paraspar sparsh karte the

aur jo nirdoṣ angon wali thi

👉 nishchit kadmon se aage badhta chala gaya।

🌺 Chapter 18 ka Saar

Rātri ke ant mein Rāvaṇ ka jagna

Sītā ke prati uski ati-kāmanā

Bhavya shobha ke saath Aśoka Vāṭikā mein praveś

Sau sau sundar striyon ka anuyāyi samūh

Hanumān ka gupt darśan aur satarkta

Rāvaṇ ka Sītā ki or badhna"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.19
    with st.expander("Chapter 5.19 – Sita feels great sorrow"):
        text1 = """
        Chapter 19: Sītā ka Śok (Sita’s Grief)

👑 Rāvaṇ ko dekhkar Sītā ka kampan

Jab Sītā ne Rāvaṇ, rākṣason ke rājā ko dekha—
jo yauvan se yukt, sundar, ati-mulyavān ābhūṣaṇon aur bhavya vastron se sajā hua tha—
toh woh pavan se hilte hue tāḍ vrikṣ ki bhānti kaanp uthi 🌴

Lajjā aur bhay se—

apne stan aur udar ko haathon se dhak liya

aur peeche hat gayi, apne aap ko chhupane ka prayās karte hue"""
        create_image_text_layout("attached_assets/chapter5/5.19.jpg", text1, layout="side", image_position="left")

        text2 = """
        🌊 Śok mein doobi Vaidehī

Daśagrīv Rāvaṇ ne dekha—

Vaidehī, jo bhayanak rākṣasiyon se ghiri hui thi

aur jo duḥkh se toot chuki thi

Woh—

samudra mein doobti hui nāv ke saman lag rahi thi ⚓

🌾 Zameen par baithi dharm-nishṭh Sītā

Nangi bhoomi par baithi hui—

Sītā, jo sadaiv dharm mein sthir rahi

kata hua daal jaise vrikṣ se tootkar gir padi ho

Maili vastron se dhaki hui—

jo ābhūṣaṇon ke yogya thi

ab nirābharaṇ thi

Woh—

kichad se lipta hua kamal-dand jaise lag rahi thi 🌸
tej toh tha, par saundarya dhundhla chuka tha

🛕 Man mein Rām ka āśray

Apne man mein—

nar-shreshṭh Rām ka āśray liya

uska man ek rath ke saman tha
jise sankalp ke ashva kheench rahe the 🐎

Woh—

Rām ke prati poori tarah samarpit

kshin sharir, rote hue

apne parijanon se bichhudi

chintā aur śok ka shikār

Aur use apne duḥkh ka koi ant dikhai nahi deta tha।

🌪️ Upmāon mein Sītā ka duḥkh

Dukh se hilti-dulti hui Sītā—

Nāg-rāj ki patni jaise mantra se bandhi ho

ya Rohiṇī, jo Dhumaketu ke peechhe lagne se peedit ho

ya koi kulīn aur sādhvī strī, jo vivāh ke kaaran neech kul mein aa padi ho

Woh aisi thi jaise—

khoi hui pratishṭhā

tyaagi hui shraddhā

andhakaar se dhaka hua man

tooti hui āśā

ujda hua bhavishya

galat samjha gaya ādeś

pralaya mein mit chuka desh

devon dwara thukrāya gaya yajña

badalon se dhaka poornimā ka chandrama

ujda hua kamal-sarovar

yoddhāon se rahi hui sena

grahaṇ mein pada chandrama

sookhi hui nadi

apavitra kiya gaya vedi

bujhi hui agni

phoolon se rahit kamal-van,
jiske pakshi haathiyon ke garjan se bhaybhīt ho gaye hon 🐘

🌑 Virah mein shoonya hoti Sītā

Apne pati se bichhud kar—

woh sookhi hui nadi jaise ho gayi

ang na dhone ke kaaran
krishna paksha ki raat si lag rahi thi 🌘

Jo kabhi—

ratnon se bhare mahal mein rehti thi

komal aur sukumār thi

Aaj—

dhoop mein murjhata hua kamal-dand jaise lag rahi thi ☀️

🐘 Bandhi hui hathni ki tarah

Jaise—

pakdi hui hathni

khambhe se bandhi

apne saathi ko yaad kar

baar-baar aah bharti hai

Waise hi—

Sītā bhi—

baar-baar saans bhar rahi thi

apne priyatam Rām ke liye 💔

Uske—

lambe, kaale baal

bilkul asanvarit

peeth par bikhar gaye the

Aur woh—

varsha ritu ke ant mein ghane van se dhaki prithvi jaise dikh rahi thi 🌧️🌳

🙏 Prārthanā aur tapasya

Bhookh, śok, bhay aur chintā se peedit—

ati-kshin

ekākinī

upvās aur tapasya se kamzor

Fir bhi—

devī ke saman tej yukt

haath jod kar

Rām se prārthanā kar rahi thi—

“Rāvaṇ ka vināś ho” 🔥

🔥 Rāvaṇ ka vināś-yukt prayās

Is prakār—

nirdosh

niraparādh

shyām-netron wali

komal palakon wali Maithilī

ko dekh kar—

⚠️ Rāvaṇ, apne hi vināś ki or badhte hue,
use mohit karne ka prayās karne laga।

🌺 Chapter 19 ka Saar

Rāvaṇ ko dekh Sītā ka bhay aur lajjā

Uska sharirik aur mansik kṣay

Rām mein poorn āśray

Upmāon ke madhyam se gahan śok ka varnan

Rāvaṇ ka adharm-purn lobh — jo uske vināś ka kāraṇ banega"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.20
    with st.expander("Chapter 5.20 – Ravana asks Sita to marry him"):
        text1 = """
        Chapter 20: Rāvaṇ ka Sītā se Vivāh ka Prastāv (Ravana begs Sita to wed him)

👑 Rāvaṇ ka madhur par vishayukt prastāv

Tab Rāvaṇ,
us asahāy Sītā ke nikat aaya—
jo rākṣasiyon se ghiri hui,
tapasyā aur sanyam ka vrat dhāran kiye hue thi।

Mithyā madhur vākya aur vinīt bhaav dikhāte hue Rāvaṇ bola—"""
        create_image_text_layout("attached_assets/chapter5/5.20.jpg", text1, layout="side", image_position="left")

        text2 = """
        💬 Rāvaṇ ke vachan

“O Sundarī,
jinki jaṅghāen hāthi ke sund jaise hain,
jo mujhe dekhkar apne stan aur sharīr ko dhak rahi ho,
jaise mujhse bhaybhīt ho —
main tumse prem karta hoon, Maithilī ❤️

O Vishāl-netrā,
poore jagat dwārā pūjit,
mujh par kripā karo।
Yahan na koi purush hai,
na koi aisa rākṣas jo rūp badal sake,
isliye apne hriday se bhay ko nikaal do, O Sītā।

⚠️ Rākṣas dharm ka adharm-purn tark

Rāvaṇ aage bola—

“Rākṣason ke liye yeh sadiyon purānā adhikār hai
ki ve dusron ki patniyon ko
ya to apni ichchhā se grahan karein
ya bal-pūrvak haran karein।

Phir bhi, O Maithilī,
main tumhe sparsh tak nahi karūnga
kyunki tum mere prati anurāg nahi rakhti।
Lekin main poori tarah tumhare vash mein hoon,
isliye mujh par vishvās karo aur
mere prem ko svīkār karo।”

🌺 Sītā ke sanyam par vyangya

“O Devī,
bhay tyāg do, sahas dhāran karo।
Ek jata bandhkar rehna,
maili vastron mein bhoomi par sona,
aur anāvashyak upvās—
yeh tum jaise saundarya ko shobha nahi dete।

Mere saath rehkar
tum pushp-mālā, sugandh, chandan,
ratna-ābhūṣaṇ, madirā,
rājasi shaiyā, gān, nritya aur sangeet ka anand lo 🎶

Tum striyon mein moti ho,
is dasha mein rehna tumhare yogya nahi।
Apne purāne saundarya ko phir se dhāran karo।”

⏳ Yauvan ka bhay dikhaana

“O Sundarī,
tumhara yauvan behta hua nadi-jal hai—
jo ek baar chala gaya
phir kabhi laut kar nahi aata।

Tumhari rachna karne ke baad
Vishvakritā ne apna kaam rok diya,
kyunki tum jaisi sundar koi aur nahi!
Tumhe dekhkar kaun sthir reh sakta hai?
Brahmā tak vichlit ho jaate hain,
phir anya jeev ka kya kehna?”

👑 Rājya, dhan aur shakti ka pralobhan

“O Chandra-vadanī,
meri rani ban jao aur
meri anek sundar striyon mein
shreshṭh maharānī bano।

Jo dhan maine teenon lokon se jeeta hai,
woh sab tumhara hai।
Mera sampoorn rājya tumhe samarpit karta hoon।

Tumhare liye
poori prithvī jeetkar
usse Rājā Janak ko lauta dūnga।

Dharti par koi meri shakti ka muqabla nahi kar sakta।
Dev aur Dānava—
sab mere yuddh mein asahāy ho gaye the।
Unke dhwaj toot gaye, sainya bikhar gaya!”

⚔️ Rām ka apmān

Phir Rāvaṇ ne Rām ko nicha dikhāte hue kaha—

“Meri sampatti aur vaibhav dekho, Maithilī।
Rām se tum kya paogi?

Woh valkal (bark) pehenta hai,
rājya se vanchit ho chuka hai,
bhoomi par sota hai,
tapasvī ban chuka hai।

Kaun jaane woh jeevit bhi hai ya nahi?
Tum us taare ki tarah ho
jo kaale badalon ke peechhe chhup gaya ho।

Rāghav tumhe kabhi dhundh nahi paayega।
Jaise Hiranyakashipu
Indra se apni patni Kirti ko
wapas nahi la saka—
waise hi Rām bhi asamarth hai।”

💎 Antim pralobhan

“O Madhur-hāsini,
tum mere hriday ko
usi tarah har leti ho
jaise Suparna ne nāg ko utha liya।

Tumhare vastra phate hue hain,
tum ābhūṣaṇ-rahit ho—
phir bhi tumhe dekhkar
mera man meri sabhi raniyon se
virakt ho jaata hai।

O Janak-nandinī,
meri raniyon par shāsan karo,
yeh sab tumhari dāsiyan banengi
jaise Apsarāyen Shri Lakshmī ki seva karti hain।

Mere saath is sansār ke sukh bhogo,
Kuver ke dhan ka poora anand lo।
Tapasya, shakti, yash, dhan—
kisi mein bhi Rām mere barābar nahi।

Isliye piyo, khao, anand lo,
main tumhe poora jagat de dunga!”

🌊 Rāvaṇ ka swapn

“O Komalāṅgī,
mere saath samudra-tat ke pushpit upvanon mein vihar karo,
jahan kaale bhramar gunjan karte hain 🐝
aur tumhare sone ke kangan chamakte hain।”

🔥 Adhyāy 20 ka Saar

Rāvaṇ ka madhur par vishay-lobh se bhara prastāv

Dhan, rājya, shakti aur yauvan ka pralobhan

Rām ka apmān aur adharm-purn tark

Rāvaṇ ka ahankār — jo uske vināś ka beej hai"""
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
