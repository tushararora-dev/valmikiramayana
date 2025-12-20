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
        Chapter 21 – Sita Ravana ko thukraati hai (Hinglish Moral Story)

Ravana ke kathor shabd sun kar
Sita ka dil dukh se bhar gaya.
Woh kaanp rahi thi,
awaaz halki aur kamzor thi.
Phir bhi uska mann Rama par atal tha ❤️

Sita ne ek tinka (straw) uthaaya
aur apne aur Ravana ke beech rakh diya.
Ye uski maryada ka chinh tha.

Phir woh shaant muskura kar boli—"""
        create_image_text_layout("attached_assets/chapter5/5.21.jpg", text1, layout="side", image_position="left")

        text2 = """
        “Apna mann
apni patniyon par lagao, Ravana.

Jaise paapi swarg nahi pa sakta,
waise hi tum mujhe nahi paa sakte.

Jo kaam ek pativrata stree ke liye paap hai,
woh main kabhi nahi karungi.

Main achhe kul mein paida hui hoon,
aur dharmic parivaar ki bahu hoon.”

Itna kehkar
Vaidehi ne apna mukh pher liya
aur aage boli—

“Main kisi aur ki patni hoon,
isliye tumhari patni kabhi nahi ban sakti.

Achhe logon ke niyam follow karo.

Dusron ki patni
tumhari patni jaise hi raksha ke yogya hoti hai.

Apni patniyon mein hi santosh rakho.

Jo vyakti apni patniyon se bhi khush nahi hota,
woh dusron ki wajah se vinaash paata hai.”

Sita ki awaaz mein dard tha,
par shabd sach aur balwaan the ✨

“Jo raja apne mann par niyantran nahi rakhta,
uske haathon rajya aur nagar nash ho jaate hain.

Lanka dhan se bhari hai,
par tum jaise raja ke kaaran
iska vinaash nischit hai.

Jab tumhara ant aayega,
log kahenge—

‘Achha hua, ek atyachaari gira.’”

Phir Sita ne Rama ka naam liya,
aur uski aankhon mein vishwas chamak utha ✨

“Tum mujhe dhan ya vaibhav se nahi khareed sakte.

Jaise surya se uski roshni alag nahi hoti,
waise hi main Raghava se alag nahi ho sakti.

Jis bhuj par main tiki hoon,
woh Rama ki bhuj hai.

Kisi aur par main kaise aashrit ho sakti hoon?”

“Mujhe Rama ke paas lauta do.

Yeh tumhare hi hit mein hai.

Agar tum Lanka bachana chahte ho,
toh Rama se mitrata karo.

Woh sharan lene walon ka rakshak hai.”

Sita ki awaaz ab chetavani ban chuki thi ⚡

“Agar tumne aisa nahi kiya,
toh tumhara vinaash tay hai.

Tum Indra ke vajra se bach sakte ho,
par Rama ke dhanush ki garaj se nahi.

Jab us dhanush ki pratidhwani hogi,
Lanka ka har kona kaanp uthega.”

“Rama aur Lakshmana ke baan
aag ugalte saanp jaise honge.

Woh poori Lanka ko dhak lenge,
aur rakshason ka ant kar denge.”

Sita ne ant mein kaha—

“Jaise Vishnu ne teen pag mein
Shri ko Asuron se chheen liya tha,
waise hi mere swami mujhe tumse chheen lenge.

Tumne mujhe chori se uthaya,
kyunki tum unke saamne khade hone ki himmat nahi rakhte.

Sheron ke saamne
kutte kabhi nahi tikte.”

“Chahe tum Kubera ke lok mein chhupo
ya Varun ke rajya mein bhaago,
Rama ke baan se bach nahi paoge.

Jaise bijli ped ko gira deti hai,
waise hi tumhara ant hoga.”

🌸 Moral (Seekh):

💠 Pativrata aur maryada sabse badi shakti hoti hai

💠 Dharma par atal rehna hi sachchi vijay hai

💠 Ahankar aur anyay apna hi vinaash laata hai

💠 Sach aur shuddh prem kabhi harta nahi"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.22
    with st.expander("Chapter 5.22 – Ravana threatens Sita"):
        text1 = """
        Chapter 22 – Ravana ki Dhamkiyan (Hinglish Moral Story)

Sita ke sakht aur sachche shabdon ko sunkar
Ravana ka gussa bhadak utha 😠
Usne kathor awaaz mein jawab diya—

“Duniya kehti hai,
aurat jitni narmi dekhe, utni pighal jaati hai.

Par main jitni daya dikhata hoon,
tum utni hi mujhe thukraati ho.

Sirf mera prem hi
mere krodh ko roke hue hai.

Warna main ab tak
tumhe maar chuka hota.”"""
        create_image_text_layout("attached_assets/chapter5/5.22.jpg", text1, layout="side", image_position="left")

        text2 = """
        Ravana ki aankhon mein agni thi 🔥

“Tumne jo kadve shabd bole hain,
unke liye tum mrityu ki yogya ho.

Fir bhi prem ke kaaran
main tumhe jeene de raha hoon, Maithili.”

Phir Ravana ne bhayanak dhamki di—

“Main tumhe do mahine ka samay deta hoon.

Uske baad
tumhe meri patni banna hoga.

Agar tumne mana kiya,
toh mere rasoiyye
tumhare ang kaat kar
mere bhojan ke liye tayaar karenge.”

Yeh sunkar
Apsaraon aur Gandharv kanyaon ka dil kaanp gaya 😨
Unhone ankhon aur isharo se
Sita ko himmat di 🌸

Unse shakti paakar
Sita ne phir Ravana se kaha—
ab uski awaaz mein bhay nahi, chetavani thi ⚡

“Lagta hai Lanka mein
koi tumhara bhala chahne wala nahi.

Isliye koi tumhe
is paap se rok nahi raha.

Teenon lokon mein kaun
Rama ki patni ko chhoone ka
sahas karega?”

“Jaise gusse mein haathi
jungle ke khargosh ko kuchal deta hai,

waise hi tum, Ravana,
Rama ke saamne
tinke ke samaan ho.”

Sita ki aankhen aag si chamak rahi thi ✨

“Tum tabhi tak garajte ho
jab tak Rama saamne nahi hote.

Jab tumne
Dasaratha ke putra ki patni ko dhamkaya,

tumhari jeebh
sookh kyun nahi gayi?”

“Agar Rama ka aadesh hota,
toh main apni tapasya se
tumhe isi kshan
raakh bana deti.”

“Tumne mujhe chhal se uthaya,
Rama ko van se door bhej kar.

Yeh tumhari veerta nahi,
tumhari kayarata hai.”

Yeh sunkar
Ravana ka chehra aur bhi bhayanak ho gaya 😡
Woh kaale baadal jaisa lag raha tha,
badi-badi bhujaon ke saath,
aankhen laal,
jeebh agni si 🔥

Woh pahad jaise khada tha,
gehne aur malaon se saja hua.

Usne phir zehreeli awaaz mein kaha—

“Aaj main tumhe nasht kar dunga,
jaise sandhya mein
surya ki roshni mit jaati hai.”

Phir Ravana ne
bhayanak rakshasiyon ko dekha—
koi ek aankh wali,
koi haathi ke pair wali,
koi ghode jaise pair wali,
koi baal se bhari,
koi vikrit muh wali 😱

Ravana ne hukm diya—

“Dhamki se, lalach se,
meethi baaton se,
tohfe dekar—

kisi bhi tarah
Sita ko mere paksh mein karo.”

Tab ek rakshasi
Dhanyamalini aage badhi
aur Ravana ko gale lagakar boli—

“Maha Raja,
is manushya stree ke peeche kyun pade ho?

Main hoon na tumhare saath.

Jo zabardasti prem karta hai,
use sirf dukh milta hai.

Par jahan prem dono taraf ho,
wahan hi sachcha sukh hota hai.”

Dhanyamalini Ravana ko le jaane lagi.
Ravana thahaka maar kar hansa 😏
aur phir mahal ki ore chal pada.

Dharti uske kadmon se kaap uthi 🌍
Aur Ravana
apne chamakte mahal mein chala gaya.

Sita wahin reh gayi…
kaamp rahi thi,
par uska mann ab bhi Rama mein sthir tha ❤️

🌸 Moral (Seekh):

💠 Dhamki aur bal se prem nahi jeeta ja sakta

💠 Ahankar ant ko bulata hai

💠 Dharma aur satya sabse badi raksha hote hain

💠 Sita jaise dridh vishwas se hi burai harti hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.23
    with st.expander("Chapter 5.23 – The demon women try to convince Sita"):
        text1 = """
        Chapter 23 – Rakshasiyan Sita ko Ravana se shaadi ke liye manati hain

Ravana dhamki dekar
aur rakshasiyon ko aadesh dekar
wahan se chala gaya.

Woh apne mahal ke andar chala gaya.

Jaise hi Ravana gaya,
bhayanak dikhne wali rakshasiyan
Sita ke paas aa gayin 😠
Unki awaaz kathor thi,
aankhon mein gussa bhara tha."""
        create_image_text_layout("attached_assets/chapter5/5.23.jpg", text1, layout="side", image_position="left")

        text2 = """
        Unhone Sita se kaha—

“O Sita,
tum Ravana jaise mahaan rakshas ke saath
sambandh ki keemat nahi samajh rahi.

Woh Paulastya ke vansh ka hai,
Dashagriva, mahaan aur shaktishaali!”

Phir unmein se ek rakshasi,
Ekjata, gusse se boli—

“Sita, suno!
Paulastya
Brahma ke chhe putron mein se ek the.

Unse Vaishravas hue,
aur unke putra hain Ravana.

Itne mahaan vansh ka raja
tumhe apni patni banana chahta hai.

Tum mana kyun karti ho,
O sundar roop wali?”

Phir doosri rakshasi
Harijata aage aayi.
Uski aankhen billi jaisi ghoom rahi thi 😡

“Woh Ravana hai
jisne 33 devtaon ko
aur unke raja Indra ko
yudh mein hara diya.

Tum aise veer ke saath
shaadi kyun nahi karna chahti?

Woh kabhi yudh se peechhe nahi hatta.

Mandodari jaisi rani ko chhod kar
woh sirf tumhe chahta hai.

Tum uske sundar mahal mein rahogi,
hazaaron abhushan pehnogi,
aur woh tumhari pooja karega!”

Uske baad ek aur rakshasi,
Vikata, boli—

“Ravana baar-baar
Gandharvon, Nagas aur Danavon ko
yudh mein hara chuka hai.

Itna dhanwaan aur shaktishaali raja
jab khud tumhe chaahe,
toh tum kyun inkaar karti ho?”

Phir Durmukhi naam ki rakshasi
aage badhi aur boli—

“O sundar netron wali nari,
us Ravana se kyun nahi darti
jiske bhay se
suraj tej se nahi chamakta,
hawa dheemi behne lagti hai,
ped phool gira dete hain,
aur pahaad aur badal
paani barsa dete hain?”

Uski awaaz aur kathor ho gayi 😠

“Yeh sab hum
tumhare bhale ke liye keh rahe hain.

Ravana ko apna pati maan lo.

Agar tumne mana kiya,
toh nishchit samjho—
tumhari mrityu ho jayegi!”

Sita chup thi…
kamzor nahi,
par dridh aur sthir 🌸

Uska mann ab bhi
sirf Rama mein basa tha ❤️

🌼 Moral (Seekh):

💠 Bal aur bhay se dharma nahi badalta

💠 Sachcha prem dabav se nahi hota

💠 Sita ka vishwas humein sikhata hai –
satya par tikke rehna hi sabse badi shakti hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.24
    with st.expander("Chapter 5.24 – The demon women scare and threaten Sita"):
        text1 = """
        Chapter 24 – Rakshasiyon ki bhayanak dhamki (Menace of the Female Titans)

Sabhi bhayanak rakshasiyan
ek saath Sita par chilla padiं 😠
Unke shabd kathor the,
dil ko chubhne wale.

Woh boli—"""
        create_image_text_layout("attached_assets/chapter5/5.24.jpg", text1, layout="side", image_position="left")

        text2 = """
        “Sita,
tum Ravana ke mahal mein
sukh se kyun nahi rehti?

Woh mahal sona-chaandi se bhara hai,
komal bistar aur sukh hi sukh hai.

Tum kyun ek saadharan insaan Rama
ke liye ro rahi ho?

Rama ko bhool jao.
Tum use dobara kabhi nahi dekhogi.

Ravana teenon lokon ka dhan rakhta hai.
Usi ke saath raho aur khush raho.

Tum ek aurat ho,
phir kyun us aadmi ke liye dukh karti ho
jo rajya se nikaal diya gaya hai
aur kasht bhari zindagi jee raha hai?”

Yeh sab sunkar
Sita ki kamal jaisi aankhon mein aansu aa gaye 🌸😢
Par uski awaaz shant thi,
par vishwas se bhari.

Sita boli—

“Tum jo keh rahi ho,
woh adharm hai.

Ek manav stree
rakshas ki patni nahi ban sakti.

Agar chaho toh
mujhe kha jao,
par main kabhi haan nahi kahungi.

Mera pati chahe gareeb ho,
chahe rajya se vanvaasit ho,
par wahi mere liye
guru aur devta hai.

Jaise
Saci Indra ke saath rehti hai,
Arundhati Vasishtha ke saath,
Damayanti Nala ke saath—

waise hi
main sirf Rama ke saath hoon.”

Sita ke shabd sunkar
rakshasiyan aur bhi gusse mein aa gayin 🔥
Unhone use gher liya.

Hanuman chupchaap
Shingshapa vriksh par baitha
sab kuch dekh aur sun raha tha 🐒🌳

Rakshasiyan bhala-bhala bolte hue,
honth chaat-te hue,
bhale bhale hathiyaaron ke saath
Sita ko dhamkane lagin—

“Kya tumhe lagta hai
Ravana tumhara pati banne layak nahi? 😡”

Dar se kaanpte hue,
Sita ne apne aansu ponchhe
aur Shingshapa ke neeche baith gayi.
Uske kapde gande ho chuke the,
chehra peela pad gaya tha,
dil dukh se bhara tha 💔

Par uska dharm ab bhi majboot tha.

Phir ek bhayanak rakshasi
Vinata chilla kar boli—

“Bas karo ab!
Tum apni pativratta dikha chuki ho.

Ab hamari baat maan lo.

Ravana ko apna pati maan lo.

Rama bechara hai,
uski zindagi bhi zyada nahi bachi.

Agar tumne hamari baat na maani,
toh hum tumhe abhi kha jayenge!”

Doosri rakshasi Vikata ne gusse mein
mutthi bheench kar kaha—

“Sita,
tum samajhti kyun nahi?

Tum samundar ke us paar ho
jahan koi nahi aa sakta.

Ravana ne tumhe qaid kiya hai.
Indra bhi tumhe chhuda nahi sakta.

Jawani jaldi khatam ho jaati hai.

Jab tak hai,
Ravana ke saath sukh bhogo.

Agar mana kiya,
toh main tumhara dil phaad kar kha jaungi!”

Phir Chandari naam ki rakshasi
bhala ghumate hue boli—

“Is stree ko dekh kar
mujhe ise kha jaane ka mann kar raha hai.”

Praghasa boli—

“Isse baat karna bekaar hai.
Iski saans bandh kar dete hain.”

Ajamukhi aur Shurpanakha bhi hans kar boli—

“Isse maar kar
hum naachenge aur sharab piyenge!”

Yeh sab bhayanak dhamkiyan sunkar
Sita ka dhairya toot gaya 😢
Devkanya jaisi Sita
phoot-phoot kar rone lagi.

Par uske aansuon ke beech bhi
ek sach chamak raha tha—

✨ Rama ke prati uska vishwas abhi bhi zinda tha.

🌼 Moral (Seekh):

💠 Sita ka dhairya dikhata hai ki sachcha dharm akela bhi majboot hota hai

💠 Dhamki aur bhay se satya nahi badalta

💠 Andhkaar jitna bhi ghera ho, vishwas ki roshni bujh nahi sakti"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.25
    with st.expander("Chapter 5.25 – Sita feels hopeless"):
        text1 = """
        Chapter 25 – Sita ka mann tootna (Sita gives way to Despair)

Rakshasiyon ki bhayanak dhamkiyon ne
Sita ka dil tod diya 😢
Janak ki beti, Vaidehi,
ab apne aansu rok nahi paayi.

Tooti hui awaaz mein,
siskiyon ke beech,
woh boli—

“Ek manav stree
kabhi rakshas ki patni nahi ban sakti.

Chahe tum mujhe tukdon mein kaat do,
par main tumhari baat
kabhi nahi maanungi.”"""
        create_image_text_layout("attached_assets/chapter5/5.25.jpg", text1, layout="side", image_position="left")

        text2 = """
        Rakshasiyon se ghiri hui,
Ravana ke darr se kaanpti hui,
Sita ko kahin bhi sharan nahi mili.
Woh zor-zor se kampne lagi,
jaise jungle mein
hirni apne jhund se bichhad jaaye
aur charon taraf bhookhe bhediye hon 🦌🐺

Ashoka ke ped ki phoolon bhari shaakh
ko pakad kar,
Sita gham mein doob gayi. 🌸
Uska mann sirf
apne prabhu Rama ko yaad kar raha tha.

Aansoon ki dhaar
uske komal vaksh par beh rahi thi.
Dukh itna gehra tha
ki use uska ant dikhai nahi de raha tha.

Woh zameen par gir padi,
jaise aandhi mein
kele ka ped jad se ukhad jaata hai 🌪️
Darr se uska chehra safed pad gaya.
Uski lambi choti
hil rahi thi,
jaise koi saanp sarakta ho 🐍

Dukh se bhar kar,
Sita rone lagi
aur karun swar mein pukaarne lagi—

“O Rama!” 😭
“O Lakshmana!”
“O Maa Kaushalya!”
“O Maa Sumitra!”

Phir woh boli—

“Sach hi kaha hai rishiyon ne—
koi bhi jeev
apne samay se pehle nahi marta.

