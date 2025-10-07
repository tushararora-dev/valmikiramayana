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

Is yajna ke dwara, Raja Dasaratha ke chaar putra honge, jo apaar veerta (<span style="color:#FF5733;">valour</span>) wale honge aur poore vishwa me prasiddh honge, aur unke vansh ki mahima ko badhaenge.’ Sanatkumara ne ye katha Satya-Yuga ke prarambh me sunayi.
        """
        create_image_text_layout("attached_assets/chapter1/1.11.1.jpg", text1, layout="side", image_position="left")


        text2 = """
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

Beech-beech me pundit (<span style="color:#FF5733;">scholars</span>) bhi gyaan-vivad karte rahe. Yajna ke sthaan par 18 khambhe (<span style="color:#FF5733;">pillars</span>) lagaye gaye, har ek alag lakdi ka, sone se sajaya gaya aur phool aur chandan se sajaaya gaya. Fire pits aur yajna ke samagriyon ka dhyaan brahmins aur masons ne rakha.

        """
        create_image_text_layout("attached_assets/chapter1/1.14.1.jpg", text1, layout="side", image_position="left")


        text2 = """
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


    create_image_text_layout("attached_assets/chapter1/chapter11.jpg", layout="full")

