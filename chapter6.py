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
        Chapter 1 – Rama felicitates Hanuman (Hinglish Story Rewrite)

Hanuman apni poori journey calmly suna raha tha.
Uski baatein sunte hi Rama ka dil khushi se bhar gaya.

Rama muskuraye aur bole,
“Hanuman, tumne jo kaam kiya hai, woh duniya ka sabse mushkil kaam tha.
Aisa kaam koi aur soch bhi nahi sakta.”

Unki awaaz mein garv tha.
“Is bade samundar ko paar karna aasaan nahi tha.
Sirf Garuda aur Vayu jaise shaktishaali hi yeh kar sakte hain.
Par tumne kar dikhaya.”"""
        create_image_text_layout("attached_assets/chapter6/6.1.jpg", text1, layout="side", image_position="left")

        text2 = """
        Rama ne aage kaha,
“Lanka ek bahut hi majboot nagri hai.
Wahan Ravana ka raaj hai.
Dev, Danav, Yaksha, Gandharva… koi bhi wahan jaakar zinda wapas nahi aa sakta.
Par tum gaye, kaam poora kiya, aur laut aaye.”

Hanuman shaant khade the.
Unke chehre par ahankaar nahi tha.
Sirf bhakti aur vinamrata thi.

Rama bole,
“Ek sacha sevak wahi hota hai jo mushkil kaam ko bhi khushi se poora kare.
Tumne Sugriva ka kaam poore mann se kiya.
Tum sach mein shreshth sevak ho.”

Phir Rama ki aankhen nam ho gayi.
Unhone kaha,
“Tumhari wajah se humein Sita ka pata chala.
Lakshmana aur main bach gaye.
Par mera dil bhaari hai.
Main tumhara yeh ehsaan kaise chukaun?”

Rama thoda ruk gaye.
Phir bole,
“Abhi main sirf itna hi kar sakta hoon.”

Itna kehkar Rama ne Hanuman ko gale laga liya.
Unke haath kaanp rahe the, khushi se.
Hanuman ne bhi sir jhuka liya.
Unka kaam poora ho chuka tha.

Thodi der baad Rama gehri soch mein pad gaye.
Unhone samundar ki taraf dekha.

Rama bole,
“Sita mil gayi hai, yeh sach hai.
Par yeh samundar bahut bada hai.
Vanar sena ise kaise paar karegi?”

Unki awaaz mein chinta thi.
“Ab aage kya karein?
Kaise sab ko doosre kinare tak le jayein?”

Yeh kehkar Rama chup ho gaye.
Unka mann ghabra raha tha.
Woh gehri soch mein doob gaye.

Yahin se ek nayi chunauti shuru hoti hai…"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.2
    with st.expander("Chapter 6.2 – Sugriva comforts Rama"):
        text1 = """
        Chapter 2 – Sugriva consoles Rama (Hinglish Story Rewrite)

Rama gehri udaasi mein doob gaye the.
Unki aankhon mein chinta saaf dikh rahi thi.

Tab Sugriva aage aaye.
Unki awaaz shaant thi, par bharosa bhari hui.

Sugriva bole,
“Rama, aap aise dukhi kyun ho jaise koi aam insaan ho?
Aap veer ho.
Is tarah ka vishad aapko shobha nahi deta.”

Unhone dheere se kaha,
“Ab to humein Sita ka pata chal gaya hai.
Shatru ka thikana bhi jaan liya hai.
Phir darr kis baat ka?”"""
        create_image_text_layout("attached_assets/chapter6/6.2.jpg", text1, layout="side", image_position="left")

        text2 = """
        Sugriva ne Rama ki taraf vishwas se dekha.
“Aap buddhimaan ho.
Shastra jaante ho.
Apne mann ko sambhaliye.
Yeh bekaar ke darr safalta ke dushman hote hain.”

Phir Sugriva ne samundar ki taraf ishara kiya.
“Yeh samundar chahe kitna bhi bhayanak ho,
hum ise paar karenge.
Lanka par hamla karenge
aur Ravana ka ant karenge.”

Unki awaaz mein josh aa gaya.
“Jo vyakti dukh aur darr mein dooba rehta hai,
woh kuch bhi bada kaam nahi kar paata.
Aisa vyakti khud hi apna nuksaan karta hai.”

Sugriva bole,
“Yeh vanar sena aapke liye aag mein bhi kood jaane ko tayyar hai.
Inka saahas dekh kar mujhe poora vishwas hai.”

Unhone garv se kaha,
“Mujhe ijazat dijiye.
Main Ravana ko maar kar Sita ko wapas laaunga.”

Phir woh bole,
“Par pehle humein ek pul banana hoga.
Bina pul ke Lanka tak pahunchna mushkil hai.
Samundar itna bhayanak hai
ki Dev aur Asur bhi bina pul ke wahan nahi ja sakte.”

Sugriva muskuraye.
“Jaise hi pul banega
aur sena us par se guzregi,
Ravana pehle hi haar chuka samjho.”

Unhone vanaron ki taraf dekha.
“Yeh yoddha apna roop badal sakte hain.
Pathar aur ped se shatru ko kuchal denge.”

Phir Sugriva ne Rama se kaha,
“Is kamzori ko chhod dijiye, Maharaj.
Dukh se insaan kamzor ho jaata hai.
Jo karna hai, usey dridhta se aur jaldi karna chahiye.”

Unki baat mein seekh thi.
“Shakti ke saath dharm jodo.
Maha-veer yoddha dukh ko apni taakat khatm karne nahi dete.”

Sugriva ne vishwas se kaha,
“Aap jaise dhanurdhar ke saamne
teenon lokon mein koi tik nahi sakta.
Hum aapke saath hain.
Aapki jeet nishchit hai.”

Ant mein Sugriva bole,
“Jaise hi hum samundar paar kar lenge,
Sita aapko jaldi hi mil jaayengi.
Ab shok chhodiye
aur apna krodh aur saahas jagaiye.”

Rama chup the.
Par unke mann mein nayi roshni jag chuki thi.
Umeed phir se zinda ho rahi thi.

Yuddh ka marg ab saaf dikhne laga…"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.3
    with st.expander("Chapter 6.3 – Hanuman tells Rama about Lanka’s strength"):
        text1 = """
        Chapter 3 – Hanuman describes the Strength of Lanka (Hinglish Story Rewrite)

Sugriva ki samajhdaar baatein sun kar
Rama ka mann thoda shaant ho gaya.

Rama ne Hanuman ki taraf dekha.
Unki awaaz sthir thi.

Rama bole,
“Tapasya ke bal se main samundar paar kar sakta hoon.
Chaahun to pul bana sakta hoon.
Chaahun to samundar ko shaant bhi kar sakta hoon.”"""
        create_image_text_layout("attached_assets/chapter6/6.3.jpg", text1, layout="side", image_position="left")

        text2 = """
        Phir Rama ne poocha,
“Par Lanka kaisi hai?
Uski suraksha kaisi hai?
Gate kaise hain?
Sena kitni strong hai?”

Unhone dhyaan se kaha,
“Tum wahan gaye the.
Sab kuch dekha hai.
Mujhe aise batao
jaise main khud wahan khada hoon.”

Hanuman aage aaye.
Unka chehra gambhir tha.
Par awaaz shaant aur spasht thi.

Hanuman bole,
“Rama, main sab bataunga.
Lanka ki deewarein,
uske gaddhe,
uski sena…
sab kuch.”

Phir Hanuman ne kehna shuru kiya.

“Lanka ek bhari-bhari shehar hai.
Wahan log khush dikhte hain.
Haathi, rath aur rakshas har jagah hain.”

“Us shehar ke chaar bade gate hain.
Gate bahut unche hain.
Lohe ke bhaari darwaaze lage hue hain.”

“Har gate ke paas hathiyaar rakhe hain.
Bhale, pathar, teer…
sab kuch tayyar rehta hai.”

Hanuman ne aage kaha,
“Lanka ke chaaro taraf sunehri deewar hai.
Deewar par ratn, moti aur mani chamak rahe hain.”

“Deewar ke bahar gehre gaddhe hain.
Unmein thanda paani hai.
Magar aur machhliyan bhi hain.”

“Pul uthane wale bridge hain.
Aur har jagah yuddh ke yantra lage hue hain.
Shatru aaye to seedha gaddhon mein gir jaaye.”

Hanuman ne gambhir swar mein kaha,
“Ravana khud bahut shaktishaali hai.
Woh hamesha yuddh ke liye tayyar rehta hai.
Apni sena par hamesha nazar rakhta hai.”

“Lanka pahaad par basi hai.
Chaaro taraf samundar hai.
Wahan koi naav aasaani se nahi pahunch sakti.”

“Ghode, haathi, rath…
sab kuch wahan bhara pada hai.
Lanka devon ke shehar jaisi lagti hai.”

Phir Hanuman ne sena ka vivaran diya.

“Purab ke gate par
das hazaar yoddha khade hain.”

“Dakshin ke gate par
ek lakh sainik hain.”

“Paschim ke gate par
talwar aur dhal wale yoddha hain.”

“Uttar ke gate par
laakhon sainik hain.
Rath aur ghodon par sawar.”

“Shehar ke beech mein bhi
hazaaron rakshas hain.
Sab anubhav wale yoddha.”

Hanuman thoda ruk gaye.
Phir bole,
“Mainne Lanka ki deewarein todi hain.
Gaddhe bhare hain.
Shehar ko aag bhi lag chuki hai.”

“Isliye agar hum samundar paar kar lein,
to Lanka humari hai.”

Unki awaaz mein vishwas tha.
“Angada, Jambavan, Nala, Nila
sab tayyar hain.”

“Bas aap aadesh dijiye, Rama.
Shubh samay mein hum nikal padenge.
Aur Sita ko wapas le aayenge.”

Rama chup the.
Par unki aankhon mein ab darr nahi tha.
Sirf tayyari aur sankalp tha.

Ab yuddh door nahi tha…"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.4
    with st.expander("Chapter 6.4 – The army reaches the sea shore"):
        text1 = """
        Chapter 4 – The Army reaches the Shores of the Sea (Hinglish Story Rewrite)

Hanuman ki poori baat sun kar
Rama ne dridh awaaz mein kaha,
“Ab mujhe sab kuch pata chal gaya hai.
Lanka ko nasht karne ka samay aa gaya hai.”

Rama Sugriva ki taraf mude.
“Ab deri nahi.
Suraj shubh sthiti mein hai.
Yeh vijay ka samay hai.”

Unki aankhon mein sankalp tha.
“Ravana kahin bhi chhup jaaye,
woh bach nahi paayega.
Jab Sita ko mere aane ka pata chalega,
unhe nayi zindagi milegi.”"""
        create_image_text_layout("attached_assets/chapter6/6.4.jpg", text1, layout="side", image_position="left")

        text2 = """
        Rama ne aakash ki taraf dekha.
“Saare shagun achhe hain.
Meri jeet nischit hai.”

Yeh sunkar Sugriva aur Lakshmana
Rama ke aage jhuk gaye.

Rama phir bole,
“General Nila ko aage bhejo.
Woh rasta dekhe.
Jahan phal, mool, paani aur chhaaya mile.”

Unhone chetavani di,
“Rakshas rasta bigaad sakte hain.
Isliye savdhaan rehna.”

Phir Rama ne sena ko vyavasthit kiya.
“Majboot vanar aage rahenge.
Kamzor peeche rukenge.”

Hanuman ke kandhon par chadh kar
Rama beech mein chale.
Jaise Indra Airavata par hote hain.

Lakshmana Angada ke kandhon par the.
Peeche Jambavan aur Sushena the.

Sugriva ne aadesh diya.
Aur tab vanar sena chal padi.

Pahaadon se, gufaon se,
hazaaron vanar nikal aaye.
Har taraf shor tha.
Josh tha.
Yuddh ki aag thi.

“Ravana ka ant hoga!”
Vanar zor se garaj rahe the.

Ped ukhad rahe the.
Phool ud rahe the.
Koi uchhal raha tha.
Koi palti kha raha tha.

Sena dakshin disha mein badhti chali.
Dharti kaanp rahi thi.
Dhoor aur shabd se sooraj bhi dhundhla lag raha tha.

Raste mein pahad aaye.
Jangal aaye.
Nadi aur jheel bhi aayi.

Vanar naha rahe the.
Phal kha rahe the.
Shahad pee rahe the.
Par ruk nahi rahe the.

Sabka ek hi lakshya tha.
Sita ko wapas lana.

Aakhir Rama Mahendra Parvat par pahunche.
Wahan se unhone pehli baar
us vishaal samundar ko dekha.

Lehron ki awaaz garaj rahi thi.
Machhli aur kachhue dikh rahe the.

Sahya aur Malaya Parvat paar kar ke
sena samundar ke kinare pahunchi.

Rama neeche utre.
Lakshmana aur Sugriva saath the.

Rama bole,
“Hum Varuna ke ghar pahunch gaye hain.
Ab sochna hoga
is samundar ko kaise paar karein.”

Unhone aadesh diya,
“Yahin shivir lagao.
Har neta apni sena ke saath rahe.
Koi dushman chhupa ho to dhyaan rakho.”

Sugriva ne turant vyavastha kar di.
Kinare par vanar sena
ek doosre samundar jaise lag rahi thi.

Lehren garaj rahi thi.
Aur vanar sena bhi.

Raat aayi.
Chand samundar mein chamak raha tha.
Lehren naach rahi thi.

Samundar gehra tha.
Bhayanak tha.
Magar Rama sthir the.

Vanar samundar ko dekh rahe the.
Darr bhi tha.
Par vishwas bhi.

Yahin se
sabse badi pariksha shuru hone wali thi…"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.5
    with st.expander("Chapter 6.5 – Rama feels sad thinking about Sita"):
        text1 = """
        Chapter 5 – Rama is afflicted when thinking of Sita (Hinglish Story Rewrite)

Samundar ke uttari kinare
vanar sena ne shivir lagaya.
Nila sena ka netritva kar rahe the.
Mainda aur Dvivida
har disha mein pahra de rahe the.

Sab kuch surakshit tha.

Rama chupchaap khade the.
Lakshmana unke paas hi the.

Tab Rama dheere se bole,
“Lakshmana, log kehte hain
samay ke saath dukh kam ho jaata hai.
Par mera dukh
har din badhta ja raha hai.”"""
        create_image_text_layout("attached_assets/chapter6/6.5.jpg", text1, layout="side", image_position="left")

        text2 = """
        Unki awaaz bhaari ho gayi.
“Main is baat ka shok nahi karta
ki Sita mujhse door hai.
Main is baat ka shok karta hoon
ki uski yuva avastha
yun hi beet rahi hogi.”

Rama ne gehri saans li.
“Hey Pawan Dev,
us jagah jao jahan Sita hai.
Use chhoo kar
mujhe bhi chhoo lena.
Mujhe thoda sa sukoon milega.”

Unki aankhen bhar aayi.
“Jab use utha kar le jaaya gaya tha,
uski pukaar
aaj bhi mere kaanon mein gunjti hai.
‘Bachao…’”

“Wahi awaaz
mere shareer ko jalati rehti hai.
Jaise zeher pee liya ho.”

Rama bole,
“Meri judai angaar hai.
Meri yaadein aag hain.
Aur mera prem
mujhe din-raat jala raha hai.”

Unhone Lakshmana se kaha,
“Tum yahin raho.
Main samundar ke paas jaakar
thoda shaant hona chahta hoon.”

“Bas itna hi kaafi hai
ki hum dono
ek hi dharti par zinda hain.”

Rama ne kaha,
“Jaise sookhi zameen
keechad se jeevan paati hai,
waise hi main
sirf is vishwas se jee raha hoon
ki Sita abhi zinda hai.”

Unki awaaz kaanp rahi thi.
“Kab main usse fir se dekh paunga?
Uske kamal jaise netra…
uska komal chehra…”

“Kab woh mujhe gale lagayegi
aur khushi ke aansu bahayegi?”

Rama ne dard se kaha,
“Main uska sahaara hoon.
Phir bhi woh rakshason ke beech
ek anath jaise jee rahi hogi.”

“Janak ki beti…
Dasharath ki bahu…
aaj akeli hogi.”

Phir Rama ne dridh swar mein kaha,
“Jab main Ravana ko haraunga,
tab Sita fir se chamkegi.
Jaise badalon ke baad
chaand nikal aata hai.”

“Par abhi…
dukh aur upvaas ne
uska shareer kamzor kar diya hoga.”

Rama ki aankhon se aansu beh gaye.
“Us din, jab main
is dukh ko tyag dunga…
us din mera mann shaant hoga.”

Rama bolte rahe.
Aur dheere-dheere
suraj doob gaya.

Shaam ho gayi.

Lakshmana ne unhe sambhalna chaha.
Par Rama ka mann
ab bhi Sita mein hi tha.

Phir bhi Rama ne
apni sandhya pooja ki.
Dukh ke saath.
Prem ke saath.

Raat ke saath
unka virah aur gehra ho gaya…"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.6
    with st.expander("Chapter 6.6 – Ravana asks advice from his people"):
        text1 = """
        Chapter 6 – Ravana apne Sabha se Salah leta hai (Hinglish Story Rewrite)

Hanuman ne Lanka mein
jo bhayankar kaam kiya tha,
usey dekh kar
Ravana ka mann hil gaya.

Ek bandar ne
poori nagri hila di thi.
Mahal tod diye.
Rakshason ko maar diya.
Aur Sita se mil kar
zinda wapas chala gaya.

Yeh sab soch kar
Ravana ne sir jhuka liya."""
        create_image_text_layout("attached_assets/chapter6/6.6.jpg", text1, layout="side", image_position="left")

        text2 = """
        Phir usne
apne sab rakshas netaon ko dekha
aur kaha,

“Lanka, jo kabhi kisi ke liye
asambhav thi,
aaj ek bandar ne
usey ujaad diya.”

“Hanuman ne
meri nagri ko
ulta-pulta kar diya.”

“Ab mujhe batao,
main kya karun?”

“Tum sab kushal ho.
Buddhimaan ho.
Mujhe sahi raasta batao.”

Ravana ne aage kaha,
“Gyaani log kehte hain
ki sahi salah
jeet ki jad hoti hai.”

“Isliye main
tum sab se
salah lena chahta hoon.”

Phir Ravana ne
teen prakaar ke logon ki baat ki.

“Is duniya mein
teen tarah ke manushya hote hain.”

“Pehla—
jo apne mitron,
buzurgon aur gyaaniyon se
salah leta hai,
aur phir poori taakat se
kaam karta hai.
Wahi sabse uttam hota hai.”

“Doosra—
jo akela hi sochta hai
aur apna kaam karta hai.
Woh madhyam hota hai.”

“Tisra—
jo bina soche samjhe kehta hai,
‘Main sab kar lunga.’
Woh sabse neecha hota hai.”

Ravana ne gambhir swar mein kaha,
“Jaise log teen prakaar ke hote hain,
waise hi salah bhi
achhi, madhyam aur buri hoti hai.”

“Jo salah
achhe vichaar ke baad,
shastra aur buddhi se
milkar di jaaye,
woh sabse achhi hoti hai.”

“Jo salah
bahut behas ke baad mile,
woh madhyam hoti hai.”

“Aur jahan sab
sirf apni-apni baat par ade rahein,
aur koi nishkarsh na nikle,
woh salah vinash laati hai.”

Isliye Ravana ne kaha,
“Ab tum sab
mujhe batao
ki kya karna chahiye.”

“Rama aa raha hai.
Hazaaron vanaron ke saath.”

“Woh samundar ko bhi
paar kar lega.
Ya usey sukha dega.
Ya koi aur upaay karega.”

“Uske saath
Lakshmana hai.
Aur poori vanar sena hai.”

Ravana ne ant mein kaha,
“Ab tum hi batao,
Lanka aur sena ko
kaise bachaya jaaye?”

Sab rakshas chup ho gaye.
Sab soch mein pad gaye.

Ab Ravana ki kismet
apni hi sabha ke haathon mein thi…"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.7
    with st.expander("Chapter 6.7 – The demons encourage Ravana"):
        text1 = """
        Ravana ki baat sun kar
sabhi balwaan rakshas
haath jod kar khade ho gaye.
Par unki buddhi
ahankaar se dhaki hui thi.

Unhone Ravana ke mann mein
dushman ke liye
tiraskar bhar diya.

Rakshas bole,
“Hey Maharaj,
aap itna chintit kyun ho?”"""
        create_image_text_layout("attached_assets/chapter6/6.7.jpg", text1, layout="side", image_position="left")

        text2 = """
        “Humare paas
bahut badi sena hai.
Gada, talwar, bhala,
teer aur shakti—
sab kuch hai.”

“Ek Rama aur kuch bandar
aapka kya bigaad lenge?”

Phir unhone Ravana ke
purane kaarnaame yaad dilaye.

“Hey Rakshason mein shreshth,
kya aapne Bhogavati par
akraman nahi kiya tha?”

“Kya aapne
Nagon ki jaati ko
yuddh mein haraaya nahi tha?”

“Mount Kailash par rehne wale
Kubera ko
aapne yuddh mein
paraajit nahi kiya tha?”

“Yakshon ke beech
aapne tabahi macha di thi.
Mahadev ka mitra hone ka
ghamand bhi
usey nahi bacha paaya.”

Rakshas bole,
“Maya Danav
aapse itna dara
ki usne apni beti
aapko de di.”

“Madhu jaise mahaan daitya ko
aapne hara diya.”

“Naglok mein jaa kar
aapne Vasuki, Takshaka
jaise shaktishaali naagon ko
saal bhar ke yuddh ke baad
juka diya.”

“Unse
maya-vidya bhi seekhi.”

Unhone aur badha-chadha kar kaha,
“Varuna ke putron ko
aapne khule maidan mein haraaya.”

“Samundar ke andheron mein jaa kar
aapne Mrityu tak ko
paraajit kiya.”

“Dharti par
Indra jaise shaktishaali
kitne hi yoddha the.
Par sab aapke saamne
tik nahi paaye.”

“Phir Rama kya cheez hai?”

Rakshas hansne lage.
“Raghava
na shakti mein
na veerta mein
aapke barabar hai.”

“Phir aap khud
kyun yuddh karein?”

“Indrajit
akela hi
poori vanar sena ko
khatm kar sakta hai.”

Unhone Indrajit ki mahima gaayi.

“Maheshwar ki pooja se laut kar
Indrajit ne
aisa vardaan paaya hai
jo is sansaar mein
durlabh hai.”

“Woh devon ke samundar tak gaya.
Unke raja ko utha laaya.
Baad mein
Brahma ke aadesh se
Indra ko chhod diya gaya.”

“Devta bhi
uski veerta ke saamne
jhuk gaye.”

Rakshas bole,
“Isliye Maharaj,
Indrajit ko bhejiye.”

“Woh Rama ko bhi marega
aur vanaron ko bhi.”

“Aap jaise mahaan raja ko
yeh sochna bhi shobha nahi deta
ki koi aapko hara sakta hai.”

“Rama ka ant
nishchit hai.”

Ravana ne yeh sab suna.
Uske hriday mein
garv aur ahankaar
aur gehra ho gaya.

Yahin se
vinash ki disha
aur spasht ho jaati hai…"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.8
    with st.expander("Chapter 6.8 – Ravana’s generals boast proudly"):
        text1 = """
        Ravana ki sabha mein
ab ghamand ki hawa chal rahi thi.

Sabse pehle
senapati Prahasta aage aaya.
Woh kaale baadal jaisa lag raha tha.
Usne haath jod kar kaha,

“Hum Dev, Danav, Gandharva,
Pisach, pakshi aur naag—
sabko yuddh mein hara sakte hain.”

“Phir yeh do manushya
aur kuch bandar
humare saamne kya hain?”"""
        create_image_text_layout("attached_assets/chapter6/6.8.jpg", text1, layout="side", image_position="left")

        text2 = """
        Uski awaaz mein gussa tha.
“Nashe aur laparwahi mein
hum Hanuman se dhokha kha gaye.”

“Par jab tak main zinda hoon,
woh bandar
Lanka mein dobara
zinda nahi ghusega.”

“Main samundar se ghiri
is poori bhoomi ko
bandaron se saaf kar dunga.”

“Bas aadesh dijiye, Maharaj!”

Phir Durmukha bola.
Uski awaaz thandi,
par zeher se bhari thi.

“Hum is apmaan ko
kabhi bardasht nahi karenge.”

“Is bandar ne
shehar ujada.
Mahal jalaaye.
Aur humare raja ka
apmaan kiya.”

“Main akela jaakar
un sab bandaron ko
maar dunga.”

“Chahe woh
samundar mein chhupe ho,
swarg mein ho
ya narak mein!”

Tab Vajradanshtra uth khada hua.
Uske haath mein
khoon se sani
badi gada thi.
Gusse mein woh garaj utha.

“Hanuman kya cheez hai?”

“Jab tak Rama, Sugriva
aur Lakshmana zinda hain,
tab tak yeh bandar
kuch bhi nahi.”

“Main aaj hi jaunga.
Aur akela hi
Rama, Sugriva aur Lakshmana ko
maar kar lautunga.”

Usne aur ek chaal batayi.
“Hazaaron rakshas hain
jo roop badal sakte hain.”

“Hum manushya ban kar
Rama ke paas jaayenge.”

“Usse kahenge,
‘Hum Bharata ki taraf se aaye hain.’”

“Rama turant
apni sena ke saath aayega.”

“Tab hum aasmaan se
pathar aur teer barsa kar
vanar sena ko
nasht kar denge.”

“Rama aur Lakshmana
bhi bach nahi paayenge.”

Phir Nikumbha,
Kumbhakarna ka putra,
gusse mein bola,

“Tum sab yahin raho.”

“Main akela hi
Rama, Lakshmana, Sugriva,
Hanuman
aur poori vanar sena ko
maar dunga.”

Aakhri mein
pahaad jaisa bada rakshas
Vajrabahu bola.
Woh gusse mein
apne hont chaat raha tha.

“Tum sab
aaram se baitho.”

“Sharaab piyo.
Mauj karo.”

“Main akela hi
poori vanar sena ko
kha jaunga.”

“Sugriva, Lakshmana,
Hanuman, Angada—
koi bhi nahi bachega.”

Sab rakshas
apni-apni shakti ka
dikhava kar rahe the.

Koi bhi
shant buddhi se
soch nahi raha tha.

Aur Ravana…
un sab baaton ko sun kar
aur bhi
ahankaar mein doob raha tha.

Yahin se
Lanka ke vinash ki
ghadi aur kareeb aa rahi thi…"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.9
    with st.expander("Chapter 6.9 – Vibhishana advises Ravana to return Sita"):
        text1 = """
        Ravana ki sabha mein
sab rakshas gusse se bhare hue the.
Unke haath mein gada, bhala, talwar,
teer-dhanush chamak rahe the.

Sab ek hi baat bol rahe the,
“Aaj hum Rama, Lakshmana, Sugriva
aur us bandar Hanuman ko
maar kar rahenge!”

Sabka khoon khol raha tha.

Tab Vibhishana aage aaye.
Unhone shant swar mein
sabko haath se roka."""
        create_image_text_layout("attached_assets/chapter6/6.9.jpg", text1, layout="side", image_position="left")

        text2 = """
        “Ruko,”
unhone kaha.

Unhone sabko baithaya
aur haath jod kar
Ravana se bole.

“Bhai,
gyani log kehte hain
ki jab teen upaayon se
lakshya na mile,
tab bal ka prayog
bahut soch-samajh kar hota hai.”

“Rama koi aam shatru nahi hai.
Woh satark hai.
Woh jeet ke liye tayaar hai.
Aur uske saath
daivik shakti hai.”

“Usne apni indriyon ko
niyantran mein rakha hai.
Aisa vyakti
aasaani se haraaya nahi ja sakta.”

Vibhishana ne aage kaha,
“Hanuman ne samundar paar kiya.
Kaun soch sakta tha
woh kaise jaayega?”

“Humare shatru ke paas
bahut saadhan hain.
Bahut sena hai.”

“Usey halki nazar se
dekhna
badi bhool hogi.”

Phir unhone seedhi baat kahi.
“Bhai,
Rama ne aapka
kya bigaada tha?”

“Janasthan mein
Khara ne pehle
seema ka ullanghan kiya.
Rama ne
apni raksha ki.”

“Ismein Rama ka
kya dosh hai?”

Vibhishana bole,
“Is poore sankat ka
ek hi kaaran hai—
Sita ka apaharan.”

“Isi wajah se
hum is musibat mein pade hain.”

“Isliye
Maithili ko
louta dena hi
sabse sahi raasta hai.”

Unki awaaz bhaari ho gayi.
“Is jhagde ko
aage badhaane ka
kya laabh?”

“Rama bina kaaran
kabhi yuddh shuru nahi karta.”

“Yeh uchit nahi
ki hum aise
dharmic aur shaktishaali
raja se yuddh karein.”

“Usse pehle ki
uske teer
Lanka ko jala daalein,
ghode, haathi
aur dhan-daulat sab nasht ho jaaye,
Sita ko wapas kar do.”

“Vanar sena aane se pehle
Maithili ko lautao.”

Vibhishana ne
ant mein vinati ki.
“Bhai,
hamare khoon ka vaasta.”

“Meri salah
tumhare hit mein hai.”

“Rama ke teer
bilkul nishchit hain.
Chamakte hue,
surya jaise tez.”

“Der mat karo.”

“Krodh chhod do.
Dharm ka maarg apnao.”

“Taaki hum
apne putron aur parivaar ke saath
shaanti se jee saken.”

“Maithili ko
Dasharath ke putra ko
louta do.”

Vibhishana chup ho gaye.

Ravana ne kuch nahi kaha.
Usne sabko
sabha se vida kar diya.

Aur akela
apne mahal ke
andar chala gaya.

Par uske mann mein
ahankaar aur krodh
abhi bhi zinda tha…"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.10
    with st.expander("Chapter 6.10 – Vibhishana strongly repeats his advice"):
        text1 = """
        Subah hui.
Naya din nikla.

Vibhishana, jo dharm aur buddhi mein sthir tha,
Ravana ke mahal mein pravesh karta hai.

Woh mahal
pahaadon jaisa vishaal tha.
Sona chamak raha tha.
Hathiyon ki garaj,
shankh aur nagadon ki awaaz
har taraf goonj rahi thi."""
        create_image_text_layout("attached_assets/chapter6/6.10.jpg", text1, layout="side", image_position="left")

        text2 = """
        Sundar striyaan
galion mein baatein kar rahi thi.
Devon ke ghar jaisa
sab kuch lag raha tha.

Vibhishana dheere se
apne bade bhai Ravana ke paas gaya.
Usne pranam kiya.
Aur Ravana ke sanket par
baith gaya.

Phir shant swar mein bola.

“Bhai Ravana,”
“jab se Sita yahan aayi hai,
ashubh sanket dikh rahe hain.”

“Yagya ki aag
theek se nahi jal rahi.”
“Dhuaan zyada hai.
Chingariyan ud rahi hain.”

“Yagya sthalon mein
saap aur keede dikh rahe hain.”

“Gaiyon ka doodh
sukh gaya hai.”
“Hathiyon ka mad
behna band ho gaya.”

“Ghode bechain hain.”
“Gadhe, bhains aur khacchar
ro rahe hain.”

Vibhishana ki awaaz bhaari ho gayi.

“Kaale kauwe
mandiron par jama ho rahe hain.”
“Giddh shehar ke upar
mandra rahe hain.”

“Shaam hote hi
siyar cheekhne lagte hain.”

“Jungle ke jaanwar
shehar ke darwazon par
ikatthe ho rahe hain.”

“Yeh sab sanket
achhe nahi hain.”

Phir Vibhishana ne
seedhi baat kahi.

“Bhai,
is sab ka ek hi upaay hai.”

“Sita ko
Rama ko lautana hoga.”

Usne haath jod liye.

“Agar meri baat se
aapko bura laga ho,
toh mujhe maaf karna.”

“Par sach yahi hai.”

“Sab log mann hi mann
yeh maante hain.”

“Par darr ke maare
koi bol nahi raha.”

“Main sirf wahi keh raha hoon
jo maine dekha
aur suna hai.”

“Ab jo theek lage,
aap wahi kijiye.”

Vibhishana chup ho gaya.
Sabha mein sannata chha gaya.

Ravana ka chehra
laal ho gaya.
Uski aankhon mein
gussa bhar aaya.

Woh zor se bola,

“Mujhe kahin bhi
koi darr nahi dikh raha!”

“Rama
kabhi Sita ko
wapas nahi le ja paayega!”

“Chahe Indra samet
sab devta
uska saath de dein,
phir bhi
woh mujhe nahi hara sakta!”

Yeh keh kar
Dashanan ne
Vibhishana ko
sabha se nikaal diya.

Vibhishana shant raha.
Uske chehre par
dukh tha.

Dharm ne phir
ahankaar ko chetaya…
par ahankaar ne
sunne se inkaar kar diya."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.11
    with st.expander("Chapter 6.11 – Ravana calls a meeting of his court"):
        text1 = """
        1️⃣ Paap aur kaam ka asar

Ravana ek adharmi raja ban chuka tha.
Woh apni kaamna (lust) ka gulam ho gaya tha.

Apne sachche mitron (jaise Bibishana) ki baat ignore kar raha tha

Sirf Sita (Vaidehi) ke khayalon mein dooba hua tha

Bina sahi wajah ke bhi yuddh chhedna chahta tha

📌 Ramayana yahan clear batati hai:

Jab raja apne vivek ko chhod deta hai, tab uski shakti dheere-dheere ghatti hai."""
        create_image_text_layout("attached_assets/chapter6/6.11.jpg", text1, layout="side", image_position="left")

        text2 = """
        2️⃣ Ravana ka shandar pravesh

Ravana apne sone ke rath par sabha ki taraf nikalta hai:

Rath sona, moti, moonga (coral) se saja hua

Ghode achhe trained

Saath mein rakshas sena –

hathi

ghode

rath

gada, talwar, bhale, dart

Pure raaste:

nagade

turahi

shankh

gaadiyon ki garaj

👉 Lanka poori hil jaati hai, jaise aakash mein pakshi bhar gaye ho.

3️⃣ Vishvakarma ki sabha

Sabha:

Vishvakarma dwara banayi gayi

Zameen shuddh sone ki

600 bhayankar rakshas raksha mein

Singhhasan panna (emerald) ka

Ravana:

hiran ke chamde par baitha

mote gaddo ke saath

poori shaan-o-shaukat ke saath

📌 Baahar se shobha, andar se andhapan.

4️⃣ Rakshason ko bulaya jata hai

Ravana hukm deta hai:

“Sab rakshason ko turant bulao!
Dushman bada vaar karne wala hai!”

Doot:

poori Lanka chhaan marte hain

ghar, sadak, garden, sab jagah

bina formalities sabko utha laate hain

Rakshas:

rath chhod dete hain

hathi, ghode chhod kar

sabha mein sher jaise gufa mein ghuste hain

5️⃣ Sabha ka mahaul

Sab apni jagah par baith jaate hain (rank ke hisaab se)

Mantri – buddhimaan

Yoddha – balshaali

Sab shant, gambhir

Bibishana bhi aata hai,
pair chhoo kar pranam karta hai.
(Par Ravana ab bhi uski baat sunne ko taiyaar nahi.)

Sabki aankhen:
👉 sirf Ravana ke chehre par tiki hui

6️⃣ Ant mein Ravana ka varnan

Ramayana ke shabd bohot gehre hain:

Ravana un yoddhaon ke beech
Indra jaisa lag raha tha,
par asal mein woh vinaash ki disha mein chal chuka tha.

🌿 Is Chapter ka Gehra Arth (Moral)

Ahankaar + Kaam = Patan

Shakti bina dharm ke sirf dikhawa hoti hai

Sach bolne wale mitra ko ignore karna, raja ke liye sabse bada paap hota hai

👉 Yeh sabha yuddh ki shuruaat ka sanket hai
👉 Aur Ravana ke ant ka bhi…"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.12
    with st.expander("Chapter 6.12 – Ravana talks with Kumbhakarna"):
        text1 = """
        Chapter 12 – Ravana aur Kumbhakarna ka Samvaad (Hinglish Moral Story Style)

Ravana ne sabha par nazar daali.
Usne Prahasta se kaha,
“City ki raksha ke liye sena ko sahi jagah lagao.”

Prahasta ne turant kaam kiya.
Shehar ke andar aur bahar sena bithai.
Phir Ravana se bola,
“Sab ready hai, ab bina chinta aage badhiye.”"""
        create_image_text_layout("attached_assets/chapter6/6.12.jpg", text1, layout="side", image_position="left")

        text2 = """
        Ravana thoda shaant hua.
Usne sabke saamne apna mann khola.

“Jo baat galat ho, ya sahi,
mujhe bataana tum sab ka farz hai.

Tum sab hamesha meri jeet ka saath dete aaye ho.
Jaise devta Indra ke peeche chalte hain,
waise hi tum mere saath ho.”

Phir Ravana ne ek gehri saans li.

“Sita…
main use Dandaka van se yahan laaya.
Par woh mujhe sweekaar nahi karti.

Woh itni sundar hai
ki meri buddhi ka control chala gaya hai.
Main kaam aur gusse ke beech phans gaya hoon.
Yahi meri sabse badi kamzori ban gayi.”

Usne aage kaha,
“Rama aur Lakshmana samundar paar kaise aayenge?
Yeh sochna mushkil hai.
Par mujhe lagta hai, jeet meri hi hogi.”

Yeh sunte hi Kumbhakarna gusse mein aa gaya.
Uski awaaz garaj uthi.

“O Ravana!
Yeh kaam tumhe shobha nahi deta.

Tumne bina salah liye
Sita ko utha liya.
Yahi galti hai.

Jo raja bina soche kaam karta hai,
use baad mein pachhtana padta hai.”

Usne seedhi baat boli.

“Galat shuruat ka ant hamesha bura hota hai.
Dushman hamesha
aisi galtiyon se hi
raasta dhoond leta hai.”

Phir bhi Kumbhakarna ne kaha,

“Par ab jab yuddh tay hai,
main peeche nahi hatunga.

Apne bade sharir aur gada ke saath
main dushman par toot padunga.
Rama, Lakshmana aur vanaron ka naash kar dunga.”

Usne ant mein bola,

“Tum nishchint raho.
Jab main jeet kar aaunga,
tab Sita tumhari hogi.”

🌿 Is Chapter ka Moral

Kaam aur ahankaar raja ko andha kar dete hain

Bina salah liya gaya faisla vinaash laata hai

Bal se zyada buddhi zaroori hoti hai

Yeh chapter dikhata hai:
Ravana ko sach dikhaya ja raha tha…
par woh dekhna hi nahi chahta tha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.13
    with st.expander("Chapter 6.13 – Ravana tells an old story"):
        text1 = """
        Chapter 13 – Ravana aur Punjikasthala ki Kahani (Hinglish Moral Story Style)

Ravana gusse mein tha.
Uska chehra laal ho gaya tha.
Yeh dekhkar Mahaparshva ne thoda socha
aur haath jod kar bola.

“Jo jungle mein jaakar
wahan ka shahad na chakkhe,
woh moorkh hota hai.

Aap hi sabke swami ho,
O Mahaveer Ravana.
Apne shatru ko kuchal kar
Vaidehi ke saath apna samay bitao.

Kumbhakarna aur Indrajit jaise yoddha
akela hi Indra se takra sakte hain.
Phir dar kis baat ka?”

Mahaparshva ne kaha,
“Is samay shakti ka upyog hi sahi raasta hai.”"""
        create_image_text_layout("attached_assets/chapter6/6.13.jpg", text1, layout="side", image_position="left")

        text2 = """
        Ravana ne uski baat suni.
Phir dheere se bola,

