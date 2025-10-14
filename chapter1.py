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
    create_image_text_layout("attached_assets/chapter1/chapter1.jpg", layout="full")


    text0 = """
    <h2>Chapter 1: Bala Kanda ( Book of Youth)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")


    # Chapter1
    with st.expander("Chapter 1.1 – Shri Narad tells Valmiki about Rama"):
        text1 = """
Ek din <span style="color:#FF5733;">Maharishi Valmiki</span>, jo sab muniyon me sabse bade aur sabse vidvan (<span style="color:#FF5733;">learned</span>) the, apne tapasya (<span style="color:#FF5733;">meditation</span>) aur shastra adhyayan (<span style="color:#FF5733;">study of scriptures</span>) ke beech, soch rahe the:

"Duniya me aaj aisa kaun hai, jo bahut hi guni (<span style="color:#FF5733;">talented</span>) aur veer (<span style="color:#FF5733;">heroic</span>) ho, jo sab kartavya (<span style="color:#FF5733;">duties</span>) jaanta ho, satya-premi (<span style="color:#FF5733;">truthful</span>), dharmic (<span style="color:#FF5733;">righteous</span>), sabke liye dayaalu (<span style="color:#FF5733;">benevolen</span>t), gyaanwan (<span style="color:#FF5733;">wise</span>), prabhavit (<span style="color:#FF5733;">eloquent</span>), sundar, dhairyavan (<span style="color:#FF5733;">patient</span>) aur krodh me bhi aisa ki logon ke dil me bhay (<span style="color:#FF5733;">fear</span>) daal de?"

        """
        create_image_text_layout("attached_assets/chapter1/1.1.1.jpg", text1, layout="side", image_position="left")

        text2 = """
Is sawaal ka uttar dene ke liye <span style="color:#FF5733;">Narada Muni</span>, jo bhut, vartamaan aur bhavishya ke gyaanwan the, bole: "Aise log bahut rare hote hain, lekin main aapko bata sakta hoon. Ikshvaku vansh me janme, unka naam hai Rama. Ve dharmic, veer, gyaanwan aur sabke hit ke liye sochne wale hain. Unka sharir majboot, bhujayein lambi, gardan shankh (<span style="color:#FF5733;">conch</span>) jaise aur naak prominent (<span style="color:#FF5733;">uddharit</span>) hai. Ve dhanurvidya (<span style="color:#FF5733;">archery</span>) me mahir, neeti aur dharm ke jaankaar, sadaiva dayalu aur pratigya (<span style="color:#FF5733;">promise</span>) me dridh (<span style="color:#FF5733;">firm</span>) hain."
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
<span style="color:#FF5733;">Narada</span> ne aur bataaya: "<span style="color:#FF5733;">Rama</span> sabke liye rakshak (<span style="color:#FF5733;">protector</span>) hain, jo dharm ka palan karte hain. Ve Vishnu ke saman veer (<span style="color:#FF5733;">courageous</span>) hain, dhairya me prithvi jaise, daan me Kuvera (<span style="color:#FF5733;">wealth god</span>) jaise aur satya me poornata (<span style="color:#FF5733;">perfection</span>) ke pratik hain. Ve <span style="color:#FF5733;">Raja Dasharath</span> ke putra aur sabke liye dayaalu hain."

Rama ka Vanvaas (Exile): <span style="color:#FF5733;">Raja Dasharath</span> ne Rama ko rajya ka uttaradhikari (<span style="color:#FF5733;">heir</span>) banane ki tayari ki, lekin <span style="color:#FF5733;">Rani Kaikeyi</span>, apne purane vachan (<span style="color:#FF5733;">promised boons</span>) ka sahara le kar, Rama ko 14 saal ke liye vanvaas (<span style="color:#FF5733;">forest exile</span>) bhejne aur apne putra <span style="color:#FF5733;">Bharata</span> ko rajya dene ki maang ki. <span style="color:#FF5733;">Raja Dasharath</span> ne apni pratigya aur maryada ka palan karte hue, apne priye putra <span style="color:#FF5733;">Rama</span> ko vanvaas bhej diya. Rama ne Sita aur apne bhai <span style="color:#FF5733;">Lakshmana</span> ke saath van ki ore rukh kiya.
        """
        create_image_text_layout("attached_assets/chapter1/1.1.2.jpg", text3, layout="side", image_position="right")

        text4 = """
<span style="color:#FF5733;">Raja Dasharath</span> ka ant ho gaya, lekin <span style="color:#FF5733;">Bharata</span>  ne rajya lene se inkaar kiya aur van me jaake Rama ke charan sparsh (<span style="color:#FF5733;">touch</span>) kiye. Rama ne usse apne paduka (<span style="color:#FF5733;">sandals</span>) diye aur rajya sambhalne ke liye kaha. <span style="color:#FF5733;">Bharata</span> ne seva aur vinamrata ke saath rajya sambhala aur <span style="color:#FF5733;">Rama</span> ke wapsi ka intezaar kiya. Van me Sukh aur Rakshas se Yudh: <span style="color:#FF5733;">Rama, Lakshmana aur Sita</span> ne van me sukh se jeevan bitaya, lekin rakshas (<span style="color:#FF5733;">demons</span>) unko pareshan karne lage. <span style="color:#FF5733;">Shurpanakha</span>, jo roop badal sakti thi, ko <span style="color:#FF5733;">Rama</span> aur <span style="color:#FF5733;">Lakshmana</span> ne hara diya. Khara, Dushana aur Trishira jaise dusht rakshas ko bhi Rama ne hara diya aur <span style="color:#FF5733;">14,000</span> rakshason ka vinaash kiya. Sita Ka Haraan (<span style="color:#FF5733;">Abduction</span>): <span style="color:#FF5733;">Ravana</span> ne Maricha ke saath Sita ko haran (<span style="color:#FF5733;">kidnap</span>) kiya aur Jatayu ko maar diya. <span style="color:#FF5733;">Rama</span> ko <span style="color:#FF5733;">Sita</span> ke haaran ka dukh hua. Van me unhone Kabandha naamak rakshas ko mara aur uski antim iccha poori ki.
        """
        create_image_text_layout(text_content=text4, layout="full")


        text5 = """
Phir Rama ne Shabari, ek tapasvi mahila se mulaqat ki, jo unka aadar (<span style="color:#FF5733;">worship</span>) karti thi. Van ke Pampa lake par Rama ne <span style="color:#FF5733;">Hanuman aur Sugriva</span> se mulaqat ki, aur <span style="color:#FF5733;">Sugriva</span> ko dosti me jod kar <span style="color:#FF5733;">Bali</span> ko hara kar Sugriva ko rajya diya. Sugriva ke sainiko ne Sita ki talash shuru ki.

Lanka Yatra aur Ravana Vadh: <span style="color:#FF5733;">Hanuman</span> ne Lanka jaake Sita ko Ashoka van me paya aur unhe <span style="color:#FF5733;">Rama</span> ka sandesh diya. Lanka ko aag laga kar, ve wapas aaye. Rama ne samudra par Nala ke netritva me pul banaya aur Lanka par chadhai ki. Lanka me <span style="color:#FF5733;">Ravana</span> ka yudh hua aur <span style="color:#FF5733;">Rama</span> ne Ravana ko maara, Sita ko wapas laya. Sita ne agni pariksha (<span style="color:#FF5733;">trial by fire</span>) di aur apni pavitrata (<span style="color:#FF5733;">purity</span>) sabit ki.


        """
        create_image_text_layout("attached_assets/chapter1/1.1.3.jpg", text5, layout="side", image_position="left")


        text6 = """
Rama Rajya aur Lok Anand (<span style="color:#FF5733;">Happiness</span>): Rama ne Vibishana ko Lanka ka raja banaya aur apne vanvaas ke baad Ayodhya me rajya sambhala. <span style="color:#FF5733;">Rama aur Sita</span> ke rajya me sab log sukhi, swasth (<span style="color:#FF5733;">healthy</span>) aur nirdosh (<span style="color:#FF5733;">safe</span>) rahe. Sab Vedic yajna (<span style="color:#FF5733;">sacrifices</span>) aur daan me lage, rajya samruddh (<span style="color:#FF5733;">prosperous</span>) hua, aur unhone apne vanvaasi (<span style="color:#FF5733;">subjects</span>) ke hit me sab kuch kiya. Rama ne <span style="color:#FF5733;">11,000</span> saal tak rajya kiya aur phir apni divya loka Vaikuntha wapsi hui. Paath ka Phal (<span style="color:#FF5733;">Merit of Reading Ramayana</span>) Jo koi bhi is kahani ko shraddha aur bhakti se padhta hai, uska jeevan pavitra (<span style="color:#FF5733;">pure</span>) hota hai, aur saari paap (<span style="color:#FF5733;">sins</span>) door ho jate hain.
        """
        create_image_text_layout(text_content=text6, layout="full")

    # Chapter2
    with st.expander("Chapter 1.2 – Valmiki makes the poem style to tell the story"):

        text1 = """
Jab <span style="color:#FF5733;">Maharishi Valmiki</span> ne <span style="color:#FF5733;">Narada</span> ji ki baatein suni, to unka man adbhut (<span style="color:#FF5733;">wonder</span>) aur bhakti (<span style="color:#FF5733;">devotion</span>) se bhar gaya. Unhone dil se Rama ki pooja (<span style="color:#FF5733;">worship</span>) ki aur Narada ji ko samman dete hue unhe aakaash (<span style="color:#FF5733;">sky/heaven</span>) ki ore jaane ki ijazat di.