Itna dukh,
itna kasht hone ke baad bhi
main abhi zinda hoon.

Haay!
Main kitni abhagi hoon.

Apne rakshak se door,
main aise doob rahi hoon
jaise toofan mein
bhara hua jahaz samundar mein doob jaata hai.

Rama ke bina
main us kinare ki tarah hoon
jo tez dhaara se dheere-dheere gir jaata hai.”

Uski aankhon mein
Rama ki chhavi thi 🌼

“Kitne bhaagyashali hain woh
jo mere prabhu ko dekh paate hain.

Jinki aankhein phoolon jaisi hain,
chal sher jaisi hai,
jo kritagy aur madhur vaani wale hain.

Rama ke bina
saans lena bhi mushkil lag raha hai,
jaise kisi ne zehar pee liya ho.

Ab meri zindagi bas ant ki ore hai.”

Phir woh khud se poochhne lagi—

“Maine pichhle janm mein
kaunsa bada paap kiya hoga
jo mujhe aaj
itna bhayanak dukh mil raha hai?

Mera mann marna chahta hai,
par yeh rakshasiyan
mujhe jeene par majboor kar rahi hain.

Haay!
Insaan hona hi shraap hai,
doosron par nirbhar rehna bhi shraap hai.

Jab insaan marna chahe
tab bhi mar nahi sakta.”

🌸 Moral (Seekh):

💠 Sita ka dukh dikhata hai ki sabse pavitra log bhi kathin samay se guzarte hain

💠 Sachcha prem aur dharm kabhi kamzor nahi hota, chahe mann toot jaaye

💠 Umeed ka diya kabhi bujhata nahi, bas hawa tez hoti hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.26
    with st.expander("Chapter 5.26 – Sita predicts the destruction of the demons"):
        text1 = """
        Chapter 26 – Sita ka bhavishyavani: Rakshason ka vinash (Sita prophesies the Titan’s Destruction)

Aankhon se aansu behte hue,
sir jhukaye hue,
Janak ki beti Sita
phir se vilap karne lagi 😢

Dukh se pagal si hokar,
woh zameen par lotne lagi,
jaise kisi nanhe ghode ka bachcha
maa se bichhad gaya ho.

Woh cheekh kar boli—

“Main Raghava ki patni hoon.
Phir bhi main dhokhe se
rakshason ke jaal mein phans gayi.

Nirdayi Ravana mujhe utha le gaya.

Rakshason ke beech bandi ban kar,
unki gaaliyon aur dhamkiyon ko sunte hue,
ab mujhse jeena bardasht nahi hota.”"""
        create_image_text_layout("attached_assets/chapter5/5.26.jpg", text1, layout="side", image_position="left")

        text2 = """
        Uska mann bhar aaya—

“Rama ke bina
jeevan, dhan aur gehne
kis kaam ke hain?

Shayad mera hriday lohe ka hai,
jo itne dukh ke baad bhi
toota nahi.

Dhikkar hai mujh par,
jo apne swami ke bina bhi
saans le rahi hoon.”

Woh gusse aur dridhata se boli—

“Mera baayã pair bhi
us rakshas ko sparsh nahi karega.

Ravana jaise paapi se
main prem kaise kar sakti hoon?

Chahe mujhe tukdon mein kaat diya jaaye,
ya aag mein jala diya jaaye,
main kabhi Ravana ke aage
explains nahi karungi.”

Phir usse Rama yaad aaye 💔

“Rama dharmic, kritagy aur karunamay hain.

Janasthana mein
unhone akele hi
14,000 rakshason ka vinash kiya tha.

Agar unhe pata hota
ki main yahan Lanka mein hoon,
toh kya woh chup rehte?”

Uski aankhon mein vishwas chamak utha 🔥

“Samundar bhi unke teeron ko
nahi rok sakta.

Lanka kitni bhi door ho,
Rama mujhe paakar rahenge.

Jis din unhe sach pata chalega,
Lanka jal uthegi.”

Woh bhavishyavani karne lagi—

“Har ghar se rakshasiyon ka rona uthega.

Jinke pati mare jaayenge,
woh bilakhengi.

Lanka,
shav-dah sthalon ke dhuẽ se bhar jaayegi.

Gidh mandrayenge,
aur nagar shamshan jaisa lagega.”

Sita ne spasht shabdon mein kaha—

“Ravana ka vinash nishchit hai.

Uske marne ke baad,
Lanka ek vidhwa nagri ban jaayegi.

Apni shaan kho degi.

Rama ke laal kinare wali aankhon ke
teer
poori nagri ko bhasm kar denge.”

Phir uski awaaz kamzor ho gayi…

“Shayad Ravana ne
mujhe apne bhojan ke liye soch liya hai.

Main asahaya hoon.

Rama ke bina
main kuch nahi kar sakti.”

Nirasha us par chha gayi 🌑

“Agar Rama aur Lakshmana zinda hote,
toh woh poori dharti chhaan maarte.

Shayad woh bhi
rakshason ke haathon mare gaye hon.

Agar aisa hai,
toh mrityu hi mere liye shreshth hai.”

Ant mein,
Sita ne gehri saans le kar kaha—

“Dhanya hain woh mahatma
jo ichha aur dwesh se pare hain.

Jinhe na prem bandhata hai,
na ghrina jalaati hai.

Unhe mera pranam 🙏

Rama se bichhad kar,
dusht Ravana ke adheen hokar,
ab main apna jeevan
tyaag dena chahti hoon.”

🌸 Moral (Seekh):

💠 Sachcha dharm gir kar bhi haar nahi maanta

💠 Paap ka ant nishchit hota hai, chahe samay lage

💠 Vishwas aur satya, andhere mein bhi deepak jaise hote hain"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.27
    with st.expander("Chapter 5.27 – Trijata tells her dream"):
        text1 = """
        Chapter 27 – Trijata ka Sapna (Trijata’s Dream)

Sita ke shabd sunkar
rakshasiyan aur bhi gusse mein aa gayi 😡
Kuch turant bhaag kar
Ravana ko sab batane chali gayi.

Baaki rakshasiyan phir se
Sita ko daraane lagi.

“Kya samajhti ho khud ko, Sita?
Aaj hi hum tumhara maans kha jaayengi.
Jin rakshason ke vinash ki baat tum karti ho,
aaj wahi tumhe kha jaayenge.”"""
        create_image_text_layout("attached_assets/chapter5/5.27.jpg", text1, layout="side", image_position="left")

        text2 = """
        Yeh sab dekh kar
Trijata, jo buddhi aur anubhav se bhari thi,
aage aayi.

Uski awaaz shaant thi,
par shabdon mein gehra vishwas tha।

“Arre moorkhon!
Agar kisi ko khaana hai toh mujhe kha lo,
par Sita ko haath mat lagana.

Woh Janak ki beti hai,
aur Raja Dasharath ki bahu.

Kal raat maine ek bhayankar sapna dekha hai.
Aisa sapna jo rakshason ke vinash
aur is stri ke pati ki vijay batata hai.”

Yeh sunkar
sab rakshasiyan thodi ghabra gayi 😰
aur cheekh kar boli:

“Achha?
Toh sapna poora batao!
Kya dekha tumne?”

Tab Trijata ne apna sapna sunaya—

“Maine dekha
ek divya rath,
jo haathi-daant ka bana tha.

Usse sau hans kheench rahe the.

Us rath mein
Rama aur Lakshmana the,
chamakte vastron mein,
phoolon ki mala pehne hue.”

“Phir maine dekha
Sita ko,
shuddh safed vastron mein.

Woh ek safed parvat par khadi thi,
samundar se ghiri hui.

Aur woh Rama se mil rahi thi,
jaise surya se roshni milti hai ☀️”

“Phir Rama ek vishal haathi par baithe the,
chaar daanton wala,
aur Lakshmana saath mein the.

Dono veer
apni tej se chamak rahe the.

Sita unke paas aayi
aur haathi par chadh gayi.”

“Phir maine dekha
Sita ne apne haath se
surya aur chandra ko chhoo liya.

Aur phir
Rama, Lakshmana aur Sita
Lanka ke upar khade the.”

Uske baad Trijata ka swar aur kathor ho gaya—

“Aur phir maine Ravana ko dekha.

Zameen par gira hua.
Sir munda hua.
Tel mein lipta hua.
Laal kapde pehne.

Pushpak vimaan se girta hua.

Ek kaali stri
uski gardan mein rassi daal kar
use maut ki disha mein kheench rahi thi.”

“Kumbhakarna aur Ravana ke putron ko bhi dekha.

Sabke sir munde hue the.
Sab tel mein lipte hue.

Sirf Vibhishan
safed chhatri ke neeche khada tha,
apne mantriyon ke saath.”

“Lanka jal rahi thi 🔥

Darwaaze toot rahe the.

Rakshas zameen par gir rahe the.

Shehar samundar mein doob raha tha.”

Phir Trijata ne sab rakshasiyon ko chetavani di—

“Bas karo ab!

Rama Sita se milne hi wale hain.

Agar tumne is pavitra stri ko
aur sataya,
toh Rama tum sab ka vinash kar denge.

Ab use darao mat.
Usse maafi maango.

Uske pairon mein giro.

Sirf Sita hi
tumhe is maha-vinaash se bacha sakti hai.”

Usne Sita ki aur dekh kar kaha—

“Is devi mein
koi dosh nahi.

Uska dukh
sirf ek chhaya jaisa hai,
jo ab mitne wala hai.”

Phir Trijata ne
shubh sanket bataye—

“Sita ki baayi aankh ka phadakna,
baayã baahu aur jaangh ka kaanpna—

yeh sab vijay ke chinh hain.

Pakshi bhi pedon par ga rahe hain,
jaise shubh ghadi ka sandesh de rahe hoon 🐦”

Yeh sab sunkar
Sita ke chehre par
pehli baar halki si roshni aayi ✨

Usne dheere se kaha—

“Agar yeh sab sach hua,
toh main tum sabki raksha karungi.”

🌸 Moral (Seekh):

💠 Sach aur dharm ka saath dene wale ko hamesha shakti milti hai

💠 Sapne kabhi-kabhi bhavishya ka darpan hote hain

💠 Ghamand ka ant aur bhakti ki vijay nishchit hoti hai
"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.28
    with st.expander("Chapter 5.28 – Sita cries and laments"):
        text1 = """
        Chapter 28 – Sita ka Vilap (Sita’s Lament)

Ravana ke kathor aur nirdayi shabd sun kar
Sita ka sharir kaanp utha —
jaise jungle ke kinaare
sher ke hamle se
ek madha-hathi kaanp jaata ho 🐘🦁

Ravana ki dhamkiyon se
aur charon taraf se rakshason se ghir kar
woh komal hriday wali rajkumari
poori tarah niraasha mein doob gayi,
jaise koi chhoti si ladki
ghane jungle mein akeli chhod di gayi ho."""
        create_image_text_layout("attached_assets/chapter5/5.28.jpg", text1, layout="side", image_position="left")

        text2 = """
        Sita apne mann mein sochne lagi:

“Rishiyon ki baat sach hai—
mrityu apne nirdharit samay se pehle nahi aati.

Itni apmaan aur peeda ke baad bhi
main abhi tak jeevit hoon.

Mera hriday kitna kathor hoga
jo aaj bijli se tootne wale parvat-shikhar ki tarah
sau tukdon mein nahi bikhra!”

“Ismein mera dosh nahi.

Woh bhayanak rakshas
mujhe maar sakta hai,
par jaise ek brahman
neeche jaati ke vyakti ko
ved-vidya nahi de sakta,
waise hi main
Ravana ko apna prem
kabhi nahi de sakti.”

Uske mann mein bhay aur bhi gehra ho gaya:

“Agar do maheene ke andar
mere prabhu prakat nahi hue,
toh woh neech Ravana
mujhe apne tez shastron se
tukdon mein kaat daalega—

jaise koi vaidya
maa ke hriday se
garbh ko cheer kar nikaal deta hai.”

“Yeh do maheene
pal bhar mein beet jaayenge,
aur main bhi
us chor ki tarah
mrityu ke liye le jaayi jaungi
jo raat khatam hote hi
dand ke liye bandha jaata hai.”

Phir Sita ka vilap aur gehra ho gaya:

“O Rama!
O Lakshmana!
O Sumitra Maa!
O Kaushalya Maa!

Main toofan mein phansi hui
doobti hui naav ki tarah
nash hone wali hoon.”

“Nishchit hi woh dono veer rajkumar
us maaya-mrig ke jaal mein phans kar
bijli se ghayal sher ya bail ki tarah
gir pade honge.

Bhagya ne hi
us hiran ka roop lekar
mujhe bhramit kiya—
aur meri moorkhta se
maine Rama aur Lakshmana ko
uske peeche bhej diya.”

“O Rama!
Satya-vrat dhari!
Lambi bhujon wale!

Jiska mukh poornima ke chandra jaisa hai! 🌕

Tum sab praniyon ke mitra aur rakshak ho,
aur tumhe pata bhi nahi
ki main rakshason ke haathon
mrityu ke nikat hoon.”

“Mere liye
jiske sivay koi devta nahi,
meri tapasya,
mera zameen par sona,
mera dharm aur pativrata—

sab vyarth ho gaye,
jaise kisi kritaghn ke liye ki gayi seva.”

“Tum apne pita ki aagya ka palan karke,
apna vrat poora karke,
van se laut kar
shantipurn jeevan jeeyoge,
anek sundar striyon ke saath.

Aur main—
jo tumse nishtha se prem karti thi—
apni hi bhakti ke kaaran
nash ho rahi hoon.”

“Main vish ya shastra se
apna jeevan samapt kar leti,
par is rakshason ke nagar mein
koi mujhe woh bhi dene wala nahi.”

Is gehre shok mein doob kar
Sita ne apne keshon ka bandhan khol diya
aur boli:

“Isi rassi se
main apna jeevan samaapt karungi
aur mrityu ke lok ko prapt ho jaungi.”

Us sundar, komal aur pavitra Sita ne
us ped ki shaakh pakad li
jiske neeche woh khadi thi
aur Rama, Lakshmana aur apne parivaar
ka smaran karne lagi 🌿

Tab achanak—
kai shubh lakshan prakat hue ✨
jo duniya bhar mein mangal ke chinh maane jaate hain:

Hriday ko shanti dene wale sanket

Bhay ko door karne wale anubhav

Aasha jagane wali spasht soochna

Yeh sab is baat ka sanket the
ki Sita ka dukh ab samapt hone wala hai
aur aane wala samay shubh hai 🌸

🌼 Moral (Seekh):

🔹 Dharm aur nishtha kabhi vyarth nahi jaati

🔹 Jab andhera sabse gehra hota hai, tabhi ujala nikat hota hai

🔹 Bhagya pariksha leta hai, par satya ka saath kabhi nahi chhodta"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.29
    with st.expander("Chapter 5.29 – Sita notices good signs of hope"):
        text1 = """
        Chapter 29 – Sita ko Shubh Sanket Dikhai Dete Hain

Jab woh nirdosh aur sundar Sita
abhi bhi chinta aur bhay mein doobi hui thi,
tab achanak uske chaaron taraf
shubh sanket dikhai dene lage ✨
bilkul waise jaise
kisi dhani vyakti ke charon taraf
sevak khade ho jaate hain.

Sita ki badi aur sundar baayi aankh,
jiska putli gehra kaala tha,
halke-halke phadakne lagi 👁️
jaise paani mein machhli ke hilaane se
kamal ka phool ghoom jaata ho 🌸"""
        create_image_text_layout("attached_assets/chapter5/5.29.jpg", text1, layout="side", image_position="left")

        text2 = """
        Uski komal baayi bhuja,
jo kabhi
Chandan aur Agaru se sugandhit thi
aur jo pehle
uske prabhu Rama ka takiya bani thi,
baar-baar kaanpne lagi 🤍

Uski baayi jangh,
jo haathi ki patli sundar soond jaisi thi,
achanak hilne lagi 🐘
yeh sanket tha
ki Sita jaldi hi Rama ko dekhegi.

Uski sunehri saari,
jo ab dhool se bhar chuki thi,
uske sundar kandhon se
dheere se phisal gayi.
Maithili ke daant
anar ke beej jaise chamak rahe the 🍎

In sab mangal chinhon ko dekh kar
Sita ke mann ko tasalli mili 💛
uske hriday mein
nayi aasha jaag uthi.

Woh Sita,
jo abhi tak
dhoop aur tez hawa se
sookhi hui lata jaisi lag rahi thi,
ab
der se aayi baarish se jeevit hone lagi 🌧️🌱

Uska chehra phir se chamak utha ✨
uske Bimba phal jaise hoth,
sundar aankhen,
palakon ka ghoomav,
aur tez chamakte daant—
sab apni pehli sundarta mein laut aaye
jaise Rahu ke muh se chhoot kar
chandrama phir se chamak uthe 🌕🌙

Uska niraasha door ho gayi,
thakaan mit gayi,
mann ka jvar shaant ho gaya,
aur dukh dheere-dheere pighal gaya ❄️➡️💧

Uska hriday
ab aanand se bhar gaya
aur woh mahaan nari
phir se utni hi sundar lagne lagi
jitna shukla paksh ka sheetal chandra 🌙✨

🌼 Moral (Seekh):

🔹 Jab bhagya badalne wala hota hai, prakriti khud sanket deti hai

🔹 Aasha ka ek chhota sa chinh bhi jeevan ko roshan kar sakta hai