“Mahaparshva,
main tumhe apni ek purani kahani sunata hoon.”

Uski awaaz bhaari ho gayi.

“Bahut pehle,
jab apsara Punjikasthala
Brahma ji ki pooja ke liye ja rahi thi,
main use raste mein mila.

Us ghatna ke baad
Brahma ji ne mujhe shraap diya.

Unhone kaha,
‘Ravana,
agar aaj ke baad
tum kisi aur stri par zabardasti karoge,
toh tumhara sir tukdon mein toot jaayega.’”

Ravana ne gehri saans li.

“Isi shraap ke darr se
main Sita par zor nahi daalta.
Mera gussa samundar jaisa gehra hai,
meri shakti aandhi jaisi tez hai.

Par Rama is baat ko nahi jaanta.
Isi liye woh mujhse yuddh karne aa raha hai.”

Usne garv se kaha,

“Jo sote hue sher ko jagata hai,
woh apna ant khud bulata hai.

Jab meri teer-kamaan chalayegi,
Rama aur uski sena
aag mein ghire jungle jaise jal jaayegi.

Jaise suraj sitaron ki roshni mita deta hai,
waise hi main un sabko mita dunga.”

🌿 Is Chapter ka Moral

Shraap aur niyam bhi sabse shaktishaali ko baandh dete hain

Ahankaar insaan ko apni hi taqat par andha bana deta hai

Jo apni shakti par ghamand karta hai,
woh apni haar ko nazarandaaz karta hai

Yeh chapter dikhata hai:
Ravana sirf bahar se balwaan tha,
andar se woh darr aur ahankaar ke beech phansa hua tha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.14
    with st.expander("Chapter 6.14 – Vibhishana criticizes Ravana’s courtiers"):
        text1 = """
        Chapter 14 – Bibishana ne Ravana ke Darbar ki Soch par Sawal Uthaya

(Hinglish • short sentences • moral story tone)

Bibishana chupchaap sun raha tha.
Ravana ka ghamand.
Kumbhakarna ka garajna.

Uska mann dukhi ho gaya.
Phir usne shaant par majboot awaaz mein kaha.

“O Raja Ravana,
tum Sita ko yahan kyun laaye?

Woh ek zehreela saanp jaisi hai.
Uski chinta uska vish hai.
Uski hansi uske daant hain.
Uski paanch ungliyaan paanch phan.

Jab tak vanar sena Lanka par nahi chadhi,
abhi bhi samay hai.
Maithili ko Rama ko lauta do.”"""
        create_image_text_layout("attached_assets/chapter6/6.14.jpg", text1, layout="side", image_position="left")

        text2 = """
        Bibishana ne seedha sach bola.

“Na Kumbhakarna,
na Indrajit,
na Mahaparshva,
na Nikumbha,
koi bhi Rama ko yuddh mein hara nahi sakta.

Agar tum surya, devta
ya mrityu ke lok mein bhi chhup jao,
Rama se bach nahi paoge.”

Yeh sunkar Prahasta bol pada.

“Humein devtaon se darr nahi.
Yaksha, Gandharva, Naag – kisi se bhi nahi.
Rama toh ek insaan hai.
Usse kyun darein?”

Bibishana ka chehra aur gambhir ho gaya.
Usne kaha,

“Prahasta,
tum log sach nahi dekh rahe.

Rama koi aam insaan nahi hai.
Woh dharm, bal aur anubhav ka sangam hai.

Samundar bina naav ke paar karna
jitna mushkil hai,
utna hi namumkin hai Rama ko harana.

Tum isliye ghamand kar rahe ho
kyunki Rama ke teer
abhi tumhare shareer ko chhuye nahi hain.

Jis din woh teer chale,
saans bhi saath chhod degi.”

Bibishana ne darbar ki taraf dekha.

“Tum sab Raja ko dushman jaise behla rahe ho,
dost jaise nahi.

Sachcha mitra wahi hota hai
jo Raja ko galat raaste se kheench kar bachaye,
chahe baal pakad kar hi kyun na le aana pade.

Ravana aaj ahankaar ke samundar mein doob raha hai.
Aur Rama woh lahar hai
jo sab kuch baha le jaayegi.”

Usne fir wahi baat dohraayi.

“Maithili ko Rama ko lauta do.
Yahi rajya ka bhala hai.
Yahi Lanka ka bhala hai.
Yahi Raja ka bhala hai.”

🌿 Moral of the Chapter

Sach bolne wala hi sachcha mitra hota hai

Jhooti tarif Raja ko barbaadi ki taraf le jaati hai

Ahankaar se bada shatru koi nahi

Samay par liya gaya sahi faisla hi raksha karta hai

Bibishana ne sach bola.
Par sach sunne ke liye
dil bhi saaf hona chahiye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.15
    with st.expander("Chapter 6.15 – Vibhishana scolds Indrajit for boasting"):
        text1 = """
        Chapter 15 – Bibishana ne Indrajit ke Ghamand ko Daanta

(Hinglish • short sentences • moral story tone)

Bibishana ki baat sun kar
Indrajit ka gussa bhadak gaya.
Uska chehra laal ho gaya.
Aankhon mein ghamand chamakne laga.

Usne zor se kaha:

“O mere chhote chacha Bibishana,
yeh darr bhari baatein kya hain?

Tumhare siwa koi aisa nahi sochega.
Tumhare andar veerta nahi hai.
Na himmat.
Na sahas.

Rama aur Lakshmana kaun hain?
Sirf do insaan.

Hum mein se ek bhi
akela kaafi hai unhe mitaane ke liye.

Kya maine devtaon ke raja Indra ko nahi giraya?
Kya Airavat ko maine zameen par nahi patka?
Devta bhag gaye the mere darr se.

Phir yeh do manushya kya cheez hain?”"""
        create_image_text_layout("attached_assets/chapter6/6.15.jpg", text1, layout="side", image_position="left")

        text2 = """
        Indrajit ke shabd garaj rahe the.
Par Bibishana shaant raha.
Uski awaaz gambhir thi.
Par pyaar bhi tha.

Usne kaha:

“Beta Indrajit,
tum abhi jawaan ho.
Tumhari soch abhi pakki nahi hui.

Tum samajh nahi pa rahe
kya sahi hai aur kya galat.

Sach kahun toh,
tum anjaane mein Ravana ke shatru ban rahe ho.

Ghamand mein uska saath dekar
tum usse vinaash ki taraf dhakel rahe ho.

Tumhari baatein bachpana hain.
Tum Rama ke teeron ki taakat nahi jaante.

Woh teer sirf loha nahi hote.
Woh Brahma ka dand jaise hote hain.
Woh Yamraj ke dand jaise hote hain.

Unka saamna koi nahi kar sakta.”

Bibishana ne sabki taraf dekha.
Phir Ravana ki taraf.

Aur bola:

“Abhi bhi samay hai.
Sita ko Rama ko lauta do.

Usse samman ke saath bhejo.
Dhan, ratna, gehne ke saath.

Tabhi hum shanti se jee paayenge.
Warna yeh ghamand
sab kuch jala dega.”

🌿 Moral of the Chapter

Jawaani ka ghamand andha hota hai

Sach bolna kabhi-kabhi kadwa lagta hai, par wahi raksha karta hai

Taakat se zyada samajh zaroori hoti hai

Jo salah vinaash laaye, woh dosti nahi hoti

Bibishana ne fir sach bola.
Par sach sunna
har kisi ke bas ki baat nahi hoti."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.16
    with st.expander("Chapter 6.16 – Ravana insults Vibhishana and sends him away"):
        text1 = """
        Chapter 16 – Ravana ne Bibishana ko daanta, aur Bibishana ne Lanka chhod di

(Hinglish • short sentences • children’s moral story tone)

Bibishana ne sach bola tha.
Samajh ke saath bola tha.
Par Ravana ka mann andha ho chuka tha.

Ravana gusse se bola:

“Dushman ke saath rehna
ya zehrele saanp ke saath rehna
phir bhi theek hai.

Par aise dost ke saath rehna nahi,
jo dost bankar dushman ka saath de.

Rishta-daar sabse zyada khatarnak hote hain.
Wahi sabse pehle girane ki koshish karte hain."""
        create_image_text_layout("attached_assets/chapter6/6.16.jpg", text1, layout="side", image_position="left")

        text2 = """
        Jo power mein hota hai,
jo strong hota hai,
jo raja hota hai,
use sabse pehle apne hi jalte hain.”

Ravana aur tez bolne laga:

“Jaise haathi jaal se nahi darte,
par apne hi jaise logon se darte hain.

Waise hi
sabse bada khatra
apno se hi hota hai.

Mujhe raja banne par samman milta hai,
yeh baat tumhe hazam nahi ho rahi.

Jaise lotus ke patte par paani nahi tikta,
waise hi bure logon ke saath dosti nahi tikti.

Agar yeh baat koi aur bolta,
toh main use zinda na chhodta!

Tum par laanat hai,
apni jaati ke kalank!”

Yeh sunkar Bibishana ka dil dukha.
Par uska dimaag shaant raha.
Usne gussa nahi kiya.
Sach ka saath nahi chhoda.

Woh uth khada hua.
Haath mein gada thi.
Uske saath chaar aur rakshas the.

Bibishana ne kaha:

“Bhai,
tum galat raaste par ho.

Bada bhai pita ke samaan hota hai.
Isliye main abhi bhi tumhara samman karta hoon.

Par galat baatein
main sah nahi sakta.

Jo log sach bolte hain,
unhe sunna mushkil hota hai.

Jhooth bolne wale bohot mil jaate hain.
Par bhalaai ke liye kadwa sach bolne wale
bahut kam hote hain.

Main nahi chahta tha
ki tum maut ke phande mein phanso.

Main nahi chahta tha
ki Rama ke chamakte teer
tumhe chhed dein.

Veer log bhi
jab maut aati hai
toh ret ki deewar jaise gir jaate hain.”

Bibishana ki awaaz bhaari ho gayi.

Usne kaha:

“Main tumhe bachana chahta tha.
Lanka ko bachana chahta tha.
Rakshason ko bachana chahta tha.

Par tumhe meri baat pasand nahi aayi.

Ab main ja raha hoon.

Mere bina shayad
tum khud ko zyada khush samjho.

Yaad rakhna,
jab jeevan ka ant paas hota hai,
toh log apno ki salah nahi sunte.”

Bibishana ne aakhri baar dekha.
Phir aakash ki taraf badh gaya.
Lanka peeche chhoot gayi.
Sach ka raasta aage tha.

🌿 Moral of the Chapter

Sach bolna dosti ka sabse bada farz hota hai

Ghamand insaan ko andha bana deta hai

Jo kadwa sach bole, wahi sacha hitai hota hai

Galat raaste par chalne wale raja apna hi vinaash bulate hain

Yahin se
Bibishana ka naya safar shuru hota hai
— dharm ke saath,
sach ke saath."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.17
    with st.expander("Chapter 6.17 – The monkeys discuss Vibhishana"):
        text1 = """
        Chapter 17 – Bibishana ko lekar Vanaron ki baat

(Hinglish • short sentences • moral story tone)

Bibishana Ravana se alag ho chuka tha.
Woh seedha Rama aur Lakshmana ke paas aaya.

Door se hi
woh Mount Meru ke shikhar jaisa dikh raha tha.
Bijli ki tarah chamakta hua."""
        create_image_text_layout("attached_assets/chapter6/6.17.jpg", text1, layout="side", image_position="left")

        text2 = """
        Uske saath
chaar veer rakshas the.
Sab shastra aur kavach se sajje hue.
Heere-jawahar se chamak rahe the.

Vanaron ke neta
use dekh kar ruk gaye.

Sugriva soch mein pad gaya.
Usne Hanuman aur baaki vanaron se kaha:

“Yeh rakshas
zaroor hume maarne aa raha hai.
Shastra leke aaya hai.
Chaar aur rakshas saath hain.”

Yeh sunte hi
vanar gusse mein aa gaye.
Ped aur patthar utha liye.

Unhone kaha:

“Hukum do Maharaj!
Abhi in sabko gira dete hain.”

Tab Bibishana
uttar disha ke kinare par ruk gaya.
Shaant tha.
Bina ghamand ke bola.

Usne zor se kaha:

“Mera naam Bibishana hai.
Main Ravana ka chhota bhai hoon.

Ravana ne hi
Jatayu ko maara
aur Sita Mata ko utha kar laya.

Sita yahan bandi hai.
Majboori mein rakhi gayi hai.

Maine baar-baar Ravana ko samjhaya.
Par woh nahi maana.

Usne mujhe apmaanit kiya.
Isliye main apni patni aur bete ko chhod kar
yahan sharan lene aaya hoon.

Kripya
Raghava ko batao
ki Bibishana sharan maangne aaya hai.”

Sugriva ko gussa aa gaya.
Woh turant Rama ke paas gaya.

Usne Lakshmana ke saamne kaha:

“Yeh dhokha ho sakta hai, Prabhu!

Yeh rakshas
bhes badalne mein mahir hote hain.

Yeh Ravana ka bhai hai.
Yeh hum par achanak vaar kar sakta hai.

Dushman ki madad
kabhi nahi leni chahiye.

Ho sakta hai
Ravana ne ise bheja ho.

Main maanta hoon
ise maar dena chahiye!”

Sugriva chup ho gaya.
Sab Rama ki taraf dekhne lage.

Rama shaant rahe.
Unhone kaha:

“Tumhare raja ne
samajhdari ki baat kahi hai.

Sankat ke samay
mitron ki salah sunni chahiye.”

Vanar bole:

“Prabhu,
aap sab jaante ho.

Phir bhi
aap humse poochte ho.
Yeh aapki mahanta hai.

Sab mantri apni baat rakhein.”

Sabse pehle
Angada bole:

“Har deserter ko parakhna chahiye.
Bina jaanche bharosa theek nahi.

Agar laabh ho
toh swikaar karein.
Agar nuksaan ho
toh mana karein.”

Sharabha ne kaha:

“Pehle jaasoo bhejo.
Puri jaanch ho.”

Jambavan bole:

“Dushman ke ghar se aaya hai.
Savdhaan rehna chahiye.”

Mainda ne kaha:

“Dheere-dheere prashn poochho.
Uske mann ko samjho.
Phir faisla lo.”

Akhir mein
Hanuman bole.
Unki awaaz shaant thi.
Par baat gehri thi.

“Prabhu,
Bibishana ka chehra saaf hai.
Uski boli mein kapat nahi.

Achanak jaasoo bhejna
use shanka mein daal dega.

Insaan ka sach
waqt ke saath samne aata hai.

Bibishana
Ravana ki burai jaanta hai.
Aur aapki dharma-pravritti bhi.

Isliye
usne yeh raasta chuna.

Mujhe is par vishwas hai.
Par antim faisla
aapka hi hona chahiye.”

Sab chup ho gaye.
Hawa bhi jaise ruk gayi.

Ab faisla
Rama ke haath mein tha 🌿"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.18
    with st.expander("Chapter 6.18 – Rama listens to the monkeys’ advice"):
        text1 = """
        Chapter 18 – Rama ne Bibishana ko sharan dene ka faisla kiya

(Hinglish • short sentences • simple • moral story tone)

Hanuman ki baat sun kar
Rama shaant hue.
Unhone sabki taraf dekha
aur bole:

“Maine bhi socha hai Bibishana ke baare mein.
Jo vyakti
dost ban kar mere paas aaye,
main use kabhi mana nahi karta.

Agar galti bhi ho jaaye,
toh bhi
koi sachcha insaan
mujhe dosh nahi de sakta.”"""
        create_image_text_layout("attached_assets/chapter6/6.18.jpg", text1, layout="side", image_position="left")

        text2 = """
        Sugriva ne phir kaha.
Woh dhyaan se bole:

“Prabhu,
jo apne bhai ko musibat mein chhod de,
woh baad mein kisko nahi chhodega?
Aise vyakti par bharosa kaise karein?”

Rama halki muskaan ke saath
Lakshmana ki taraf mude.
Unhone kaha:

“Sugriva ne jo kaha,
woh bina soch ke nahi kaha.

Par rajaon ka dharm alag hota hai.
Raja ke do dushman hote hain—
uske rishtedaar
aur uske padosi.

Isliye
Bibishana yahan aaya hai.

Sab bhai Bharata jaise nahi hote.
Aur sab dost bhi ek jaise nahi hote.”

Phir Rama ne dharm ki baat kahi:

“Shastra kehte hain—
jo sharan maange,
use thukrana paap hai.

Hum rakshason ke raja nahi hain.
Bibishana humse rajya nahi maang raha.

Uska aana
Ravana ke rajya mein phoot daalega.
Yahi uska asli kaaran hai.”

Sugriva phir bhi chinta mein tha.
Usne kaha:

“Prabhu,
mujhe lagta hai
Ravana ne ise bheja hai.
Yeh dhokha ho sakta hai.”

Rama gambhir hue.
Unhone kaha:

“Sugriva,
chahe woh buri niyat se aaye,
mujhe koi nuksaan nahi pahuncha sakta.

Rakshas, danav, yaksha—
sabko main chaahe
ungli ke siray se mita sakta hoon.”

Phir Rama ne ek kahani sunayi:

“Ek kabootar ne
apne dushman ko bhi sharan di.
Usne apna maans tak arpan kar diya.

Agar ek pakshi
itna bada dharm nibha sakta hai,
toh main kyun nahi?”

Rama ne spasht shabd bole:

“Jo haath jod kar sharan maange,
chahe woh dushman hi kyun na ho,
use maarna maha paap hai.

Jo dar ke maare
ya gusse mein
sharan dene se inkaar karta hai,
woh apna punya kho deta hai.”

Phir Rama ne pratigya li:

“Jo bhi mere paas aakar kahe—
‘Main tumhara hoon’,
use main raksha doonga.

Chahe woh Bibishana ho
ya khud Ravana.”

Yeh sun kar
Sugriva ka mann badal gaya.
Usne sir jhuka kar kaha:

“Prabhu,
aap dharm ke shikhar ho.

Ab mujhe bhi
Bibishana par vishwas hai.

Use turant
apne beech le aaiye.”

Usi pal
Rama ne Bibishana ko apnaya.
Jaise devraj
apne saathi ko apnata hai.

✨ Yahin se dharm ki jeet shuru hoti hai."""
        create_image_text_layout(text_content=text2, layout="full")
    # Chapter 6.19
    with st.expander("Chapter 6.19 – Vibhishana is brought before Rama"):
        text1 = """
        Chapter 19 – Bibishana ko Rama ke saamne laya gaya

(Hinglish • short • simple • children’s moral story tone)

Rama ne jab
Bibishana ko sharan di,
toh Bibishana ne
sir jhuka liya.
Uski aankhen zameen par thi.

Phir woh khushi se
aakash se neeche utra.
Apne chaar saathiyon ke saath
daudta hua Rama ke paas aaya.

Bibishana ne
Rama ke charanon mein gir kar kaha:"""
        create_image_text_layout("attached_assets/chapter6/6.19.jpg", text1, layout="side", image_position="left")

        text2 = """
        “Main Ravana ka chhota bhai hoon.
Usne mera apmaan kiya.
Isliye main aapki sharan aaya hoon.

Main Lanka chhod aaya.
Dost, dhan, sab chhod diya.
Ab meri zindagi,
mera rajya,
meri khushi —
sab aapke hawale hai.”

Rama ne
shaant aur gahri nazar se
Bibishana ko dekha.
Phir dheere se bole:

“Bibishana,
mujhe sach batao.
Rakshason ki taakat kya hai?
Aur unki kamzori kya hai?”

Bibishana ne
imaandari se sab bataya:

“Ravana ko ek vardaan mila hai.
Dev, nag, gandharva
use hara nahi sakte.

Mera bada bhai
Kumbhakarna bahut balwaan hai.

Prahasta uski sena ka neta hai.
Indrajit yuddh mein
adrishya ho jaata hai.

Lanka mein
bahut saare rakshas hain.
Sab roop badal sakte hain.
Ravana ne devtaon ko bhi haraya hai.”

Rama ne
dhyaan se suna.
Phir vishwas ke saath bole:

“Yeh sab mujhe pehle se pata hai.
Main Ravana ko avashya maarunga.
Uske saare sahayak bhi girenge.

Uske baad
tumhe Lanka ka raja banaunga.
Yeh mera vachan hai.

Chahe Ravana
pataal mein chhup jaaye,
ya kisi dev ke paas bhag jaaye,
woh bachega nahi.

Jab tak Ravana aur uske vansh ka
ant nahi hota,
main Ayodhya nahi jaunga.
Main apne bhaiyon ki kasam khata hoon.”

Bibishana ne
phir sir jhuka diya.
Uski aankhon mein aas thi.

Usne kaha:

“Main poori taakat se
aapki madad karunga.
Yuddh mein
rakshason ki pankti tod dunga.”

Rama ne
use gale laga liya.
Phir Lakshmana se bole:

“Samundar ka jal lao.
Bibishana ka
raja ke roop mein abhishek karo.”

Lakshmana ne
Rama ki baat maani.
Sab vanar neta
wahaan maujood the.

Jaise hi Bibishana
raja bana,
sab vanar bol uthe:

“Bahut achha!
Bahut achha!”

Phir Hanuman aur Sugriva ne poocha:

“Hum itni badi vanar sena ke saath
samundar kaise paar karein?
Kya upaay hai?”

Bibishana ne shaant swar mein kaha:

“Rama ko
samundar ke devta se
prarthna karni chahiye.
Woh apni hi vansh ka hai.
Woh avashya madad karega.”

Sugriva aur Lakshmana
yeh sandesh Rama ke paas le gaye.
Rama ko yeh yojana pasand aayi.

Rama muskuraye aur bole:

“Bibishana ka vichaar uchit hai.
Tum dono bhi socho
aur jo sahi lage, batao.”

Sugriva aur Lakshmana bole:

“Is yojana ke bina
Lanka pahunchna mushkil hai.
Samundar par pul banana zaroori hai.
Chalo, samundar ke paas chalte hain.”

Tab Rama
kusha ghaas se bhare
samundar ke kinare ki taraf chale.

✨ Yahin se
samundar par pul banne ki kahani shuru hoti hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.20
    with st.expander("Chapter 6.20 – Ravana sends Shuka to Sugriva"):
        text1 = """
        Chapter 20 – Ravana ne Shuka ko Sugriva ke paas bheja

(Hinglish • short • simple • children’s moral story tone)

Ek rakshas tha,
naam Shardula.
Woh Ravana ka jaasoos tha.

Shardula ne dekha ki
Sugriva ki sena
samundar ke kinare camp mein hai.
Vanar aur bhaloo
samundar jaise anant lag rahe the."""
        create_image_text_layout("attached_assets/chapter6/6.20.jpg", text1, layout="side", image_position="left")

        text2 = """
        Woh turant Lanka lauta
aur Ravana se bola:

“Hey Maharaj,
vanaron aur bhaluon ki
bahut badi sena aa chuki hai.

Rama aur Lakshmana
samundar ke kinare pahunch gaye hain.
Yeh sena har disha mein
bahut door tak phaili hai.

Ab turant sochna hoga.
Ya toh baat-cheet,
ya samjhauta,
ya phir phoot daalni hogi.”

Shardula ki baat sunkar
Ravana chintit ho gaya.
Usne turant
apne chalaak doot Shuka ko bulaya.

Ravana bola:

“Tum Sugriva ke paas jao.
Meethi aur chalaak baaton se kaho:

‘Tum bahut shaktishaali ho.
Tum mere bhai jaise ho.
Agar main Sita ko le aaya
toh tumhe kya lena-dena?

Tum Kishkindha wapas jao.
Lanka ko koi nahi jeet sakta.
Na dev, na gandharva,
na manushya, na vanar.’”

Shuka aakash mein uda
aur Sugriva ke camp ke upar jaakar
yeh sandesh bolne laga.

Lekin jaise hi
vanaron ne use dekha,
woh gusse mein aa gaye.

Kuch vanar uchhle,
kuch mukke maare.
Sab milkar
Shuka ko peetne lage.

Shuka chillaya:

“Hey Rama!
Doot ko maarna paap hai.
Main sirf sandesh laaya hoon.
Mujhe mat maaro!”

Rama ne turant kaha:

“Isse mat maaro.”

Vanar ruk gaye.
Shuka ne sambhal kar
phir se baat shuru ki:

“O Sugriva,
main Ravana ka sandesh bolun?”

Sugriva gusse mein bola:

“Tum mere mitra nahi ho.
Tum Rama ke dushman ho.

Ravana ko jaakar keh do,
jaise Bali gira tha
waise hi woh bhi girega.

Main apni sena ke saath
Lanka ko gher lunga
aur raakh bana dunga.

Ravana kahin bhi chhup jaaye,
use Rama se koi nahi bacha sakta.”

Tab Angada aage aaya
aur bola:

“Yeh doot nahi,
yeh jaasoos hai.
Isse pakad lo.
Lanka wapas na jaane do.”

Sugriva ke ishare par
vanaron ne Shuka ko pakad liya.
Use baandh diya.
Woh dard mein chillane laga.

Shuka roya:

“Meri pankh nochi ja rahi hain!
Meri aankhen nikaali ja rahi hain!
Hey Rama, mujhe bacha lo!”

Rama ne uski awaaz suni.
Unka hriday daya se bhar gaya.

Rama bole:

“Isse chhod do.”

Vanaron ne Shuka ko chhod diya.
Uski jaan bach gayi.

✨ Seekh (Moral):
Sacha yoddha
dushman ke saath bhi
dharma nahi chhodta.
Rama ne dikhaya
ki daya aur niyam
shakti se bhi bade hote hain."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.21
    with st.expander("Chapter 6.21 – Rama becomes angry at the sea god"):
        text1 = """
🌊 Scene ka Arth (Context)

Yeh adhyay Yuddha-kāṇḍa ka ek bahut mahatvapūrṇ mod hai.
Yahin se Setu-Bandhan (Ram Setu) ki ghatnaon ka adhar banta hai.

🧘‍♂️ 1. Rama ka Tapasya-bhav

Rama
Rama samudra ke kinare Darbha aur Kusha ghaas bichha kar:

Purab ki or mukh karke

Hath jod kar

Samudra Dev Sagara ko naman karte hain

Woh 3 din aur 3 raat shant, niyamit aur maryada ke saath lete rehte hain.

👉 Arth:
Rama pehle vinamrata aur dharma ka marg apnate hain.
Bal hone ke baad bhi pehle anurodh (request) karte hain, na ki bal-prayog."""
        create_image_text_layout("attached_assets/chapter6/6.21.jpg", text1, layout="side", image_position="left")

        text2 = """
        😶 2. Samudra ka Maun (Silence)

Teen raat beet jaati hain,
par Sagara prakat nahi hota.

Yahin Rama ko spasht ho jaata hai:

“Jo log sirf vinamrata ko kamzori samajhte hain,
unke saath kathorata avashyak hoti hai.”

👉 Yeh Rajniti + Dharma ka gyaan hai
— sirf daya se har samasya nahi sulajhti.

🔥 3. Rama ka Krodh (Controlled Anger)

Rama ka roop badal jaata hai:

Aankhen laal

Dhanush kas kar pakda

Teer zehrile saanp jaise

Woh kehte hain:

“Agar samudra rasta nahi dega,
toh main ise sukha dunga!”

Aur Rama teer chhod dete hain.

🌊 Samudra mein:

Lehren pahadon jaisi uthti hain

Magar-machh, saanp, daanav bhay se bhagte hain

Pura sagar kaanp uthta hai

👉 Yeh darshata hai:
Rama ka krodh andha nahi,
balki niyantrit aur dharmic hai.

✋ 4. Lakshmana ka Hastakshep

Lakshmana
Lakshmana turant aage badhte hain aur Rama ka dhanush pakad kar kehte hain:

“Aapke jaise mahavir ko krodh se kaam nahi lena chahiye.
Aapka uddeshya bina vinaash ke bhi poora ho sakta hai.”

Isi pal Devarshi aur Brahmarshi bhi akash se bolte hain:

“Ruko! Ruko!”

👉 Seekh:
Mahaan vyakti ke paas
krodh ka niyantran aur vivek dono hone chahiye.

🌉 Is Adhyay ka Gehra Sandesh

Dharma pehle, Shakti baad mein

Daya ko kamzori samajhne walon ke liye kathorata zaruri

Sahi samay par sahi maryada

Rama yahan sirf yoddha nahi, Maryada-Purushottam dikhte hain"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.22
    with st.expander("Chapter 6.22 – The army crosses the sea"):
        text1 = """
        🌊 Rama aur Samudra ka Samvaad

Rama samudra ke kinare khade the.
Unki awaaz gambhir thi, aankhon mein tej.

Rama bole,
“Aaj agar samudra raasta nahi dega,
toh mere teer usse jhukne par majboor kar denge.”

Unhone apna Brahma-dand jaise teer dhanush par chadhaaya.
Aasman kaanp utha.
Pahad hil gaye.
Nadi, jheel, taare – sab dar gaye.

Par Rama peeche nahi hate.
Woh sirf apna kartavya yaad kar rahe the."""
        create_image_text_layout("attached_assets/chapter6/6.22.jpg", text1, layout="side", image_position="left")

        text2 = """
        🌊 Samudra Dev ka Prakat Hona

Tab Samudra Dev Sagara khud lehron se nikle.
Hari-emerald jaise rang ke, motiyon se sajje hue.
Ganga aur Sindhu nadiyaan unke saath thi.

Samudra ne haath jod kar kaha,
“O Raghava, main apni prakriti ke viruddh paani ko jam nahi sakta.
Par main tumhari madad zaroor karunga.
Vanar sena ko main dharti jaise sambhaal lunga.”

Rama shant hue, par bole,
“Mera teer vyarth nahi ja sakta.
Batao, ise kahan chhodun?”

Samudra ne uttar diya,
“Uttar mein Drumakulya naam ki jagah hai.
Wahan paapi log mere jal ko ganda karte hain.
Wahin teer chhod do.”

Rama ne teer chhoda.
Wahan Maru Registan bana.
Par Rama ne use vardaan diya –
“Yeh bhoomi upjaau aur sugandhit hogi.”

👉 Seekh:
Sachchi shakti vinaash ke baad bhi kalyaan karti hai.

🌉 Ram Setu ka Nirmaan

Samudra ne phir kaha,
“Nal, Vishvakarma ke putra, setu bana sakte hain.”

Nala aage aaye aur bole,
“Mujhe apni kala ka ghamand nahi,
par main yeh kaam kar sakta hoon.
Sab vanar milkar setu banayenge.”

Fir kya tha!

🌳 Vanar:

Bade-bade ped

🪨 Pahadon jaise patthar

🌺 Phoolon se bhare vriksh
sab samudra mein laane lage.

Har din setu aage badhta gaya:

1st din – 14 yojan

2nd din – 20 yojan

3rd din – 21 yojan

4th din – 22 yojan

5th din – 23 yojan

Aur ban gaya Ram Setu –
chamkta hua, majboot, sundar.

👉 Seekh:
Jab sab milkar kaam karein,
toh samudra bhi raasta de deta hai.

🐒 Vanar Sena ka Paar Utarna

Kuch vanar:

Setu par chale

Kuch paani mein kud gaye

Kuch aakash mein uchhal gaye

Har taraf utsah aur shor tha.

Hanuman aur Angada
Rama aur Lakshmana ko kandhon par le gaye.

Akhirkaar poori sena Lanka ke kinare pahunch gayi.

🌟 Devon ka Aashirvaad

Aasman se Dev, Rishi, Gandharva sab dekh rahe the.
Unhone gupt roop se Rama ka abhishek kiya aur kaha,

“Tum vijayi ho,
tum manushyon mein bhi Dev ho.”

🌼 Is Adhyay ki Badi Seekh

Vinamrata pehle, kathorata baad mein

Shakti ka matlab vinaash nahi, maryada hai

Teamwork se asambhav bhi sambhav ho jaata hai

Rama yahan sirf yoddha nahi, nay aur dharm ke rakshak hain"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.23
    with st.expander("Chapter 6.23 – Rama sees good and bad signs"):
        text1 = """
        Rama ne aas-paas dekha.
Unki aankhen gambhir ho gayi.
Unhone apne chhote bhai Lakshmana ko gale lagaya.

Rama bole,
“Lakshmana, mujhe bhayanak sanket dikh rahe hain.
Aaj ka din bahut bada badlaav laane wala hai.”"""
        create_image_text_layout("attached_assets/chapter6/6.23.jpg", text1, layout="side", image_position="left")

        text2 = """
        🌪️ Ashubh Sanket (Bad Omens)

Rama ne dhyaan se sab bataya:

Tez aandhi aur dhool ka toofan uth raha tha

Dharti kaanp rahi thi, pahad hil rahe the

Ped gir rahe the

Baadal bhayanak jaanwaron jaise garaj rahe the

Khoon jaise rang ki baarish gir rahi thi

Suraj se aag ka gola girta dikh raha tha

Shaam ka aasmaan laal chandan jaisa darawna lag raha tha

Raat mein:

Chand kaala-laal ghera liye hua tha

Suraj feeka aur tamra rang ka lag raha tha

Taare dhool mein chhup gaye

Kauwe, giddh, aur garud ghoom-ghoom kar gir rahe the

Gidder daraavne swar mein ro rahe the

Rama bole,
“Yeh sab yeh batata hai ki bhayanak yuddh aane wala hai.
Bahut saare veer gir sakte hain.”

👉 Seekh:
Samajhdaar vyakti sanketon ko pehchaan leta hai
aur bina dare apna kartavya nibhata hai.

⚔️ Yuddh ka Nirdhar

Rama ne kaha,
“Ab deri nahi.
Aaj hi hum Lanka par chadhai karenge.
Sena ko tukdiyon mein baant do.”

Apna dhanush aur baan uthakar
Rama Lanka ki disha mein badh gaye.

🐒 Vanar Sena ka Utsaah

Sugriva aur
Vibhishana
sena ke aage the.

Saare vanar zor-zor se chilla uthe,
“Ravana ka vinash ho!”

Unka shor, unka josh,
Rama ko bahut prasann kar gaya.

👉 Seekh:
Jab neta dharm par chalta hai,
toh sena apne aap uske saath khadi ho jaati hai.

🌼 Is Adhyay ki Saral Seekh

Sanket humein taiyaar rehna sikhate hain

Sacha veer dar ke baavjood aage badhta hai

Ekjut sena har kathinai ka samna kar sakti hai

Rama sirf yoddha nahi, buddhimaan margdarshak bhi hain"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.24
    with st.expander("Chapter 6.24 – Shuka tells Ravana how monkeys treated him"):
        text1 = """
        Rama ki sena bilkul chamak rahi thi.
Jaise poornima ki raat mein chaand chamakta hai.
Itni badi sena ke kadmon se dharti bhi kaanp rahi thi.

🔔 Lanka mein Shor

Lanka ke jungle ke paas
dhol, nagade aur gongs zor-zor se bajne lage.
Unki awaaz itni tez thi ki
vanaron ke rongte khade ho gaye.

Vanar bahut khush ho gaye.
Unhone aur bhi zor se jaykaar lagayi.
Unki garaj bijli aur baadal jaisi thi.
Yeh awaaz Rakshason tak pahunch gayi."""
        create_image_text_layout("attached_assets/chapter6/6.24.jpg", text1, layout="side", image_position="left")

        text2 = """
        🌸 Rama ko Sita yaad aayi

Rama ne Lanka ko dekha.
Rang-birange jhande, sundar mahal.
Par unka mann udaas ho gaya.

Unhone socha,
“Yahin meri Sita bandi hai.
Bilkul Rohini jaise, jo grah ke kabze mein hoti hai.”

Rama ne gehri saans li
aur Lakshmana se bole:

“Dekho Lakshmana,
yeh shehar Vishvakarma ka banaya hua hai.
Pahadon par basa,
jaise aasmaan ko chhoo raha ho.

Bagiche phoolon se bhare hain,
panchhi ga rahe hain,
madhumakkhiyan ghoom rahi hain.
Lanka bahar se sundar hai,
par andar se adharmi.”

👉 Seekh:
Sirf bahari khoobsurti par bharosa mat karo.

⚔️ Sena ka Vibhajan

Rama ne sena ko sahi jagah baanta:

Angada aur Nila – beech mein

Rishabha – daahine paksh

Gandhamadana – baayein paksh

Rama khud aage, saath mein Lakshmana

Peechhe suraksha mein Sugriva

Vanar bole,
“Hum pahadon se Lanka tod denge,
ya phir nangi haathon se!”

🕊️ Shuka ko Chhodna

Rama ne kaha,
“Shuka ko chhod do.”

Shuka
dara hua Lanka bhaag gaya.

😡 Ravana ka Gussa

Ravana ne Shuka ko dekha.
Uske pankh tute hue the.

Ravana bola,
“Yeh kya haal bana liya?
Bandar ne maar diya kya?”

Shuka ne darr ke saath kaha:
“Prabhu, jaise hi main gaya,
vanaron ne mujhe peet diya.
Baat karne ka mauka hi nahi mila.

Rama samundar par pul bana kar aa gaya hai.
Vanar aur bhaaloo pahadon jaise hain.
Ab sirf do raaste bache hain:
ya toh Sita ko lautao,
ya yuddh ka saamna karo.”

🔥 Ravana ka Ahankaar

Ravana gusse se bola:

“Main Sita kabhi nahi dunga!
Chahe devta bhi aa jaayein.
Rama ne meri taqat abhi dekhi hi nahi.
Mere baan zehrele saanpon jaise hain!”

👉 Seekh:
Ahankaar aadmi ko andha kar deta hai.
Sach sun kar bhi jo na maane,
uska patan pakka hota hai.

🌼 Is Adhyay ki Saral Seekh

Ahankaar sabse bada shatru hai

Sach bolne wala kabhi kamzor nahi hota

Dharma ke saath khadi sena kabhi nahi hara karti"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.25
    with st.expander("Chapter 6.25 – Ravana sends spies Shuka and Sarana"):
        text1 = """
        Rama
samundar paar kar chuke the.
Vanaron ki sena Lanka ke saamne khadi thi.

Yeh dekh kar Ravana
thoda chauk gaya.
Usne kabhi socha bhi nahi tha
ki samundar par pul ban sakta hai.

😠 Ravana ka Aadesh

Ravana ne apne do mantriyon ko bulaya —
Shuka aur
Sarana.

Ravana bola:"""
        create_image_text_layout("attached_assets/chapter6/6.25.jpg", text1, layout="side", image_position="left")

        text2 = """
        “Bandar ban kar jao.
Unki sena ke beech ghuso.
Gino unke neta.
Samjho unki taakat.
Aur mujhe sab sach batao.”

🐒 Bheed jo ginne mein na aaye

Shuka aur Sarana
vanar ka roop le kar ghus gaye.

Par jaise-jaise aage badhe,
unke hosh udd gaye.

Vanar samundar jaise anant the.
Kuch aa rahe the.
Kuch pul par the.
Kuch pehle hi pahunch chuke the.

Garaj, shor, himmat —
sab kuch bhayankar tha.

👀 Bibishana ne pehchaan liya

Bibishana
sab dekh raha tha.

Usne turant pehchaan liya
ki yeh dono Rakshasa spy hain.

Unhe pakad kar
Rama ke paas le aaya.

🙏 Rama ka Dharam

Shuka aur Sarana dar gaye.
Haath jod kar bole:

“Prabhu,
humein Ravana ne bheja hai.
Hum sirf dekhne aaye the.”

Rama muskuraye.
Aur shaant swar mein bole:

“Tumne jo dekhna tha dekh liya?
Agar kuch reh gaya ho,
Bibishana tumhe dikha dega.

Tum doot ho.
Aur doot ko maara nahi jaata.”

👉 Yahin Rama ka dharma chamka.

🕊️ Sandesh Ravana ke liye

Rama ne kaha:

“Lanka jao.
Aur Ravana se kehna —

‘Kal subah
mere baan Lanka ki deewaron par girenge.
Jo sena tumne Sita ko harne mein use ki,
use taiyaar rakhna.’”

Shuka aur Sarana ne naman kiya:
“Aap vijayi hon!”

😨 Lanka laut kar sach

Lanka pahunch kar
unhone Ravana se kaha:

“Prabhu,
Rama ne humein zinda chhod diya.
Unki sena atoot hai.

Rama, Lakshmana, Sugriva
aur Bibishana —
yeh chaar hi Lanka ko gira sakte hain.

Vanar sirf madad hain.
Asli taakat Rama ka dharma hai.

Ab bhi waqt hai.
Sita ko lauta do.”

🌼 Is Adhyay ki Seedhi Seekh

Dharma mein daya hoti hai

Ahankaar sach ko nahi dekh pata

Jo sharan mein aaye, uski raksha karna hi raj dharma hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.26
    with st.expander("Chapter 6.26 – Sarana describes the monkey leaders"):
        text1 = """
        Sarana