Narada ji ke chale jaane ke baad, <span style="color:#FF5733;">Valmiki Maharishi</span> Tamasa nadi ke kinare gaye, jo Ganga ke paas thi. Wahan unhone dekha ki nadi ka paani kitna pavitra (<span style="color:#FF5733;">pure</span>) aur saaf hai, aur socha ki ye bilkul ek dharmik (<span style="color:#FF5733;">good</span>) insaan ke man jaise shuddh hai. Maharishi ne apne shishya Bharadvaja se kaha: "Beta, paani ka matra dekho, ab meri chhadi (<span style="color:#FF5733;">bark robe</span>) lao aur mujhe snan (<span style="color:#FF5733;">bath</span>) karna hai. Der mat karo."
        """
        create_image_text_layout("attached_assets/chapter1/1.2.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Bharadvaja ne turant jaake robe laayi aur Maharishi ne usse pehn kar snan kiya, aur pitra aur devtaon ko jal arpan (<span style="color:#FF5733;">water offering</span>) diya. Phir ve van me ghoomte hue prakriti (<span style="color:#FF5733;">nature</span>) ka anand lene lage. Krauncha Bird ka Katha (<span style="color:#FF5733;">The Bird Incident</span>): Tab Valmiki ne dekha ki do krauncha (<span style="color:#FF5733;">crane</span>) birds apni prem (<span style="color:#FF5733;">love</span>) me khushi se khel rahe hain. Achaanak, ek shikari (<span style="color:#FF5733;">hunter</span>) aaya aur male bird ko maar diya. Female bird dukh (<span style="color:#FF5733;">grief</span>) me cheekh uthi aur apne partner ke liye shok (<span style="color:#FF5733;">mourning</span>) karne lagi. Valmiki Maharishi ka hriday (<span style="color:#FF5733;">heart</span>) us dukh se bhar gaya. Unhone shikari ko gussa me kuch shabd bole: "Tumne prem ke pal me pakde hue bird ko maara, tum kabhi samriddhi (<span style="color:#FF5733;">prosperity</span>) nahi paoge." Phir unhone socha ki ye shabd unke karuna (<span style="color:#FF5733;">compassion</span>) se aaye hain.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Metrical Verse ka Janm: Unhone shishya Bharadvaja ko kaha ki jo shabd unke hriday se spontaneously (<span style="color:#FF5733;">apne aap</span>) nikle hain, use chaar padaon (<span style="color:#FF5733;">feet</span>) me likho, jo vina (<span style="color:#FF5733;">musical instrument</span>) par gaaye ja sakte hain. Bharadvaja ne shabd yaad kiye aur Maharishi bahut prasann (<span style="color:#FF5733;">happy</span>) hue.

Snan ke baad, Valmiki ne hermitage (<span style="color:#FF5733;">ashram</span>) wapas jaake pooja aur dharmik kriyaen ki. Tab Brahma ji, vishw ke srishti karta (<span style="color:#FF5733;">creator</span>), unke samne aaye. Valmiki ne unka aadar (<span style="color:#FF5733;">respect</span>) kiya aur Brahma ji ne unhe aashirwad diya: "Ye shabd jo tumne krauncha ke dukh se banaye, kavita (<span style="color:#FF5733;">poetry</span>) ban jaaye. 
        """
        create_image_text_layout("attached_assets/chapter1/1.2.2.jpg", text3, layout="side", image_position="right")

        text4 = """
Tum Rama ki kahani jo dharm aur gun se bhari hai, usse kavya roop me varnit karo. Tumhare shabd kabhi galat nahi honge. Jab tak parvat aur nadiyan hain, Rama ki kahani amar rahegi. Tum bhi uchch sthaan (<span style="color:#FF5733;">higher regions</span>) me sadaiv sthir rahoge."

Valmiki Maharishi aur Bharadvaja is adbhut ghatna se hairan (<span style="color:#FF5733;">amazed</span>) ho gaye. Valmiki ne apne man me bhagwan ki aradhana (<span style="color:#FF5733;">meditation on Lord</span>) ki aur socha ki Rama ki kahani ko isi tarah kavya (<span style="color:#FF5733;">verse</span>) me likha jaaye. Is tarah, Shri Valmiki ne Rama ji ke jeevan aur Ravana vadh ki kahani ko sundar aur sushil (<span style="color:#FF5733;">beautiful and measured</span>) chhandon me likhna shuru kiya, jo jagat ke liye anant punya (<span style="color:#FF5733;">merit</span>) ka kaam ban gayi.

        """
        create_image_text_layout(text_content=text4, layout="full")

    # Chapter3
    with st.expander("Chapter 1.3 – Amazing deeds of Rama that will be told"):

        text1 = """
<span style="color:#FF5733;">Maharishi Valmiki</span>, jo ab Narada ji ki kahaniyon se prabhavit (<span style="color:#FF5733;">inspired</span>) ho chuke the, apne haath-pair dhoke aur thoda paani pee kar, kusha grass ki seat par baith gaye, haath jode aur poorv disha (<span style="color:#FF5733;">east</span>) ki taraf mukh kar dhyaan (<span style="color:#FF5733;">meditation</span>) me lag gaye.

Unke dhyaan aur Shri Brahma ki kripa (<span style="color:#FF5733;">grace</span>) se, Maharishi ne Rama, Sita aur Lakshmana ke jeevan ke sab anubhav (<span style="color:#FF5733;">experiences</span>) dekhe. Ve sab kuch dekh rahe the jaise haath par fal rakha ho – poora aur spasht (<span style="color:#FF5733;">clear</span>). Is drishtikon (<span style="color:#FF5733;">vision</span>) se prabhavit ho, Maharishi ne socha ki ye kahani kavya (<span style="color:#FF5733;">verse</span>) me likhi jaaye, jo duniya ke liye dharm, sukh aur manoranjan (<span style="color:#FF5733;">delight</span>) laye. Rama ke Mukhya Karya aur Guna (<span style="color:#FF5733;">Main Deeds and Qualities</span>)
        """
        create_image_text_layout("attached_assets/chapter1/1.3.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Valmiki ne likha ki Shri Rama ki kahani me ye sab hote hain: Rama ka janm aur balya (<span style="color:#FF5733;">childhood</span>), Unka veer (<span style="color:#FF5733;">valor</span>) aur sabke prati daya (<span style="color:#FF5733;">benevolence</span>), Unka sundar (<span style="color:#FF5733;">pleasing</span>) swabhav aur satya-premi (<span style="color:#FF5733;">truthful</span>) svabhav, Maharishi Vishwamitra ki seva aur unse shiksha lena, Maha-dhanush (<span style="color:#FF5733;">great bow</span>) todna, Sita se vivaah (<span style="color:#FF5733;">marriage</span>), Parasurama se vivad, Rajyabhishek (<span style="color:#FF5733;">coronation</span>) ki tayyari, Kaikeyi ka virodh aur Rama ka vanvaas (<span style="color:#FF5733;">forest exile</span>), Raja Dasharath ka dukh aur mrityu (<span style="color:#FF5733;">death</span>), Ayodhya ke logon ka shok (<span style="color:#FF5733;">grief</span>), Ganga paar karna aur Bharadvaja ke ashram jana, Cittrakuta par vanvas me rehna, Bharata ka aana aur rajya ke liye prarthana (<span style="color:#FF5733;">request</span>) karna, Rama ka rajya na lena aur Bharata ko paduka dena, Van me Karya aur Rakshason se Yudh.
        """
        create_image_text_layout(text_content=text2, layout="full")


        text3 = """
Dandaka van me asuraon ka vinaash (<span style="color:#FF5733;">destruction of evil</span>), Sharabhanga aur Sutikshna jaise Maharishiyon se mulaqat, Anasuya se Sita ki shiksha, Agastya Maharishi ka darshan, Panchavati me basna, Jatayu se mulaqat aur Shurpanakha se samvad (<span style="color:#FF5733;">conversation</span>), Shurpanakha ka mutilation aur Khara, Dusana, Trishira ka vinaash, Ravana ka aagman, Maricha ka vinaash, aur Sita ka haran (<span style="color:#FF5733;">abduction</span>), Jatayu ka mrityu aur Kabandha se mulaqat, Pampa jheel par Shabari se darshan, Rishyamukha par Hanuman se mulaqat aur Sugriva se dosti, Bali ka yudh aur vadh, Sugriva ka rajya sthapna (<span style="color:#FF5733;">installation</span>), Sita ki Talash aur Lanka Yatra, Van me Sugriva ke saath monkey sena ka aayojan (<span style="color:#FF5733;">organization</span>), Rama ki anguthi (<span style="color:#FF5733;">ring</span>) Hanuman ko dena, Sampati se Lanka ke baare me jankari lena, Hanuman ka samudra par chalang (<span style="color:#FF5733;">leap</span>), Singhika naam ki female demon ka vinaash
        """
        create_image_text_layout("attached_assets/chapter1/1.3.2.jpg", text3, layout="side", image_position="right")

        text4 = """
Lanka me pravesh aur Sita ka darshan Ashoka van me, Ravana aur female asuraon se Sita ki raksha, Trijata ka sapna aur Hanuman ko Sita ka ring dena, Van me Lanka ka agni prahar (<span style="color:#FF5733;">burning of Lanka</span>), Lanka Par Vijay aur Sita ki Wapsi, Nala aur Nila ke netritva me samudra par pul banana, Lanka ki siege aur Vibishana ka sharan lena, Kumbhakarna aur Meghanada ka vinaash, Ravana ka vadh, Sita se milna aur Lanka me Vibishana ko rajya dena, Pushpaka viman se Ayodhya wapsi, Bharata se milna aur rajya grahan (<span style="color:#FF5733;">coronation</span>), Monkey sena ka farewell aur janata ka anand (<span style="color:#FF5733;"joy</span>), Valmiki ne in sab deeds aur unke vishesh guno ko pavitra kavya (<span style="color:#FF5733;">sacred poem</span>) me likha, jo dharm, sukh aur manohar (<span style="color:#FF5733;">charming</span>) kahani ke roop me amar hai.
        """
        create_image_text_layout(text_content=text4, layout="full")

    # Chapter4
    with st.expander("Chapter 1.4 – Rama’s sons recite the poem"):

        text1 = """
Jab Shri Rama abhi Ayodhya ke raja the, tab Maharishi Valmiki ne apna sundar aur pavitra (<span style="color:#FF5733;">holy</span>) Ramayana likh liya. Isme unhone <span style="color:#FF5733;">24,000</span> shlok likhe, jo <span style="color:#FF5733;">500</span> adhyay (chapters) aur 6 kand (<span style="color:#FF5733;">books</span>) me bante hain. Uske baad unhone epilogue bhi likha. Maharishi ne socha: "Ab main is kahani ko kisey sikhaun?" Tab Rama aur Sita ke putra, Kusha aur Lava, Maharishi ke paas aaye aur unke charanon ko chhu kar samman dikhaya. Valmiki ne dekha ki dono putra vidyavan (<span style="color:#FF5733;">wise</span>) aur vedon ke gyaan me vishwas (<span style="color:#FF5733;">faith</span>) rakhte hain. Ve dono kavya aur sangeet me mahir (<span style="color:#FF5733;">skilled</span>) the, to Maharishi ne unhe poora Ramayana sikha diya. Kusha aur Lava ki Siksha aur Gayaki: Maharishi ne unhe Rama aur Sita ke sab guno aur Ravana vadh ki kahani sikhayi.
        """
        create_image_text_layout("attached_assets/chapter1/1.4.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Ye kavya tri-laya (<span style="color:#FF5733;">three measures of time</span>) aur saat swaron (<span style="color:#FF5733;">seven notes</span>) me gaaya ja sakta tha. Kavya me prem, veerta (<span style="color:#FF5733;">courag</span>e), krodh (<span style="color:#FF5733;">anger</span>), shok (<span style="color:#FF5733;">grief</span>), daya (<span style="color:#FF5733;">compassion</span>), hasya (<span style="color:#FF5733;">laughter</span>), aur shanti (<span style="color:#FF5733;">serenity</span>) jaise bhav samaye hue the.

Kusha aur Lava divya sundar (<span style="color:#FF5733;">god-like beauty</span>) aur melodious voice ke saath is kavya ko baar-baar gaye aur yaad kiya. Ve Ramayana ko sages, brahmins aur rishiyon ke samne prastut (<span style="color:#FF5733;">present</span>) karte, jaise Maharishi ne sikhaya tha. Rama ke Sabha me Prastuti : Ek din, dono putra Shri Rama ki sabha me gaye aur poora Ramayana gaaya. Sabha me baithe rishiyon ne unki melody aur kavya ka prashansha (<span style="color:#FF5733;">praise</span>) kiya, aur anand se aansu bahaye. Ve bole:
"Kya khoobsurat gaate ho! Kya adbhut kavya hai, Shri Rama ki kahani!"
        """
        create_image_text_layout(text_content=text2, layout="full")


        text3 = """
Kuch rishiyon ne loshta (<span style="color:#FF5733;">water pots</span>) diye, Kuch ne meethay phal (<span style="color:#FF5733;">fruits</span>), Kuch ne bark robe aur antelope skin diye, Kuch ne yajnopavit (<span style="color:#FF5733;">sacred thread</span>), kusha grass, yellow cloth, aur rosary diye, Sab ne unhe aashirwad diya: "Lambi umar pao, aur gyaan prapt karo". Rama ka Samman aur Sukh : Rishiyon ne kaha: "Ye kavya aur iski chhand (<span style="color:#FF5733;">metre</span>) bhavishya ke kavi ke liye adhar hai. Jo ise sunega, uska man prasann hoga, gyaan badega aur sharir tandurust rahega." Shri Rama, jo apni rajya sabha se guzre, ne Kusha aur Lava ko swaagat aur samman diya. Ve apni golden throne par baithe aur sabhi mantriyon aur bhaiyon ke saath in dono ki prashansha ki.
        """
        create_image_text_layout("attached_assets/chapter1/1.4.2.jpg", text3, layout="side", image_position="right")

        text4 = """

Shri Rama ne kaha: "Suno ye itihasik kavya, jo ye do divya minstrels (<span style="color:#FF5733;">guitar/singing artists</span>) ga rahe hain. Isme ghatnayein aur seekh chhupi hai." Kusha aur Lava ne apni vinas (<span style="color:#FF5733;">musical instruments</span>) ko tune karke Ramayana spasht aur madhur dhun me gaaya. Sabha me sab log dhyaan se sune aur man aur hriday (<span style="color:#FF5733;">heart</span>) se prasann hue. Shri Rama ne unki mahanta aur sangeet ke gun ki prashansha ki aur ve dono aur mehnat se apni kala dikhate rahe.
        """
        create_image_text_layout(text_content=text4, layout="full")

    # Chapter5
    with st.expander("Chapter 1.5 – King Dasaratha’s kingdom and city"):

        text1 = """
Puranon ke hisaab se, dharti (<span style="color:#FF5733;">earth</span>) ke saat dwip (<span style="color:#FF5733;">seven islands</span>) hamesha ek shaktishaali raja ke under rahe hain, jo Manu ke vanshaj (<span style="color:#FF5733;">descendants</span>) me se hote the aur hamesha vijayi (<span style="color:#FF5733;">victorious</span>) rahe. Un shaktishaali rajo me se ek tha <span style="color:#FF5733;">Sagara</span>, jiske <span style="color:#FF5733;">60,000</span> putra ne samundar khoda tha. Ye Ramayana isi Ikshvaku vansh aur Sagara ke gharane ki kahani batata hai. Ye poori kahani vishwas ke saath suni jaaye. Koshala aur Ayodhya: Sarayu nadi ke kinare, ek bada aur samruddh (<span style="color:#FF5733;">prosperous</span>) desh tha, jiska naam tha Koshala. Yahan ke log sukhi aur santusht the. Is desh me tha Ayodhya, jo teenon lokon (<span style="color:#FF5733;">three worlds</span>) me mashhoor tha. Isse Manu ji, jo manusyon me pramukh the, ne banaya tha.
        """
        create_image_text_layout("attached_assets/chapter1/1.5.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Sheher ke raaste (<span style="color:#FF5733;">streets</span>) 60 mile tak phailay hue the, saaf-suthre aur phoolon se sajaye hue. Sheher ke pramukh raaste ko paani se sprinkle kiya jaata tha aur phool bikher diye jaate the. Rajdhani ki raksha King Dasaratha karte the, jaise Indra Amaravati ki raksha karte hain. Ayodhya me sab kuch shandar aur sundar tha: Mahan aur mazboot gate, khubsurat bazaar aur market, Fortifications jo maharathi engineers ne banaye the. Bards, singers aur public musicians har jagah gungunate rehte the, Logon ke ghar bade, arched aur decorated the, flags aur banners ke saath, Bagiche aur aam ke baag sheher ko aur sundar banate the, jaise ladki ne hariyali ki kamar pehni ho.
        """
        create_image_text_layout(text_content=text2, layout="full")
        text3 = """
Sheher me: Gaj, ghode, gai, oont aur khachchar dikhte the, Bahut saare raajdooton (<span style="color:#FF5733;">ambassadors</span>) aur vyapari (<span style="color:#FF5733;">merchants</span>) aate-jate rehte the, Log shanti se vyapar karte the, Rajmahal aur Ghar, Ayodhya ke rajmahal Indra ke Amaravati jaise shandar the, sone aur ratno se sajaye hue Mahal ke gumbad (<span style="color:#FF5733;">domes</span>) pahaad jaise lagte the, Sheher me tall aur sundar ghar, music aur sukh se bhare hue, Noble logon ke ghar, jaise aerial chariots jisme pavitra aur dharmik log heaven me jaate hain, Veer Senani aur Gyaani Log, Sheher ke veer yoddha kabhi bhagte huye dushman ko nahi maarte, Sab skilled archers the, sound se target ko maarne wale, Bahut ne singh, baagh aur bhediye apne weapons se mara, Sheher me hazaron chieftains ka basera tha, aur ye sab King Dasaratha ne banwaya, Ayodhya me vidwaan (<span style="color:#FF5733;">learned men</span>) aur sages bhi rehte the: Jo rituals aur dharmik karyo me nishthavan the, Artists, craftsmen aur Veda ke gyaani log, Yoga aur mystical gyaan me mahir rishis.
        """
        create_image_text_layout("attached_assets/chapter1/1.5.2.jpg", text3, layout="side", image_position="right")

    # Chapter6
    with st.expander("Chapter 1.6 - The beautiful city of Ayodhya"):

        text1 = """
Ayodhya ek sundar aur samruddh (<span style="color:#FF5733;">prosperous</span>) nagari thi, jahan rehte the Maharaj Dasharatha, jo Maharaj Manu ke vansaj (<span style="color:#FF5733;">descendant</span>) the. Ve Vedo ke gyaan me nipun (<span style="color:#FF5733;">learned</span>) the, aur unka sabse bada dhan tha satya aur dharma (<span style="color:#FF5733;">truth and virtue</span>). Dasharatha apne vachanon (<span style="color:#FF5733;">promises</span>) ke pakke the — ek aise raja jo kabhi apni baat se nahi mukarte the. Ve shant, buddhimaan, aur apne praja ke dil ke bahut kareeb the.
        """
        create_image_text_layout("attached_assets/chapter1/1.6.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Unka parakram (<span style="color:#FF5733;">valour</span>) Indra ke barabar tha, aur dhan (<span style="color:#FF5733;">wealth</span>) me ve Kuber ke samaan the. Ve ek mahan rathi (<span style="color:#FF5733;">charioteer</span>) aur yagna karne wale dharmic raja the, jo hamesha sahi marg (<span style="color:#FF5733;">path of righteousness</span>) par chalte the. Jaise Indra Amaravati me raj karta hai, waise hi Maharaj Dasharatha Ayodhya par raj karte the. Ayodhya ke log bhi unke jaise hi sundar swabhav ke the — sachche, samajhdaar, aur santusht (<span style="color:#FF5733;">content</span>). Har vyakti apne dharm aur kartavya (<span style="color:#FF5733;">duty</span>) me laga rehta tha. Koi lalchi (<span style="color:#FF5733;">greedy</span>) nahi tha, koi jhooth bolne wala nahi tha. Har ghar dhan, ann (<span style="color:#FF5733;">grain</span>), aur pashuon (<span style="color:#FF5733;">cattle</span>) se bhara rehta tha.
        """
        create_image_text_layout(text_content=text2, layout="full")


        text3 = """
Wahan koi chor nahi tha, koi asatya (<span style="color:#FF5733;">untruthful</span>) ya paapi nahi tha. Har purush aur nari pavitra (<span style="color:#FF5733;">pure</span>), vinamra (<span style="color:#FF5733;">humble</span>) aur sanyamit (<span style="color:#FF5733;">self-controlled</span>) the. Sab log roz nahaate the, apne sharir par chandan aur gulab ke sugandhit tel (<span style="color:#FF5733;">fragrant oils</span>) lagate the. Har koi apne parivar ke saath khush rehta tha.

Brahman log dharm aur vedadhyayan (<span style="color:#FF5733;">study of Vedas</span>) me lage rehte the. Koi bhi bhagwan ke astitva (<span style="color:#FF5733;">existence</span>) ko nahi niraakar karta tha. Koi bhi bhog-vilason (<span style="color:#FF5733;">worldly pleasures</span>) me atka nahi tha. Sab apne dharm aur tapasya me sthir (<span style="color:#FF5733;">firm</span>) the. Kisi ko rog (<span style="color:#FF5733;">disease</span>) nahi tha, koi dukh nahi tha. Sab log bade umr tak jeete the, apne gharon me bachchon, poton aur susheel (<span style="color:#FF5733;">virtuous</span>) mahilaon ke saath.
        """
        create_image_text_layout("attached_assets/chapter1/1.6.2.jpg", text3, layout="side", image_position="right")


        text4 = """
Yodha (<span style="color:#FF5733;">warriors</span>) veer aur nishank (<span style="color:#FF5733;">fearless</span>) the — ve shatruse yuddh me kabhi peeche nahi hatte. Ve dhanu-vidya (<span style="color:#FF5733;">archery</span>) me nipun the, aur sher ke saman veer (<span style="color:#FF5733;">lion-hearted</span>) the. Ayodhya me duniya ke sabse ache ghode aur hathi the — kuch Himavat (<span style="color:#FF5733;">Himalaya</span>) ke pahaadon se, kuch Kamroja aur Vanaya desh se laaye gaye the. Ye hathi bade-bade pahaadon jaise lagte the, aur Ayodhya ko ek ajeya (<span style="color:#FF5733;">invincible</span>) nagari banate the — jise koi bhi yuddh me hara nahi sakta tha. Aur iss Ayodhya nagari ke beech rehte the Maharaj Dasharatha — jaise chand apne tare (<span style="color:#FF5733;">stars</span>) ke beech chamakta hai. Ve ek shaktishaali aur nyayapriya (<span style="color:#FF5733;">just</span>) raja the, jin ke rajya me har praja khushhal (<span style="color:#FF5733;">prosperous</span>) thi.
        """
        create_image_text_layout(text_content=text4, layout="full")

    # Chapter7
    with st.expander("Chapter 1.7 - How the kingdom is run"):

        text1 = """
Ayodhya ke Maharaj Dasharatha ke mantrigan (<span style="color:#FF5733;">ministers</span>) hamesha unke kalyaan (<span style="color:#FF5733;">welfare</span>) aur rajya ke hit me lage rehte the. Ye sabhi mantri Ikshvaku vansh (<span style="color:#FF5733;">royal lineage</span>) ke the aur apne dharm aur satya par adharit (<span style="color:#FF5733;">truth-based</span>) salaah dete the. In mantriyon me aath sabse prasiddh (<span style="color:#FF5733;">famousr</span>) the — Dhrishti, Jayanta, Vijaya, Siddhartha, Arthasadhaka, Ashoka, Mantrapala aur Sumantra. Ye sab raja ke sacha saathi the, jo din-raat rajya ke kaam me lage rehte the, bina thake aur bina lalach (<span style="color:#FF5733;">greed</span>) ke. 
        """
        create_image_text_layout("attached_assets/chapter1/1.7.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Raja Dasharatha ke saath Maharishi Vasishtha aur Maharishi Vamadeva jaise mahan rishiyon ka sahyog (<span style="color:#FF5733;">guidance</span>) bhi tha. Ye dono raja ke dharmik (<span style="color:#FF5733;">spiritua</span>l) aur rajneetik (<span style="color:#FF5733;">political</span>) guru the, jo unhe har kadam par margdarshan (<span style="color:#FF5733;">guidance</span>) dete the. In sabhi mantriyon ke gun (<span style="color:#FF5733;">qualities</span>) bahut adbhut the — ve imaandaar, dharmik (<span style="color:#FF5733;">righteous</span>), sabr wale (<span style="color:#FF5733;">patient</span>), aur prajaa ke dukh-sukh samajhne wale the. Ve kabhi bhi anyay (<span style="color:#FF5733;">injustice</span>) nahi karte the aur apne hi putron (<span style="color:#FF5733;">sons</span>) ko dand (<span style="color:#FF5733;">punishment</span>) dete the agar ve galti karte.

Unhe arthashastra (<span style="color:#FF5733;">economics</span>) aur yudh-niti (<span style="color:#FF5733;">war strategy</span>) dono ka poora gyaan tha. Ve hamesha shatru par nyay ke anusaar dand dete the — na zyada, na kam. Unka uddeshya (<span style="color:#FF5733;">motive</span>) tha nyay aur rajya ki shanti (<span style="color:#FF5733;">peace</span>). Ve sabhi mantri pavitra (<span style="color:#FF5733;">pure</span>) charitra ke the. Koi bhi bure karmo me nahi pada tha, aur sab ek-doosre ke saath prem aur samman (<span style="color:#FF5733;">respect</span>) se rehte the. Unke vichar (<span style="color:#FF5733;">thoughts</span>) hamesha uchch aur tark-sangat (<span style="color:#FF5733;">logical</span>) hote the.
        """
        create_image_text_layout(text_content=text2, layout="full")


        text3 = """
Mantrigan itne samajhdaar the ki ve logon ki zaruraton (<span style="color:#FF5733;">needs</span>) ko samajh kar turant raja tak pahunchate the, jisse koi bhi praja akeli ya pareshaan nahi rehti thi. Maharaj Dasharatha bhi apne rajya me kabhi adharm (<span style="color:#FF5733;">injustice</span>) ko jagah nahi dete the. Isi wajah se unka naam “Satya Sagar” (<span style="color:#FF5733;">ocean of truth</span>) ke roop me pura jagat me prasiddh tha.

Raja Dasharatha ek aise shaktishaali aur dayalu (<span style="color:#FF5733;">benevolent</span>) raja the jinka koi saman (<span style="color:#FF5733;">equal</span>) nahi tha. Unka tejas (<span style="color:#FF5733;">radiance</span>) Surya (<span style="color:#FF5733;">Sun</span>) ke saman chamakta tha, aur unka rajya Indra ke Amaravati jaisa samruddh (<span style="color:#FF5733;">prosperous</span>) aur khushhaal (<span style="color:#FF5733;">happy</span>) tha. Ayodhya unke shasan me ek swarg (<span style="color:#FF5733;">heaven</span>) ke jaisi lagti thi — nyay, samriddhi aur prem se bhari hui.
        """
        create_image_text_layout("attached_assets/chapter1/1.7.2.jpg", text3, layout="side", image_position="right")

    # Chapter8
    with st.expander("Chapter 1.8 - King Dasaratha wants a son, so he plans a special yajna (sacrifice)"):
        text1 = """
Ayodhya ke mahaan aur dharmic (<span style="color:#FF5733;">righteous</span>) Raja Dasharatha apni tapasya (<span style="color:#FF5733;">austerities</span>) aur punya (<span style="color:#FF5733;">good deeds</span>) ke bawajood, ek baat se bahut dukhi the — unke koi putra (<span style="color:#FF5733;">son</span>) nahi tha. Ek din unhone man hi man socha,
"Main Ashwamedh Yagya (<span style="color:#FF5733;">horse sacrifice</span>) karunga, taaki mujhe ek putra prapt ho." Yeh soch kar Raja Dasharatha ne apne mantriyon ki sabha (<span style="color:#FF5733;">meeting</span>) bulayi aur mukhya mantri Sumantra se kaha, "Turant sab rishi (<span style="color:#FF5733;">sages</span>) aur purohit (<span style="color:#FF5733;">priests</span>) ko bulao."
        """
        create_image_text_layout("attached_assets/chapter1/1.8.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Sumantra ne turant Suyagna, Vamadeva, Javali, Kasyapa aur Maharishi Vasishtha jaise gyaani (<span style="color:#FF5733;">wise</span>) brahminon ko bula liya. Raja Dasharatha ne sab mahapurushon ko pranam karke kaha,
"Main hamesha dharma ka palan karta hoon, par ab tak mujhe putra prapt nahi hua. Main yeh Ashwamedh Yagya karna chahta hoon, kripya mujhe batayein ki ise safal (<span style="color:#FF5733;">successful</span>) kaise banaya jaaye." Rishiyon ne Raja ki ichha sun kar prasanna (<span style="color:#FF5733;">pleased</span>) hoke kaha,
"Rajan, aapne bahut sahi nirnay liya hai. Yeh yagya aapke sapne ko poora karega. Iska sthal (<span style="color:#FF5733;">place</span>) Sarayu nadi ke uttar kinare (<span style="color:#FF5733;">north bank</span>) par chuna jaye."

Yeh sunkar Raja Dasharatha bahut khush hue. Unhone apne mantriyon ko aadesh diya ki yagya ke liye sab taiyariyan karo, ghode (<span style="color:#FF5733;">horse</span>) ko suraksha ke saath chhodo aur yagya shala (<span style="color:#FF5733;">sacrificial pavilion</span>) banwao. Raja ne kaha,
"Dhyaan rahe, yagya ke dauran kisi ko dukh na ho. Agar kisi ko peeda hui, to yagya ka phal (<span style="color:#FF5733;">result</span>) khatam ho jaayega. Isliye poori shraddha aur niyam ke saath iska samapan karo."
        """
        create_image_text_layout(text_content=text2, layout="full")


        text3 = """

Mantriyon ne kaha, "Rajan, aapka aadesh sar aankhon par!" Rishiyon ne Raja ko ashirwad diya aur chale gaye. Uske baad Raja Dasharatha apne rajmahal me gaye, jahan unki teen raaniyaan rehti thi — sab unse bahut prem karti thi.Raja ne muskura kar kaha,
"Main ek yagya karne ja raha hoon taaki humare ghar ek putra janme. Tum sab bhi iske niyam (<span style="color:#FF5733;">discipline</span>) ka paalan karna."Yeh sunkar sab raaniyan khushi se chamak uthi, jaise sardi ke baad khile hue phoolon (<span style="color:#FF5733;">flowers</span>) par dhoop chamak rahi ho.
        """
        create_image_text_layout("attached_assets/chapter1/1.8.1.jpg", text3, layout="side", image_position="right")

    # Chapter9
    with st.expander("Chapter 1.9 - Sumantra tells a story about a son being born"):

        text1 = """
Ek din, jab Raja Dasharath apne yagya (<span style="color:#FF5733;">sacrifice</span>) ki taiyari kar rahe the, tab unke mantri Sumantra ne unse kaha,
“Maharaj, maine ek bahut purani parampara suni thi — ek bhavishyavani (<span style="color:#FF5733;">prophecy</span>) — jo bade tapasvi (<span style="color:#FF5733;">sage</span>) Sanatkumara ne kahi thi. Uske hisaab se aapko ek putra zarur prapt hoga.”

Sumantra ne bataya ki Sanatkumara ne kaha tha:
“Rishi Kashyap ke vansh (<span style="color:#FF5733;">lineage</span>) me ek tapasvi hoga jiska naam Vibhandak hoga, aur uska beta Rishyasringa. Ye Rishyasringa apne pita ke saath van (<span style="color:#FF5733;">forest</span>) me rahenge — kisi aur aadmi ya stree (<span style="color:#FF5733;">woman</span>) se door. Vah dono din-raat bhagwan ki aradhana (<span style="color:#FF5733;">worship</span>) karte rahenge.”
        """
        create_image_text_layout("attached_assets/chapter1/1.9.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Phir Sumantra ne ek purani ghatna (<span style="color:#FF5733;">incident</span>) batayi —
“Anga desh me ek raja tha, Lomapada naam ka. Usne apni praja ke saath anyaay (<span style="color:#FF5733;">injustice</span>) kiya, isliye uske rajya me sukhha (<span style="color:#FF5733;">drought</span>) pad gaya. Sab log pareshan ho gaye. Tab Raja Lomapada ne apne purohit (<span style="color:#FF5733;">priests</span>) aur brahminon se poocha,
‘Batao, main kaunsa prayaschit (<span style="color:#FF5733;">repentance</span>) karu taaki ye sukhha khatam ho jaaye?’

Brahminon ne kaha,
‘Raja, agar aap Rishi Vibhandak ke putra Rishyasringa ko yahan bula lenge, to varsha (<span style="color:#FF5733;">rain</span>) zarur aayegi. Aap apni beti Shanta ka vivaah (<span style="color:#FF5733;">marriage</span>) us tapasvi se kar dijiyega.’” Par jab Raja Lomapada ne ye kaam apne mantriyon ko diya, to sab dare —
“Rishi bahut shaktishaali hain, humein unhe bulane ka sahas (<span style="color:#FF5733;">courage</span>) nahi hai.”
        """
        create_image_text_layout(text_content=text2, layout="full")


        text3 = """
Tab unhone ek upaay (<span style="color:#FF5733;">plan</span>) socha —
“Hum kuch sundar nartakiyan (<span style="color:#FF5733;">courtesans</span>) bhejte hain, jo apni madhur (<span style="color:#FF5733;">sweet</span>) baaton se Rishyasringa ko manayengi aur unhe rajya me le aayengi.” Aur jab Rishyasringa rajya me aaye, tab sach me baarish hone lagi aur Anga desh me sukhha khatam ho gaya.
Uske baad Raja Lomapada ne apni beti Shanta ka vivaah unse kar diya.

Sumantra ne Dasharath se kaha,
“Maharaj, isi Rishi Rishyasringa ke dwarā aapko bhi ek putra prapt hoga.” Ye sunkar Raja Dasharath bahut prasann (<span style="color:#FF5733;">delighted</span>) hue aur bola,
“Mujhe aur batao Sumantra, Raja Lomapada ne kaise us mahaan rishi ko apne rajya tak laya tha.”

        """
        create_image_text_layout("attached_assets/chapter1/1.9.2.jpg", text3, layout="side", image_position="right")

    # Chapter10
    with st.expander("Chapter 1.10 - How Rishyasringa comes to King Lomapada’s court"):

        text1 = """
Jab Raja Dasharath ne Sumantra se poocha, “Kaise us mahaan rishi ko rajya tak laya gaya tha?” — tab Sumantra ne poori kahani batani shuru ki:

“Maharaj,” Sumantra bole,
“Raja Lomapada ke mantriyon ne kaha,
‘Humein ek yojna (<span style="color:#FF5733;">plan</span>) mil gayi hai jisse hum Rishi Rishyasringa ko yahan la sakte hain. Vah van (<span style="color:#FF5733;">forest</span>) me rehte hain, aur apni tapasya (<span style="color:#FF5733;">penance</span>) aur dhyaan me poore mann se lage hue hain. Unhe sansaarik sukh (<span style="color:#FF5733;">worldly pleasures</span>) ka zara bhi gyaan nahi hai.’
        """
        create_image_text_layout("attached_assets/chapter1/1.10.1.jpg", text1, layout="side", image_position="left")


        text2 = """
‘To hum unhe manoranjak vasthuon (<span style="color:#FF5733;">things that please the senses</span>) se akarshit karenge. Sundar aur sobha se saja hua kuch nartakiyan (<span style="color:#FF5733;">courtesans</span>) vahaan jaakar apne madhur geet aur mohak (<span style="color:#FF5733;">charming</span>) vyavhaar se unhe rajya tak le aayengi.’” Raja Lomapada ko ye upaay pasand aaya aur usne turant anumati (<span style="color:#FF5733;">permission</span>) de di.

Phir ve nartakiyan van me gayin, aur rishi ke ashram ke paas apna nivaas banaya. Rishyasringa ke pita, Rishi Vibhandak, unka bahut dhyaan rakhte the, isliye vah kabhi ashram ke bahar nahi jaate the — na kisi aadmi ko dekha tha, na kisi stree (<span style="color:#FF5733;">woman</span>) ko. Lekin ek din, vidhi (<span style="color:#FF5733;">destiny</span>) ke likhe se, Rishyasringa thoda ashram ke bahar nikle. Tab unhone dekha — kuch sundar stree, rang-birangi poshaak (<span style="color:#FF5733;">clothes</span>) pehne hue, geet ga rahi hain.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Ve unke paas gaye, aur poochha gaya,
“Tum kaun ho, kiske putra ho, aur is andhkaar van me kyun rehte ho?” Rishyasringa ne nirmalta se jawab diya,
“Main Rishi Vibhandak ka beta hoon, mera naam Rishyasringa hai. Mera ashram yahi paas me hai — aap sab wahan chalo, main aapka satkaar (<span style="color:#FF5733;">hospitality</span>) karna chahta hoon.”

Nartakiyan muskura kar unke saath gayin. Rishyasringa ne unka svagat paani, phal aur jad-mool (<span style="color:#FF5733;">roots</span>) se kiya. Par un streeyon ne apne saath mithaai (<span style="color:#FF5733;">sweets</span>) aur pakwaan (<span style="color:#FF5733;">delicacies</span>) laaye the, aur bola,
“Ye khaas aapke liye laye hain, kripya swikaar kijiye.”
        """
        create_image_text_layout("attached_assets/chapter1/1.10.2.jpg", text3, layout="side", image_position="right")


        text4 = """
Rishyasringa, jinhone kabhi aisa bhojan (<span style="color:#FF5733;">food</span>) nahi chhuka tha, use phal samajh kar kha gaye.
Thodi der baad, nartakiyan chintit (<span style="color:#FF5733;">worried</span>) hokar kehne lagi,
“Ab humein upvaas (<span style="color:#FF5733;">fast</span>) karna hai,” aur vah wahan se chali gayin.

Unke jaane ke baad, Rishyasringa ka man udyas (<span style="color:#FF5733;">sad</span>) ho gaya. Agle din vah aur bhi bechain (<span style="color:#FF5733;">restless</span>) dikhai diye. Tab phir se wahi stree wahan aayi — aur boli,
“Hey sundar muni, aaj aap humare ashram chalo, hum aapka aur acchha swagat karenge.” Rishyasringa unke saath chal pade.
Jaise hi ve Anga nagar (<span style="color:#FF5733;">city</span>) me pravesh (<span style="color:#FF5733;">enter</span>) hue, turant baarish (<span style="color:#FF5733;">rain</span>) hone lagi! Poora rajya khushiyon se bhar gaya.
        """
        create_image_text_layout(text_content=text4, layout="full")

        text5 = """




Raja Lomapada samajh gaye — “Rishyasringa ji hamare rajya me aa gaye hain!”
Vah turant unse milne gaye, pranam kiya, paani aur bhojan (<span style="color:#FF5733;">food offerings</span>) diya, aur vinamrata se (<span style="color:#FF5733;">humbly</span>) kaha,
“Hey maharshi, kripya apne pita Rishi Vibhandak se krodh (<span style="color:#FF5733;">anger</span>) na karne ka ashirvaad dijiye.”

Phir Raja ne apni beti Rajkumari Shanta ka vivaah (<span style="color:#FF5733;">marriage</span>) Rishyasringa se kar diya.
Aur us din ke baad se, Rishyasringa apni patni Shanta ke saath khushi aur samman (<span style="color:#FF5733;">respect</span>) se Anga nagar me rahne lage.

        """
        create_image_text_layout("attached_assets/chapter1/1.10.3.jpg", text5, layout="side", image_position="left")

    # Chapter11
    with st.expander("Chapter 1.11 - Rishyasringa comes to Ayodhya"):

        text1 = """
Sumantra ne Raja Dasharath se kaha:
“Maharaj, Sanatkumara ne kaha tha ki — ‘Ikshvaku vansh me ek dharmic aur satya-premi (<span style="color:#FF5733;">truth-loving</span>) raja hoga, jiska naam Dasaratha hoga. Vah Anga ke Raja Lomapada se mitrata karega.

Raja Dasaratha apne mitra Lomapada ke paas jaakar unse anurodh karega ki Rishyasringa, Rajkumari Shanta ka pati, uski sahayata kare ek vishesh yajna (<span style="color:#FF5733;">sacrifice</span>) me, taaki usko putra prapt ho. Lomapada raja soch-vichar ke baad Rishyasringa ko Dasaratha ke saath jaane ki anumati (<span style="color:#FF5733;">permission</span>) dega.
        """
        create_image_text_layout("attached_assets/chapter1/1.11.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Is yajna ke dwara, Raja Dasaratha ke chaar putra honge, jo apaar veerta (<span style="color:#FF5733;">valour</span>) wale honge aur poore vishwa me prasiddh honge, aur unke vansh ki mahima ko badhaenge.’ Sanatkumara ne ye katha Satya-Yuga ke prarambh me sunayi.

Raja Dasharath ne apne mantri Sumantra ki salah ko maana aur turant Guru Vasishtha ko is yojna ke baare me bataya. Vasishtha ne bhi is yojna me sahmati di. Phir raja, apni raniyon, mantriyon aur purohits (<span style="color:#FF5733;">priests</span>) ke saath, Rishyasringa ke rajya ke liye nikal padhe. Kai van aur nadiyon ko paar karte hue, ve Raja Lomapada ke rajya pahunch gaye.

Wahan unhone Rishyasringa ko dekha — chamak rahe the, jaise agni (<span style="color:#FF5733;">fire</span>) me ujala. Raja Lomapada ne mitrata aur samman dikhate hue Dasharath ka pranam kiya aur Rishyasringa ko unki sahmati batayi. Saat din tak Dasharath ne Lomapada ke rajya me atithi seva (<span style="color:#FF5733;">hospitality</span>) ka anand liya. Fir raja ne kaha,
“Hey Maharaj, ab main ek vishesh karya (<span style="color:#FF5733;">important task</span>) karna chahta hoon. Kripya Shanta aur unke pati ko mere rajya le jaane dein, taaki ve meri sahayata karein.” Raja Lomapada ne kaha,
“Jaayen, aap apni patni ke saath Dasarath ke rajya me ja sakte hain.”
        """
        create_image_text_layout(text_content=text2, layout="full")


        text3 = """
Rishyasringa ne is aadesh ko maana aur apni patni Shanta ke saath Raja Dasharath ke saath Ayodhya ke liye chal pade.

Raja Dasharath ne apne mitra ko vida (<span style="color:#FF5733;">farewell</span>) di aur tez gati se sandeshvahak (<span style="color:#FF5733;">messengers</span>) bheje, taaki Ayodhya me rishi ke aagman (<span style="color:#FF5733;">arrival</span>) ki taiyari ho jaaye. Ayodhya ke logon ne sari taiyari ki aur bahut khushi se rishi aur unki patni ka swagat kiya — jaise Indra Kasyapa ko swarg me samman (<span style="color:#FF5733;">tribute</span>) dete hain.

Rishi aur Rajkumari Shanta ko rajmahal ke antaral (<span style="color:#FF5733;">inner apartments</span>) me laya gaya. Raja Dasharath aur raniyon ne unka pooja (<span style="color:#FF5733;">honour</span>) aur samman (<span style="color:#FF5733;">respect</span>) kiya.
Is tarah Rishyasringa aur Shanta Ayodhya me shanti aur khushi ke saath rehne lage, jaise Brihaspati Mahendra nagar me apna nivaas karte hain.
        """
        create_image_text_layout("attached_assets/chapter1/1.11.2.jpg", text3, layout="side", image_position="right")

    # Chapter12
    with st.expander("Chapter 1.12 - Rishyasringa agrees to help with the sacrifice"):

        text1 = """
Samay beet gaya aur bahar (<span style="color:#FF5733;">spring</span>) ka mausam aa gaya. Raja Dasharath ne socha, “Aaj shubh din hai, ab main yajna (<span style="color:#FF5733;">sacrifice</span>) shuru karoon.”  Raja ne Rishyasringa ke saamne jhuk kar pranam kiya aur unse kaha:
“Hey Mahapurush (<span style="color:#FF5733;">god-like sage</span>), kripya meri sahayata kijiye, taaki mere vansh (<span style="color:#FF5733;">dynasty</span>) ki raksha ho aur mujhe putra prapt ho.”

Rishyasringa ne sweekriti (<span style="color:#FF5733;">agree</span>) di aur kaha,
“Raja, aap yajna ke liye saari vastu (<span style="color:#FF5733;">sacrificial materials</span>) pradan kijiye aur ghoda (<span style="color:#FF5733;">horse</span>) chhodne dein.” Raja ne turant mantri Sumantra ko aadesh diya ki Veda ke gyaan wale purohits (<span style="color:#FF5733;">priests</span>) ko bulaya jaaye aur sages Vamadeva, Javali, Kasyapa, Vasishtha aur anya mahan brahmins ko amantrit (<span style="color:#FF5733;">invite</span>) kiya jaaye.
        """
        create_image_text_layout("attached_assets/chapter1/1.12.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Sumantra ne shighra (<span style="color:#FF5733;">hurry</span>) se sabhi brahmins ko sammaan ke saath raja ke paas laya. Raja ne unka pranam kiya aur vinamrata se kaha:
“Hey Sages, meri ichha hai ki mujhe putra prapt ho, isliye main Ashwamedha yajna (<span style="color:#FF5733;">horse-sacrifice</span>) kar raha hoon. Aapke margdarshan se aur Rishyasringa ke ashirwad se, mujhe safalta milegi.”

Brahmins ne raja ko salah di:
“Raja, aapka iccha satya aur dharmik hai. Aapko chaar veer (<span style="color:#FF5733;">valiant</span>) putra milenge, jo poore vishwa me prasiddh honge.” Raja ne apne mantriyon se kaha:
“Chaar uchit purohits (<span style="color:#FF5733;">high priests</span>) ko bulao aur ghoda chhodo, 400 veer yoddhaon ke suraksha me. Sarayu nadi ke kinare yajna ka mandap (<span style="color:#FF5733;">pavilion</span>) banwayo aur suraksha ke niyam (<span style="color:#FF5733;">protective rites</span>) dhyaan me rakho.”
        """
        create_image_text_layout(text_content=text2, layout="full")


        text3 = """
Raja ne ye bhi kaha ki yajna ke dauran kisi ko bhi dukh ya hani na ho, warna yajna ka fal shunya ho jaata hai. Mantri aur purohits ne raja ki baat ko maana aur kaam shuru kiya. Brahmins ne vishwas dilaya ki yajna bina kisi badha ke poora hoga aur pranam karke wapas chale gaye. Brahmins ke chale jaane ke baad, raja ne apne mantriyon se vida li aur apni raniyon ke saath private apartments me chale gaye.
        """
        create_image_text_layout("attached_assets/chapter1/1.12.2.jpg", text3, layout="side", image_position="right")

    # Chapter13
    with st.expander("Chapter 1.13 - The sacrifice begins"):
        text1 = """
Agla saal aaya, bahar (<span style="color:#FF5733;">spring</span>) ka mausam phir se chhaya. Raja Dasharath ne socha: “Ab main putra ke liye yajna (<span style="color:#FF5733;">sacrifice</span>) shuru karoon.” Raja ne Guru Vasishtha ke saamne pranam kiya aur vinamrata se kaha:
“O Mahapurush (<span style="color:#FF5733;">Great Sage</span>), kripya is pavitra kriya (<span style="color:#FF5733;">holy ceremony</span>) ko dharmik parampara ke anusar poora kijiye. Aap dayaalu hain aur mere Guru bhi hain, is yajna ka bhar aap uthaiye.”

Vasishtha ne kaha:
“Jaise aap chahte hain, main vaisa hi karunga.” Phir Shri Vasishtha ne purohits (<span style="color:#FF5733;">priests</span>), kalakaar (<span style="color:#FF5733;">artists</span>), lekhak (<span style="color:#FF5733;">writers</span>), naatakkaar (<span style="color:#FF5733;">actors</span>), nrityakar (<span style="color:#FF5733;">dancers</span>) ko bulaya.
        """
        create_image_text_layout("attached_assets/chapter1/1.13.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Vasishtha ne unse kaha:
“Raja ke aadesh par maha-yajna shuru kijiye. Hazaron eent (<span style="color:#FF5733;">bricks</span>) lao aur mandap, mehmaan-gharon aur brahmins ke liye suvidhaayein tayar kijiye. Duri-dur ke logon ke liye bhi aaramdayak makaan aur bhojan ki vyavastha ho. Sabhi ko vinamrata aur maryada se seva do, kisi ko krodh, lobh ya ichha se hani na ho. Sabko samman mile taaki kaam safal ho.” Logon ne kaha:
“Humein aadesh samajh aa gaya, O Maharishi (<span style="color:#FF5733;">Sage</span>), hum sab poora karenge.”

Phir Vasishtha ne Sumantra se kaha:
“Sabhi dharmic rajyon ke rajaon, brahmins, kshatriya, vaishya aur shudra ko amantran (<span style="color:#FF5733;">invite</span>) bhejo. Sabse pehle Mithila ke mahaan Raja Janaka ko bulao, phir Kashi, Kaikeya, Anga ke Raja Lomapada aur Magadha ke Raja ko amantrit karo. Baaki poorvi aur dakshini deshon ke raja bhi aayein.”
        """
        create_image_text_layout(text_content=text2, layout="full")


        text3 = """
Sumantra ne sabhi rajyon me teerath (<span style="color:#FF5733;">messengers</span>) bheje aur kuch rajaon ko sath lekar aya. Kuch hi dino me, door-daraz ke raja apni uphaar-saman (<span style="color:#FF5733;">gems & gifts</span>) ke saath pahunche.

Vasishtha ne Raja Dasharath ko kaha:
“O Raja, sab raja aaye aur unka samman kiya gaya. Ab aap yajna sthal (<span style="color:#FF5733;">sacrificial ground</span>) jaake sab saman aur vyavastha dekhein. Sab kuch shubh aur sahi hai.” Rishyasringa ko mukhya purohit (<span style="color:#FF5733;">chief priest</span>) chuna gaya aur yajna shuru hua. Raja aur raniyan prarambhik kriyaon (<span style="color:#FF5733;">preliminary rituals</span>) me lage.
        """
        create_image_text_layout("attached_assets/chapter1/1.13.2.jpg", text3, layout="side", image_position="right")

    # Chapter14
    with st.expander("Chapter 1.14 - All the right rituals are performed"):

        text1 = """
Saal bhar ghoomne ke baad, ghoda (<span style="color:#FF5733;">horse</span>) wapas aaya aur Sarayu nadi ke kinare Raja Dasharath ka yajna jaari raha. Rishyasringa aur anya purohits (<span style="color:#FF5733;">priests</span>) ne sabhi kriyaayein sahi dhang se poori ki. Pravargya aur Upasada jaise vishesh karm (<span style="color:#FF5733;">special rites</span>) poore kiye gaye. Brahmins ne devtaon ki pooja ki aur Indra ko yajna ka hissa arpit kiya. Sabne soma-ras (<span style="color:#FF5733;">sacred juice</span>) piya, jo paap ko door karta hai.

Yajna me sab kuch shastra ke anusar aur sahi dhang se hua. Brahmins, sevak, aur anya log sabhi ko aahar (<span style="color:#FF5733;">food</span>) aur seva (<span style="color:#FF5733;">hospitality</span>) di gayi. Buzurg, bachche aur mahilayein bhi sampoorna suvidha prapt kar rahe the. Raja ne vastu, sona (<span style="color:#FF5733;">gold</span>), aur dhan sabko bakshe, aur khana-pina har kisi ke liye prabandhit tha.
        """
        create_image_text_layout("attached_assets/chapter1/1.14.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Beech-beech me pundit (<span style="color:#FF5733;">scholars</span>) bhi gyaan-vivad karte rahe. Yajna ke sthaan par 18 khambhe (<span style="color:#FF5733;">pillars</span>) lagaye gaye, har ek alag lakdi ka, sone se sajaya gaya aur phool aur chandan se sajaaya gaya. Fire pits aur yajna ke samagriyon ka dhyaan brahmins aur masons ne rakha.

Ghoda aur anya pashu yajna ke niyam ke anusar bandh diye gaye. Queen Kaushalya ne ghode ko teen talwar ke vaar se arpit kiya aur raat bhar uske paas rehti rahi. Brahmins ne ghode ka charbi aag me arpit kiya aur King Dasharath ne paap ka prashaman kiya.  Yajna ke teen din me Agnishtoma, Uktha aur Atiratra jaise rites hue. Jyotishtoma, Vishnajit, Abhijit jaise maha-yajna bhi kiye gaye.

Yajna ke ant me Raja Dasharath ne chaur pradesh (<span style="color:#FF5733;">four parts</span>) apne raja ke daakshina (<span style="color:#FF5733;">charity</span>) me diye aur bade dharmik udaharan ke roop me bhoomi aur dhan brahmins ko arpit kiya. Brahmins ne kaha: “O Raja, hum itni badi bhoomi aur rajya sambhal nahi sakte, kripya humko kuch chhota uphaar dein.” Raja ne 1 crore (<span style="color:#FF5733;">100 million</span>) sona aur 4 crore (<span style="color:#FF5733;">400 million</span>) chandi diye. Har ek ko uska nyayik hissa mila. Dusre brahmins aur yajna dekhne aaye logon ko bhi dhan aur uphaar diye gaye. Ek bhikshuk ne raja ki diamond ki kangan maangi aur raja ne bina hichkichaye de diya.
        """
        create_image_text_layout(text_content=text2, layout="full")


        text3 = """
Brahmins santusht huye, Raja Dasharath ne unka baar-baar pranam kiya. Brahmins ne Raja ko ashirwad diya ki ve sada dharmik aur veer bane rahein. Tab Raja ne Rishyasringa se poocha:
“O Mahapurush, mujhe aur kya karna chahiye taaki mujhe putra ho?” Rishyasringa ne kaha:
“O Raja, aapko chaar putra honge, jo rajvansh ko sada banaye rakhenge.”

        """
        create_image_text_layout("attached_assets/chapter1/1.14.2.jpg", text3, layout="side", image_position="right")

    # Chapter15
    with st.expander("Chapter 1.15 - Shri Vishnu decides to take birth on Earth"):

        text1 = """
Rishyasringa ne yajna (<span style="color:#FF5733;">sacrifice</span>) shantipurna tareeke se poora kiya. Tab sab devas (<span style="color:#FF5733;">gods</span>), gandharvas (<span style="color:#FF5733;">celestial musicians</span>) aur rishis (<span style="color:#FF5733;">sages</span>) us pavitra agni ke paas ikattha hue aur Brahma se prarthana karne lage:

“Hey Bhagwan, woh Ravana (<span style="color:#FF5733;">evil demon</span>) humein aur devtaon ko satata hai — uski taakat se hum pareshan hain. Usne Indra ko bhi haraaya, rishiyon ko tang kiya aur anek buraiyaan ki. Kripya use hataa do.”
        """
        create_image_text_layout("attached_assets/chapter1/1.15.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Brahma ne socha aur bola,
“Ravana ko koi deva (<span style="color:#FF5733;">god</span>), gandharva ya yaksha maar nahin sakta — usne ye boons paaye the. Lekin usne ‘insaan’ se amaratva (<span style="color:#FF5733;">invulnerability</span>) ki maang nahin ki — isliye sirf manav (<span style="color:#FF5733;">human</span>) hi use hara sakta hai.”

Tabhi Shri Vishnu (jo sabka rakshak hai), apni shankh (<span style="color:#FF5733;">conch</span>), chakra (<span style="color:#FF5733;">discus</span>) aur gada (<span style="color:#FF5733;">mace</span>) ke saath prakat huye. Sab devta unke charanon me shraddha se aaye aur vinamrata se bole: “Hey Madhusudana (Vishnu), aap hi hamara asraam (<span style="color:#FF5733;">refuge</span>) ho. Kripya insaan ke roop me Avatar le ke Ravana ka vinash karo. Humari raksha karo.” 
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Vishnu ne daya se kaha,
“Thik hai — main manav roop me utarunga. Main Ravana aur uske saathi sabko hara dunga. Aur is duniya me insaanon ke liye 11,000 saal tak raj karunga.”

Phir Vishnu ne nishchay kiya ki wo Raja Dasaratha ke ghar chaar putron ke roop me janam lenge — taki Ravana ka vinash ho aur dharma (<span style="color:#FF5733;">righteousness</span>) phir sthapit ho. Sab devta, gandharva aur rishis khush hokar gaye aur Vishnu ko prashansa (<span style="color:#FF5733;">praise</span>) di —
“Hey Lord, duniya se is buraai ko mita do aur phir apne divya ghar (<span style="color:#FF5733;">heaven</span>) me wapas chalo.”
        """
        create_image_text_layout("attached_assets/chapter1/1.15.2.jpg", text3, layout="side", image_position="right")

    # Chapter16
    with st.expander("Chapter 1.16 - Vishnu plans to be born as Dasaratha’s four sons"):        

        text1 = """
Sab devtaon ki prarthana (<span style="color:#FF5733;">prayer</span>) sun kar Shri Narayana (Lord Vishnu) muskuraye aur pyar se bole —
“Hey Devtaon, batao to sahi, woh dusht (<span style="color:#FF5733;">evil</span>) Ravana ko kaise maara jaa sakta hai?” Sab devta ek sur me bole, “Hey Prabhu, aap hi insaan (<span style="color:#FF5733;">human</span>) roop me janm lijiye aur usse yudh (<span style="color:#FF5733;">battle</span>) me maar dijiye! Ravana ne Brahma ji se varadan (<span style="color:#FF5733;">boon</span>) paaya hai ki use koi devta, daanav (<span style="color:#FF5733;">demon</span>) ya gandharva nahi maar sakta. Lekin usne insaan se suraksha nahi maangi, kyunki use laga insaan kamzor hai.” Vishnu ji ne haan me sir hilaaya aur kaha,
“Thik hai — main insaan roop me prithvi (<span style="color:#FF5733;">earth</span>) par jaunga. Aur Ravana ka ant (<span style="color:#FF5733;">end</span>) karunga.”

        """
        create_image_text_layout("attached_assets/chapter1/1.16.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Us samay Raja Dasharatha Ayodhya me ek putra prapti yagya (<span style="color:#FF5733;">sacrifice for a son</span>) kar rahe the. Vishnu ji ne socha,
“Main isi mahaan aur nyaypriya (<span style="color:#FF5733;">just</span>) raja ke ghar janm lunga.” Tabhi agni (<span style="color:#FF5733;">fire</span>) ke beech se ek divya purush (<span style="color:#FF5733;">heavenly being</span>) nikle — unka roop sooraj jaisa chamak raha tha, unke haath me ek sunehra patra (<span style="color:#FF5733;">golden bowl</span>) tha, jisme payasa (<span style="color:#FF5733;">sweet rice pudding</span>) tha — devtaon dwara banaaya gaya.

Wo bola, “Hey Raja Dasharatha, ye payasa Prajapati ne bheja hai. Isse apni raaniyon ko khilao — tumhe chaar putra milenge.” Raja Dasharatha ne us patra ko shraddha se apne mastak (<span style="color:#FF5733;">forehead</span>) se lagaya aur dil se khushi me bhar gaye — jaise koi garib aadmi khazana paale! Phir Dasharatha ne payasa apni teen raaniyon me baanta — Aadha Rani Kaushalya ko diya,

        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Ek-teehaai Rani Sumitra ko, Aur ek-hissa Rani Kaikeyi ko. Baad me jo thoda bacha, wo bhi Sumitra ko de diya. Sab raaniyan bahut khush ho gayin aur bhagwan ka dhanyavaad kiya. Kuch samay baad, unke garbh (<span style="color:#FF5733;">wombs</span>) me prakash chamakne laga — jaise sooraj ki roshni. Raja Dasharatha ka mann khushi se bhar gaya — ab unka sabse bada sapna poora hone wala tha! 
        """
        create_image_text_layout("attached_assets/chapter1/1.16.2.jpg", text3, layout="side", image_position="right")

    # Chapter17
    with st.expander("Chapter 1.17 - Gods take birth as monkey warriors"):

        text1 = """
Ab jab Bhagwan Vishnu Raja Dasharatha ke ghar chaar putron ke roop me aane wale the, tab Brahma ji ne sab devtaon se kaha — “Hey Devtaon! Bhagwan Vishnu ab manav (<span style="color:#FF5733;">human</span>) roop me dharti par janm lene wale hain. Unki madad karne ke liye tum sab bhi vanar kul (<span style="color:#FF5733;">monkey tribe</span>) me janm lo. Tum sab shaktishaali, buddhimaan (<span style="color:#FF5733;">wise</span>), aur yudh-vidya (<span style="color:#FF5733;">warfare</span>) me nipun (<span style="color:#FF5733;">skilled</span>) yoddha ban kar unka saath do.” 

Brahma ji ne aur kaha — “Tumme se kuch log apsara (<span style="color:#FF5733;">nymphs</span>), gandharva, aur tapasiya (<span style="color:#FF5733;">female ascetics</span>) ke roop me bhi janm lo, jisse ve sab shaktishaali vanar putron ko janm dein.” Phir Brahma ji muskuraaye aur bole, “Yaad hai? Jab maine kabhi jamhai (<span style="color:#FF5733;">yawn</span>) li thi, tab ek mahaan bhalu (<span style="color:#FF5733;">bear</span>) Jambavan janma tha!” To sab devta apni apni shakti se vanar yoddhaon ko janm dene lage —
        """
        create_image_text_layout("attached_assets/chapter1/1.18.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Indra ne Bali ko utpann kiya, Surya dev (<span style="color:#FF5733;">Sun god</span>) ne Sugriva ko, Brihaspati ne buddhimaan Tara ko, Kubera ne Gandhamadana ko, Vishwakarma ne shaktishaali Nala ko, Agni dev (<span style="color:#FF5733;">Fire god</span>) ne tejesvi Nila ko,
Ashwini Kumars ne Minda aur Dvivida ko, Varuna ne Suchena ko,
Pavana dev (<span style="color:#FF5733;">Wind god</span>) ne ek anokhe aur balwan putra Hanuman ko janm diya! Hanuman ka sharir vajra (<span style="color:#FF5733;">diamond</span>) jaisa kathin tha aur unki gati (<span style="color:#FF5733;">speed</span>) garud (eagle) jaisi tez!
Buddhi aur shakti me unka koi sammaan (<span style="color:#FF5733;">equal</span>) nahi tha. Dheere dheere, hazaaron vanar, bhalu aur kapi (<span style="color:#FF5733;">chimpanzee</span>) janm lene lage. Sabke andar apne devta jaise guna (<span style="color:#FF5733;">qualities</span>) the — shaktishaali, veer (<span style="color:#FF5733;">brave</span>), aur nirmal hriday (<span style="color:#FF5733;">pure-hearted</span>). 
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Ye sab vanar parvat (<span style="color:#FF5733;">mountain</span>) tod sakte the, bade bade ped ukhaad sakte the, aur bijli (<span style="color:#FF5733;">lightning</span>) ki tarah tezi se udh sakte the! 
Unki dahad (<span style="color:#FF5733;">roar</span>) se jungle ghoom uthta tha, aur panchhi (<span style="color:#FF5733;">birds</span>) bhi aasman se gir jaate the! Unke neta (<span style="color:#FF5733;">leaders</span>) the Bali aur Sugriva, aur unke saathi the Hanuman, Nala, aur Nila jaise mahan yoddha.
Ye sab vanar veer ban kar jungle aur parvaton me rehne lage, prakriti (<span style="color:#FF5733;">nature</span>) ke rakshak aur dharti ke veer putra! Aur sabhi ka ek hi lakshya tha —
Bhagwan Vishnu ke roop Shri Ram ki sahayata karna, aur dusht (<span style="color:#FF5733;">evil</span>) Ravana ka vinash (<span style="color:#FF5733;">destruction</span>) karna! 
        """
        create_image_text_layout("attached_assets/chapter1/1.18.2.jpg", text3, layout="side", image_position="right")

    # Chapter18
    with st.expander("Chapter 1.18 - Dasaratha’s sons are born and grow up"):

        text1 = """
Raja Dasharatha ka yagya (<span style="color:#FF5733;">sacrifice</span>) safalta se poora hua. Sab devta (<span style="color:#FF5733;">gods</span>) apna hissa lekar apne-apne lok (<span style="color:#FF5733;">abodes</span>) wapas chale gaye.
Raja ne bhi apni patniyon (<span style="color:#FF5733;">queens</span>), sena (<span style="color:#FF5733;">army</span>), aur sab logon ke saath Ayodhya wapas aakar apne rajya me sukh se rehna shuru kiya. Kuch samay baad — chh (<span style="color:#FF5733;">six</span>) ritu beet gayi. Chaitra mahina ke navami tithi (<span style="color:#FF5733;">ninth day</span>) ko, jab Punarvasu nakshatra chal raha tha aur sab grah (<span style="color:#FF5733;">planets</span>) shubh sthiti me the, tab ek adbhut (<span style="color:#FF5733;">wonderful</span>) ghatna hui 

Queen Kaushalya ke garbh se janm hua Bhagwan Shri Ramachandra ka!
Unka janm hote hi poora mahal prakashit (<span style="color:#FF5733;">glowing</span>) ho gaya, aur Kaushalya maa Aditi devi ki tarah chamak rahi thi. Phir Queen Kaikeyi ke garbh se Bharat janme — vinamra (<span style="color:#FF5733;">humble</span>), sundar aur dharmic (<span style="color:#FF5733;">righteous</span>).
Aur Queen Sumitra ne janm diya Lakshman aur Shatrughna ko — dono veer (<span style="color:#FF5733;">brave</span>) aur dhanur-vidya (<span style="color:#FF5733;">archery</span>) me nipun (<span style="color:#FF5733;">skilled</span>). 
        """
        create_image_text_layout("attached_assets/chapter1/1.18.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Jab chaaron rajkumar janme, aasman me gandharv (<span style="color:#FF5733;">celestial singers</span>) geet gaane lage, apsara (<span style="color:#FF5733;">celestial nymphs</span>) nritya (<span style="color:#FF5733;">dance</span>) karne lagi, aur devtaon ne pushpon (<span style="color:#FF5733;">flowers</span>) ki varsha (<span style="color:#FF5733;">rain</span>) kar di. Ayodhya ke galiyon me utsav (<span style="color:#FF5733;">celebration</span>) chha gaya —
sab jagah dhol, shehnai aur nritya ke madhur swar gunj uthe
Raja Dasharatha ne brahmino ko daan (<span style="color:#FF5733;">donations</span>), sona, gaaye (<span style="color:#FF5733;">cows</span>) aur vastra (<span style="color:#FF5733;">clothes</span>) diye.

Barahve din (<span style="color:#FF5733;">12th day</span>) par Sage Vasishtha ne naamkaran (<span style="color:#FF5733;">naming ceremony</span>) kiya — Kaushalya ke putra ka naam rakha gaya Ramachandra, Kaikeyi ke putra ka naam Bharata, Sumitra ke dono putron ke naam Lakshmana aur Shatrughna. Sab chaaron putr sundar, veer aur vidya (<span style="color:#FF5733;">knowledge</span>) me pratibhashali (<span style="color:#FF5733;">brilliant</span>) the.
Par Shri Ram sabse alag chamak rahe the —
satya (<span style="color:#FF5733;">truth</span>), daya (<span style="color:#FF5733;">kindness</span>), aur maryada (<span style="color:#FF5733;">nobility</span>) ke moorti (<span style="color:#FF5733;">embodiment</span>). 

Ram aur Lakshman ek dusre ke bina kabhi na khate na sote the.
Jab bhi Ram shikar (<span style="color:#FF5733;">hunt</span>) par jaate, Lakshman dhanush-baan (<span style="color:#FF5733;">bow and arrows</span>) lekar unke saath hote. Wahi prem (<span style="color:#FF5733;">love</span>) Bharata aur Shatrughna ke beech bhi tha. Raja Dasharatha apne chaaron putron se utna hi khush the jitna Brahma ji chaar Vedaon se. 
Sab rajkumar Veda padhte, guru ko samman dete aur shastra-vidya (<span style="color:#FF5733;">weapon training</span>) me niptai dikhate.

Ek din, jab Raja Dasharatha apne mantriyon aur purohito ke saath baithak (<span style="color:#FF5733;">council</span>) me the, tab ek mahan rishi aaye —
Rishi Vishwamitra! Darban (<span style="color:#FF5733;">doorkeeper</span>) turant jaa kar bola —
“Prabhu, Gadhi putra Vishwamitra Muni, aapke dwar (<span style="color:#FF5733;">gate</span>) par aaye hain!” Raja Dasharatha aur Guru Vasishtha turant unka swagat (<span style="color:#FF5733;">welcome</span>) karne gaye.
Jaise Brahma ji Indra ka satkar karte hain, waise hi raja ne Vishwamitra ji ka abhinandan (<span style="color:#FF5733;">greeting</span>) kiya,
unhe arghya (<span style="color:#FF5733;">welcome water</span>) diya aur poorn samman se rajmahal me bulaya.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Vishwamitra ne rajya aur praja (<span style="color:#FF5733;">subjects</span>) ki khair-khabar li —
“Raja Dasharatha, kya sab praja sukh me hai? Kya sab yajna (<span style="color:#FF5733;">sacrifices</span>) dharm ke anusaar chal rahe hain? Kya aapke senapati wafadar hain? Kya mehmano ka satkar hota hai?”

Raja Dasharatha ne vinamrata (<span style="color:#FF5733;">humility</span>) se kaha —
“Hey Muniwar (<span style="color:#FF5733;">great sage</span>), aapka aana mere liye amrit (<span style="color:#FF5733;">nectar</span>) paane jaisa hai.
Aap mere liye devata tulya (<span style="color:#FF5733;">equal to gods</span>) hain. Kripya apna uddeshya (<span style="color:#FF5733;">purpose</span>) batayein.
Main aapki seva (<span style="color:#FF5733;">service</span>) ke liye sada taiyaar hoon.” Raja ke in madhur (<span style="color:#FF5733;">sweet</span>) aur dharmik shabdon ko sun kar Vishwamitra ji prasann (<span style="color:#FF5733;">pleased</span>) hue.
Aur tab shuru hui wo kahani jahan se Ram ke jeevan ka asli adhyay (<span style="color:#FF5733;">chapter</span>) aarambh hota hai…
        """
        create_image_text_layout("attached_assets/chapter1/1.18.2.jpg", text3, layout="side", image_position="right")

    # Chapter19
    with st.expander("Chapter 1.19 - Sage Vishvamitra asks for help"):

        text1 = """
Ek din jab Rishi Vishvamitra Ayodhya aaye, Raja Dasharatha ne unka poora satkar (<span style="color:#FF5733;">respect</span>) kiya. Vishvamitra ne vinamr (<span style="color:#FF5733;">humble</span>) tareeke se bola:
“Hey Maharaj, aapke shabdon se mujhe bada anand (<span style="color:#FF5733;">joy</span>) hua. Ab main apni baat bataunga — aap ise pura kijiye.”

Vishvamitra ne bataya ki jab bhi wo yajna (<span style="color:#FF5733;">sacrifice</span>) karte hain, do bade rakshas (<span style="color:#FF5733;">demons</span>) — Maricha aur Suvahu — aake us pooja ko bigaad dete hain. Ye dono bahut chalak (<span style="color:#FF5733;">clever</span>) aur bhayankar (<span style="color:#FF5733;">fearsome</span>) hain: jab yajna poorn hone wali hoti hai, ye aate hain aur agni ko lahu (<span style="color:#FF5733;">blood</span>) aur maans (<span style="color:#FF5733;">flesh</span>) se gandha (<span style="color:#FF5733;">defile</span>) kar dete hain. Isse Vishvamitra ke pavitra karya (<span style="color:#FF5733;">holy work</span>) fail ho jaate hain.
        """
        create_image_text_layout("attached_assets/chapter1/1.19.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Vishvamitra ne kaha:
“Main krodh me aakar inko shraap nahin de sakta, kyunki yajna ke samay gussa dikhana sahi nahi. Isliye mujhe aapke ek veer putra ki zaroorat hai — Shri Ramacandra. Aap apna putra mujhe dein — main use apni raksha me rakhunga. Ram in rakshason ko hara dega aur main usse vidya (<span style="color:#FF5733;">knowledge</span>) sikhaunga. Usse teenon lok (<span style="color:#FF5733;">three worlds</span>) me prasiddhi (<span style="color:#FF5733;">fame</span>) milegi.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Bas 10 din ke liye Rama ko mujhe de dijiyega — is dauran main apna yajna pura kar dunga. Vasishtha aur anya rishiyon ko bhi aap se salaah leni chahiye. Ye kaarya shubh (<span style="color:#FF5733;">auspicious</span>) hai, dukh mat karo.”

Vishvamitra ki baat sun kar Raja Dasharatha ka dil bhar aaya. Usko apne priye putra ko dena mushkil laga. Raja itna ashant hua ki wo dar ke maare behosh (<span style="color:#FF5733;">fainted</span>) ho gaya.
        """
        create_image_text_layout("attached_assets/chapter1/1.19.2.jpg", text3, layout="side", image_position="right")

    # Chapter20
    with st.expander("Chapter 1.20 - Dasaratha is unsure but thinks"):
        text1 = """

Raja Dasharatha behosh hone ke baad jaag uthe. Unhone turant kaha,
“Mera Rama abhi sirf pandrah saal ka hai — wo jawaan nahi hua. Kaise main apne pyare beta ko rakshason (<span style="color:#FF5733;">demons</span>) se ladne bhej doon? Main khud apni sena lekar jaunga. Mere anubhav (<span style="color:#FF5733;">experience</span>) wale yoddha aur sainik (<span style="color:#FF5733;">soldiers</span>) hi in dushmanon se ladein — Rama bachpan ka ladka hai!” Raja ne darate hue kaha, “Main kabhi nahi chahunga ki mera beta akela jaaye. Agar aap chahen toh mera pura sena aapke saath chale, par Rama ko mat le jaaiye. Main unhe apni jaan se bhi zyada pyara maanta hoon.”
        """
        create_image_text_layout("attached_assets/chapter1/1.20.1.jpg", text1, layout="side", image_position="left")


        text2 = """


Tab Rishi Vishvamitra (sage) ne samjhaya:
“Raja, ye rakshas bahut shaktishaali hain. Ravana aur uske saathi—Marica aur Suvahu—atyant chalak (<span style="color:#FF5733;">crafty</span>) aur maharathi (<span style="color:#FF5733;">great warriors</span>) hain. Unhe sirf insaan hara sakta hai, kyunki unhone devtaon se aise varadan (<span style="color:#FF5733;">boons</span>) liye the jo devtaon ko bhi nahi harne dete. Sirf ek sachcha, dharmik aur veer manav — jaise Rama — hi inka vinash (<span style="color:#FF5733;">destruction</span>) kar sakta hai.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Raja Dasharatha ye sab sun kar aur pareshan ho gaya. Uska dil bhar aaya aur wo gusse se hil gaya—kyunki apne beta ko dena uske liye bahut kathin tha.
Vishvamitra ko Raja ke in shabdon se krodh aa gaya — unhone socha ki samay zaya ho raha hai aur yajna (<span style="color:#FF5733;">sacrifice</span>) ruk nahi sakti.
        """
        create_image_text_layout("attached_assets/chapter1/1.20.2.jpg", text3, layout="side", image_position="right")

    # Chapter21
    with st.expander("Chapter 1.21 - Dasaratha finally agrees"):

        text1 = """
Jab Raja Dasharatha ne apne beta Rama ke liye chinta (<span style="color:#FF5733;">concern</span>) se bhare shabd kahe, tab Maharishi Vishvamitra kuch naraaz ho gaye.  
Unhone kaha, “Hey Raja, tum Raghu vansh me paida hue ho — jahan vachan (<span style="color:#FF5733;">promise</span>) todna shobha nahi deta! Tumne jo kaha, usse badalne ka yeh iraada (<span style="color:#FF5733;">intention</span>) tumhare kul ke layak nahi hai. Agar tum apna vachan todna chahte ho, to main yahan se chala jaata hoon. Tum apne mitron aur parivar ke saath sukh se raho, hey ‘vachan-bhang karne wale Raja’!”  

Vishvamitra ke krodh (<span style="color:#FF5733;">anger</span>) se dharti kaap uthi, aur devta bhi dar gaye.  
Tab Rishi Vasishtha — jo bahut gyaani aur dhairyavaan the — beech me aaye aur Raja ko shaant karte hue bole:
        """
        create_image_text_layout("attached_assets/chapter1/1.21.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“Hey Dasharatha, tum Ikshvaku vansh ke ho — tumhara dharma (<span style="color:#FF5733;">righteousness</span>) sab log jaante hain. Tum sachai aur dhairya ke prateek (<span style="color:#FF5733;">symbol</span>) ho. Tumhe apna vachan nibhana chahiye, kyunki jo apna vaada todta hai, uska punya (<span style="color:#FF5733;">merit</span>) chala jaata hai.”  

Rishi Vasishtha ne aur samjhaya: “Tumhara beta Rama yuddh (<span style="color:#FF5733;">battle</span>) me naya hai, lekin use darne ki zarurat nahi. Jab tak Maharishi Vishvamitra uske saath hain, koi bhi rakshas (<span style="color:#FF5733;">demon</span>) uska kuch nahi bigaad sakta. Vishvamitra swayam ek mahaan yogi, tapasvi (<span style="color:#FF5733;">ascetic</span>) aur shastron ke maharathi (<span style="color:#FF5733;">master of weapons</span>) hain. Unhone apni tapasya aur gyaan se hazaron astra-shastra (<span style="color:#FF5733;">divine weapons</span>) prapt kiye hain. Unke samne koi asur, devta, ya manav tik nahi sakta.”  
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Rishi Vasishtha ne kaha, “Tumhe apna vachan nibhana chahiye, aur Rama ko Vishvamitra ke saath bhejna chahiye. Wo surakshit rahega aur bahut kuch seekhega bhi.”   Yeh sab sun kar, Raja Dasharatha ne apna dil mazboot kiya aur Rama ko Vishvamitra ke saath bhejne ke liye haan kar di.  Unhone khushi aur vishwas ke saath apna vachan nibhaya — jaise ek sachcha Raghuvanshi Raja karta hai.
        """
        create_image_text_layout("attached_assets/chapter1/1.21.2.jpg", text3, layout="side", image_position="right")

    # Chapter22
    with st.expander("Chapter 1.22 - Rama and Lakshmana go with Vishvamitra"):

        text1 = """
Subah ka samay tha. Rishi Vasishtha ke kehne par, Raja Dasharatha ne khushi ke saath apne dono bete — Rama aur Lakshmana — ko bulaya. Raja ne unke liye shanti paath (<span style="color:#FF5733;">peace chant</span>) karvaya, aur Rishi Vasishtha ne aashirvaad (<span style="color:#FF5733;">blessing</span>) diya. Uske baad Dasharatha ne pyaar se dono beto ke sir ko soongha (<span style="color:#FF5733;">traditional gesture of affection</span>) aur kaha, “Tum dono meri shaan ho, dhairya rakho aur Rishi Vishvamitra ki seva me sada nishtha (<span style="color:#FF5733;">devotion</span>) se raho.”
        """
        create_image_text_layout("attached_assets/chapter1/1.22.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Phir Rama aur Lakshmana ne pranam karke raja se vida li. Jaise hi ve mahal se nikle, pawan dev (<span style="color:#FF5733;">Vayu</span>) ne thandi, sugandhit hawa behai. Upar se devtaon ne phool barsaye, shankh (<span style="color:#FF5733;">conch</span>) bajne lage aur dhol nagade gunj uthe — jaise swarg bhi in dono yuvraaj ka swagat kar raha ho. 

Vishvamitra aage-aage chal rahe the, unke peeche Rama, aur uske baad Lakshmana, haath me dhanush (<span style="color:#FF5733;">bow</span>) aur peeth par tarqush (<span style="color:#FF5733;">quiver</span>) liye hue. Unka roop itna tejasvi (<span style="color:#FF5733;">radiant</span>) tha ki dishaayein chamak uthi — jaise do surya prakash de rahe ho. Ve dono aise lag rahe the jaise Kartikeya aur Ganesh, Bhagwan Shiva ke shaurya (<span style="color:#FF5733;">valor</span>) ke do roop ho.

Thodi door chalne ke baad, ve Sarayu nadi ke kinare pahuche. Wahan Rishi Vishvamitra ne pyar se kaha, “Hey Rama beta, ab apna sharir is pavitra paani se shuddh (<span style="color:#FF5733;">purify</span>) karo. Main tumhe do mahan vidya (<span style="color:#FF5733;">knowledge</span>) sikhana chahta hoon — Bala aur Atibala. In dono vidyaon se tumhe kabhi thakaan, bimari, ya budhapa (<span style="color:#FF5733;">old age</span>) nahi chhuega. Koi bhi rakshas (<span style="color:#FF5733;">demon</span>) tumhe nuksaan nahi pahucha sakega. Tumhara gyaan, tej (<span style="color:#FF5733;">brilliance</span>) aur samajh (<span style="color:#FF5733;">wisdom</span>) teenon lokon me sabse alag hoga.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Vishvamitra ne aur kaha, “Yeh dono vidyaen, Bala aur Atibala, sabhi vidyaon ki maa hain. Inke dwara tum apni bhukh aur pyaas par niyantran (<span style="color:#FF5733;">control</span>) kar sakoge. Yeh vidya Brahma ki betiyan hain, aur main tumhe yeh sikhane ke layak samajhta hoon.”

Rama ne nadi ka paani apne sharir par dala aur kaha, “Hey Mahaan Rishi, main aapka sevak hoon, kripya mujhe yeh vidya sikhaiye.” Tab Vishvamitra ne Rama ko dono vidya sikhai. Jaise hi Rama ne Bala aur Atibala me siddhi (<span style="color:#FF5733;">mastery</span>) paayi, uska tej surya ke saman chamak utha.

Us raat dono bhai — Rama aur Lakshmana — Rishi Vishvamitra ke charanon (<span style="color:#FF5733;">feet</span>) ki seva karke, Sarayu ke tat par ek aasan (<span style="color:#FF5733;">bed</span>) ghans (<span style="color:#FF5733;">grass</span>) ka bana kar so gaye.  
Rama dharti par sone ke aadat nahi the, par fir bhi apne guru ke shant shabdon ko sunte hue neend me chale gaye.
        """
        create_image_text_layout("attached_assets/chapter1/1.22.2.jpg", text3, layout="side", image_position="right")

    # Chapter23
    with st.expander("Chapter 1.23 - They reach the hermitage of Sage Kama"):

        text1 = """
Subah hone se thoda pehle, Rishi Vishvamitra ne apne ghaas ke aasan (<span style="color:#FF5733;">grass bed</span>) par baith kar pyaar se kaha,  “Hey Rama, Kaushalya ke putra (<span style="color:#FF5733;">son of Queen Kaushalya</span>), subah hone wali hai, uth kar apne snan aur prarthana (<span style="color:#FF5733;">morning devotions</span>) karo.”

Rama aur Lakshmana turant jaag gaye, nadi ka paani le kar achman (<span style="color:#FF5733;">purification</span>) kiya, Surya dev ko jal chadhaya (<span style="color:#FF5733;">offered water to the rising sun</span>), apne pitron (<span style="color:#FF5733;">ancestors</span>) ko shraddha se yaad kiya, aur fir Gayatri mantra ka uchcharan (<span style="color:#FF5733;">recitation</span>) karne lage. Apni pooja-pooja karke, dono bhai ne Rishi Vishvamitra ko namaskar kiya aur agle safar ke liye taiyaar ho gaye.
        """
        create_image_text_layout("attached_assets/chapter1/1.23.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Thodi der baad ve us sthal (<span style="color:#FF5733;">place</span>) par pahuche jahan Ganga aur Sarayu nadi ek saath milti thi —  
yeh drishya itna pavitra tha ki dono bhai ke chehre khushi se chamak uthe. Unhone dekha ki wahan kai sant (<span style="color:#FF5733;">holy sages</span>) apne ashram me dhyaan aur yog (<span style="color:#FF5733;">meditation</span>) me lage hue the. Unka chehra shaant aur man pavitra tha. Rama ne muskurate hue pucha, “Hey Mahaan Rishi, yeh sundar ashram kis ka hai? Kaun rehta hai yahan? Hum janna chahte hain.”

Rishi Vishvamitra muskuraaye aur bole, “Hey Rama, suno beta — bahut samay pehle Kandarpa, jise sab Kama Dev kehte hain, yahan dhyaan lagakar Bhagwan Shiva ki aradhana (<span style="color:#FF5733;">worship</span>) karte the. Ek din jab Bhagwan Shiva apni nav-vivahit patni (<span style="color:#FF5733;">newly wedded wife</span>) ke saath guzar rahe the, tab Kama Dev ne unke man me prem jagane ki koshish ki. Lekin Bhagwan Shiva to sab par niyantran (<span style="color:#FF5733;">control</span>) rakhne wale hain — unhe yeh koshish achhi nahi lagi aur unhone krodh (<span style="color:#FF5733;">anger</span>) me apni teesri aankh (<span style="color:#FF5733;">third eye</span>) khol di. Us tej (<span style="color:#FF5733;">flame</span>) se Kama Dev ka sharir bhasm (<span style="color:#FF5733;">turned to ashes</span>) ho gaya.

Tab se, usse Ananga (jiska koi sharir nahi, <span style="color:#FF5733;">bodiless</span>) kaha jaane laga. Aur jahan-jahan uske ang (<span style="color:#FF5733;">limbs</span>) gire, us desh ko Anga kehte hain.” Rishi Vishvamitra ne fir kaha,  “Yeh ashram Bhagwan Shiva ka pavitra sthaan hai. Yahan ke sant log unke bhakt hain — pavitra aur paap se pare. Aaj hum yahan raat guzarayenge. Subah hum is pavitra nadi ko paar karke apni yatra aage badhaenge. Ab tum dono snan (<span style="color:#FF5733;">bath</span>) karo, Gayatri ka jap (<span style="color:#FF5733;">chant</span>) karo aur havan (<span style="color:#FF5733;">fire offering</span>) karke yahan shaant raat bitao.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Jab Rama aur Vishvamitra baatcheet kar rahe the, toh ashram ke rishi log apne yog bal (<span style="color:#FF5733;">power of meditation</span>) se samajh gaye ki bade mahan atithi (<span style="color:#FF5733;">great guests</span>) aa rahe hain. Unhone turant paani aur phool se arghya (<span style="color:#FF5733;">welcome offering</span>) diya, aur dono rajkumaron ka swagat kiya.

Unhone unhe ashram me bulaya, kahaniyaan sunayi, purani parampara (<span style="color:#FF5733;">traditions</span>) aur dharmik gyaan (<span style="color:#FF5733;">spiritual wisdom</span>) bataya. Sabne mil kar shaam ki pooja ki aur Rama, Lakshmana aur Vishvamitra ne us pavitra Kama ke ashram me raat sukoon se bitai.
        """
        create_image_text_layout("attached_assets/chapter1/1.23.2.jpg", text3, layout="side", image_position="right")

    # Chapter24
    with st.expander("Chapter 1.24 - The scary dark forest of Taraka"):

        text1 = """
Subah ke samay, jab suraj ugta hai, do rajkumar — Rama aur Lakshmana, apni daily pooja (<span style="color:#FF5733;">worship</span>) kar ke Rishi Vishvamitra ke saath nikalte hain. Ashram ke sab tapasvi (<span style="color:#FF5733;">saints</span>) unke saath nadi tak jaate hain aur unke liye ek sundar nauka (<span style="color:#FF5733;">boat</span>) laate hain.

Sab kehte hain — “Hey Mahaan Rishi, der mat kijiye, iss nauka me baith jaiye taaki dhoop (<span style="color:#FF5733;">sunlight</span>) tez hone se pehle hum paar ho jayein.” Vishvamitra ji sabko pranam karte hain aur dono rajkumar ke saath nadi paar karne lagte hain. Jab nauka beech nadi me hoti hai, to Rama aur Lakshmana ek zor ka shor (roar of water) sunte hain. Rama puchte hain, “Hey Gurudev, ye paani itna zor se kyun goonj raha hai?”

        """
        create_image_text_layout("attached_assets/chapter1/1.24.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Vishvamitra muskura kar samjhate hain — “Rama, ye awaaz tab hoti hai jab Sarayu nadi aur Ganga nadi ek dusre se milti hain. Sarayu ka janm Manasarovar (Lake of the Mind) se hua tha, jo Kailash Parvat par hai — wahi jahan Brahma ji ne apne man (mind) se ek pavitra sarovar banaya tha. Jab ye dono pavitra nadiyan milti hain, to yahi dhwani (sound) hoti hai. Ab dono ko pranam karo.” Dono bhai haath jod kar nadiyon ko namaskar karte hain, aur jab kinare pahuchte hain, tab apni yatra aage badhate hain.

Thodi der chalne ke baad unhe ek andhera aur bhayanak van (dark and scary forest) dikhta hai. Rama kehte hain —
“Gurudev, ye van to bahut daravana (<span style="color:#FF5733;">terrifying</span>) lag raha hai! Idhar har jagah ajeeb awaazein aa rahi hain — jangli janwar (wild animals) dahad rahe hain, pakshi (birds) cheekh rahe hain. Dekhiye! Idhar suar (boars), sher (lions), bagh (tigers), aur haathi (elephants) sab hain. Van me Dhara, Patala, Tinduka jaise ped (trees) hain — ye sach me bhayankar jagah lagti hai.”

Vishvamitra dhairya se kehte hain — “Putra Rama, is van ki kahani suno. Pehle yahan do shahar the — Malava aur Karusha. Dono swarg jaise samruddh (<span style="color:#FF5733;">prosperous</span>) aur khushhaal the. Jab Indra devta ne dusht Vritrasura ko maara, to unhe ek paap (sin) laga kyunki unhone ek brahmin ka vadh kiya tha. Devta aur rishi ne Indra ko Ganga ke pavitra jal se snan karaya, taaki unka paap dhul jaye.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Phir Indra ne in dono shahron ko vardaan diya —
‘Yeh shahar sadaa samruddh aur prasiddh (<span style="color:#FF5733;">famous</span>) rahenge.’” Lekin samay ke saath, yahan ek dusht yakshini (female demon) paida hui — jiska naam tha Taraka. Uske paas 1000 haathiyon jitni shakti (<span style="color:#FF5733;">strength</span>) thi! Uska pati tha Sunda, aur beta Maricha, jo Indra jitna balwaan (<span style="color:#FF5733;">powerful</span>) tha.

Vishvamitra ne kaha —
“Rama, ye Taraka bahut hi bhayanak aur krur (<span style="color:#FF5733;">cruel</span>) hai. Ye raste band karti hai aur logon ko darta rakhti hai. Ab hum uske van me ja rahe hain. Mera aadesh hai — tum us dusht Taraka ka vadh (<span style="color:#FF5733;">defeat</span>) karo aur is desh ko mukt (<span style="color:#FF5733;">free</span>) karao. Uske dar se yahan koi nahi aata — lekin tum, Rama, is van me phir se jeevan laa sakte ho.”
        """
        create_image_text_layout("attached_assets/chapter1/1.24.2.jpg", text3, layout="side", image_position="right")

    # Chapter25
    with st.expander("Chapter 1.25 - Vishvamitra convinces Rama to fight evil"):

        text1 = """
Rama ne ghabrakar pucha,
“Guruji, yakshini (<span style="color:#FF5733;">female spirit/demon</span>) to kamzor hoti hain — phir Taraka ko itni shakti (<span style="color:#FF5733;">strength</span>) kaise mili? Uske haath kitne majboot hain — hazaar haathi jaisi!”

Vishvamitra ne pyar se muskuraake kaha,
“Beta, sab kuch kaaran ke saath hota hai. Suno iska poora kissa.
Ek samay ek yaksha (<span style="color:#FF5733;">nature-spirit</span>) tha jiska naam Suketu tha. Wo bahut punya (<span style="color:#FF5733;">virtuous</span>) tha par uske koi santaan (<span style="color:#FF5733;">child</span>) nahi the. Usne itni tapasya (<span style="color:#FF5733;">penance</span>) ki ki Brahma usse prasann (<span style="color:#FF5733;">pleased</span>) huye. Brahma ne usse ek beti dene ka vachan diya — uska naam Taraka rakha gaya. Brahma ne usme hazaar haathi jaisi shakti (<span style="color:#FF5733;">strength of a thousand elephants</span>) bhi de di.”
        """
        create_image_text_layout("attached_assets/chapter1/1.25.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“Taraka jab badi hui to uska vivaah Sunda se hua, aur unka beta hua — uska naam Marica. Marica bahut balwaan (<span style="color:#FF5733;">powerful</span>) ho gaya. Lekin kismet me kuch aur likha tha — jab Rishi Agastya ne Sunda par shraap (<span style="color:#FF5733;">curse</span>) diya, to Marica ko bhi shraap laga aur wo ek rakshasa (<span style="color:#FF5733;">demon</span>) ban gaya. Taraka par bhi shraap pada — uska saundarya (<span style="color:#FF5733;">beauty</span>) chala gaya, aur wo ek bhayankar rakshasi (<span style="color:#FF5733;">female demon</span>) ban gayi jo manushyon ko kha jaati (<span style="color:#FF5733;">devours</span>) thi.”

Vishvamitra ne aage bataya,
“Rama, jab Agastya ne use sanshodhit (<span style="color:#FF5733;">cursed</span>) kiya, Tab se Taraka ne is zameen ko barbaad kar diya — gaon loot liye, raste rok diye, aur logon ko dara diya. Uska beta Marica bhi bahut khatarnak hai — vah Indra jaisa majboot hua. Isiliye ye jungle aur desh ajib aur andhera ho gaya.” 

Phir Vishvamitra ne bade bhav se kaha,
“Beta, yeh tumhara kartavya (<span style="color:#FF5733;">duty</span>) hai — ek yodha (<span style="color:#FF5733;">warrior</span>) aur rajkumar ko apni praja (<span style="color:#FF5733;">people</span>) ki raksha (<span style="color:#FF5733;">protection</span>) karni chahiye. Jo rajyadharma (<span style="color:#FF5733;">kingly duty</span>) hai, usme kabhi-kabhi kathor (<span style="color:#FF5733;">tough</span>) kaam karne padte hain — jinse logo ko bachaya ja sake. Purane raje aur devta bhi kabhi kathor nirnay le chuke hain jab duniya ka hit (<span style="color:#FF5733;">welfare</span>) zaruri tha.”

Vishvamitra ne misal di,
“Dekho, Indra ne Manthara jaisi auraton ko saza di jab unhone anyaay kiya; Vishnu ne bhi kuch kathor nirnay liye jab usse duniya bachani thi. Isliye ab tumhe dar kar peeche nahi hatna. Taraka bilkul dusht (<span style="color:#FF5733;">evil</span>) hai — use turant samapt (<span style="color:#FF5733;">destroy</span>) karna hoga.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Rama ne gahra saans li aur vinamr (<span style="color:#FF5733;">humble</span>) ho kar bola,
“Guruji, aapne jo bataya, main samajh gaya. Jo bhi karna hai, main karunga — desh aur rishiyon (<span style="color:#FF5733;">sages</span>) ki raksha ke liye.”

Vishvamitra ne khush hokar uska ashirwad (<span style="color:#FF5733;">blessing</span>) diya aur kaha,
“Ab chalo — us andhere van (<span style="color:#FF5733;">dark forest</span>) ki ore. Tumhe mahan kaushalon (<span style="color:#FF5733;">skills</span>) aur aashirwad milenge. Ab tum apna himmat (<span style="color:#FF5733;">courage</span>) dikhao.” 
        """
        create_image_text_layout("attached_assets/chapter1/1.25.2.jpg", text3, layout="side", image_position="right")

    # Chapter26
    with st.expander("Chapter 1.26 - How Rama defeats the demon Taraka"):

        text1 = """
Rama dhyaan se Vishvamitra ke shabd sun rahe the. Unke mann me himmat aur utsaah (<span style="color:#FF5733;">courage and excitement</span>) bhar gaya. Namrata se haath jod kar unhone kaha —
“Guruji, pitaji Dasharatha ne mujhe aapki seva (<span style="color:#FF5733;">service</span>) ke liye bheja hai. Aap jo kahenge, main bina sankoch (<span style="color:#FF5733;">hesitation</span>) ke karunga. Isse rishiyon (<span style="color:#FF5733;">sages</span>), raja aur janata (<span style="color:#FF5733;">people</span>) — sabka bhala (<span style="color:#FF5733;">good</span>) hoga.”

Yeh kehkar Rama ne apna dhanush (<span style="color:#FF5733;">bow</span>) uthaya aur taar (<span style="color:#FF5733;">string</span>) khinch kar chhoda — TWANG! Poora jungle us awaz se goonj utha. Pedon ke peeche chipi prani (<span style="color:#FF5733;">creatures</span>) ghabra gaye. Taraka ne bhi woh dahad (<span style="color:#FF5733;">sound</span>) suni — aur uska gussa aasman chhoo gaya! 

Gusse se bhar kar, Taraka dhaad kar Rama ki or bhagi. Jab Rama ne use dekha — to wo ek bhayankar (<span style="color:#FF5733;">terrifying</span>) rakshasi thi — vishaal (<span style="color:#FF5733;">huge</span>) sharir, bhaddaa (<span style="color:#FF5733;">ugly</span>) chehra aur aankhon me agni jaisi chamak!
Rama ne Lakshmana se kaha, “Bhai, dekho! Ye hai Taraka! Iska roop hi logon ke dil me bhay (<span style="color:#FF5733;">fear</span>) bhar deta hai. Par main ise nahi maarunga — kyunki stri (<span style="color:#FF5733;">woman</span>) ko maarna uchit nahi. Main bas ise rok dunga — taaki ye aur nuksaan na kare.”
        """
        create_image_text_layout("attached_assets/chapter1/1.26.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Lekin Taraka ne joru se cheekh kar mitti (<span style="color:#FF5733;">dust</span>) ka badal utha diya! Poora van andhera ho gaya. Fir usne apne jadui bal (<span style="color:#FF5733;">magic powers</span>) se pathar (<span style="color:#FF5733;">rocks</span>) barsa diye! Rama ne apni teer-dhanu (<span style="color:#FF5733;">bow and arrows</span>) se un sab ko roka aur aage badhkar uske dono haath kaat diye. Lakshmana ne bhi turant uske kaan aur naak kaat diye — ab Taraka cheekhne lagi, roop badalne lagi, kabhi gayab hoti, kabhi door se pathar barsati.

Vishvamitra ne zor se pukara,
“Rama! Ab aur daya (<span style="color:#FF5733;">mercy</span>) mat dikhao! Agar ye bachi, to fir se yagna (<span style="color:#FF5733;">holy rituals</span>) bigaad degi. Surya (<span style="color:#FF5733;">sun</span>) dhal raha hai — abhi maaro ise!” Rama ne turant Vishvamitra ke sanket (signal) par dhyaan diya. Unhone apne turant lakshya paane wale teer (arrows that follow sound) nikale, aur Taraka ke chaaro taraf chhode. Ek teer uske hriday (<span style="color:#FF5733;">heart</span>) me ghus gaya — aur wo zameen par girkar pran tyag kar gayi (<span style="color:#FF5733;">gave up her life</span>).

        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Asmaan se devta (<span style="color:#FF5733;">gods</span>) khush hokar bole —
“Shabash, Shabash Shri Rama!” Indra ne bhi prarthana ki — “Hey Vishvamitra, ise apne divya astra (<span style="color:#FF5733;">divine weapons</span>) sikhao — ye dono bhai mahan kaam karenge!” 

Devta pranam karke apne lok (<span style="color:#FF5733;">heavens</span>) laut gaye.
Vishvamitra ne Rama ke sir par haath rakha aur kaha,
“Beta Rama, aaj raat yahin araam karo. Kal hum mere ashram (<span style="color:#FF5733;">hermitage</span>) chalenge.” 

Rama muskuraaye aur shaant man se so gaye. Jungle, jo pehle andhera aur bhayanak tha, ab phir se khushhaal (<span style="color:#FF5733;">beautiful</span>) ho gaya — champa, ashok, aur aam ke pedon se saja hua. Aur us raat, Rama ka naam — “Taraka-vijayi” (<span style="color:#FF5733;">slayer of Taraka</span>) — asmaan tak gunj utha. 
        """
        create_image_text_layout("attached_assets/chapter1/1.26.2.jpg", text3, layout="side", image_position="right")

    # Chapter27
    with st.expander("Chapter 1.27 - Rama gets special divine weapons"):

        text1 = """
Subah ka suraj uga tha. Jungle me pichli raat jaise shaanti thi, waisa sukoon kahin aur nahi. Sage Vishvamitra muskuraaye aur pyar bhare swar me bole — “Hey Rama, Raghu vansh ke veer putra! Main tumse bahut prasann (<span style="color:#FF5733;">happy</span>) hoon. Tumne apna kartavya (<span style="color:#FF5733;">duty</span>) bahut imaandari se nibhaya hai. Aaj main tumhe kuch aise divya astra (<span style="color:#FF5733;">celestial weapons</span>) dene ja raha hoon, jinse tum devtaon (<span style="color:#FF5733;">gods</span>), asuron (<span style="color:#FF5733;">demons</span>) aur nagon (<span style="color:#FF5733;">serpents</span>) sab par vijay (<span style="color:#FF5733;">victory</span>) pa sakte ho.” Rama ne vinamr (<span style="color:#FF5733;">humble</span>) bhaav se haath jode. Tab Vishvamitra ne kaha —
        """
        create_image_text_layout("attached_assets/chapter1/1.27.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“Yeh lo Rama — Sudarsana Chakra aur Danda Astra, Vishnu Chakra, Indra Astra, aur Kala Astra (<span style="color:#FF5733;">weapon of time</span>), Mahendra ka Gada (<span style="color:#FF5733;">mace</span>) aur Brahma-Shira Astra, Shankara Astra, aur dono maha-gade — Kaumodaki aur Lohitamukhi, Dharmapasha, Kalapasha, Varunapasha (yeh teeno jaadu jaisi rassi hain jo dushman ko baandh deti hain), Agneya Astra (<span style="color:#FF5733;">fire weapon</span>) aur Vayuvya Astra (<span style="color:#FF5733;">wind weapon</span>), Hayashira Astra (<span style="color:#FF5733;">horse-headed weapon</span>), Krauncha Astra (<span style="color:#FF5733;">crane weapon</span>), aur aur bhi kai shaktiyaan.” Fir unhone Rama ko Gandharva Astra, Manava Astra, aur Madana Astra (<span style="color:#FF5733;">love weapon</span>) bhi diye — jisse manushya ka man lalach aur moh (<span style="color:#FF5733;">desire</span>) me ulajh jaata hai.

Vishvamitra ne haste hue kaha, “Hey Veer Rama! Ab tum sab astron ke raaz (<span style="color:#FF5733;">secrets</span>) jaante ho. In sab ko dhyaan se sikh lo. Tumhe ab duniya me koi hara nahi sakta.” Phir Rishi Vishvamitra ne purificatory mantr (<span style="color:#FF5733;">holy chants</span>) padhe, aur jab Rama ne apne mantr kahe, to sab astra-devata (<span style="color:#FF5733;">weapon deities</span>) Rama ke samne prakat hue.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Haath jod kar bole — “Hey Raghuvanshi Rama, hum aapke sevak hain. Jab bulaoge, tab turant prakat honge.” Rama ne vinamrta se kaha —
“Thik hai, main jab tumhe pukarunga, tum meri sahayata (<span style="color:#FF5733;">help</span>) karna.” Vishvamitra muskuraaye. Jungle me ek pavitra hawa behi. Rama ne guru ko pranam kiya aur bola — “Gurudev, ab chaliye. Agla yatra (<span style="color:#FF5733;">journey</span>) humare intezaar me hai.” Aur is tarah, Shri Rama divya shastron ke saath, Vishvamitra ke saath, apni adhyatmik aur veerta bhari yatra par aage badhe.
        """
        create_image_text_layout("attached_assets/chapter1/1.27.2.jpg", text3, layout="side", image_position="right")

    # Chapter28
    with st.expander("Chapter 1.28 - Rama learns how to use them"):

        text1 = """
Subah ke baad, jab Rama ne sab divya astra (<span style="color:#FF5733;">celestial weapons</span>) aur unke mantr (<span style="color:#FF5733;">chants</span>) le liye, to Vishvamitra haste hue aage chalne laga aur Rama se bola:
“O beta, tumne aise astra paaye hain jo devta aur asur bhi aasani se nahi paa sakte. Ab main tumhe sikhaunga ki inhen kaise chhoda (<span style="color:#FF5733;">release</span>) karte hain aur kaise wapas bulaate (<span style="color:#FF5733;">withdraw</span>) hain.” Rama vinamrata se poochha:
“Guruji, jab main koi astra chhod doon to use wapas kaise bulaoon? Aur in sabka upyog kaise karoon?”

Tab Vishvamitra ne dhairya se sikhaaya — aur bahut si vidya (<span style="color:#FF5733;">techniques</span>) aur mantr diye. Unhone kuch astraon ke naam bole — jaise Satyavana, Satyakirti, Dhrishta, Raphasa, Parangmukha, Lakshya, Jyotisha, Vimala — aur aur bhi anek shaktishaali astra (<span style="color:#FF5733;">weapons</span>) diye — kuch aise jo aag jaise chamakte the, kuch dhuan (<span style="color:#FF5733;">smoke</span>) jaise, aur kuch surya-chandrama ki tarah tej (<span style="color:#FF5733;">bright</span>) the.
        """
        create_image_text_layout("attached_assets/chapter1/1.28.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Vishvamitra ne samjhaya ki har astra ka ek niyamit mantra (<span style="color:#FF5733;">specific chant</span>) hota hai, aur jab wo mantra ucharit (<span style="color:#FF5733;">recited</span>) kiya jaata hai to astra ki devata (<span style="color:#FF5733;">weapon-deity</span>) prakat (<span style="color:#FF5733;">appear</span>) ho jaati hai. Jab devata prakat hoti, woh vinamr hokar kehti:
“O Raja-vanshi Rama, hum tumhaare sevak hain — jab bulao, hum turant madad karenge.”

Rama ne sab astra-devtaon ko namaskar (<span style="color:#FF5733;">salute</span>) kiya aur kaha, “Jab awashyakta ho, tab aao aur meri sahayata karo. Ab tum sab wapas chala jao.” Sab devta vinamrata se chale gaye aur Rama ne Vishvamitra ko pranam karke bola: “Gurudev, ab hum aage badhein.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Phir Rama ne dekha ki paas hi pahaad ke paas ek ghaana (<span style="color:#FF5733;">thick</span>) van aur ek sundar jhadi jaisi jagah dikh rahi hai — ek chhota sa grove jahan hiran (<span style="color:#FF5733;">deer</span>) ghoom rahe the aur pakshi (<span style="color:#FF5733;">birds</span>) madhur ga rahe the. Woh hairan hua aur puchha:
“Guruji, yeh kaun sa ashram (<span style="color:#FF5733;">hermitage</span>) hai? Kya hum ab us bhayanak forest ko paar kar chuke hain jahan rakshas (<span style="color:#FF5733;">demons</span>) aate the? Kya yeh aapka hi ashram hai jahan apne yajna (<span style="color:#FF5733;">sacrifice</span>) ki raksha ke liye aap aaye the? Bataiye, main turant taiyaar hoon—main un rakshason ka nasht (<span style="color:#FF5733;">destroy</span>) kar dunga.”

Vishvamitra muskura ke bola:
“Thoda aage badhte hain — main tumhe sab ghatnaon ka vivaran (<span style="color:#FF5733;">story</span>) bataunga aur phir aage ka marg (<span style="color:#FF5733;">path</span>) chunenge.” Aur is tarah, Rama ne shastron ki vidya aur unke mantra seekh liye, aur dono aage badh kar us shant aur hare-bhare sthaan par aaram (<span style="color:#FF5733;">rest</span>) karne lage — kyunki ab unke paas gyan (<span style="color:#FF5733;">knowledge</span>) aur shakti (<span style="color:#FF5733;">power</span>) dono the, jo unhe aane wale kathin kaamon ke liye taiyaar karte the.
        """
        create_image_text_layout("attached_assets/chapter1/1.28.2.jpg", text3, layout="side", image_position="right")

    # Chapter29
    with st.expander("Chapter 1.29 - Vishvamitra tells the story of his hermitage"):

        text1 = """
Jab Shri Rama ne apne guru Vishvamitra se poocha, “Guruji, yeh kaunsa van (<span style="color:#FF5733;">forest</span>) hai? Yahaan kitni shanti aur pavitrata (<span style="color:#FF5733;">purity</span>) hai!” Tab Vishvamitra muskuraaye aur kaha:  

“Rama, yeh wahi pavitra (<span style="color:#FF5733;">holy</span>) sthal hai jahan Bhagwan Vishnu ne kabhi apni kathin tapasya (<span style="color:#FF5733;">penance</span>) ki thi.  Isse Siddha-Ashram kaha jaata hai — kyunki yahan bade-bade rishi aur devta apni tapasya mein safal (<span style="color:#FF5733;">successful</span>) hue the.” Phir Vishvamitra ne ek sundar kahani sunaai:  
        """
        create_image_text_layout("attached_assets/chapter1/1.29.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“Bahut saal pehle, Raja Bali, jo Virochana ka beta tha, itna shaktishaali (<span style="color:#FF5733;">powerful</span>) ho gaya tha ki usne Indra aur anya devtaon ko hara diya tha, aur teenon lokon (<span style="color:#FF5733;">three worlds</span>) par raaj karne laga. Tab sab devta bhay (<span style="color:#FF5733;">fear</span>) se bhar gaye aur Agni ke saath milkar Vishnu Bhagwan ke paas aaye. Unhone kaha, ‘Prabhu, Raja Bali ek maha-yajna (<span style="color:#FF5733;">great sacrifice</span>) kar raha hai. Jab tak wo poora na ho, tab tak humein bachaiye (<span style="color:#FF5733;">protect</span>). Aap apne Yog-shakti (<span style="color:#FF5733;">divine power</span>) se ek Vamana roop (<span style="color:#FF5733;">dwarf form</span>) lijiye aur usse rokiye.’” Us samay Rishi Kashyapa aur unki patni Aditi bhi hazaar varshon (<span style="color:#FF5733;">thousand years</span>) se tapasya kar rahe the.  
Unhone Vishnu ko prarthana (<span style="color:#FF5733;">pray</span>) ki:   “Prabhu, aap hi sabke karta aur data ho (<span style="color:#FF5733;">the giver of all</span>). Aap humare putra (<span style="color:#FF5733;">son</span>) bankar janm lijiye aur devtaon ki raksha kijiye.”

Bhagwan Vishnu prasann (<span style="color:#FF5733;">pleased</span>) hue aur bole:  “Kashyapa, tumhe var milta hai — main tumhara putra bankar janm loonga.” Aur fir Bhagwan Vishnu ne Aditi ke garbh se janm liya —  Vamana avatar (<span style="color:#FF5733;">dwarf form</span>) ke roop mein.  Wo Raja Bali ke paas gaye aur vinamrata se bola: “Mujhe bas utni zameen (<span style="color:#FF5733;">land</span>) de do jitni main apne teen kadam (<span style="color:#FF5733;">three steps</span>) mein naap sakoon.”

Bali ne haan kar di —  aur tab Vamana Bhagwan ne apne teen kadamon mein poora brahmand (<span style="color:#FF5733;">whole universe</span>) naap liya! Vishvamitra ne kaha: “Rama, wahi Vamana Bhagwan ka ashram ab mera tapasya sthal (<span style="color:#FF5733;">hermitage</span>) hai. Lekin yahaan kuch rakshas (<span style="color:#FF5733;">demons</span>) aake yajna (<span style="color:#FF5733;">sacrifice</span>) ko bigaadte hain. Ab tum yahaan rukkar unka ant (<span style="color:#FF5733;">end</span>) karoge. Aaj hum milkar is Siddha-Ashram mein pravesh karte hain.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Phir Rama aur Lakshmana apne guru ke saath ashram mein pravesh kiye. Ashram chandrama ki roshni jaise chamak raha tha (<span style="color:#FF5733;">shining like the moon</span>). Wahan ke sab rishi Vishvamitra ko dekh kar khush hue, pranam kiya, aur dono rajkumaron ka swagat (<span style="color:#FF5733;">welcome</span>) kiya. Thoda aaram karne ke baad, Rama aur Lakshmana ne kaha:  “Gurudev, ab aapka yajna aarambh (<span style="color:#FF5733;">begin</span>) kijiye. Hum dono poori raat jagkar (<span style="color:#FF5733;">stay awake</span>) iski raksha karenge.” Aur phir Vishvamitra ne man mein dhyaan lagakar yajna prarambh kiya — Rama aur Lakshmana ne shastron ke paas baithkar apne guru ke dharm karya ki raksha ka sankalp (<span style="color:#FF5733;">vow</span>) liya. 
        """
        create_image_text_layout("attached_assets/chapter1/1.29.2.jpg", text3, layout="side", image_position="right")

    # Chapter30
    with st.expander("Chapter 1.30 - Rama defeats Maricha and Suvahu who disturb the yajna"):

        text1 = """
Rama aur Lakshman, dono Rajkumar, samay aur jagah ke hisaab se sab jaante the. Unhone Rishi Vishvamitra se poocha — “Guruji, ye do raakshas (<span style="color:#FF5733;">demons</span>) kab aate hain? Humein pehle se taiyaar rehna hoga.” Ashram ke log khush hue aur bole —
“Rajkumaro, agle 6 din tak yagya (<span style="color:#FF5733;">sacrifice</span>) chalta rahega. Rishi Vishvamitra is dauraan maun (<span style="color:#FF5733;">silent</span>) rahenge. Tum dono ko poori raksha (<span style="color:#FF5733;">protection</span>) karni hogi.”

Tab Rama aur Lakshman ne apne dhanush (<span style="color:#FF5733;">bow</span>) aur baan (<span style="color:#FF5733;">arrows</span>) le liye aur bina soye 6 din tak yagya ki rakhwali ki. Pehle 5 din shanti se bita gaye, par 6th din, Rama ne kaha — “Lakshman, aaj kuch hone wala hai. Taiyaar ho jao.”
        """
        create_image_text_layout("attached_assets/chapter1/1.30.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Jaise hi Rama ne ye kaha, yagya ki agni (<span style="color:#FF5733;">fire</span>) achanak zor se bhadak uthi. Brahmin aur Vishvamitra ne dekha ki yagya ke saare saman (<span style="color:#FF5733;">items</span>) jalne lage. Tab achanak aasman se ek bhayanak (<span style="color:#FF5733;">terrifying</span>) shabd hua — jaise bijli ki garaj (<span style="color:#FF5733;">thunder</span>)! Maricha aur Suvahu apne saathi raakshason (<span style="color:#FF5733;">demons</span>) ke saath hawa mein dikhai diye, aur unhone yagya pe laal khoon (<span style="color:#FF5733;">blood</span>) barsana shuru kar diya! Rama aur Lakshman ka gussa badh gaya.  
Rama bola —  “Lakshman, dekho in rakshason ko! Aaj main inhe Manava Astra (<span style="color:#FF5733;">divine weapon</span>) se mita dunga, jaise hawa badalon ko uda deti hai.”

Rama ne chamakta hua Manava Astra chalaya — woh seedha Maricha ke seene (<span style="color:#FF5733;">chest</span>) mein laga!  
Maricha hawa mein ude aur samundar mein jaake gire — poore 100 miles door! Rama bola —  “Dekho Lakshman! Ye Astra ki shakti (<span style="color:#FF5733;">power</span>) hai. Maricha behosh ho gaya, par abhi zinda hai. Ab main Suvahu aur baaki raakshason ka anth karunga!” Phir Rama ne Agni Astra (<span style="color:#FF5733;">fire weapon</span>) chalaya — woh Suvahu ke seene (<span style="color:#FF5733;">chest</span>) mein laga, aur Suvahu wahin girkar mar gaya. Baaki raakshason ko Rama ne Vayu Astra (<span style="color:#FF5733;">wind weapon</span>) se uda diya.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Sab raakshas mar gaye, aur yagya shanti se poora hua. Rishiyon ne khushi se kaha —  “Rama, tumne hamare yagya ko bacha liya! Tum sach mein Indra jaise vijayi (<span style="color:#FF5733;">victorious</span>) ho.” Vishvamitra muskuraaye aur bole — “Rama, aaj mera uddeshya (<span style="color:#FF5733;">purpose</span>) poora hua. Tumne apne Guru ka aadesh (<span style="color:#FF5733;">command</span>) poori shraddha se maana. Ab ye Siddha Ashram apne naam ke layak (<span style="color:#FF5733;">worthy</span>) ban gaya hai.”
        """
        create_image_text_layout("attached_assets/chapter1/1.30.2.jpg", text3, layout="side", image_position="right")

    # Chapter31
    with st.expander("Chapter 1.31 - Vishvamitra starts his journey"):

        text1 = """
Rama aur Lakshman ne Rishi Vishvamitra ka yagya safalta se poora karwa diya tha. Us raat dono Rishi ke ashram (<span style="color:#FF5733;">hermitage</span>) mein shaanti se soye. Subah, suraj ugte hi, dono ne snan (<span style="color:#FF5733;">bath</span>) kiya aur Rishi Vishvamitra ke paas gaye. Namaskar karke bole — “Guruji, hum dono aapke sevak (<span style="color:#FF5733;">servants</span>) hain. Ab hume kya karna hai? Aapka agla aadesh (<span style="color:#FF5733;">command</span>) kya hai?” Vishvamitra aur anya rishiyon ne muskurakar kaha —
        """
        create_image_text_layout("attached_assets/chapter1/1.31.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“Rama aur Lakshman, Raja Janaka, Mithila ke raja, ek maha yagya (<span style="color:#FF5733;">great sacrifice</span>) kar rahe hain. Hum sab wahan ja rahe hain. Tum dono bhi humare saath chalo.Wahan tumhe ek adbhut dhanush (<span style="color:#FF5733;">amazing bow</span>) dikhega — ye dhanush Devtaon (<span style="color:#FF5733;">gods</span>) ne Raja Janaka ko diya tha. Ye itna bhari (<span style="color:#FF5733;">heavy</span>) hai ki na Asur (<span style="color:#FF5733;">demons</span>), na Gandharv (<span style="color:#FF5733;">celestial beings</span>), koi ise tod ya jod (<span style="color:#FF5733;">bend or string</span>) nahi paaya! Bahut se mahan raja aaye, par sab asafal rahe.” Vishvamitra ne bataya —
“Raja Janaka ne ek purane yagya ke dauran ye dhanush Devtaon se paaya tha. Unhone kaha tha — ‘Is dhanush ko mandir (<span style="color:#FF5733;">temple</span>) mein rakho, aur dhup, deep aur phoolon se puja (<span style="color:#FF5733;">worship</span>) karo.’”

Phir Vishvamitra bole —
“Ab mera yagya safal (<span style="color:#FF5733;">successful</span>) ho gaya hai. Main Siddha Ashram chhod kar Ganga ke kinare, Himalaya ke paas, Mithila ki or ja raha hoon.” Ye kehkar Rishi Vishvamitra ne ashram ka parikrama (<span style="color:#FF5733;">circumambulation</span>) kiya aur apni yatra (<span style="color:#FF5733;">journey</span>) shuru ki. Saare rishi unke saath chal diye — unke saaman (<span style="color:#FF5733;">belongings</span>) ratho (<span style="color:#FF5733;">wagons</span>) mein rakhe gaye. Ashram ke pakshi (<span style="color:#FF5733;">birds</span>) aur jaanwar bhi unke peeche chal pade, jab tak Rishi ne pyar se unhe wapas nahi bhej diya.

        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Suraj dhalte samay sab log Shona nadi ke kinare pahunche. Wahan sabne snan karke sandhya prarthana (<span style="color:#FF5733;">evening prayers</span>) aur agni puja (<span style="color:#FF5733;">fire ritual</span>) ki.

Uske baad Rama aur Lakshman ne Rishi Vishvamitra ko pranam kiya aur unke paas baith gaye. Rama ne muskurakar poocha —
“Guruji, ye jagah bahut sundar hai, hare-bhare ped aur van (<span style="color:#FF5733;">forest</span>) se bhari hui! Kripya batayein, ye kaunsi bhoomi (<span style="color:#FF5733;">land</span>) hai?” Vishvamitra prasann (<span style="color:#FF5733;">pleased</span>) hue aur bole — “Rama, suno, main tumhe is desh (<span style="color:#FF5733;">country</span>) ki puri kahani batata hoon…”
        """
        create_image_text_layout("attached_assets/chapter1/1.31.2.jpg", text3, layout="side", image_position="right")

    # Chapter32
    with st.expander("Chapter 1.32 - Vishvamitra talks about his ancestors and King Kusha"):

        text1 = """
Vishvamitra ne Shri Rama se kaha — “Rama, purane samay mein ek raja tha jiska naam Kusha tha. Vah ek brahmin ka putra tha, tapasvi (<span style="color:#FF5733;">ascetic</span>), dharm-nishth (<span style="color:#FF5733;">righteous</span>), aur sada satvik (<span style="color:#FF5733;">virtuous</span>) logon mein prasiddh. Vah ek sundar aur uchch kul ki mahila Bhidharvi se vivaah kiya aur unke chaar putra hue, sab apne pita jaise shaktishaali aur guni (<span style="color:#FF5733;">virtuous</span>) the. Unke naam the: Kushamba, Kushanabha, Umuritarajasa aur Basu. Ye chaar rajkumar shaktishaali aur kriyashil (<span style="color:#FF5733;">active</span>) the. Raja Kusha ne unhe kshatriya dharma sikhate hue kaha:

‘Mere putron, apne praja (<span style="color:#FF5733;">subjects</span>) ki raksha aur palan karo; isme maha punya (<span style="color:#FF5733;">great merit</span>) hai.’ In adeshon ko poora karne ke liye, chaaron putron ne apne-apne sheher banaye aur unka naam rakha. Kushamba ne apne sheher ka naam Kaushambi rakha.
        """
        create_image_text_layout("attached_assets/chapter1/1.32.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Kushanabha ne sheher ka naam Mahodaya rakha. Umuritarajasa ne sheher ka naam Dharmaranya rakha. Basu ne sheher ka naam Giribrat ya Basumati rakha, jo paanch parvaton (<span style="color:#FF5733;">mountains</span>) se ghera hua tha, aur beech se Magadhi nadi (<span style="color:#FF5733;">Shona</span>) bah rahi thi, jaise sundar haar (<span style="color:#FF5733;">garland</span>). Rama, Kushanabha ne ek apsara (<span style="color:#FF5733;">nymph</span>) Ghritaci se vivaah kiya aur unke ek sau sundar putriyan (<span style="color:#FF5733;">daughters</span>) hui. Jab ve bade hue, to bahut sundar dikhti thi. Ek din, ve sundar vastron mein saja-kar bagiche mein ghoom rahi thi, ga rahi, naach rahi aur vadya bajaa rahi thi — jaise deviyon ka roop dharti par utar aaya ho, ya jaise taare akash mein chamak rahe ho.

In sundar rajkumariyon ko dekhkar, Vayu devta (<span style="color:#FF5733;">wind god</span>) ne kaha: ‘Main tumhe apni patni banaana chahta hoon; apni mrityu-may roop chhod do, main tumhe amar bana dunga. Yuvaavastha (<span style="color:#FF5733;">youth</span>) jaldi guzar jaati hai; mere saath vivaah karke tum sada sundar rahogi.’ Par rajkumariyon ne uska vaaky (<span style="color:#FF5733;">speech</span>) sunkar hans kar kaha:

‘O Vayu, tum manushyon ke dil ki baat jaante ho, par hum jaanti hain tumhare dil ki baat. Tum hume apmaan (<span style="color:#FF5733;">insult</span>) kyon karte ho? Hum apne tapasya aur niyantran (<span style="color:#FF5733;">self-control</span>) ke bal se tumhe hara sakti hain, par dharm aur maryada ke anusar, hum apne pitaji ki ichha se hi pati chunenge. Ve hi hamare liye dev jaise hain.’

        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Vayu devta krodhit (<span style="color:#FF5733;">angry</span>) hua aur unke sharir mein pravesh karke unka roop badal diya. Dukhit rajkumariyan apne pitaji ke paas aayi aur unhe sab bataya. Raja dukhit hoke bola: ‘Betao, kya hua? Kisne tumhe aisa avaid (<span style="color:#FF5733;">unjust</span>) prabhav diya? Sab sach batao.’ Raja ka dil dukh aur chinta se bhara ho gaya.”
        """
        create_image_text_layout("attached_assets/chapter1/1.32.2.jpg", text3, layout="side", image_position="right")

    # Chapter33
    with st.expander("Chapter 1.33 - King Kushanabha’s 100 daughters"):

        text1 = """
Jab Raja Kushanabha ne apni sau rajkumariyon se poocha ki kya hua, to ve apne sir unke charanon par rakh kar boli: “Pitaji, Vayu Devta, jo har jagah hai, ne bura raasta apnaya aur humein dharm ka palan chhodne ke liye majboor kiya. Humne use kaha ki hum apne jeevan ka marg khud nahi chun sakte kyunki aap abhi jeevit hain, aur agar use humse vivaah karna ho to aap se poochna chahiye. Par ye paap kaari devta hamari baat ko nafrat karte hue humara sharir tod-dal diya.”

Raja ne apni betiyon ki baat suni aur kaha: “Tumne sahansheelta (<span style="color:#FF5733;">forbearance</span>) dikhakar uchit vyavhaar kiya. Jo log vinamr (<span style="color:#FF5733;">humble</span>) aur dharm-nishth (<span style="color:#FF5733;">righteous</span>) hote hain, ve mahan hote hain. Sahansheelta purush aur stri dono ka shobha hai. Tumne kuchh aisa kiya jo sab nahi kar sakte. Betiyon, sahansheelta hi daan (<span style="color:#FF5733;">gift</span>) hai, sahansheelta hi satya (<span style="color:#FF5733;">truth</span>) hai, sahansheelta hi yajna (<span style="color:#FF5733;">sacrifice</span>) hai. Insaan ki asli shobha sahansheelta mein hai; yahi dharma hai. Sansaar sahansheelta par sthapit hai.”
        """
        create_image_text_layout("attached_assets/chapter1/1.33.1.jpg", text1, layout="side", image_position="left")


        text2 = """

Raja ki baat sun kar rajkumariyon ka dukh kam hua aur unhe chhoda diya. Phir Raja Kushanabha ne apne mantriyon ko bulaya aur unse poochha ki betiyon ka vivaah sahi samay aur sahi kul se kaise ho. Us samay, ek mahan muni Chuli, jo tapasvi (<span style="color:#FF5733;">ascetic</span>) aur atyant dharm-nishth (<span style="color:#FF5733;">righteous</span>) tha, apni mukti ke liye tapasya mein laga hua tha.

Wahi par nymph Urmila ki ek kumari beti Somada, muni ki seva mein lagi hui thi. Ve uske guru ki seva lagan aur shraddha (<span style="color:#FF5733;">devotion</span>) ke saath karti thi. Guru ne dekha aur khush hoke kaha: “Main tumse prasanna hoon, tumhari ichha kya hai jo main poori karu?” Somada ne madhur swar mein kaha: “O Rajaon ke Raja, main ek putra chahati hoon, jo divya shakti (<span style="color:#FF5733;">divine power</span>) se yukt ho, dharm aur bhagwan ke bhakt (<span style="color:#FF5733;">devotee</span>) ho. Mera koi pati nahi hai aur na hi main kisi ki patni banna chahti hoon, kyunki main brahmacarini (<span style="color:#FF5733;">celibate female</span>) hoon. Aap apni yog shakti (<span style="color:#FF5733;">divine energy</span>) se mujhe putra pradan kijiye.” Muni Chuli ne uski baat sunkar khushi se apna man ka bal pradarshit kiya aur usko ek putra diya, jiska naam Brahmadatta rakha. Brahmadatta Kampila ka raja bana aur Indra ke samaan samriddh (<span style="color:#FF5733;">prosperous</span>) hua.

        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Raja Kushanabha ne tay kiya ki wo apni betiyon ka vivaah Raja Brahmadatta se karenge. Kushanabha ne Brahmadatta ko apne paas bulaya aur khushi khushi apni betiyon ka vivaah diya. Raja Brahmadatta, jo Indra ke samaan mahan tha, ek-ek karke rajkumariyon ke haath le kar vivaah kiya. Jaise hi usne unke haath liye, rajkumariyon ka sharir phir se sundar aur saakarik (<span style="color:#FF5733;">restored</span>) ho gaya. Raja Kushanabha apni betiyon ko sundar aur swasth dekh kar atyant khush hua.

Is tarah, Raja Kushanabha ne apni betiyon ka vivaah Raja Brahmadatta se kar diya aur unke guruon ko unke saath saath nyaay (<span style="color:#FF5733;">justice</span>) aur maryada (<span style="color:#FF5733;">dignity</span>) ke saath unke naya ghar le jaane ka aadesh diya. Somada apne putra ke vivaah aur rajkumariyon ke saath khush hui aur Raja Kushanabha ki punya (<span style="color:#FF5733;">virtue</span>) aur dharmik pravritti (<span style="color:#FF5733;">righteous conduct</span>) ki prashansa ki.
        """
        create_image_text_layout("attached_assets/chapter1/1.33.2.jpg", text3, layout="side", image_position="right")

    # Chapter34
    with st.expander("Chapter 1.34 - Gadhi, father of Vishvamitra"):

        text1 = """
“O Ramaji, apni betiyon ke vivaah ke baad, paap-mukt (<span style="color:#FF5733;">sin-free</span>) Raja Kushanabha ne ek yajna (<span style="color:#FF5733;">sacrifice/ritual</span>) karne ka nischay kiya, jisse use ek putra prapt ho. Yajna ke samay, Maharaja Kusha, jo Shri Brahma ke putra the, Raja Kushanabha se bole: ‘Mere beta, tumhe ek putra hoga jo tum jaisa dharm-nishth (<span style="color:#FF5733;">righteous</span>) aur satyavadi (<span style="color:#FF5733;">truthful</span>) hoga, uska naam Gadhi rakha jaega, aur vah tumhe amar prasiddhi (<span style="color:#FF5733;">immortal fame</span>) dega.’

Kuch samay baad, Raja Kushanabha ko ek putra hua, jo dharm aur sadachar (<span style="color:#FF5733;">virtue</span>) ka premi tha, aur uska naam Gadhi rakha gaya. “Yahi Gadhi, O Rama, mera dharm-nishth pita tha. Aur main Kusha vansh (<span style="color:#FF5733;">lineage</span>) me janma hua, isliye mujhe Kaushika kaha gaya.
        """
        create_image_text_layout("attached_assets/chapter1/1.34.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“Meri ek badi behen thi, Satyavati, jo sachche bhartiya pati Richika ki patni bani. Jab uske pati ka dehaant (<span style="color:#FF5733;">demise</span>) hua, to vah swarg ko chali gayi aur Kaushiki nadi ka roop dharan kar liya. Ye nadi pavitra (<span style="color:#FF5733;">holy</span>) aur sundar hai, aur iska jal manushyon ko punya (<span style="color:#FF5733;">merit/blessing</span>) deta hai. Duniya ko aashirvaad dene ke liye meri behen Satyavati Himalaya ke paas Kaushiki nadi ban gayi. “O Rama, apne pati ke prem mein sthapit, sachchai aur dharm ke saath meri behen Satyavati aaj Kaushiki nadi hai, nadiyon mein mahan aur bahut shubh (<span style="color:#FF5733;">auspicious</span>) hai.

“O Rama, yajna karne ke liye, main Siddha-Ashrama aaya aur apna uddeshya (<span style="color:#FF5733;">purpose</span>) pura kiya. “O Rama, tumhare prashn par, maine apne parivaar aur vansh (<span style="color:#FF5733;">lineage/family</span>) ka varnan kiya; raat kaafi beet gayi, ab vishraam (<span style="color:#FF5733;">rest</span>) karo, taki kal taaza hokar yatra (<span style="color:#FF5733;">journey</span>) jaari rakhein. Shanti (<span style="color:#FF5733;">peace/blessing</span>) ho tum par!

“Pedon ki patiyan shant hain, pakshi aur jaanwar chup hain, aur andhera chhaya hua hai. Raat kaise beet gayi, pata bhi nahi chala. Aakash sitaron se chamak raha hai, jaise hazaron aankhen hum par nazar rakh rahi ho. “Ujjwal chaand apni thandi kirno ke saath dheere-dheere upar uth raha hai, andhera door kar raha hai. Raat ke vandhak (<span style="color:#FF5733;">obstacles</span>) aur bhayankar maans-hari yaksh (<span style="color:#FF5733;">terrifying flesh-eating spirits</span>) yahan-wahan ghoom rahe hain.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
In baaton ke baad, mahaan Rishi Vishvamitra shant ho gaye. Anya muniyon ne unki prashansa ki aur kaha: “Shabash, shabash, O Rishi! Kusha vansh ne hamesha dharm ka palan kiya aur is vansh ke raja dharm-nishth aur mahan the. Is vansh mein, aap Vishvamitra, ati-prashansaniya (<span style="color:#FF5733;">highly admirable</span>) hain, aur sundar Kaushiki nadi se is rajasv ka gaurav aur badh gaya hai.”

Is tarah mahaan muniyon ne Rishi Vishvamitra ki prashansa ki. Surya ke pashchim (<span style="color:#FF5733;">west</span>) doobne par, unhone vishraam liya. Shri Ramacandra aur unke bhai Lakshmana, jo hairan the, ne bhi Rishi ko pranam kiya aur vishraam ke liye chale gaye.
        """
        create_image_text_layout("attached_assets/chapter1/1.34.2.jpg", text3, layout="side", image_position="right")

    # Chapter35
    with st.expander("Chapter 1.35 - The holy river Ganga is born"):

        text1 = """
Raat ko Shona nadi ke kinare anya muniyon ke saath bitane ke baad, Shri Vishvamitra ne Rama se subah kaha: “Utho, O Rajkumar, din ki shuruat ho gayi hai, tum par shubh (<span style="color:#FF5733;">auspicious</span>) ho! Apni prabhat pooja (<span style="color:#FF5733;">morning prayer</span>) karo aur yatra (<span style="color:#FF5733;">journey</span>) ke liye taiyaar ho jao.”

Shri Rama ne mahaan Rishi ki baat mani, apni prabhat pooja ki aur taiyaar hue. Unhone kaha: “O Bhagwan ko jaanne wale, Shona nadi ke jal (<span style="color:#FF5733;">waters</span>) bahut shallow (<span style="color:#FF5733;">uphla</span>) aur retile bed (<span style="color:#FF5733;">sand bed</span>) par hain, kripya humein bataiye ki ise kaise paar karna chahiye.” Rishi ne uttar diya:
        """
        create_image_text_layout("attached_assets/chapter1/1.35.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“O Rajkumar, main tumhe dikhaunga ki mahaan rishiyon ne ise kaise paar kiya tha.” Phir ve nadi paar kar gaye aur sundar vanon (<span style="color:#FF5733;">forests</span>) aur jangalon ke beech yatra karte rahe. Der shaam tak, ve pavitra Ganga nadi ke kinare pahunch gaye, jo rishiyon ki priya (<span style="color:#FF5733;">beloved</span>) thi. Sundar swans aur cranes ke saath nadi aur bhi manohar (<span style="color:#FF5733;">beautiful</span>) lag rahi thi, jise dekh kar Rama, Lakshmana aur rishiyon ko anand (<span style="color:#FF5733;">joy</span>) hua.

Ve kinare ruk kar nadi me snan (<span style="color:#FF5733;">bath</span>) kiya, apni yajna ki agni (<span style="color:#FF5733;">sacrificial fire</span>) prajvalit ki aur baliyon ka bhojan kiya. Parampara (<span style="color:#FF5733;">tradition</span>) ke anusar, unhone apne purvajon (<span style="color:#FF5733;">ancestors</span>) ko jal arpan (<span style="color:#FF5733;">offering of water</span>) kiya aur vastr bicha kar Ganga ke kinare baith gaye.

Muniyon ke beech baith kar, Shri Rama ne Vishvamitra se poocha: “O Maharishi, main is pavitra nadi ka katha (<span style="color:#FF5733;">story</span>) sunna chahta hoon, jo teen lokon (<span style="color:#FF5733;">three worlds</span>) se guzar kar ant me sagar me milti hai. Kaise Shri Gunga teen lokon se guzar kar sagar me pravesh karti hai?” Is prashn par, Shri Vishvamitra ne Ganga nadi ki utpatti (<span style="color:#FF5733;">origin</span>) aur katha sunani shuru ki:

“O Rama, mahaan Himavat, Himalaya ke Maharaja aur saare ratno ke khazane ke adhikari, ke do betiyan thi, jo prithvi par apaar sundar (<span style="color:#FF5733;">extremely beautiful</span>) thi. Unki mata Mena, Himachala ki patni, Mount Meru ki putri thi. Badi beti ka naam Gunga aur chhoti beti ka naam Uma tha. “Devas, kuch pavitra kriyaayein (<span style="color:#FF5733;">holy acts</span>) karne ke ichhuk (<span style="color:#FF5733;">willing</span>) the, unhone Shri Gunga ko apne saath le liya aur uske pita ki ijazat se uska upyog kiya.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
“Himachala, samajhdaar (<span style="color:#FF5733;">wise</span>) aur sabhi jeevon ke hit ko dhyan me rakhte hue, apni beti Gunga ko devas ko de diye, jo duniya ko shuddh (<span style="color:#FF5733;">pure</span>) karne wali thi. Devas uske krutagn (<span style="color:#FF5733;">grateful</span>) hokar le gaye aur sab par aashirvaad (<span style="color:#FF5733;">blessing</span>) diya. “O Raghu vansh ke Rajkumar, Himachala ki doosri beti Uma, apne aasan (<span style="color:#FF5733;">seat/meditation spot</span>) aur tapasya me lag gayi, aur unka vivaah Shri Mahadeva se hua, kyunki Himachala ne socha ki vah ek uchit pati (<span style="color:#FF5733;">suitable husband</span>) hain.”

“O Rama, maine tumhe bataya Himachala ki do betiyon ke bare me, jo poore jagat me venerated (<span style="color:#FF5733;">respected</span>) hain: nadi Gunga aur Uma Devi. “O mere putra, O shishyon ke mukhya, maine tumhe bataya ki Shri Gunga devas ke saath swarg gayi aur vah pavitra nadi ban gayi, jiska jal sab paap (<span style="color:#FF5733;">sins</span>) ko nasht (<span style="color:#FF5733;">destroys</span>) karta hai.”
        """
        create_image_text_layout("attached_assets/chapter1/1.35.2.jpg", text3, layout="side", image_position="right")

    # Chapter36
    with st.expander("Chapter 1.36 - The story of Uma, daughter of Himalaya"):

        text1 = """
Rama aur Lakshmana ne Vishvamitra ki kahani bahut dhyan se suni aur bole, “Guruji, bahut hi pavitra (<span style="color:#FF5733;">holy</span>) kahani sunayi. Ab bataiye — Himalaya ke Raja ki chhoti beti Uma ka kya hua? Aur Ganga (Tripathaga) kaise zameen par aayi?”

Vishvamitra ne muskurake kahani shuru ki: “Sunlo, Rama. Mahadeva (Lord Shiva) ne Parvati se vivah (<span style="color:#FF5733;">marriage</span>) kiya. Dono ne sau saal tak saath bitaya, par unka koi santaan (<span style="color:#FF5733;">child</span>) nahi hua. Devta (<span style="color:#FF5733;">gods</span>) ghabra gaye aur Brahma se bole —  ‘Agar in dono ka putra paida hua, to uski shakti (<span style="color:#FF5733;">power</span>) kaun jhel payega?’  
        """
        create_image_text_layout("attached_assets/chapter1/1.36.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Phir Mahadeva ne apni urja dharti par chhod di. Wo urja pahaadon, samundaron aur vanon (<span style="color:#FF5733;">forests</span>) mein chhayi. Par jab dharti us tej (<span style="color:#FF5733;">radiance</span>) ko jhel na payi, to devtaon ne Vayu (<span style="color:#FF5733;">wind god</span>) aur Agni (<span style="color:#FF5733;">fire god</span>) se kaha ki milkar is urja ka roop badal dein. Us milan se ek ujla (<span style="color:#FF5733;">bright</span>) pahaad aur ek tejomay (<span style="color:#FF5733;">brilliant</span>) van bana —  aur us tej se Karttikeya (Skanda), devon ka yodha-putra (<span style="color:#FF5733;">warrior son of the gods</span>), janma hua.

Sab devta aur rishi khush hue aur Mahadev aur Uma ki stuti (<span style="color:#FF5733;">praise</span>) ki. Lekin Uma krodhit (<span style="color:#FF5733;">angry</span>) ho gayi — usne devtaon ko shikayat ki ki unhone use maa banne se roka. Gusse mein Uma ne haath mein paani lekar devtaon par shraap (<span style="color:#FF5733;">curse</span>) diya: “Tum sab nishchit roop se santaan-heen (<span style="color:#FF5733;">childless</span>) rahoge.”  
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Phir usne dharti ko bhi shraap diya: “Dharti! Tum hamesha badalti rahogi, kai rajaon ke adheen rahogi, aur tum bhi kabhi apna putra nahi paayegi.” Mahadev ne jab devtaon ko dukh bhara dekha, to Uma ke saath Himalaya ke upar ek shikhar (<span style="color:#FF5733;">peak</span>) — Himavatprabhava — par jakar aur bhi gehri yog aur tapasya mein lag gaye. Ab, Rama — maine Uma ki kahani bata di. Agla hissa Ganga ki utpatti (<span style="color:#FF5733;">origin</span>) ka hai, jise main aage bataunga.”
        """
        create_image_text_layout("attached_assets/chapter1/1.36.2.jpg", text3, layout="side", image_position="right")

    # Chapter37
    with st.expander("Chapter 1.37 - Ganga, the elder daughter of the king"):

        text1 = """
Jab Mahadev ji aur Mata Uma Himalaya ke shikhar (<span style="color:#FF5733;">peak</span>) par gehri tapasya (<span style="color:#FF5733;">deep meditation</span>) kar rahe the, tab devata (<span style="color:#FF5733;">gods</span>) pareshaan ho gaye. Unke leader Mahadev ji to tapasya mein the, to sab devata — Indra aur Agni ke saath — Brahma ji ke paas gaye. Sabne vinamrata se kaha, “Hey Brahma ji, Mahadev ji hamare neta (<span style="color:#FF5733;">leader</span>) hain, par ab wo tapasya mein chale gaye hain. Kripya kuch aisa kijiye jisse sansaar ka bhala (<span style="color:#FF5733;">good</span>) ho sake.”

Brahma ji ne shaant swar (<span style="color:#FF5733;">gentle voice</span>) mein kaha, “Uma Devi ka shraap (<span style="color:#FF5733;">curse</span>) badla nahi ja sakta. Par chinta mat karo — Agni dev Ganga se ek putra (<span style="color:#FF5733;">son</span>) paida karenge jo devtaon ke dushmanon (<span style="color:#FF5733;">enemies</span>) ka vinaash (<span style="color:#FF5733;">destruction</span>) karega. aur Uma Devi apni behan ke is bachche ko apna samjhenge.”
        """
        create_image_text_layout("attached_assets/chapter1/1.37.1.jpg", text1, layout="side", image_position="left")
        text2 = """

Yeh sunkar sab devata prasann (<span style="color:#FF5733;">happy</span>) ho gaye aur Agni dev se kaha — “Hey Agni, humari madad karo aur ek shaktishaali putra paida karo.” Agni dev Ganga Devi ke paas gaye aur bole, “Hey Devi, devta chahte hain ki hum milkar ek balwaan (<span style="color:#FF5733;">powerful</span>) putra janmen.” Ganga Devi ne apna roop badla aur ek sundar apsara (<span style="color:#FF5733;">celestial nymph</span>) ban gayin. Agni dev ne apna tej (<span style="color:#FF5733;">divine energy</span>) unmein sthapit kiya. Par kuch samay baad Ganga Devi ne kaha, “Hey Agni dev, main is tej ko zyada der tak nahi sambhal sakti. Mera sharir (<span style="color:#FF5733;">body</span>) jal raha hai jaise aag lag gayi ho!”

Agni dev bole, “Toh is tej ko Himalaya ke paas rakh do.” Tab Ganga Devi ne wo tej (<span style="color:#FF5733;">divine energy</span>) dharti par chhoda. Jahan wo gira, wahan se sona (<span style="color:#FF5733;">gold</span>) utpann hua —  itna chamakdaar ki aas-paas ki mitti (<span style="color:#FF5733;">soil</span>) chandi (<span style="color:#FF5733;">silver</span>) aur tamba (<span style="color:#FF5733;">copper</span>) ban gayi! Isi liye sona ko “Jatarupa” (<span style="color:#FF5733;">fire-born</span>) kaha gaya. Us tej se ek divya (<span style="color:#FF5733;">divine</span>) shishu (<span style="color:#FF5733;">child</span>) janma hua —  Kumara, jise sabne pyaar se Karttikeya kaha.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Krittika naam ki deviyan (<span style="color:#FF5733;">goddesses</span>) us bachche ki maa ban gayin. Bachcha bahut tejomayi (<span style="color:#FF5733;">radiant</span>) tha —  uske chhe mukh (<span style="color:#FF5733;">six faces</span>) the, aur wo ek saath chheon deviyon ka doodh pita tha! Jaise-jaise wo bada hua, usne asuron (<span style="color:#FF5733;">demons</span>) ko yudh (<span style="color:#FF5733;">battle</span>) ke liye chunauti di. Devataon ne use apna senapati (<span style="color:#FF5733;">commander-in-chief</span>) bana diya. Sab devata aur Agni dev ne uska aashirvaad (<span style="color:#FF5733;">blessing</span>) diya.

Vishvamitra ji ne kaha —  “Hey Rama, yeh thi Ganga aur Karttikeya ki adbhut (<span style="color:#FF5733;">wonderful</span>) kahani. Jo koi shraddha (<span style="color:#FF5733;">faith</span>) aur bhakti (<span style="color:#FF5733;">devotion</span>) se is kahani ko sunega, use lambi aayu (<span style="color:#FF5733;">long life</span>), santaan (<span style="color:#FF5733;">children</span>) aur param sukh (<span style="color:#FF5733;">great joy</span>) prapt hoga.”
        """
        create_image_text_layout("attached_assets/chapter1/1.37.2.jpg", text3, layout="side", image_position="right")
    
    # Chapter38
    with st.expander("Chapter 1.38 - The story of King Sagara, Rama’s ancestor"):

        text1 = """
Ek samay ki baat hai, Ayodhya mein ek mahaan aur dayalu raja rehta tha — Raja Sagara. Woh bahadur (<span style="color:#FF5733;">brave</span>), nyay-priya (<span style="color:#FF5733;">justice-loving</span>), aur apne praja (<span style="color:#FF5733;">people</span>) se bahut prem karne wale the. Lekin unke jeevan mein ek dukh tha — unke koi santaan (<span style="color:#FF5733;">children</span>) nahi the. Unki do patniyan thi —  Rani Keshini, Raja Vidharba ki beti, jo satya (<span style="color:#FF5733;">truthful</span>) aur dharmik thi, aur Rani Sumati, Raja Arishtanemi ki beti, jo bahut sundar aur komal (<span style="color:#FF5733;">gentle</span>) thi.  

        """
        create_image_text_layout("attached_assets/chapter1/1.38.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Raja Sagara ne ek din faisla kiya ki woh Himalaya jaakar kathin tapasya (<span style="color:#FF5733;">penance</span>) karenge. Poore 100 saal tak unhone van (<span style="color:#FF5733;">forest</span>) mein rahkar dhyaan aur tapasya ki. Unki tapasya se prasann (<span style="color:#FF5733;">pleased</span>) hokar Maharishi Bhrigu unke saamne prakat hue aur bole:  “Hey rajan (<span style="color:#FF5733;">king</span>), tumhare ghar mein bahut putra (<span style="color:#FF5733;">sons</span>) honge. Tumhara naam teenon lokon (<span style="color:#FF5733;">three worlds</span>) mein mashhoor hoga. Tumhari ek rani se ek putra hoga aur doosri se 60,000 putra janm lenge!”  

Yeh sunkar dono raniyan rishi ke paas gayin aur puchha: “Hey maharishi, bataiye hum mein se kiske kitne putra honge?” Rishi muskuraaye aur bole: “Yeh tumhari iccha (<span style="color:#FF5733;">wish</span>) par nirbhar karta hai. Ek tum mein se rajvansh (<span style="color:#FF5733;">dynasty</span>) ka vaanshaj (<span style="color:#FF5733;">heir</span>) janmega, aur doosri mein 60,000 tejasvi (<span style="color:#FF5733;">radiant</span>) putra honge.”  Rani Keshini ne kaha — “Mujhe ek putra chahiye jo mahan bane.”  Aur Rani Sumati ne kaha — “Mujhe 60,000 veer (<span style="color:#FF5733;">brave</span>) putra chahiye.”  

Kuch samay baad, Rani Keshini ne ek putra ko janm diya — uska naam rakha gaya Asamanjasa. Aur Rani Sumati ke garbh se ek bada sa lauki (<span style="color:#FF5733;">gourd</span>) nikla! ab use khola gaya, to usme se 60,000 chhote shishu (<span style="color:#FF5733;">babies</span>) nikle! Unhe makhan (<span style="color:#FF5733;">butter</span>) ke ghado (<span style="color:#FF5733;">pots</span>) mein rakha gaya aur sambhala gaya, aur dheere-dheere woh bade hoke veer yuva (<span style="color:#FF5733;">young warriors</span>) ban gaye.  
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Lekin Asamanjasa ek ajeeb ladka nikla — woh nadi Sarayu ke paas jaakar chhote bachchon ko pakad kar pani mein phenka karta tha! Aur jab bachche doob jaate, to woh hans kar khush hota. Uske bure kaamon se praja dukhi ho gayi aur usse rajya se nikal diya gaya. Uska ek beta tha — Amshuman, jo bahadur, vinamra (<span style="color:#FF5733;">polite</span>), aur sabka priya (<span style="color:#FF5733;">beloved</span>) tha. kuch varsh baad, Raja Sagara ne socha — “Ab mujhe ek mahaan yajna (<span style="color:#FF5733;">sacrifice</span>) karna chahiye.” Unhone apne purohit (<span style="color:#FF5733;">priests</span>) ko bula kar yajna ki tayyari shuru ki.  Aur isi se shuru hoti hai Raja Sagara aur unke vansh ki adbhut kahani — jisme Ganga ka prithvi par aana likha gaya hai.
        """
        create_image_text_layout("attached_assets/chapter1/1.38.2.jpg", text3, layout="side", image_position="right")
    
    # Chapter39
    with st.expander("Chapter 1.39 - Sagara’s horse is stolen during a yajna"):

        text1 = """
Jab Shri Rama ne Raja Sagara ki purani kahani suni, to unhone muskurate hue Vishvamitra Muni se kaha —
“Hey Muni, aap hamesha sukhi (<span style="color:#FF5733;">prosperous</span>) rahen! Mujhe batayein, mere poorvaj (<span style="color:#FF5733;">ancestor</span>) Raja Sagara ne yajna (<span style="color:#FF5733;">sacrifice</span>) kaise kiya tha?”

Rishi Vishvamitra, Rama ki utsukta (<span style="color:#FF5733;">curiosity</span>) dekh kar prasann (<span style="color:#FF5733;">happy</span>) hue aur bole —
“Suno Rama! Himalaya aur Vindhya parvat ke beech ek pavitra bhoomi (<span style="color:#FF5733;">holy land</span>) hai. Wahi jagah Raja Sagara ne apna maha-yajna kiya tha.
Us yajna ke liye ek pavitra ghoda (<span style="color:#FF5733;">sacrificial horse</span>) chhoda gaya tha, jiska raksha (<span style="color:#FF5733;">protection</span>) karne ka kaam Raja Sagara ne Amshuman, apne veer (<span style="color:#FF5733;">brave</span>) pothay (<span style="color:#FF5733;">grandson</span>), ko diya tha.” Lekin kuch samay baad, ek rakshas (<span style="color:#FF5733;">demon</span>) bhesh (<span style="color:#FF5733;">disguise</span>) badal kar aaya aur yajna wala ghoda chura le gaya! 🐎💨
        """
        create_image_text_layout("attached_assets/chapter1/1.39.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Jab purohit (<span style="color:#FF5733;">priests</span>) ne dekha ki ghoda gayab ho gaya hai, to woh ghabra kar raja ke paas daudte hue aaye aur bole —
“Hey Maharaj! Koi dusht (<span style="color:#FF5733;">wicked</span>) chaur (<span style="color:#FF5733;">thief</span>) ghoda le gaya hai! Kripya turant use dhoondh kar wapas layein!” Raja Sagara ne apne 60,000 putron ko bulaya aur kaha —
“Mere veer putro! Ek rakshas (<span style="color:#FF5733;">demon</span>) ne hamara yajna (<span style="color:#FF5733;">sacrifice</span>) ka ghoda chura liya hai.
Tum sab usse dhoondo aur dharti (<span style="color:#FF5733;">earth</span>) ke chaaro taraf talash karo. Main yajna (<span style="color:#FF5733;">sacrifice</span>) se uth nahi sakta, isliye tum sab jao aur tab tak khoj (<span style="color:#FF5733;">search</span>) karo jab tak ghoda mil na jaye!”

Raja Sagara ke putron ne apne pita ka aadesh (<span style="color:#FF5733;">command</span>) suna aur bade utsah (<span style="color:#FF5733;">enthusiasm</span>) se puri dharti (<span style="color:#FF5733;">earth</span>) par khoj (<span style="color:#FF5733;">search</span>) shuru ki. Lekin jab ghoda kahin nahi mila, to unhone apne nakhun (<span style="color:#FF5733;">nails</span>) — jo vajra (<span style="color:#FF5733;">diamond</span>) jaise sakht the — se dharti (<span style="color:#FF5733;">earth</span>) ko khodna (<span style="color:#FF5733;">dig</span>) shuru kar diya! Jab unhone zameen khodni shuru ki, to poori dharti (<span style="color:#FF5733;">earth</span>) kaanp uthi! Unhone hal (<span style="color:#FF5733;">ploughs</span>), kodal (<span style="color:#FF5733;">spades</span>), aur anya auzaar (<span style="color:#FF5733;">tools</span>) se zameen ko ukhad diya. Is prakriya (<span style="color:#FF5733;">process</span>) mein kai naag (<span style="color:#FF5733;">serpents</span>), rakshas (<span style="color:#FF5733;">demons</span>), aur asur (<span style="color:#FF5733;">evil beings</span>) mare gaye.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Ve dharti (<span style="color:#FF5733;">earth</span>) ko 60,000 yojan (<span style="color:#FF5733;">miles</span>) tak khodte gaye!
Unhone parvaton (<span style="color:#FF5733;">mountains</span>) ko cheer diya, samudron (<span style="color:#FF5733;">oceans</span>) ko hilaa diya, aur Jambudweep (<span style="color:#FF5733;">earth’s realm</span>) tak pahunch gaye.

Itni tabahi (<span style="color:#FF5733;">destruction</span>) dekh kar sab devta (<span style="color:#FF5733;">gods</span>), gandharva (<span style="color:#FF5733;">celestial musicians</span>), aur naag (<span style="color:#FF5733;">serpent beings</span>) dare hue Brahma ji ke paas gaye aur vinamr (<span style="color:#FF5733;">humbly</span>) hokar bole —
“Hey Prabhu! Raja Sagara ke putra poori dharti (<span style="color:#FF5733;">earth</span>) ko khod kar bigaad rahe hain!
Jo bhi unhe rokta hai, use ve turant maar kar kehte hain — ‘Tu chor (<span style="color:#FF5733;">thief</span>) hai! Tu hi ghoda chura kar le gaya!’” Aise Raja Sagara ke putron ki talash (<span style="color:#FF5733;">search</span>) ab ek bade rahasya (<span style="color:#FF5733;">mystery</span>) ki taraf badh rahi thi —
ghoda kaha gaya tha, aur kisne chura liya tha? 
        """
        create_image_text_layout("attached_assets/chapter1/1.39.2.jpg", text3, layout="side", image_position="right")
    
    # Chapter40 
    with st.expander("Chapter 1.40 - Sagara’s sons search for the horse"):

        text1 = """
Jab Raja Sagara ke putron ne dharti (<span style="color:#FF5733;">earth</span>) khodna shuru kiya, to us shor-sharabe (<span style="color:#FF5733;">uproar</span>) se poori dharti gungunane lagi, jaise bijli (<span style="color:#FF5733;">thunder</span>) gir rahi ho! Raja Sagara ke veer putron ne duniya ka chakkar lagaya, devtaon (<span style="color:#FF5733;">gods</span>), rakshas (<span style="color:#FF5733;">demons</span>), aur naag (<span style="color:#FF5733;">serpents</span>) ko haraya, lekin yajna ka ghoda ya chor (<span style="color:#FF5733;">thief</span>) kahin nahi mila.

Ve laut kar apne pita ke paas aaye aur bole — “Hey Pita! Humne poori dharti ghoom li, lekin ghoda kahin nahi mila. Kripya humein aadesh dein ki kya karein.” Raja Sagara ne krodh (<span style="color:#FF5733;">anger</span>) se kaha —
“Jaao! Dharti ko phir se khodo, ghoda pakdo, apna kaam poora karo aur wapas aao!”
        """
        create_image_text_layout("attached_assets/chapter1/1.40.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Dharti ke Rahasyamay (<span style="color:#FF5733;">mysterious</span>) Jeev Sagara ke putron ne phir se khodna shuru kiya aur pehli baar ek mahan haathi (<span style="color:#FF5733;">giant elephant</span>) dekha, jo parvat (<span style="color:#FF5733;">mountain</span>) jaise bada tha! Naam tha Vimpaksha, aur uski har chaal (<span style="color:#FF5733;">step</span>) se poori dharti kaanp jaati thi! Ve putra uske saamne jhuke aur uska dhyan se samman (<span style="color:#FF5733;">salutations</span>) kiya.

Phir ve dusre haathi Mahapadma ko dekhe, jo dharti ke doosre hisse ko sambhal raha tha.
Aur Hima-Pandara, ek safed (<span style="color:#FF5733;">white</span>) haathi, jo uttari (<span style="color:#FF5733;">northern</span>) bhag ko sambhal raha tha, usse bhi unhone pooja (<span style="color:#FF5733;">worship</span>) ki.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Kapila Muni aur Ghoda Ant me, ve poore utsah (<span style="color:#FF5733;">zeal</span>) ke saath khodte hue Shri Kapila ke paas pahunch gaye, jahan ghoda char raha tha.
Soch kar ki Kapila ne ghoda chura liya, ve krodhit (<span style="color:#FF5733;">angry</span>) hue aur ploughs, ped (<span style="color:#FF5733;">trees</span>), pathar (<span style="color:#FF5733;">rocks</span>) utha kar unke paas bhaage, chillate hue —
“Tu ghoda churaane wala chor (<span style="color:#FF5733;">thief</span>) hai! Hum Sagara ke putra tumhe pakad lenge!” Lekin Shri Kapila, jo anant shakti (<span style="color:#FF5733;">immeasurable power</span>) wale the, sirf ek ‘H’m’ ki aawaz se ve sab raakh (<span style="color:#FF5733;">ashes</span>) ho gaye! 
        """
        create_image_text_layout("attached_assets/chapter1/1.40.2.jpg", text3, layout="side", image_position="right")

    # Chapter41
    with st.expander("Chapter 1.41 - Amshuman finds the horse and his uncle’s ashes"):

        text1 = """
Raja Sagara ko bahut din beet gaye lage the. Uske bete ghaayab (<span style="color:#FF5733;">missing</span>) the aur yajna (<span style="color:#FF5733;">sacrifice</span>) bhi adhoora tha. Tab usne apne pyaare pota, Amshuman (<span style="color:#FF5733;">grandson</span>) ko bulaya.
“Beta,” bola raja, “tu bahadur (<span style="color:#FF5733;">brave</span>) aur samajhdaar hai. Jaake mere bhaiyon ko aur us ghode (<span style="color:#FF5733;">horse</span>) ko dhoondh la. Sambhal ke ja — talwar, dhanush (<span style="color:#FF5733;">bow</span>) aur teer le.”

Amshuman ne turant taiyaari ki. Raste mein usko devta (<span style="color:#FF5733;">gods</span>), naag (<span style="color:#FF5733;">serpents</span>), aur anya praani milke samman (<span style="color:#FF5733;">respect</span>) diye. Woh sab kah rahe the — “Aage badh, tera kaam safal hoga.”



        """
        create_image_text_layout("attached_assets/chapter1/1.41.1.jpg", text1, layout="side", image_position="left")

        text2 = """
Woh pahunchta gaya — aur pahle us bade haathi (<span style="color:#FF5733;">elephant</span>) se mila, jo zameen ko sambhalte the. Haathi ne kaha, “Beta, aage ja — tera uddeshya poora hoga.” Amshuman ne sab haathiyon ko pranam (<span style="color:#FF5733;">bowed</span>) kiya aur aage chala. Phir ek bhayanak jagah par Amshuman ko kuch dikhayi pada — zameen mein badi badi raakh (<span style="color:#FF5733;">ashes</span>) ki ek bhari chita si padi thi. Wo dekhta hi rona shuru kar diya. Ye raakh uske chachaon (<span style="color:#FF5733;">uncles</span>) ki thi — jo kapila muni ke samne gusse mein jal kar khatam ho gaye the.

Tabhi uska nazar ek bada sa garud (<span style="color:#FF5733;">eagle</span>) par pada — jo uska mamu (<span style="color:#FF5733;">maternal uncle</span>) tha. Garud ne kaha:
“Hey veer (<span style="color:#FF5733;">hero</span>) Amshuman, in putron ka nash (<span style="color:#FF5733;">destruction</span>) Kapila muni ke gusse se hua — yeh unki kismet thi. Ab jo tyohaar (<span style="color:#FF5733;">funeral rite</span>) karna hai woh seedha nahi kiya ja sakta. Inki antya-kriya (<span style="color:#FF5733;">last rites</span>) tabhi safal hogi jab inki raakh par Ganga (<span style="color:#FF5733;">the holy river</span>) ka pavitra paani (<span style="color:#FF5733;">sacred water</span>) chhodega.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Amshuman ne turant ghoda pakda aur wapas Ayodhya gaya. Usne raja ko sab kuch bataya — raakh, Garud ki baat aur Ganga ki maang. Raja Sagara ne socha, bahut prayas kiye — par Ganga ko dharti par laana aasaan nahi tha.

Aise bahut saal beet gaye. Raja Sagara ne bahut rajya kiya, par jab tak Ganga zameen par nahi utari, uske parivaar ki shanti (<span style="color:#FF5733;">peace</span>) adhuri rahi. Aakhirkaar, Raja Sagara apne dharm (<span style="color:#FF5733;">duty</span>) poore karne ke baad is jagah se chale gaye.
        """
        create_image_text_layout("attached_assets/chapter1/1.41.2.jpg", text3, layout="side", image_position="right")

    # Chapter42
    with st.expander("Chapter 1.42 - Bhagiratha does penance to bring Ganga down"):

        text1 = """
Raja Amshuman ke baad, uske mantri (<span style="color:#FF5733;">ministers</span>) ne rajya (<span style="color:#FF5733;">kingdom</span>) sambhal liya aur Amshuman ke putra Dilipa ko raja bana diya. Amshuman ne Himalaya ki unchaiyon (<span style="color:#FF5733;">peaks</span>) par jaake kathin yogic tapasya (<span style="color:#FF5733;">meditation & penance</span>) ki. 32,000 saal tak tapasya karne ke baad bhi pavitra nadi (<span style="color:#FF5733;">holy river</span>) Ganga zameen par nahi aayi, aur Amshuman ne apni atma (<span style="color:#FF5733;">soul</span>) ko mukti (<span style="color:#FF5733;">released</span>) de di.

Raja Dilipa, apne purvajon (<span style="color:#FF5733;">ancestors</span>) ki stithi dekh kar bahut dukhi (<span style="color:#FF5733;">grieved</span>) tha. Usne roz socha ki Ganga ko kaise dharti par laya jaaye aur apne purvajon ki antya-kriya (<span style="color:#FF5733;">funeral rites</span>) poori ho. Tabhi uske ghar mein ek santan (<span style="color:#FF5733;">child</span>) ka janm hua — Bhagiratha. Bhagiratha bada hoke ek dharmic (<span style="color:#FF5733;">righteous</span>) aur shaktishaali (<span style="color:#FF5733;">powerful</span>) raja bana. Lekin uska mann tha ki woh apne purvajon ki aatmaon ko mukti de aur Ganga ko dharti par laye.
        """
        create_image_text_layout("attached_assets/chapter1/1.42.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Bhagiratha ne rajya apne mantriyon ko de diya aur Gokama ke pavitra sthal (<span style="color:#FF5733;">holy place</span>) par jaake kathin tapasya karne laga. Usne apne haath upar karke, indriyon (<span style="color:#FF5733;">senses</span>) ko niyantrit (<span style="color:#FF5733;">controlled</span>) karke paanch agniyon (<span style="color:#FF5733;">fires</span>) ke beech khade hokar, sirf mahine mein ek baar bhojan (<span style="color:#FF5733;">food</span>) liya. Ye tapasya hazaar saal tak chalti rahi!

Akhirkaar, Shri Brahma, sabke bhagwan (<span style="color:#FF5733;">Lord of the world</span>), Bhagiratha ki tapasya se prasanna (<span style="color:#FF5733;">pleased</span>) hue. Unhone kaha:
“Bhagiratha beta, tumhari tapasya bahut shubh hai. Kuch bhi mangho (<span style="color:#FF5733;">ask</span>) aur tumhari iccha poori ho.”Bhagiratha ne vinamrata (<span style="color:#FF5733;">humble</span>) se kaha:
“Hey Bhagwan, meri tapasya ka phal (<span style="color:#FF5733;">fruit</span>) ye ho ki mai apne purvajon ki aatmaon ko mukti de sakun — unki antya-kriya Ganga ke pavitra paani (<span style="color:#FF5733;">holy water</span>) se ho. Aur kripya mujhe santan (<span style="color:#FF5733;">heir</span>) bhi de do, taaki Ikshvaku vansh (<span style="color:#FF5733;">dynasty</span>) bana rahe.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Shri Brahma ne kaha:
“Bhagiratha, tumne maha mangal (<span style="color:#FF5733;">great wish</span>) maangi hai. Tumhara santan hoga. Lekin Ganga, Himalaya ki sabse badi beti, jab dharti par aayegi, dharti use nahi sambhal paayegi. Sirf Shiv hi is shakti ko sambhal sakte hain.” Phir Shri Brahma aur devta apni sthaan (<span style="color:#FF5733;">region</span>) par wapas chale gaye aur Bhagiratha ki tapasya ka fal dene ke liye tayari ho gayi.
        """
        create_image_text_layout("attached_assets/chapter1/1.42.2.jpg", text3, layout="side", image_position="right")

    # Chapter43
    with st.expander("Chapter 1.43 - Lord Shiva lets the sacred river flow"):

        text1 = """
Raja Bhagiratha ne apni tapasya (<span style="color:#FF5733;">austerities / hard meditation</span>) bahut hi shiddat (<span style="color:#FF5733;">intensity</span>) se ki. Ek saal tak, sirf ek ungli (<span style="color:#FF5733;">toe</span>) par khade hokar, haath upar karke, hawa par tairte hue, Bhagiratha ne Shri Shiva ki pooja (<span style="color:#FF5733;">adoration</span>) ki.

Akhirkaar, Shri Mahadeva (<span style="color:#FF5733;">Shiva</span>), jo sabko poojya (<span style="color:#FF5733;">adored</span>) hai, Bhagiratha se bole:
“Hey Bhagiratha, mai khush hoon. Jo tum chahte ho, mai poora karunga — mai Ganga ko apne sir par grahan (<span style="color:#FF5733;">receive</span>) karunga.”

Fir, Himalaya ki sabse badi beti, Ganga Devi, ek maha-nadi (<span style="color:#FF5733;">mighty river</span>) ban kar Shiva ke sir par utarni lagi. Usne socha ki yeh itni shakti se aayegi ki Shiva ko dharti se utha de.
        """
        create_image_text_layout("attached_assets/chapter1/1.43.1.jpg", text1, layout="side", image_position="left")


        text2 = """

Shiva ne ye socha aur gusse (<span style="color:#FF5733;">anger</span>) mein aakar, apne baalon (<span style="color:#FF5733;">locks of hair</span>) mein Ganga ko rok liya. Itni saalon tak Ganga Shiva ke baalon mein phasi rahi aur zameen tak nahi pahunchi. Fir Bhagiratha ne phir se apni tapasya shuru ki. Shiva, Bhagiratha ki tapasya dekh kar, Ganga ko Brindusara jheel (<span style="color:#FF5733;">lake</span>) mein bahne diya. Aur wahan se Ganga 7 nadiyon (<span style="color:#FF5733;">streams</span>) mein bat gayi: Hladini, Pavani, Nalini — east ki taraf Sucakshu, Sita, Sindhav — west ki taraf 7th stream — Bhagiratha ke chariot (<span style="color:#FF5733;">divine cart</span>) ke peeche
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Raja Bhagiratha apne shahi rath (<span style="color:#FF5733;">royal chariot</span>) mein aage badhe aur Ganga Devi unke peeche chal rahi thi. Jab Ganga ne dharti par paani (<span style="color:#FF5733;">water</span>) giraya, tab devta, rishi, yaksha, aur swarg ke saare log (<span style="color:#FF5733;">celestial beings</span>) aaye aur us pavitra nadi ko dekha. Paani ki jhalak (<span style="color:#FF5733;">sparkle</span>) itni sundar thi ki jaise bijli chamak rahi ho ya hans (<span style="color:#FF5733;">swans</span>) ud rahe ho.

Fir Bhagiratha Ganga ke paani se apne purvajon (<span style="color:#FF5733;">ancestors</span>) ki antya-kriya (<span style="color:#FF5733;">funeral rites</span>) poori karne laga. Jaise hi pavitra Ganga ne unke ashes (<span style="color:#FF5733;">raakh</span>) ko chhua, King Sagara ke 60,000 putraon ki atmaen pavitra ho gayi aur ve swarg (<span style="color:#FF5733;">heaven</span>) ko chali gayi.
        """
        create_image_text_layout("attached_assets/chapter1/1.43.2.jpg", text3, layout="side", image_position="right")

    # Chapter44
    with st.expander("Chapter 1.44 - Bhagiratha completes the funeral rites"):

        text1 = """
Raja Bhagiratha, pavitra Ganga Devi ke saath, samundar ke kinare (<span style="color:#FF5733;">seashore</span>) pahunch gaye. Wahan unhone Zameen ke neeche ke kshetra (<span style="color:#FF5733;">subterranean region</span>) mein jaakar dekha ki King Sagara ke 60,000 putra raakh (<span style="color:#FF5733;">ashes</span>) mein badal chuke the.

Jab Ganga ka paani un ashes par gira, tab Shri Brahma, jo sabhi jagat ke prabhu (<span style="color:#FF5733;">Lord of the Worlds</span>) hain, Bhagiratha se bole: “Hey Bhagiratha, tumne King Sagara ke 60,000 putron ki atmaon ko mukti (<span style="color:#FF5733;">redeem / free</span>) dilayi. Ve ab swarg (<span style="color:#FF5733;">heaven</span>) mein sukh se baste hain. Jab tak samundar ka paani dharti par rahega, tab tak ye putra swarg mein sukh paate rahenge.
        """
        create_image_text_layout("attached_assets/chapter1/1.44.1.jpg", text1, layout="side", image_position="left")

        text3 = """
Ab se, Ganga Devi tumhari badi beti (<span style="color:#FF5733;">eldest daughter</span>) ke roop mein jaani jayengi aur duniya bhar mein tumhare naam se pavitra nadi ke roop mein prasiddh (<span style="color:#FF5733;">famous</span>) rahengi. Is nadi ko Shri Ganga, Tripathaga aur Bhagirathi kaha jayega.”

Brahma ne aage kaha:  
“Bhagiratha, apne purvajon ke funeral rites poore karna tumhara kartavya (<span style="color:#FF5733;">duty</span>) hai. Pehle King Sagara, King Amshuman, aur tumhare pita Dilipa bhi ye kaam nahi kar paaye the. Par tumne hi is maha-kaarya (<span style="color:#FF5733;">great task</span>) ko poora kiya. Tumne apna dharma (<span style="color:#FF5733;">sacred duty</span>) sampurn kiya aur duniya mein amar (<span style="color:#FF5733;">undying</span>) naam kamaya.”

Phir Bhagiratha ne Ganga ke paani se apne purvajon ki antya-kriya ki aur unke ashes ko pavitra (<span style="color:#FF5733;">holy</span>) kar diya. Uske baad ve apne rajya (<span style="color:#FF5733;">kingdom</span>) wapas gaye. Log khushi se jhoom uthe, sabko sukh-shanti mili, aur desh mein dhani, samruddh aur prasannata aayi.
        """
        create_image_text_layout("attached_assets/chapter1/1.44.2.jpg", text3, layout="side", image_position="right")

    # Chapter45 
    with st.expander("Chapter 1.45 - The city of Vishala and the churning of the ocean"):

        text1 = """
Shri Rama aur Lakshmana, Shri Vishvamitra ki kahani sun kar hairan ho gaye. Dono ne kaha: “Wow, Maharishi! King Sagara aur Ganga Devi ki kahani sach mein adbhut hai!” Raat guzar gayi aur dono raja-mahraj ne socha ki kaise ye pavitra nadi dharti par aayi. Subah, Shri Rama ne apni pooja karke Vishvamitra se poocha: “Maharishi, ab humein Ganga ke is pavitra aur adbhut janm ki aur yatra ka pata chala hai. Chaliye is nadi ko paar karte hain aur sages se milte hain.” Shri Vishvamitra ne ferryman bulaya aur sabko nadi ke paar pahunchaya. Wahan se unhone door ek shandar Vishala City dekhi, jo Indra ke sheher jaise sukhad aur shobha se bhara tha. Rama ne poochha: “Maharishi, ye shandar sheher kaun chalata hai? Mujhe iska itihas sunaiye.”

        """
        create_image_text_layout("attached_assets/chapter1/1.45.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Vishvamitra ne shuru kiya: “O Rama! Suno! Ye kahani maine Indra se suni hai. Satya Yuga mein, Diti ne ek balwaan beta paida kiya, jo Daitya / Asura (<span style="color:#FF5733;">Daitya / Asura</span>) ban gaya. Aur Aditi ne ek dharmik aur shaktishaali beta paida kiya, jo Deva (<span style="color:#FF5733;">Deva</span>) bana. Ye dono chahte the ki ve amar aur swasth rahein. Sochne ke baad, unhone decide kiya ki Kshiroda (<span style="color:#FF5733;">ocean of milk</span>) ko churn kar Amrit (<span style="color:#FF5733;">nectar of immortality</span>) prapt karenge.

Is ke liye unhone Vasuki (<span style="color:#FF5733;">snake</span>) ko rassi banaya aur Mandara Mountain ko churn karne ke liye use kiya. Saalon tak churning ke baad, Vasuki ne zeher udaya, jo duniya ko khatam kar sakta tha. Devas ne Lord Shiva ke paas jaakar prarthana ki:  
“Hey Mahadeva! Humein bachaiye!” Shri Shiva ne us zeher ko apni gardan se rok liya aur duniya ko bachaya.

Phir churning jaari raha. Lekin Mandara Mountain dhansne laga. Devas aur gandharvas ne Shri Vishnu se madad maangi. Vishnu ne Kachhua (<span style="color:#FF5733;">tortoise</span>) ka roop dharan kiya aur pahaad ko samarthan diya. Kayi saal baad, Shri Dhanvantari prakat hua, jiske saath bahut saari sundar Apsaras (<span style="color:#FF5733;">jal se nikalne wali devi</span>) bhi aayi.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Iske baad Varuni, Varuna ki beti, janmi. Devas ne use nahi liya, par Asuras ne khushi se swikar kiya. Phir Uccaihshravas (<span style="color:#FF5733;">divine horse</span>) aur Kaustubha (<span style="color:#FF5733;">jewel</span>) samudra se nikal aaye. Ant mein, Amrit (<span style="color:#FF5733;">nectar of immortality</span>) bhi samundar se prapt hua.

Devas aur Daityas ke beech ladai hui, par Shri Vishnu ne Mohini ka roop dharan (<span style="color:#FF5733;">taking the form of Mohini</span>) karke Amrit (<span style="color:#FF5733;">nectar of immortality</span>) ko bachaya. Jin logon ne Vishnu ka virodh kiya, ve vinash ho gaye. Iske baad, Indra devas ka raja bana aur dharmik tareeke se rajya karne laga.”
        """
        create_image_text_layout("attached_assets/chapter1/1.45.2.jpg", text3, layout="side", image_position="right")

    # Chapter46 
    with st.expander("Chapter 1.46 - Diti does penance to have a powerful son"):

        text1 = """
Ek samay ki baat hai, O Rama, jab Diti bahut dukhi thi. Uske bachche, jo shaktishaali the, Indra ne maar diye the. Diti ka dil to toot gaya. Vo apne pati Rishi Kashyapa ke paas gayi aur boli,
“Prabhu, aapke shaktishaali putron ne mere bachche le liye. Main chahti hoon ek aisa beta jo Indra ko hara sake. Main chahe kitna bhi kathin (<span style="color:#FF5733;">hard</span>) tap karna pade, main karungi — bas aap mujhe aisa putra dena jo balvaan (<span style="color:#FF5733;">strong</span>), veer (<span style="color:#FF5733;">brave</span>) aur dridh sankalp wala ho.”

Rishi Kashyapa ne shaant mann se kaha,
“Be it so! Agar tum ek hazaar saal tak pavitra (<span style="color:#FF5733;">pure</span>) raho aur kathin tap karo, to tumhe ek beta milega jo Indra ko hara sakta hai. Mere ashirwad se tumhara beta teenon lok (<span style="color:#FF5733;">worlds</span>) ka raja hoga.” Diti ko santosh mila aur vo Kushaplava van (<span style="color:#FF5733;">forest</span>) mein chali gayi. Wahaan usne kathin tapasya (<span style="color:#FF5733;">penance</span>) shuru ki.
        """
        create_image_text_layout("attached_assets/chapter1/1.46.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Indra ne ye sab dekha aur samjha — “Agar ye beta paida ho gaya, to mera vinash (<span style="color:#FF5733;">destruction</span>) nischit hai.”
To Indra ne chalaki se Diti ki seva karni shuru ki. Har din vo use aag, kusha grass aur sab zaroori cheezein laakar deta, aur jab Diti thak jaati, to uske pair dabaata. Aise hi Indra ne ek hazaar saal minus das din tak seva ki. Phir Diti khush hokar boli,
“Indra, tumhara pita ne mujhe vachan diya hai. Ab bas das din baaki hain, fir tumhara bhai janm lega — jo tumhe hara sakta hai, par main chahti hoon tum dono milkar teenon lok sambhalo.”

Lekin, ek dopahar Diti thak gayi aur galti se ulte pair rakhkar so gayi — jo tapasya mein ashuddh (<span style="color:#FF5733;">impure</span>) mana jata hai. Indra ne ye dekha aur hans pada. Usne socha, “Ab mauka mil gaya!”
Woh Diti ke shareer mein apni shakti se ghus gaya aur uske garbh (<span style="color:#FF5733;">womb</span>) mein bachche ko apne gadha (<span style="color:#FF5733;">mace</span>) se saat tukdon mein kaat diya.

        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Tab Diti ne dard se chillakar kaha,
“Mat maaro, mat maaro!”
Par Indra ne har baar bola, “Rud mat karo (<span style="color:#FF5733;">Don’t weep</span>), rud mat karo,” aur fir bhi tukde kar diye.

Jab sab khatam hua, Indra ne vinamr (<span style="color:#FF5733;">humble</span>) hokar kaha,
“Hey Devi, maaf kardo. Tumne apne pair usi disha mein rakhe jahan sir hona chahiye tha — ye ashuddh kriya thi. Tumhara beta mera vinaash banne wala tha, isliye mujhe ye karna pada. Mujhe kshama karo (<span style="color:#FF5733;">forgive me</span>).” Aur is tarah Diti ka kathin tap ek kathin ant tak pahucha, jahan se ek nayi katha ki shuruaat hoti hai — Marut devtaon ki.
        """
        create_image_text_layout("attached_assets/chapter1/1.46.2.jpg", text3, layout="side", image_position="right")

    # Chapter47 
    with st.expander("Chapter 1.47 - The sages and princes reach Vishala"):

        text1 = """
Diti, jo apne foetus ko saat parts me divide hone ke baad pareshaan (<span style="color:#FF5733;">worried/upset</span>) thi, Indra se boli:
“Ye sab meri galti (<span style="color:#FF5733;">fault/mistake</span>) se hua, O Indra, aap bilkul dosh-mukt (<span style="color:#FF5733;">blameless</span>) hain. Ye saat parts ab forty-nine winds ke protector (<span style="color:#FF5733;">guardian/defender</span>) banenge. Ye saat divine appearance (<span style="color:#FF5733;">god-like appearance</span>) wale beta Bala-kanda winds ke naam se jane jayenge. Ek Brahma ke region me ghoome, ek Indra ke region me, ek space me, aur baaki chaar aapke instructions (<span style="color:#FF5733;">orders/directions</span>) ke hisaab se kahin bhi jaayein. Ye sab Maruts ke naam se jane jayenge.”

Indra, jiski aankhen thousand-eyed (<span style="color:#FF5733;">having a thousand eyes / all-seeing</span>) thi, ne kaha:
“O Devi (<span style="color:#FF5733;">goddess/mother</span>), aapki ichha (<span style="color:#FF5733;">wish/desire</span>) poori hogi. Aapke beta Tapovana forest me devas (<span style="color:#FF5733;">divine beings/gods</span>) ke roop me ghoomenge.” Phir maa aur beta khushi se heaven (<span style="color:#FF5733;">swarg</span>) me chale gaye.

        """
        create_image_text_layout("attached_assets/chapter1/1.47.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Yahi wahi Tapovana forest hai jahan Indra pehle Diti ki seva (<span style="color:#FF5733;">service/help</span>) karta tha. Yahan ek great city Vishala banayi gayi, jo righteous (<span style="color:#FF5733;">pious/virtuous</span>) Prince Vishala (King Ikswaku aur Alambusa ka beta) ne establish ki. Vishala ke vanshaj (<span style="color:#FF5733;">descendants</span>): Vishala ka beta: Hemacandra, Hemacandra ka beta: Sucandra, Sucandra ka beta: Dhumrashva, Dhumrashva ka beta: Srinjaya, Srinjaya ka beta: Sahadeva, Sahadeva ka beta: Krishashva, Krishashva ka beta: Somadatta, Somadatta ka beta: Kakustha, Kakustha ka beta: King Pramati (Vishala ke present ruler, illustrious (<span style="color:#FF5733;">famous/glorious</span>) aur invincible (<span style="color:#FF5733;">unbeatable</span>)), Sab rulers, King Ikswaku ki kripa (<span style="color:#FF5733;">grace/blessing</span>) se, long-lived, virtuous (<span style="color:#FF5733;">good/pious</span>) aur mighty (<span style="color:#FF5733;">strong/powerful</span>) the.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Rama ne kaha: “Chalo yahan raat guzaarte hain, aur kal King Janaka se milte hain.” Jab King Pramati ne Shri Vishvamitra ke aane ki khabar suni, to wo apne spiritual preceptor (<span style="color:#FF5733;">teacher/guide</span>) aur relatives ke saath unhe welcome (<span style="color:#FF5733;">greet/honor</span>) karne aaye.
Unhone joined palms se due worship (<span style="color:#FF5733;">respectful prayer</span>) diya aur Shri Vishvamitra ki well-being poochi. King ne kaha:
“O Muni (<span style="color:#FF5733;">sage/holy man</span>), aaj mai bahut lucky hoon ki aapne mere kingdom me aane ki kripa ki. Mai sabse blessed (<span style="color:#FF5733;">fortunate</span>) hoon.”
        """
        create_image_text_layout("attached_assets/chapter1/1.47.2.jpg", text3, layout="side", image_position="right")

    # Chapter48 
    with st.expander("Chapter 1.48 - Sage Gautama’s hermitage"):

        text1 = """
King Pramati ne Shri Vishvamitra se poocha: “O Muni, ye dono yuva (<span style="color:#FF5733;">youth</span>) kaun hain? Ye devtaon (<span style="color:#FF5733;">god</span>) ke barabar shaktiwale lagte hain, haathi ki tarah chal rahe hain (<span style="color:#FF5733;">gait</span>), sher aur bail ki tarah bahadur hain, unki aankhen kamal jaise hain. Inke haath me talwar, dhanush aur baan (<span style="color:#FF5733;">quiver</span>) hain. Ye sundar hain, jaise swarg ke Asvins (<span style="color:#FF5733;">Asvin</span>). Ye paidal kyun aa rahe hain? Inke pita kaun hain?”

Shri Vishvamitra ne raja ko poori kahani batai ki kaise ye Siddha Ashram (<span style="color:#FF5733;">hermitage</span>) gaye aur asuron (<span style="color:#FF5733;">demon</span>) ka vadh kiya. Raja bahut khush hua aur in dono ko izzat (<span style="color:#FF5733;">respect</span>) se rakha. Shri Rama aur Lakshmana ko mehmaan nawazi (<span style="color:#FF5733;">hospitality</span>) mili aur raat yahi ruke. Agle din ve Mithilapuri, King Janaka ke rajdhani ke liye chale. Jab unhone shahar ko door se dekha, to bole: “Kitna sundar hai!” Phir unhone ek khubsurat aur khali (<span style="color:#FF5733;">uninhabited</span>) hermitage dekhi. Rama ne Vishvamitra se poocha: “O Muni, ye sundar hermitage kiski hai? Ye khali kyun hai?”

        """
        create_image_text_layout("attached_assets/chapter1/1.48.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Shri Vishvamitra ne jawab diya: “O Rama, suno. Ye Ashram Rishi Gautama ka tha aur bahut adbhut (<span style="color:#FF5733;">wonder</span>) tha, devtaon ke liye bhi. Yahan unki patni Ahalya ke saath ve yoga (<span style="color:#FF5733;">spiritual</span>) karte the, hazaaron saal tak. Ek din, jab Gautama door gaye, Indra ne Ahalya ko akela (<span style="color:#FF5733;">alone</span>) paaya. Usne apni shakl (<span style="color:#FF5733;">form</span>) Gautama ki le li aur kaha: ‘O Ahalya, main tumse prerit (<span style="color:#FF5733;">desire</span>) hoon, apna kartavya poora karein (<span style="color:#FF5733;">duty</span>).’

Ahalya ne pehchaana par haan kar di. Fir usne Indra se kaha: ‘O Indra, main khush hoon, ab chhupke jao. Gautama se bachao khud ko aur mujhe.’ Indra hans diya aur bola: ‘O sundar patni, main khush hoon. Ab jaata hoon.’ Tabhi Gautama wapas aaye. Gautama ko dekh kar Indra dar gaya. Gautama shakti se bhara (<span style="color:#FF5733;">powerful</span>), aag ki tarah chamak raha tha, haath me pavitra (<span style="color:#FF5733;">sacred</span>) fuel aur kusha ghas (<span style="color:#FF5733;">grass</span>) tha. Indra safed (<span style="color:#FF5733;">pale</span>) ho gaya. Gautama ne dekha aur usse shraap (<span style="color:#FF5733;">curse</span>) diya:
‘O burra, meri shakl lekar paap (<span style="color:#FF5733;">sin</span>) kiya. Ab tum shaktheen (<span style="color:#FF5733;">impotent</span>) ho jao.’
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """

Indra turant apni purush (<span style="color:#FF5733;">manhood</span>) shakti kho baitha. Phir Gautama ne Ahalya ko shraap diya:
‘Tum yahan sthir (<span style="color:#FF5733;">immovable</span>) rahogi hazaaron saal. Tumhara bhojan (<span style="color:#FF5733;">food</span>) sirf hawa hoga. Tum dhool jaise (<span style="color:#FF5733;">invisible</span>) dikhoongi. Jab Rama, Dasaratha ke putra, aayenge, tab tumhare paap dur honge. Use seva (<span style="color:#FF5733;">service</span>) karo bina swarth ke, tab tum apni asli roop me lautogi.’

Is tarah Gautama ne Ahalya ko shraap diya aur apna ashram chhod diya. Ve Himalaya (<span style="color:#FF5733;">mountains</span>) ki choti par jaake yoga (<span style="color:#FF5733;">practice</span>) karne lage, jahan siddh (<span style="color:#FF5733;">sage</span>) baste the.
        """
        create_image_text_layout("attached_assets/chapter1/1.48.2.jpg", text3, layout="side", image_position="right")

    # Chapter49 
    with st.expander("Chapter 1.49 - Rama frees Ahalya from the curse"):

        text1 = """
Indra, apni purush shakti (<span style="color:#FF5733;">virility</span>) kho dene ke baad, udaas (<span style="color:#FF5733;">melancholy</span>) ho gaya aur Agni aur doosre devtaon (<span style="color:#FF5733;">gods</span>) se bola: “Gautama Maharishi ke tapasya (<span style="color:#FF5733;">ascetic practices</span>) me badha daal kar, jinhone meri shakti (<span style="color:#FF5733;">power</span>) par kabza (<span style="color:#FF5733;">usurp</span>) karne ki koshish ki, maine devtaon ka kaam poora kiya. Unka krodh (<span style="color:#FF5733;">wrath</span>) bhadka kar, maine unka shraap (<span style="color:#FF5733;">curse</span>) apne upar bulaya aur Ahalya ko ninda (<span style="color:#FF5733;">denounce</span>) kiya. Ab mujhe meri shakti (<span style="color:#FF5733;">manhood</span>) wapas chahiye. O Devtaon, madad karo!” Phir devta, Agni ke netritva (<span style="color:#FF5733;">head</span>) me, pitris (<span style="color:#FF5733;">ancestors</span>), kavyavahanas aur doosre jeev (<span style="color:#FF5733;">beings</span>) ke paas gaye aur bole:

        """
        create_image_text_layout("attached_assets/chapter1/1.49.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“Indra apni purush shakti kho chuke hain. Is ram (<span style="color:#FF5733;">male Sheep</span>) ki shakti (<span style="color:#FF5733;">power</span>) ko Indra me graft karne do. Ram ko hum badle me puraskrit (<span style="color:#FF5733;">compensate</span>) karenge. Aaj se jo log aapko propitiate (<span style="color:#FF5733;">please</span>) karna chahenge, ve kastrated ram ka bali (<span style="color:#FF5733;">sacrifice</span>) dein aur bada punya (<span style="color:#FF5733;">merit</span>) prapt karein.” Pitris ne Agni ki baat maani aur ram ke testicles Indra me graft kiye. Tab se, logon ne hamesha gelded ram ka bali (<span style="color:#FF5733;">sacrifice</span>) dena shuru kiya. Ye ghatna (<span style="color:#FF5733;">event</span>) dikhaati hai ki Mahatma ki tapasya (<span style="color:#FF5733;">practice</span>) kitni apar (<span style="color:#FF5733;">immeasurable</span>) shaktiwali (<span style="color:#FF5733;">powerful</span>) hai.

Ab Shri Rama ne aadesh (<span style="color:#FF5733;">command</span>) maana aur hermitage me gaye, pehle Vishvamitra ke saath. Wahan unhone dekha Ahalya ko, jo apni yogic (<span style="color:#FF5733;">spiritual</span>) practice se shaktishaali (<span style="color:#FF5733;">powerful</span>) bani thi. Devas, asuras ya manushya (<span style="color:#FF5733;">men</span>) use nahi dekh sakte the. Ahalya itni sundar (<span style="color:#FF5733;">beautiful</span>) thi jaise Brahma ne khud banayi ho — ek nymph ki tarah, mist me chhupi hui, aur Rishi Gautama ke shraap (<span style="color:#FF5733;">curse</span>) ki wajah se invisible (<span style="color:#FF5733;">dikhai nahi dene wali</span>) rahi. Ye tab tak rahegi jab tak Shri Ramacandra use nahi dekhte.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Shri Rama aur Lakshmana ne Ahalya ke pair chume (<span style="color:#FF5733;">reverence</span>) aur Ahalya ne Gautama ke shraap ki baatein yaad karke unke samne shraddha (<span style="color:#FF5733;">devotion</span>) me gir gayi. Fir Ahalya ne unhe mehmaan nawazi (<span style="color:#FF5733;">hospitality</span>) di jaise shastra (<span style="color:#FF5733;">scriptures</span>) me likha hai. Rama aur Lakshmana ne bhi unki izzat (<span style="color:#FF5733;">honour</span>) sweekar ki. Tabhi swarg se phoolon (<span style="color:#FF5733;">flowers</span>) ki barish hui, devtaon ne baje, celestial nymphs (<span style="color:#FF5733;">swargiya pari</span>) ne naach kiya aur sab khush hue.

Gautama Maharishi, apni divya shakti (<span style="color:#FF5733;">divine power</span>) se sab jaan gaye aur hermitage aaye. Unhone dekha ki Ahalya apni asli roop (<span style="color:#FF5733;">form</span>) me laut gayi hai. Dono, Gautama aur Ahalya, Shri Rama ki pooja (<span style="color:#FF5733;">worship</span>) ki aur fir apni tapasya (<span style="color:#FF5733;">spiritual life</span>) continue ki. Shri Rama ne sabki vandana (<span style="color:#FF5733;">homage</span>) sweekar ki aur Mithila ke liye chale gaye.
        """
        create_image_text_layout("attached_assets/chapter1/1.49.2.jpg", text3, layout="side", image_position="right")

    # Chapter50
    with st.expander("Chapter 1.50 - King Janaka’s place of sacrifice"):

        text1 = """
Shri Rama aur Lakshmana, Sage Vishvamitra ke saath, King Janaka ke yagna (<span style="color:#FF5733;">sacrifice</span>) ke jagah par aaye. Unhone bada sundar mandap (<span style="color:#FF5733;">pavilion</span>) dekha aur bole: “King Janaka ne badi acchi taiyari (<span style="color:#FF5733;">preparation</span>) ki hai!”

Wahan hazaaron brahmins (<span style="color:#FF5733;">priests</span>) aaye hue the, Veda padhne waale, aur bahut saari gaadiyaan (<span style="color:#FF5733;">carts</span>) bhi thi. Rama aur Lakshmana ne Vishvamitra se kaha ki ek shaant jagah chun lo jahan woh aaram (<span style="color:#FF5733;">rest</span>) kar saken. Vishvamitra ne ek alag aur paani wali jagah chuni.

        """
        create_image_text_layout("attached_assets/chapter1/1.50.1.jpg", text1, layout="side", image_position="left")


        text2 = """
King Janaka ko jab pata chala ki Vishvamitra aa gaye hain, to woh apne purohit (<span style="color:#FF5733;">priest</span>) Shatananda aur mantrimandal (<span style="color:#FF5733;">ministers</span>) ke saath unko welcome karne aaya. Usne Vishvamitra ko honey-wala paani (<span style="color:#FF5733;">water with honey</span>) diya — yeh unki parampara (<span style="color:#FF5733;">tradition</span>). Janaka ne poocha ki sab kuch theek chal raha hai kya, aur poore samuh ka haal-chaal liya.

Phir Janaka ne pucha, “Ye dono jawaan veer (<span style="color:#FF5733;">princes</span>) kaun hain? Inki chal-dhal (<span style="color:#FF5733;">bearing</span>) aur shakti (<span style="color:#FF5733;">strength</span>) devta jaise hai. Kaun hain ye?”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """

Vishvamitra ne bataya: “Ye King Dasaratha ke putra (<span style="color:#FF5733;">sons</span>) hain.” Aur phir unhone unki purani kahani (<span style="color:#FF5733;">story</span>) sunayi — kaise woh Siddha-Ashrama gaye, asuron (<span style="color:#FF5733;">demons</span>) se lade, Ahalya ko bachaya, aur Gautama rishi se mile.

Ant mein Vishvamitra ne kaha ki ab woh sab mil kar bada dhanush (<span style="color:#FF5733;">bow</span>) dekhne jayenge — jo King Janaka ke paas rakha hua hai. Sab chup ho gaye aur aage ka safar tay hua.
        """
        create_image_text_layout("attached_assets/chapter1/1.50.2.jpg", text3, layout="side", image_position="right")

    # Chapter51
    with st.expander("Chapter 1.51 - Gautama’s son Shatananda"):

        text1 = """
Jab Mahatma Vishvamitra ne apni baatein samapt ki, tab Rishi Gautama ke putra (<span style="color:#FF5733;">son</span>) Shatananda, jo yog (<span style="color:#FF5733;">meditation and self-control</span>) ke bal se tejasvi (<span style="color:#FF5733;">radiant</span>) the, Shri Rama ko dekh kar adbhut (<span style="color:#FF5733;">wonder</span>) aur anand (<span style="color:#FF5733;">delight</span>) se bhar gaye.

Unhone Vishvamitra se pucha, “Hey Maharishi, kya meri maa Ahalya, jo itne saalon se tapasya (<span style="color:#FF5733;">austerity</span>) kar rahi thi, unhe aapne Shri Rama ko dikhaya? Kya meri maa ne in do veer (<span style="color:#FF5733;">brave</span>) Rajkumaron ka atithya (<span style="color:#FF5733;">hospitality</span>) phalon aur jo kuchh ashram mein mila, usse kiya? Kya aapne meri maa ko Indra ke dhokhe (<span style="color:#FF5733;">deception</span>) ki kahani bhi batayi? Kya Rama ke darshan (<span style="color:#FF5733;">sight</span>) se meri maa ko mere pita (<span style="color:#FF5733;">father</span>) ka kshama (<span style="color:#FF5733;">forgiveness</span>) mila? Aur kya mere pita ne Rama ka sammaan (<span style="color:#FF5733;">honour</span>) kiya?”

        """
        create_image_text_layout("attached_assets/chapter1/1.51.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Vishvamitra ne muskurate hue kaha, “Hey Mahamuni (<span style="color:#FF5733;">great sage</span>), maine wahi kiya jo samay aur dharm (<span style="color:#FF5733;">duty</span>) ke anusar uchit (<span style="color:#FF5733;">proper</span>) tha. Jaise Rishi Jamadagni ne apni patni Renuka ko shraap (<span style="color:#FF5733;">curse</span>) diya tha aur baad mein use kshama kiya, waise hi tumhare pita Gautama ne bhi Ahalya ko apne paas wapas swikar (<span style="color:#FF5733;">accept</span>) kiya.”

Ye sunkar Shatananda ne Shri Rama se kaha, “Hey Mahaan Purush (<span style="color:#FF5733;">great being</span>), aapka aagaman (<span style="color:#FF5733;">arrival</span>) sabke liye shubh (<span style="color:#FF5733;">auspicious</span>) hai. Aapne meri maa ko unke purane roop (<span style="color:#FF5733;">form</span>) mein lauta diya, ye bada punyakarya (<span style="color:#FF5733;">virtuous act</span>) hai. Kaun hai jo Vishvamitra jaise maharishi ki mahima (<span style="color:#FF5733;">glory</span>) ko poora varnan (<span style="color:#FF5733;">describe</span>) kar sake? Unhone rajrishi (<span style="color:#FF5733;">royal sage</span>) se brahmarishi (<span style="color:#FF5733;">highest sage</span>) tak ka safar tapasya aur gyaan se tay (<span style="color:#FF5733;">complete</span>) kiya. Unke jaise aur koi nahi.”

Phir Shatananda ne Rama se kaha, “Hey Rama, suno, main aapko Vishvamitra ka itihas (<span style="color:#FF5733;">story</span>) sunata hoon. Puraane samay mein ye bade dharmik (<span style="color:#FF5733;">virtuous</span>) aur gyaani (<span style="color:#FF5733;">wise</span>) raja the. Raja Kusha, jo Prajapati ke putra the, unka putra (<span style="color:#FF5733;">son</span>) tha Gadhi, aur Vishvamitra Gadhi ke putra (<span style="color:#FF5733;">son</span>) the.

Jab Vishvamitra ne rajya (<span style="color:#FF5733;">kingdom</span>) sambhala, to unhone hazaron saal tak dharm aur nyay (<span style="color:#FF5733;">justice</span>) se praja (<span style="color:#FF5733;">people</span>) ka palan (<span style="color:#FF5733;">govern</span>) kiya. Ek din unhone apni sena (<span style="color:#FF5733;">army</span>) ke saath duniya bhraman (<span style="color:#FF5733;">travel</span>) karne ka faisla kiya. Bahut se nagar (<span style="color:#FF5733;">cities</span>), nadiyan (<span style="color:#FF5733;">rivers</span>), pahaad (<span style="color:#FF5733;">mountains</span>) aur van (<span style="color:#FF5733;">forests</span>) paar karte hue, wo Rishi Vasishtha ke ashram (<span style="color:#FF5733;">hermitage</span>) tak pahuche.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Wo ashram ek swarg (<span style="color:#FF5733;">heaven</span>) jaisa tha — har tarah ke pedon, phoolon, aur pakshiyon (<span style="color:#FF5733;">birds</span>) se bhara hua. Shant mriga (<span style="color:#FF5733;">deer</span>) idhar-udhar ghoom rahe the, aur devata (<span style="color:#FF5733;">gods</span>), gandharva (<span style="color:#FF5733;">celestial musicians</span>) aur siddha (<span style="color:#FF5733;">perfected beings</span>) wahan aate the. Bahut se brahmin aur yogi (<span style="color:#FF5733;">sages</span>) wahan tap kar rahe the — kuchh hawa pe jeete, kuchh paani pe, aur kuchh fal-mool (<span style="color:#FF5733;">fruits and roots</span>) pe.

Sab apni pratha (<span style="color:#FF5733;">tradition</span>) ke anusar snan (<span style="color:#FF5733;">bath</span>), japa (<span style="color:#FF5733;">chanting</span>), aur pitri-tarpan (<span style="color:#FF5733;">ancestor offering</span>) karte the. Kai grihastha (<span style="color:#FF5733;">householders</span>) apni patniyon ke saath yoga karte the. Sach mein, wo ashram Brahma ke lok (<span style="color:#FF5733;">abode</span>) jaisa lagta tha. Vishvamitra ne jab use dekha, unka man khushi aur adbhut (<span style="color:#FF5733;">wonder</span>) se bhar gaya.”
        """
        create_image_text_layout("attached_assets/chapter1/1.51.2.jpg", text3, layout="side", image_position="right")

    # Chapter52
    with st.expander("Chapter 1.52 - King Vishvamitra visits Sage Vasishtha"):

        text1 = """
Ek din, jab Raja Vishvamitra ne Rishi Vasishtha ke ashram (<span style="color:#FF5733;">hermitage</span>) ko dekha, toh unka dil khushi se bhar gaya. Unhone namrata (<span style="color:#FF5733;">humility</span>) se Rishi ko pranam (<span style="color:#FF5733;">bow</span>) kiya. Rishi Vasishtha ne unka pyaar se swagat kiya aur bola, “Raja Vishvamitra, aap baithiye.” Phir unhone unhe ashram mein mile fal (<span style="color:#FF5733;">fruits</span>) aur jad (<span style="color:#FF5733;">roots</span>) khilaye.

Raja Vishvamitra ne bhi bade vinamra (<span style="color:#FF5733;">humble</span>) tareeke se unse poocha, “Hey Muni, sab theek hai na? Aapka yagna (<span style="color:#FF5733;">sacrifice</span>), tapasya (<span style="color:#FF5733;">meditation</span>) aur shishya (<span style="color:#FF5733;">disciples</span>) sab sukh se hain?”


        """
        create_image_text_layout("attached_assets/chapter1/1.52.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Rishi Vasishtha muskura kar bole, “Sab achha hai, Raja! Batao, tumhara rajya (<span style="color:#FF5733;">kingdom</span>) kaisa chal raha hai? Praja (<span style="color:#FF5733;">people</span>) khush hain? Tum apne sipahiyon (<span style="color:#FF5733;">soldiers</span>) aur mitron (<span style="color:#FF5733;">friends</span>) ka dhyan rakhte ho na? Tumhara khazana (<span style="color:#FF5733;">treasury</span>) aur parivar sab theek hain?” Raja Vishvamitra bole, “Sab bhagwan ke kripa (<span style="color:#FF5733;">blessing</span>) se theek hai, Maharishi.”

Dono kuch der tak purani baatein (<span style="color:#FF5733;">ancient stories</span>) karte rahe, aur apas mein bahut khush hue. Thodi der baad, Rishi Vasishtha bole, “Hey Raja, tum apni sena (<span style="color:#FF5733;">army</span>) ke saath aaye ho. Mujhe tumhe aur tumhare logon ko bhoj (<span style="color:#FF5733;">feast</span>) dena hai. Kripya mera nimantran (<span style="color:#FF5733;">invitation</span>) swikaar karo.” Raja Vishvamitra bole, “Maharishi, aapke madhur (<span style="color:#FF5733;">sweet</span>) shabd hi mere liye sabse bada satkar (<span style="color:#FF5733;">honour</span>) hain. Aapne mujhe fal aur pavitra (<span style="color:#FF5733;">pure</span>) jal (<span style="color:#FF5733;">water</span>) diya, ye mere liye kafi hai.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """

Par Rishi Vasishtha ne kaha, “Nahi Raja, mehmaan (<span style="color:#FF5733;">guest</span>) ke roop mein tumhara bhojan karana mera kartavya (<span style="color:#FF5733;">duty</span>) hai.” Tab Raja Vishvamitra ne kaha, “Theek hai Maharishi, jaise aap chahein.”

Phir Rishi Vasishtha ne apni chamatkari (<span style="color:#FF5733;">magical</span>) gai (<span style="color:#FF5733;">cow</span>) Kamadhenu, jise Shabala bhi kehte hain, ko bulaya. Unhone kaha,
“Hey Shabale, meri baat suno. Raja Vishvamitra aur unki sena ko bhojan karana hai. Tum to ichchha-purti (<span style="color:#FF5733;">wish-fulfilling</span>) gai ho, tum sab kuch kar sakti ho. Isliye unke liye turant swadisht (<span style="color:#FF5733;">tasty</span>) bhojan banao — har prakar ke, jo khaya, piya, chata aur choosa ja sakta hai!”
        """
        create_image_text_layout("attached_assets/chapter1/1.52.2.jpg", text3, layout="side", image_position="right")

    # Chapter53
    with st.expander("Chapter 1.53 - Vishvamitra wants Shabala"):

        text1 = """
Shabala, jo ki ek ichchha-purti (<span style="color:#FF5733;">wish-fulfilling</span>) gai (<span style="color:#FF5733;">cow</span>) thi, Shri Vasishtha ke hukum (<span style="color:#FF5733;">instruction</span>) ke mutabik sabko bhojan (<span style="color:#FF5733;">food</span>) deti thi. Ganne (<span style="color:#FF5733;">sugar cane</span>), alag-alag prakar ke mithai (<span style="color:#FF5733;">sweets</span>), shahad (<span style="color:#FF5733;">honey</span>), peesa hua jau (<span style="color:#FF5733;">crushed barley</span>), madira (<span style="color:#FF5733;">wine</span>) aur anya drinks, garam chawal (<span style="color:#FF5733;">hot rice</span>) pahaadon jitna, doodh (<span style="color:#FF5733;">milk</span>), sabzi (<span style="color:#FF5733;">curry</span>) aur chhe ras (<span style="color:#FF5733;">six tastes</span>) wale bhojan, saath hi jaggery ki mithai, sabko milte aur sab khush (<span style="color:#FF5733;">delighted</span>) ho gaye. Sabne Rishi Vasishtha ke atithya (<span style="color:#FF5733;">hospitality</span>) ka poora anand liya.

Raja Vishvamitra apne pariwar ke purohit (<span style="color:#FF5733;">family priests</span>), mantri (<span style="color:#FF5733;">ministers</span>) aur sevak (<span style="color:#FF5733;">attendants</span>) ke saath bhojan karte hue bahut prasanna (<span style="color:#FF5733;">pleased</span>) hue.

        """
        create_image_text_layout("attached_assets/chapter1/1.53.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Jab sabko bhojan mil gaya, Raja ne Shri Vasishtha se kaha,
“O Maharishi, aapne mujhe rajsi (<span style="color:#FF5733;">royal</span>) bhojan diya, ab meri baat suno. Hey Mahaan Rishi, mujhe Shabala do. Main tumhe 1 lakh (<span style="color:#FF5733;">hundred thousand</span>) behad acchi gaayen (<span style="color:#FF5733;">cows</span>) de dunga. Shabala ek ratna (<span style="color:#FF5733;">jewel</span>) hai aur raja ko ratna milna chahiye—prakritik niyam (<span style="color:#FF5733;">natural law</span>) ke mutabik, yeh mere adhikar (<span style="color:#FF5733;">right</span>) mein hai.”

Shri Vasishtha ne vinamrata (<span style="color:#FF5733;">humility</span>) se jawab diya,
“O Raja, main Shabala ko dene ke liye taiyaar nahi hoon, chahe aap mujhe 1 crore (<span style="color:#FF5733;">ten million</span>) gaayen kyon na dein. Chahe aap pahaad (<span style="color:#FF5733;">mountains</span>) bhar chandi (<span style="color:#FF5733;">silver</span>) bhi dein, main Shabala nahi dunga, kyunki woh mera ashram ki rakshak (<span style="color:#FF5733;">protector</span>) hai.

“Jaise ek dharmic (<span style="color:#FF5733;">righteous</span>) vyakti apni izzat (<span style="color:#FF5733;">good name</span>) ka dhyan rakhta hai, waise hi main Shabala ka dhyan rakhta hoon. Wo mujhe devas (<span style="color:#FF5733;">gods</span>), pitris (<span style="color:#FF5733;">ancestors</span>) aur anya jeevon (<span style="color:#FF5733;">beings</span>) ko santusht (<span style="color:#FF5733;">satisfy</span>) karne mein madad karti hai. Mera pavitra (<span style="color:#FF5733;">sacred</span>) yagna (<span style="color:#FF5733;">sacrifice</span>) aur anya Vedic kriya (<span style="color:#FF5733;">rituals</span>), saath hi gyaan (<span style="color:#FF5733;">learning</span>) ke kaam, Shabala par nirbhar (<span style="color:#FF5733;">depend</span>) karte hain. Isliye main use kabhi nahi dunga. Shabala meri sabse badi sampatti (<span style="color:#FF5733;">wealth</span>) aur jeevan hai.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """

Lekin Shri Vasishtha ke ye shabd (<span style="color:#FF5733;">words</span>) Raja ki iccha ko aur badha (<span style="color:#FF5733;">increase</span>) diye. Raja, bade jazbe (<span style="color:#FF5733;">emotion</span>) mein, bola:
“O Mahaan Muni, main aapko 14,000 hathi (<span style="color:#FF5733;">elephants</span>) sunehre (<span style="color:#FF5733;">golden</span>) alankaar (<span style="color:#FF5733;">trappings</span>) ke saath, 108 sunehre (<span style="color:#FF5733;">gold</span>) rath (<span style="color:#FF5733;">chariots</span>), har rath mein 4 safed ghode (<span style="color:#FF5733;">white horses</span>), 11,000 ghode (<span style="color:#FF5733;">horses</span>) sunehre laghu (<span style="color:#FF5733;">golden harness</span>) ke saath aur 1 crore (<span style="color:#FF5733;">ten million</span>) gaayen, har rang ki, yuva (<span style="color:#FF5733;">young</span>) aur swasth (<span style="color:#FF5733;">healthy</span>), de dunga. Hey Rishi, bas mujhe Shabala do, main jitna chaaho sona (<span style="color:#FF5733;">gold</span>) bhi dunga. Kripya Shabala do aur mere uphaar (<span style="color:#FF5733;">gifts</span>) swikaar karo.”

Phir Rishi Vasishtha ne sachchai se kaha,
“O Raja, kisi bhi haalat (<span style="color:#FF5733;">condition</span>) mein main Shabala ko nahi dunga. Wo meri ratna (<span style="color:#FF5733;">jewel</span>) hai, meri sampatti (<span style="color:#FF5733;">wealth</span>) hai, meri jeevan shakti (<span style="color:#FF5733;">life force</span>) hai, aur yeh mujhe yagna aur anya zarurat (<span style="color:#FF5733;">needs</span>) poora karne mein madad karti hai. Isliye main Shabala kabhi nahi dunga.”
        """
        create_image_text_layout("attached_assets/chapter1/1.53.2.jpg", text3, layout="side", image_position="right")

    # Chapter54
    with st.expander("Chapter 1.54 - Vishvamitra tries to take Shabala by force"):

        text1 = """
O Rama, jaante hue ki Shri Vasishtha apni ichha se Shabala ko nahi denge, Raja Vishvamitra ne socha ki use zabardasti (<span style="color:#FF5733;">by force</span>) le jaaya jaye. O Raghava, jab Shabala ko zabardasti le jaaya ja raha tha, udaas (<span style="color:#FF5733;">sad</span>) aur pareshan (<span style="color:#FF5733;">distressed</span>), wo soch rahi thi:
“Hey, Vasishtha ne mujhe kyun chhod diya? Maine unka kya bura kiya? Raja ke sevak (<span style="color:#FF5733;">servants</span>) mujhe hermitage se kyun le ja rahe hain? Main to nirdosh (<span style="color:#FF5733;">innocent</span>) aur dayalu (<span style="color:#FF5733;">docile</span>) hoon, Mahatma Vasishtha mujhe priya (<span style="color:#FF5733;">dear</span>) hain; maine kya paap (<span style="color:#FF5733;">fault</span>) kiya jo unhone mujhe chhod diya?”

        """
        create_image_text_layout("attached_assets/chapter1/1.54.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Baar-baar sigh karte hue, Shabala, raja ke sevakon ke haathon se chutkar, tezi se bhaagi aur apna sir (<span style="color:#FF5733;">head</span>) pavitra Rishi ke paon (<span style="color:#FF5733;">feet</span>) par rakh diya. Shri Vasishtha ke saamne khadi, aansu (<span style="color:#FF5733;">tears</span>) bahate hue, zor se cheekhti (<span style="color:#FF5733;">crying</span>) boli:
“O Lord, O Brahma ke putra, kya aapne sach mein mujhe chhod diya? Raja ke sevak mujhe aapke saamne se zabardasti kyon le ja rahe hain?”

Dukhi Shabala ko dekh kar, Shri Vasishtha ne kaha jaise apni behen se baat karte,
“O Shabala, yeh meri ichha (<span style="color:#FF5733;">will</span>) se nahi ho raha, na hi tumne mujhe kuch bura kiya. Raja apne lalach (<span style="color:#FF5733;">desire</span>) mein mujhe tumse le ja raha hai. Mere paas tumhe bachane ki shakti (<span style="color:#FF5733;">power</span>) nahi hai. Raja yoddha (<span style="color:#FF5733;">warrior</span>) hai aur uska saath ek bada sena (<span style="color:#FF5733;">army</span>) hai, ghode (<span style="color:#FF5733;">horses</span>), hathi (<span style="color:#FF5733;">elephants</span>) aur rath (<span style="color:#FF5733;">chariots</span>) ke saath; sach mein wo mujhse zyada shaktishaali (<span style="color:#FF5733;">mighty</span>) hai.”

Shabala, jo tark (<span style="color:#FF5733;">argument</span>) mein nipun (<span style="color:#FF5733;">skilled</span>) thi, Shri Vasishtha ki baatein sun kar boli,
“O Mahaan Rishi, yoddha ki shakti (<span style="color:#FF5733;">power</span>) ek pavitra muni (<span style="color:#FF5733;">holy sage</span>) ke saamne kuch bhi nahi hai. O Mahaan Lord, ek muni ki shakti divya (<span style="color:#FF5733;">divine</span>) hai aur dhyan aur tapasya (<span style="color:#FF5733;">spiritual practices</span>) par adharit (<span style="color:#FF5733;">based</span>) hai, isliye woh seema rahit (<span style="color:#FF5733;">limitless</span>) hai; aap, O Lord, Vishvamitra se hazaar guna (<span style="color:#FF5733;">immeasurably</span>) zyada shaktishaali ho. Raja ki shakti to bahut hai, par wo aapke barabar nahi aa sakta. O Lord, apni shakti se mujhe is dusht (<span style="color:#FF5733;">wicked</span>) ke garv (<span style="color:#FF5733;">pride</span>) aur shakti ko nasht (<span style="color:#FF5733;">destroy</span>) karne do. Shri Vasishtha ne kaha: “Thik hai! Apni adhyatmik (<span style="color:#FF5733;">spiritual</span>) shakti se ek sena (<span style="color:#FF5733;">army</span>) banao jo raja ki sena ko hara de.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """

Bhalaan (lowing) karte hue, Shabala ne turant (<span style="color:#FF5733;">instantly</span>) apni shakti se sauyon videshi (<span style="color:#FF5733;">foreign</span>) sainik (<span style="color:#FF5733;">soldiers</span>) bana diye, jo Raja Vishvamitra ki sena ko nasht (<span style="color:#FF5733;">destroy</span>) karne lage. Apni sena ko haarte dekh, Raja Vishvamitra gusse mein (<span style="color:#FF5733;">angry</span>) chadhkar apne rath (<span style="color:#FF5733;">chariot</span>) par chadh gaya aur haathiyar (<span style="color:#FF5733;">weapons</span>) se hazaaron logon ko maara.

Shabala ne, apni banayi hui sena ko nasht dekh kar, ajeeb prani (<span style="color:#FF5733;">strange beings</span>) shakas banaye, itni sankhya mein ki poori dharti (<span style="color:#FF5733;">earth</span>) bhar gayi. Ve bahut veer (<span style="color:#FF5733;">valorous</span>) the, unki twacha (<span style="color:#FF5733;">skins</span>) sone jaise chamak rahe the, peele (<span style="color:#FF5733;">yellow</span>) kavach (<span style="color:#FF5733;">armor</span>) pehne, talwar (<span style="color:#FF5733;">scimitar</span>) aur gada (<span style="color:#FF5733;">mace</span>) le kar Raja ki sena ko aag ki tarah nasht karne lage. Phir mahaan Vishvamitra ne yogic haathiyar (<span style="color:#FF5733;">weapons</span>) ka upayog (<span style="color:#FF5733;">use</span>) karke Shabala ki sena mein afra-tafri (<span style="color:#FF5733;">disorder</span>) paida ki.
        """
        create_image_text_layout("attached_assets/chapter1/1.54.2.jpg", text3, layout="side", image_position="right")

    # Chapter55
    with st.expander("Chapter 1.55 - Shabala makes an army and defeats Vishvamitra’s men"):

        text1 = """
Jab mahaan yoddha (<span style="color:#FF5733;">warriors</span>) gir rahe the, Vishvamitra ki sena ke haathiyar (<span style="color:#FF5733;">weapons</span>) se, Shri Vasishtha ne Shabala se kaha:
“O Shabala, apni Yoga (<span style="color:#FF5733;">spiritual power</span>) se aur yoddha banao (<span style="color:#FF5733;">create warriors</span>).”

Shabala ne zor se bhalaan (low) kiya aur apne pair (<span style="color:#FF5733;">feet</span>) aur udders se shaktishaali sainik (<span style="color:#FF5733;">well-armed soldiers</span>) bana diye, aur apne baalon (<span style="color:#FF5733;">hair</span>) aur jaanghon (<span style="color:#FF5733;">thighs</span>) se adbhut yoddha Harita aur Kirata janme. Inke dwara, Vishvamitra ki poori sena – hathi (<span style="color:#FF5733;">elephants</span>), ghode (<span style="color:#FF5733;">horses</span>) aur rath (<span style="color:#FF5733;">chariots</span>) – turant nasht (<span style="color:#FF5733;">destroyed</span>) ho gayi.

Apni poori sena ko Shri Vasishtha ki shakti se nasht dekh kar, Raja Vishvamitra ke sau putra (<span style="color:#FF5733;">sons</span>), shaktishaali aur vichaar se chalne wale (<span style="color:#FF5733;">thought-propelled</span>) haathiyar lekar, gusse mein Vasishtha ki taraf bhaage. Shri Vasishtha ne sirf “H’m!” ki dhvani (<span style="color:#FF5733;">sound</span>) di aur ve sab turant khatam ho gaye. Mahaan Rishi Vasishtha ke dwara, peshwari sena (<span style="color:#FF5733;">infantry</span>), ghode aur rath, saath hi Vishvamitra ke putra, turant raakh (<span style="color:#FF5733;">ashes</span>) ho gaye.

        """
        create_image_text_layout("attached_assets/chapter1/1.55.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Phir mahaan Raja Vishvamitra, jinki sena aur putra nasht ho chuke the, sharm (<span style="color:#FF5733;">shame</span>) aur chinta (<span style="color:#FF5733;">dismay</span>) se bhare ho gaye. Apni mahima (<span style="color:#FF5733;">glory</span>) se vanchit (<span style="color:#FF5733;">deprived</span>), wo bina lehron wale samundar (<span style="color:#FF5733;">waveless ocean</span>) ya bina daanton wale saap (<span style="color:#FF5733;">snake bereft of fangs</span>) jaise dikh rahe the. Jaise pankh (<span style="color:#FF5733;">wings</span>) bina pakshi (<span style="color:#FF5733;">bird</span>), unka atma-vishwas (<span style="color:#FF5733;">confidence</span>) toot gaya, garv (<span style="color:#FF5733;">pride</span>) nimna (<span style="color:#FF5733;">humbled</span>) ho gaya, aur wo chinta (<span style="color:#FF5733;">anxiety</span>) se bhare ho gaye. Apna rajya (<span style="color:#FF5733;">kingdom</span>) keval apne ek shesh (<span style="color:#FF5733;">remaining</span>) putra ko samarpit (<span style="color:#FF5733;">bestowed</span>) karke, van me tapasya (<span style="color:#FF5733;">asceticism</span>) karne chale gaye.

Kuch samay baad, unhe Shri Mahadeva, dayaalu (<span style="color:#FF5733;">magnanimous</span>) vardaan (<span style="color:#FF5733;">boon</span>) dene wale, ka ashirvad (<span style="color:#FF5733;">favour</span>) mila. Mahadeva ne Vishvamitra se poocha:
“O Raja, aap tapasya kyon kar rahe ho? Aapki ichha (<span style="color:#FF5733;">desire</span>) kya hai? Main jo chaho tumhe de dunga.” Shri Vishvamitra ne pranam (<span style="color:#FF5733;">obeisance</span>) karte hue kaha:
“O Mahaan Bhagwan, agar aap mujhe ashirvad dete ho, to Upanishad aur anya shiksha (<span style="color:#FF5733;">learning</span>) sikhaiye. Archery (<span style="color:#FF5733;">dhanurvidya</span>) aur sabhi haathiyar (<span style="color:#FF5733;">weapons</span>) ka gyaan do, jo danava, yaksha, asura aur anya prani (<span style="color:#FF5733;">beings</span>) jaante hain, ve mujhe prapt ho.” Mahadeva ne kaha:
“Thik hai” aur apne ghar (<span style="color:#FF5733;">abode</span>) ko wapas chale gaye.

Raja Vishvamitra, Mahadeva se haathiyar (<span style="color:#FF5733;">weapons</span>) prapt kar, chaand ke poore (<span style="color:#FF5733;">full moon</span>) samay ke samundar (<span style="color:#FF5733;">sea</span>) jaise khush ho gaye. Ab unhone Vasishtha ko jeetne (<span style="color:#FF5733;">subdue</span>) ka sankalp (<span style="color:#FF5733;">resolve</span>) kar liya aur usse apna bandi (<span style="color:#FF5733;">captive</span>) samjha. Apne hermitage jaate hue, unhone apne mahan haathiyar (<span style="color:#FF5733;">great weapons</span>) barish (<span style="color:#FF5733;">rain</span>) ki tarah chhode, Tapovan ke van (<span style="color:#FF5733;">forest</span>) ko aag (<span style="color:#FF5733;">blaze</span>) lag gayi. In bhayankar (<span style="color:#FF5733;">dreadful</span>) haathiyar se, sab Rishi (<span style="color:#FF5733;">sages</span>) chaaron taraf bhag gaye; Vasishtha ke shishya (<span style="color:#FF5733;">disciples</span>) aur anek pakshi (<span style="color:#FF5733;">birds</span>) aur prani (<span style="color:#FF5733;">beasts</span>) bhi bhag gaye. Shri Vasishtha ka hermitage suna (<span style="color:#FF5733;">deserted</span>) ho gaya aur gahra (<span style="color:#FF5733;">deep</span>) sannata (<span style="color:#FF5733;">silence</span>) chha gaya, jaise banjar (<span style="color:#FF5733;">barren</span>) khet ho.

        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Shri Vasishtha baar-baar bolte:
“Darro mat, darro mat, main Vishvamitra ko nasht (<span style="color:#FF5733;">destroy</span>) kar dunga jaise surya (<span style="color:#FF5733;">sun</span>) subah ki dhund (<span style="color:#FF5733;">morning mist</span>) mita deta hai.” Phir mahaan Rishi Vasishtha, jo silent prayer (<span style="color:#FF5733;">japa</span>) mein pratham (<span style="color:#FF5733;">foremost</span>) hain, Vishvamitra se gusse mein bole:
“Tumne mera purana aur shubh (<span style="color:#FF5733;">auspicious</span>) hermitage nasht kar diya, O Dusht (<span style="color:#FF5733;">wicked</span>) aur bhramit (<span style="color:#FF5733;">deluded</span>) vyakti, tum khud nasht ho jao.” Apni danda (<span style="color:#FF5733;">staff</span>), jo Yama ke danda jaise (<span style="color:#FF5733;">rod of Yama</span>) thi, utha kar, ve nangi aag (<span style="color:#FF5733;">naked flame</span>) jaise aage bade.
        """
        create_image_text_layout("attached_assets/chapter1/1.55.2.jpg", text3, layout="side", image_position="right")