🔹 Sachchi nishtha ka phal avashya milta hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.30
    with st.expander("Chapter 5.30 – Hanuman thinks about what to do next"):
        text1 = """
        Chapter 30 – Hanuman ke Vichaar (Hinglish Moral Story Style)

Veer Hanuman,
jo ped ki shaakhon mein chhupa hua tha,
Sita, Trijata aur rakshasiyon ki
saari baatein dhyaan se sun chuka tha.

Woh upar se
Sita ko dekhta raha 🌸
jo Nandana van ki apsara jaisi lag rahi thi.
Uske mann mein
bahut saare vichaar aane lage."""
        create_image_text_layout("attached_assets/chapter5/5.30.jpg", text1, layout="side", image_position="left")

        text2 = """
        Hanuman ne socha:

“Jise hazaaron, lakhon vanar
har jagah dhoondh rahe the,
woh Sita yahin hai.
Aur use dhoondhne wala
main hoon.”

“Main ek chatur doot ban kar
is nagari mein aaya hoon.
Maine Ravana ki shakti,
rakshason ki sena,
aur Lanka ke saare raaz dekh liye hain.”

“Ab mera kartavya hai
is dukh se tooti hui nari ko
dhaarash dena 💛
jo apne prabhu Rama ke liye
pal-pal tadap rahi hai.”

“Agar main bina use santvana diye
wapis chala gaya,
toh meri yatra vyarth ho jaayegi.”

Hanuman ka mann aur bhaari ho gaya:

“Agar main kuchh na bola,
toh yeh pavitra Sita
aasha chhod degi…
aur shayad apna jeevan bhi.”

“Phir Rama poochhenge:
‘Sita ne kya kaha?’
Aur agar maine usse baat hi na ki,
toh main kya uttar doonga?”

Phir Hanuman ne socha:

“Lekin rakshasiyon ke saamne
baat karna asambhav hai.”

“Agar main
manushya jaise shabd
ya shuddh Sanskrit boloon,
toh Sita mujhe
Ravana samajh sakti hai 😨”

“Woh darr ke chilla degi,
aur sab rakshasi
hathiyaar le kar mujh par toot padegi.”

“Yadi yudh hua,
toh ya toh main thak jaunga
ya pakad liya jaunga.”

“Aur sabse bura yeh—
un rakshasiyon ke krodh mein
Sita ko hi maar diya jaa sakta hai.”

“Tab Rama aur Sugreev ka
poora yojna hi nasht ho jaayega.”

Hanuman gehri soch mein pad gaya:

“Yudh hamesha anishchit hota hai ⚔️
aur ek doot ko
soch-samajh kar hi kaam karna chahiye.”

“Ek galat kadam
poori yatra ko bigaad sakta hai.”

Phir achanak
Hanuman ke mann mein
ek uttam upaay aaya ✨

Woh bole (mann hi mann):

“Main Rama ka naam loonga.”

“Main Rama ke gun gaaunga.
Unki daya, unka dharm,
unka veerta—
sab kuchh meethi awaaz mein kahunga.”

“Rama ka naam sunte hi
Sita ka mann shaant ho jaayega 🌼
kyunki uska hriday
hamesha Rama mein basa hai.”

“Is tarah woh mujhse daregi nahi,
aur meri baat sunegi.”

Hanuman ne dridh nischay kiya:

“Main kuchh bhi karunga,
lekin Sita ko aasha doonga.”

“Main apna roop chhota hi rakhunga,
aur awaaz komal aur sachi hogi.”

Aur phir… 🌿
Maha-veeri Hanuman,
ped ki shaakh se
neeche Sita ko dekhte hue,
madhur aur nirmal swar mein bolna shuru karte hain—

🌼 Rama ka naam le kar…

🌟 Moral (Seekh):

🔹 Sahi samay par sahi shabd sab kuchh badal dete hain

🔹 Sachcha doot sirf bal se nahi, buddhi se jeet ta hai

🔹 Aasha dena sabse bada sahas hota hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.31
    with st.expander("Chapter 5.31 – Hanuman praises Lord Rama"):
        text1 = """
        Hanuman ne sab kuch soch liya.
Kab bolna hai.
Kaise bolna hai.

Phir wo bahut meethi awaaz mein bole.
Unki baatein seedha Sita ke dil tak pahunch rahi thi."""
        create_image_text_layout("attached_assets/chapter5/5.31.jpg", text1, layout="side", image_position="left")

        text2 = """
        “Ek mahaan raja the.
Unka naam tha Dasharath.

Unke paas rath the.
Ghode the.
Haathi the.

Par sabse badi baat,
unka dil daya se bhara tha.

Wo kisi ko dukh dena nahi chahte the.
Wo Ikshvaku vansh ki shaan the.”

“Unke sabse bade putra ka naam tha Rama.
Unka chehra chand jaisa chamakta tha.

Wo buddhi mein tez the.
Dhanush chalane mein sabse shreshth the.

Wo apne vachan par atal rehte the.
Sabka raksha karte the.
Dharm ke rakshak the.”

“Pita ke vachan ke liye,
Rama ne rajya chhod diya.

Apni patni Sita
aur bhai Lakshman ke saath
wo van chale gaye.”

“Van mein rehkar bhi,
Rama chup nahi rahe.

Jo rakshas logon ko satate the,
un sab ka ant kiya.

Janasthan mein
Khara aur Dushan ko maara.”

“Yeh sun kar Ravana gusse se jal utha.
Usne chal se kaam liya.

Marich ko sone ka hiran banaya.
Rama ko van ke andar kheench liya.

Aur phir
Sita ko utha le gaya.”

“Rama toot nahi gaye.
Wo Sita ko dhoondhne nikle.

Van mein unki dosti hui
Sugriva naam ke vanar raja se.”

“Rama ne Bali ka ant kiya.
Sugriva ko rajya diya.

Phir hazaaron vanar
chaaro dishaon mein bheje gaye.”

“Main unhi mein se ek hoon.
Mera naam Hanuman hai.

Sampati ke kehne par
main samundar paar karke yahan aaya.

Chaar sau yojan ka samundar
maine ek chhalaang mein paar kiya.”

“Rama ne mujhe bataya tha
aapki sundarta,
aapke lakshan,
aapki pavitrata.

Isi liye
main aapko pehchaan paya.”

Yeh kehkar
Hanuman chup ho gaye.

Sita hairaan reh gayi.
Unhone apne uljhe baalon ko hataya.
Aur Shingshapa ped ki taraf dekha.

Unka mann anand se bhar gaya.
Rama ka naam sunte hi
unka dukh halka ho gaya.

Chaaro dishaon mein dekhte hue,
unhone ped par dekha
Vayu-putra Hanuman ko.

Wo ugte hue suraj jaise chamak rahe the.
Sugriva ke mantri.
Buddhi aur bal ka adbhut sangam.

🌼 Seekh (Moral)

💛 Sachchi bhakti meethi boli se pehchaani jaati hai

🔥 Rama ka naam sunkar bhi umeed jeeti uthti hai

🌿 Sahi samay par sahi shabd chamatkaar karte hain"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.32
    with st.expander("Chapter 5.32 – Sita notices Hanuman"):
        text1 = """
        Sita ne us vanar ko dekha.
Wo ped ki shaakhon mein chhupa tha.

Safed vastra pehne hue.
Bijli ki chamak jaisa.
Ashok ke phoolon jaise chamakta hua.
Jaise sona aag mein tap kar nikla ho.

Sita ka dil zor se dhadakne laga."""
        create_image_text_layout("attached_assets/chapter5/5.32.jpg", text1, layout="side", image_position="left")

        text2 = """
        Us vanar ka chehra shaant tha.
Par Sita darr gayi.

Unhone mann hi mann socha,
“Yeh kaisa bhayanak vanar hai?
Dekhne mein ajeeb aur darawna.”

Unka darr aur badh gaya.
Aankhon se aansu behne lage.

Sita zor se boli,
“O Rama!
O Rama!
O Lakshmana!”

Unki awaaz dheere-dheere kamzor ho gayi.

Phir unhone dobara us vanar ko dekha.
Wo vinamr tha.
Sir jhukaye khada tha.

Sita ne mann mein kaha,
“Yeh shayad sapna hai.”

Us vanar ke chehre par gehre nishaan the.
Par uski aankhon mein daya aur gyaan tha.

Wo Vayu-putra Hanuman the.
Vanaron mein Indra jaise.

Yeh dekh kar
Sita behosh ho gayi.
Jaise jaan hi chali gayi ho.

Thodi der baad
unhe hosh aaya.

Unhone socha,
“Vanar ko sapne mein dekhna
shastron ke hisaab se ashubh hota hai.

Kya Rama theek honge?
Lakshmana ke saath honge?
Mere pita Janak surakshit honge?”

Phir unhone mann mein kaha,
“Par yeh sapna kaise ho sakta hai?
Main toh dukh mein so bhi nahi pa rahi.

Rama se door rehkar
mere jeevan mein koi sukh nahi.”

“Main din-raat
sirf Rama ke baare mein sochti hoon.

Isliye shayad
mujhe sab kuch Rama se juda hi dikhai deta hai.”

“Par agar yeh sirf bhram hota,
toh iski koi aakriti nahi hoti.

Par yeh vanar
saaf-saaf dikh raha hai.
Aur bol bhi raha hai.”

Sita ne aankhen band ki.
Aur mann hi mann prarthna ki:

“Hey Vachaspati Dev!
Hey Indra Dev!
Hey Brahma ji aur Agni Dev!

Kripya yeh vardaan do
ki jo mere saamne khada hai
wo sach ho,
sirf mera bhram na ho.”

Sita ka dil ummeed aur darr ke beech jhool raha tha.
Par kahin na kahin,
ek chhoti si roshni jal uthi.

🌼 Seekh (Moral)

🌱 Bahut zyada dukh mein bhi mann sach aur bhram ko pehchanne ki koshish karta hai

💛 Shraddha aur prarthna mushkil samay mein sahara banti hai

🌟 Umeed kabhi achanak roop mein saamne aa jaati hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.33
    with st.expander("Chapter 5.33 – Hanuman talks with Sita"):
        text1 = """
        Hanuman dheere se ped se neeche utre.
Unka chehra moongon (coral) jaisa chamak raha tha.
Wo bilkul saadhe roop mein the.

Haath jod kar
wo Sita ke paas aaye.
Aur naram awaaz mein bole."""
        create_image_text_layout("attached_assets/chapter5/5.33.jpg", text1, layout="side", image_position="left")

        text2 = """
        “Hey Devi,
aap kaun ho?

Aapki aankhen kamal ke phool jaisi hain.
Aap maili si reshmi saadi pehne ho.
Ped ki shaakh pakad kar khadi ho.

Aapki aankhon se aansu beh rahe hain.
Jaise tootey hue ghade se paani girta hai.

Aap kaun ho?
Devtaon mein se ho?
Rakshason, Nagas, Gandharvas ya Yakshon mein se?

Ya phir
Rudra, Vayu ya Vasu kul se ho?

Mujhe toh lagta hai
aap divya ho.

Kya aap Rohini ho,
jo Chandra se bichhad gayi?

Ya Arundhati ho,
jo Vasishtha se door chali aayi?

Kya aap
apne pita,
bhai,
putra
ya pati ke liye ro rahi ho?

Aap baar-baar
ek raja ka naam le rahi ho.

Aapke lakshan dekh kar
lagta hai
aap kisi raja ki patni ya putri ho.

Kya aap wahi Sita ho,
jise Ravana ne Janasthan se utha liya?

Aap par mangal ho.

Aapka dukh,
aapki sundarta
aur aapka tapasi vesh dekh kar
mujhe poora vishwas hai—

Aap Shri Rama ki patni ho.”

Hanuman ke muh se
Rama ka naam sunte hi
Sita ka mann hil gaya.

Unki aankhon mein
aansu ke saath
thodi si roshni aa gayi.

Sita boli:

“Main
raja Dasharatha ki bahu hoon.
Jo dharti ke mahaan raja the.

Main
Videha ke raja Janak ki beti hoon.
Mera naam Sita hai.

Aur main
buddhimaan aur dharmic
Shri Rama ki patni hoon.

Barah saal tak
main Rama ke saath
sukh se rahi.

Har khushi mili.
Har ichha poori hui.

Teerhve saal
mantriyon ki salah se
Rama ka rajyabhishek tay hua.

Puri Ayodhya khush thi.

Tab
Rani Kaikeyi ne
raja se kaha:

‘Agar Rama raja bane,
toh main bhojan aur jal chhod dungi.
Aur apna jeevan tyag dungi.

Jo do vardan
aapne mujhe diye the,
unhe poora kijiye.

Rama ko vanvaas bhejiye.’

Raja Dasharatha
apne vachan ke daas the.

Wo bahut roye.
Par vachan nahi toda.

Unhone Rama se kaha
ki raj chhod do.

Rama ne bina jhijhak kaha,
‘Main pitaji ki baat maanta hoon.’

Rajya se zyada
unke liye
vachan aur dharm tha.

Rama ne
raj ke kapde chhod diye.

Unhone mujhe
apni maa ke paas chhodna chaha.

Par main kaise rehti?

Rama ke bina
swarg bhi mujhe soona lagta.

Isliye
main bhi tapasya ka vesh pehen kar
unke saath van chali.

Lakshmana bhi
bark aur kusha ke vastra pehen kar
saath aaye.

Hum teenon
ghane van mein aa gaye.

Aur jab Rama
Dandakaranya van mein the,

Tab
dusht Ravana
mujhe utha le gaya.

Usne
do mahine ka samay diya hai.

Uske baad
wo mujhe maar dega.”

Sita chup ho gayi.
Unki aankhon mein dukh tha.
Par Rama ka naam lete hue
unke chehre par dhairya bhi tha.

🌼 Seekh (Moral)

🌱 Sachcha dharm mushkil samay mein bhi nahi chhodta

💛 Prem aur vishwas insan ko sabse bada bal deta hai

🌟 Jahan dharm hota hai, wahan sahayata avashya aati hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.34
    with st.expander("Chapter 5.34 – Sita feels unsure and afraid of Hanuman"):
        text1 = """
        Sita ke dukhi shabd sun kar
Hanuman ne use shaant karna chaha.

Wo bole:

“Hey Devi Vaidehi,
main Rama ka sandeshwahak hoon.

Rama bilkul surakshit hain.
Wo aapki khairiyat pooch rahe hain."""
        create_image_text_layout("attached_assets/chapter5/5.34.jpg", text1, layout="side", image_position="left")

        text2 = """
        Dasharatha ke putra Rama,
jo Ved jaante hain,
jo Brahmastra ke gyaani hain,
aapko pranam bhejte hain.

Lakshmana bhi,
jo aapke pati ke sabse priya saathi hain,
man hi man dukhi hote hue bhi,
aapko naman karte hain.”

Rama aur Lakshmana ka naam sunte hi
Sita ka sharir kaanp gaya.

Par ye kaanpna
khushi ka tha.

Wo boli:

“Sach hi kaha gaya hai.
Kabhi-kabhi
sau saal baad bhi
sukh aa hi jaata hai.”

Sita aur Hanuman
khushi se baat karne lage.

Dono ke beech
bharosa badhne laga.

Par jaise hi
Hanuman thoda paas aaye,
Sita ka mann ghabra gaya.

Usne socha:

“Arre!
Kahin ye Ravana hi toh nahi?
Kisi aur roop mein?”

Dar se
usne Ashok vriksh ki shaakh chhod di.
Aur zameen par baith gayi.

Hanuman ne turant
jake pranam kiya.

Sita dar ke maare
aankh nahi utha pa rahi thi.

Par uska vinamra jhukna dekh kar
Sita ne dheere se kaha:

“Agar tum Ravana ho,
aur mujhe dukh dene ke liye
ye roop liya hai,
toh ye bahut paap hai.

Tum wahi ho
jo Janasthan mein
sadhu bankar aaya tha.

Mujhe aur mat satao.
Main bhookh aur dukh se
pehle hi kamzor ho chuki hoon.

Par…
tum poore Ravana nahi lagte.

Tumhe dekh kar
mere mann mein shanti aa rahi hai.

Agar tum sach mein
Rama ke sandeshwahak ho,
toh tumhara swagat hai.

Mujhe Rama ke baare mein sunao.
Unki baatein
mere mann ko baha le jaane do.

Ye sapna toh nahi?
Par sapne mein bandar dekh kar
khushi nahi hoti.

Aur mujhe toh khushi ho rahi hai.

Kya mera mann bhram mein hai?
Ya bhookh ne mujhe kamzor kar diya?

Nahi…
main poori tarah hosh mein hoon.
Aur tumhe saaf-saaf dekh rahi hoon.”

Sita ke mann mein
ek aur baat ghoom rahi thi.

“Rakshas toh
roop badal sakte hain.”

Isi soch mein
wo chup ho gayi.

Hanuman samajh gaye.
Unhone phir madhur shabdon mein kaha:

“Rama surya jaise tejasvi hain.
Chandra jaise shaant hain.

Wo sabke priya hain.
Kubera jaise daani hain.

Vishnu jaise veer.
Vachaspati jaise madhur vakta.

Kaamdev jaise sundar.
Aur adharmiyon ko
nyay se dand dene wale.

Marich ne hiran ka roop liya.
Isi wajah se Rama van se door gaye.
Aur Ravana aapko utha le gaya.

Par zyada din nahi bache.

Rama apne tej baanon se
Ravana ka ant karenge.

Main wahi sandesha laaya hoon.

Rama aapki chinta karte hain.
Lakshmana bhi.

Sugriva,
vanaron ke raja,
jo Rama ke mitra hain,
wo bhi aapko pranam bhejte hain.

Bahut jald
aap Rama aur Lakshmana ko
phir dekhenge.

Main Sugriva ka mantri hoon.
Mera naam Hanuman hai.

Main samudra paar karke
Lanka aaya hoon.

Main Ravana nahi hoon.
Apna doubt chhod dijiye.
Aur mere shabdon par vishwas rakhiye.”

Sita ne Hanuman ko dekha.
Unke mann ka bojh
thoda halka ho gaya.

Unki aankhon mein
pehli baar
ummeed ki roshni chamki.

🌼 Seekh (Moral)

🌱 Dukh ke samay shak aana swabhavik hai

🤍 Sachcha vinamrata aur madhur vaani se pehchana jaata hai

🌟 Umeed ka ek shabd bhi jeevan badal sakta hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.35
    with st.expander("Chapter 5.35 – Hanuman proves he is Rama’s messenger"):
        text1 = """
        Rama ke baare mein
