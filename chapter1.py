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
    with st.expander("Chapter 1.1 – Shri Narada Relates the Story of Rama"):
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
    with st.expander("Chapter 1.2 – Sage Valmiki Creates the Metrical Form for the Story"):

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
    with st.expander("Chapter 1.3 – The Deeds of Rama Described in the Sacred Poem"):

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
    with st.expander("Chapter 1.4 – Shri Rama’s Sons Chant the Poem"):

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
    with st.expander("Chapter 1.5 – King Dasaratha’s Kingdom and Capital"):

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




    create_image_text_layout("attached_assets/chapter1/chapter11.jpg", layout="full")