ne himmat ke saath sach bola.
Par yeh sach
Ravana
ko bilkul pasand nahi aaya.

Ravana gusse mein bola:

“Chahe Devta, Gandharva aur Asura
sab milkar mujh par chadh aayein,
main Sita ko kabhi nahi lautaunga!
Tum bandar se pit kar dar gaye ho,
isliye mujhe kamzor samajh rahe ho.”

Uska ahankaar aur bhi badh gaya."""
        create_image_text_layout("attached_assets/chapter6/6.26.jpg", text1, layout="side", image_position="left")

        text2 = """
        🏰 Ravana Lanka ke mahal par chadha

Ravana apne safed, unche mahal par chadh gaya.
Wahan se usne
pahaad, jungle aur samundar
sab par nazar daali.

Aur jo usne dekha,
uska ghamand hil gaya.

👉 Har jagah vanar hi vanar the.
Jaise dharti khud chal kar aa gayi ho.

Ravana ne poocha:

“Kaun hain yeh neta?
Kaun inki sena chala raha hai?
Kaun mere saamne garaj raha hai?”

🐒 Sarana ne ek-ek neta ka naam bataya

Sarana bola:

🔊 Nila

“Jo Lanka ke saamne garaj raha hai,
jiski awaaz se shehar kaanp raha hai —
woh Nila hai.
Sugriva ka senapati.”

🦁 Angada

“Jo pair patak raha hai,
poori dharti ko hila raha hai —
woh Angada hai.

Yeh Bali ka beta hai.
Sugriva ka vaaris.
Aur Rama ka sabse wafadar.

Isi ki salah se
Hanuman ne Sita ko dhoonda.”

🌉 Nala

“Angada ke paas jo khada hai,
pul banane wala —
woh Nala hai.”

⚔️ Shveta

“Safaid rang ka veer,
tez aur nidar —
uska naam Shveta hai.
Yeh sena ko sajane ja raha hai.”

🌄 Kumuda aur Kanda

“Pahaadon se aaye hue
Kumuda aur Kanda —
dono keh rahe hain
ki Lanka ko mita denge.”

🦁 Rambha

“Jo sher jaisa dikh raha hai,
teen sau koti vanar jiske saath hain —
woh Rambha hai.”

🔥 Sharabha

“Jo kabhi peeche nahi hatta,
aankhon se aag barsata hai —
uska naam Sharabha hai.
Uske paas chaar lakh vanar hain.”

☁️ Panasa

“Jo badal jaisa lagta hai,
jiski garaj door tak jaati hai —
woh Panasa hai.
Uske saath pachaas lakh neta hain.”

🐒 Vinata, Krathana aur Gavaya

Vinata – tez aur bhaari sena ke saath

Krathana – yuddh ke liye lalkaar raha hai

Gavaya – laal rang ka balwaan vanar,
jiske saath 70 lakh yoddha hain

😨 Sarana ka antim sach

Sarana ne ant mein kaha:

“Raja,
yeh sab neta ginne se bahar hain.
Har ek apni sena ka malik hai.
Yeh sirf vanar nahi…
toofan hain.”

🌼 Is Adhyay ki Seedhi Seekh

Ahankaar sach dekhne nahi deta

Sach batane wala hamesha nirbhay hota hai

Jab anyaay badhta hai, to ek nahi, poori sena uth khadi hoti hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.27
    with st.expander("Chapter 6.27 – Sarana continues his report"):
        text1 = """
        Sarana
ne Ravana se kaha:

“Raja, main aapko un sab veeron ke baare mein bata raha hoon
jo Rama ke liye
apni jaan bhi chhod dene ko tayyar hain.”

🐒 Hara – Aag jaisi poonch wala vanar

“Jo vanar aage badh raha hai,
jiski poonch ke baal laal, peele, kaale aur safed hain,
aur jo sooraj ki roshni jaisi chamak raha hai —
uska naam Hara hai.

Uske peeche hazaaron vanar hain,
haath mein ped aur pathar uthaye.
Sab Lanka par hamle ka intezaar kar rahe hain.”"""
        create_image_text_layout("attached_assets/chapter6/6.27.jpg", text1, layout="side", image_position="left")

        text2 = """
        🐻 Bhalu Sena – Pahaadon jaisi taakat

“Jo kaale baadal jaisi lag rahi sena hai,
jo pahaadon, maidano aur nadiyon ko dhak chuki hai —
yeh bhalu yoddha hain.

Unka raja Dhumra hai.
Aur uske saath uska chhota bhai —
Jambavan.”

Sarana bola:

“Jambavan pahaad jaisa hai.
Budhiman hai, shant hai,
par yuddh mein kabhi nahi rukta.

Devta aur Asuron ke yuddh mein
usne Devtaon ki madad ki thi.
Use kai vardaan mile hain.”

⚔️ Rambha – Gusse aur shanti dono ka malik

“Jo kabhi zor se uchhalta hai,
aur kabhi bilkul shaant khada rehta hai —
uska naam Rambha hai.

Vanar usi ko dekh kar
apna hausla badhate hain.”

🐵 Samnadana – Vanaron ka purkh

“Jo chaar pairon par chalta hai,
jiska seena ek kos uncha hai,
jo shandar aur balwaan hai —
woh Samnadana hai.

Yeh vanaron ka purvaj hai.
Kabhi Indra se bhi yuddh kar chuka hai
aur haar nahi maana.”

🌳 Krathana – Haar na maan-ne wala neta

“Jambhu vriksh ke neeche jo baitha hai,
jahan Kinnera rehte hain —
uska naam Krathana hai.

Hazaaron vanar uske saath hain.
Woh bhi kehta hai:
‘Lanka toot kar rahegi!’”

🌊 Pramathin – Garajne wala yoddha

“Jo Ganga ke paas rehta hai,
haathi tak jisse darte hain —
uska naam Pramathin hai.

Uske saath
hazaaron, lakhon vanar hain.
Unki garaj se dharti kaanp jaati hai.”

🐒 Gavaksha aur Golangula sena

“Jo kaale muh wale vanar hain,
jinhone pul banaya tha —
woh Gavaksha ke netritva mein hain.

Yeh khud Lanka ko tod dena chahte hain.”

🏔️ Kesharin aur Sone jaise pahaad

“Jis sunehre pahaad par
har mausam mein phal lagte hain,
jahan shuddh shahad milta hai —
wahan Kesharin rehta hai.

Woh bhi yuddh ke liye taiyaar hai.”

☀️ Shatabali – Sooraj ki taraf dekhne wala veer

“Jo hamesha sooraj ki taraf mukh karta hai,
jiska naam poore sansaar mein mashhoor hai —
woh Shatabali hai.

Woh shapath leta hai:
‘Main Lanka ko mita dunga.’
Rama ke liye woh apni jaan bhi de dega.”

😨 Sarana ka antim sandesh

Sarana ne ant mein kaha:

“Raja,
Gaja, Gavaksha, Gavaya, Nala, Nila —
har ek ke paas das-das koti yoddha hain.

Inki ginti mumkin nahi.
Sab pahaadon jaise bade,
aur dharti ko ulat dene ki taakat rakhte hain.”

🌼 Is Adhyay ki Seedhi Seekh

Jab sach chhupaaya jaata hai, tab khatra badhta hai

Ekta aur dharm ke saath aayi sena ko koi rok nahi sakta

Ahankaar aankhon par parda daal deta hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.28
    with st.expander("Chapter 6.28 – Shuka also lists the enemy warriors"):
        text1 = """
        Sarana ke bolne ke baad,
ab Shuka aage aaya.
Usne Ravana se kaha:

🐘 Haathi jaise vanar

“Raja, kya aap dekh rahe ho?
Jo vanar haathi jaise dikhte hain,
jinke sharir se shakti tapak rahi hai.

Yeh Ganga ke kinare ke bargad jaise khade hain,
aur Himalaya ke saal vriksh jaise majboot hain.

Yeh apna roop badal sakte hain.
Daityon aur Danavon jaise balwaan hain.
Inki sankhya 21 million se bhi zyada hai.

Yeh sab Sugriva ke saathi hain,
aur Kishkindha inka ghar hai.”"""
        create_image_text_layout("attached_assets/chapter6/6.28.jpg", text1, layout="side", image_position="left")

        text2 = """
        ⚔️ Mainda aur Dvivida

“Wahan do vanar saath khade hain.
Bilkul devta jaise lagte hain.

Unke naam Mainda aur Dvivida hain.
Yudh mein unka koi muqabla nahi.

Brahma ke vardaan se
unhone amrit piya hai.
Woh kehte hain —
‘Hum akela hi Lanka gira denge.’”

🌬️ Hanuman – Vayu ka putra

“Raja, jo vanar wahan khada hai,
haathi jaisa balwaan aur gusse se bhara —
wahi hai Hanuman.

Yahi Lanka aaya tha Sita ko dhoondhne.
Yahi samundar paar karke gaya tha.

Uske pita Kesari hain
aur maa-pita ka vardaan hai Vayu ka bal.

Bachpan mein usne sooraj ko phal samajh kar
pakadne ki koshish ki thi.
Gir gaya, jabda toot gaya,
isi liye uska naam Hanuman pada.

Usne pehle hi Lanka jala di thi,
kya aap bhool gaye, Raja?”

🏹 Rama – Dharm ka yoddha

“Ab us yoddha ko dekhiye,
jo kaale rang ka hai,
kamal jaise netron wala.

Woh Rama hai.

Veda ka gyaan rakhta hai.
Brahma-astra chalana jaanta hai.
Uske teer aakash ko cheer dete hain.

Uska gussa Mrityu jaisa hai
aur veerta Indra ke samaan.

Usi ki patni Sita ko
aap Janasthana se utha laaye.”

🛡️ Lakshmana – Bhai ka pran

“Rama ke daahine jo khada hai,
sone jaisa chamakta hua —
woh Lakshmana hai.

Har shastra mein nipun.
Bhai ke liye jaan dene ko tayyar.

Usne shapath li hai —
‘Main saare rakshason ka ant kar dunga.’”

👑 Bibishana – Lanka ka naya raja

“Rama ke baayein taraf jo khada hai,
rakshason ke saath —
woh Bibishana hai.

Isi ko Rama ne
Lanka ka raja bana diya hai.

Woh gusse mein hai
aur aapse yuddh ke liye badh raha hai.”

🐒 Sugriva – Vanaron ka samrat

“Beech mein jo pahaad ki tarah khada hai,
jiski shakti naapna mushkil hai —
woh Sugriva hai.

Uske gale mein sone ki mala hai,
jisme Lakshmi ka vaas hai.

Bali ke marne ke baad
Rama ne use yeh rajya diya.”

🔢 Sena ki an-ginti sankhya

Shuka ne aakhri baat kahi:

“Raja, inki ginti karna namumkin hai.
Koti, shanku, maha-vrinda, padma, samudra —
yeh sab sena uske saath hai.

Yeh sena aag ke gole jaisi hai.
Agar yuddh hua, to bhayankar hoga.

Isliye, Raja,
ya to yeh yuddh jeeto —
ya haar se bachne ka upaay socho.”

🌼 Is Adhyay ki Seekh

Sach bataane wale dushman se bhi seekh milti hai

Bal se bada hota hai dharm aur ekta

Ahankaar sach ko sunna band kar deta hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.29
    with st.expander("Chapter 6.29 – Ravana sends more spies"):
        text1 = """
        Ravana ne jab
vanaron ke sabse bade yoddha dekhe,
toh uska dil hil gaya.

Usne dekha —
Rama ke saath Lakshmana,
bilkul right side mein khada.
Paas hi Bibishana,
jo ab Rama ke saath tha.

Aage Sugriva, vanaron ka raja.
Uske paas Angada, Hanuman, Jambavan,
aur bahut se veer vanar khade the.

Yeh sab dekhkar
Ravana ka gussa phoot pada 😠"""
        create_image_text_layout("attached_assets/chapter6/6.29.jpg", text1, layout="side", image_position="left")

        text2 = """
        🔥 Ravana ka gussa

Ravana ne Shuka aur Sarana ko daant diya.

“Tum kaise mere saamne
dushman ki tareef kar sakte ho?”
Ravana garja.

“Tumne shastron se kuch seekha hi nahi.
Aise sevak hona hi mere liye sharm ki baat hai.

Agar tumhare purane kaam yaad na hote,
toh main tumhe zinda hi nahi chhodta!”

Ravana ne unhe bhaga diya.
“Jaao!
Tum mere liye mar chuke ho!”

Shuka aur Sarana chup-chaap
sir jhuka kar nikal gaye.

🕵️ Naye jasus ka hukum

Phir Ravana ne Mahodara se kaha,
“Turant naye jasus bulao!”

Kuch hi der mein
naye rakshas jasus aa gaye.
Woh himmati the.
Aur chalak bhi.

Ravana bola:

“Jaakar pata lagao —
Rama kya soch raha hai.
Uske saath kaun rehta hai.
Woh kab sota hai, kab jaagta hai.
Aur agla kadam kya hoga.”

Ravana ne kaha,
“Jo raja dushman ko jaanta hai,
usey zyada zor lagana nahi padta.”

Jasus khush ho gaye.
Unhone “Jai ho!” kaha
aur nikal pade.

👀 Pakde gaye jasus

Jasus bhes badal kar
Suvela parvat ke paas pahuche.

Wahan Rama, Lakshmana,
Sugriva aur Bibishana the.
Aur saath mein badi vanar sena.

Yeh dekhkar
jasus kaanp gaye 😨

Bibishana ne turant pehchan liya.
Usne kaha,
“Yeh jasus hain!”

Ek jasus Shardula ko pakad liya gaya.

Vanar use maarne lage.
Par Rama ne daya dikhayi.

Rama bola,
“Isse chhod do.”

Shardula bhi bach gaya.

😵 Haare hue jasus

Maar kha kar,
darr ke maare,
jasus Lanka wapas bhaage.

Ravana ke paas jaakar bole:

“Raja,
Rama ki sena
Suvela parvat ke paas camp kiye hue hai.”

Yeh sunkar
Ravana aur bhi chintit ho gaya.

🌱 Is Adhyay ki Seekh

Gussa sach sunne nahi deta

Jasus bhi tab fail hote hain jab saamne dharm khada ho

Daya, shakti se bhi badi hoti hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.30
    with st.expander("Chapter 6.30 – Shardula reports back to Ravana"):
        text1 = """
        Lanka ke jasus aakar bole,
“Rama apni badi sena ke saath
Suvela Parvat ke paas camp kiye hue hai.”

Yeh sunkar
Ravana ka mann ghabra gaya.

Usne Shardula ko dekha.
Shardula ka chehra dara hua tha.

Ravana bola,
“Tum aise kyun kaanp rahe ho?
Kya vanaron ne tumhe hara diya?”"""
        create_image_text_layout("attached_assets/chapter6/6.30.jpg", text1, layout="side", image_position="left")

        text2 = """
        😨 Shardula ka darr

Shardula dheemi awaaz mein bola:

“O Raja,
un vanaron par nazar rakhna namumkin hai.
Har taraf pahad jaise vanar khade hain.

Jaise hi main andar gaya,
mujhe pakad liya gaya.
Mujhe ghusa, laat, daant sab mila.

Mujhe poori sena mein ghumaya gaya.
Khoon se bhara hua,
main Rama ke saamne laya gaya.

Vanar mujhe maarna chahte the.
Par Rama ne kaha —
‘Ruko!’

Usi daya ne meri jaan bachayi.”

Shardula ne aage kaha:

“Rama wohi hai
jisne patharon se samundar bhar diya.
Woh Lanka ke bilkul gate par hai.
Uski sena Garuda jaisi vyavastha mein khadi hai.

Ab der mat karo, Raja.
Ya toh Sita ko wapas karo,
ya yuddh ke liye taiyaar ho jao.”

🔥 Ravana ka ghamand

Ravana thoda socha.
Phir garaj kar bola:

“Chahe devta, gandharva, daanav
sab mere khilaaf aa jaayein,
main Sita wapas nahi dunga!”

Phir usne poocha:
“Un vanaron mein kaun-kaun hai?
Kitni shakti hai unmein?
Sach batao!”

🐒 Vanar sena ka varnan

Shardula ne kaha:

“Raja,
unmein kai aise yoddha hain
jo devtaon ke putra hain.

Hanuman, pavan putra

Angada, Indra ka pota

Nala, Vishvakarma ka putra

Mainda aur Dvivida, amar shakti wale

Nila, sena ka mahan neta

Sugriva, vanaron ka raja

Hazaron nahi,
lakhon-kotiyon vanar hain.

Aur unke beech
Rama khud khade hain.

Wahi Rama
jisne Khara, Dushana,
Viradha, Kabandha jaise
bhayanak rakshason ko maara.

Aur saath mein
Lakshmana,
jo bijli jaisi teer chala sakta hai.

Aakhri baat, Raja —
aapke bhai Bibishana bhi
Rama ke saath khade hain.
Rama ne unhe Lanka ka bhavishya raja bana diya hai.”

Shardula chup ho gaya.
Usne kaha,
“Ab faisla aapka hai.”

🌱 Is Adhyay ki Seekh

Ghamand sach ko dekhne nahi deta

Daya shatru ko bhi jeet leti hai

Jab adharm badhta hai, to dharm sena ban jaata hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.31
    with st.expander("Chapter 6.31 – Ravana lies to Sita about Rama’s death"):
        text1 = """
        Lanka mein khabar phail chuki thi.
Rama apni badi sena ke saath Suvela Parvat par aa chuke the.

Yeh sun kar Ravana thoda ghabra gaya, par uska mann bahut chalak tha.
Usne socha—
👉 “Agar main Sita ka mann tod doon, to jeet meri hogi.”

🧙‍♂️ Jhooth ka Jaadu

Ravana ne apne ek jaadugar rakshas ko bulaya.
Usse kaha,
“Jaadu se Rama ka kata hua sir aur unka dhanush bana do.”

Jaadugar ne turant maya (illusion) bana diya."""
        create_image_text_layout("attached_assets/chapter6/6.31.jpg", text1, layout="side", image_position="left")

        text2 = """
        🌳 Ashok Vatika ka Dard

Ravana Ashok Vatika mein gaya.
Wahan Sita zameen par baithi thi,
sir jhuka hua,
aankhon mein aansu,
sirf Rama ka naam dil mein.

Ravana ne mithhe par zehrele shabd bole:

“Jis Rama par tumne bharosa kiya tha,
woh ab zinda nahi raha.
Meri sena ne unhe raat mein maar diya.”

💔 Jhoothi Kahani

Ravana bolta gaya—
“Lakshmana gir gaye,
Sugriva mara gaya,
Hanuman bhi nahi bache,
saari vanar sena khatam ho gayi.”

Phir usne kaha,
“Yeh dekho… Rama ka sir aur unka dhanush.”

Jaadugar ne woh jhootha sir Sita ke saamne gira diya.

😢 Sita ka Vishwas

Sita ne jaise hi dekha,
unka shareer kaanp gaya.
Aankhon se aansu behne lage.
Dil mein dard uth gaya.

Par…
unke mann mein ek awaaz thi—

👉 “Mera Rama aise nahi mar sakta.”

🌸 Sita ki Shakti

Sita ne Rama ke charitra aur shakti ko yaad kiya.
Unka dhairya bana raha.

Unhone Ravana ki taraf dekha—
na gussa,
na darr,
sirf shaant vishwas.

📖 Is Kahani ki Seekh

Sach kabhi jhooth se nahi haar ta

Prem aur vishwas sabse badi shakti hote hain

Dharm par tikka insaan kabhi toot-ta nahi"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.32
    with st.expander("Chapter 6.32 – Sita feels hopeless and sad"):
        text1 = """
        Sita ne jab woh sir aur dhanush dekha,
unka dil toot gaya.
Unki aankhon ko laga—
“Yeh mere Rama hi hain.”

Unka shareer kaanpne laga.
Dil mein dard umad aaya.
Aur woh zor se boli—

😢 Sita ka Vilap

“Khush ho jao, Kaikeyi!
Tumhari wajah se aaj Rama nahi rahe.
Jinhone kabhi kisi ka bura nahi kiya,
unhe van bhej diya gaya.”

Yeh kehte-kehte
Sita zameen par gir padi,
jaise ped jadh se kat gaya ho।"""
        create_image_text_layout("attached_assets/chapter6/6.32.jpg", text1, layout="side", image_position="left")

        text2 = """
        💔 Toota Hua Mann

Thodi der baad jab unhe hosh aaya,
woh us jhoothe sir ke paas gayi
aur roti hui boli—

“Rama…
tumne mujhe bachane ka wada kiya tha.
Aur aaj main akeli reh gayi.”

Unhone socha—
👉 “Patni ke liye pati ka marna sabse bada dukh hota hai.”

🌧️ Yaadon ka Bojh

Sita ko yaad aaya—

Rama ka pyaar

unka saath

unka wada

Unhone kaha,
“Tumhare bina
meri zindagi andheri ho gayi.”

🔥 Apne Aap Ko Doshi Samajhna

Sita ne apne aap se kaha—
“Shayad meri wajah se
Rama is musibat mein pade.”

Unka mann shok aur guilt se bhar gaya.

🙏 Antim Prarthana

Sita ne Ravana se kaha—
“Ravana,
agar Rama sach mein nahi rahe,
to mujhe bhi unke paas jaane do.”

Unki awaaz kamzor thi,
par dard bahut gehra tha.

🌀 Sach Ka Pehlu

Jab Ravana wahan se chala gaya,
jaadu ka sir aur dhanush gaayab ho gaye.

Yeh sab sirf ek dhokha tha.
Par Sita ka dukh bilkul sachcha tha.

📖 Is Kahani ki Seekh

Jhooth sach jaisa lag sakta hai,
par zyada der tak nahi tikta

Prem aur vishwas insaan ko sabse gehre dukh mein bhi zinda rakhta hai

Sita ka dhairya dukh mein bhi kamzor nahi pada"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.33
    with st.expander("Chapter 6.33 – Sarama comforts Sita"):
        text1 = """
        Is adhyay mein andhera chhantna shuru hota hai.
Jahan pichhle chapter mein Sita poori tarah toot chuki thi,
yahin se aasha ki pehli kiran aati hai — Sarama ke roop mein.

🌸 Sarama ka Parichay

Sarama ek Rakshasi hai,
lekin uska hriday shuddh aur karunamay hai.
Woh Ravana ki jaasoos nahi,
balki Sita ki chup-chaap rakshak ban chuki thi.

Jab Sita Rama ka sir samajhkar behosh ho chuki thi,
Sarama sab dekh aur sun rahi thi."""
        create_image_text_layout("attached_assets/chapter6/6.33.jpg", text1, layout="side", image_position="left")

        text2 = """
        💬 Sarama ka Satya-vachan

Sarama Sita se kehti hai:

“Jo kuch Ravana ne kaha,
sab jhooth aur maya tha.”

Aur phir woh tark ke saath sach batati hai:

Rama jaise veer ko
neend mein maara jaana asambhav hai

Rama rajneeti, yuddh aur atma-vidya ke gyata hain

Lakshmana jaise rakshak ke saath
unhe koi dhokhe se nahi maar sakta

Vanaron ki sena ko ek raat mein mita dena namumkin hai

👉 Yeh sab Ravana ka jaadu aur manasik yudh tha

🔥 Ravana ka Darr

Sarama batati hai ki:

Ravana ko jaasooson se khabar mil chuki hai

Rama samudra paar karke Lanka ke paas pahunch chuke hain

Isi darr mein Ravana sabha bula kar
poori sena ko yudh ke liye tayyar kar raha hai

Yani —

Jo jhooth bol raha tha, wahi andar se kaanp raha hai

🥁 Yudh ke Sanket

Sita khud sunti hai:

Nagadon ki awaaz

Ghode, haathi, rath taiyaar

Rakshason ka shor

Sarama kehti hai:

“Yeh awaaz vijay ki nahi,
vinaash ki pehchan hoti hai.”

🌕 Bhavishya ka Darshan

Sarama Sita ko bhavishya dikhaati hai:

Rama Ravana ka vinash karenge

Sita ko baahon mein bhar lenge

Unke lambe samay se bandhe hue baal kholenge
(jo shok ka prateek the)

Aankhon se dukh ke aansu nahi, khushi ke aansu girenge

📖 Is Adhyay ki Gehri Seekh

Sach ka saath kabhi bhi kahin se aa sakta hai
– shatru ke ghar se bhi

Sab rakshas bure nahi hote, jaise sab insaan achhe nahi hote

Jhooth zyada zor se chillata hai,
par sach shant rehta hai

Dhairya (Patience) hi Sita ka sabse bada shastra hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.34
    with st.expander("Chapter 6.34 – Sarama secretly watches Ravana’s plans"):
        text1 = """
        Sita abhi-abhi gehre dukh se bahar aayi thi.
Sarama ke shabdon ne uske mann par
baarish ki tarah shanti barsa di thi.

Par Sarama yahin nahi ruki.
Usne socha —

“Agar main Sita ki sachchi mitra hoon,
toh sirf dilasa kaafi nahi.”

🌸 Sarama ka Sankalp

Sarama muskurate hue kehti hai:

“Main aakash mein bina sahare ud sakti hoon.
Na hawa (Pavan) aur na hi Garuda
mujhe pakad sakte hain.”"""
        create_image_text_layout("attached_assets/chapter6/6.34.jpg", text1, layout="side", image_position="left")

        text2 = """
        Woh Sita se kehti hai:

“Agar tum chaho,
main Ravana ke plans jaanch kar
chup-chaap wapas aa sakti hoon.”

💔 Sita ka Dar aur Aasha

Sita dheere se bolti hai:

Ravana mujhe roz daraata hai

Ashoka Vatika mein main bandi hoon

Rakshasiyon ke beech meri saans ghutti hai

Aur phir Sita kehti hai:

“Bas itna jaan lo,
sabha mein mere baare mein kya faisla hua.”

👉 Yeh ek bandi ki nahi,
ek dhairya se bhari rani ki awaaz thi

🕵️‍♀️ Sarama ka Gupt Mission

Sarama turant Ravana ki sabha mein jaati hai.
Chhupkar sunti hai.
Aur jo woh sunti hai, woh sach hota hai — kathor sach.

⚖️ Sabha ka Sach

Sarama wapas aakar Sita ko batati hai:

Ravana ki maa ne bhi kaha:

“Sita ko izzat ke saath wapas bhej do.”

Ek buzurg mantri ne bhi samjhaya:

“Samudra paar karna,
Hanuman ka aana,
yeh sab aam baat nahi.”

Par Ravana…

ziddi hai

ahankari hai

lalchi hai

Sarama ke shabd saaf hote hain:

“Ravana tumhe tab tak nahi chhodega
jab tak woh yudh mein maara na jaye.”

🔥 Ant ka Sanket

Sarama kehti hai:

“Darr Ravana ko nahi hila sakta.
Sirf Rama ke baan hi
uska ghamand tod sakte hain.”

Aur sach mein —

Vanar sena ke nagade bajte hain

Zameen kaanp uthti hai

Lanka ke rakshason ka mann toot jata hai

Unhe pehli baar lagta hai:

“Hamara raja galat tha.”

📖 Is Adhyay ki Seekh

Sach bolne wale shatru ke ghar mein bhi mil sakte hain

Ahankaar kabhi samjhauta nahi karta,
sirf vinaash karta hai

Dhairya aur gyaan milkar hi raksha karte hain

Jab sena ka shor badhta hai,
toh adharma ka ant paas hota hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.35
    with st.expander("Chapter 6.35 – Malyavan advises Ravana to make peace"):
        text1 = """
        Nagade baj rahe the.
Narsinghe ghoonj rahe the.
Aur Rama apni sena ke saath
Lanka ke kareeb pahunch chuke the.

Yeh awaaz sun kar
Ravana thoda rukta hai.
Phir gusse mein bolta hai:

“Main Rama ko jaanta hoon.
Uski taakat ki baatein bhi suni hain.
Par tum sab ab chup kyun ho?”"""
        create_image_text_layout("attached_assets/chapter6/6.35.jpg", text1, layout="side", image_position="left")

        text2 = """
        🧠 Malyavan ka Gyaan

Tab Ravana ke naana,
buddhiman Malyavan aage aate hain.

Woh shaant swar mein kehte hain:

“Raj dharma yeh kehta hai —
samay dekh kar faisla lo.”

Unke shabd gehre hote hain, par seedhe:

Jo raja sahi waqt pe shanti aur yudh ka chunav jaanta hai

Wahi lamba raj karta hai

Shaktishaali shatru ko kabhi halka nahi lena chahiye

⚖️ Seedhi Salah

Malyavan saaf kehte hain:

“Rama se shanti karo.
Sita ko wapas de do.
Yahi is yudh ka mool karan hai.”

Woh bolte hain:

Devta Rama ke paksh mein hain

Rishi uski vijay chahte hain

Yeh yudh jeet ke liye nahi,
vinaash ke liye hai

🌪️ Burai ka Phal

Malyavan Ravana ko yaad dilate hain:

“Jab adharma badhta hai,
toh shakti dusron ke paas chali jaati hai.”

Woh kehte hain:

Tumne ghamand chuna

Tumne dharma chhoda

Isi liye shatru mazboot ho gaye

🔮 Apashagun ke Sanket

Malyavan Lanka ke darawne sanket batate hain:

Aasmaan se khoon jaisi baarish

Janwar ro rahe hain

Pakshi maut ka sandesh de rahe hain

Sapno mein bhayankar aakritiyan

Prakriti bhi Lanka ke viruddh hai

Woh kehte hain:

“Yeh sab vinaash ke lakshan hain.”

🕊️ Antim Chetavni

Malyavan gambhir hokar bolte hain:

“Rama koi sadharan manushya nahi.
Woh Vishnu ke samaan shakti rakhta hai.
Samudra par pul banana
kisi aam vyakti ka kaam nahi.”

Aur phir antim shabd:

“Ravana,
apne bhale ke liye
Rama se shanti kar lo.”

📖 Is Adhyay ki Seekh

Budhape ka gyaan anmol hota hai

Ghamand sach sunne nahi deta

Adharma ka phal vinaash hota hai

Shanti kamzori nahi,
buddhi ka pramaan hoti hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.36
    with st.expander("Chapter 6.36 – Ravana strengthens Lanka’s defenses"):
        text1 = """
        Malyavan ki baat
Ravana ko bilkul pasand nahi aayi.

Uski aankhen gusse se laal ho gayi.
Bhale shabd bhi use kaante jaise lage.

Woh garaj kar bola:

“Maine tumhari baat nahi suni.
Kaise tum Rama jaise ek aadmi ko
mere barabar samajh sakte ho?”

😡 Ghamand Bhara Uttar

Ravana aur tez awaaz mein bola:

“Rama kaun hai?
Vanar uske saath hain.
Baap ne use vanvaas de diya.
Aur tum mujhe —
Devtaon ka bhay —
uske barabar rakhte ho?”

Uska ghamand bol raha tha:

“Devta bhi mujhse ladne se darte hain.
Main kisi ke aage jhukne ke liye paida hi nahi hua.”"""
        create_image_text_layout("attached_assets/chapter6/6.36.jpg", text1, layout="side", image_position="left")

        text2 = """
        ⚔️ Yudh ka Sankalp

Ravana ne saaf kaha:

“Sita ko wapas dena?
Kabhi nahi!”

“Chahe Rama ne samudra par pul bana liya ho,
is mein kaunsa chamatkar hai?”

“Main shapath leta hoon —
Rama yahan se zinda wapas nahi jayega.”

Malyavan chup ho gaye.
Budhhi haar gayi,
ghamand jeet gaya.

🏰 Lanka ki Raksha Yojna

Ab Ravana ne Lanka ki suraksha ka plan banaya.

Usne sheher ke har gate par
apne sabse taakatvar yoddha khade kar diye:

Poorv Dwaar (East Gate): Prahasta

Dakshin Dwaar (South Gate): Mahaparshva aur Mahodara

Paschim Dwaar (West Gate):
apna beta Indrajit

Uttar Dwaar (North Gate): Shuka aur Sarana

Sheher ka beech: Veer Virupaksha

Ravana ne kaha:

“Main khud bhi morcha sambhalunga!”

🌪️ Bhagya ka Khel

Sab taiyari ho gayi.
Lanka band ho chuki thi.
Yudh tay tha.

Ravana ne socha —
“Ab koi kami nahi.”

Par kahani yahi sikhati hai:

Jab ghamand buddhi se bada ho jaye,
toh suraksha ke beech bhi
vinaash ka rasta khul jaata hai.

📖 Is Adhyay ki Seekh

Achhi salah ko thukrana
aksar vinaash laata hai

Ghamand aankhon par parda daal deta hai

Sirf shakti par bharosa
buddhi ke bina adhoora hota hai

Raksha ki deewar
ahankaar se toot jaati hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.37
    with st.expander("Chapter 6.37 – Rama plans the attack"):
        text1 = """
        Lanka ke samne, Mount Suvela par,
sabse bade yoddha ek jagah ikattha hue.

Is sabha mein the:

Rama

Sugriva

Hanuman

Jambavan

Vibhishana

Angada, Lakshmana, Nala, Nila, Mainda, Dvivida aur anya vanar veer

Sabke saamne Lanka thi—
mazboot, gheri hui,
devtaon ke liye bhi kathin.

Sabne kaha:

“Yeh Lanka Ravana dwara surakshit hai.
Bina yojna ke yudh vinaash laayega.
Aao pehle soch-vichaar karein.”"""
        create_image_text_layout("attached_assets/chapter6/6.37.jpg", text1, layout="side", image_position="left")

        text2 = """
        🦅 Vibhishana ki Gupt Jaankari

Tab Vibhishana, Ravana ke chhote bhai, bole —
shant, sachche aur nirbhik.

Unhone kaha:

“Hamare guptchar panchi ke roop mein
Lanka ke andar gaye the.
Mujhe poori raksha-vyavastha pata hai.”

Lanka ke Dwaar aur Rakshak

Poorv Dwaar: Prahasta

Dakshin Dwaar: Mahaparshva aur Mahodara

Paschim Dwaar:
Indrajit (hazaron yoddha)

Uttar Dwaar: Ravana khud

Sheher ka madhya: Virupaksha

“Lakhon sena,
10,000 haathi,
20,000 ghode,
aur anant paidal yoddha.”

Vibhishana ne yeh bhi kaha:

“Yeh bhay dikhane ke liye nahi,
aapka krodh jagane ke liye hai.
Aap devtaon ke samaan veer hain,
Rama!”

⚔️ Rama ki Yudh-Yojna

Tab Rama bole —
shaant, spasht aur nishchit.

Hamla Vibhaag

Poorv Dwaar:
Nila, Prahasta ka samna karega

Dakshin Dwaar:
Angada, Mahaparshva aur Mahodara se ladega

Paschim Dwaar:
Hanuman apni sena ke saath sheher mein ghusega

Uttar Dwaar:
Rama aur Lakshmana khud Ravana ka samna karenge

Kendra:
Sugriva, Jambavan aur Vibhishana sambhalenge

Rama ne saaf kaha:

“Ravana ka vadh
sirf main karunga.”

🐒 Vanar Sena ki Pehchaan

Rama ne ek mahatvapurn niyam bataya:

“Yudh ke dauran
vanar apna roop nahi badlenge.
Yahi hamari pehchaan hogi.”

Sirf 7 yoddha
manav roop mein ladenge:

Rama

Lakshmana

Vibhishana

aur uske 4 saathi

🌄 Yudh se Pehle ka Sankalp

Rama ne Mount Suvela par hi
apna mukhya sthaan chuna.

Fir—

Vanar sena ke saath,
utsah aur dhairya se bhare hue,
Rama Lanka ki taraf badhe.

Yudh nishchit tha.
Dharma tay tha.
Aur Ravana ka ant bhi.

📖 Is Adhyay ki Seekh

Yudh se pehle yojna
shakti se zyada zaroori hoti hai

Sach bolne wala shatru ka bhai
bhi mitra ban sakta hai

Achha neta har yoddha ko
uski sahi jagah deta hai

Ahankaar sena badha sakta hai,
par buddhi hi vijay dilati hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.38
    with st.expander("Chapter 6.38 – The army climbs Mount Suvela"):
        text1 = """
        Yeh tay karne ke baad ki
raat Mount Suvela par bitayi jaayegi,
Rama
apne saath Lakshmana,
Sugriva
aur dharmic Vibhishana
se madhur aur shant swar mein bole.

Rama ne kaha:

“Aao hum Mount Suvela par chadhein.
Yeh pahaadon ka raja hai.
Yahan se hum Lanka ko saaf dekh paayenge.”

Phir Rama ne gambhir swar mein kaha:

“Ravana ne meri Sita ko utha kar
apna hi vinaash bula liya hai.
Usse na dharma ki chinta hai,
na nyay ki,
na apne vansh ke maan ki.”"""
        create_image_text_layout("attached_assets/chapter6/6.38.jpg", text1, layout="side", image_position="left")

        text2 = """
        ⛰️ Pahaad ki Chadhai

Yeh kehkar Rama
Mount Suvela ki sundar dhalaanon ki taraf badhe.

Unke peeche:

Lakshmana, dhanush-baan ke saath, satark

Sugriva, apne mantriyon ke saath

Vibhishana, poore vishwas ke saath

Vanar sena to
hava ki gati se uchhalti-koodti
har disha se pahaad chadhne lagi.

Zyada samay nahi laga
aur sab shikhar par pahunch gaye.

🏯 Lanka ka Darshan

Upar se unhone dekha:

Lanka, jo hawa mein latakti hui si lag rahi thi

Bade-bade dwaar

Mazboot deewarein

Har jagah rakshas yoddha

Deewaron par khade
kaale rakshas
aise lag rahe the
jaise ek aur zinda deewar ho.

Yeh dekhkar
vanar sena ka josh aur badh gaya.
Sabke muh se yudh ke naare goonjne lage.

🌙 Raat ka Shant Pal

Ab suraj
laal rang mein doob raha tha.
Shaam ka ujala phail gaya.

Thodi der mein
poorn chandrama ke saath
shaant raat aa gayi.

Tab Rama ne:

Vibhishana ka abhinandan kiya

Vanar netaon ke saath
Mount Suvela par
apna sthaan banaya

Wahan sab
raat ke liye vishram karne lage.

📖 Is Adhyay ki Seekh

Yudh se pehle sthiti ko samajhna
buddhimaani hoti hai

Gussa nahi, drishti aur dhairya
achhe neta ki pehchaan hai