itna sundar varnan sun kar,
Vaidehi ka mann pighal gaya.

Wo pyaar se boli:

“Tum Rama se kahan mile?
Lakshmana ko kaise jaante ho?

Insaan aur vanar
kaise mitra bane?

Mujhe phir se batao.
Rama aur Lakshmana ke
lakshan batao.

Unka roop.
Unki bhuja.
Unki shakti.

Mera dukh kam ho jayega.”"""
        create_image_text_layout("attached_assets/chapter5/5.35.jpg", text1, layout="side", image_position="left")

        text2 = """
        Hanuman muskuraye.
Aur bole:

“Devi Vaidehi,
aapne mujhe Rama ka
doot maan liya.

Ye mera saubhagya hai.

Ab suno.
Main Rama aur Lakshmana ka
sachcha varnan karta hoon.”

“Rama ke netra
kamal jaise hain.

Unka mukh
chandrama jaisa shant hai.

Tej Surya jaisa.
Dharya dharti jaisa.

Buddhi Brihaspati jaisi.
Yash Indra jaisa.

Wo sab praniyon ke rakshak hain.
Dharma ke sanrakshak hain.

Sach aur nyay
unke jeevan ka mool hai.

Unki bhuja lambi aur balwan hain.
Kandhe chaunde hain.

Unki awaaz
dundubhi jaise gambhir hai.

Unki chal
sher aur hathi jaise shant aur majboot hai.

Lakshmana bhi
bilkul un jaise hain.

Bas rang mein antar hai.
Rama shyam varn ke hain.
Lakshmana swarn jaise ujjwal hain.

Dono bhai
aapse milne ke liye
vyakul hain.”

Hanuman ne phir
poori kahani sunayi.

“Van mein ghoomte hue
Rama aur Lakshmana
Sugriva se mile.

Sugriva ko
uske bhai Bali ne
rajya se nikal diya tha.

Pehle dar laga.
Par phir mitrata hui.

Rama ne Sugriva ka dukh samjha.
Sugriva ne Rama ka.

Dono ne ek doosre ki madad ka vachan diya.”

“Bali ka vadh hua.
Sugriva vanaron ka raja bana.

Fir
aapko dhoondhne ke liye
vanar sena chali.

Jab aapke gehne
aakash se gire the,
unhe hum lekar
Rama ke paas gaye.

Rama unhe seene se laga kar
bahut roye.

Aapke bina
wo jeevit reh kar bhi
jal rahe hain.

Jaise parvat par
aag dhadhak rahi ho.”

Hanuman ki awaaz
aur gambhir ho gayi.

“Hum sab
aapko dhoondhte-dhoondhte
haar gaye the.

Marne ka bhi soch liya tha.

Tab Sampati aaye.
Jatayu ke bhai.

Unhone bataya
ki aap Lanka mein hain.

Main samudra langh kar
yahan aaya.

Raat mein Lanka mein pravesh kiya.

Ravana ko dekha.
Aur aapko bhi.

Main hi Hanuman hoon.

Sugriva ka mantri.
Vayu ka putra.

Ye mera sach hai.

Ab mujhe pehchaan lijiye.”

Hanuman ke shabd
dil se nikle hue the.

Sita ka dukh
ab bharose mein badalne laga.

Unki aankhon se
khushi ke aansu behne lage.

Unka chehra
chandrama jaise chamak utha.

Jaise
Rahu ke baad
chand phir se nikla ho.

Sita ne mann hi mann kaha:

“Ab koi sandeh nahi.

Ye sach mein
Rama ka doot hai.”

Hanuman phir bole:

“Devi,
ab aap batao.

Main aur kya kar sakta hoon?

Aapka sandesh
main Rama tak pahuchaunga.

Bahut jald
Rama Ravana ka ant karenge.

Aur aapko yahan se le jayenge.”

🌸 Seekh (Moral)

🌱 Sach hamesha shant aur spasht hota hai

🤍 Vishwas sabse pehle dil ko chhoota hai

🔥 Bhakti aur kartavya se asambhav bhi sambhav ho jaata hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.36
    with st.expander("Chapter 5.36 – Sita asks Hanuman many questions"):
        text1 = """
        Hanuman ne Sita ka vishwas
aur gehra karne ke liye
phir se bola.

Unki awaaz shant thi.
Dil se nikli hui."""
        create_image_text_layout("attached_assets/chapter5/5.36.jpg", text1, layout="side", image_position="left")

        text2 = """
        “Devi Sita,
main Rama ka doot hoon.

Main vanar hoon.
Par Rama ka vishwas
mere saath hai.

Ye dekhiye.”

Hanuman ne
ek angoothi nikali.

Wo Rama ki thi.
Us par Rama ka naam
likha tha.

“Ye angoothi
Rama ne khud di hai.

Taaki aap mujh par
poora vishwas kar saken.

Aapka dukh
ab zyada din ka nahi.”

Sita ne jab
wo angoothi dekhi,
unka hriday bhar aaya.

Unhone use
haathon mein liya.

Aisa laga
jaise Rama
saamne khade ho.

Unki aankhen chamak uthi.
Aansoo khushi ke the.

Unka chehra
chand jaise ho gaya.
Jaise baadal hat gaye hon.

Sita ne Hanuman ko
mitra ki tarah dekha.

Aur boli:

“O shreshth vanar,
tum sach mein veer ho.

Akele Lanka aana
aasaan nahi tha.

Samudra paar karna
bahut bada kaam hai.

Tum Ravana se bhi
nahi darte.

Tum koi saadhaaran vanar
nahi ho.

Rama ne tumhe
parakh kar hi bheja hoga.”

Phir Sita ke mann mein
bahut saare sawal aaye.

Wo dheere-dheere boli:

“Kya Rama
theek hain?

Kya Lakshmana
swasth hain?

Mere bina
kya Rama vyakul hain?

Kya wo mujhe
yaad karte hain?

Kya wo mujhe
bachaane ki tayyari
kar rahe hain?

Kya unka dhairya
abhi bhi bana hua hai?

Kya Bharata
unki madad karega?

Kya Sugriva
vanar sena ke saath
aayega?

Kya main
Ravana ka ant
apni aankhon se
dekh paungi?

Kya Rama ka
sone jaisa chehra
mere bina
feeka ho gaya hai?”

Sita ruk gayi.
Wo aur sunna chahti thi.

Hanuman ne
haath jod kar
vinamrta se bola:

“Devi,
Rama abhi ye nahi jaante
ki aap yahan hain.

Isliye wo
abhi aaye nahi.

Jaise hi wo
ye sach jaanenge,
wo turant aayenge.

Vanar aur bhaalu sena ke saath.

Samudra bhi
unhe nahi rok paayega.

Lanka bhi
tik nahi paayegi.”

Hanuman ki awaaz
aur dridh ho gayi.

“Devi,
Rama aapke bina
so nahi paate.

Unka mann
sirf aap mein laga rehta hai.

Kabhi unki aankh lagti hai,
to wo uth kar bolte hain:
‘Sita…’

Koi phool dekhte hain,
to aap yaad aati hain.

Koi fal dekhte hain,
to aapka naam lete hain.

Lakshmana
unke liye fal-mool
tayaar karte hain.

Rama tapasya ka
jeevan jee rahe hain.

Main parvaton ki shapath leta hoon.
Mandar, Meru, Vindhya ki.

Aap jaldi
Rama ko dekhenge.

Unki sundar aankhen.
Unka shant mukh.

Aapka milan
ab door nahi.”

Hanuman ke shabd sun kar
Sita ka mann
khushi se bhar gaya.

Par saath hi
Rama ke dukh ka soch kar
unhe kasak hui.

Wo aisi lag rahi thi
jaise sharad ka chand
baadal ke peeche
chhup kar
phir nikal aaye.

🌸 Seekh (Moral)

🤍 Sachcha prem doori mein bhi kam nahi hota

🔥 Vishwas aur dhairya dukh ko sahne ki shakti dete hain

🌱 Sacha doot wahi hota hai jo asha jagaye"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.37
    with st.expander("Chapter 5.37 – Sita refuses to go with Hanuman alone"):
        text1 = """
        Chand jaise chehre wali
Sita ne
Hanuman ki baat suni.

Phir shaant,
par gambhir swar mein boli.

“O Vanar-veera,
tumne mujhe bataya
ki Rama mujhe yaad karke
dukh mein doobe hain.

Ye baat
amrit jaise hai,
par zehar ke saath mili hui."""
        create_image_text_layout("attached_assets/chapter5/5.37.jpg", text1, layout="side", image_position="left")

        text2 = """
        Chahe sukh ho
ya dukh,
vidhi apna kaam karti hai.

Koi bhi
bhagya se nahi bach sakta.

Dekho,
main, Rama aur Lakshmana
sabhi kasht mein hain.”

Sita ki aankhen bhar aayi.

“Jaise toota hua jahaz
kinare ki talash karta hai,
waise hi Rama
apne dukh ka ant chaahte hain.

Ravana ne
mujhe maarne ka samay
tay kiya hai.

Sirf do mahine
baaki hain.

Uske bhai
Vibhishan ne use samjhaya.

Par Ravana ne
baat nahi maani.

Budhe aur gyaani
Avindha ne bhi
vinaash ki bhavishyavani ki.

Par Ravana andha bana raha.”

Sita ne
thoda bal pakda.

“Phir bhi
mujhe vishwas hai.

Mera hriday shuddh hai.
Aur Rama ke gun
anant hain.

Unmein dhairya hai.
Karuna hai.
Shakti hai.

Janasthan mein
unhone akele
chaudah hazaar rakshas
maare the.

Wo surya jaise hain.
Unke baan
surya ki kirnein hain.

Rakshason ka jheel
wo sookha denge.”

Itna keh kar
Sita phir ro padi.

Tab Hanuman bole:

“Devi,
chaaho to main
aaj hi aapko
yahan se le chaloon.

Meri peeth par baithiye.
Main samudra paar
aapko Rama tak
le jaa sakta hoon.

Main poori Lanka
Ravana samet
utha sakta hoon.

Aaj hi
aap Rama se mil sakti hain.”

Sita pehle
chakit hui.

Phir boli:

“O Hanuman,
ye kaise sambhav hai?

Tum itne chhote ho.

Mujhe
itni door kaise le jaoge?”

Hanuman ne socha:

“Sita meri shakti
nahi jaanti.”

Hanuman ne
apna roop badla.

Wo badhne lage.

Parvat jaise ho gaye.

Unka sharir
aag aur pahad sa
lagne laga.

“Main poori Lanka
ukhaad sakta hoon.

Aaiye Devi,
der na kijiye.”

Sita ne
unka vishal roop dekha.

Aur namrata se boli:

“O Mahaveer,
ab main tumhari shakti
samajh gayi hoon.

Tum sach mein
pawan ke putra ho.

Par mujhe
sochna hoga.

Kya ye uchit hoga?”

Sita ne
shaant mann se kaha:

“Agar main
tumhari peeth se gir gayi,
to samudra mein
shikaar ban jaungi.

Rakshas tumhara
peecha karenge.

Tum nishastra hoge.

Aur mujhe
bachate-bachate
yuddh mein phas jaoge.

Yuddh ka
parinaam anishchit hota hai.

Agar mujhe kuch ho gaya,
to sab vyarth ho jaayega.”

Sita ne
aakhri aur gehri baat kahi:

“Main
sirf Rama ko
sparsh kar sakti hoon.

Ravana ne mujhe
zabardasti chhua.

Par main tab
asahaay thi.

Agar Rama aakar
Ravana ko maar kar
mujhe le jaayein,
to wahi unke yogya hai.

Unke saamne
Dev, Naag, Rakshas
koi nahi tik sakta.

Isliye, Hanuman,
Rama, Lakshmana
aur Sugriva ko
yahan le aao.

Unke bina
main jee nahi sakti.

Ab mujhe
phir se khushi do.”

🌸 Seekh (Moral)

🤍 Maryada aur dharm bal se bhi bade hote hain

🕊️ Sita ka vishwas sirf shakti par nahi, nyay par tha

🔥 Sachchi vijay wahi hoti hai jo dharm ke saath ho"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.38
    with st.expander("Chapter 5.38 – Sita gives Hanuman her jewel"):
        text1 = """
        Sita ke shabd sun kar
Hanuman ka mann bhar aaya.

Wo muskuraye
aur vinamr swar mein bole.

“O Janaki,
tumne jo kaha
wo bilkul uchit hai.

Tumhari maryada,
tumhara pativrata dharm,
sab Rama ke yogya hai."""
        create_image_text_layout("attached_assets/chapter5/5.38.jpg", text1, layout="side", image_position="left")

        text2 = """
        Samudra paar karna
tumhare liye uchit nahi.

Aur jo tumne kaha
ki tum sirf Rama ko hi sparsh kar sakti ho,
ye tumhari pavitrata dikhata hai.”

Hanuman ne aage kaha:

“Maine tumse aisa kehna
sirf isliye chaha
kyunki main Rama ka kaam
poora karna chahta tha.

Main tumhe
aaj hi Rama ke paas
le jaana chahta tha.

Par ab,
jaise tum keh rahi ho,
main wahi karunga.”

Phir Hanuman bole:

“Ab mujhe
koi aisa chinh do
jisse Rama ko
mujh par poora vishwas ho jaaye.”

Sita ki aankhon se
aansoo behne lage.

Bhari awaaz mein boli:

“Ek chinh hai.
Bahut hi pavitra.

Tum Rama se kehna
ek purani ghatna.”

Sita ne yaad kiya
Chitrakoot ka samay.

“Mandakini nadi ke paas
hum dono the.

Tum jheel mein snaan karke
mere seene par
vishram kar rahe the.

Ek kauwa aaya.
Usne mujhe chonch maari.

Main gussa hui.
Use hataana chaha.

Par wo baar-baar
waapas aata raha.

Thak kar
main tumhari baahon mein
aa gayi.

Tum hase.
Aur pyaar se
mere aansoo ponch diye.

Main tumhari baahon mein
so gayi.

Aur tum bhi.”

Sita ki awaaz aur bhari ho gayi.

“Jab main uthi,
us kauwe ne
mujhe phir chot pahunchayi.

Tum jaag gaye.

Tumhara krodh
aag jaise tha.

Tumne
kusha ghaas se
Brahmastra banaya.

Kauwa teeno lokon mein bhaga.

Par kahin sharan na mili.

Aakhir wo tumhare paas
lauta.

Tumne daya dikhayi.

Uska ek aankh
le liya.

Aur uski jaan bacha li.”

Sita ne dard se kaha:

“Jo tumne
ek kauwe ke liye kiya,
kya wo mujh par bhi
yaad nahi aata?

Ravana ko
ab tak dand kyon nahi mila?”

Sita ro padi.

Hanuman ne
turant kaha:

“Devi,
ye satya hai
ki Rama tumhare dukh se
badal gaye hain.

Lakshmana bhi
unke dukh mein
jal rahe hain.

Ab jab main tumhe
pa gaya hoon,
sab badlega.

Rama Ravana ko
avashya nasht karenge.

Aur tumhe
ghar le jaayenge.”

Hanuman ne poocha:

“Ab mujhe batao,
Rama, Lakshmana
aur Sugriva ko
kya sandesh doon?”

Sita ne dhairya se kaha:

“Rama ko
mera pranam kehna.

Aur Lakshmana ko bhi.

Wo jisne
sab sukh chhod kar
Rama ka saath diya.

Jo mujhe
maa samaan maanta hai.

Us veer se kehna
ki main unke sahas ko
yaad karti hoon.”

Phir Sita ne
aakhri baat kahi:

“Rama se kehna—

Mera sirf ek mahina baaki hai.
Uske baad main nahi rahungi.

Ye sach hai.

Mujhe Ravana se
jaldi mukt karo.”

Itna keh kar
Sita ne
apne vastra se
ek chamakta hua
motiyon ka abhushan nikala.

Wo wahi tha
jo kabhi
uske maathe par
shobha deta tha.

Usne Hanuman ko diya
aur boli:

“Ye Rama ko dena.”

Hanuman ne
us anmol ratna ko
shraddha se liya.

Sita ko pranam kiya.

Aur man hi man
Rama ke paas
laut gaye.

Uska hriday shaant tha.

Uska kartavya
ab spasht tha.

🌸 Seekh (Moral)

🤍 Vishwas chinh se nahi, bhavna se hota hai

🕊️ Sita ka abhushan yaad ka sandesh hai

🔥 Dharma aur dhairya hi jeet dilate hain"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.39
    with st.expander("Chapter 5.39 – Hanuman comforts and calms Sita"):
        text1 = """
        Sita ne
Hanuman ko
woh anmol moti de diya.

Phir dheere se boli:

“Ye chinh
Rama turant pehchaan lenge.

Isse unhe
teen chehre yaad aayenge.
Mere pita Janaka,
Raja Dasharath,
aur main.”"""
        create_image_text_layout("attached_assets/chapter5/5.39.jpg", text1, layout="side", image_position="left")

        text2 = """
        Sita ki aankhon mein
umeed bhi thi
aur darr bhi.

“O Hanuman,”
wo boli,
“apni poori shakti se socho.

Socho ki
Rama ko
ab kya karna chahiye.

Meri peeda
ka ant kaise hoga.

Tum hi
mujhe is dukh se
bahar nikaal sakte ho.”

Hanuman ne
vinamrta se sir jhukaya.

“Tathaastu,”
usne kaha.

Jab Hanuman
jaane laga,
toh Sita ka mann
kaamp utha.

Aansoo bhari awaaz mein boli:

“O Hanuman,
Rama, Lakshmana,
Sugriva
aur sab vanaron ko
mera mangal sandesh dena.

Unka bhala chaho.
Unke liye shubh kaamna karo.

Rama se aisa kehna
ki jab tak main zinda hoon,
mujhe yahan se
bachaa lein.

Mere shabd
unke saahas ko
sau guna badha denge.

Mujhse milne ki ichha
unhe aur bhi
veer bana degi.”

Hanuman ne
haath jod kar kaha:

