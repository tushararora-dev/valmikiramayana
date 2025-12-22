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
        """
        create_image_text_layout("attached_assets/chapter6/6.11.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.12
    with st.expander("Chapter 6.12 – Ravana talks with Kumbhakarna"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.12.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.13
    with st.expander("Chapter 6.13 – Ravana tells an old story"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.13.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.14
    with st.expander("Chapter 6.14 – Vibhishana criticizes Ravana’s courtiers"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.14.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.15
    with st.expander("Chapter 6.15 – Vibhishana scolds Indrajit for boasting"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.15.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.16
    with st.expander("Chapter 6.16 – Ravana insults Vibhishana and sends him away"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.16.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.17
    with st.expander("Chapter 6.17 – The monkeys discuss Vibhishana"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.17.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.18
    with st.expander("Chapter 6.18 – Rama listens to the monkeys’ advice"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.18.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")
    # Chapter 6.19
    with st.expander("Chapter 6.19 – Vibhishana is brought before Rama"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.19.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.20
    with st.expander("Chapter 6.20 – Ravana sends Shuka to Sugriva"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.20.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.21
    with st.expander("Chapter 6.21 – Rama becomes angry at the sea god"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.21.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.22
    with st.expander("Chapter 6.22 – The army crosses the sea"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.22.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.23
    with st.expander("Chapter 6.23 – Rama sees good and bad signs"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.23.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.24
    with st.expander("Chapter 6.24 – Shuka tells Ravana how monkeys treated him"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.24.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.25
    with st.expander("Chapter 6.25 – Ravana sends spies Shuka and Sarana"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.25.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.26
    with st.expander("Chapter 6.26 – Sarana describes the monkey leaders"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.26.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.27
    with st.expander("Chapter 6.27 – Sarana continues his report"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.27.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.28
    with st.expander("Chapter 6.28 – Shuka also lists the enemy warriors"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.28.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.29
    with st.expander("Chapter 6.29 – Ravana sends more spies"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.29.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.30
    with st.expander("Chapter 6.30 – Shardula reports back to Ravana"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.30.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.31
    with st.expander("Chapter 6.31 – Ravana lies to Sita about Rama’s death"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.31.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.32
    with st.expander("Chapter 6.32 – Sita feels hopeless and sad"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.32.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.33
    with st.expander("Chapter 6.33 – Sarama comforts Sita"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.33.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.34
    with st.expander("Chapter 6.34 – Sarama secretly watches Ravana’s plans"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.34.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.35
    with st.expander("Chapter 6.35 – Malyavan advises Ravana to make peace"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.35.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.36
    with st.expander("Chapter 6.36 – Ravana strengthens Lanka’s defenses"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.36.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.37
    with st.expander("Chapter 6.37 – Rama plans the attack"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.37.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.38
    with st.expander("Chapter 6.38 – The army climbs Mount Suvela"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.38.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.39
    with st.expander("Chapter 6.39 – Lanka is described in detail"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.39.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
        create_image_text_layout(text_content=text2, layout="full")


    # Chapter 6.40
    with st.expander("Chapter 6.40 – Sugriva and Ravana fight fiercely"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter6/6.40.jpg", text1, layout="side", image_position="left")

        text2 = """
        """
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