Uchchai par jaakar hi
badi tasveer saaf dikhti hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.39
    with st.expander("Chapter 6.39 – Lanka is described in detail"):
        text1 = """
        Mount Suvela par raat bitane ke baad,
subah hote hi
veer vanar sena ne
Lanka ki taraf dekha.

Jo unhone dekha,
woh adbhut tha.
Sab hairaan reh gaye."""
        create_image_text_layout("attached_assets/chapter6/6.39.jpg", text1, layout="side", image_position="left")

        text2 = """
        🌳 Lanka ke Van aur Bagiche

Lanka ke jungle
bahut bade aur sundar the.
Har taraf hariyali thi.

Champak, Ashok, Bakul,
Sala, Tala jaise ped the.
Kahi laal, kahi peele phool.
Har jagah sugandh phaili hui thi.

Belon ne pedon ko
gehne jaise saja diya tha.
Phool aur phal se bhare ped
aise lag rahe the
jaise raja saj-dhaj kar khade ho.

Halki thandi hawa chal rahi thi.
Us hawa mein phoolon ki khushboo thi.
Pakshi madhur swar mein gaa rahe the.

Yeh sab dekh kar
vanar sena ko
Lanka aur bhi vishesh lagne lagi.

🐒 Vanaron ka Aage Badhna

Kuch vanar neta
Rama ki anumati lekar
aage badhe.

Unke zor se garajhne par
pakshi ud gaye.
Hiran aur hathi
idhar-udhar bhaagne lage.

Unke kadmon se
dharti kaanp uthi.
Dhool badalon ki tarah
udne lagi.

⛰️ Trikuta Parvat

Lanka
Trikuta Mountain
par basi hui thi.

Yeh parvat
itna uncha tha
jaise aakash ko chhoo raha ho.

Sone ki tarah chamakta,
bahut vishaal,
aur chadhne mein asambhav.

Is parvat par basi Lanka
aur bhi shaktishaali lag rahi thi.

🏯 Sone-si Chamakti Lanka

Lanka shehar:

Bahut chaudi aur lambi

Bade-bade safed dwar

Sone aur chandi ki deewarein

Mahal aur mandir
shehar ko sajate the.
Har taraf vaibhav hi vaibhav tha.

Ek mahal
hazaar khambon wala tha.
Woh itna uncha tha
jaise Kailash parvat ho.

Yahi
Ravana ka nivas tha.

Shehar mein:

Bagiche

Chaurahen

Pakshiyon ki awaaz

Har taraf samriddhi

Sab kuch swarg jaisa lag raha tha.

👑 Rama ka Manan

Yeh sab dekhkar
Rama
chup ho gaye.

Unki aankhon mein
aashcharya tha.
Par mann shaant tha.

Lakshmana ke bade bhai
samajh gaye the:

“Yeh shehar sundar hai,
par anyay se bhara hua hai.”

Rama apni badi sena ke saath
us majboot nagar ko dekhte rahe.
Unke mann mein
sirf ek sankalp tha —
nyay ki sthapna.

📖 Is Adhyay ki Seekh

Bahari sundarta
andar ke sach ko nahi chhupa sakti

Vaibhav bina dharma ke
sirf bhram hota hai

Sachcha yoddha
sirf shakti nahi,
nyay ke liye ladta hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.40
    with st.expander("Chapter 6.40 – Sugriva and Ravana fight fiercely"):
        text1 = """
        Mount Suvela ke shikhar par
Rama
apni vanar sena ke saath khade the.

Unki nazar seedhi
Lanka par padi.

👑 Lanka ke Dwaar par Ravana

Lanka ke ek bade gate par
Ravana
akela khada tha.

Safed chamars hil rahe the.
Chhatra uske sir ke upar tha.

Laal chandan se lipta sharir.
Sone ke gehne.
Kapde sone ke taar se bune hue.

Uska shareer
shaam ke badalon jaisa lag raha tha.

Par us seene par
purane yuddhon ke ghaav bhi the."""
        create_image_text_layout("attached_assets/chapter6/6.40.jpg", text1, layout="side", image_position="left")

        text2 = """
        🐒 Sugriva ka Achanak Hamla

Yeh dekh kar
Sugriva
ka khoon khol utha.

Gussa aaya.
Ek pal bhi nahi ruka.

Woh seedha
parvat se uchhal kar
Lanka ke gate par aa gaya.

Usne garaj kar kaha:

“Main Rama ka mitra hoon.
Aaj tu mujhse nahi bachega!”

Aur ek hi jhatke mein
Ravana ka mukut
zamin par gira diya.

⚔️ Bhayanak Mall-Yuddh

Ravana bhadak gaya.
Usne Sugriva ko pakad kar
zamin par patak diya.

Sugriva phir uchhla.
Usne bhi zor ka prahar kiya.

Dono khoon se laal the.
Pasina beh raha tha.

Kabhi ek upar,
kabhi doosra.

Mukkey, thappad,
pakad, patak.

Kabhi sher aur baagh jaise.
Kabhi do gusse wale hathi jaise.

Zameen kaanp rahi thi.
Ped gir rahe the.

Yuddh lamba chala.
Par koi thakta nahi tha.

✨ Sugriva ki Vijay

Akhir Ravana ne
maya ka sahara liya.

Sugriva samajh gaya.

Usne aasman ki taraf
uchhal laga di.

Ravana thak chuka tha.
Saans tez thi.
Aankhon mein ghabrahat thi.

Sugriva ne yuddh jeet liya.

Woh aakash mein
soch ki raftaar se udaa
aur apni sena ke paas laut aaya.

Vanar uska
jai-jai-kaar karne lage.

Rama ke chehre par
santosh tha.

📖 Is Adhyay ki Seekh

Ahankar hamesha thakaan laata hai

Sachchi shakti dharma ke saath hoti hai

Kabhi-kabhi jeetna matlab maarna nahi,
balatkaar todna hota hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.41
    with st.expander("Chapter 6.41 – Rama sends Angada as a messenger"):
        text1 = """
        Sugriva ko veerata ke chinh ke saath dekhkar,
Rama, Lakshmana ke bade bhai,
use gale lagate hain 🤍

Aur pyaar ke saath daant bhi dete hain।"""
        create_image_text_layout("attached_assets/chapter6/6.41.jpg", text1, layout="side", image_position="left")

        text2 = """
        🌿 Rama ka Sugriva ko samjhana

Rama bole:

“Sugriva, bina mujhse pooche
tumne bahut jaldbazi ki.

Ek raja ko aisa nahi karna chahiye.
Tumhari is himmat ne
mujhe, sena ko aur Vibhishana ko
bahut chinta mein daal diya.

Socho, agar tumhe kuch ho jaata,
toh Sita, Bharata,
Lakshmana aur Shatrughna ka kya hota?”

Rama thode bhavuk ho gaye 😔

“Main maanta hoon tum bahut veer ho,
par bina soche risk lena
sahi nahi.

Agar tum lautkar na aate,
toh mera sankalp tay tha—
Ravana aur uski sena ko maar kar
Vibhishana ko Lanka ka raja banaata,
Bharata ko Ayodhya ka singhasan deta
aur phir main apna jeevan tyag deta.”

🐒 Sugriva ka uttar

Sugriva bole:

“Prabhu,
jisne aapki Sita ko haran kiya,
use dekhkar
main apni shakti ko kaise rok leta?”

Rama muskuraye 😊
aur Sugriva ki veerta ki prashansa ki।

🌪️ Ashubh Sanket (Bad Omen)

Phir Rama Lakshmana se bole:

“Dekho,
tez hawa chal rahi hai,
dharti kaanp rahi hai,
pahaad hil rahe hain.

Ped gir rahe hain 🌳
laal sandhya darawani lag rahi hai.
Suraj se jaise aag ka ghera gir raha ho.

Raat ko chand bhi kala aur laal dikhta hai 🌕
Pakshi aur jaanwar
bhayankar awaaz nikaal rahe hain.

Yeh sab
bhayanak yuddh ka sanket hai.

Isliye aaj hi
Ravana ke kile par
hamla karna hoga!”

🛡️ Sena ka Vibhajan

Rama ne turant sena ko taiyaar kiya।

Neela, Mainda aur Dvivida → Poorvi Dwaar

Angada, Rishabha aur dusre veer → Dakshin Dwaar

Hanuman → Pashchim Dwaar

Sugriva → Madhya sthaan

Rama aur Lakshmana → Uttar Dwaar

Vanar aur bhalu
ped 🌲 aur pathar 🪨
hathiyaar bana kar
Lanka ko chaaron taraf se gher lete hain।

Lanka par jaise
doosri deewar ban jaati hai!

Rakshas ghabra jaate hain 😨
poori Lanka kaanp uthti hai।

🕊️ Angada ko Sandesh

Rama shant ho kar bole:

“Yuddh se pehle
raja ka dharm hota hai
shaanti ka sandesh dena.

Isliye Angada,
tum Lanka jao.

Ravana se kehna—

👉 ‘Ab bhi mauka hai.
Sita ko samman ke saath lauta do.
Yudh na chaho to bhi theek.’

👉 ‘Agar nahi maana,
toh main tumhe, tumhare putron ko
aur poori Rakshas jaati ko
samaapt kar doonga.’

👉 ‘Vibhishana hi Lanka ka raja banega.’”

Angada ne haan kaha 🙏
aur aakash ke raaste
Lanka pahunch gaya।

🔥 Angada aur Ravana

Angada ne Ravana ke sabha mein
Rama ka sandesh
bilkul sach-sach suna diya.

Ravana gusse se kaanp utha 😡

“Is vanar ko maar do!”
usne chillakar kaha।

Rakshas Angada ko pakad lete hain,
par Angada chupchaap sab dekh raha tha।

Achaanak—
💥 Angada ne teen rakshason ko uthaya,
mahal par chalang lagayi
aur chhat tod di!

Poora mahal hil gaya 🏰⚡

Angada zor se bola:
“Main Bali ka beta Angada hoon!”

Phir woh udta hua
wapas Rama ke paas aa gaya।

Vanar sena khush ho gayi 🐒🎉
Rakshas sena dar gayi 😨

🌼 Is Adhyay ki Seekh

Veerta ke saath soch zaroori hai

Yuddh se pehle shaanti ka prayas hona chahiye

Ahankar ant ka kaaran banta hai

Sachcha neta sabki suraksha sochta hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.42
    with st.expander("Chapter 6.42 – The demons attack suddenly"):
        text1 = """
        🏰 Ravana ko Khabar milti hai

Rakshas Ravana ke paas jaakar batate hain—
“Rama aur Vanar sena ne poori Lanka ko gher liya hai!”

Yeh sunkar Ravana gusse se bhar jaata hai 😡
Woh mahal ke upar chadhkar
poori Lanka ko dekhta hai—

Pahaad

Van

Bagiche

Aur har taraf an-ginit vanar

Ravana sochta hai:
“In sabko kaise khatam kiya jaaye?”

Thodi der baad
uska ghamand phir jaag uthta hai 😈
Aur woh Rama aur vanar sena ko ghoorne lagta hai।"""
        create_image_text_layout("attached_assets/chapter6/6.42.jpg", text1, layout="side", image_position="left")

        text2 = """
        💔 Rama ko Sita ki Yaad

Udhar Rama
Lanka ki taraf badhte hue
Sita ko yaad karte hain।

Unke mann mein dard uthta hai—

“Janak ki beti,
hirni jaisi aankhon wali Sita,
sirf mere liye
nangi zameen par so rahi hogi…”

Yeh soch kar
Rama ka sankalp aur mazboot ho jaata hai 🔥

📢 Rama ka Aadesh

Rama vanaron se kehte hain:

“Ab aur der nahi!
Shatru ka vinash taiyaar karo!”

Yeh sunte hi
vanar zor-zor se garajne lagte hain 🐒

“Hum Lanka ko
patharon, pedon aur apni mutthiyon se tod denge!”

🪨🌳 Vanar Sena ka Toofan

Vanar sena:

Bade-bade pathar phenkti hai

Ped ukhaad kar maarte hai

Deewarein tod dete hain

Khaiyon ko mitti, lakdi aur pathar se bhar dete hain

Lanka ke
burj, darwaaze aur meharaabein
tootne lagti hain 🏰💥

Naare goonj uthte hain:

“Jai Shri Rama!”

“Jai Lakshmana!”

“Jai Sugriva!”

🧭 Charo Dwaaron par Yojna

Poorv Dwaar → Kumuda (10 koti vanar)

Dakshin Dwaar → Shatabali (20 koti vanar)

Pashchim Dwaar → Sushena

Uttar Dwaar → Rama, Lakshmana aur Sugriva

Rama ke ek taraf Gavaksha,
doosri taraf Dhumra aur bhallu sena 🐻

Vibhishana har jagah Rama ke saath rehte hain 🤍

🔥 Ravana ka Pratighaat

Gusse mein Ravana hukm deta hai:

“Rakshaso! Bahar niklo aur hamla karo!”

Turant—

Nagade bajte hain 🥁

Shankh aur turhi goonj uthti hain 📯

Rakshas sena baadalon jaise umad padti hai ⚡

Jaise pralaya ka samundar toot pada ho!

⚔️ Bhayanak Yuddh

Phir shuru hota hai
Rakshas vs Vanar Mahayuddh ⚔️

Rakshas:

Gada, bhala, kulhaadi

Vanar:

Ped, pathar, daant aur naakhun

Naare lagte hain:

Vanar: “Jai Sugriva!”

Rakshas: “Ravana ki Jai!”

Rakshas deewaron se
kaante aur bhale phenkte hain,
toh vanar hawa mein uchhal kar
unhe kheench kar neeche gira dete hain!

Dharti
kichad aur lahu se bhar jaati hai 🌍
Yuddh itna bhayanak hota hai
ki dekhkar rom-rom kaanp jaaye।

🌼 Is Adhyay ki Seekh

Anyay ke khilaaf jab sab ek ho jaate hain, to sabse bada kila bhi gir sakta hai

Prem aur karuna se bhara krodh, vinash nahi nyay laata hai

Ahankar shakti ko andha kar deta hai

Sachchai ke paksh mein ladne wale kabhi akele nahi hote"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.43
    with st.expander("Chapter 6.43 – Monkeys and demons fight"):
        text1 = """
        ⚔️ Yuddh Poori Taaqat se Shuru

Vanar sena
poori shakti se lad rahi thi 🐒🔥
Aur rakshas bhi
ghodon, haathiyon aur rathon par chadh kar
Ravana ka naam lete hue
aage badh rahe the.

Sone se sajje ghode,
aag jaise chamakte haathi,
aur suraj jaise chamakते rath—
sab yuddh ke liye taiyaar the.

Donon taraf se
seedha takraav hua 💥"""
        create_image_text_layout("attached_assets/chapter6/6.43.jpg", text1, layout="side", image_position="left")

        text2 = """
        🥊 Veer vs Veer

Har taraf
ek se ek bhayanak muqabla ho raha tha:

Angada aur Indrajit
do pahadon jaise takra rahe the

Hanuman ne Jambumali se loha liya

Sugriva ne Praghasa par zor se vaar kiya

Lakshmana ne Virupaksha ka saamna kiya

Rama par kai rakshas ek saath toot pade

Har vanar
dharma ke liye lad raha tha.
Har rakshas
ghamand mein bhara tha.

🌪️ Khoon ki Nadiyaan

Yuddh itna bhayanak ho gaya
ki lahu behne laga.

Baal ghaas jaise lag rahe the

Khoon pani ki tarah beh raha tha

Zameen par rath, haathi, ghode aur sharir bikhre the

Lag raha tha
jaise poori dharti
is yuddh ko dekh kar kaanp rahi ho 🌍

🔥 Veerta ke Adbhut Drishya

Angada ne Indrajit ka rath tod diya

Hanuman ne ek hi haath se
rakshas ka rath palat diya

Sugriva ne ped se vaar karke
shatru ko gira diya 🌳

Lakshmana ne ek hi prahar mein
bhayanak rakshas ko dhool chata di

Rama ne
ek saath chaar shatruon ko
apne teer se gira diya 🏹✨

Vanar hansi ke saath lad rahe the,
rakshas cheekh ke saath gir rahe the.

🪨 Pathar, Ped aur Parakram

Vanar:

Pathar uthate

Bade ped tod kar maarte

Daant aur naakhun se vaar karte

Rakshas:

Gada

Teer

Bhale

Talwar

Har vaar ke saath
aasmaan aur dharti goonj uthti 🌩️

🌙 Din Ka Ant

Jab din dhalne laga,
rakshas thak chuke the.

Unke sharir khoon se bhare the,
mann mein darr tha 😨

Unhone socha:
“Bas raat aa jaaye…”

Vanar sena
abhi bhi tayaar thi.
Unki aankhon mein
jeet ki chamak thi ✨

🌼 Is Adhyay ki Seekh

Sachchai ke liye ladne wale kabhi thakte nahi

Ghamand taaqat ko kamzor bana deta hai

Ek saath milkar ladne se sabse bada shatru bhi gir jaata hai

Dharma ke paksh mein ladna hi sachi veerta hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.44
    with st.expander("Chapter 6.44 – Angada shows great bravery"):
        text1 = """
        🌑 Andheri Raat, Bhayanak Yuddh

Suraj doob gaya.
Raat aa gayi 🌙
Aur yuddh aur bhi bhayanak ho gaya.

Andhere mein
vanar aur rakshas
ek-dusre ko pehchan nahi pa rahe the.

“Tu rakshas hai?”

“Tu vanar hai?”

Bas awaazein thi—
“Maaro!”
“Pakdo!”
“Yahin ruk!”

Andhera, shor aur gussa
sab ek saath the 😨"""
        create_image_text_layout("attached_assets/chapter6/6.44.jpg", text1, layout="side", image_position="left")

        text2 = """
        🔥 Raat Mein Aag Jaise Yuddh

Rakshas andhere mein
pahadon jaise lag rahe the.
Unke gehre rang
aur bhayanak dikh rahe the.

Par vanar bhi kam nahi the 🐒💪
Unhone:

ghodon par hamla kiya

jhande aur pankh noch daale

haathiyon ko kaata

rathon ko tod diya

Har taraf
bhagdaud aur cheekh-pukaar thi.

🏹 Rama aur Lakshmana ka Prakop

Rama aur Lakshmana
teer chala rahe the
jaise zehreeli saanp 🐍✨

Dikhne wale bhi gire,
chhupe hue bhi gire.

dhool aankhon mein bhar gayi

khoon nadiyon ki tarah behne laga

Raat
pralay jaise lag rahi thi 🌪️

🔔 Shor aur Vinaash

nagade baj rahe the

shankh goonj rahe the

ghode hinhina rahe the

ghaayal cheekh rahe the

Zameen par
laashe pahadon jaise jama thi.

Lag raha tha
jaise duniya ka ant aa gaya ho 😔

🔥 Rama ka Adbhut Shaurya

Andhere ka fayda uthakar
kai rakshas
Rama par toot pade.

Par Rama ne
pal bhar mein
aag jaise teer chala diye 🏹🔥

Ek hi baar mein
kai bade rakshas gir gaye.

Unke teer
raat ko roshan kar rahe the
jaise jugnu ✨

Rakshas
jalte hue patangon jaise
girne lage.

🐒 Angada ka Veer Kaarnaama

Usi yuddh mein
Angada
sabse aage tha 💪🔥

Usne:

dushman ke ghode maare

rath tod daale

rakshason ko kuchal diya

Indrajit
thak gaya 😠
Aur achanak
gayab ho gaya—
adrishya!

Yeh dekh kar
sab dev aur rishi
Angada ki taarif karne lage 🌟

Vanar sena ne
“Bahut achha! Bahut achha!”
ka naara lagaya 🎉

🐍 Indrajit ka Maya-jaal

Par Indrajit
haar maan ne wala nahi tha.

Usne apni maya ka sahara liya 😈
Aur adrishya hokar
Rama aur Lakshmana par
bijli jaise teer barsa diye ⚡

Teer
saanpon jaise the 🐍
Aur unhone
Rama-Lakshmana ko
jaal mein baandh diya.

Vanar sena dekh kar
sann reh gayi 😢

Unke neta
bandhan mein the…

🌼 Is Adhyay ki Seekh

Veerta sirf taaqat nahi, himmat se hoti hai

Dharma ke liye ladne wala kabhi akela nahi hota

Ghamand aur maya se jeet temporary hoti hai

Sachchai chahe bandhi ho, par haarti nahi"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.45
    with st.expander("Chapter 6.45 – Indrajit wounds Rama and Lakshmana"):
        text1 = """
        🌑 Chinta Bhara Pal

Rama ko chinta hui 😔
Indrajit kahan gaya?

Sach jaanne ke liye
Rama ne 10 veer vanaron ko bheja:

Angada

Hanuman

Nila

Dvivida

Sharabha

aur anya shoor veer

Sab khushi se
aakash mein uchhal pade 🌌
haath mein bade-bade ped le kar."""
        create_image_text_layout("attached_assets/chapter6/6.45.jpg", text1, layout="side", image_position="left")

        text2 = """
        🐍 Adrishya Dushman

Par Indrajit adrishya tha 😈
Andhere mein
kisi ko dikhai nahi diya.

Usne teer chala diye—
saanpon jaise teer 🐍🏹

Vanar ghayal ho gaye,
unka raasta ruk gaya.

Koi bhi
Indrajit ko dekh nahi paaya
jaise baadal suraj ko chhupa lete hain ☁️☀️

🔥 Rama–Lakshmana Par Teer Varsha

Indrajit ne
Rama aur Lakshmana par
lagataar teer barsa diye.

Unke sharir par
ek bhi jagah khaali nahi thi 😢
Har taraf se
khoon beh raha tha.

Dono
kimshuk ke ped jaise lag rahe the—
laal-laal phoolon se bhare hue 🌺

😈 Indrajit ka Ghamand

Adrishya Indrajit bola:

“Jab main dikhai nahi deta,
toh Devraj Indra bhi mujhe nahi pakad sakta.
Tum dono toh phir bhi insaan ho!”

Usne aur zyada teer chala diye 😠
aur zor-zor se hansne laga.

💔 Veer Gir Pade

Teeron ke jaal mein
Rama aur Lakshmana
hil bhi nahi pa rahe the.

Thak gaye…
zakhmi ho gaye…
aur phir—

Rama gir pade 😭
Unka sone jaisa dhanush
haath se chhoot gaya.

Lakshmana ne jab yeh dekha,
unka dil toot gaya 💔

“Rama ke bina
main jee nahi sakta,”
unka mann bol utha.

🐒 Vanar Sena ka Dukh

Vanar sena ne
jab apne prabhu ko girte dekha—

aankhon mein aansu aa gaye 😢

cheekhein goonj uthi

himmat toot si gayi

Hanuman aage aaye,
sab vanar
Rama–Lakshmana ke paas
ikatthe ho gaye.

Dono bhai
behosh pade the,
teeron se bhare hue.

Har taraf
sirf shok aur sannata tha 🌫️

🌼 Is Adhyay ki Seekh

Bura ghamand hamesha andhera laata hai

Dharma ke veer bhi kabhi-kabhi girte hain

Par sachchai kabhi khatam nahi hoti

Andhera jitna gehra ho, subah utni hi paas hoti hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.46
    with st.expander("Chapter 6.46 – The monkey army feels hopeless"):
        text1 = """
        😢 Shok ka Maha-Pal

Jab vanaron ne
Rama aur Lakshmana ko
teeron se chhalni,
behosh pade dekha—

toh poori vanar sena ka dil hil gaya 💔

Sugriva, Bibishana, Hanuman, Angada,
Nila, Dvivida, Mainda, Sushena—
sab rote hue
Raghukul ke veeron ke paas aa gaye.

Dono bhai
teeron ki sej par
halke-halke saans le rahe the,
khoon se bheege hue,
jaise do sone ke dhwaj gir gaye hon 🩸"""
        create_image_text_layout("attached_assets/chapter6/6.46.jpg", text1, layout="side", image_position="left")

        text2 = """
        🪄 Adrishya Indrajit ka Ghamand

Indrajit,
jo abhi bhi adrishya tha,
khud apni jeet par itra raha tha 😈

Usne kaha:

“Rama aur Lakshmana
ab mere teeron se bandhe hain.
Devta bhi unhe chhuda nahi sakte!”

Aur phir
usne vanar veeron par bhi teer barsa diye—
Nila, Hanuman, Angada, Jambavan—
sab ghayal ho gaye.

Titans ne khushi mein
garjana ki:
“Rama mar gaya!” ⚡

Aur Indrajit
jeet ka ghosh karte hue
Lanka laut gaya.

🐒 Sugriva ka Dar aur Tootta Himmat

Yeh sunte hi
Sugriva ka sahas toot gaya 😨
Aankhon se aansu behne lage,
shareer kaanp raha tha.

Unhe laga—
“Sab kuch khatam ho gaya…”

🌿 Bibishana ka Dhairya aur Gyaan

Tab Bibishana aage aaye ✨
shaant, gambhir, aur dridh.

Unhone Sugriva se kaha:

“Dar mat, O Vanarraj.
Yeh yudh ki reeti hai.
Abhi sab kuch samaapt nahi hua.”

Unhone Sugriva ke aansu ponchhe,
mantra padhe,
aur himmat di:

“Rama abhi mare nahi hain.
Lakshmi unka saath nahi chhodti.
Jab ve chetna mein aayenge,
sabka bhay door ho jaayega.”

Bibishana ne kaha:

Abhi ghabraana mrityu jaisa hai

Raja ka kaam hai sena ko sambhalna

Veer girte hain,
par dharma kabhi nahi girta

🔥 Vanar Sena mein Nayi Asha

Bibishana
poori sena mein ghoom-gloom kar
sabko dhairya dete rahe 🌼

Unki shaant muskaan dekh kar
vanaron ka dar dheere-dheere kam hua.

👑 Lanka mein Jhooti Khushi

Udhar Lanka mein—
Indrajit ne Ravana se kaha:

“Rama aur Lakshmana mare pade hain!”

Ravana khushi se uchhal pada 😠
apne bete ko gale lagaya,
aur socha—
ab vijay nishchit hai.

Par woh nahi jaanta tha…

🌅 Is Adhyay ki Seekh

Asli neta woh hota hai jo andhere mein bhi himmat de

Jhooti jeet zyada der tikti nahi

Dharma ke veer gir sakte hain, par haarte nahi

Asha tab sabse zaroori hoti hai jab sab kuch toota hua lage"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.47
    with st.expander("Chapter 6.47 – Sita sees Rama and Lakshmana fallen"):
        text1 = """
        Ravana ka beta Indrajit
Lanka laut chuka tha.
Use laga—
uska kaam poora ho gaya 😈

Udhar battlefield par,
vanar veer Rama ke ird-gird khade the.
Hanuman, Angada, Nila, Jambavan—
sab satark the.

Halki si ghas bhi hile,
toh ve chilla uthte—
“Rakshas!” ⚔️"""
        create_image_text_layout("attached_assets/chapter6/6.47.jpg", text1, layout="side", image_position="left")

        text2 = """
        😏 Ravana ka Kroor Aadesh

Lanka mein Ravana khush tha.
Usne Sita ki rakshika rakshasiyon ko bulaya.

Aur ghamand se bola:

“Jaakar Vaidehi ko batao—
Rama aur Lakshmana mare pade hain.
Use Pushpaka Vimaan mein bithao
aur battlefield dikhao!”

Uska mann tha—
Sita toot jaaye.
Umeed chhod de.
Aur uske paas aa jaaye 😠

🚩 Pushpaka Vimaan aur Jhooti Ghoshna

Rakshasiyan Pushpaka Vimaan mein
Sita ko bitha kar udi.

Lanka bhar mein ghoshna hui—
“Rama aur Lakshmana mare gaye!”

Rakshas khush the.
Vanar dukhi.

💔 Sita ka Hriday-Vidaarak Drishya

Vimaan se Sita ne dekha—

Gire hue vanar

Dukhi sena

Aur beech mein…

Rama aur Lakshmana 😭

Teeron se chhalni.
Dhanush toot chuke the.
Kavach bikhar chuka tha.
Nishchet pade hue.

Jaise agni ke do yuva putra
zamin par so gaye hon.

😭 Sita ka Vilap

Yeh dekhte hi
Sita ka hriday toot gaya 💔

Aankhon se aansu ruk na sake.
Uska shareer kaanp utha.

Usne apne praan-priy ko
is haal mein dekha—
aur zor-zor se rone lagi.

Lakshmana bhi wahin pade the.
Dono veer.
Dono shaant.

Sita ne socha—
“Sab khatam ho gaya…”

Aur dukh se bhari awaaz mein,
Maithili rone-bilakhne lagi,
yeh maan kar
ki uska Rama ab nahi raha…

🌱 Is Adhyay ki Seekh

Sabse bada dukh tab hota hai jab umeed toot-ti dikhe

Adharma hamesha sach ka jhoota darshan karata hai

Par sach abhi poora saamne aaya nahi hota"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.48
    with st.expander("Chapter 6.48 – Sita cries in sorrow"):
        text1 = """
        Yeh adhyay Sita ke hriday ko poori tarah khol deta hai.
Yahan na yuddh hai, na shastra—
sirf virah, dukh aur prashn hain 💔

😭 Sita ka Antardvand (Inner Conflict)

Jab Sita ne Rama aur Lakshmana ko yuddh-bhoomi par nishchet dekha,
toh uska vishwas toot gaya.

Woh kehti hai:

“Mere shareer ke shubh lakshan jhoothe ho gaye?”

“Panditon ne kaha tha main kabhi vidhwa nahi banungi—phir yeh kya hai?”

Woh apne saare shubh chihnon ka varnan karti hai—
kamal-chihn, sundar ang, shubh rekhaen—
aur phir poochhti hai:

“Agar sab kuch shubh hai,
toh mera Rama kyun gira?”

Yeh sirf shok nahi—
yeh dharma aur bhagya par prashn hai."""
        create_image_text_layout("attached_assets/chapter6/6.48.jpg", text1, layout="side", image_position="left")

        text2 = """
        🌊 Bada Dukh: Kaushalya ka Smaran

Sita ke shabd yahan aur gehre ho jaate hain.

Woh kehti hai—

“Main apne liye nahi ro rahi…
main apni saas Kaushalya ke liye ro rahi hoon.”

Kaushalya, jo roz sochti hai:
“Kab Rama, Lakshmana aur Sita wapas aayenge?”

Yeh pankti
maa ke swapn ke tootne ka dukh dikhaati hai 😔

🌱 Trijata ka Aashvasan (Hope ka Deepak)

Tab Trijata bolti hai.

Shaant, spasht aur prem se 💠

Woh kehti hai:

Agar Rama sach mein mare hote,
toh vanar sena bikhar jaati

Yahan abhi bhi vyavastha aur satarkta hai

Pushpaka Vimaan bhi tumhe yahan na laata

Aur sabse mahatvapurn:

“Mrityu ke baad chehra badal jaata hai,
par Rama aur Lakshmana ki divyata abhi bhi bani hui hai.”

Isliye woh kehti hai—
“Woh jeevit hain.”

🙏 Sita ka Vishwas

Sita haath jod kar kehti hai:

“May it be so.”

Yeh poori tarah khushi nahi—
par asha ka ek beej hai 🌸

🌑 Ashoka Vatika mein Vaapsi

Pushpaka Vimaan wapas mudta hai.
Sita fir Ashoka Vatika aa jaati hai.

Par jo drishya usne dekha—
woh uske mann mein zinda reh jaata hai.

Aur uska dukh
aur gehra ho jaata hai.

🪔 Is Adhyay ki Gehri Seekh

Sita ka vilap = bhagya vs dharma ka sangharsh

Shubh lakshan bhi pariksha mein padte hain

Aasha tab bhi zinda rehti hai jab sab kuch toota lage"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.49
    with st.expander("Chapter 6.49 – Rama wakes up and cries for Lakshmana"):
        text1 = """
        Chapter 49 – Rama ka Jagna aur Lakshmana ke liye Vilap

Yeh adhyay bhai ke prem aur maanav kamzori ko bahut gehra dikhata hai.
Yahan Bhagwan nahi—
ek bhai rota hua dikhai deta hai 💔

🌑 Yuddh-Bhoomi ka Drishya

Teer aur baanon se bandhe hue
Rama aur Lakshmana
zameen par pade the.

Khoon beh raha tha.
Saans saap jaise chal rahi thi.
Charon taraf vanar sena aansuon mein doobi khadi thi 😔"""
        create_image_text_layout("attached_assets/chapter6/6.49.jpg", text1, layout="side", image_position="left")

        text2 = """
        🌅 Rama ka Hosh Mein Aana

Apni antar shakti se
Rama behoshi se jaag gaye.

Par jaagte hi
unki nazar Lakshmana par padi—
ghayal, nishchet, baanon mein jakda hua.

Aur tab
Rama ka hriday toot gaya 💔

😭 Rama ka Dukh Bhara Vilap

Rama bol pade:

“Agar Lakshmana nahi raha,
toh Sita mil jaaye ya jeevan mil jaaye—
mujhe kuch nahi chahiye.”

Woh kehte hain:

Sita jaisi patni dobara mil sakti hai

par Lakshmana jaisa bhai kabhi nahi

“Agar Lakshmana paanch tatvon mein mil gaya,
toh main bhi yahin apni saansen chhod dunga.”

👩‍👦 Maaon ka Smaran

Rama ki aankhon ke saamne
maaen aa jaati hain—

Kaushalya

Kaikeyi

aur sabse zyada Sumitra

Rama kehte hain:

“Main Sumitra ko kya jawab dunga?
Woh toh apne bete ke liye roti rahegi.”

Yeh shabd
maa–beta ke rishton ka bojh dikhate hain 😢

🏹 Lakshmana ki Mahanta

Rama Lakshmana ki veerta yaad karte hain:

Kabhi kathor shabd nahi bole

Ek saath 500 baan chala sakta tha

Indra ke baan bhi kaat deta tha

Rajmahal ka sukh chhod kar vanvaas aaya

Aur aaj—

“Wahi Lakshmana,
baanon ki sej par pada hai.”

Rama ke liye
yeh surya ke ast hone jaisa tha 🌑

🌊 Sugriva se Vidaai ke Shabd

Rama dukhi hokar Sugriva se kehte hain:

“Ab tum wapas chale jao.
Tumne apna dharma nibha diya.”

Woh vanaron ke balidaan ko yaad karte hain—
Hanuman, Angada, Jambavan, Mainda, Dvivida…

“Tum sabne apna farz poora kiya.”

Aur ant mein kehte hain:

“Main tum sab se vida leta hoon.”

Yeh sun kar
vanar sena ki aankhen bhar aati hain 😭

⚠️ Achanak Bhay

Tabhi door se
ek kaala-sa, tej swaroop aata dikhta hai.

Vanar sochte hain—
“Yeh Ravani hai!”

Aur dar ke maare
peeche hat jaate hain.

Par woh Bibishana tha—
jo sach aur dharma ke saath tha.

🪔 Is Adhyay ki Gehri Seekh

Veerta bhi bhai ke dukh ke aage chup ho jaati hai

Rama yahan maryada purushottam nahi—
ek rota hua bhai hai

Sachcha prem
shakti ke saath-saath karuna bhi hota hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.50
    with st.expander("Chapter 6.50 – Garuda frees Rama and Lakshmana"):
        text1 = """
        Chapter 50 – Garuda ne Rama aur Lakshmana ko Mukti di

Yeh adhyay asha, daivi sahayata aur sachchai ki jeet ka sandesh deta hai 🌟
Jab sab kuch toot-ta hua laga,
tab bhagwan ki kripa khud utri.

😨 Vanar Sena mein Afra-Tafri

Sugriva hairaan hokar poochte hain:

“Yeh bhagdad kyun?
Sena toh toofan mein phansi naav jaise lag rahi hai!”

Angada kehte hain:

“Rama aur Lakshmana baanon se dhake hue,
khoon mein latpat zameen par pade hain.”

Par Sugriva mehsoos karte hain—
kuch aur bhi gadbad hai."""
        create_image_text_layout("attached_assets/chapter6/6.50.jpg", text1, layout="side", image_position="left")

        text2 = """
        ⚠️ Galat Pehchaan, Galat Darr

Tabhi Bibishana
gada haath mein liye bolte hue aate hain:

“Victory to Rama! Victory to Rama!”

Par vanar ghabra jaate hain—
unhe lagta hai yeh Ravana ka beta hai 😰

Sugriva turant Jambavan ko kehte hain:

“Sabko batao, yeh Bibishana hai, shatru nahi!”

Aur dheere-dheere sena shaant hoti hai 🌿

😢 Bibishana ka Vilap

Bibishana Rama-Lakshmana ko dekh kar toot jaate hain:

“Mere bhai ke bete ne dhokhe se
in dono veeron ko is haal mein laa diya!”

Woh rote hue kehte hain:

“Meri saari ummeed inhi par thi.
Agar yeh na rahe, toh main bhi sab kho chuka hoon…”

🤝 Sugriva ka Vishwas

Sugriva Bibishana ko gale lagate hain:

“Ravana aur uska beta jeet nahi sakte.
Rama aur Lakshmana bachenge.
Tum nishchint raho—
Lanka ka raj tumhara hi hoga.”

🌿 Sushena ka Upay

Sugriva chahte hain Rama ko Kishkindha le jaaya jaaye,
par Sushena bolte hain:

“Isse pehle bhi dev-asur yuddh mein
dev behosh hue the.
Brihaspati ne unhe jadibootiyon se bachaya.”

Woh kehte hain:

Samjivani

Vishalya

yeh dono daivi jadibootiyan laani hongi.

Aur kehte hain:

“Is kaam ke liye
Hanuman hi jaa sakte hain.”

🌪️ Achanak Pralay jaisa Drishya

Tabhi—

tez aandhi 🌬️

bijli ⚡

samundar mein hulchul 🌊

ped girne lage 🌳

Sab dar gaye…

🦅 Garuda ka Aagman

Achanak aakash se
aag ke gole jaise chamakte hue
Garuda prakat hue 🦅✨

Unhe dekhte hi—

jo baan saap ban kar bandhe hue the

woh turant bhaag gaye 🐍➡️

Garuda ne Rama aur Lakshmana ko chhua.

✨ Chamatkar

Garuda ke sparsh se:

zakhm bhar gaye

chehra chamak utha

bal, buddhi, yaad-dasht
sab dugna ho gaya

Rama aur Lakshmana
phir se khade ho gaye 🌞

🙏 Rama ka Prashn

Rama poochte hain:

“Aap kaun hain?
Aapko dekh kar mujhe
pita Dasharatha ki yaad aa rahi hai.”

Garuda muskura kar kehte hain:

“Main tumhara mitra hoon, Rama.
Main Garuda hoon.”

⚔️ Garuda ka Updesh

Garuda kehte hain:

“Indrajit ke jaadu ko
devta bhi nahi tod sakte the.
Tum dono bhagyashaali ho.”

Aur chetavni dete hain:

“Rakshas yuddh mein dhokha dete hain.
Tumhara hathiyaar sirf dharma aur maryada hai.
Kabhi un par bharosa mat karna.”

🕊️ Vidaai aur Asha

Garuda jaane se pehle kehte hain:

“Jab Ravana marega
aur Lanka shant hogi,
tab tum Sita ko wapas laoge.”

Aur phir
hawa ki raftaar se
aakash mein gaayab ho gaye 🌌

🎉 Vanar Sena ka Utsav

Rama aur Lakshmana ko theek dekh kar:

vanar garajne lage 🦁

nagade bajne lage 🥁

shankh phoonke gaye 📯

Aur phir—

“Lanka par phir se hamla!”

🌺 Is Adhyay ki Seekh

Jab sab asha toot jaaye,
tab bhi bhagwan ka sahara hota hai

Dharm ke raaste par chalne wale
kabhi akela nahi hota