“Devi,
Rama avashya aayenge.

Bade-bade devta,
daitya,
ya raakshas bhi
unka saamna
nahi kar sakte.

Agar zarurat pade,
toh wo Surya,
Varun,
ya Yama se bhi
yuddh kar sakte hain.”

Sita ne
Hanuman ki baaton mein
sachchai mehsoos ki.

Phir ek vinamr ichha rakhi:

“O Veer,
agar tumhe theek lage,
toh ek din aur ruk jao.

Tumhari upasthiti se
mera dukh
kuch der ko kam hota hai.

Agar tum aaj chale gaye,
toh tumhare lautne tak
mera jeevan
badi kathinai mein rahega.”

Phir Sita ne
apna sabse bada darr kaha:

“Samudra bahut vishaal hai.

Rama, Lakshmana
aur vanar sena
ise kaise paar karenge?

Is sansaar mein
sirf teen hi
samudra paar kar sakte hain.
Garud,
tum,
aur Vayu.”

Phir boli:

“Main jaanti hoon
tum akela bhi
sab kar sakte ho.

Par yeh vijay
Rama ki honi chahiye.

Ravana ko hara kar,
mujhe le jaana
Rama ka hi kartavya hai.

Isi mein
unka yash hai.”

Hanuman ne
shaant aur
pyaari awaaz mein kaha:

“O Janaki,
chinta mat karo.

Sugriva tayari kar chuke hain.

Laakhon vanar
unke saath aayenge.

Kuch vanar
mere jaise shaktishaali hain.

Kuch mujhse bhi
adhik balwaan.

Koi kamzor nahi.

Jab main yahan aa sakta hoon,
toh wo sab bhi
avashya aa sakte hain.”

Hanuman ne aage kaha:

“Rama aur Lakshmana
surya aur chandra jaise hain.

Ravana aur uski sena
unke saamne
tik nahi paayegi.

Jab Lanka par
vanar sena garjegi,
toh pahaad bhi
kaanp uthenge.”

Sita ka mann
halka ho gaya.

Uski aankhon mein
phir se umeed chamki.

Hanuman ne
aakhri baar kaha:

“Rama tumse milenge.

Ravana ka ant
tumhari aankhon ke saamne hoga.

Tab tum
Rama se
waise hi milogi
jaise Sachi
Indra se mili thi.

Thoda sa dhairya rakho.

Main jaldi lautunga.”

Sita ne
sir jhuka kar
Hanuman ko dekha.

Uske mann mein
pehli baar
shaanti utri.

🌼 Seekh (Moral)

💛 Dhairya sabse badi shakti hai

🤝 Sacha sevak vishwas jagata hai

🌅 Andhera kitna bhi gehra ho, subah zaroor aati hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.40
    with st.expander("Chapter 5.40 – Hanuman says goodbye to Sita"):
        text1 = """
        Hanuman ki baatein sunkar
Sita ka mann
thoda shaant hua.

Usne
pyaar bhari
aur arth-poorn baaton mein kaha:

“Jaise baarish
pakti fasal ko
khushi deti hai,
waise hi tumhe dekhkar
mera mann
jeevit ho uthta hai,
O Hanuman."""
        create_image_text_layout("attached_assets/chapter5/5.40.jpg", text1, layout="side", image_position="left")

        text2 = """
        Tum mere Rama ki
madhur baatein bolte ho.
Isliye tum
mere liye
varadaan ho.

Meri daya karke
aisa kaam karo
ki main
jaldi se
us veer purush se
mil sakoon.”

Phir Sita boli:

“Rama ko
woh sab yaad dilana
jo sirf hum dono jaante hain.

Us kaue ki baat
jiska ek aankh
unhone nikaal diya tha.

Aur woh pal bhi,
jab mera tilak
mit gaya tha
aur Rama ne
apne haathon se
naya tilak
mere gaal par banaya tha.

Ye sab
unhe turant yaad aa jaayega.”

Sita ki awaaz
bharra gayi.

Aansoo behte hue boli:

“Unse kehna—

‘O Indra jaise veer,
tum kaise sah sakte ho
ki Sita
raakshason ke beech
bandi bani rahe?

Jo moti
mere maatha ko sajata tha,
use maine
bahut sambhaal kar rakha.

Dukh mein bhi
main use dekh kar
tumhe mehsoos karti hoon.

Agar tum deri karoge,
toh main
ek maheena bhi
zinda nahi rahungi.

Ravana ka bhay
mujhe har pal sataata hai.

Agar mujhe laga
ki tum aane mein
hichkichaa rahe ho,
toh main
usi pal
apna praan tyaag dungi.’”

Sita ki aankhon se
aansoo behte rahe.

Hanuman ka
hriday bhar aaya.

Usne
dridhta se kaha:

“O Devi,
main kasam khaata hoon.

Tumhare dukh se
Rama ka chehra
peela pad gaya hai.

Aur Rama ko dukhi dekhkar
Lakshmana bhi
vyakul hai.

Ab jab maine tumhe
dekh liya hai,
toh nirasha ka
koi kaaran nahi.

Bahut jald
tumhare saare dukh
samaapt honge.”

Hanuman aage bola:

“Rama aur Lakshmana
Lanka ko
raakh bana denge.

Ravana ka ant hoga.

Aur tum
apne Rama ke saath
apne nagar
loti aaogi.”

Hanuman ne phir kaha:

“Ab mujhe
koi aisa chinh do
jise dekhkar
Rama turant
meri baat maan le.”

Sita ne
shaant swar mein kaha:

“Main pehle hi
woh chinh
tumhe de chuki hoon.

Us moti ko dekhkar
Rama ko
sab yaad aa jaayega.”

Hanuman ne
woh anmol moti
aadar se liya.

Sir jhukaya.

Vida lene laga.

Jab Sita ne dekha
ki Hanuman
apna roop bada karke
udne ko taiyaar hai,
toh uski aankhon se
phir aansoo beh nikle.

Roti hui boli:

“O Hanuman,
Rama aur Lakshmana ko
mera pranam kehna.

Sugriva
aur sab vanaron ko bhi.

Rama se kehna
ki main
iss dukh ke samudra mein
doob rahi hoon.

Raakshason ki dhamkiyon se
mera mann
kaamp raha hai.

Mujhe yahan se
jaldi bachaa lein.

Tumhara bhala ho,
O Vanar-shreshth.”

Hanuman ne
ye sab baatein
hriday mein basa li.

Uska kaarya
poora ho chuka tha.

Usne
man hi man
uttar disha ka path
paar kar liya.

Aur
Rama tak pahunchne ke liye
udaan bharne ko
taiyaar ho gaya.

🌼 Seekh (Moral)

🌱 Umeed zinda rakhti hai

🤝 Sachcha doot sirf sandesh nahi, sahara bhi hota hai

🌞 Prem aur vishwas se bada koi bal nahi"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.41
    with st.expander("Chapter 5.41 – Hanuman destroys the Ashoka garden"):
        text1 = """
        Sita se aashirvaad lene ke baad,
Hanuman dheere se Ashoka Vatika se bahar nikla.

Uske mann mein soch chali.

“Main apna main kaam kar chuka hoon.
Sita mil gayi.
Par ab kuch aur bhi zaroori hai.”"""
        create_image_text_layout("attached_assets/chapter5/5.41.jpg", text1, layout="side", image_position="left")

        text2 = """
        Hanuman ne socha:

“Rakshason se baat karke kaam nahi banega.
Na daan kaam aayega.
Na unmein phoot daali ja sakti hai.
Yahan sirf shakti hi kaam karegi.”

Usne mann mein kaha:

“Jab Rakshas apne shresht yoddha haarte dekhenge,
tab unka ghamand tootega.
Ek achha doot wahi hota hai
jo main kaam ke saath
dushman ki taakat bhi jaan le.”

Hanuman ne faisla kiya:

“Main is sundar Ashoka Vatika ko nasht karunga.
Isse Ravana ka gussa bhadkega.
Phir woh apni sena bhejega.
Aur mujhe Rakshason ki asli taakat dikh jaayegi.”

🔥 Ashoka Vatika ka Vinash

Phir Hanuman badal gaya.

Wo toofan jaisa ho gaya.

Bade-bade ped ukhaadne laga

Lataayein tod di

Phool bikhar gaye

Pavilions gir gaye

Haathi, hiran, pakshi —
sab bhay se chillane lage.

Jo vatika swarg jaisi thi,
wo jang ka maidan ban gayi.

Aisa laga jaise
aag ne poori bagiya ko jala diya ho.

Ashoka ke ped gir gaye.
Sundarta toot gayi.
Har taraf barbadi thi.

Wo jagah
jo pehle rajkumariyon ka khel-sthal thi,
ab khandhar ban chuki thi.

⚔️ Yuddh ke liye Taiyaar

Sab kuch todne ke baad,
Hanuman ruk gaya.

Wo dwaar par khada ho gaya,
aankhon mein tej,
shareer mein bijli.

Uska ek hi sankalp tha:

“Ab Rakshas aayein.
Main akela kaafi hoon.”

🌼 Is Adhyay ki Seekh

💥 Kabhi-kabhi shanti nahi, shakti zaroori hoti hai

🐒 Hanuman sirf bhakt nahi, strategist bhi hai

⚔️ Doot ka kaam sirf sandesh dena nahi,
dushman ki taakat naapna bhi hota hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.42
    with st.expander("Chapter 5.42 – Hanuman kills Ravana’s guards"):
        text1 = """
        Ashoka Vatika mein jab
ped girne lage, pakshi chillane lage,
to poori Lanka mein bhay phail gaya.

Janwar idhar-udhar bhaagne lage.
Aakash mein ashubh sanket dikhne lage."""
        create_image_text_layout("attached_assets/chapter5/5.42.jpg", text1, layout="side", image_position="left")

        text2 = """
        😨 Rakshasiyon ka Dar

Neend se uthi hui rakshasiyan
jab ujdi hui vatika dekhti hain,
to kaanp jaati hain.

Aur tab Hanuman apna roop aur bada kar leta hai.

Wo pahad jaisa dikhne lagta hai.
Aankhon mein bijli.
Shareer se shakti tapak rahi thi.

Rakshasiyan ghabra kar
Sita se poochti hain:

“Yeh kaun hai?
Kahan se aaya?
Tumse baat kyun ki?”

🌸 Sita ka Shaant Uttar

Sita shant rehkar kehti hain:

“Rakshas to roop badal sakte hain.
Main kaise pehchaan paati?
Jo saanp hai, use saanp hi jaane.

Mujhe to darr lag raha hai.
Mujhe lagta hai yeh bhi koi rakshas hi hai.”

Ye sunte hi
rakshasiyan bhaag jaati hain.

Kuch seedha Ravana ke paas pahunchti hain.

🔥 Ravana ka Krodh

Rakshasiyan kehti hain:

“Rajaa, ek bhayanak bandar aaya hai.
Usne Ashoka Vatika tod di.
Bas jahan Sita baithi hai,
us jagah ko chhod diya.

Wo Sita se baat bhi kar raha tha.”

Yeh sunte hi
Ravana ka gussa aag ban gaya.

Uski aankhon se
jaise jalta hua tel beh raha ho.

⚔️ Kinkaron ka Aadesh

Ravana garaj kar kehta hai:

“Kinkaro!
Us bandar ko pakad lao!”

Turant
80,000 Kinkar
gada, bhale, talwar, aur lohe ke hathiyaar lekar
Ashoka Vatika ki taraf daud padte hain.

🐒 Hanuman ka Garjan

Hanuman gate par khada hota hai.
Tail zor se ghumata hai.
Aur garaj kar bolta hai:

“Jai Shri Ram!
Jai Lakshmana!
Jai Sugriva!

Main Rama ka sevak Hanuman hoon.
Hazaar Ravana bhi
mera kuch nahi bigaad sakte!”

Uski awaaz se
pakshi aasman se girne lagte hain.

💥 Bhayankar Yuddh

Kinkar chaaron taraf se hamla karte hain.

Hanuman paas pada
lohe ka danda uthata hai.

Aur phir…

ek vaar

do vaar

teesra vaar

Rakshas girte jaate hain.

Hanuman
kabhi zameen par,
kabhi hawa mein
bijli ki tarah ghoom raha tha.

Jaise Indra vajra se daityon ko todta ho.

🩸 Kinkaron ka Ant

Kuch hi der mein
saare Kinkar mare jaate hain.

Ashoka Vatika ka dwaar
rakshason ke shareeron se bhar jaata hai.

Hanuman phir se
gate par khada ho jaata hai.

Aankhon mein jung ki aag.
Mann mein agla yuddh.

😱 Ravana ko Sandesh

Jo thode se rakshas bache,
wo bhaag kar Ravana ko batate hain:

“Rajaa…
Kinkar sab maare gaye.”

Yeh sunte hi
Ravana aur bhi bhadak jaata hai.

Aur wo
Prahasta ke veer putra ko yuddh ke liye bhejta hai.

🌼 Is Adhyay ki Seekh

🐒 Sachhi shakti sirf shareer ki nahi, dharma ki hoti hai

⚔️ Ghamand bina buddhi ke, vinash laata hai

🌟 Hanuman sirf yoddha nahi, bhakt aur rakshak bhi hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.43
    with st.expander("Chapter 5.43 – Hanuman destroys temples and buildings"):
        text1 = """
        Kinkaron ko maarne ke baad
Hanuman thodi der sochta hai.

Uske mann mein vichaar aata hai:
“Vatika to tod di.
Par mandir abhi baaki hai.
Ab uska ghamand bhi todna hoga.”"""
        create_image_text_layout("attached_assets/chapter5/5.43.jpg", text1, layout="side", image_position="left")

        text2 = """
        🐒 Hanuman ka Udaan Bharna

Hanuman zor se uchhalta hai.
Seedha us vishal mandir par jaa pahunchta hai.

Wo mandir
Meru parvat jaisa uncha tha.
Suraj ki roshni jaisa chamak raha tha.

Hanuman upar chadh jaata hai.
Uska shareer aur bhi bada ho jaata hai.
Lanka kaanp uthti hai.

Uski garaj se
pakshi gir jaate hain.
Mandir ke rakshak behosh ho jaate hain.

📣 Hanuman ka Garjan

Hanuman zor se bolta hai:

“Jai Shri Ram!
Jai Lakshmana!
Jai Sugriva!

Main Hanuman hoon.
Pawan putra.
Rama ka sevak.

Hazaar Ravana bhi
mera kuch nahi bigaad sakte.
Lanka ko tod kar
aur Sita maa ko pranam karke
main yahan se chala jaunga!”

Uski awaaz se
rakshason ke dil hil jaate hain.

⚔️ Mandir Rakshakon ka Hamla

Mandir ke
100 rakshak
talwar, bhala, gada le kar aa jaate hain.

Wo chaaron taraf se
Hanuman par vaar karte hain.

Teer suraj jaise chamak rahe the.
Lanka ka aakash
yuddh se bhar gaya.

🔥 Aag ka Pralay

Hanuman ko gussa aa jaata hai.

Wo mandir ka
sona chadha hua bada stambh
jad se ukhaad leta hai.

Use zor se ghumata hai.

Ghumte hi
aag bhadak uthti hai.

Mandir jalne lagta hai.
Aag aasman tak pahunch jaati hai.

Rakshak girte jaate hain.
Hanuman un sab ka vinash kar deta hai.

Wo aisa lag raha tha
jaise Indra vajra chala raha ho.

🌪️ Rakshason ko Chetavani

Hanuman hawa mein khada hokar bolta hai:

“Sugriva ke saath
hazaaron Hanuman aa rahe hain!

Koi haathi jitna taqatwar hai.
Koi hazaar haathi jitna.

Daant aur naakhun
hi unke hathiyaar hain.

Jab Rama ka krodh jaagega,
to Lanka, Ravana, aur tum sab mit jaoge.”

🌼 Is Adhyay ki Seekh

🔥 Ghamand aur adharm kabhi nahi bachta

🐒 Bhakti mein shakti hoti hai

⚔️ Sach ke liye lada gaya yuddh paawan hota hai

🌟 Hanuman vinash bhi karte hain,
par dharma ke liye"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.44
    with st.expander("Chapter 5.44 – Hanuman kills the warrior Jambumalin"):
        text1 = """
        Ravana ke aadesh par
Prahasta ka veer putra Jambumalin
yuddh ke liye nikalta hai.

🛡️ Jambumalin ka Pravesh

Jambumalin:

Bade daant wala

Ati bhayanak roop

Lal vastra, haar, mukut aur chamakte kundal pehne hue

Gadhe jute hue rath par savaar

Jaise hi wo apna Indra ke samaan dhanush chadhaata hai,
uski taan se garajti bijli jaisi awaaz hoti hai.

➡️ Aakash aur chaaro dishaayein
us ghoonj se bhar jaati hain."""
        create_image_text_layout("attached_assets/chapter5/5.44.jpg", text1, layout="side", image_position="left")

        text2 = """
        🐒 Hanuman vs Jambumalin

Hanuman use aate dekhkar
garjana karta hai.

Jambumalin turant hamla karta hai:

Chandrakar teer se Hanuman ke chehre par vaar

Kalgi wale teer se sir par

10 lohe ke teer baahon mein

➡️ Hanuman ka laal, taamba rang chehra
suraj ki roshni mein chamakte badal jaisa lagne lagta hai.
Khoon se rangaa hua chehra
laal kamal par sunehre binduon jaisa dikhta hai.

🪨 Parvat aur Vriksh ka Yuddh

Ghayal hokar Hanuman:

Ek vishal chattan (pathar) uthakar phenkta hai
➡️ Jambumalin use 10 teeron se tod deta hai

Fir Hanuman:

Ek bahut bada Saal ka ped ukhaad leta hai

Use hawa mein ghumata hai

Jambumalin:

4 teeron se ped kaat deta hai

5 teer baahon mein

1 pet mein

10 seene ke beech

➡️ Hanuman ka shareer teeron se bhara hua,
par krodh aur bhi bhadak uthta hai.

⚔️ Antim Prahar — Jambumalin ka Ant

Hanuman:

Ek gada (club) uthata hai

Use tez gati se ghumakar

Seedha Jambumalin ke seene par maar deta hai

💥 Itna bhayanak prahar hota hai ki:

Sir

Baah

Jangha

Dhanush

Rath

Ghode

Hathiyaar

👉 Sab ek saath chuur-chuur ho jaate hain.

Jambumalin:
🌳 Kata hua vriksh (oak) ki tarah
dharti par gir jaata hai
— nishpran.

😡 Ravana ka Krodh

Jab Ravana ko pata chalta hai ki:

Kinkar bhi mare gaye

Jambumalin bhi vadh ho gaya

➡️ Uska krodh aag ki tarah bhadak uthta hai
Aankhen laal ho jaati hain.

Turant aadesh deta hai:

“Mere mantriyon ke veer putron ko bhejo!
Jo shakti aur parakram mein adbhut hain.”

🌟 Is Adhyay ki Seekh

🔥 Adharm ke veer bhi dharm ke samne tik nahi paate

🐒 Hanuman ka sharir ghaayal hota hai,
par sankalp kabhi nahi

⚔️ Ek sachcha sevak
peeda mein bhi aur balwaan hota hai

🌺 Bhakti + Veerta = Ajey Shakti"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.45
    with st.expander("Chapter 5.45 – Hanuman kills the sons of Ravana’s ministers"):
        text1 = """
        🔥 Ravana ka agla daav

