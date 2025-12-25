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