Dhokha kuch pal jeet sakta hai,
par sachchai hamesha ant mein jeetti hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.51
    with st.expander("Chapter 6.51 – Dhumraksha comes to fight"):
        text1 = """
        Bandar sena ka zordaar shor poore aakash ko hila raha tha 🐒⚔️
Unki awaaz samundar tak goonj rahi thi.

Yeh shor Ravana ke kaan tak pahunch gaya.
Ravana ghabra gaya aur bola:

“Yeh bandar itna khush kyun hain?
Maine toh Rama aur Lakshmana ko be-hosh kar diya tha.
Phir yeh itna bada hungama kyun?”

Usne turant apne rakshason ko hukm diya:
“Jaakar dekho! Sach kya hai!”"""
        create_image_text_layout("attached_assets/chapter6/6.51.jpg", text1, layout="side", image_position="left")

        text2 = """
        😱 Sach Sun Kar Ravana Ka Dar

Rakshas deewar par chadhe…
Aur jo dekha, unka rang udd gaya 😨

Rama aur Lakshmana bilkul theek the

Bandhan toot chuke the

Dono sher jaise khade the

Bandar sena unke saath khadi thi

Rakshas bhaag kar Ravana ke paas aaye aur bole:

“Raja!
Jin teeron ne dono bhaiyon ko baandha tha,
woh bekaar ho chuke hain.
Rama–Lakshmana phir se shaktishaali ho gaye hain.”

Yeh sun kar Ravana ka gussa aur darr dono badh gaye 🔥
Usne daant pees kar kaha:

“Agar Indrajit ke astr bhi kaam nahi aaye,
toh meri shakti khatre mein hai!”

⚔️ Dhumraksha Ko Aadesh

Ravana ne turant ek bhayanak rakshas ko bulaya—
Dhumraksha

“Bina der kiye jao.
Badi sena le jao.
Aur Rama–Lakshmana ko maar daalo!”

Dhumraksha ne haan mein sir jhukaya
aur sena jama karne nikal pada.

🛡️ Rakshason Ki Bhayanak Sena

Bhale-bhale hathiyaar ⚔️

Gada, talwaar, bhala

Rath, haathi, tez ghode 🐘🐎

Garajne aur hansne ki awaazein

Dhumraksha sone se sajje rath par baitha tha.
Woh pashchim dwaar se nikla,
jahan Hanuman pehra de rahe the.

⚠️ Bure Shagun (Bad Omens)

Jaise hi Dhumraksha aage badha:

Aakash se khun barsa ☁️🩸

Zameen kaanpne lagi

Andhera chha gaya

Giddh rath par baith gaye

Yeh sab bure shagun the.

Dhumraksha ka dil kaanp utha,
aur rakshas sena bhi darr gayi.

🐒 Saamne Bandar Sena

Aur tab…
Dhumraksha ne dekha—

Bandar sena samundar ki lehron jaisi faili hui thi 🌊
Aur unke beech,
Rama aur Lakshmana raksha kavach jaise khade the.

Yuddh ab nishchit tha.

🌟 Is Chapter Ka Moral

Adharm se jeeti hui shakti tikti nahi

Dharma jab jaagta hai, toh darr bhi kaanp jata hai

Bure shagun ghamand ka ant batate hain

Sach aur nyay ke saath khadi sena hamesha balwaan hoti hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.52
    with st.expander("Chapter 6.52 – Hanuman kills Dhumraksha"):
        text1 = """
        Jaise hi Dhumraksha yuddh-kshetra mein aaya,
poori Vanar Sena garaj uthi 🐒⚔️
Ped, patthar, chattanen – jo haath laga, wahi shastra ban gaya.

⚔️ Bhayanak Sangharsh: Vanar vs Rakshas

Rakshas bhale, gada, trishul, teer se vaar kar rahe the

Vanar ped, chattan, daant aur panjon se palat-waar

Aakash garaj raha tha, dharti lahu se bhar rahi thi

Yeh yuddh itna bhayanak tha ki:

Rath toot gaye

Jhande gir pade

Haathi-ghode pahaadon jaise dhah gaye

Yuddh ka shor ek sangeet jaisa lag raha tha –
teer ki taar, ghodon ki hin-hinahat, haathiyon ki garaj 🎶⚔️"""
        create_image_text_layout("attached_assets/chapter6/6.52.jpg", text1, layout="side", image_position="left")

        text2 = """
        🔥 Dhumraksha ka Prakop

Apni sena ko haarte dekh,
Dhumraksha khud aage aaya.

Vanaron ko kaat raha tha

Khoon ki nadiyaan beh rahi thi

Kai veer vanar shaheed ho gaye

Vanar sena lad rahi thi,
par rakshas ka prakop bhayanak tha.

🌪️ Hanuman ka Pravesh

Tab Hanuman ne dekha
ki vanar sena pe bhari sankat aa gaya hai.

Unki aankhen krodh se laal ho gayi 🔥
Haath mein ek vishal chattan utha li.

Ek hi prahar mein:

Dhumraksha ka rath choor-choor

Dhwaj, pahiye, dhanush – sab toot gaye

Dhumraksha rath chhod kar
gada le kar zameen par aa gaya.

🗻 Antim Yuddh: Hanuman vs Dhumraksha

Dhumraksha ne apni gada Hanuman ke sir par maari ⚡

Par Hanuman hilay bhi nahi

Fir Hanuman ne:

Pahaad ka shikhar utha kar

Seedha Dhumraksha ke sir par de maara

💥 Rakshas ke ang-ang toot gaye
Aur Dhumraksha
pahaad ki tarah dharti par gir pada – mrit 💀

😱 Rakshason ki Haar

Apne senapati ko marta dekh:

Rakshas bhag kar Lanka bhaag gaye

Vanar sena ne unka peecha kiya

Aur Hanuman,
shatruon ka vinash kar,
thak kar bhi prasann hue 😊

Vanar veeron ne:

Hanuman ka jay-jaykaar kiya

Unhe badhai di

🌟 Is Adhyay ka Moral

Adharm ki sena chahe badi ho, dharma ke saamne tik nahi sakti

Hanuman shakti ka nahi, bhakti aur kartavya ka prateek hain

Ghamand aur hinsa ka ant nishchit hota hai

Jab raksha ke liye krodh uthta hai, woh bhi dharmic ho sakta hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.53
    with st.expander("Chapter 6.53 – Vajradamshtra enters the battle"):
        text1 = """
        Jab Ravana ne suna
ki Dhumraksha maara gaya hai,
toh uska gussa aag ban gaya 🔥
Woh saap ki tarah hiss karne laga.

Usne apne shaktishaali senapati
Vajradamshtra ko bulaya aur bola:

👉 “Turant jao!
Rama,
Sugriva
aur in sab vanaron ko hara do!”

Vajradamshtra ne garaj kar kaha,
“Aisa hi hoga!” ⚔️"""
        create_image_text_layout("attached_assets/chapter6/6.53.jpg", text1, layout="side", image_position="left")

        text2 = """
        🚩 Rakshason ki Bhayanak Sena

Vajradamshtra:

Haathi, ghode, khacchar, gadhon ki sena lekar nikla

Rang-birange jhande lahrane lage

Sona-jade rath chamakne lage ✨

Rakshas:

Talwar, bhale, gada, trishul, teer

Rangin kavach pehne

Mad se bhare haathiyon par sawaar

Poori sena
bijli-chamakte baadalon jaisi lag rahi thi ⚡☁️

⚠️ Ashubh Sanket (Bad Omens)

Jaise hi sena nikli:

Aakash se ulka-paat hua

Siyaar bhayanak awaaz mein cheekhne lage

Zameen ladkhadane lagi

Yeh sab ashubh sanket the 😨
Par Vajradamshtra ruka nahi.

🐒⚔️ Yuddh ka Aarambh

Rakshas aage badhe,
toh Vanar Sena ne bhi
zor se garjana ki 🐒🔥

Phir shuru hua:

Ped aur patthar vs talwar aur bhale

Rath takraaye

Nagade aur shankh goonj uthe

Har taraf:

Khoon

Tooti hui talwaren

Gire hue jhande

Yuddh ka shor
kan phaad dene wala tha 🔊

🌪️ Vajradamshtra ka Atank

Vajradamshtra:

Yuddh-bhoomi mein bhay faila raha tha

Vanaron ko tezi se girata ja raha tha

Woh Mrityu-devta jaisa lag raha tha 😈

Par tab:

Hanuman aur

Angada
aage badhe 💥

🦁 Angada ka Pratishodh

Angada,
ankhon mein krodh liye,
haath mein vishal ped utha kar
rakshason par toot pada 🌳⚔️

Rakshas ped ki tarah girne lage

Unke sir chakna-choor ho gaye

Sena bikharne lagi

Yuddh-bhoomi:

Tooti hui rath

Gire hue haathi-ghode

Khoon ki nadiyaan

Par Angada rukaa nahi 💪

🌟 Is Adhyay ka Moral

Gussa aur ahankaar hamesha vinaash laata hai

Bure sanket ignore karna, aur zidd mein ladna, haar ka kaaran banta hai

Dharma ke liye ladne wale thode hote hain, par shaktishaali hote hain

Sachchi veerta, ahankaar ko hara deti hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.54
    with st.expander("Chapter 6.54 – Angada kills Vajradamshtra"):
        text1 = """
        Jab Vajradamshtra ne dekha
ki uski poori sena
Angada ki shakti se
tut rahi hai,
toh uska gussa aag ban gaya 🔥

Usne apna bhayanak dhanush khincha,
jo Indra ke vajra jaisa chamak raha tha ⚡
Aur vanaron par
teeron ki baarish kar di."""
        create_image_text_layout("attached_assets/chapter6/6.54.jpg", text1, layout="side", image_position="left")

        text2 = """
        ⚔️ Bhayankar Yuddh

Rakshas: teer, talwar, gada lekar toot pade

Vanar: ped aur bade patthar utha kar ladne lage 🌳🪨

Yuddh itna bhayanak tha ki:

Zameen khoon se bhar gayi

Aakash mein pakshi mandraane lage

Har taraf cheekh aur garjana thi

Fir bhi:
👉 Vanar peeche nahi hate
👉 Rakshas bhi zidd par the

🦁 Angada vs Vajradamshtra

Jab vanar sena ghabra kar
Angada ke paas aa gayi,
toh Angada aur Vajradamshtra
aamne-saamne aa gaye ⚔️

Yeh yuddh tha:
🦁 Sher aur
🐘 madmast haathi ke jaise.

Vajradamshtra ne:

Hazaaron teer chalaye

Angada ka sharir khoon se bhar diya

Par Angada toota nahi 💪

🪨 Parvat jaisa Prahar

Angada ne pehle:

Ek bada ped phenka 🌳
Rakshas ne use kaat diya.

Phir Angada ne:

Ek vishal patthar ghumaa kar phenka 🪨
Woh Vajradamshtra ke rath par gira
Aur rath chur-chur ho gaya 💥

Phir:

Angada ne poora pahad ka tukda utha liya
Aur seedha
Vajradamshtra ke sir par de maara ⚡

Rakshas:

Ladkhada gaya

Khoon ugalne laga

Shakti tootne lagi

⚔️ Antim Yuddh (Final Fight)

Ab dono:

Talwar aur dhaal lekar

Bilkul paas aa gaye

Khoon se bhare hue,
dono Kimshuka ke phool jaise lag rahe the 🌺

Achanak:
🔥 Angada ki aankhon mein bijli chamki
Aur usne ek tez talwar uthayi.

⚔️ Ek hi vaar mein
Angada ne Vajradamshtra ka
sir alag kar diya.

Rakshas ka sir zameen par gira,
aur yuddh khamosh ho gaya.

🏃‍♂️ Rakshason ki Haar

Apne senapati ko gira dekh kar:

Rakshas dar kar bhagne lage 😨

Sab Lanka ki taraf bhaag gaye

Aur:
🎉 Vanar sena jeet gayi 🎉

Angada:

Sab ke beech khada tha

Indra dev jaise chamak raha tha ✨

Sab vanaron ne uski veerata ka samman kiya 🙏

🌟 Is Adhyay ka Moral

Sachchi veerta kabhi haar nahi maanti

Gussa aur ahankaar ant mein vinash laata hai

Dharma ke liye ladne wala hamesha vijayi hota hai

Ek sacha veer poori sena se zyada shaktishaali hota hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.55
    with st.expander("Chapter 6.55 – Akampana attacks the monkeys"):
        text1 = """
        Jab Vajradamshtra ke vadh ka samachar
Ravana tak pahuncha,
toh uska krodh simha ke garjan jaisa phoot pada 🐍🔥

Ravana ne apne senapati se kaha:

“Akampana ko sena ke saath bhejo.
Woh shastron ka maha-vidwaan hai,
yuddh ka premi hai,
aur mere liye apna praan bhi de sakta hai.
Wah Rama, Lakshmana aur Sugriva sabko nasht kar dega.”"""
        create_image_text_layout("attached_assets/chapter6/6.55.jpg", text1, layout="side", image_position="left")

        text2 = """
        ⚔️ Akampana ka Prasthaan

Akampana:

Badal ke jaise rang ka

Garajti bijli jaisi awaaz ⚡

Sone se saja hua rath

Bhayanak rakshason se ghirā hua

Yeh woh yoddha tha:
👉 jo devtaon ke saamne bhi kabhi kampit nahi hua

Lekin…
❗ Apashakun shuru ho gaye

Rath ke ghode thak gaye

Baayi aankh phadakne lagi

Chehra peela pad gaya

Tez aur ulta hawa chalne lagi 🌬️

Pakshi aur pashu rone lage 🦅

Phir bhi:
👉 Akampana ne kismat ko nazarandaaz kiya
👉 Aur yuddh ki or badhta raha

🌪️ Yuddh ka Mahatandav

Jaise hi Rakshas sena aayi:

Vanar ped utha kar khade ho gaye 🌳

Aakash aur samudra garaj uthe 🌊

Fir:
⚔️ Bhayanak yuddh shuru ho gaya

Cheekh

Garjana

Shastron ki takrahat

Rath, dhwaj, dhal – sab tootne lage

Itni dhool uthi ki:
❌ Dost aur dushman pehchaane nahi ja rahe the
❌ Rakshas rakshas ko maar rahe the
❌ Vanar vanar par gir padte the

Zameen:

Khoon aur kichad se bhar gayi 🩸

Laashen hi laashen dikhne lagi

🐒 Vanar Veeron ka Pratihar

Jab dhool baithi,
toh phir se:

Ped

Patthar

Gada

Bhale

sab chalne lage.

Rakshas:

Teer aur bhale se vanaron ko gira rahe the
Vanar:

Ped aur chattan se rakshason ko kuchal rahe the 💥

🔥 Akampana ka Prayās

Akampana:

Apni sena ko sambhalne laga

Rakshason ko utsaahit kiya

Lekin tabhi:
🐒 Vanar neta toot pade

Kumuda

Nala

Mainda

In teenon ne:

Bade-bade ped uthaye

Rakshason ke jhund kuchal diye

Dushman ki panktiyaan tod di ⚡

Rakshas sena mein:
❌ Afra-tafri mach gayi
❌ Yuddh ka santulan bigad gaya

🌟 Is Adhyay ka Arth (Moral)

Apashakun ko andekha karna vinash ka sanket hota hai

Sirf shastra nahi, dharma aur sahas bhi yuddh jeetate hain

Jab neta ghamand mein andha ho jaaye, sena tut jaati hai

Ekjut veer poori sena par bhaari padte hain"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.56
    with st.expander("Chapter 6.56 – Hanuman kills Akampana"):
        text1 = """
        Jab Akampana ne dekha
ki vanar neta uski sena ko kuchal rahe hain,
toh uska gussa aag ban gaya 🔥

Usne apne saarathi ko garaj kar kaha:
“Rath tez chalao.
Aaj main in vanaron ko mita dunga!”"""
        create_image_text_layout("attached_assets/chapter6/6.56.jpg", text1, layout="side", image_position="left")

        text2 = """
        ⚔️ Akampana ka Atyachar

Akampana:

Tez ghoḍon wale rath par aaya

Teeron ki baarish kar di 🏹

Vanar:

Panktiyaan toot gayi

Bahut se girne lage

Har taraf afra-tafri mach gayi

Laga jaise sab kuch khatam ho jaayega…

🐒 Hanuman ka Aagman

Tab Hanuman aage badhe 💨
Apne saathi girte dekh,
unka dil dard aur krodh se bhar gaya.

Hanuman ko dekhte hi:

Vanaron ka hausla laut aaya

Sab uske ird-gird khade ho gaye

Hanuman:
👉 chattan ki tarah atal
👉 teeron ko nazarandaaz karta hua

🔥 Mahaveer ka Pratihar

Akampana ne Hanuman par bhi teer barsaaye.
Lekin Hanuman:

Hilaa tak nahi

Muskuraya 😌

Usne ek bada pathar uthaya
Aur ghoomakar Akampana ki taraf phenka.

Akampana ne:

Teeron se us chattan ko tod diya

Yeh dekh:
❗ Hanuman ka krodh aur badh gaya

🌳 Ped bana Astra

Hanuman ne:

Parvat jaisa Ashvakarna ka ped ukhaad liya 🌳

Garaj kar aage dauda

Jahan-jahan gaya:

Ped toot gaye

Haathi, rath, sainik sab kuchle gaye

Rakshas:

Bhaagne lage

Dar se cheekhne lage 😨

☠️ Antim Yuddh

Akampana ne:

14 teer Hanuman ke sharir mein maar diye

Hanuman:

Teeron se bhara hua

Phir bhi prakashmaan ✨

Jaise phoolon se bhara vriksh

Usne:

Ek aur bada ped ukhaada

Zordaar kood lagaya

Aur Akampana ke sir par vaar kiya 💥

⚡ Ek hi prahar mein Akampana gir gaya
Zameen par nishchal.
Praan chhod chuka tha.

🏃‍♂️ Rakshason ki Haar

Apna neta marte dekh:

Rakshas kaanp uthe

Hathiyaar phenke

Lanka ki taraf bhaage

Vanar:

Unka peecha karte rahe

Garjana se aakash goonj utha 🐒🌩️

🌸 Vijay aur Sammaan

Hanuman:

Shant hue

Sab vanaron ko samman diya

Unhe naman mila:

Rama

Lakshmana

Sugriva

Vibhishana

Aur devtaon se bhi 🙏

Hanuman:
👉 Vishnu ke saman vijayi lage
👉 Dharma ke rakshak bane

🌟 Is Adhyay ki Seekh (Moral)

Ghamand ka ant nishchit hota hai

Sachcha bal shastra se nahi, dharma se aata hai

Jab ek veer khada hota hai, poori sena khadi ho jaati hai

Hanuman jaise yoddha sahas aur seva ka jeevit roop hain"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.57
    with st.expander("Chapter 6.57 – Prahasta comes to fight"):
        text1 = """
        Akampana ke marne ki khabar sunte hi
Ravana ka chehra utar gaya 😠
Gussa tha.
Par mann mein chinta bhi thi.

Usne apne mantriyon ke saath baithkar socha.
Shehar Lanka gher liya gaya tha.
Har taraf vanar sena thi."""
        create_image_text_layout("attached_assets/chapter6/6.57.jpg", text1, layout="side", image_position="left")

        text2 = """
        .

👑 Ravana ka Faisla

Ravana ne apne vishwasniya senapati
Prahasta se kaha:

“Yeh nagri sirf kuch hi log bacha sakte hain.
Main, Kumbhakarna, Indrajit…
aur tum, Prahasta.”

Usne aadesh diya:
👉 “Badi sena ke saath niklo.
Vanaron ko dara do.
Unka shor sunte hi woh bhaag jayenge.”

Ravana ko laga:

Vanar asthir hain

Discipline nahi hai

Garaj sunke toot jayenge

Yeh uska bhram tha.

🛡️ Prahasta ka Uttar

Prahasta ne shant swar mein kaha:

“Raja, pehle bhi maine kaha tha—
Sita ko lautana hi shreshth marg hai.
Par ab yuddh tay ho chuka hai.”

Usne aage kaha:
“Main aapka rin chukaunga.
Mera jeevan, dhan, sab aapka hai.
Aaj main yuddh mein praṇ de dunga.”

Yeh kehkar usne sena bulane ka aadesh diya ⚔️

🏹 Rakshas Sena ki Taiyari

Pal bhar mein:

Lanka yoddhaon se bhar gayi

Haathi, ghode, rath, sab saj gaye

Talwarein chamak uthi

Nagade aur shankh bajne lage

Havan hua.
Devtaon ko smaran kiya gaya.
Sugandhit hawa behne lagi 🌬️

Sabko laga:
👉 “Aaj rakshason ka din hai.”

🚩 Prahasta ka Rath

Prahasta apne shandaar rath par chadha:

Sona jada hua

Tez ghode

Jhanda sarp ke chinh ke saath 🐍

Woh baadal jaisa garajta hua
purab ke dwaar se nikla.

Uske saath:

Narantaka

Kumbhahanu

Mahanada

Samunata

Badi sena ke beech
Prahasta pralay jaise lag raha tha.

⚠️ Ashubh Sanket

Par jaise hi woh nikla…

Aasmaan se ulka giri 🌠

Gidad aag ugalte hue roye

Baadalon se khoon ki baarish hui

Giddh jhande par baith gaya

Ghode ladkhada gaye

Sab ashubh tha.

Par Prahasta ne dhyaan nahi diya.
Ghamand ne aankhen bandh kar di.

🐒 Vanar Sena Taiyaar

Doosri taraf:

Vanar ped ukhaad rahe the 🌳

Bade patthar uth rahe the 🪨

Garjana hone lagi

Yuddh ka shankhnaad goonj utha 🌩️

Prahasta ne socha:
👉 “Main in sabko mita dunga.”

Aur garajta hua
woh vanar sena par toot pada
jaise patanga aag par girta hai 🔥

🌟 Is Adhyay ki Seekh (Moral)

Achhi salah ko nazarandaz karna vinaash laata hai

Ghamand aankhon par parda daal deta hai

Ashubh sanket ko samajhna bhi buddhi hai

Yuddh shuru hone se pehle hi haar likhi ja sakti hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.58
    with st.expander("Chapter 6.58 – Prahasta is killed"):
        text1 = """
        Jab Prahasta
apni badi sena ke saath yuddh ke liye badha,
toh Rama muskuraye 😊
aur Vibhishana se poocha:

“Yeh kaun hai jo itni gati aur ghamand ke saath aa raha hai?”

Vibhishana ne shant swar mein kaha:
“Yeh Prahasta hai.
Ravana ki sena ka mukhya senapati.
Bahut balwaan aur yuddh-vidya mein nipun.”"""
        create_image_text_layout("attached_assets/chapter6/6.58.jpg", text1, layout="side", image_position="left")

        text2 = """
        ⚔️ Yuddh ka Toofan

Prahasta garajta hua aage badha.
Uske saath rakshason ki bheed thi.

Vanar sena ne bhi garaj kar jawab diya 🐒
Aur bhayankar yuddh shuru ho gaya.

Rakshas: talwar, bhale, gada, teer

Vanar: ped 🌳, patthar 🪨, mukke 👊

Aasmaan shor se bhar gaya.
Zameen lahu se laal ho gayi.

Hazaron vanar gire.
Hazaron rakshas bhi dharti par gir pade.

🔥 Veeron ke Veer

Prahasta ke saathi ek-ek karke gire:

Narantaka ko Dvivida ne giraya

Samunnata ko Durmukha ne

Mahanada ko Jambavan ne

Kumbhahanu ko Tara ne

Yeh dekh Prahasta aur bhadak utha 😡
Usne teeron ki baarish kar di.

Yuddh ek toofan ban gaya.

🐒 Nila ka Pravesh

Tab vanaron ke veer
Nila
aage aaye.

Prahasta ne un par
aag jaise teer barsa diye 🔥
Par Nila ne sab seh liya.

Aankhen band karke
woh parvat jaise khade rahe.

⚡ Antim Sangharsh

Nila ne ek bada sa ped uthaya
aur Prahasta ke ghodon ko gira diya.

Prahasta ne krodh mein gada uthayi
aur rath se kood pada.

Dono aamne-saamne the.
Khoon se bheege hue.
Do matwale haathi jaise 🐘🐘

Prahasta ne gada se vaar kiya.
Nila ladkhadaye…
par gire nahi.

Nila ne ek bahut bada patthar uthaya
aur poori shakti se Prahasta ke sir par de maara 🪨

💥 Prahasta ka Patan

Patthar toot gaya.
Prahasta bhi toot gaya.

Uska shareer dharti par gira
jaise ped jad se kat jaata hai 🌳

Rakshas sena yeh dekh kar
bhay se bhaag gayi.

Netā ke bina
sena kabhi tik nahi paati.

🌼 Vijay aur Sammaan

Nila vijayi hue 🏆
Aur jab wapas aaye,
Rama aur Lakshmana ne
unhe samman diya 🙏

Vanar sena khushi se garaj uthi.

🌟 Is Adhyay ki Seekh (Moral)

Ghamand hamesha girata hai

Shakti se zyada dhairya jeetata hai

Netā girta hai toh sena bhi toot jaati hai

Dharma ke saath khade rehne wale ant mein vijayi hote hain"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.59
    with st.expander("Chapter 6.59 – Ravana shows his power in battle"):
        text1 = """
        Prahasta ke girte hi
rakshas sena ghabra gayi 😨
Aur bhagte hue
Ravana ke paas pahunchi.

Yeh sunte hi
Ravana ka krodh aag ban gaya 🔥
Uski aankhen laal ho gayi.

“Ab main khud yuddh mein utarunga,”
usne garaj kar kaha."""
        create_image_text_layout("attached_assets/chapter6/6.59.jpg", text1, layout="side", image_position="left")

        text2 = """
        ⚔️ Ravana ka Pravesh

Ravana apne chamakte rath par chadha.
Narsinghon aur nagadon ki awaaz ghoonj uthi.

Rakshas sena
parvat jaise dikhti thi 🏔️
Aur samne vanar sena
ped aur patthar le kar khadi thi 🐒

Yeh maha-yuddh tha.

👑 Vibhishana ka Parichay

Rama ne poocha:
“Yeh kaun-kaun se veer hain?”

Vibhishana ne ek-ek ko bataya.
Indrajit.
Atikaya.
Nikumbha.
Aur beech mein khud Ravana.

Rama ne shant swar mein kaha:
“Iska tej sooraj jaisa hai.
Par adharm ka ant nischit hai.”

🐒 Sugriva Girte Hain

Ravana ne pehla vaar kiya.
Uska teer
Sugriva ko laga.

Sugriva behosh ho gaye.
Rakshas khush ho uthe 😈

Par vanar rukhe nahi.

🔥 Hanuman ka Samna

Hanuman
seedha Ravana ke paas aaye.

“Tum devtaon se surakshit ho,”
Hanuman bole,
“par vanaron se nahi.”

Ravana muskuraya.
Aur zor se thappad mara 👊

Hanuman hil gaye…
par gire nahi.

Unke vaar se
Ravana bhi kaanp utha 😲

🛡️ Lakshmana aur Nila

Ravana ne
Nila ko shaktishaali teer se gira diya.

Phir woh
Lakshmana par toot pada.

Dono mein bhayankar yuddh hua.
Teer, shastra, bhale…
sab chala.

Ek shaktishali bhala
Lakshmana ke seene mein laga.

Lakshmana gir pade 😔

🐒✨ Hanuman ka Balidaan

Hanuman daud kar aaye.
Lakshmana ko utha liya.

Unhe phool jaisa halka laga 🌸
Yeh bhakti ka bal tha.

Ravana phir se sambhla
Aur wapas vaar karne laga.

🌩️ Rama ka Krodh

Yeh dekh
Rama ka dhairya toot gaya.

Hanuman ke kandhon par chadh kar
Rama ne Ravana par prahar kiya ⚡

Unke teeron ne
Ravana ka rath tod diya.
Mukoot gira diya 👑

Ravana behosh ho gaya.

Sab devta, rishi, vanar
jai-jai kar uthe 🙌

🌼 Karuna ka Vijay

Ravana hosh mein aaya.
Toh Rama ne teer neeche rakhe.

Rama bole:
“Tum thak chuke ho.
Aaj main tumhe nahi maarunga.”

“Lanka jao.
Aaram karo.
Aur phir poori shakti se lautna.”

Yeh veeron ka dharm tha.

Ravana sharm se jhuk gaya.
Aur Lanka laut gaya.

🌟 Is Adhyay ki Seekh (Moral)

Asli shakti karuna mein hoti hai

Veerta ka matlab hamesha maarna nahi

Dharma yuddh mein bhi maryada hoti hai

Ghamand toot sakta hai, par dharm amar rehta hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.60
    with st.expander("Chapter 6.60 – The demons wake Kumbhakarna"):
        text1 = """
        🏰 Ravana ka Manthan (Inner Conflict)

Lanka laut kar Ravana ka garv choor ho chuka tha.
Usse pehli baar ehsaas hua ki Rama ke teeron ka saamna uske vardaan bhi nahi kar pa rahe.

Ravana ko yaad aayi:

Ikshvaku vansh ka shraap

Vedavati ka abhishap

Deviyon aur rishiyon ki bhavishyavani

Aur tab usne ek hi naam liya — Kumbhakarna."""
        create_image_text_layout("attached_assets/chapter6/6.60.jpg", text1, layout="side", image_position="left")

        text2 = """
        😴 Kumbhakarna: Shap aur Nindra

Kumbhakarna
— Rakshason ka jeevit parvat ⛰️
— Brahma ke shap se lambi-lambi neend mein bandha

Kabhi:

6–8 mahine

Kabhi 9 din
tak so jaata tha, bina hosh ke.

Ravana garja:

“Jab Lanka jal rahi ho, tab yeh mahakaay so raha hai!”

🔊 Rakshason ka Asafal Prayas

Rakshas gaye Kumbhakarna ki gufa mein:

Shankh, nagade, ghantiyaan 🔔

Haathi, ghode, oont us par chadhaye

Hazaron log daudte rahe uske sharir par

Phir bhi…
woh nahi jaga 😨

Aakhir:

Bhookh ka prahar hua 🍖

Sharir par bhaar badha

Aur achanak —

💥 Kumbhakarna uth baitha!

👁️ Bhayankar Uday

Jab Kumbhakarna jaga:

Aankhen aag ke gole 🔥

Saans aandhi jaisi 🌪️

Aakaar pahaad se bada

Uska jamaai:

Hazaron janwaron ka maans

Khoon aur madira 🍷

Phir usne poocha:

“Bina kaaran mujhe koi jagata nahi… batao, kya sankat hai?”

⚠️ Sach ka Prakash

Mantri Yupaksha ne kaha:

Ek manav ne Lanka ko hila diya

Vanar pahaadon jaise aa gaye

Ek hi vanar (Hanuman) ne nagar jala diya 🔥

Ravana ko Rama ne jeevan-daan diya 😶

Yeh sun kar Kumbhakarna garja:

“Aaj hi main Rama–Lakshmana aur vanar sena ka ant kar dunga!”

🍷 Yuddh se Pehle Utsav

Hajaaron ghade madira

Maans ke pahaad

Snan, abhishek, shastra-dharan

Kumbhakarna chala —
Yamraj ki tarah ⚔️

Uske kadam se:

Prithvi kaanp uthi 🌍

Akash andhera ho gaya

Vanar sena mein bhay fail gaya 😱

Kuch bhage,
kuch gir pade,
kuch Rama ki sharan mein gaye.

🌑 Is Adhyay ki Gehri Seekh

Adharm ka antim sahara bhi bhay se hi utta hai

Jab buddhi haar jaaye, tab bal ko jagaya jaata hai

Par bhay se uthaya gaya bal bhi ant mein dharm ke saamne girta hai"""
        create_image_text_layout(text_content=text2, layout="full")
    # Chapter 6.61
    with st.expander("Chapter 6.61 – The story of Kumbhakarna is told"):
        text1 = """
        Rama apna dhanush haath mein liye khade the.
Tab unhone dekha ek bahut bada rakshas aage badh raha hai.
Uske sir par mukut tha.
Badan pahaad jaisa.
Aankhen peeli aur bhayanak.

Usse dekh kar vanar sena phir se ghabra gayi 😨
Kuch bhag gaye, kuch chup gaye.

Rama thode hairaan hue.
Unhone Bibishana se poocha:

“Yeh kaun hai?
Itna bada, itna bhayanak!
Maine aaj tak aisa jeev nahi dekha.”"""
        create_image_text_layout("attached_assets/chapter6/6.61.jpg", text1, layout="side", image_position="left")

        text2 = """
        📖 Bibishana ne batayi Kumbhakarna ki purani kahani

Bibishana bole, shaant awaaz mein:

“Prabhu, yeh Kumbhakarna hai.
Ravana ka bhai.
Sabse zyada shaktishaali rakshas.

Yeh sirf vardaan se strong nahi hai.
Yeh janm se hi maha-shaktimaan hai.”

👶 Janm se hi bhookh aur vinash

Jab Kumbhakarna paida hua,
toh bachcha hote hue bhi usse bahut bhookh lagti thi.

Woh hazaaron logon ko kha gaya

Rishiyon ke ashram ujaad diye

Devta bhi darr gaye

Sab log Indra ke paas gaye aur bole:

“Agar yeh aise hi raha, duniya khatam ho jayegi!”

⚡ Devta aur Brahma ka nirnay

Indra ne apna vajra chalaya.
Par Kumbhakarna rukne wala nahi tha.

Aakhir sab Brahma ji ke paas gaye.
Brahma ji ne Kumbhakarna ko bula kar kaha:

“Tum duniya ke liye khatra ho.
Aaj se tum gehri neend mein rahoge.”

Yeh sunte hi Kumbhakarna gir pada.
Shap lag chuka tha.

😴 Neend ka vardaan aur shraap

Ravana ghabra gaya.
Usne Brahma ji se vinati ki:

“Use hamesha ke liye mat sulaiye.
Thoda samay jagne ka bhi de dijiye.”

Brahma ji ne kaha:

6 mahine neend

1 din jagna

Sirf ek din ke liye woh uthta,
khata-peeta
phir wapas so jata.

⚠️ Aaj kyun jaga Kumbhakarna?

Bibishana bole:

“Rama,
aaj Ravana darr gaya hai.
Isliye usne Kumbhakarna ko jagaya.

Kumbhakarna ab bhookh aur gusse mein hai.
Woh vanaron ko kha jana chahta hai.”

Vanar sena yeh sun kar aur darr gayi 😟

🕊️ Rama ka sahas aur buddhi

Rama muskuraye 😊
Aur bole:

“Yeh sirf darr ka roop hai.
Koi machine nahi, par
dharm ke saamne koi shakti tik nahi sakti.”

Phir Rama ne Nila ko aadesh diya:

Vanar sena ko sambhalo

Pathar, ped, chattan uthao

Darna nahi

🐒 Vanar sena ka hausla wapas aaya

Hanuman, Angada, Nila, Gavaksha
sab aage badhe 💪

Vanar phir se garje:

“Jai Shri Rama!”

Ped aur chattan haath mein liye
woh Lanka ke darwazon ki taraf badhne lage.

🌟 Is Adhyay ki Seekh

Bina buddhi ke shakti vinash laati hai

Bhay se jagaya gaya bal andha hota hai

Sachcha sahas gyaan aur dharm se aata hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.62
    with st.expander("Chapter 6.62 – Kumbhakarna meets Ravana"):
        text1 = """
        Kumbhakarna, jo abhi-abhi gehri neend se jaga tha, apni poori bhayanak shakti ke saath Lanka ke rajpath par aage badh raha tha.
Uska har kadam dharti ko kaanpa deta tha.

Hazaaron rakshas uske saath the,
ghar-ghar se phoolon ki varsha ho rahi thi 🌸
jaise koi maha-yoddha vijay yatra par ho."""
        create_image_text_layout("attached_assets/chapter6/6.62.jpg", text1, layout="side", image_position="left")

        text2 = """
        🏰 Ravana ke mahal mein pravesh

Jab Kumbhakarna ne sone se chamakte mahal ko dekha,
toh woh andar gaya.

Usne dekha —
Ravana, jo hamesha garv se bhara rehta tha,
aaj chinta aur bhay mein dooba hua hai.

Kumbhakarna ko dekhte hi Ravana khada ho gaya,
use gale lagaya 🤝
aur samman ke saath paas bithaya.

❓ Kumbhakarna ka prashn

Kumbhakarna, jinki aankhen abhi bhi krodh se laal thi, bole:

“Bhai…
mujhe zabardasti neend se kyun uthaya?
Batao,
kaun tumhe dara raha hai?
Aur kis ka vadh chahte ho mujhse aaj?”

😔 Ravana ka dard aur asahai pukaar

Tab Ravana ne apna mann khol diya.

Usne kaha:

“Rama ne samudra paar kar liya hai

Vanaron ne samudra par setu bana diya

Lanka ke van-upvan tak nasht ho rahe hain

Mere sabse bade yoddha mare ja chuke hain 😞

“Main har upaay kar chuka hoon,
par ab koi sahara nahi bacha.”

Ravana ki awaaz mein ahankaar nahi,
sirf bebasi thi.

🙏 Bhai se bhai ki vinati

Ravana ne kaha:

“Aaj Lanka mein sirf
bache aur boodhe bache hain.

Bhai,
sirf tum hi is nagar ko bacha sakte ho.”

Usne Kumbhakarna ko un yuddhon ki yaad dilayi
jab usne Devtaon ko bhi hara diya tha.

“Tum jaisa bal kisi ke paas nahi.

Aaj,
sirf bhai ke liye
apni shakti dikhao.”

🌪️ Aakhri ummeed

Ravana ne kaha:

“Jaise hawa badalon ko uda deti hai,
waise hi
vanar sena ko bikher do.”

Is pal Ravana ne pehli baar apna garv chhod kar
sirf ek baat ki —

👉 “Mujhe bachao.”

🌟 Is Adhyay ki Seekh

Ahankaar tootne par hi sachchai dikhti hai

Galat raah par chal kar, balwaan bhi akela ho jaata hai

Jab buddhi galat ho, tab shakti ka sahara liya jaata hai

👉 Agla Adhyay:
Kumbhakarna ka yuddh ke liye nikalna —
jahan bal aur bhookh dono ek saath dikhenge ⚔️"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.63
    with st.expander("Chapter 6.63 – Kumbhakarna comforts Ravana"):
        text1 = """
        Ravana ka dukh sun kar
Kumbhakarna halka sa hans pada 😏
lekin us hansi ke peeche gehri samajh thi.

🗣️ Kumbhakarna ki Kadvi Sachchai

Kumbhakarna bola:

“Bhai…
jo galat karta hai,
usse uska phal milta hi hai.”

Usne shant par teekhe shabdon mein kaha:

Tumne mantriyon ki baat nahi suni

Apni taakat par zyada ghamand kiya

Jo kaam pehle hona chahiye tha,
use baad mein kiya

Aur jo baad mein sochna chahiye tha,
use pehle kar daala

👉 Galat samay par kiya gaya sahi kaam bhi nuksaan deta hai."""
        create_image_text_layout("attached_assets/chapter6/6.63.jpg", text1, layout="side", image_position="left")

        text2 = """
        👑 Achha Raja Kaun Hota Hai?

Kumbhakarna samjhaata hai:

Achha raja salah leta hai

Dharm, arth aur kaam —
teeno ka santulan rakhta hai

Jo sirf haan mein haan milane walon ki baat sunta hai,
woh barbaad hota hai

Jo lalchi aur moorkh salahkar rakhta hai,
woh apni hi naav dooba deta hai

Usne yaad dilaya:

“Mandodari aur Bibishana ne bhi
yahi kaha tha…”

😡 Ravana ka Gussa

Ravana bhadak utha 🔥

Usne kaha:

“Ab purani baatein kyun?
Ab jo ho gaya, ho gaya!