Jab:

Kinkaras mare ja chuke the

Jambumalin bhi vadh ho gaya

Tab Ravana (Rakshason ka Indra) ne apna agla sabse balwaan daav chala.

👉 Usne apne mantriyon ke 7 putron ko yuddh ke liye bheja."""
        create_image_text_layout("attached_assets/chapter5/5.45.jpg", text1, layout="side", image_position="left")

        text2 = """
        ⚔️ 7 Veer Rakshas ka pravesh

Ye 7 yoddha:

Agni jaise tejashvi

Ati veer aur astr-shastr mein nipun

Sone se jare hue rathon par savaar

Jinke rathon ki garjana bijli aur garajti badliyon jaisi thi

Dhanush kheechte hi aasmaan mein bijli chamakne jaisa drishya

➡️ Ye sab apni sena ke saath
Hanuman par vijay paane ke liye jal rahe the

Lekin:

Unki maaon ka man ashant tha

Kinkaron ki mrityu ka samaachaar sunkar
unke hriday mein bhay sama gaya tha

🐒 Hanuman vs 7 Mantri-putra

Hanuman:

Lanka ke dwaar par atal khada

Nirbhay, achal, tejashvi

Rakshas:

Apne garajte rathon se

baarish jaise anek teer barsa dete hain

➡️ Hanuman ka shareer
baarish mein dhake parvat jaisa lagta hai
— poora teeron se chhup jaata hai

🌪️ Hanuman ki adbhut yuddh-kala

Hanuman:

Aakash mein tez gati se ghoomta hai

Teeron aur rathon ko
adbhut chaalaki se bachata hai

Wo aisa lagta hai jaise:

Indra badliyon ke saath khel raha ho

Phir Hanuman:

Ek bhayankar garjana karta hai
➡️ Puri rakshas sena ka hriday kaanp uthta hai

💥 Rakshason ka vinash (Sharir se yuddh)

Hanuman ne:

Kisi ko hath ki thapad se maara

Kisi ko pair se

Kisi ko ghooson se

Kisi ko nakhon se cheera

Kisi ko seene aur jangha ke zor se gira diya

Kuch rakshas sirf garjana se hi gir pade

➡️ Ye yuddh astr-shastr ka nahi
👉 shuddh bal, parakram aur bhakti ka tha

🌊 Lanka ka bhayanak drishya

Yuddh ke baad:

Rakshas chaaro dishaon mein bhaag gaye

Haathi cheekhne lage

Ghode gir pade

Rath, jhande, chhatriyaan toot kar bikhar gayin

Sadkon par khoon ki nadiyaan behne lagi

Lanka cheekh-pukaar se goonj uthi

🐒 Hanuman ka sankalp

Un 7 mantri-putron ko maar kar bhi:

Hanuman thakta nahi

Garv mein nahi aata

➡️ Phir se Lanka ke dwaar par khada ho jaata hai

Sochta hai:

“Aur kaun hai jo apni shakti dikhana chahta hai?”

🌟 Is Adhyay ki Mukhya Seekh

🔥 Adharm ki sena chahe kitni bhi badi ho, bhakti ke aage tik nahi sakti

🐒 Hanuman astr-shastr ke bina bhi
vinash karne mein saksham hain

⚔️ Ye yuddh sirf sharir ka nahi,
dharm aur adharma ka hai

🌺 Hanuman ab bhi apne kartavya ke madhya mein hain
— ahankaar se door"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.46
    with st.expander("Chapter 5.46 – Hanuman kills five generals and their armies"):
        text1 = """
        Ravana ne suna ki
uske mantriyon ke bete bhi maare ja chuke hain.
Uska chehra kaala pad gaya.
Dil ke andar dar tha,
par bahar se usne use chhupa liya.

Ravana ne socha:
“Ab faisla ho jaayega.”

Usne apne 5 bade senapati bulaye:
Virupaksha, Yupaksha, Durdharsha, Praghasa aur Basakarna.
Sab bahut veer the.
Tez hawa jaise chalne wale.
Yuddh ke master."""
        create_image_text_layout("attached_assets/chapter5/5.46.jpg", text1, layout="side", image_position="left")

        text2 = """
        Ravana bola:
“Tum sab apni badi sena ke saath jao.
Ghode, rath aur haathi le jao.
Is bandar ko zinda pakad ke lao.

Dhyaan se kaam lena.
Yeh normal bandar nahi lagta.
Isme alag hi shakti hai.
Ho sakta hai yeh Indra ka bheja hua koi dev ho.

Main ne Bali, Sugriva, Jambavan jaise
bahut shaktishaali bandar dekhe hain.
Par yeh un sab se alag hai.

Yuddh ka nateeja kabhi pakka nahi hota.
Isliye poori taakat lagana.”

Paanch ke paanch senapati
apni sena ke saath nikal pade.
Rath chamak rahe the.
Haathi gusse mein the.
Ghode tez daud rahe the.

Unhone Hanuman ko dekha.
Gate par khada hua.
Suraj jaise chamak raha tha.
Bada sharir.
Majboot baahen.
Nirbhay aankhen.

Sab taraf se
teer aur hathiyaar barasne lage.

Durdharsha ne
Hanuman ke maathay par
paanch tez teer maare.

Hanuman ne zor se garjana ki.
Aasman aur dishaayein goonj uthi.

Durdharsha ne
ek saath sau teer chhod diye.

Par Hanuman ne
hawa ki tarah
sab teeron ko rok diya.

Phir Hanuman bada ho gaya.
Aur bijli ki tarah
Durdharsha ke rath par kood pada.

Rath toot gaya.
Ghode mar gaye.
Durdharsha dharti par gira.
Aur wahi mara gaya.

Ab Virupaksha aur Yupaksha aage aaye.
Gada le kar Hanuman par toot pade.

Hanuman hawaa mein phisla.
Phir neeche utar kar
ek Sala ka ped ukhaad liya.

Us ped se
dono rakshason ko maara.
Aur dono wahi gir pade.

Ab Praghasa aur Basakarna bache.
Ek hansi udata hua aaya.
Doosra bhala le kar gusse mein dauda.

Tez vaar hue.
Hanuman ke sharir se khoon behne laga.
Par woh ubhte hue suraj jaisa lag raha tha.

Phir Hanuman ne
pahad ka shikhar tod liya.
Ped, jaanwar, saanp sab uske saath the.

Us shikhar ko
un dono par patak diya.

Dono rakshas
chur-chur ho gaye.

Ab paanchon senapati
aur unki sena khatam ho chuki thi.

Hanuman ne
baaki sena ko bhi mita diya.
Haathi se haathi.
Rath se rath.
Yoddha se yoddha.

Sadke laashon se bhar gayi.
Lanka kaanp uthi.

Sab kuch khatam karke
Hanuman phir se
gate par ja kar khada ho gaya.

Bilkul Kaal ki tarah.
Shaant.
Par bhayanak.

Moral (Seekh) 🌼

Sachchi shakti dharma se aati hai

Akele bhi sahi ke liye ladne wala jeet sakta hai

Ahankaar aur atyachar ka ant nishchit hai

Bhakti aur kartavya Hanuman ko mahaan banate hain"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.47
    with st.expander("Chapter 5.47 – Hanuman kills Aksha"):
        text1 = """
        Jab Ravana ne suna
ki paanch senapati aur unki poori sena
Hanuman ke haathon maari ja chuki hai,
toh uska mann hil gaya.

Uski nazar padi
apne yuva putra Aksha par.
Aksha aag ki tarah utha.
Uski aankhon mein yuddh ka junoon tha.

Gold se saja hua divya rath,
aath bijli jaise tez ghode,
asankhya astr-shastr,
aur apni sena ke saath
Aksha nikal pada.

Uska rath
devtaon aur rakshason ke liye bhi
ajeet maana jaata tha."""
        create_image_text_layout("attached_assets/chapter5/5.47.jpg", text1, layout="side", image_position="left")

        text2 = """
        Gate par
Hanuman khada tha.
Shaant.
Par pralay jaise.

Aksha ne Hanuman ko dekha.
Uski aankhon mein
adar bhi tha aur garv bhi.

Phir yuddh shuru hua.

Aksha ne
teen zehrele teer
Hanuman ke maathay par maare.

Khoon behne laga.
Par Hanuman
ubhte hue suraj jaise lag raha tha.

Aasman kaanp utha.
Pawan ruk si gayi.
Pahad hil gaye.
Samundar uthalne laga.

Devta bhi
yeh yuddh dekh kar
stabdh ho gaye.

Aksha ne
teeron ki baarish kar di.
Jaise badal pahadon par baraste hain.

Hanuman hawa ki tarah
teeron ke beech se nikal gaya.

Phir Hanuman sochne laga:

“Yeh sirf bachcha nahi hai.
Isme veerta hai, sahas hai.
Par agar ise chhoda,
toh yeh aag ban kar phail jaayega.”

Dharma ke liye
kabhi-kabhi kathor nirnay lena padta hai.

Hanuman ne
ek hi vaar mein
aath ghodon ko haath se maar diya.

Rath hawa se gir kar
dharti par toot gaya.

Aksha rath chhod kar
talwar aur dhanush ke saath
aakash mein kooda.

Tab Hanuman ne
Garud jaise use pakda.
Pairon se ghoomaya.
Aur zor se
dharti par patak diya.

Aksha ka sharir
chur-chur ho gaya.

Ravana ka putra
yuddh-bhoomi mein
veer-gati ko praapt hua.

Sab devta, rishi, yaksh, nag
Indra ke saath
yeh drishya dekh rahe the.

Sab hairaan the.

Hanuman phir se
gate par ja kar khada ho gaya.

Bilkul aise
jaise pralay ke samay Mrityu khadi hoti hai.

Shaant.
Par atal.

Moral (Seekh) 🌿

Veerta umr se nahi, dharma se aati hai

Yuva shakti agar ahankaar mein ho, toh vinash laati hai

Sachche yoddha dushman ka samman bhi karte hain

Par adharma ko badhne dena paap hai

Hanuman bhakti ke saath buddhi aur nyay ka bhi prateek hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.48
    with st.expander("Chapter 5.48 – Hanuman allows himself to be captured"):
        text1 = """
        Aksha ke vadh ke baad
Ravana ka ahankaar hila,
par usne apna bhay chhupa liya.

Ab usne apna sabse shaktishaali putra – Indrajit (Meghnad) ko bulaya.

Ravana bola (arth ke saath):

“Tu hi hai jo devtaon ko bhi yuddh mein hara chuka hai.
Tu Brahma ke divya astron ka gyaata hai.
Hanuman ko maarna mushkil hai,
par use bandhna sambhav hai.”

Yahan Ravana ek badi baat samajh chuka tha:
👉 Hanuman ko shastra se maara nahi ja sakta."""
        create_image_text_layout("attached_assets/chapter5/5.48.jpg", text1, layout="side", image_position="left")

        text2 = """
        Indrajit ka aagman

Indrajit divya rath par chadha –

chaar singhon jaise ghode

indradhwaj laga hua

dhanush se bijli jaise teer

Jab rath aaya,

dishaen andheri ho gayin

siyaron ki awaaz ghoonj uthi

dev, rishi, yaksh sab dekhne aa gaye

Yeh saadharan yuddh nahi tha.

Hanuman vs Indrajit

Dono mahaveer:

ek taraf Ram bhakt Hanuman

doosri taraf Ravana ka putra Indrajit

Aakash mein yuddh hua.
Hanuman teeron se bach jaata.
Indrajit ka har vaar nishfal hota.

Indrajit samajh gaya:

“Yeh maara nahi ja sakta.”

Tab usne Brahmastra ka prayog kiya
— jo maar nahi, bandhne ke liye tha.

Hanuman ka maha-tyaag

Jaise hi Brahmastra laga,
Hanuman gir pada.

Par yahan sabse badi baat hui 👇

Hanuman ne khud ko chhudaya nahi.

Kyun?

Hanuman sochta hai:

“Yeh Brahma ka astra hai.
Iska maan rakhna dharm hai.
Aur agar main bandi banta hoon,
toh mujhe Ravana ke darbar tak jaana milega.”

👉 Yeh kamzori nahi, ran-neeti thi.

Hanuman jaan-bujhkar:

shaant raha

hilna band kar diya

apne aap ko bandhne diya

Titano ki galti

Rakshason ne
Brahmastra ke bandhan ke upar
rassi aur bark ke bandhan baandh diye.

Isse Brahmastra ka prabhav samaapt ho gaya.

Indrajit samajh gaya:

“Inhone mantra-vidya nahi samjhi.
Ab astr ka asar khatam ho gaya.”

Par Hanuman ne koi ishara nahi kiya.

Woh maar khata raha,
ghaseeta gaya,
par chup raha.

Ravana ke darbar mein pravesh

Bandha hua Hanuman
Ravana ke darbar mein laya gaya.

Sab chillaye:

“Maar do!”

“Jala do!”

“Khaa jao!”

Par Ravana ne shaant rehkar
mantriyon ko kaha:

“Isse poochho –
Kaun hai?
Kisne bheja?
Kya sandesh hai?”

Tab Hanuman ne pehli baar bola:

“Main Sugriva ka doot hoon.”

Aur yahin se
Ravana–Hanuman samvaad shuru hota hai
— jo poore Ramayan ka
sabse gyaan aur garv se bhara hissa hai.

Moral (Gehri Seekh) 🌿

Kabhi-kabhi bandi banna bhi jeet ka hissa hota hai

Shakti se zyada buddhi mahatvapurn hoti hai

Dev-astr ka maan rakhna bhi dharm hai

Hanuman sirf yoddha nahi, maha-niti-gyata bhi hain

Jo apni shakti jaanta hai, wahi shaant reh sakta hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.49
    with st.expander("Chapter 5.49 – Hanuman sees Ravana and is surprised"):
        text1 = """
        Hanuman bandhan mein tha.
Sharir par chot thi.
Par mann bilkul shaant tha.

Jab usne Ravana ko dekha,
toh woh pal bhar ke liye ruk gaya.

Ravana ka roop adbhut tha.

Sone jaise chamakdar vastra.
Heeron aur motiyon ka mukut.
Laal chandan se lipta sharir.
Aankhen laal, par tej se bhari hui.

Woh apne ratn-jade singhasan par baitha tha.
Chaar taraf sundar rakshasiyaan thi.
Haath mein chamri se bane chauri hil rahe the."""
        create_image_text_layout("attached_assets/chapter5/5.49.jpg", text1, layout="side", image_position="left")

        text2 = """
        Hanuman ne dekha:
Ravana ke haath sarp jaise majboot the.
Ungliyon mein chamakte hue ratn the.
Uski chhati par motiyon ki mala thi.

Woh Mandar Parvat jaise sthir aur bhari lag raha tha.
Jaise badalon se ghira hua koi shikhar.

Hanuman man hi man bola:

“Kitni shakti hai ismein…
Kitna tej hai…
Kitni sampatti aur mahima!”

Phir Hanuman ne socha:

“Agar yeh adharmi na hota,
toh yeh Indra bhi ban sakta tha.
Devlok ka rakshak ban sakta tha.”

Par agle hi pal
Hanuman ka mann bhaari ho gaya.

Usne socha:

“Par iska ghamand, iska anyaay,
iska ahinsa aur ahankaar
isse duniya ka shatru bana dete hain.”

“Yeh shakti raksha ke liye nahi,
vinaash ke liye hai.”

Hanuman ko ascharya bhi hua
aur dukh bhi.

Woh samajh gaya:
👉 Shakti bina dharm ke vinaash ban jaati hai.

Bandha hua hone ke baawajood,
Hanuman ka mann kabhi kamzor nahi hua.

Woh jaanta tha:
Sach aur dharm ke saath Ram khade hain.

Aur jahan Ram hain,
wahan Ravana jaisi shakti bhi haar jaati hai.

Moral (Seekh) 🌿

Sirf shakti hona kaafi nahi

Dharm ke bina shakti vinaash ban jaati hai

Sundar roop aur tej bhi ghamand ko sahi nahi bana sakte

