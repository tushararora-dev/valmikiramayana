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