Mujhe updesh nahi,
samadhan chahiye!”

Ravana ne sakht awaaz mein kaha:

“Agar tum sach mein mere ho,
to apni taakat dikhao.

Dost wahi hota hai
jo museebat mein bachaye!”

🤍 Kumbhakarna ka Badla Hua Swabhav

Kumbhakarna samajh gaya
👉 “Bhai gusse mein hai.”

Ab uski awaaz shaant aur bharose se bhari thi.

Usne kaha:

“Shaant ho jao, bhai.
Jab tak main zinda hoon,
tumhein darr ki zarurat nahi.”

⚔️ Yuddh Ka Vaada

Kumbhakarna ne poore vishwas se kaha:

Main Rama aur Lakshmana ka saamna karunga

Vanar sena ko bhaga dunga

Lanka ke logon ke aansu ponch dunga

Tum apni aankhon se meri taakat dekhoge

Uski awaaz aur tez ho gayi:

“Agar Indra, Yama ya Agni bhi aaye,
to main unse bhi lad jaaun!”

🦾 Ahankaar aur Andha Vishwas

Kumbhakarna bola:

“Mujhe hathiyaaron ki zarurat nahi.
Mere haath hi kaafi hain.”

Usne ghamand se kaha:

“Aaj main Rama ko maar kar
tumhari khushi laaunga.”

🍷 Ravana ko Tasalli

Aakhri mein Kumbhakarna bola:

“Tum shok chhodo,
madira piyo,
aur nischint raho.”

“Aaj Rama marega,
aur Sita hamesha ke liye tumhari hogi.”

🌟 Is Adhyay ki Seekh

Achhi salah tabhi kaam aati hai jab samay par maani jaye

Shakti bina buddhi ke andhi hoti hai

Ahankaar insaan ko sach dekhne nahi deta

Gusse mein diya gaya vachan aksar vinaash laata hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.64
    with st.expander("Chapter 6.64 – Mahodara gives advice"):
        text1 = """
        Kumbhakarna ki baat sun kar
Mahodara aage aaya.
Uski awaaz tez thi,
lekin soch chaalaak thi. 😈

🗣️ Mahodara ka Jawab

Mahodara bola:

“Kumbhakarna,
tu bahut taakatwar hai,
par tu sirf bal par bharosa karta hai.”

Usne seedha kaha:

Sirf shakti se sab kuch nahi hota

Aage kya hoga, yeh sochna zaroori hota hai

Raja Ravana moorkh nahi hai

Use samay, sthal aur nuksaan–faayda sab pata hai

Mahodara ne thoda taana maara:

“Tu jawani ke josh mein
sirf bolna jaanta hai.”"""
        create_image_text_layout("attached_assets/chapter6/6.64.jpg", text1, layout="side", image_position="left")

        text2 = """
        ⚖️ Dharma, Arth aur Kaam

Mahodara samjhaata hai:

Dharma, arth aur kaam
dushman nahi hote

Galat tareeke se paaya gaya sukh
aakhirkaar dukh deta hai

Jo log sirf sukh ke peeche bhaagte hain
unka ant yahin hota hai

👉 Galat raasta chhota lagta hai,
par akhir mein gehra gaddha hota hai.

⚠️ Rama ka Khatra

Mahodara ne gambhir awaaz mein kaha:

Rama ne Janasthana ke rakshason ko akela mita diya

Woh ghayal sher jaisa hai

Use chhedna matlab
sote hue saanp ko jagaana 🐍

Usne seedha sawal poocha:

“Tu akela Rama se kaise ladega?”

🧠 Mahodara ki Chaalaak Yojana

Phir Mahodara Ravana ki taraf muda
aur dheere se bola:

“Yuddh zaroori nahi.
Dhokha zyada asaan hai.”

Usne apni plan batayi:

Hum log bolenge
“Hum Rama se ladne gaye”

Khoon mein lipte wapas aayenge
aur kahenge
“Rama aur Lakshmana mar gaye”

Poore Lanka mein jashn hoga 🎉

Afsaan phail jaayega
“Vanar sena khatam ho gayi”

Phir Ravana
chupke se Sita ke paas jaayega

💔 Sita ko Todne ki Koshish

Mahodara bola:

Sita ko kaha jaayega
“Rama nahi raha”

Dukh mein doobi Sita
kamzor ho jaayegi

Uphaar, sona, sukh dikha kar
use behlaaya jaayega

Uska vishwas tha:

“Dukh aur akelapan
aadmi ko galat faisla karne par majboor kar deta hai.”

🏆 Lalach Bhara Sapna

Mahodara ne ant mein kaha:

“Na sena maregi,
na tum khatre mein padoge.”

“Sirf chaal se
tum jeet jaoge.”

Usne muskurate hue bola:

“Yahi sabse aasan jeet hai.”

🌟 Is Adhyay ki Seekh

Shakti bina buddhi ke andhi hoti hai

Dhokha turant faayda deta hai,
par lambi haar likh deta hai

Sachcha prem jhoot se kabhi nahi jeeta ja sakta

Dukh mein liya gaya faisla aksar galat hota hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.65
    with st.expander("Chapter 6.65 – Kumbhakarna joins the battle"):
        text1 = """
        Mahodara ki baat sunkar
Kumbhakarna gusse mein aa gaya.
Uski aankhen laal thi,
awaaz garaj rahi thi. 😠

🗣️ Kumbhakarna ka Ghoshna

Kumbhakarna ne Ravana se kaha:

“Aaj hi main
Rama ko maar kar
is khatre ko khatam kar dunga.”

Usne garv se bola:

Veer log baatein nahi karte

Veer log karke dikhate hain

Jo sirf meethi baat kare
woh yuddh barbaad kar dete hain

Uska maanna tha:

“Lanka barbaad ho chuki hai
sena khatam ho rahi hai
par main ab bhi zinda hoon.”"""
        create_image_text_layout("attached_assets/chapter6/6.65.jpg", text1, layout="side", image_position="left")

        text2 = """
        😈 Mahodara par Taana

Kumbhakarna ne Mahodara ko bhi nahi chhoda:

“Tu sirf bolna jaanta hai”

“Tu yuddh se darta hai”

“Aise log hi raja ko gumraah karte hain”

Usne kaha:

“Main jaaunga,
akela bhi ladunga
aur sab galat neeti ka badla loonga.”

👑 Ravana ka Vishwas

Ravana hans pada. 😏
Usne kaha:

“Sach hai!
Mahodara Rama se darr gaya hai.”

Ravana ne Kumbhakarna ki tarif ki:

“Tu mera sabse bada sahara hai”

“Teri shakti ka koi muqabla nahi”

“Vanar tujhe dekh kar bhaag jayenge”

Usne kaha:

“Jaao, yeh ghadi
Rakshason ke liye sabse mahatvapurn hai.”

🗡️ Yuddh ki Taiyari

Kumbhakarna ne apna
bhala (spear) uthaya.
Woh sone se saja tha,
bijli jaisa chamak raha tha ⚡

Us bhale par:

dushmano ka khoon laga tha

uski aag jaise chamak thi

Kumbhakarna bola:

“Main akela kaafi hoon.
Aaj bhookh mein
main vanaron ko kha jaunga.”

⚠️ Ravana ka Rokna

Ravana ne samjhaaya:

“Akela mat jaa.
Vanar bahut taakatwar hain.”

Isliye:

Rakshas sena saath bheji gayi

haathi, ghode, rath bhi nikle

Ravana ne khud
Kumbhakarna ko sajaya:

mukut 👑

kundal

haar

sone ka kavach

Woh jalti hui agni jaisa lag raha tha 🔥

🌪️ Bhayankar Aakaar

Kumbhakarna ab
aur bhi bhayankar ho gaya:

pahad jitna bada

aankhen rath ke pahiye jaisi

kadam se dharti kaanp uthi 🌍

Usne hans kar kaha:

“Aaj vanar
aag ke patangon ki tarah
jal kar khatam ho jayenge.”

Usne sach bola:

“Vanar buri jaati nahi hai,
par Rama hi asli dushman hai.”

🌩️ Apashakun (Bure Sanket)

Jab Kumbhakarna nikla:

andhera chha gaya

bijli giri ⚡

dharti aur samundar kaanp gaye

giddh bhale par baith gaya

baaya haath aur aankh phadki

Sab bure sanket the.

Par Kumbhakarna ne
koi dhyaan nahi diya.

🐒 Vanar Sena Mein Darr

Jaise hi vanaron ne
Kumbhakarna ko dekha:

sab dishaon mein bhaag gaye

badal jaise bikhar gaye ☁️

kuch gir pade

kuch behosh ho gaye

Kumbhakarna zor se hasa 😈
uski hansi garajti badalon jaisi thi.

Woh apni bhari gada uthakar
Mrityu devta ki tarah
vanar sena par toot pada. ⚔️

🌟 Is Adhyay ki Seekh

Ghamand shakti ko andha bana deta hai

Bure sanket ignore karna vinaash laata hai

Sirf bal se yuddh nahi jeeta jaata

Jo apne aap ko sabse bada samajhta hai,
wahi sabse pehle girta hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.66
    with st.expander("Chapter 6.66 – Angada scolds the fleeing monkeys"):
        text1 = """
        Jaise hi Kumbhakarna shehar ki deewar se kood kar bahar aaya,
uski bhayankar garaj se:

paani hil gaya 🌊

pahaad kaanp gaye 🏔️

bijli ki awaaz bhi dab gayi ⚡

Uska aakaar pahaad jaisa tha.
Uski aankhen aag jaisi thi. 🔥"""
        create_image_text_layout("attached_assets/chapter6/6.66.jpg", text1, layout="side", image_position="left")

        text2 = """
        😱 Vanar Sena Mein Bhagdad

Jaise hi vanaron ne use dekha:

koi idhar bhaaga

koi udhar

koi samundar mein kood gaya 🌊

koi hawa mein uchhal gaya

bhalu pedon par chadh gaye 🌳

kuch gir kar behosh ho gaye 😵

Poora maidan afra-tafri se bhar gaya.

🦁 Angada ka Gussa

Yeh dekh kar Angada bhadak utha.
Usne zor se pukara:

“Tum sab bhaag kahan rahe ho?
Apni veerata aur vansh bhool gaye kya?”

Usne Nala, Nila, Gavaksha aur Kumuda se kaha:

“Darr kar bhaagna shobha nahi deta”

“Woh akela hai, hum sab milkar use hara sakte hain”

“Woh sirf tumhe darrana chahta hai”

Angada bola:

“Wapas aao!
Apni taakat par bharosa rakho!”

⚔️ Dobara Yuddh

Angada ki baaton se
kuch vanar ruk gaye.
Unhone:

ped uthaye 🌲

chattan uthayi 🪨

pahad ke tukde phenke

Vanar mad haathi ki tarah
Kumbhakarna par toot pade.

🔥 Par Kumbhakarna Ruka Nahi

Par Kumbhakarna:

hila bhi nahi

jaise jungle mein aag lag jaaye 🔥

waise hi vanaron ko girata chala gaya

Khoon se bhare vanar
zameen par gir gaye
jaise laal phoolon wale ped gir jaate hain 🌺

🏃‍♂️ Fir Se Darr

Phir se:

kuch bhaag gaye

kuch samundar mein

kuch pahaadon mein

kuch gir kar behosh

Darr phir jeet gaya. 😨

📣 Angada ka Aakhri Updesh

Angada phir chillaya:

“Ruko!
Yuddh karo!
Bhaag kar kahin suraksha nahi milegi!”

Usne kaha:

“Agar tum bhaage,
tumhari patniyaan tum par hasegi”

“Darr se bhaagna
veeron ke liye mrityu se bhi bura hai”

“Jo ladte hue marte hain,
unhe Swarg milta hai”

“Jo bhaagte hain,
unka naam mitt jaata hai”

Angada bola:

“Aaj ya toh jeet milegi
ya amar kirti.”

😔 Vanaron ka Jawaab

Vanaron ne kaha:

“Kumbhakarna ne bahut tabahi macha di hai.
Abhi jeena zaroori hai.”

Aur woh fir se bikhar gaye.

🌟 Umeed Ki Kiran

Lekin Angada ne haar nahi maani.
Usne baar-baar samjhaya.

Aakhir:

vanar shaant hue

himmat juti 💪

Angada ke aadesh maane

Aur phir se yuddh ke liye wapas aaye. ⚔️

🌈 Is Adhyay ki Seekh

Darr sabse bada dushman hota hai

Sahi neta haar ke waqt bhi himmat deta hai

Izzat aur veerata bhaag kar nahi milti

Milkar ladne se sabse bada daitya bhi hara ja sakta hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.67
    with st.expander("Chapter 6.67 – Kumbhakarna fights fiercely"):
        text1 = """
        Angada ki lalkaar sunkar vanar sena phir se palti.
Darr ko peeche chhod, balidaan ka sankalp lekar sab Kumbhakarna par toot pade.

🔥 Kumbhakarna ka Bhayankar Tandav

Kumbhakarna ne:

hazaaron vanaron ko ek hi jhatke mein gira diya

kaiyon ko baahon mein pakad kar kuchal diya

aur kuch ko nigal gaya 😨

Woh Garud jaise sarpon ko kha jaata ho—aisa lag raha tha.
Zameen khoon se bhar gayi, aur vanar sena phir ghabra uthi."""
        create_image_text_layout("attached_assets/chapter6/6.67.jpg", text1, layout="side", image_position="left")

        text2 = """
        💥 Veeron ka Pratirodh

Hanuman ne pahad ka shikhar uthakar prahar kiya

Nila, Rishabha, Sharabha jaise veer bhi lage rahe

Par Kumbhakarna ko jaise koi farq hi nahi padta

Usne Sugriva ko pakad liya aur Lanka ki or le chala.
Vanaron ka mann toot gaya…

🧠 Hanuman ka Vivek

Hanuman ne socha:

“Sugriva swayam apni veerta se chhoot sakta hai.
Abhi sena ko sambhalna zyada zaroori hai.”

Aur sach mein—
Sugriva ne daant aur nakhunon se Kumbhakarna ke kaan-naak cheer diye
aur chhalang laga kar Rama ke paas aa gaye 🙏

⚔️ Lakshmana ka Pravesh

Ab Lakshmana ne yuddh sambhala:

Teer par teer barsaaye

Kumbhakarna ko laal-ghayal kar diya

Par daitya ab bhi andha ho chuka tha,
dost-dushman ka bhed bhool kar sabko khata ja raha tha.

🏹 Shri Rama ka Mahapravesh

Tab Rama aage badhe—
shaant, dridh, aur dharma se bhare.

Unke teeron se:

Kumbhakarna ka gadda-dharan haath kata

phir dusra haath

phir pair

Fir bhi woh Rahu ki tarah Rama par toot pada!

☀️ Antim Prahaar

Rama ne Brahma-dand jaise tej wala divya teer chhoda—
jo bijli se tez, surya se prakashmaan tha.

Woh teer:

Kumbhakarna ka sheesh kaat gaya

dharti kaanp uthi 🌍

devtaon ne jai-jai kaar ki 🙌

Kumbhakarna
—jo kabhi na hara tha—
aaj dharma ke haath se gir pada.

🌸 Vijay ka Utsav

Aakash se pushpon ki varsha hui

Vanar sena ke chehre kamal jaise khil gaye

Rama surya ki tarah andhkaar se nikal aaye ☀️

🌿 Is Adhyay ki Gehari Seekh

Bal bina dharma andha hota hai

Ahankar jitna bada, patan utna gehra

Sahi netritva (Angada, Hanuman) sena ko phir khada karta hai

Ant mein satya aur dharma hi vijayi hota hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.68
    with st.expander("Chapter 6.68 – Ravana mourns Kumbhakarna’s death"):
        text1 = """
        Jab Kumbhakarna Rama ke haathon gir pada,
toh kuch daitya bhagte hue Ravana ke paas aaye.

Unhone kaha,
“Rajaa…
jo kaal ka bhi muqabla karta tha,
aaj woh mar chuka hai.”

Unhone bataaya—
Kumbhakarna ka aadha sharir samundar mein gir gaya hai.
Uska sir Lanka ke dwar par pada hai.
Naak aur kaan kate hue hain.
Khoon se lathpath sharir
jaise aag se jala hua vriksh."""
        create_image_text_layout("attached_assets/chapter6/6.68.jpg", text1, layout="side", image_position="left")

        text2 = """
        💔 Ravana ka Girna

Yeh sunte hi Ravana behosh ho gaya.
Uska gham asahniya tha.

Bhatije—
Devantaka, Narantaka, Trishiras, Atikaya—
sab bilakh pade.
Mahodara aur Mahaparshva ka mann bhi toot gaya.

😭 Vilap aur Pachhtava

Hosh mein aakar Ravana roya:

“Haay mere veer bhai…
mere bal ka stambh chala gaya.

Tu tha jo
devtaon aur asuron ko dara deta tha.
Aaj tu Rama ke ek teer se gir gaya?

Jise Indra ka vajra bhi hila na saka,
usey ek manushya ne gira diya?

Ab Lanka ka kya hoga?
Vanar sena ab deewaron par chadh aayegi.

Mujhe na rajya chahiye,
na Sita.
Kumbhakarna ke bina
yeh sab arthheen hai.

Bibishana ne jo kaha tha…
aaj sab sach sabit ho gaya.
Maine usey nikala,
aur apna hi vinaash bula liya.”

🌑 Ant mein Shunya

Ravana ka ahankar toot chuka tha.
Uski awaaz bhari hui thi.
Aankhon mein sirf pashchatap tha.

Bhai ke shok mein dooba,
woh phir se behosh ho gaya.

🌿 Is Adhyay ki Seekh

Bal aur ghamand bina dharma ke tikte nahi

Jo sahi salah ko thukrata hai,
uska ant dukh aur pachtave se hota hai

Apno ka naash
ahankar ki sabse badi keemat hoti hai"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.69
    with st.expander("Chapter 6.69 – Angada kills Narantaka"):
        text1 = """
        Ravana abhi bhi Kumbhakarna ke shok mein dooba tha.
Uski aankhon mein aansu the.
Dil bhaari tha.

Tab Trishiras aage aaya aur bola,
“Raja, veer log shok mein nahi doobte.
Aap teenon lok jeet chuke ho.
Phir himmat kyun toot rahi hai?”

Usne kaha,
“Chaaho toh main khud yuddh mein jaaun.
Aaj Rama ka ant kar dunga.”

Yeh sunte hi
Devantaka, Narantaka aur Atikaya bhi taiyaar ho gaye.
Sab ke sab gusse aur garv se bhare hue the.

Ravana ne apne putron ko gale lagaya.
Unhe shastra, abhushan aur ashirvaad diya.
Aur kaha,
“Jaao… yuddh mein vijay laao.”"""
        create_image_text_layout("attached_assets/chapter6/6.69.jpg", text1, layout="side", image_position="left")

        text2 = """
        ⚔️ Yuddh ka Garjana

Daitya sena Lanka se nikli.
Hathi, ghode, rath…
Sab garajte baadal jaise lag rahe the.

Saamne vanar sena bhi taiyaar thi.
Haath mein patthar.
Ped aur pahad uthaye hue.

Dono taraf se
bhayanak yuddh shuru ho gaya.

🔥 Narantaka ka Atank

Narantaka apne tez ghode par chadha.
Haath mein chamakta bhala tha.

Usne vanaron par
bijli ki tarah hamle kiye.
Ek ke baad ek
sauon vanar girne lage.

Vanar sena phir se ghabra gayi.
Kuch bhaagne lage.

Tab Sugriva ne dekha
aur zor se bola,
“Angada!
Jaao aur us daitya ka ant karo!”

🦁 Angada ka Pravesh

Angada, Bali ka beta,
aage badha.

Uske paas
na koi shastra tha,
na kavach.

Sirf bal aur dhairya.

Usne Narantaka se kaha,
“Kamzor vanaron se kyun ladta hai?
Agar veer hai toh
mere se lad!”

💥 Antim Mukabla

Narantaka gusse mein bhala phenka.
Par Angada ka seena
heere jaisa majboot tha.

Bhala toot gaya.

Gusse mein Narantaka ne mukka mara.
Angada thoda ladkhadaya,
par gira nahi.

Phir Angada ne
apni poori shakti se
Narantaka ke seene par prahar kiya.

Daitya ka seena toot gaya.
Khoon behne laga.
Aur Narantaka
pahad ki tarah gir pada.

🌸 Vijay ka Ullas

Aakash se devtaon ne
jai-jai ka naad kiya.

Vanar sena khush ho gayi.
Rama ke chehre par
santosh ki muskaan thi.

Angada ne
ek aur mahaan vijay haasil ki.

🌱 Is Adhyay ki Seekh

Sirf shastra nahi, sahas aur atma-vishwas bhi jeet dilata hai

Ghamand se bhara bal
sachche dhairya ke aage gir jaata hai

Yuva veer bhi
mahaan kaam kar sakte hain"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.70
    with st.expander("Chapter 6.70 – Many demon warriors are killed"):
        text1 = """
        Narantaka ke girte hi
Devantaka, Trishiras aur Mahodara ro pade.
Unka gussa aansuon se bhi tez tha.

Phir ek saath
teenon Angada par toot pade.

Mahodara hathi par chadha.
Devantaka ke haath mein bhari gada thi.
Trishiras apne chamakte rath se teer chala raha tha."""
        create_image_text_layout("attached_assets/chapter6/6.70.jpg", text1, layout="side", image_position="left")

        text2 = """
        🦁 Angada ki Atal Himmat

Angada ne
ek bada sa ped ukhaada
aur Devantaka ki taraf phenka.

Trishiras ne teeron se ped kaat diya.
Par Angada ruka nahi.

Usne hathi par chadhkar
ek zor ka prahar kiya.
Mahodara ka hathi gir pada…
aur Mahodara bhi.

🔥 Devantaka ka Ant

Devantaka ne gusse mein
Hanuman par gada chalayi.

Hanuman ne pal bhar mein
apni mutthi se uska sir phod diya.
Devantaka wahi gir gaya.
Yahin uska ant ho gaya.

🌪️ Mahodara ka Vadh

Nila ne
chattan uthakar Mahodara par phenki.

Mahodara sambhal nahi paaya.
Ek bhayanak prahar laga
aur Mahodara dharti par gir pada.

⚔️ Trishiras vs Hanuman

Ab Trishiras, teen sir wala daitya,
Hanuman se bhid gaya.

Teer, ped, chattan—
sab fail ho gaye.

Hanuman ne aakhir mein
Trishiras ko pakda
aur ek hi vaar mein uske teenon sir kaat diye.

Teen sir dharti par gire.
Aakash ghoom utha.

Vanar sena ne
jai-jai ka naad kiya.

💥 Mahaparshva (Matta) ka Ant

Ab Mahaparshva, jise Matta bhi kehte the,
gusse mein aag ban gaya.

Usne Rishabha par hamla kiya.
Rishabha gir pada…
par phir uth khada hua.

Usne Matta ki hi gada chheen li
aur usi gada se Matta ko maar giraaya.

Mahaparshva ka bhi ant ho gaya.

🌸 Yuddh ka Palatna

Ek ke baad ek
daitya veer girte gaye.

Devantaka – mara
Trishiras – mara
Mahodara – mara
Mahaparshva – mara

Yeh dekhkar
Rakshas sena bhaag khadi hui.
Apne shastra chhod kar
sirf jaan bachane lagi.

Vanar sena ka hausla
aasmaan chhoone laga.

🌱 Is Adhyay ki Seekh

Gussa aur ghamand
ant mein haar laate hain

Ekjut hokar ki gayi ladai
sabse badi shakti hoti hai

Sachcha veer girta hai,
par haar maanta nahi"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.71
    with st.expander("Chapter 6.71 – Lakshmana kills Atikaya"):
        text1 = """
        Jab Atikaya ne dekha ki
uski sena haar chuki hai,
uske bhai aur chacha mare ja chuke hain,
toh uska gussa aag ban gaya 🔥.

Atikaya apne chamakte hue rath par chadha.
Uska rath sooraj jaise chamak raha tha.
Uski garaj sun kar vanar sena kaanp uthi.

Kuch vanar bole,
“Yeh toh phir se Kumbhakarna aa gaya!” 😨
Aur sab bhag kar Rama ke paas aa gaye."""
        create_image_text_layout("attached_assets/chapter6/6.71.jpg", text1, layout="side", image_position="left")

        text2 = """
        🌿 Rama ka Prashn

Rama ne shaant swar mein poocha:
“Yeh kaun sa rakshas hai,
jo pahad jaisa lagta hai aur itna tej chamak raha hai?”

Tab Bibishana bole:
“Yeh Ravana ka beta Atikaya hai.
Isse Brahma ka vardaan mila hai.
Iska kavach aam hathiyaron se tootta nahi.
Agar ise roka nahi gaya,
toh yeh vanaron ko nasht kar dega.”

⚔️ Yuddh ki Chunauti

Atikaya zor se bola:
“Main chhote sainikon se nahi ladta.
Jo samna karna chahta hai,
woh aage aaye!”

Yeh sunkar Lakshmana aage badhe.
Unki aankhon mein nidarata thi.

Atikaya hansa:
“Tum toh bachche ho.
Mere samne tik nahi paoge.”

Lakshmana shaant par dridh bole:
“Veerta umar se nahi,
karm se pehchani jaati hai.
Aaj tum apni shakti dikhao,
aur main apni.”

🔥 Bhayankar Sangharsh

Dono taraf se teer chhootne lage.
Aakash jalne laga.
Devta, Rishi, sab yeh yuddh dekh rahe the.

Lakshmana ke teer
Atikaya ke kavach se takra kar toot jaate.
Tab Vayu Dev ne kaha:
“Brahma ka vardaan hai uske paas.
Sirf Brahmastra se hi iska ant hoga.”

✨ Antim Kshan

Lakshmana ne mantr padhkar
Brahmastra chala diya.

Poora aakash kaanp utha.
Sooraj, chaand, sab tharrane lage.

Woh divya teer seedha Atikaya par gaya.
Uske saare hathiyaar bekaar ho gaye.
Aur ek pal mein—
Atikaya ka sir dharti par gir gaya.

Pahad jaisa shareer gir pada.
Rakshas sena bhay se bhag gayi.

🌸 Vijay aur Shanti

Vanar sena khushi se chilla uthi 🐒✨.
Sabne Lakshmana ko pranam kiya.

Yeh sirf ek yuddh nahi tha.
Yeh seekh thi:

Ahankar aur vardaan bhi dharm ke samne haar jaate hain.
Sachchi shakti vinamrata aur kartavya mein hoti hai.

Lakshmana ne bina ghamand ke
apna kartavya poora kiya.
Aur dharm phir jeet gaya 🌼."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.72
    with st.expander("Chapter 6.72 – Ravana makes new battle plans"):
        text1 = """
        Jab Ravana ne suna ki
Atikaya bhi
Lakshmana ke haathon maara gaya,
toh uska mann ashant ho utha 😔.

Usne man hi man socha—

“Dhumraksha, Akampana, Prahasta, Kumbhakarna…
sabhi mahaan yoddha, sabhi gir gaye.
Jo kabhi ajay lagte the,
woh bhi Rama ke saamne tik na sake.”"""
        create_image_text_layout("attached_assets/chapter6/6.72.jpg", text1, layout="side", image_position="left")

        text2 = """
        🐍 Indrajit ki Yaad

Ravana ko sirf ek baat ka sahara tha—
uska beta Indrajit.

Usne kaha:
“Indrajit ne Rama aur Lakshmana ko Nagpaash se baandh diya tha.
Woh bandhan Devta bhi nahi tod sakte the!
Par phir bhi…
woh dono mukt kaise ho gaye?
Yeh kaun si shakti hai jo mere samajh se pare hai?”

Yahan Ravana pehli baar mehsoos karta hai—
ahankar ki deewar darak rahi hai.

⚔️ Ravana ki Raksha-Yojna

Ab Ravana ko yeh samajh aa gaya tha
ki yuddh jeetna mushkil hota ja raha hai.

Isliye usne aadesh diya:

Lanka ke har dwar par pehra badha diya jaye

Ashoka Vatika, jahan Sita bandi hain,
wahan double suraksha

Raat, aadhi raat, subah—
har samay chauksi

Vanar sena ki har gati par nazar 👀

Burjon aur darwazon ko majboot kiya jaye

Rakshason ko bola gaya:
“Zara si bhi laaparvahi mat karna.
Rama ko halka mat samajhna.”

🌑 Andar ka Tootna

Aadesh dekar Ravana apne mahal mein chala gaya.
Bahari roop se woh Raja tha,
par andar—

beta mar chuka tha

bhai gir chuke the

sena toot chuki thi

Uska krodh andar hi andar jal raha tha,
par saath hi
bhay aur shok bhi tha.

“Ab yeh yuddh sirf shakti ka nahi,
bhagya ka ho gaya hai…”

🌿 Moral Soch

Is adhyay ki shiksha bahut gehri hai:

Jab ahankar tootne lagta hai,
tab manushya sirf raksha ke baare mein sochta hai,
vijay ke baare mein nahi.

Ravana ab bhi yojna bana raha hai,
par uska vishwas kamzor ho chuka hai.
Yeh adharm ke patan ka sanket hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.73
    with st.expander("Chapter 6.73 – Invisible Indrajit defeats the monkeys"):
        text1 = """
        Jab Lanka ke jo rakshas yoddha bache hue the, woh wapas laut kar
Ravana ko batate hain ki
Devantaka, Trishiras aur Atikaya sab maare ja chuke hain,
toh Ravana shok aur peeda mein doob jata hai 😔.

Uske aansu behne lagte hain —
beta, bhai, sena… sab kuch toot chuka tha."""
        create_image_text_layout("attached_assets/chapter6/6.73.jpg", text1, layout="side", image_position="left")

        text2 = """
        🔥 Indrajit ka Pratijñā

Tab aage aata hai Ravana ka sabse bhayanak putra —
Indrajit (Meghnad).

Woh garaj kar kehta hai:

“Jab tak Indrajit zinda hai, pitaji, aap shok mat kijiye!
Aaj Rama
aur Lakshmana
dono mere baanon se zameen par girenge!”

Yeh sirf ghamand nahi tha —
yeh tap, mantra aur astron se bhara hua sankalp tha.

🕯️ Gupt Yajna aur Adrishya Shakti

Yuddh mein utarne se pehle Indrajit ne gupt yajna kiya 🔥
— Agni ko ahuti, mantra, bali.

Yeh ek niyam tha:
jab tak yajna poora na ho, Indrajit adrishya (invisible) ho jata hai.

Jaise hi mantra poore hote hain:

➡️ Indrajit
➡️ uska rath
➡️ ghode
➡️ dhanush
➡️ sab kuch aankhon se gaayab

Aakash bhi kaanp uthta hai 🌌.

⚔️ Adrishya Aakraman

Ab jo hota hai woh bhayanak hai:

Vanar sena par har disha se baan

Dikhai koi nahi deta,
par maut barasti ja rahi hai ☄️

Hanuman, Sugriva, Angada, Jambavan, Nila —
sab ghayal ya behosh ho jaate hain.

Vanar cheekhte hain:

“Shatru dikhai kyun nahi deta?!”

Par koi uttar nahi.

🏹 Rama–Lakshmana bhi Ghayal

Indrajit yahin nahi rukta.

Adrishya hote hue woh
Rama aur Lakshmana par bhi
mantra-yukt baanon ki baarish kar deta hai.

Rama soch mein pad jaate hain aur Lakshmana se kehte hain:

“Yeh Brahma ki shakti ka prabhav hai.
Aaj hum ise shaant hriday se sahenge.
Jab Indrajit humein nishkriya samjhega,
tab ghamand mein laut jaayega.”

Yeh kshatriya dhairya ka shreshth udaharan hai 🙏.

🏁 Indrajit ki Asar

Vanar sena bikhar chuki

Bade yoddha behosh

Rama–Lakshmana bhi nishkriya se

Indrajit garajta hai —
aur vijayi samajhkar Lanka laut jaata hai.

Ravana ke saamne jaakar kehta hai:

“Maine sabko hara diya.”

🌑 Adhyay ki Gehri Seekh

Is adhyay ka sandesh bahut spasht hai:

Adharm jab mantra aur chhal ka sahara leta hai,
tab lagta hai jaise woh jeet raha hai —
par woh jeet asthayi hoti hai.

Indrajit ne jeeta,
par niyam todne aur adhura yajna
uske ant ka kaaran banega (aane wale adhyayon mein)."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.74
    with st.expander("Chapter 6.74 – Hanuman brings the healing mountain"):
        text1 = """
        Yuddh ke maidan mein Rama
aur Lakshmana
behosh pade the 😔.

Unhe dekhkar vanar sena ka hausla toot gaya.
Sugriva, Angada, Nila —
koi bhi samajh nahi pa raha tha kya kare.

Sab taraf khamoshi aur dard tha."""
        create_image_text_layout("attached_assets/chapter6/6.74.jpg", text1, layout="side", image_position="left")

        text2 = """
        🕊️ Bibishana ka Vishwas

Tab aage aaye Bibishana.

Unhone shaant awaaz mein kaha:

“Ghabrao mat.
Yeh Brahma ke astr ka prabhav hai.
Rama–Lakshmana ne ise sweekar kiya hai
taaki devtaon ke niyam ka maan rahe.”

Unke shabd thode sahara bane,
par ghav abhi gehre the.

🌑 Raat ka Drishya

Raat mein Hanuman
aur Bibishana battlefield mein ghoomne lage.

Zameen par:

gire hue vanar

tootey hue haath–pair

har taraf khoon 😢

Yeh drishya dil hila dene wala tha.

🐻 Jambavan ka Vishwas

Tab unki nazar padi Jambavan par.

Jambavan bahut ghayal the,
par aankhon mein abhi bhi umeed thi.

Woh bole:

“Agar Hanuman zinda hai,
toh sab kuch zinda hai!”

Yeh sunkar Hanuman aage aaye,
Jambavan ke charan chhuye 🙏.

Jambavan ke chehre par
nayi roshni aa gayi ✨.

🌿 Sanjeevani ka Rahasya

Jambavan ne Hanuman se kaha:

“Sirf tum hi sabko bacha sakte ho.
Himalaya jao.
Wahan ek parvat hai —
Sanjeevani aushadhiyon ka parvat.”

Unhone chaar jadibootiyon ke naam bataye:

Sanjeevani – jeevan lautane wali

Vishalyakarani – zehr aur baan ke ghav mitaane wali

Sandhani – haddiyan jodne wali

Suvarnakarani – shareer ko naya bal dene wali

“Inhe lekar turant wapas aao!”

🦁 Hanuman ki Udaan

Yeh sunte hi Hanuman ke sharir mein
nayi shakti bhar gayi ⚡.

Woh pahaad par chadhe —
pahaad kaanp utha!

Phir ek bhayanak garaj ke saath
Hanuman aakash mein udd gaye 🌬️.

Samundar, nadiyaan, sheher —
sab neeche chhoot gaye.

Hanuman hawa se bhi tez the.

🏔️ Parvat hi Utha Liya

Himalaya pahunch kar
Hanuman ko jadibootiyan pehchaan mein nahi aayi.

Tab unhone kaha:

“Agar pehchaan nahi ho rahi,
toh poora parvat hi le jaata hoon!”

Aur Hanuman ne
poora Sanjeevani Parvat hi utha liya 😲.

Aakash chamak utha.
Devta bhi dekh kar hairaan ho gaye.

🌸 Jeevan ki Wapsi

Hanuman jab parvat lekar wapas aaye,
vanar sena ne khushi se naare lagaye 🎉.

Jadibootiyon ki sugandh se:

Rama uthe

Lakshmana uthe

Sugriva, Angada, Jambavan

sab vanar yoddha theek ho gaye 🌼

Jo gir chuke the,
woh bhi jaag gaye —
jaise gehri neend ke baad subah ho 🌅.

🌈 Is Adhyay ki Seekh

Is kahani ki sabse badi seekh:

Umeed jab tootne lage,
tab sachha mitra aur vishwas
sabse badi shakti ban jaata hai.

Jambavan ka bharosa
aur Hanuman ka kartavya
— dono ne asambhav ko sambhav bana diya 💛."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.75
    with st.expander("Chapter 6.75 – Monkeys set Lanka on fire"):
        text1 = """
        Us raat Sugriva
ne Hanuman se kaha:

“Ab Kumbhakarna gir chuka hai.
Ravana kamzor ho gaya hai.
Samay aa gaya hai.
Lanka par chadhai karo!”

Vanar sena taiyaar ho gayi 🔥."""
        create_image_text_layout("attached_assets/chapter6/6.75.jpg", text1, layout="side", image_position="left")

        text2 = """
        🌙 Andheri Raat, Jalti Mashalein

Suraj Astachal ke peeche chhup gaya.
Raat gehri ho gayi.

Vanar mashaal le kar
Lanka ki taraf daud pade.

Jaise hi mashalein dikhi,
Rakshas pehredaar bhaag khade hue 😱.

🔥 Lanka Jal Uthi

Vanaron ne:

gate jala diye

sadkein jala di

mahal aur haveliyaan jala di

Sona, chandi, moti, heere —
sab aag mein pighalne lage.

Mehngi khushboo, reshmi kapde,
hathi–ghode, rath, hathiyaar —
sab raakh ban gaye.

Poori Lanka jalta hua samundar lag rahi thi 🌊🔥.

😨 Rakshason ka Haal

Rakshas ghabra gaye.
Koi:

bachchon ko utha kar bhaaga

koi jalte kapdon ke saath gir pada

Sundar mahal toot kar gir rahe the.
Auratoin ki cheekhein door tak goonj rahi thi.

Lanka aisi lag rahi thi
jaise pralay aa gaya ho.

🏹 Rama–Lakshmana phir taiyaar

Is beech
Rama
aur
Lakshmana
poori tarah theek ho chuke the 💪.

Rama ne apna dhanush uthaya.
Dhanush ki awaz se hi
rakshason ke dil kaanp gaye.

Ek bada gate
Rama ke baan se gir gaya.

⚔️ Sugriva ka Aadesh

Sugriva ne zor se kaha:

“Gate ke andar ghuso!
Jo peeche hatega,
woh doshi hoga!”

Vanar sena sheher ke andar ghus gayi 🦍🔥.

😡 Ravana ka Gussa

Jab Ravana ne
jalti hui Lanka dekhi,
uska gussa phoot pada.

Usne Kumbha aur Nikumbha ko
badi sena ke saath bheja.

Aakash mein:

talwaaron ki chamak

mashaalon ki roshni

nagadon ki goonj

Sab kuch bhayanak lag raha tha.

🩸 Bhayanak Yudh

Vanar aur Rakshas
aamne–saamne aa gaye.

Vanar:

ped

pathar

mukkon se waar kar rahe the

Rakshas:

talwaar

gada

bhaalon se vaar kar rahe the

Ek dusre ko girate,
phir khud gir jaate.

Har taraf shor,
har taraf yudh ⚔️.

🌟 Is Adhyay ki Seekh

Is adhyay ki sabse badi seekh:

Adharma chahe kitna bhi shaktishali ho,
jab dharma jaagta hai,
to andhkaar jal kar khatam ho jaata hai.