Hanuman ne Ravana ki shakti ko maana,
par uske adharm ko kabhi swikaar nahi kiya"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.50
    with st.expander("Chapter 5.50 – Hanuman is questioned by the demons"):
        text1 = """
        Hanuman bandha hua Ravana ke saamne khada tha.
Uski aankhen shaant thi.
Par Ravana gusse se jal raha tha.

Ravana ne Hanuman ko dekha.
Uska mann thoda ghabra bhi gaya.

Woh sochne laga:

“Kahin yeh Nandi toh nahi?
Wahi jo Kailash par maine mazaak udaya tha
aur jisne mujhe shraap diya tha?”

“Ya phir yeh Vali ka beta Bali toh nahi,
jo bandar ke roop mein yahan aa gaya ho?”"""
        create_image_text_layout("attached_assets/chapter5/5.50.jpg", text1, layout="side", image_position="left")

        text2 = """
        Gusse se Ravana ki aankhen laal ho gayi.

Usne apne mantri Prahasta se kaha:

“Is dusht ko poochho!
Batao yeh kahan se aaya?
Isne Ashok Vatika kyun ujadi?
Mere rakshason ko kyun maara?
Meri nagri mein ghusne ki himmat kaise hui?”

Prahasta aage aaya aur Hanuman se bola:

“O Bandar, daro mat.
Sach bolo toh tumhari jaan bach sakti hai.”

“Kya Indra ne tumhe bheja hai?
Ya Kuvera, Yama, Varun ne?”

“Ya phir Vishnu ne tumhe bheja hai,
jeet ki laalach mein?”

“Tumhara roop bandar jaisa hai,
par tumhari shakti bandar jaisi nahi lagti.”

“Sach batao,
warna jhooth bolne par mrityu nischit hai!”

Hanuman muskuraaya.
Uski awaaz shaant aur nidar thi.

Usne kaha:

“Main na Indra ka doot hoon,
na Yama ka,
na Varun ka.”

“Na main Kuvera se juda hoon,
aur na Vishnu ne mujhe bheja hai.”

“Main sach mein ek bandar hoon.
Jaisa dikhta hoon, waisa hi hoon.”

“Main yahan sirf
Lanka ke raja ko dekhne aaya tha.
Isliye maine vatika tod di.”

“Jab rakshason ne mujh par hamla kiya,
toh apni jaan bachane ke liye
mujhe ladna pada.”

Hanuman ne aage kaha:

“Na hathiyaar mujhe bandh sakte hain,
na zanjeerein.”

“Yeh vardaan mujhe
Brahma ji se mila hai.”

“Maine jaan-bujhkar
Brahmastra ke aage jhukna sweekar kiya.”

“Main chahta tha ki
mujhe Ravana ke saamne laya jaaye.”

Phir Hanuman ne seedha Ravana ki taraf dekha aur bola:

“Main Shri Ram ka doot hoon.”

“Unki shakti aseemit hai.”

“Agar aap apna bhala chahte ho,
toh meri baat dhyaan se suniye,
hey Lanka ke raja.”

Hanuman ke shabd sach aur himmat se bhare hue the.
Sab rakshas chup ho gaye.

Moral (Seekh) 🌿

Sach bolne wala vyakti bandhan mein bhi nidar hota hai

Ghamand sawal karta hai, par sach shaant jawab deta hai

Hanuman ne na apni shakti chhupayi, na jhooth bola

Doot ka kaam ladna nahi, sach kehna hota hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.51
    with st.expander("Chapter 5.51 – Hanuman speaks bravely and fearlessly"):
        text1 = """
        Chapter 51 – Hanuman ke Shabd (Sundara-kanda ka sabse shaktishali sandesh)

Yeh adhyay Ramayana ka turning point hai. Yahin par pehli baar Hanuman bina bhay ke Ravana ke samne dharma ka sach bolte hain.

Hanuman apna parichay dete hain

Hanuman seedha kehte hain:

“Main Sugriva ka doot hoon”

Sugriva Ravana ko bhai samajhkar salaam bhejte hain

Yeh sandesh upar se nahi, neeche se bhi nahi — barabari ka hai

👉 Doot hote hue bhi Hanuman dabte nahi. Yeh Ram bhakti ki shakti hai."""
        create_image_text_layout("attached_assets/chapter5/5.51.jpg", text1, layout="side", image_position="left")

        text2 = """
        Rama ka parichay – shabd, shastra se zyada tez

Hanuman batate hain:

Rama kaun hain

Kaise Dasharatha ke aadesh par van gaye

Kaise Bali ko ek hi baan se mara

Kaise Sugriva ko rajya dilaya

⚔️ “Jisne Bali ko gira diya, usse koi bhi nahi rok sakta.”

Sabse tez prahar – Sita par

Hanuman Ravana ko seedha chetavani dete hain:

“Parayi patni ka apaharan tum jaise gyani ko shobha nahi deta”

Sita tumhare liye vish mila bhojan hai

“Tumhe lagta hai tum amar ho, par Rama manushya hote hue bhi mrityu ban sakte hain”

🔥 Yeh baat Ravana ke ahankaar ko todne wali thi.

Lanka ke vinaash ki bhavishyavani

Hanuman saaf kehte hain:

“Main akela Lanka jala sakta hoon”

Par Rama ne abhi aadesh nahi diya

Jab vanar sena aayegi,
Lanka raakh ban jayegi

🐒 Yeh ghamand nahi, sach hai — jo Hanuman pehle hi dikha chuke the.

Aakhri updesh (Last Warning)

Hanuman Ravana ko antim avsar dete hain:

“Janaki ko lautaa do
Apna vansh, mitra, putra aur nagari bacha lo”

Par…

Ravana ka faisla

Hanuman ke satya-vachan
Ravana ko zehar jaise lagte hain

👁️‍🗨️ Aankhen laal
😡 Ahankaar jaag utha

👉 Ravana aadesh deta hai:
“Is vanar ko maar do.”

Gehri Seekh (Moral)

Satya kadwa hota hai, isliye ahankari use bardasht nahi kar paate

Doot ka kaam sirf sandesh dena nahi, dharm yaad dilana bhi hota hai

Jo stri ka apmaan karta hai, apna vinaash bulata hai

Bhakti jab sahas ban jaaye, toh vanar bhi devtaon ko hila deta hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.52
    with st.expander("Chapter 5.52 – Vibhishana asks Ravana to spare Hanuman"):
        text1 = """
        Chapter 52 – Vibhishan ne Hanuman ke liye awaaz uthayi

Hanuman ke sach aur kadve shabd sunkar
Ravana ka gussa aag ban gaya 🔥

Usne turant aadesh diya:
👉 “Is vanar ko maar daalo!”

Vibhishan ka dil dhadak utha

Yeh sunte hi Vibhishana ka mann hil gaya.
Woh jaante the — yeh galat hai.

Shaant hokar,
bina dare,
woh apne bade bhai Ravana ke saamne aaye."""
        create_image_text_layout("attached_assets/chapter5/5.52.jpg", text1, layout="side", image_position="left")

        text2 = """
        Vibhishan ne dharm ki baat kahi

Vibhishan ne pyaar aur shanti se kaha:

“Gussa thoda shaant karo, bhai.”

“Yeh sirf ek doot hai.”

“Doot ko maarna kabhi bhi dharm nahi hota.”

🕊️ Sach bolna aasaan nahi hota, par zaroori hota hai.

Doot ko maarna adharma hai

Vibhishan samjhaate hain:

Doot sandesh laata hai, yuddh nahi

Uski galti ka dand bhejne wale ko milta hai

Doot ke liye dand ho sakta hai:

baal kaat dena

sharir par nishaan

apmaan

❌ Par maut kabhi nahi

Ravana ka gussa phir bhadka

Ravana garaj kar bola:

“Paapi ko maarna paap nahi hota!”

Uski aankhon mein ahankaar tha 😡
Uske mann mein dharm dab chuka tha.

Vibhishan ka sabse bada satya

Vibhishan ne fir bhi haar nahi maani:

“Agar tum doot ko maar doge, koi aur sandesh lekar nahi aayega.”

“Asli dand Rama aur Lakshman par padna chahiye.”

“Is vanar ko maarna tumhari shaan ke khilaaf hai.”

🌿 Jo sach bolta hai, woh akela bhi ho sakta hai.

Yuddh ki baat, par nyay ke saath

Vibhishan bole:

“Tumhein yuddh pasand hai.”

“Toh Rama-Lakshman se saamna karo.”

“Tumhare veer yoddha taiyaar hain.”

⚔️ Yeh bhay se nahi, garv se bola gaya satya tha.

Ravana ne pehli baar socha…

Vibhishan ke shabd
Ravana ke gusse se takraaye 💥

Aur…
pehli baar Ravana ne sochna shuru kiya 🤯

Shayad…
yeh vanar maarne layak nahi.

Moral (Seekh)

Sach bolna gaddari nahi hota

Doot ka samman sabse upar hota hai

Gussa buddhi ko andha kar deta hai

Jo dharm ke saath khada hota hai, wahi asli veer hota hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.53
    with st.expander("Chapter 5.53 – Hanuman is taken through the city as a prisoner"):
        text1 = """
        Chapter 53 – Hanuman ko bandhan mein shehar ghumaya gaya

Ravana ne thandi saans li.
Usne kaha:

“Doot ko maarna galat hai.
Par saza toh milegi.”

Ravana bola:
👉 “Vanar ki poonchh hi uska ghamand hoti hai.
Iski poonchh jala do.”

Aur hukm diya:
👉 “Jalti poonchh ke saath isse poori Lanka ghumao.”"""
        create_image_text_layout("attached_assets/chapter5/5.53.jpg", text1, layout="side", image_position="left")

        text2 = """
        Hanuman ki poonchh mein aag

Rakshason ne
Hanuman ki poonchh par
kapda lapeta,
tel daala,
aur aag laga di 🔥

Hanuman ka sharir aur bada ho gaya.
Jaise jungle mein aag bhadak jaaye.

Woh gusse mein garja,
par bandha rehna chuna.

Hanuman ka mann shaant tha

Hanuman ne socha:

“Main chaahun toh sabko gira doon.”

“Par main Rama ke kaam se aaya hoon.”

“Unke liye main yeh seh loonga.”

💛 Yeh shakti nahi, bhakti thi.

Lanka ki sadkon se guzarna

Nagare baje.
Shankh baje.
Bachche, auratein, buddhe – sab dekhne aaye.

Log chilla rahe the:
👉 “Yeh jasoos hai!”

Hanuman chupchaap
Lanka ko dekh raha tha 👀
Unchi imaaratein.
Sundar sadkein.
Bade mahal.

Sita ki aankhon se aansu

Rakshasiyaan bhaag kar
Sita ke paas aayi.

Boli:
👉 “Wahi vanar…
uski poonchh jal rahi hai.”

Sita ka dil kaanp utha 😢
Unhone agni dev se prarthana ki:

🙏
“अगर मैं सच्ची पतिव्रता हूँ,
तो इस वानर को मत जलाना।”

Agni dev ne chamatkaar dikhaya

Aag bhadak rahi thi 🔥
par Hanuman ko dard nahi.

Thandi hawa chali ❄️
Pawan dev ne foonk maari.

Hanuman hairaan hua:

“इतनी आग…
पर मुझे कुछ नहीं जल रहा!”

✨ Yeh Rama ki kripa thi.
✨ Yeh Sita ki pavitrata thi.
✨ Yeh Pawan pita ka ashirvaad tha.

Ab Hanuman ka roop badla

Hanuman ne socha:

“Bas ho gaya.
Ab vanar chup nahi rahega.”

💥 Channnng!
Rassiyan toot gayi.

Woh ek hi chhalang mein
shehar ke gate par pahunch gaya.

Chhota bana.
Bandhan utaare.
Phir pahaad jaisa bada ho gaya.

Aag ki poonchh, suraj jaisa tej

Gate par ek lohe ka danda pada tha.
Hanuman ne uthaya.

Rakshas gire.
Gate saaf hua.

Jalti poonchh
suraj ki kiranon jaisi lag rahi thi ☀️

Hanuman ne poori Lanka ko dekha.

🔥 Yeh sirf shuruaat thi.

Moral (Seekh)

Sachcha sevak dard bhi hans kar sehta hai

Bhakti aag ko bhi thanda kar deti hai

Shanti jab toot ti hai, toh vinash aata hai

Hanuman ka gussa = dharm ka shastra"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.54
    with st.expander("Chapter 5.54 – Hanuman burns the city of Lanka"):
        text1 = """
        Chapter 54 – Hanuman ne Lanka jala di (Lanka Dahan)

Hanuman ne upar se poori Lanka ko dekha.
Usne mann mein socha:

“Kaam ho chuka hai.
Baag ujad gaya.
Rakshas mare gaye.
Ab sirf Lanka ka ghamand todna baaki hai.”

Uski poonchh abhi bhi aag se jal rahi thi 🔥
Jaise badal ke andar bijli chamak rahi ho."""
        create_image_text_layout("attached_assets/chapter5/5.54.jpg", text1, layout="side", image_position="left")

        text2 = """
        Aag ki shuruaat

Hanuman ne chhalang lagayi.
Ek chhat se doosri chhat.

🔥 Dhadak!
Pehla mahal jala.

Phir doosra.
Phir teesra.

Woh rukta nahi tha.
Hawa jaisa tez.
Aag jaisa bhayanak.

Rakshason ke mahal jalne lage

Hanuman ne:

senapatiyon ke ghar jala diye

yoddhaon ke mahal jala diye

khazane jala diye

shastra-graha jala diye

Sona, chandi, heere
pighal kar behne lage 💎

Rakshas chillane lage:

👉 “Yeh vanar nahi!
Yeh toh Agni Dev khud hai!”

Lanka mein hahakar

Auratein bachchon ko le kar bhaagi 😢
Kuch log aag mein gir pade.
Kuch chhaton se kud gaye.

Shehar mein sirf cheekhein thi.
Sirf dhuaan.
Sirf aag.

🔥 Poora Lanka jal raha tha.

Hanuman ka dhyan

Itni tabahi ke beech bhi
Hanuman ka mann shaant tha.

Uske mann mein sirf ek naam tha:

💛 Rama

Na gussa.
Na ahankaar.
Sirf kartavya.

Ashoka Vatika surakshit

Ek jagah aisi thi
jahan aag nahi pahunchi.

🌿 Ashoka Vatika
Jahan Sita thi.

Hanuman ne dhyan rakha.
Sita ko koi nuksaan nahi hua.

🔥 Dharm ne paap ko chhua,
par pavitrata ko nahi.

Devta bhi hairaan

Aasmaan se Devta dekh rahe the 😮
Rishi, Gandharva, Siddha sab bole:

“Yeh sirf vanar nahi.
Yeh Ishwar ki ichchha hai.”

Hanuman poori Lanka jala kar
samundar ke kinaare aaya 🌊

Aur apni jalti poonchh
samundar mein bujha di.

🔥➡️🌊

Lanka khaak, Hanuman shaant

Lanka jal chuki thi.
Ghamand toot chuka tha.
Sandesh pahunch chuka tha.

Hanuman ne upar dekha
aur mann hi mann bola:

“Ab Rama ka kaam shuru hoga.”

Moral (Seekh)

Ghamand ka ant nischit hota hai

Bhakti ke aage aag bhi thandi pad jaati hai

Hanuman ka gussa bhi dharm se bandha tha

Jahan Sita aur Rama ka naam hai, wahan vinaash bhi maryada mein hota hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.55
    with st.expander("Chapter 5.55 – Hanuman worries about Sita’s safety"):
        text1 = """
        Chapter 55 – Hanuman ki chinta aur Sita ki raksha ka nishchay

Lanka jal chuki thi.
Har taraf aag, dhuaan aur hahakar tha.
Rakshas bhay se bhaag rahe the.

Par is sab ke beech, Hanuman ka mann achanak ashant ho gaya."""
        create_image_text_layout("attached_assets/chapter5/5.55.jpg", text1, layout="side", image_position="left")

        text2 = """
        Hanuman ka pachtava

Hanuman ne socha:

“Maine gusse mein aakar kya kar diya?
Agar is aag mein Sita jal gayi ho,
toh meri poori yatra vyarth ho gayi!”

Usse apna gussa paap jaisa lagne laga.
Usne kaha:

gussa buddhi chheen leta hai

gussa guru aur sajjanon ka bhi apmaan kara deta hai

gussa vivek ko andha kar deta hai

Hanuman ne khud ko doshi maana:

“Lanka jalana chhoti baat hai,
par agar Sita ko nuksaan hua ho,
toh main apne swami Rama ka kaam bigaad chuka hoon.”

Uske mann mein bhay aur dukkh umad aaya 😔

Atma-tyag ka vichaar

Usne yahan tak soch liya:

samundar mein kud jaaun

agni mein pravesh kar jaun

jeevit rehkar Rama, Sugriva aur Lakshmana ka saamna kaise karunga?

Usse laga:

“Mere kaaran Ikshvaku vansh ka naash ho jaayega.”

Umeed ki kiran

Phir Hanuman ne kuch baatein yaad ki:

Agni ne uski poonchh nahi jalayi

Mainaka parvat ne samundar mein sahayata ki

Sita pavitrata ki moorti hai

Tab usne socha:

“Agni, jo mujhe nahi jala saka,
woh Sita ko kaise jala sakta hai?
Pavitrata ko aag chhoo nahi sakti.”

Sita ki tapasya, satitva aur Rama ke prem par usse vishwas hua 💛

Dev-vani (divine confirmation)

Tab Hanuman ne Charanon (divya rishiyon) ko baat karte suna:

“Poora Lanka jal gaya hai,
par Janaki surakshit hai!
Yeh ek adbhut chamatkar hai!”

Ye shabd amrit jaise the 🕊️
Hanuman ka mann turant halka ho gaya.

Hanuman ka nischay

Ab sab spasht tha:

Sita surakshit hai

Rama ka kaam safal hua

Lanka ka ghamand toot chuka

Hanuman ne nischay kiya:

“Main jaane se pehle Sita ko ek baar aur dekhunga,
phir Rama ke paas laut kar
unhe sab suchit karunga.”

Adhyay ki Seekh (Moral)

Veerta ke saath vivek zaroori hai

Gussa sab kuch jala sakta hai, par bhakti sab kuch bacha leti hai

Sita jaise pavitr aatmaon ko prakriti bhi hani nahi pahuncha sakti

Hanuman ka mahatva sirf shakti nahi, vinamrata aur pashchatap bhi hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.56
    with st.expander("Chapter 5.56 – Hanuman meets Sita again and takes leave"):
        text1 = """
        Chapter 56 – Hanuman Sita se vida leta hai

Hanuman ne Sita ko
Shimshapa tree ke neeche dekha.
Usne jhuk kar pranam kiya.

Hanuman bola,

“Devi, bhagya se aap surakshit ho.
Yeh dekh kar mera mann shant ho gaya.”"""
        create_image_text_layout("attached_assets/chapter5/5.56.jpg", text1, layout="side", image_position="left")

        text2 = """
        Sita ka mann bhar aaya

Sita ne Hanuman ko baar-baar dekha.
Unki aankhon mein aansu the 😢

Sita boli:

“Beta, agar theek lage
toh aaj yahin chup kar ruk jao.
Kal jaana.
Tumhare paas rehkar
mera dukh thoda kam ho jaata hai.”

Phir unhone dheere se kaha:

“Tum jaoge…
par kya pata
main tab tak zinda rahoon ya nahi.
Tumhare jaate hi
mera dard aur badh jaayega.”

Sita ko chinta thi:

samundar bahut bada hai

monkeys aur bears kaise aayenge?

Rama aur Lakshmana kaise pahunchenge?

Unhone kaha:

“Is samundar ko
sirf teen hi paar kar sakte hain –
Garuda, tum aur Pavan Dev.”

Sita ka garv aur maryada

Sita boli:

“Tum yeh kaam kar sakte ho,
par yeh yudh Rama ka hai.
Unhi ko Lanka jeetni chahiye.
Unki veerta hi dharma hai.”

Yeh kehkar Sita chup ho gayi.
Unki baat mein prem bhi tha,
buddhi bhi aur maryada bhi 🌸

Hanuman ka vachan

Hanuman ne haath jod kar kaha:

“Devi, chinta na karein.
Sugriva
crore-crore vanaron ke saath aa rahe hain.”

“Rama aur Lakshmana
Lanka ko apne teeron se hila denge.
Ravana ka ant nishchit hai.”

Hanuman ne vishwas dilaya:

“Bahut jaldi
aap Rama ke saath hongi.
Jaise Rohini chand ke saath hoti hai 🌙”

Sita ka mann halka ho gaya 💛

Vida ka pal

Hanuman ne phir se pranam kiya.
Sita ne ashirvaad diya.

Hanuman ne socha:

“Ab mujhe apne Prabhu Rama ke paas jaana hai.”

Mahaan chhalaang

Hanuman Arishta parvat par chadhe.
Parvat unki shakti se kaanp utha.

Jahan Hanuman ne pair rakha,
wahan chattan toot gayi.

Phir Hanuman ne:

poori shakti jodi

samundar ki taraf dekha

aur ek mahaan chhalaang laga di 🌊

Parvat dharti mein dhans gaya.
Van ke jeev bhaag gaye.
Aakash goonj utha.

Aur Hanuman…
hawaa ki tarah udaan bhar gaye 🕊️

Is adhyay ki seekh (Moral)

Prem mein dhairya zaroori hai

Veerta ko maryada ke saath chalna chahiye

Sita ka bal sharir ka nahi, charitra ka hai

Hanuman ki shakti se zyada, unki bhakti mahaan hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.57
    with st.expander("Chapter 5.57 – Hanuman returns from Lanka"):
        text1 = """
        Chapter 57 – Hanuman ka Safal Pratyavartan (The Return of Hanuman)

Lanka ko jala kar, Hanuman
ab apne prabhu Rama ke paas laut raha tha.

Ek pankh laga parvat jaise,
Hanuman ne ek hi chhalaang mein
akash ke samundar ko paar kiya 🌊☁️

Sooraj, chandrama, taare aur badal
uske raaste ke saathi ban gaye.
Kabhi badalon mein chhup jaata,
kabhi unhe cheer kar nikal aata —
bilkul chandrama ki tarah 🌙"""
        create_image_text_layout("attached_assets/chapter5/5.57.jpg", text1, layout="side", image_position="left")

        text2 = """
        Mahendra Parvat ki aur

Udaan bharte hue Hanuman ne
Mainaka Parvat ko pranam kiya
aur tez garaj ke saath
Mahendra Parvat ki aur badhe.

Unki garaj se
das dishaayein goonj uthiं ⚡
aur samundar ke us paar
vanaron ne yeh shabd sun liye.

Vanar sena ko sanket

Uttar tat par intezaar kar rahe
sab vanar pehle udaas the…

Par jaise hi
Hanuman ki garaj sunai di —
sabke chehre khil uthe 😄

Tab Jambavan bole:

“Nishchit hi Hanuman safal hua hai!
Asafal hota toh aisi garaj na karta.”

Sab vanar khushi se uchhal pade,
pedon, chattanon par chadh gaye
aur haath hila-hila kar
Hanuman ka swagat kiya 🎉

Mahaan avtar

Hanuman Mahendra Parvat par utare —
badalon ke pahaar jaise prakaashmaan ☁️

Sab vanaron ne
haath jod kar pranam kiya
aur phal, mool, shaak lekar aaye 🍌🍎

Hanuman ne
bade buzurgon ko pranam kiya
aur Angada ka haath pakad kar baith gaye.

Bas ek hi vaakya kaha:

“Maine Devi ko dekh liya hai.”

Amrit ke saman shabd

Yeh shabd sunte hi
vanaron mein anand ki lehar daud gayi ✨

Hanuman ne bataya:

Sita Ashoka Vatika mein hain

Rakshasi unki rakhwali karti hain

ek hi choti baandhe hue

upvaas se durbal

dhool se lipti

sirf Rama ka smaran karti hui 💔

Yeh sunte hi
vanaron ne nritya, uchhal, garjan shuru kar di.

Angada ka samman

Angada ne Hanuman se kaha:

“Tumhara saahas atulniya hai!
Tumne samundar paar kiya
aur hum sabko jeevan daan diya.”

“Tumhari bhakti, shakti aur sahan-shakti
apratim hai.
Ab Rama ka shok nishchit hi door hoga.”

Yudh ka sanket

Sab vanar
Hanuman ke chaaron or baith gaye
aur Lanka, Sita aur Ravana ki katha
sunne ko utavle ho gaye.

Mahendra Parvat
aisa lag raha tha
jaise swarg ka darbar ho —
beech mein Angada
aur unke paas
veer Hanuman ✨

Is adhyay ki seekh (Moral)

Bhakti aur kartavya ka milan hi veerta hai

Ek satya shabd poori sena ko jeevan de sakta hai

Hanuman ki safalta unki shakti se nahi, nishtha se aayi

Yeh adhyay Ram–Ravana yudh ka shankhnaad hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.58
    with st.expander("Chapter 5.58 – Hanuman tells everyone about his journey"):
        text1 = """
        Chapter 58 – Hanuman apni poori kahani sunate hain

(Hinglish • simple • children’s moral story tone)

Mahendra Parvat ke shikhar par
sab vanar shaant hokar baith gaye.
Unki nazar sirf Hanuman par thi 👀
sabke mann mein khushi aur utsukta thi.

Tab Jambavan ji ne pyaar se poocha:

“Veer Hanuman,
tumne Sita Mata ko kaise dhoonda?
Woh wahan kaisi hain?
Ravana unke saath kaisa vyavhaar karta hai?
Humein sab sach-sach batao.”

Hanuman ne pehle Sita Mata ko mann hi mann pranam kiya 🙏
phir muskurate hue bolna shuru kiya."""
        create_image_text_layout("attached_assets/chapter5/5.58.jpg", text1, layout="side", image_position="left")

        text2 = """
        Samundar par chhalaang

“Tum sabke saamne,”
Hanuman bole,
“main Mahendra Parvat se akash mein chhalaang laga kar
samundar paar karne nikla.

Raaste mein ek sunehra parvat dikha.
Main use todne hi wala tha,
tab usne madhur awaaz mein kaha:

‘Main Mainaka Parvat hoon.
Main tumhare pita Vayu dev ka mitra hoon.
Rama dharm ke rakshak hain,
main unki seva karna chahta hoon.’

Maine use pranam kiya
aur aage badh gaya.”

Surasa aur Sinhika

“Aage samundar mein
Devi Surasa ne mujhe roka.

Unhone kaha,
‘Tumhe meri bhojan banna hoga.’

Maine vinamrata se kaha,
‘Mata, kaam poora karke laut aunga.’

Unka muh bada hota gaya,
main aur chhota hota gaya 😄
ek pal mein unke muh mein jaakar
bahar aa gaya.

Devi khush ho gayi aur boli:

‘Jao beta,
tumhara kaam safal ho.’

Phir ek rakshasi Sinhika ne meri chhaya pakad li.
Maine turant uska ant kar diya
aur bina ruke aage badh gaya.”

Lanka mein pravesh

“Shaam hote hi
main chup-chaap Lanka mein ghusa.

Shehar ki rakshika ne mujhe roka,
par maine use hata diya.

Raat bhar khoj ki…
Ravana ke mahal dekhe…
par Sita Mata wahan nahi mili 😔

Tab mujhe Ashok Vatika dikhi.

Wahan Shimshapa vriksh ke neeche
maine Sita Mata ko dekha 🌸

Woh:

kamzor thi

upvaas mein thi

sirf Rama ka naam le rahi thi

rakshasiyon se gheri hui thi

Mera hriday bhar aaya 💔”

Ravana aur Sita ka samvaad

“Tab Ravana wahan aaya.
Usne ghamand se dhamki di.

Par Sita Mata ne nirbhay hokar kaha:

‘Tum Rama ke daas banne layak bhi nahi ho!
Tumhara ant nishchit hai.’

Ravana gusse se bhar gaya,
par Mandodari ne use shaant kiya.”

Hanuman aur Sita ka milan

“Raat ko maine dheere se bola
aur apna parichay diya.

Maine Rama ki anguthi di 💍
Sita Mata ki aankhon mein aansu aa gaye.

Unhone kaha:

‘Rama ko jaldi bulaana.
Mere paas sirf do mahine hain.’

Unhone mujhe apna choodamani diya
aur ashirvaad diya.”

Lanka ka vinash

“Sita Mata ke shabd sun kar
mera khoon khol gaya 🔥

Maine:

Ashok Vatika ujaadi

Kinkaron ko haraya

Senapatiyon ko maara

Akshay ko giraya

Ant mein Indrajit ne
Brahmastra se mujhe baandha.

Ravana ke darbar mein
maine sach keh diya:

‘Main Rama ka doot hoon.’

Ravana mujhe maarna chahta tha,
par Vibhishan ne mujhe bachaya.”

Poonch mein aag 🔥

“Ravana ne hukm diya
meri poonch jalai jaaye.

Maine mauka dekha,
bandhan toda
aur poori Lanka jala di 🔥🔥🔥

Phir mujhe chinta hui –
kahin Sita Mata ko kuch na ho gaya ho!

Tab dev vaani sunai di:

‘Sita surakshit hain.’

Mera mann shaant ho gaya 😊”

Ant aur sandesh

“Main dobara Sita Mata se mila,
unhe pranam kiya
aur yahan laut aaya.

Yeh meri poori yatra hai.

Ab jo baaki hai,
woh tum sab aur Rama ko milkar poora karna hai.”

Is adhyay ki seekh (Moral) 🌟

Shraddha aur dhairya se har mushkil paar hoti hai

Vinamrata bal se zyada shaktishaali hoti hai

Sach aur dharm ka saath dene wala kabhi akela nahi hota

Hanuman ki shakti se zyada unki bhakti mahan thi"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.59
    with st.expander("Chapter 5.59 – Hanuman urges the monkeys to rescue Sita"):
        text1 = """
        Chapter 59 – Hanuman vanaron se Sita ko bachane ki prarthana karte hain

(Hinglish • short sentences • children’s moral story tone)

Apni poori kahani sunane ke baad,
Hanuman ji ne sab vanaron ki taraf dekha 👀
unki awaaz mein josh bhi tha aur bhakti bhi.

Hanuman bole:

“Ab main sach mein khush hoon.
Rama aur Sugriva ka prayas safal raha.
Maine Sita Mata ki dridh bhakti dekhi hai.
Unka mann bilkul tootaa nahi hai."""
        create_image_text_layout("attached_assets/chapter5/5.59.jpg", text1, layout="side", image_position="left")

        text2 = """
        O vanaro 🐒
Sita Mata tapasya ki shakti se
poori dharti ko sambhaal bhi sakti hain
aur gusse mein bhasm bhi kar sakti hain.
Aag se zyada bhayankar hai unka krodh.

Ravana zinda isliye hai
kyunki use tapasya ka vardaan mila hai.
Par uska ant nishchit hai.
Woh kaam Rama ke liye rakha gaya hai.”

Vanar sena ko bulava

Hanuman aage bole:

“Ab samay aa gaya hai.
Sab shaktishaali vanar yatra ke liye taiyaar ho jao.
Jambavan ji aage honge,
Angad, Nila, Dvivida sab saath honge.

Agar main akela Lanka mein ghus sakta hoon,
shehar jala sakta hoon 🔥
toh socho,
poori vanar sena kya nahi kar sakti?”

Apni shakti par vishwas

Hanuman garv se bole:

“Tumhari anumati ho
toh main Ravana,
uske beton, bhaiyon,
aur poori rakshas sena ka ant kar sakta hoon.

Indrajit ke divya astr bhi
humein nahi rok sakte.

Jambavan ji kabhi nahi darte

Angad akela poori sena mita sakta hai

Nila parvat hila sakta hai

Dvivida ka koi muqaabla nahi

Ashvini Kumar ke putra vanar
bhi ajey hain

Aur maine toh akela hi Lanka jala di.”

Lanka mein ghoshna

Hanuman muskuraye aur bole:

“Lanka ki har gali mein
maine zor se kaha:

‘Rama aur Lakshmana ki jai!’
‘Sugriva Maharaj ki jai!’
‘Main Pavana putra Hanuman hoon!’

Yeh sandesh sabne suna.”

Sita Mata ki sthiti

Phir Hanuman ka chehra gambhir ho gaya 😔

“Par ek baat suno, mitron…

Sita Mata Ashok Vatika mein hain.
Shimshapa ped ke neeche.
Rakshasiyon se gheri hui.

Woh:

ek hi vastra pehenti hain

dhool se bhari hui hain

kamzor ho rahi hain

zameen par soti hain

Par unka mann sirf Rama mein laga hai ❤️

Ravana ko woh ghrina se dekhti hain.
Unki bhakti kabhi nahi hili.”

Samay kam hai

Hanuman ne dheemi awaaz mein kaha:

“Sita Mata har din
aur kamzor hoti ja rahi hain.
Rama se bichhadne ka dukh
unhe dheere-dheere tod raha hai.

Maine mushkil se
unke mann mein aasha jagayi hai.

Ab faisla tum sabko lena hai.”

Is adhyay ki seekh (Moral) 🌼

Ek sachcha sevak sabko jagata hai, sirf khud nahi ladta

Sangathan mein apaar shakti hoti hai

Sita jaise dhairya aur bhakti se hi adharma girta hai

Samay par sahi kadam uthana hi jeet hoti hai"""
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter 5.60
    with st.expander("Chapter 5.60 – Jambavan rejects Angada’s plan"):
        text1 = """
        Chapter 60 – Jambavan Angada ke plan ko kyun mana karte hain

(Hinglish • short • simple • moral story tone)

Hanuman ki baat sunne ke baad,
Angada aage aaye.
Unki awaaz mein josh aur garv tha.

Angada bole:

“Hum Ashvini Kumar ke putron ke baare mein jaante hain.
Woh dono ajey hain.
Brahma ji ke vardaan se unhe koi maar nahi sakta.

Unhone devtaon ko bhi hara diya tha.
Amrit bhi pee liya tha."""
        create_image_text_layout("attached_assets/chapter5/5.60.jpg", text1, layout="side", image_position="left")

        text2 = """
        Agar woh chahein,
toh poori Lanka ko mita sakte hain.
Phir hum jaise vanar kya nahi kar sakte?

Hanuman ji ne akela Lanka jala di 🔥
Sita Mata ko dekha.
Par unhe wapas nahi laaya.

Mujhe lagta hai
ki itne veer vanar hote hue
Rama ko sirf sandesh dena theek nahi.

Main akela Ravana ko maar sakta hoon.
Aur agar sab vanar saath hon,
toh jeet pakki hai.

Isliye mera vichaar hai:
Hum sab turant Lanka jaayein.
Rakshason ka naash karein.
Aur Sita Mata ko Rama aur Lakshmana ke paas le aayein.

Kishkindha ke doosron ko bulane ki zarurat nahi.”

Jambavan ka shaant aur gyaan bhara uttar

Yeh sun kar
Jambavan ji muskuraye 😊
Unki awaaz mein shanti aur buddhi thi.

Jambavan bole:

“O Angada,
tumhara vichaar veerta se bhara hai.
Par dhyaan se suno.

Humein Rama aur Sugriva ka aadesh mila tha.
Hamara kaam sirf yeh tha
ki hum Sita Mata ka pata lagayein.

Humein yeh aadesh nahi mila
ki hum unhe wapas le aayein.

Aur Rama…
woh apni pratigya ke liye mashhoor hain.
Unhone sabke saamne kaha hai
ki woh khud Sita Mata ko laayenge.

Agar hum unki jagah kaam karein,
toh unki pratigya toot jaayegi.
Aur yeh kaam unhe pasand nahi aayega.

Veerta tabhi safal hoti hai
jab maryada ke saath ho.

Isliye sabse sahi raasta yahi hai:
Hum turant wapas chalein.
Rama, Lakshmana aur Sugriva ko
poori sachchai batayein.

Jeet tab hogi
jab hum Rama ki yojna ke saath chalenge.”

Is adhyay ki seekh (Moral) 🌱

Sirf shakti hi nahi, maryada bhi zaroori hoti hai

Apne kaam ki seema pehchanna bhi gyaan hai

Sahi neta ki yojna ke saath chalna hi vijay deta hai

Veerta bina niyam ke ghamand ban jaati hai"""
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