Lanka ka jalna
sirf aag nahi thi —
yeh anyay ke ant ka sanket tha 🔥✨."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.76
    with st.expander("Chapter 6.76 – Angada kills Kumbha"):
        text1 = """
        Yeh yuddh apni bhayanakta ke shikhar par tha.
Har taraf veer gir rahe the, dharti lahu se laal thi.

Isi beech Angada
ne aage badhkar Kumbhakarna ke putra Kumbha ko chunauti di.

⚔️ Angada ka Shaurya

Kampana ne pehle Angada par prahar kiya

Angada sambhla aur chattan utha kar Kampana ko maar giraya

Fir:

Shonitaksha ne aag jaise baan chalaye

Angada ne uska dhanush tod diya

Talwaar se yuddh hua — Angada ne Shonitaksha ka kandha kaat diya

Angada akela hi andhi toofan ban gaya 🔥."""
        create_image_text_layout("attached_assets/chapter6/6.76.jpg", text1, layout="side", image_position="left")

        text2 = """
        🦍 Vanar veeron ka saath

Jab Angada teen rakshason se ghir gaya:

Mainda

Dvivida

uski madad ko aaye.

Bhayankar sangharsh hua:

Prajangha ka sir Angada ne alag kar diya

Yupaksha ko Mainda ne maar giraya

Shonitaksha ko Dvivida ne kuchal diya

Rakshas sena himmat haarne lagi 😨.

🏹 Kumbha ka Pravesh

Tab Kumbha swayam aage aaya —
dhanush kheench kar bijli jaise baan chalaye.

Dvivida gir pada

Mainda behosh ho gaya

Angada ke palak kaat diye gaye

Khoon behte hue bhi Angada ne:

Saala vriksh ukhaad kar phenka

Par Kumbha ne sab kaat diya.

Ant mein Angada behosh ho kar gir pada.

🦁 Rama ka Aadesh – Sugriva ka Pravesh

Jab Rama
ne Angada ke girne ka samachar suna,
unhone Jambavan aur vanar senapatiyon ko bheja.

Ant mein swayam
Sugriva
yuddh mein utre 💪.

🤼 Sugriva vs Kumbha – Dev aur Asur samaan yuddh

Sugriva ne:

Kumbha ka dhanush tod diya

Uski veerta ki khul kar prashansa ki
(yeh kshatriya maryada thi)

Fir dono:

Haathi jaise takraaye

Samundar mein gir gaye

Dharti kaanp uthi 🌍

Kumbha ne Sugriva ke vaksh par bijli jaisa ghunsa mara
Par Sugriva ne bhi vajra samaan mukka chalaya ⚡.

💥 Kumbha ka Ant

Sugriva ke ek prachand prahar se:

Kumbha ka seena choor ho gaya

Woh jalti hui ulka jaise dharti par gira

Kumbha maara gaya.

Dharti, parvat aur van kaanp uthe.
Rakshason par bhay chhaa gaya 😱.

🌟 Is Adhyay ki Seekh

Bal aur ghamand bina dharm ke tik nahi sakte.
Ekjut vanar sena aur sahi netritva ne
Kumbhakarna ke putra ko bhi gira diya.

Angada = veerata + sahansheelta
Sugriva = netritva + maryada

Yahi dharm ki jeet hai ✨."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.77
    with st.expander("Chapter 6.77 – Hanuman fights Nikumbha"):
        text1 = """
        Jab Kumbha mara gaya,
toh Nikumbha ka gussa aag ban gaya 🔥.

Usne Sugriva ko aise dekha
jaise aankhon se hi jala dega.

🏹 Nikumbha ka Bhayanak Roop

Nikumbha ne:

Apni bhari gada uthai

Jo Mahendra Parvat jaisi badi thi

Jo Yamraj ke dand jaise lag rahi thi

Uski gada ghoomi toh:

Aasmaan ghoomne laga

Taare kaanp gaye

Rakshas aur vanar jam gaye 😨

Nikumbha pralay ki aag jaisa tha."""
        create_image_text_layout("attached_assets/chapter6/6.77.jpg", text1, layout="side", image_position="left")

        text2 = """
        🦍 Hanuman ka Nirbhay Stand

Par Hanuman
bilkul shaant khade rahe.

Na dar.
Na peeche hatna.

Nikumbha ne poori taakat se:

Hanuman ke seene par gada maari

💥
Gada sau tukdon mein toot gayi.

Par Hanuman?
➡️ Pahaad jaise atale rahe.

👊 Bal ka Jawab Bal se

Hanuman ne:

Apni mutthi ghumayi

Aur Nikumbha ke seene par prahar kiya

Nikumbha ka:

Kavach toot gaya

Khoon bijli jaisa baha ⚡

Nikumbha ladkhadaya
par phir Hanuman ko pakadne dauda.

🤼 Antim Sangharsh

Nikumbha ne Hanuman ko uthaya,
Lanka ke log khushi se chillaye.

Par Hanuman ne:

Phir se mukka maara

Pakad se chut gaye

Aur zor se Nikumbha ko zameen par patka

Fir:

Upar se kood kar uske seene par gire

Gardan pakdi

Aur uska sir alag kar diya ⚔️

Yuddh wahi samapt ho gaya.

🌍 Yuddh ka Parinaam

Nikumbha ke girte hi:

Vanar sena ne jai-jaikaar ki

Dharti kaanp uthi

Aasmaan goonj gaya

Rakshas sena:
➡️ bhay se bhar gayi 😱.

🌟 Is Adhyay ki Seekh

Ghamand chahe kitna bhi bada ho,
sachchi shakti aur dhairya ke aage gir jaata hai.

Hanuman ne sikhaya:

Dar ke bina khade rehna

Aur dharm ke liye ladna
hi sachchi veerta hai 💛."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.78
    with st.expander("Chapter 6.78 – Maharaksha attacks Rama and Lakshmana"):
        text1 = """
        Nikumbha aur Kumbha ke mare jaane ke baad,
Ravana
ka krodh jalti hui agni jaisa ho gaya 🔥.

Dukh aur gusse mein dooba hua Ravana
apni drishti Khara ke putra Maharaksha par daalta hai.

🗣️ Ravana ka Aadesh

Ravana garaj kar bola:

“Jaao, mere putra!
Rama
aur Lakshmana
ko vanaron sahit nasht kar do!”"""
        create_image_text_layout("attached_assets/chapter6/6.78.jpg", text1, layout="side", image_position="left")

        text2 = """
        ⚔️ Maharaksha ka Pratigya

Maharaksha,
jo apni veerta par garv karta tha,
bina hichkichahat bola:

“Aadesh shirodharya hai.
Main avashya un dono ko yuddh mein gira dunga!”

Usne Ravana ki parikrama ki,
aur turant yuddh ke liye nikal pada.

🛞 Yuddh ki Taiyari

Maharaksha ne:

Apna rath bulwaya

Sena ko turant ikattha kiya

Rath ki pooja karke charioteer se kaha:
“Aage badho!”

Fir usne sena ko lalkaar kar kaha:

“Aaj mere baan
Rama–Lakshmana ko girayenge!
Aaj meri gada se
vanar sena sookhe lakdi ki tarah jalegi!”

👹 Rakshas Sena ka Garjan

Rakshas:

Bhayanak roop dharan kar sakte the

Teekhe nakhun, laal aankhen

Haathi jaise garaj

Aasmaan ko cheer dene wali cheekh

Shankh, nagade, drum
hazaaron dishaon mein goonj uthe 🌩️.

⚠️ Apashakun (Bad Omens)

Jab Maharaksha aage badha:

Saarthi ke haath se ankush gir gaya

Rath ka dhwaj gir pada

Ghode aansoo bahane lage

Tez aur kathor dhool ka aandhi uthi 🌪️

⚠️ Yeh sab ashubh sanket the.

Par…

🔥 Ghamand ki Andhi

Maharaksha aur rakshas sena ne:

In sanketon ko nazaraandaz kiya

Apni shakti aur ghamand par bharosa kiya

Yuddh-bhoomi ki taraf badh gaye

Aur lalkaarne lage:

“Yahan hoon! Yahan hoon!”

🌟 Is Adhyay ki Seekh

Jab buddhi par ghamand haavi ho jaaye,
toh ashubh sanket bhi andekhe ho jaate hain.

Maharaksha ki veerta thi,
par ahankar ne vivek ko dhak diya."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.79
    with st.expander("Chapter 6.79 – Rama kills Maharaksha"):
        text1 = """
        Jaise hi Maharaksha yuddh-bhoomi mein aaya,
sabhi vanar yoddha aage badhe.
Unke dil mein aag thi.
Aur yahan se bhayanak yuddh shuru ho gaya 🔥.

⚔️ Bhayanak Sangharsh

Vanar aur rakshas:

Ped, pathar, talwaar se lade

Gada aur bhale takraaye

Aasmaan aur dharti goonj uthi

Maharaksha ke teer bahut tez the.
Unki baarish se kai vanar ghabra kar bhaag gaye.

Rakshas garajne lage.
Unhe laga jeet unki hai."""
        create_image_text_layout("attached_assets/chapter6/6.79.jpg", text1, layout="side", image_position="left")

        text2 = """
        🏹 Rama ka Aagman

Tab Rama aage aaye.
Unhone shant mann se
rakshason par teeron ki varsha ki.

Maharaksha ka gussa aag ban gaya 🔥.

🗣️ Maharaksha ki Lalkaar

Maharaksha garja:

“Rama!
Aaj main apne pita Khara ka badla lunga!
Aaj tum mere teeron se maroge!”

Uski aankhon mein ghamand tha.
Dil mein sirf badla.

🧠 Rama ka Uttar

Rama muskuraye 🙂 aur bole:

“Yuddh shabdon se nahi,
karma se jeeta jaata hai.
Dandakaranya mein tumhare pita gire the.
Aaj tumhari baari hai!”

⚡ Maha Yuddh

Dono taraf se:

Teer toot rahe the

Aasmaan bhar gaya

Devta upar se yeh yuddh dekh rahe the

Ant mein Rama ne:

Maharaksha ka dhanush tod diya

Rath, saarathi aur ghode gir gaye

Maharaksha zameen par khada raha.
Usne Shiv-datta bhala uthaya.

🔥 Aakhri Prayas

Us bhale se aag nikal rahi thi.
Devta bhi ghabra gaye 😨.

Maharaksha ne poori taakat se
bhala Rama ki taraf phenka.

🌟 Dharma ki Vijay

Rama ne sirf chaar teeron se
us bhale ko beech hawa mein tod diya ✨.

Fir Rama ne
Agni-astra uthaya.

Ek hi teer…
aur Maharaksha gir pada.

🏆 Ant

Maharaksha ka ghamand
usi ke saath samapt ho gaya.

Rakshas dar ke maare
Lanka ki taraf bhaag gaye.

Devtaon ne aakash se kaha:

“Sadhu! Sadhu!”

🌼 Is Adhyay ki Seekh

Ghamand aur badle se andha vyakti
kabhi jeet nahi paata.
Dharma, shanti aur satya
hamesha vijayi hote hain 🌿.
"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.80
    with st.expander("Chapter 6.80 – Indrajit returns to battle"):
        text1 = """
        Maharaksha ki mrityu sunte hi Ravana ka krodh aag ki tarah bhadak utha 🔥.
Daant peeste hue usne socha—
ab kaun Rama ko rokega?

Uska bharosa sirf ek par tha —
apne putra Indrajita par.

🔥 Ravana ka Aadesh

Ravana bola:

“Tumne pehle hi Rama–Lakshmana ko bandh diya tha.
Tum drishya ho ya adrishya—
tum sabse shreshth ho!
Jaao aur is baar poori vijay lekar aao!”

Indrajita ne bina sankoch aagya maan li."""
        create_image_text_layout("attached_assets/chapter6/6.80.jpg", text1, layout="side", image_position="left")

        text2 = """
        🕯️ Yagya aur Shakti

Indrajita gaya Agni-yagya ke liye.

Pavaka ko bali di

Mantron ka uchcharan hua

Vijay ke shubh lakshan dikhe ✨

Fir usne:

Adrishya rath prapt kiya

Brahma ki shakti ka kavach paya

Ab woh roka nahi ja sakta tha.

☁️ Adrishya Aakraman

Yuddh-bhoomi mein pahunchkar
Indrajita adrishya ho gaya 😶‍🌫️.

Aasmaan:

Andhera

Dhuaan

Dishaen gum

Na rath dikha,
na ghode,
na dhanush ki dhvani.

Bas…
teeron ki varsha ☄️☄️☄️

🏹 Rama–Lakshmana Par Prahar

Adrishya Indrajita ne
Rama aur
Lakshmana
par Narachon ki baarish kar di.

Dono bhai:

Ghaayal hue

Phir bhi sthir rahe

Unhone bhi divya astra chalaye
par dushman abhi bhi adrishya tha.

🐒 Vanar Sena ka Haal

Adrishya teeron se:

Sau-sau vanar gir pade

Bhoomi lahu se rang gayi

Lakshmana ka krodh bhadka 🔥
aur unhone kaha:

“Bhaiya!
Kya main Brahmastra chala doon?”

🧘 Rama ka Dharma

Rama ne shant swar mein kaha:

“Nahi Lakshmana.
Dharma humein roakta hai.
Chhupe hue ya bhaagte shatru par
divya astra ka prayog uchit nahi.”

Fir Rama bole:

“Indrajita chahe
swarg, narak ya aakash mein chhup jaaye—
mere teer use dhoondh hi lenge.
Uska ant nishchit hai.”

🌿 Is Adhyay ki Seekh

Asur chaal se ladta hai,
par dharm bal se jeetata hai.
Rama ne aaj bhi
maryada aur nyay ka marg chuna 🙏."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.81
    with st.expander("Chapter 6.81 – Indrajit tricks the army with illusion"):
        text1 = """
        Chapter 81 – Indrajit ki Chaal aur Jhoothi Sita

Indrajit samajh gaya ki Rama ka iraada kya hai.
Woh ladayi chhod kar shehar ke andar chala gaya.
Uske mann mein gussa bhara tha.
Uski aankhen laal ho chuki thi.

Thodi der baad Indrajit phir nikla.
Is baar woh pashchim gate se aaya.
Uske saath bhayanak rakshas the.
Saamne Rama aur Lakshmana yuddh ke liye taiyaar khade the."""
        create_image_text_layout("attached_assets/chapter6/6.81.jpg", text1, layout="side", image_position="left")

        text2 = """
        Indrajit ne ek gandi chaal sochi.
Usne apni maya ka upyog kiya.
Usne rath par Sita ki jhoothi tasveer bana di.
Aur dikhaya jaise woh use maarne wala ho.

Yeh sab vanaron ko dhokha dene ke liye tha.
Vanar gusse se bhar gaye.
Sab patthar utha kar daud pade.
Unke aage Hanuman the.
Hanuman ke haath mein ek bada pahad tha.

Hanuman ne rath par Sita ko dekha.
Woh dukhi lag rahi thi.
Sirf ek choti thi.
Kapde mailay the.
Sharir par mitti lagi thi.

Hanuman kuch pal ke liye sunn ho gaya.
Abhi thodi der pehle hi usne asli Sita ko dekha tha.
Uske mann mein sawaal aaya,
“Yeh rakshas kya karne ja raha hai?”

Tab Indrajit ne talwaar nikali.
Usne sabke saamne Sita par talwaar uthayi.
Jhoothi Sita cheekhi,
“Ram! Ram!”

Hanuman ka dil toot gaya.
Uski aankhon se aansu gir pade.
Uska gussa aag ban gaya.

Hanuman garja,
“Paapi!
Auraton par haath uthana maha-paap hai.
Tu is paap se bach nahi payega.
Sita ko chhu kar tune apna ant likh diya hai.”

Itna keh kar Hanuman aur vanar sena toot pade.
Rakshas bhi teer chalane lage.
Yuddh aur bhayanak ho gaya.

Indrajit hansa.
Usne phir se talwaar uthayi.
Aur us jhoothi Sita ko kaat diya.
Woh chillata hua bola,
“Dekho! Ram ki Sita mar gayi!”

Vanar sena yeh dekh kar kaanp uthi.
Unke mann mein dukh aur bhay bhar gaya.
Woh sochne lage sab kuch khatam ho gaya.

Par yeh sirf maya thi.
Sach abhi baaki tha.
Dharma ki jeet abhi door nahi thi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.82
    with st.expander("Chapter 6.82 – Hanuman rallies the monkeys"):
        text1 = """
        Chapter 82 – Hanuman ne Vanar Sena ko Sambhala, Indrajit ka Yagya

Indrajit ki bhayanak garaj sun kar vanar darr gaye.
Uski awaaz Indra ke baadal jaisi thi.
Sab vanar idhar-udhar bhaagne lage.

Tab Hanuman, jo Vayu putra the, zor se bole.
Unhone bhaagte hue vanaron ko roka.

Hanuman ne kaha,
“Tum sab kyun bhaag rahe ho?
Tumhara veerta kahan gaya?
Dushman se peeth mat dikhao.
Mere saath yuddh mein aao!”"""
        create_image_text_layout("attached_assets/chapter6/6.82.jpg", text1, layout="side", image_position="left")

        text2 = """
        Hanuman ki baat sun kar vanaron ka mann majboot ho gaya.
Unhone patthar aur ped uthaye.
Gusse se bhare hue rakshason par toot pade.

Hanuman beech mein the.
Unke charon taraf shresht vanar the.
Jaise suraj apni roshni se andhera mita deta hai,
waise hi Hanuman ne shatru sena ko hila diya.

Hanuman ka roop kaal jaisa lag raha tha.
Dukh aur krodh se bhare hue,
unhone ek bada patthar Indrajit ke rath par phenka.

Rath ke saarathi ne turant rath mod diya.
Indrajit bach gaya.
Patthar zameen mein dhans gaya.

Ab vanar sena aur zor se garji.
Sau-sau vanar aage badhe.
Ped, chattan aur pahad uthane lage.
Indrajit par pattharon ki baarish hone lagi.

Rakshas sena bikharne lagi.
Kai rakshas pedon ke neeche dab gaye.
Yuddh aur bhi bhayanak ho gaya.

Apni sena ko pitta dekh kar Indrajit gusse se bhadak utha.
Usne teeron ki varsha kar di.
Kai veer vanar gir pade.

Par vanar bhi kamzor nahi the.
Unhone bhale, talwaar aur gadayein chalayi.
Hanuman ne bade-bade vriksh utha kar rakshason ko kuchal diya.

Ant mein rakshas peeche hat gaye.
Tab Hanuman ne apni sena se kaha,
“Humne Ram ke liye apni jaan daav par laga di.
Par jinke liye hum yuddh kar rahe the,
woh Sita ab nahi rahi.”

Vanaron ka mann bhaari ho gaya.
Hanuman ne kaha,
“Hum yeh baat Rama aur Sugriva ko batayenge.
Phir jo aadesh milega, wahi karenge.”

Yeh keh kar Hanuman dheere-dheere sena ko le kar laut aaye.

Udhar Indrajit ne dekha ki Hanuman wapas ja rahe hain.
Usne ek aur chaal sochi.
Woh Nikumbhila ke yagya sthal par gaya.

Wahan usne Agni ko ahvaan kiya.
Havan mein ahuti di.
Aag tez jalne lagi.
Agni dev santusht ho gaye.

Indrajit ne rakshason ki vijay ke liye prarthana ki.
Sab rakshas shant khade dekhte rahe.

Yuddh ab ruk gaya tha.
Par toofan abhi baaki tha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.83
    with st.expander("Chapter 6.83 – Lakshmana speaks bravely"):
        text1 = """
        Chapter 83 – Lakshman ka Kathor Vichaar

Us bhayanak yuddh ke shor ko sun kar Rama ne Jambavan se kaha,
“Dost, yeh shor bata raha hai ki Hanuman bahut kathin yuddh kar rahe hain.
Tum apni sena ke saath jao aur unki madad karo.”

Jambavan bole, “Aisa hi hoga.”
Woh bhaluon ki sena ke saath pashchim gate ki taraf chale.

Wahan unhone dekha ki Hanuman laut rahe hain.
Vanar dukhi the.
Unki aankhon mein aansu the.
Unhone yuddh chhod diya tha.

Hanuman ne bhaluon ko rok diya.
Phir sab ke saath tez kadmon se Rama ke paas aaye.
Unka mann bahut bhaari tha."""
        create_image_text_layout("attached_assets/chapter6/6.83.jpg", text1, layout="side", image_position="left")

        text2 = """
        Hanuman ne dukhi swar mein kaha,
“Yuddh ke dauraan, hamari aankhon ke saamne,
Indrajit ne roti hui Sita ko maar diya.
Yeh dekh kar mera mann toot gaya.
Isi liye main yeh sandesh dene aaya hoon.”

Yeh sunte hi Rama dharti par gir pade.
Jaise jad se kata ped gir jata hai.
Unka dukh agni ki tarah bhadak utha.

Sab vanar neta daud kar aaye.
Unhone kamal ki sugandh wala paani Rama par chhidka.
Par unka shok kam nahi hua.

Tab Lakshmana ne Rama ko apni baahon mein bhar liya.
Unki aankhon mein peeda aur gussa tha.
Unhone gehri baat kehni shuru ki.

Lakshman bole,
“Bhaiya, aap dharma ke raaste par chalte ho.
Phir bhi aapko itna dukh kyun milta hai?
Mujhe lagta hai dharma dikhai hi nahi deta.
Agar dharma hota, to aap jaise satpurush ko yeh dukh nahi milta.”

“Yadi adharma sach mein bura hota,
to Ravana kab ka nasht ho chuka hota.
Par dukh hamesha achchon ko hi kyun milta hai?”

Lakshman ka swar aur kathor ho gaya.
“Jo shaktiwaan hai, wahi jeet raha hai.
Jo dharmic hai, wahi peedit ho raha hai.
Isse lagta hai jaise dharma kamzor ho.”

Unhone kaha,
“Raj chhodna galat nirnay tha.
Dhan se hi shakti aati hai.
Dhan se hi mitra, samman aur bal milta hai.
Garib aadmi ke sapne bhi sookh jaate hain.”

Lakshman ne aage kaha,
“Jab aap vanvaas mein the,
tab ek rakshas aapki priya ko le gaya.
Yeh sab is tyag ka phal hai.”

Phir unka swar badal gaya.
Ab usme veerta thi.

Lakshman bole,
“Par bhaiya, uthiye.
Main hoon na.
Indrajit ne jo dukh diya hai,
main use apni shakti se mita dunga.”

“Janak ki putri ki mrityu ka samachar
mere khoon ko jala raha hai.
Main apne baanon se poori Lanka hila dunga.
Rath, ghode, rakshas aur uska raja—
sab ka vinash kar dunga!”

Lakshman ki aankhon mein agni thi.
Aur unke shabd yuddh ka sanket ban chuke the."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.84
    with st.expander("Chapter 6.84 – Vibhishana comforts Rama"):
        text1 = """
        Chapter 84 – Bibishan ne Rama ko Sambhala

Jab Lakshmana apne bhai ko sambhaal rahe the,
tab Bibishana wahan aaye.
Woh sena ko sambhaal kar aa rahe the.
Unke saath chaar veer rakshas the.

Bibishan ne dekha ki Rama gehre dukh mein doobe hue hain.
Vanaron ki aankhon mein aansu the.
Sabka mann bhaari tha.

Bibishan ka dil bhi dukhi ho gaya.
Unhone poocha,
“Yeh sab kya ho gaya?”"""
        create_image_text_layout("attached_assets/chapter6/6.84.jpg", text1, layout="side", image_position="left")

        text2 = """
        Tab Lakshman bole,
“Indrajit ne Sita ko maar diya!
Hanuman ne khud yeh baat batayi.
Isliye Rama shok mein doob gaye hain.”

Yeh sunte hi Bibishan ne baat kaat di.
Unhone shaant swar mein Rama se kaha,
“Hey purushon mein shreshth,
yeh baat utni hi asambhav hai
jitni samundar ka sookh jana.”

“Main Ravana ko achhi tarah jaanta hoon.
Woh kabhi bhi Sita ko nuksaan pahunchane nahi dega.
Maine usse kai baar samjhaya tha.
Par na vinati se, na dhamki se,
na hi kisi chaal se koi Sita ke paas pahunch saka.”

Bibishan ne aage kaha,
“Indrajit ne yeh sab vanaron ko darane ke liye kiya.
Woh Sita sirf maya thi.
Sachchi Sita surakshit hain.”

Phir Bibishan bole,
“Aaj Indrajit Nikumbhila mein yagya karne ja raha hai.
Agar usne yagya poora kar liya,
to woh devtaon se bhi ajey ho jayega.”

“Isliye der mat kijiye.
Aapka dukh poori sena ko kamzor kar raha hai.
Uthiye, apna sahas yaad kijiye.”

Bibishan ne dridhata se kaha,
“Lakshman ko aadesh dijiye.
Unke teekhe baan Indrajit ke yagya ko tod denge.
Jaise Indra apna vajra chhodta hai,
waise hi Lakshman Indrajit par toot padein.”

“Shatru ko maarne mein vilamb theek nahi.
Abhi ka samay sahi hai.
Lakshman ko jaane dijiye.
Yahi dharma hai.
Yahi sahi raasta hai.”

Bibishan ke shabd
Rama ke mann mein roshni ban kar utre.
Andhera dheere-dheere chhatne laga."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.85
    with st.expander("Chapter 6.85 – Lakshmana goes to fight Indrajit"):
        text1 = """
        Chapter 85 – Lakshman Nikumbhila Van ki Ore

Bibishan ki baat sunkar bhi Rama abhi poori tarah sambhal nahi paaye the.
Dukh unke mann par bhaari tha.
Thodi der baad unhone himmat jutaayi.

Rama ne Bibishana se kaha,
“Tumne jo kaha, use phir se batao.
Main sab kuch saaf-saaf sunna chahta hoon.”

Bibishan ne shant swar mein dobara kaha,
“Senayein tayaar hain.
Sab apni jagah par khade hain.
Par jab tak aap shok mein doobe rahenge,
tab tak sabka hausla tootega.”"""
        create_image_text_layout("attached_assets/chapter6/6.85.jpg", text1, layout="side", image_position="left")

        text2 = """
        Unhone aage kaha,
“Indrajit Nikumbhila van mein yagya kar raha hai.
Agar yagya poora ho gaya,
to woh ajey ho jayega.
Tab hum sab haar jayenge.”

Bibishan bole,
“Isliye Lakshmana ko turant bhejiye.
Unke baan zehrele saanp jaise honge.
Yagya todna hi Indrajit ka ant hai.”

Rama ne gambhir swar mein kaha,
“Main Indrajit ki maya ko jaanta hoon.
Woh aakash mein rath se ghoomta hai.
Uski gati badalon mein chhupe suraj jaisi hai.
Par ab der nahi ho sakti.”

Rama ne Lakshman ki taraf dekha.
Unki aankhon mein vishwas tha.
Unhone kaha,
“Lakshman,
vanar sena ke saath jao.
Hanuman tumhare saath honge.
Bhaluon ki sena aur Jambavan bhi saath jayenge.”

“Indrajit ko wahi roko.
Uski maya ko wahi tod do.”

Lakshman ka chehra tej se chamak utha.
Unhone apna divya dhanush uthaya.
Kavach pehna.
Talwar aur baan sambhale.

Lakshman bole,
“Aaj mere baan
Lanka ko hila denge.
Indrajit aaj nahi bachega.”

Yeh keh kar unhone Rama ke charan chhuye.
Teen baar parikrama ki.
Aur tez kadmon se nikal pade.

Unke saath Bibishan the.
Angada aur Vayu putra Hanuman bhi the.
Vanar sena samundar ki tarah unke peeche umad padi.

Raaste mein bhaluon ki sena mili.
Sab yuddh ke liye tayaar the.

Aage jaakar Lakshman ne dekha—
rakshas sena tayaar khadi hai.
Chamakte hathiyaar.
Rathon ki lambi panktiyan.

Lakshman ne dhanush kas liya.
Unka mann dridh tha.
Aaj dharma ka kaam unke haath mein tha.

Aur veer Lakshman
andhere mein pravesh karte hue
bhayanak shatru sena ke beech ghus gaye."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.86
    with st.expander("Chapter 6.86 – Indrajit stops his ritual to fight"):
        text1 = """
        Chapter 86 – Indrajit ne Yagya Todega, Lakshman se Yuddh

Us samay Bibishana ne Lakshmana ko sahi salah di.
Yeh salah Lakshman ke liye laabhdayak thi.
Aur rakshason ke liye vinashkari.

Bibishan bole,
“Lakshman,
patthar aur ped lekar vanar sena ko aage bhejo.
Rakshas sena ka ghera todo.
Jaise hi pankti tootegi,
Indrajit khud saamne aa jayega.”

“Der mat karo.
Apne baan chalao.
Yagya poora hone se pehle
Indrajit ko yuddh ke liye majboor karo.”"""
        create_image_text_layout("attached_assets/chapter6/6.86.jpg", text1, layout="side", image_position="left")

        text2 = """
        Bibishan ki baat sun kar Lakshman ne turant baan chhod diye.
Teer Indra ke vajra jaise girne lage.

Bhalu aur vanar ek saath aage badhe.
Unhone bade-bade ped utha liye.
Rakshas sena bhi talwaar, bhale aur teer lekar toot padi.

Yuddh bhayanak ho gaya.
Aakash andhera pad gaya.
Ped, chattan aur teer hawa mein udne lage.
Zameen kaanp uthi.

Rakshas darawane chehron ke saath vaar kar rahe the.
Vanar bhi poori shakti se jawab de rahe the.
Kai rakshas pedon ke neeche kuchle gaye.

Jab Indrajit ne dekha
ki uski sena haar rahi hai,
toh uska gussa phoot pada.

Uska yagya abhi poora nahi hua tha.
Phir bhi woh Nikumbhila van chhod kar
turant apne rath par chadh gaya.

Laal aankhen.
Haath mein dhanush.
Woh Mrityu jaise bhayanak lag raha tha.

Yeh dekh kar Hanuman aage badhe.
Unhone ek bahut bada ped ukhaad liya.
Aur rakshason par barsa diya.

Rakshas behosh hote gaye.
Zameen laashen se bhar gayi.

Ab hazaron rakshas Hanuman par toot pade.
Talwaar, bhale, gada, lohe ke dande—
sab kuch chalaya gaya.

Par Hanuman pahad jaise atal khade rahe.
Unka krodh aur bhi badh gaya.
Unhone bhayanak sanhaar macha diya.

Indrajit ne dekha
ki Hanuman akela hi sab kuchal raha hai.
Usne apne saarathi se kaha,
“Rath udhar le chalo.
Agar is vanar ko nahi roka,
toh sab rakshas nasht ho jayenge!”

Rath Hanuman ki taraf badha.
Indrajit ne teer, talwaar aur bhale chalaye.

Hanuman aur bhadak uthe.
Unhone garaj kar kaha,
“Hey Ravana ke putra!
Agar veer hai,
toh saamne aa kar
haathon se yuddh kar!”

Isi samay Bibishan ne Lakshman ko sanket diya.
Unhone kaha,
“Dekho, wahi Indrajit hai.
Woh Hanuman ko maarna chahta hai.”

“Lakshman!
Apne shreshth baan chalao.
Isi samay is rakshas ka ant karo!”

Lakshman ne dhanush uthaya.
Unki aankhon mein tej tha.
Saamne Indrajit khada tha—
ajey, ghamandi, aur bhayanak.

Aur yahin se
do maha veeron ka
saamna hone wala tha…"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.87
    with st.expander("Chapter 6.87 – Indrajit and Vibhishana argue"):
        text1 = """
        Chapter 87 – Indrajit aur Bibishan ka Aamne-Saamne Virodh

Yeh keh kar Bibishana khush ho gaye.
Woh Lakshmana ko saath lekar tez chal pade.
Thodi door jaakar woh ek gehre jungle mein pahunche.

Bibishan ne Lakshman ko ek jagah dikhayi.
Wahin Indrajit yagya karta tha.
Wahan ek bahut bada Nyagrodha (Banyan) ka ped khada tha.
Woh kaale baadal jaisa bhayanak lag raha tha."""
        create_image_text_layout("attached_assets/chapter6/6.87.jpg", text1, layout="side", image_position="left")

        text2 = """
        Bibishan bole,
“Yahin Ravana ka putra balidan deta hai.
Yahin se woh yuddh ke liye nikalta hai.
Woh adrishya ho jata hai
aur teekhe baanon se shatru ko nishkriya kar deta hai.”

“Isse pehle ki woh is ped tak pahunche,
tum apne jalte teeron se
uska rath, ghode aur saarathi tod dena.”

Lakshman bole,
“Bilkul aisa hi hoga.”
Unhone apna adbhut dhanush kas liya.

Tab achanak Indrajit saamne aaya.
Woh rath par tha.
Kavach pehne hue.
Talwaar aur dhwaj chamak rahe the.
Aag jaise tej ke saath woh aage badha.

Lakshman ne lalkaar lagayi,
“Indrajit!
Mujhse seedha yuddh karo.
Saamne aa kar ladho!”

Indrajit ne yeh suna.
Uski nazar Bibishan par padi.
Uska gussa phoot pada.

Indrajit chillaya,
“Tum mere pita ke bhai ho!
Isi vansh mein paida hue.
Phir mere pita ke shatru ka saath kyun de rahe ho?”

“Tumne apna dharma chhod diya.
Apni jaati ko chhod diya.
Dushman ke paas jaakar khade ho gaye.
Khoon ka rishta hamesha rishta hota hai.
Paraye kabhi apne nahi hote!”

“Jo apno ko chhod deta hai,
woh aakhir nasht ho jata hai.
Tum jaise log hi apne vansh ka kalank hote ho!”

Yeh sun kar Bibishan shaant rahe.
Phir gambhir awaaz mein bole,
“Indrajit,
tum mujhe nahi jaante.”

“Main rakshas vansh mein paida hua hoon,
par mere siddhant manushyon jaise hain.
Main anyaay aur kroorta ko sweekaar nahi karta.”

“Jo bhai adharm par chal pade,
usse chhod dena hi dharma hota hai.
Jaise haath par baitha saanp jhaad diya jata hai.”

Bibishan ne aage kaha,
“Paraye dhan par nazar,
parayi patni par lalach,
aur mitron par avishwas—
yeh teen gunaah vinash laate hain.”

“Tumhare pita Ravana mein
ahankaar, krodh aur anyaay bhara hai.
Isi wajah se Lanka ka ant nazdeek hai.”

Bibishan ki awaaz kathor ho gayi.
“Tum, tumhara pita aur tumhari sena—
sab mrityu ke jaal mein bandhe ho.”

“Ab tum is Nyagrodha ped tak
kabhi nahi pahunch paoge.
Tumne Rama ka apmaan kiya hai.
Iska daam tumhe chukana hoga.”

“Ab yuddh karo!
Apni poori shakti dikhao.
Par yaad rakhna—
agar Lakshman ke baanon ki seema mein aaye,
toh tum aur tumhari sena
zinda nahi bachegi!”

Hawa bhaari ho gayi.
Do paksh saamne the.
Shabd khatam ho chuke the.
Ab sirf yuddh baaki tha…"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.88
    with st.expander("Chapter 6.88 – Lakshmana and Indrajit fight"):
        text1 = """
        Chapter 88 – Lakshman aur Indrajit ka Mahayuddh

Bibishan ke shabdon ko sun kar Indrajit gusse se jal utha.
Usne aur kadve shabd kahe.
Aur poore krodh ke saath aage badha.

Woh kaale ghodon se jude rath par khada tha.
Haath mein talwaar aur bhayanak dhanush.
Uska roop Mrityu jaisa lag raha tha.

Uske saamne Lakshmana prakat hue.
Woh Hanuman ki peeth par baithe the.
Unka tej ubharte suraj jaisa tha."""
        create_image_text_layout("attached_assets/chapter6/6.88.jpg", text1, layout="side", image_position="left")

        text2 = """
        Indrajit zor se garja,
“Dekho meri shakti!
Mere baan baadalon ki baarish jaise girenge.
Tum sab ko aaj Yama lok bhej dunga!”

“Pehle bhi maine tum dono bhaiyon ko
raat ke yuddh mein behosh kar diya tha.
Kya tum bhool gaye ho?”

Lakshman ne shant par kathor awaaz mein kaha,
“Sirf bolna veerta nahi hota.
Jo kaam kar dikhaye, wahi veer hota hai.”

“Chhup kar ladna kayaron ka kaam hai.
Agar veer ho,
toh saamne aa kar ladho.
Baaton se kuch nahi hota.”

Yeh sun kar Indrajit ne dhanush khinch liya.
Tez teer zehrele saanpon jaise chhoot pade.
Lakshman ka sharir baanon se chhalni ho gaya.
Khoon behne laga.

Par Lakshman gire nahi.
Woh bina dhuen ki agni jaise chamak rahe the.

Indrajit hansa aur bola,
“Aaj jungle ke jaanwar
tumhare sharir par mandrayenge.
Rama dekhega
apne bhai ko girte hue!”

Lakshman ne dhairya se uttar diya,
“Khali ghamand se kuch nahi hota.
Ab dekhna,
main bina shor ke
tumhara ant kaise karta hoon.”

Yeh keh kar Lakshman ne dhanush kaan tak kheench liya.
Unhone paanch shaktishaali baan chhode.
Teer Indrajit ke seene mein ja lage.
Suraj ki kirnon jaise chamak uthe.

Gusse se bhara Indrajit ne bhi teen baan chhode.
Lakshman phir ghaayal hue.
Par unka sankalp nahi toota.

Ab yuddh aur bhayanak ho gaya.
Dono veer ek doosre par
teeron ki baarish kar rahe the.

Koi kisi se kam nahi tha.
Dono mein apar shakti thi.
Dono atoot veer the.

Aisa lag raha tha
jaise aakash mein do grah takra rahe ho.
Ya jaise do sher
ek jagah jam kar lad rahe ho.

Shabd khatam ho chuke the.
Ab sirf dhanush bol rahe the.
Yeh yuddh ab
ant ki taraf badh raha tha…"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.89
    with st.expander("Chapter 6.89 – The fierce battle continues"):
        text1 = """
        Chapter 89 – Lakshman aur Indrajit ka Lagataar Yuddh

Is beech Lakshmana, Dasharath ke putra,
ne gusse mein teer uthaye.
Unhone Indrajit par teeron ki baarish kar di.

Dhanush ki tan-tan sun kar
Indrajit ka chehra feeka pad gaya.
Uski aankhen Lakshman par tik gayi.

Yeh dekh kar Bibishana bole,
“Lakshman,
Indrajit ke charon taraf apashakun dikh rahe hain.
Jaldi karo.
Uska ant nazdeek hai.”"""
        create_image_text_layout("attached_assets/chapter6/6.89.jpg", text1, layout="side", image_position="left")

        text2 = """
        Lakshman ne zehrele saanp jaise teer chune.
Aur Indrajit par chhod diye.
Teer bijli jaise lage.
Indrajit kuch pal ke liye chakkar kha gaya.

Phir woh laal aankhon se aage badha.
Gusse mein chillaya,
“Kya tum bhool gaye ho?
Pehli baar maine tum dono bhaiyon ko
baandh kar gira diya tha!”

“Ab phir se mere saamne aaye ho?
Lagta hai tum mrityu chahte ho!”

Itna keh kar Indrajit ne vaar kiya.
Lakshman par saat teer lage.
Hanuman par das teer pade.
Bibishana par sau teer barsa diye.

Lakshman hase.
Bole,
“Bas itna hi?
Yeh kuch bhi nahi!”

Phir Lakshman ne bhaari teer uthaye.
Gusse mein chhod diye.
Bole,
“Veer yuddh aise nahi karte.
Tumhare teer kamzor hain.”

Lakshman ke teeron se
Indrajit ka sone ka kavach toot gaya.
Rath par bikhar gaya.
Uska sharir ghaavon se bhar gaya.

Gusse se bhara Indrajit
hazaar teer chhodne laga.
Lakshman ka divya kavach bhi toot gaya.

Ab dono ek doosre par toot pade.
Teer-teer se takra rahe the.
Khoon beh raha tha.

Yuddh bahut lamba chala.
Koi thaka nahi.
Koi peeche nahi hata.

Aisa lag raha tha
jaise aakash mein do kaale baadal takra rahe ho.
Ya jaise do pahaad aapas mein lad rahe ho.

Dono ke sharir
teeron se bhare the.
Khoon nadiyon ki tarah beh raha tha.
Phir bhi dono chamak rahe the,
jaise jungle ke phool khil gaye ho.

Lakshman aur Indrajit
barabar vaar kar rahe the.
Koi kisi se kam nahi tha.

Kaafi der tak yeh yuddh chala.
Tab Bibishana
Lakshman ke paas aa gaye.
Taaki ve thakaan se bach sakein.
Aur dharma ka yeh yuddh
ant tak ja sake."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.90
    with st.expander("Chapter 6.90 – Indrajit loses his chariot and horses"):
        text1 = """
        Chapter 90 – Indrajit ka Rath, Saarathi aur Ghode Gir Gaye

Insaan aur rakshas ka yeh yuddh
do tootey hue daanton wale haathiyon jaisa lag raha tha.
Dono ek-dusre ko haraana chahte the.

Yeh sab dekh kar Bibishana
yuddh ke aage aa gaye.
Haath mein unka shreshth dhanush tha.
Woh ant dekhna chahte the.

Bibishan ne teer chhode.
Tez aur jalte hue teer.
Rakshason par bijli jaise gिरे.
Pahaad jaise rakshas tootne lage."""
        create_image_text_layout("attached_assets/chapter6/6.90.jpg", text1, layout="side", image_position="left")

        text2 = """
        Bibishan ke saathi bhi aage badhe.
Gada, talwaar aur bhale chale.
Bibishan beech mein
ek bade haathi jaise dikh rahe the,
jinke chaaron taraf unke veer the.

Vanaron ka hausla badhane ke liye
Bibishan zor se bole,
“Indrajit hi Ravana ka aakhri sahara hai.
Uski sena ab bas itni hi bachi hai!”

“Prahasta mar chuka.
Nikumbha, Kumbhakarna,
aur kai maha-veer rakshas bhi gir chuke!”

“Tum samundar paar kar chuke ho.
Ab bas gaay ke khur ke nishaan jitna raasta baaki hai!”

“Main apne bhai ke bete ko nahi maar sakta.
Meri aankhon mein aansu aa jaate hain.
Isliye Lakshmana hi
Indrajit ka ant karenge.”

Bibishan ki baat sun kar
vanar garaj uthe.
Taali bajayi.
Cheekh-chilla ki.
Jaise mor baadal dekh kar naachte hain.

Udhar Jambavan
aur bhalu sena bhi toot padi.
Naakhun, daant, patthar—
sab chalne lage.

Rakshas bhi chup nahi rahe.
Bhale, kulhaadi, teer barsa diye.
Yuddh aur bhi bhayanak ho gaya.

Isi beech Hanuman ne
ek pahaad ka tukda tod liya.
Lakshman ko neeche utaara.
Aur hazaaron rakshason ko kuchal diya.

Phir Indrajit
phir se Lakshman par toot pada.
Dono ka seedha dvandh shuru ho gaya.

Teer itni tez chal rahe the
ki aankhon se pakadna mushkil tha.
Aakash andhera ho gaya.
Jaise suraj-chand badalon mein chhup gaye ho.

Shaam ho gayi.
Khoon behne laga.
Jungle ke jaanwar zor se bolne lage.
Rishiyon ne kaha,
“Jagat ka kalyan ho.”

Tab Lakshman ne chaar teeron se
Indrajit ke chaar kaale ghodon ko maar giraaya.
Phir ek chamakte Bhalla se
uske saarathi ka sir kaat diya.

Ab Indrajit khud
rath ki lagam sambhalne laga.
Ek haath se dhanush,
ek se ghode.

Par Lakshman ke teer
kabhi usse, kabhi ghodon ko lag rahe the.

Vanaron ne mauka dekha.
Pramathin, Rabhasa, Sharabha, Gandhamadan
sab ghodon par kud pade.

Bhaari bojh se ghode
khoon ugal kar gir pade.
Rath toot gaya.

Indrajit ab paidal ho gaya.
Par usne haar nahi maani.
Usne phir teer chhode.

Lakshman bhi rukey nahi.
Mahendra jaise dridh khade rahe.
Aur Indrajit par
teeron ki baarish karte rahe.

Ab yuddh
bina rath, bina ghodon
sirf veerta aur sankalp ka reh gaya tha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.91
    with st.expander("Chapter 6.91 – Indrajit is killed"):
        text1 = """
        Chapter 91 – Indrajit ka Ant (Death of Indrajita)

Ghode mar chuke the.
Rath toot chuka tha.
Phir bhi Indrajit
gusse se jal raha tha.
Uska veerata abhi zinda thi.

Woh aur Lakshmana
do jangli haathiyon jaise
ek-dusre par toot pade.

Vanar aur rakshas
idhar-udhar lad rahe the.
Koi apne neta ko chhodna nahi chahta tha."""
        create_image_text_layout("attached_assets/chapter6/6.91.jpg", text1, layout="side", image_position="left")

        text2 = """
        Tab Indrajit ne rakshason ko lalkaara,
“Har taraf andhera hai.
Dushman aur apna pehchaan mushkil hai.
Dar mato!
Main naya rath lekar
phir yuddh mein aaunga!”

Yeh keh kar woh chalaki se
Lanka ke andar chala gaya.
Wahan ek naya,
sone se saja hua rath tayaar hua.
Tez ghode.
Chatur saarathi.

Kismat use phir yuddh mein kheench laayi.
Indrajit tezi se
Lakshman aur Bibishana
par toot pada.

Naya rath dekh kar
sab hairaan reh gaye.
Indrajit ne
vanaron par teeron ki barsaat kar di.
Vanar ghabra kar
Lakshman ke paas aa gaye.

Tab Lakshman ne
uska dhanush kaat diya.
Indrajit ne doosra uthaya—
woh bhi toot gaya.

Lakshman ke paanch teer
Indrajit ke seene mein lage.
Khoon behne laga.

Indrajit ne phir bhi haar nahi maani.
Teeron ki baarish kar di.
Par Lakshman
hilay bhi nahi.

Lakshman ne
uske saarathi ka sir kaat diya.
Ab ghode bina niyantran
rath ghumane lage.

Lakshman ke teeron se
ghode bhi dar gaye.
Indrajit ne gusse mein
Lakshman ke maathe par
teen teer maare.

Lakshman ka chehra
teen pahaadon jaisa chamak utha.
Unhone turant
Indrajit ke chehre par
paanch teer chhod diye.

Dono khoon se lath-path the.
Phir bhi ladte rahe.
Jaise do Kimshuka ke ped.

Indrajit ne
Bibishan aur vanar netaon ko bhi
ghaayal kiya.
Tab Bibishan ne
gada se uske ghode gira diye.

Indrajit rath se kood pada.
Usne bhala phenka.
Lakshman ne use
hawa mein hi kaat diya.

Ab divya astra nikle.
Ek-dusre se takra kar
jal kar toot gaye.
Aakash kaanp utha.

Devta, rishi, gandharv
aakash se dekh rahe the.
Sab ki saansein ruk gayi.

Tab Lakshman ne
Indra ka divya astra uthaya.
Aur kaha,

“Yadi Rama
sach mein dharmic hain,
toh yeh astra
Ravana ke putra ka ant kare!”

Dhanush kaan tak kheencha.
Teer chhoda.

Aur woh teer
kabhi na chookne wala tha.

Indrajit ka sundar sir
dharti par gir pada.
Khoon beh raha tha.
Uska sharir
yuddh-bhoomi par gir gaya.

Indrajit mar chuka tha.

Vanar zor se garaj uthe.
Hanuman,
Bibishan, Jambavan
sab ne vijay ka naad kiya.

Rakshas sena bhag khadi hui.
Koi Lanka mein ghusa.
Koi samudra mein kooda.
Koi pahadon ki taraf bhaaga.

Aakash se phool barse.
Apsara naachi.
Devta khush hue.

Duniya ne saans li.
Paani saaf ho gaya.
Hawa pavitra ho gayi.

Vanaron ne Lakshman ko gher liya.
Taali bajayi.
Poonch hilayi.

“Jay Lakshman!
Jay Lakshman!”

Yeh yuddh
sirf ek jeet nahi tha.
Yeh adharm ke ek bade
stambh ka patan tha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.92
    with st.expander("Chapter 6.92 – Lakshmana is healed"):
        text1 = """
        Chapter 92 – Lakshman ke Ghaav Bhar Gaye

Lakshmana
yuddh-bhoomi mein khade the.
Sharir par ghaav the.
Khoon laga hua tha.
Par mann shaant tha.
Indrajit ka ant ho chuka tha.

Lakshman ne
Jambavan,
Hanuman
aur vanar sena ko saath liya.
Woh dheere-dheere
Rama
aur Sugriva
ke paas laut aaye.
Lakshman, Bibishana
aur Hanuman ka sahara le rahe the."""
        create_image_text_layout("attached_assets/chapter6/6.92.jpg", text1, layout="side", image_position="left")

        text2 = """
        Rama ke paas pahunch kar
Lakshman ne pranam kiya.
Teen baar parikrama ki.
Aur bhai ke paas khade ho gaye.
Jaise Indra ke paas Upendra khade hote hain.

Tab Bibishan aage aaye.
Unke chehre par khushi thi.
Unhone Indrajit ke ant ki poori kahani sunayi.

Yeh sun kar Rama ka mann bhar aaya.
Unki aankhon mein garv tha.
Unhone zor se kaha,
“Bahut badhiya, Lakshman!
Tumne bahut kathin kaam kiya hai.
Indrajit ka marna
hamari jeet ka nishaan hai.”

Rama ne Lakshman ka sir chooma.
Unhe apni god mein bithaya.
Zakhmi bhai ko
seene se laga liya.
Baar-baar pyaar se dekha.

Rama bole,
“Tumne Ravana ka sabse bada sahara tod diya hai.
Ab mujhe vishwas hai—
Ravana bhi zyada din nahi tik paayega.”

“Jab use apne putra ki mrityu ka pata chalega,
woh poori sena ke saath aayega.
Tab main uska ant karunga.”

“Lakshman,
tumhari vijay se
Sita ko paana
aur dharti par shanti laana
ab mushkil nahi raha.”

Rama ne Bibishan aur Hanuman ki bhi tareef ki.
Sabka hausla aur badh gaya.

Phir Rama ne
Sushena
ko bulaya.

Rama bole,
“Lakshman ke teer nikaalo.
Unke ghaav turant bhar do.
Aur jo bhi vanar aur bhalu ghaayal hain,
sabka ilaaj karo.”

Sushena aage aaye.
Unhone ek divya aushadhi
Lakshman ki naak ke paas rakhi.

Jaise hi Lakshman ne
uski sugandh li—
sab teer apne aap nikal gaye.
Ghaav bhar gaye.
Dard gayab ho gaya.
Bukhaar bhi utar gaya.

Lakshman phir se
poori tarah swasth ho gaye.
Unke chehre par tej tha.

Rama, Sugriva, Bibishan,
Hanuman aur Jambavan—
sab khushi se bhar gaye.

Rama ne muskurate hue kaha,
“Yeh vijay
sirf shuruaat hai.”

Indrajit gir chuka tha.
Ab Lanka ka ant
nazdeek aa raha tha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.93
    with st.expander("Chapter 6.93 – Ravana mourns his son’s death"):
        text1 = """
        Chapter 93 – Indrajit ki Mrityu ka Shok aur Ravana ka Krodh

Lanka ke dooton ne
jab Indrajit
ki mrityu dekhi,
toh bina der kiye
yeh samachar
Ravana
tak pahuncha diya.

Unhone kaha,
“Hey Maharaj,
aapke putra Indrajit
Lakshmana
ke haathon mare gaye hain.
Unke saath Bibishana bhi tha.
Humne yeh sab
apni aankhon se dekha hai.”

“Jo kabhi yuddh mein haara nahi,
jisne Indra samet devtaon ko jeeta,
woh aaj veergati ko praapt ho gaya.”"""
        create_image_text_layout("attached_assets/chapter6/6.93.jpg", text1, layout="side", image_position="left")

        text2 = """
        Yeh sunte hi
Ravana zameen par gir pada.
Kuch pal ke liye
uski chetna hi chali gayi.

Hosh aane par
woh zor-zor se rone laga.

Ravana cheekha,
“Hey Indrajit!
Tum kaise haar gaye?
Tum toh Mrityu ko bhi hara sakte the!”

“Aaj Yama mujhe
aur bhi bhayanak lagne laga hai.
Tumhare bina
teenon lok mujhe soone lag rahe hain.”

“Tum mujhe, apni maa ko,
Lanka ko chhod kar
kahaan chale gaye?”

“Hey putra,
tumse pehle mujhe mar jaana chahiye tha!”

Uska shok
ab bhayanak krodh mein badalne laga.
Uski aankhen aag jaise jal rahi thi.
Aansoo
ubalte tel jaise gir rahe the.

Woh dahadta hua bola,
“Brahma ke vardaan se
main dev aur asur se ajey hoon!”

“Mera kavach
kisi vajra se bhi nahi toot sakta.
Aaj kaun hai
jo mera saamna karega?”

“Main apna dhanush uthakar
Rama
aur Lakshman ka
vinash kar dunga!”

Putra ke shok mein
Ravana ka vivek toot gaya.
Usne bhayanak baat keh di—

“Indrajit ne
jhoothi Sita dikhayi thi.
Ab main
asli Sita
ko maar dunga!”

Talwar uthakar
woh Ashok Vatika ki taraf daud pada.
Uski patniyaan aur mantri
use rokne lage,
par woh nahi ruka.

Rakshas garajne lage,
“Aaj Rama aur Lakshman
zaroor girenge!”

Ashok Vatika mein
Sita ne Ravana ko
talwar ke saath aate dekha.
Woh kaanp uthi.

Sita rone lagi,
“Lagta hai Ravana mujhe maarne aaya hai.”

“Ya shayad
Rama aur Lakshman
mere kaaran mar gaye hain.”

“Aaj jo shankh aur nagade baj rahe hain,
kya yeh meri barbadi ka sanket hai?”

“Agar main Hanuman ke saath chali jaati,
toh aaj apne prabhu ke paas hoti.”

“Haay Maa Kaushalya!
Unka hriday toot jaayega.”

Isi beech
Ravana ke buddhimaan mantri
Suparshva
aage aaye.

Unhone kaha,
“Hey Dashanan,
krodh mein stri-vadh adharm hai.”

“Aap veer hain.
Yuddh mein jaaiye.
Kal amavasya hai—
poori sena ke saath nikliye.”

“Rama se yuddh karke
jeet haasil kijiye.”

Suparshva ki baat
Ravana ke mann mein baith gayi.
Uska krodh
thoda shaant hua.

Woh talwar neeche rakh kar
sabha bhavan ki taraf
laut gaya.

Par Lanka jaanti thi—
aakhri yuddh
ab door nahi tha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.94
    with st.expander("Chapter 6.94 – Rama fights bravely"):
        text1 = """
        Chapter 94 – Rama ke Adbhut Parakram

Sabha bhavan mein baith kar
Ravana
apne putra ke shok se toot chuka tha.
Uski saansein
ghayal sher jaise chal rahi thi.

Usne sena ke netaon se kaha,
“Ghode, rath, haathi—
sab lekar nikal jao.”

“Sirf Rama par vaar karo.
Teeron ki barsaat kar do.”

“Kal main khud
sabke saamne
Rama ka ant karunga.”"""
        create_image_text_layout("attached_assets/chapter6/6.94.jpg", text1, layout="side", image_position="left")

        text2 = """
        Ravana ka aadesh sun kar
rakshas sena nikal padi.
Haath mein gada, talwaar,
kulhaadi aur bhale the.

Vanar bhi peeche nahi rahe.
Unhone patthar aur ped uthaye.
Suraj ugte hi
bhayanak yuddh shuru ho gaya.

Khoon ki nadiyaan behne lagi.
Dhool aur cheekh se
aakash bhar gaya.

Vanar ghaavon se bhare the.
Phir bhi veerta se lade.
Par rakshas sena bahut badi thi.

Ant mein
vanar bhaag kar
Rama ke paas aa gaye.
Rama hi unka
aakhri sahaara the.

Tab Rama ne
apna dhanush uthaya.
Aur seedhe
rakshas sena ke beech
ghus gaye.

Jaise suraj
baadalon ke andar jaata hai,
waise hi Rama
dushman ke beech
adrishya ho gaye.

Sirf teer dikh rahe the.
Rakshas gir rahe the.
Par Rama kahaan hain—
yeh kisi ko samajh nahi aa raha tha.

Rakshas chillaye,
“Yeh Rama hai!”
Par ghabrahat mein
ek-doosre ko hi
Rama samajh kar
maarne lage.

Rama ne
Gandharva Astra ka prayog kiya.
Kabhi ek Rama dikhta.
Kabhi hazaar.

Unka dhanush
jalti hui mashaal
jaisa lag raha tha.

Aisa lag raha tha
jaise samay ka chakra
ghoom raha ho.
Aur uske beech
Rama khade hoon.

Sirf kuch hi ghanton mein
Rama ne akele
rakshas sena ko
nasht kar diya.

18,000 haathi.
14,000 ghode.
2 lakh paidal sainik.

Sab gir chuke the.

Jo bache,
woh jaan bachakar
Lanka bhaag gaye.

Yuddh-bhoomi
Rudra ke khel-sthal
jaisi lag rahi thi.

Aakash se
devta bole,
“Bahut achha!
Bahut achha!”

Sugriva
Jambavan
aur vanar neta
Rama ke paas aaye.

Rama shaant swar mein bole,
“Is astra ko
sirf main aur
Shiva
hi chala sakte hain.”

Devta Rama ko
pranam karne lage.
Unka mann
garv se bhar gaya.

Yeh sirf yuddh nahi tha.
Yeh dharma ka prakash tha.
Aur adharm par
ek aur bada prahaar."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.95
    with st.expander("Chapter 6.95 – Demon women cry in grief"):
        text1 = """
        Chapter 95 – Rakshasiyon ka Vilap (The Lament of the Titan Women)

Rama ke sunehre teeron se
hazaaron haathi, ghode, rath
aur veer rakshas gir chuke the.
Aag jaise chamakte jhande
ab dhool mein pade the.

Jo rakshas bach gaye the,
woh dar se kaanp rahe the.
Aur unki patniyaan—
jinhe apne putra, pati, bhai kho dene pade—
ek jagah ikattha ho kar
zor-zor se rone lagi."""
        create_image_text_layout("attached_assets/chapter6/6.95.jpg", text1, layout="side", image_position="left")

        text2 = """
        Woh bol uthi—

“Kaise us buddhi-hin Shurpanakha
ne van mein Rama
jaise mahaan purush ko
apni ichchha dikhayi?”

“Jo buddhi se andhi thi,
jo roop aur maryada se khaali thi,
usi ke kaaran
Khara aur Dushana mare gaye!”

“Usi ke kaaran
Ravana
ne Sita ka apaharan kiya
aur Rama jaise shaktishaali
veer ka krodh mol liya!”

“Viradha ne bhi Sita ko chhoona chaha tha—
Rama ne use bhi maar diya.”
“Janasthaan mein
14,000 rakshas
Rama ke teeron se gir gaye.”

“Khara, Dushana, Trishiras—
sab mare gaye.”
“Kabandh jaisa bhayanak rakshas bhi
Rama se bach nahi paaya.”

“Bali
jaisa mahaan yoddha bhi
Rama ke haath se gira.”
“Sugriva
ko phir se rajya mila—
yeh sab Rama ki shakti ka pramaan tha.”

“Phir bhi Ravana ne
kisi ki baat nahi maani.”
“Bibishana
ne sachcha updesh diya,
par usse bhi thukra diya.”

“Agar Ravana ne
Bibishana ki baat maani hoti,
toh aaj Lanka
shav-bhoomi nahi hoti!”

“Kumbhakarna mara.”
“Atikaya gira.”
“Indrajit bhi chala gaya.”
“Phir bhi Ravana ki aankhen nahi khuli.”

“Har ghar se yahi awaaz aa rahi hai—
‘Mera putra mara.’
‘Mera pati gira.’
‘Mera bhai nahi raha.’”

“Rama ne
haathi, ghode, sainik—
sab nasht kar diye.”
“Yeh kaun hai?
Rudra? Vishnu? Indra?”
“Ya swayam Kaal?”

“Ravana ko apne vardaan par
bahut ghamand tha.”
“Usne devtaon se raksha maangi,
par manav se nahi.”

“Isi liye Rama—
ek manav roop mein—
hamara vinash ban gaya.”

“Devta pehle hi jaante the
ki ek stri ke kaaran
rakshason ka ant hoga.”

“Us stri ka naam—
Sita.”

“Sita ko utha kar
Ravana ne
apni hi kabar khod li.”

“Ab humein
koi bacha nahi sakta.”
“Hum Rama ke haath aa chuke hain—
jo samay ke samaan
sab kuch mita deta hai.”

“Bibishana ne samay pe pehchaan liya
aur sahi sharan chuni.”

Rakshasiyon ne
ek-doosre ke haath pakad liye.
Aankhon mein aansoo the.
Dil mein bhay aur pachtava tha.

Yeh vilap sirf shok ka nahi tha—
yeh ahankaar ke ant ka ghoshna-patra tha."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.96
    with st.expander("Chapter 6.96 – Ravana goes to fight and sees bad signs"):
        text1 = """
        Chapter 96 – Ravana Yuddh ke liye Nikalta Hai aur Apashakun Dikhte Hain

Lanka ke har ghar se
rakshasiyon ke rone ki awaaz
Ravana
ke kaanon tak pahunch rahi thi.
Woh der tak saans leta raha.
Phir uske mann mein
aag bhadak uthi.

Usne hoth kaat liye.
Aankhen laal ho gayi.
Uska roop itna bhayanak tha
ki khud rakshas bhi
usse dekh na paayein.
Woh pralaya ki aag jaisa lag raha tha."""
        create_image_text_layout("attached_assets/chapter6/6.96.jpg", text1, layout="side", image_position="left")

        text2 = """
        Gusse mein garaj kar bola,
“Mahodara, Mahaparshva
aur Virupaksha
ko turant bulao.
Sena ko yuddh ke liye taiyaar karo!”

Dar ke maare
rakshas neta jhuk gaye.
Sab ne ek saath kaha,
“Jaise aagya, Maharaj!”

Pooja-path hua.
Ashirvaad liya gaya.
Aur veer rath par chadh kar
yuddh-bhoomi ki ore chal pade.

Ravana hansa.
Par woh hansna
khaufnaak tha.

Woh bola,
“Aaj main apne teeron se
Rama
aur Lakshmana
ko Yama ke lok bhej dunga!”

“Khara, Kumbhakarna,
Prahasta aur Indrajit—
sab ka badla aaj poora hoga!”

“Aaj mere teeron se
aakash, disha, samudra—
sab chhup jaayenge.”

“Aaj vanar sena
mere baanon ke samundar mein
doob jaayegi.”

“Aaj giddh aur lomdiyaan
dushman ke maans se
apna pet bharegi!”

“Rath taiyaar karo!
Dhanush lao!
Jo rakshas bache hain,
mere saath chalo!”

Mahaparshva ne
sena netaon ko hukm diya.
Ghar-ghar jaakar
rakshason ko bulaya gaya.

Talwaar, bhala, gada,
kulhaadi, chakr,
bhindipaal aur shatagni—
har tarah ke shastra uth gaye.

Laakhon rath aaye.
Laakhon haathi.
Karodon ghode.
Anaginat paidal sainik.

Ravana ka rath
divya shastra se bhara tha.
Sone aur motiyon se saja tha.
Ghantiyaan baj rahi thi.
Jaise suraj khud chal raha ho.

Ravana us rath par chadha.
Dharti kaanp uthi.
Nagaade, shankh,
aur yuddh-ninad goonj uthe.

Log chillaye,
“Dekho!
Sita ka haran karne wala
Raghukul ke veer se
ladne ja raha hai!”

Ravana poore ghamand se aage badha.
Mahodara, Mahaparshva
aur Virupaksha
bhi apne rathon par chadh gaye.

Par jaise hi Ravana
yuddh ke liye nikla—
apashakun shuru ho gaye.

Suraj feeka pad gaya.
Aakash andhera ho gaya.
Pakshi bhayanak cheekhne lage.
Dharti kaanp uthi.

Devtaon ne
khoon ki baarish ki.
Ravana ke ghode
ladkhada gaye.

Uske jhande par
giddh baith gaya.
Lomdiyaan bol uthi.

Ravana ki baayi aankh phadki.
Baaya haath kaanp utha.
Chehra peela pad gaya.
Awaaz bhi kamzor ho gayi.

Aakash se
ulka giri.
Garaj hui.

Yeh sab
uski mrityu ka sanket tha.

Par Ravana nahi ruka.
Usne apashakun ko nazarandaaz kiya.
Kismat use
vinash ki taraf
kheenche ja rahi thi.

Yuddh-ninad sun kar
vanar sena bhi
taiyaar ho gayi.
Dono taraf se
lalkar goonj uthi.

Ravana ne
sone ke teeron se
vanaron par kahar barsaya.
Kisi ka sir kata.
Kisi ka hriday chhida.
Kisi ke kaan,
kisi ki aankhen gayi.

Jab bhi das-sir wala Ravana
rath modta,
uska prahaar
rokna mushkil ho jaata.

Yeh yuddh
sirf shastra ka nahi tha.
Yeh ghamand aur dharma
ke beech
antim takraav tha.

Aur Ravana,
apashakun ke beech,
apne ant ki ore
badhta chala ja raha tha…"""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.97
    with st.expander("Chapter 6.97 – Sugriva fights Virupaksha"):
        text1 = """
        Chapter 97 – Sugriva aur Virupaksha ka Yuddh (Virupaksha ka Ant)

Ravana ke teeron se
bahut se vanar gir chuke the.
Unke shav dharti par pade the.
Vanar sena
aag mein phanse patangon jaise
idhar-udhar bhaag rahi thi.

Ravana
teeron ki barsaat karta hua
aage badh raha tha.
Vanar cheekhte hue
jalte hue haathiyon ki tarah
bhaagne lage.

Ravana, gusse mein,
sabko hata kar
Rama
ko dhoondhne laga."""
        create_image_text_layout("attached_assets/chapter6/6.97.jpg", text1, layout="side", image_position="left")

        text2 = """
        Yeh sab dekh kar
Sugriva
ka khoon khol utha.
Usne apni sena ka bhaar
Sushena
ko saunp diya.

Phir Sugriva
khud yuddh ke liye aage badha.
Haath mein ek bada ped tha.
Uske saath-saath
sab vanar neta bhi
patthar aur ped uthaye chal pade.

Sugriva ne zor se garjana ki.
Aur rakshas sena par toot pada.
Jaise pralaya ke samay
toofan ped gira deta hai,
waise hi Sugriva
rakshason ko kuchalta chala gaya.

Pattharon ki barsaat hui.
Rakshas
kaan aur sir katne ke baad
pahaadon ki tarah girne lage.
Cheekhon se aakash bhar gaya.

Tab Virupaksha
aage aaya.
Usne apna naam pukara.
Rath se kood kar
haathi par chadh gaya.

Zor se garaj kar
woh vanaron par toot pada.
Usne Sugriva par
teeron ki barsaat kar di.
Rakshas sena ka hausla
phir se jaag utha.

Sugriva ghaavon se bhara tha.
Par gussa aur badh gaya.
Usne ek bada ped uthaya
aur haathi ke sir par de maara.

Haathi cheekhta hua
dharti par gir pada.

Virupaksha haathi se kood gaya.
Talwar nikaali.
Bull ki khaal se bane
kavach mein saja hua
Sugriva ki taraf dauda.

Sugriva ne
ek bada patthar phenka.
Virupaksha bach gaya.
Aur talwar se
Sugriva par vaar kiya.

Sugriva kuch pal ke liye
behhosh ho kar gir gaya.

Par agle hi pal
Sugriva uth khada hua.
Usne apni mutthi ghumayi
aur Virupaksha ke seene par
zor se maar diya.

Virupaksha ne bhi
Sugriva ka kavach kaat diya.
Sugriva ghutnon par aa gira.

Phir Sugriva sambhla.
Aur bijli jaisi
ek punch maari.
Virupaksha bach gaya
aur palat kar
Sugriva ke seene par vaar kiya.

Ab Sugriva
poori tarah bhadak chuka tha.
Mauka dekh kar
usne Virupaksha ke
kanpatti par
Indra ke vajra jaise
zor se prahaar kiya.

Virupaksha
dharti par gir pada.
Uske muh se khoon behne laga.
Woh karahne laga.
Aankhen ghoom rahi thi.

Vanaron ne dekha—
dushman ka ant aa chuka tha.

Idhar-udhar
vanar aur rakshas sena
ab bhi lad rahi thi.
Cheekhon aur shor se
sab kuch goonj raha tha.
Jaise do samundar
takra rahe ho.

Virupaksha,
Sugriva ke haathon
yuddh-bhoomi par
gir chuka tha.

Vanar sena ka hausla
aasmaan chhoone laga.
Rakshas sena ka ek aur
bada sahara
toot chuka tha.

Yeh sirf ek yuddh nahi tha—
yeh adharm par dharma ki
ek aur tez chot thi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.98
    with st.expander("Chapter 6.98 – Sugriva kills Mahodara"):
        text1 = """
        Chapter 98 – Mahodara ka Ant (Sugriva ke Haathon)

Yuddh bahut bhayanak ho chuka tha.
Dono senayein
garmiyon mein sookhte hue
do talaabon jaise
dheere-dheere ghul rahi thi.

Apni sena ka nash
aur Virupaksha
ki mrityu dekh kar
Ravana
ka gussa dugna ho gaya.
Usne samajh liya—
bhagya ab uske khilaaf hai.
Uske mann mein
dar bhi aa gaya."""
        create_image_text_layout("attached_assets/chapter6/6.98.jpg", text1, layout="side", image_position="left")

        text2 = """
        Ravana ne paas khade
Mahodara
se kaha,
“Ab tum hi meri
aakhri aas ho.”

“Jaao!
Aaj apni veerta dikhao.
Mere upkaar ka
karz chukane ka
yehi samay hai!”

Mahodara ne garaj kar kaha,
“Jaise aagya, Maharaj!”
Aur woh dushman sena par
aise toot pada
jaise patanga aag par.

Mahodara ne
vanaron ke beech
bhayankar sanhaar macha diya.
Uske sunehre teeron se
vanaron ke haath, pair
aur janghein katne lagi.

Kai vanar
jaan bachakar bhaage.
Kuch Sugriva
ke paas aa gaye.

Yeh dekh kar
Sugriva ka khoon khol utha.
Woh seedha
Mahodara ki taraf dauda.

Sugriva ne
ek pahaad jaisa
bada patthar uthaya
aur zor se phenka.

Mahodara ne
shaant rehte hue
use apne teeron se
tukde-tukde kar diya.
Patthar ke tukde
giddhon ke jhund jaise
zameen par gir pade.

Sugriva aur bhi bhadak gaya.
Usne ek Saala ka ped ukhaada
aur Mahodara par de maara.
Par Mahodara ne
use bhi tod diya.

Tab Sugriva ne
zameen par padi
ek lohe ki mekh (iron bar) uthayi
aur ek zor ke vaar se
Mahodara ke ghodon ko
dharti par gira diya.

Rath bekaar ho gaya.
Mahodara kood kar neeche aaya.
Usne gada uthayi.

Ab dono saamne the—
Sugriva ke haath mein
lohe ki mekh,
Mahodara ke haath mein
chamakti hui gada.

Dono garje.
Jaise bijli se bhare
do kaale baadal.

Mahodara ne gada se
zor ka vaar kiya.
Par Sugriva ne
poori taakat se prahaar kar ke
gada tod di.

Sugriva ne phir
ek badi sunehri gada uthayi
aur Mahodara ki gada par de maari.
Is baar
dono hi shastra
tukdon mein bikhar gaye.

Ab shastra nahi bache the.
Dono ne
ghoonson se ladna shuru kiya.
Mukke barasne lage.
Dono jalte hue angaaron
jaise lag rahe the.

Kuch der baad
zameen par pade
talwaar uthayi gayi.
Dono phir se
ek-doosre par toot pade.

Mahodara ne gusse mein
Sugriva ke kavach par
talwaar maari—
par talwaar hi toot gayi.

Yeh mauka tha.

Sugriva ne
apni talwaar uthayi
aur ek hi vaar mein
Mahodara ka sir
dhad se alag kar diya.

Sunehra mukut,
kundal laga sir
dharti par gir pada.

Apne neta ko
sir-vihin dekh kar
rakshas sena ka hausla
toot gaya.
Sab bhaag khade hue.

Vanar sena
khushi se garaj uthi.
Sugriva vijayi tha.

Ravana ka gussa
aur bhadak utha.
Par Rama
ka mann
prasann ho gaya.

Mahodara ko gira kar
Surya-putra Sugriva
suraj ki tarah
tej se chamak raha tha.

Devta, rishi, yaksh
aur prithvi ke sab jeev
us vijay ko
khushi se dekh rahe the.

Yeh sirf ek yoddha ki haar nahi thi—
yeh adharm ki ek aur
badi giraavat thi."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.99
    with st.expander("Chapter 6.99 – Angada fights Mahaparshva"):
        text1 = """
        Chapter 99 – Angada aur Mahaparshva ka Yuddh

Mahodara
jab Sugriva
ke haathon mara gaya,
toh Mahaparshva
ka gussa bhadak utha.

Uski aankhen laal ho gayi.
Usne teer chalaane shuru kiye.
Vanaron ki panktiyaan
bikharne lagi.

Jaise hawa phal ko daal se tod deti hai,
waise hi Mahaparshva
vanaron ke haath-pair kaat raha tha.
Kuch ke haath kat gaye.
Kuch ke seene chhid gaye.

Vanar darr gaye.
Unka hausla tootne laga."""
        create_image_text_layout("attached_assets/chapter6/6.99.jpg", text1, layout="side", image_position="left")

        text2 = """
        Tab Angada
aage badha.
Samundar ki tarah garajta hua.
Usne apni sena ko
saans lene ka mauka dena chaha.

Angada ne
suraj jaisi chamakti
lohe ki mekh uthayi.
Aur zor se
Mahaparshva par de maari.

Mahaparshva behosh ho gaya.
Rath se neeche gir pada.
Saarathi bhi mara ja chuka tha.

Isi waqt
Jambavan
aage badhe.
Unke haath mein
pahaad jaisa patthar tha.
Unhone Mahaparshva ke
ghode aur rath tod diye.

Par Mahaparshva phir sambhal gaya.
Usne phir se
teeron ki barsaat kar di.

Angada ghaayal hua.
Jambavan ke seene mein
bhale lage.
Gavaksha
bhi teeron se chhalni ho gaya.

Angada ka gussa
ab seema paar tha.
Usne ek bahut badi
lohe ki mekh uthayi.
Dono haathon se ghumayi.
Aur Mahaparshva par phenki.

Woh mekh
Mahaparshva ke haath se
dhanush gira gayi.
Uska helmet bhi udd gaya.

Angada ne ek hi chhalaang mein
aage badh kar
uske kaan par
zor ka mukka maara.

Mahaparshva gusse se paagal ho gaya.
Usne badi kulhaadi uthayi.
Aur Angada par vaar kiya.
Par vaar kavach se phisal gaya.

Yahi mauka tha.

Angada ne
bijli jaise taakat se
apni mutthi uthayi.
Aur seene par
Indra ke vajra jaisa
prahār kiya.

Mahaparshva
wahin gir pada.
Uski saans ruk gayi.

Mahaparshva mar chuka tha.

Yeh dekh kar
rakshas sena darr gayi.
Unka hausla toot gaya.
Aur Ravana
gusse se kaanp utha.

Vanar sena
khushi se garaj uthi.
Angada ka naam
door-door tak goonj gaya.

Aakash mein devta bhi
khushi se chillaye.
Par Ravana ne
yeh shor suna
aur phir se yuddh ke liye
tayaar hone ka nischay kiya.

Seekh (Moral):
Jab ahankaar talwaar ban jaata hai,
toh dharma ka ek sachcha vaar
use tod deta hai."""
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.100
    with st.expander("Chapter 6.100 – Rama and Ravana fight with magic weapons"):
        text1 = """
        Chapter 100 – Rama aur Ravana ka Jaadu-Bhara Yuddh

Jab Mahodara,
Mahaparshva
aur Virupaksha
sab mare ja chuke the,
toh Ravana
ka gussa aag ban gaya.

Usne apne saarathi se kaha,
“Ab main Rama
aur Lakshmana
ko maar kar sabka badla loonga.
Yeh sab mere logon ke dukh ka kaaran hain.”

Ravana ne kaha,
“Rama ek vriksh hai.
Sita uska phool hai.
Aur Sugriva, Hanuman, Angada jaise vanar
uski shaakhaayein hain.
Aaj main us vriksh ko kaat doonga.”"""
        create_image_text_layout("attached_assets/chapter6/6.100.jpg", text1, layout="side", image_position="left")

        text2 = """
        Ravana apna rath tez chalata hua
Rama ki taraf badha.
Zameen kaanp uthi.
Pahaad, nadiyaan, jungle
sab hil gaye.
Pashu-pakshi darr gaye.

Ravana ne ek kaala jaadu-astra chalaaya.
Vanar idhar-udhar bhaagne lage.
Dhool aur shor chha gaya.

Par Rama khade rahe.
Shaant.
Mazboot.
Unke paas Lakshmana the.
Jaise Indra ke paas Vishnu.

Rama ne apna mahaan dhanush uthaya.
Uski awaaz se
zameen tak goonj uthi.
Ravana ne bhi teeron ki barsaat kar di.

Lakshmana ne pehle vaar kiya.
Par Ravana ne
har teer hawa mein hi kaat diya.
Ek se ek.
Teen se teen.
Das se das.

Ravana seedha Rama par aaya.
Uski aankhen gusse se laal thi.
Usne hazaaron teer chalaaye.

Rama ne bhi
apne teeron se
sab kaat diye.
Jaise saanp kat jaate hain.

Dono mahaan yoddha
ek-dusre ke chakkar kaatne lage.
Teer upar-neeche ud rahe the.
Aasmaan andhera ho gaya.
Bijli chamak rahi thi.

Yeh yuddh
Indra aur Vritra jaise lag raha tha.
Sab devta dekh rahe the.
Sab darr gaye the.

Ravana ne lohe ke bhaari teer
Rama ke maathe par chalaaye.
Par Rama bilkul nahi hile.
Jaise kamal ke phool lage hon.

Rama ne Rudra-astra chalaaya.
Par Ravana ka kavach
toota nahi.

Tab Ravana ne
bhayanak Asura-astra chalaaya.
Uske teer ajeeb the.
Kuch sher ke chehre jaise.
Kuch saanp jaise.
Kuch panch-sir wale.

Vanar darr gaye.

Tab Rama ne
Agneya-astra uthaya.
Aag jaise chamakte teer.
Suraj aur sitaaron jaise ujale.

Jaise hi dono astra takraaye,
aag aur roshni phail gayi.
Hazaaron jaadu-teer
hawa mein hi nasht ho gaye.

Ravana ka jaadu
toot gaya.

Yeh dekh kar
Sugriva
aur saare vanar
khushi se chillaye.
Unhone Rama ko gher liya.
Aur jai-jai kaar ki.

Rama muskuraaye.
Unka mann shaant tha.
Unhone ek aur baar
sabko bachaa liya.

Seekh (Moral):
Jaadu aur gussa
thode samay ke liye bhayanak lagte hain,
par sachcha dhairya aur dharma
hamesha jeet jaata hai."""
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
