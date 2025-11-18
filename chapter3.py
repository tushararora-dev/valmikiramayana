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


    # chapter1
    with st.expander("Chapter 3.1 – Rama is warmly welcomed by the sages in Dandaka Forest"):
        text1 = """
    Rama, Lakshman aur Sita jab Dandaka Forest ke andar gaye, to unhone ek sundar ashram dekha. Yahan bahut saare muni (sage) rehte the. Unke huts ke aas-paas kusha grass (holy grass), phal, jale hue sacred fire aur pooja ki cheezen rakhi hui thi. Poora jagah ek shanti wali roshni se chamak raha tha — bilkul jaise dopahar ka tezz suraj aankhon ko chubhta hai.

    Ashram ke paas hiran, bahut saari birds aur kabhi-kabhi apsara (celestial dancers) bhi dikhti thi. Bade bade vriksh phalon se bhare hue the, jaise prakriti khud un muniyon ki seva kar rahi ho.

    Rama ne apna dhanush neeche rakha aur ashram ke andar chale gaye. Sages ne unhe door se hi dekh liya, aur bade prem se unka swagat karne aa gaye. Rama ki shant soorat, unka tejas (radiance) aur unki vinamr chal sabko bahut achchi lagi. Lakshman aur Sita ko dekhkar bhi sab muniyon ke chehre par khushi aa gayi.
        """
        create_image_text_layout("attached_assets/chapter3/3.1.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
    Sages ne Rama ko ek patton se bani chhoti si hut mein bulaya. Unhone unko haath-pair dho ne ke liye paani diya, phal, phool, jad-booti sab laa kar rakh diye. Unka swagat bilkul parampara ke hisaab se kiya gaya.

    Phir sare pious sages haath jodkar bole:

    “Raghava, raja hamesha apne logon ka rakshak hota hai. Chahe hum nagar mein rahein ya jungle mein, hum aapke hi praja hain. Humein raksha chahiye, jaise maa apne bachche ko bachati hai. Aap humari dharm-practise ki hifazat kijiye.”

    Rama ne unka samman se suna, aur sages ne phir phal-phool aur apne ashram ka sab kuch unke charan mein rakh diya. Poora ashram Rama ke aane se aur bhi pavitra lagne laga.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter2
    with st.expander("Chapter 3.2 – The demon Viradha kidnaps Sita"):
        text1 = """
    Subah hote hi Rama ne sages ko pranam kiya aur Lakshman ke saath jungle ke aur andar chale gaye. Yahaan har tarah ke hiran, bhaloo aur baagh rehte the. Par jungle ka kuchh hissa ajeeb laga — raste tootey pade the, paani itna chamak raha tha ki aankhon ko dukh ho, aur birds ki awaaz bilkul nahi aa rahi thi.
    (Yeh sab Viradha naam ke rakshas ke dar ki wajah se tha.)

    Jungle ke beech, Rama–Lakshman–Sita ne ek bahut bada aur darawna rakshas dekha — Viradha.
    Woh pahad jaisa bada tha, uski aankhen andar dhansi hui, muh bahut bada, aur poora shareer khoon se bhara hua tha. Woh baagh ki khal pehna tha aur uske spear par sher, bagh, deer aur ek hathi ka sir tak latak raha tha. Usse dekhkar lagta tha jaise mrityu (death) hi saamne aa gaya ho.
        """
        create_image_text_layout("attached_assets/chapter3/3.2.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
    Viradha ne tezz garaj ke saath un teenon ko dekha aur turant un par toot pada. Dharati tak hilne lagi. Phir usne Sita ko zor se apni baahon mein uthaya aur bhaagne laga.
    Woh chillaya:
    “Main hoon Viradha, is jungle ka rakshas! Tum ascetic (one who lives simply) log ka yahan kya kaam? Yeh sundar nari meri patni banegi, aur main tum dono ka khoon pee jaaunga!”

    Sita, Viradha ki buri aur ghamandi baaton se dar gayi aur hawa mein hilti hui talaash (trembling) karne lagi — bilkul us tarah jaise hawa mein hilta hua palm tree.

    Rama ne Sita ko le jaate hue dekha, to unka chehra peela pad gaya. Unhone dukh se Lakshman se kaha:
    “Lakshman! Dekho Sita ko! Janak ji ki beti, itni pyaari aur sharif, Viradha ki baahon mein phansi hui!
    Yeh sab Kaikeyi ki wajah se hua. Usne sirf mujhe vanvaas hi nahi diya, balki aaj yeh dukh bhi dekhne ko mila. Mere liye yeh dard meri pita ki mrityu ya rajya khone se bhi bada hai!”

    Lakshman ki aankhon se aansu behne lage. Ghusse se woh sarp (snake) ki tarah hiss kar utha.
    Woh bola:
    “Bhaiya, aap kyun dukh kar rahe ho? Main hoon na! Aaj yeh Viradha mere teer se mar jayega. Jaisa Indra apni vajra (thunder bolt) se pahaad tod deta hai, waise hi main is rakshas ka hraday (heart) cheed dunga! Aaj ki raat yeh dharti is rakshas ka khoon peeyegi!”

    Lakshman ne dhanush taana — aur yudh ke liye dono bhai ready ho gaye.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter3
    with st.expander("Chapter 3.3 – Rama and Lakshmana fight Viradha"):
        text1 = """
    Viradha ne phir garaj kar poora jungle hila diya:
    “Tum kaun ho? Kahan ja rahe ho? Jawab do!”

    Rama ne shant par majboot awaaz mein kaha:
    “Hum Ikshvaku vansh (royal lineage) ke warriors hain. Jungle mein tapasya (penance) ke liye aaye hain. Par tum kaun ho, jo yahan sabko dara rahe ho?”

    Viradha ne garv se jawab diya:
    “Mera naam Viradha hai. Main Java ka beta hoon. Maine Brahma ko tapasya karke ek boon (divine blessing) paaya hai. Ab kisi bhi shastr (weapon) se mujhe maarna namumkin hai.”

    Phir woh garaj kar bola:
    “Yeh sundar स्त्री mujhe de do! Tum dono yahin se bhaag jao, tabhi bach paoge!”
        """
        create_image_text_layout("attached_assets/chapter3/3.3.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
    Rama ka chehra gusse se laal ho gaya.
    Woh bola:
    “Dusht (wicked) rakshas! Tumne maut ko khud bula liya hai. Ruko — main tumhe aaj hi gira dunga!”

    Rama ne teer laga kar do tez arrows Viradha par chala diye. Phir ek saath saat golden-tipped arrows asmaan ki speed se chhode.
    Teer Viradha ke shareer ko cheed gaye aur khoon se laal ho kar zameen par gire.

    Viradha dard se dahada, usne Sita ko chhod diya aur apna bada sa spear (long weapon) ghuma kar Rama–Lakshman par hamla kar diya. Woh itna darawna lag raha tha jaise mrityu (death) khud aa raha ho.

    Dono bhaiyon ne teeron ki baarish kar di, par Viradha hasne laga. Usne apni boon ke bal par teer nigal liye aur muh se wapas bahar phek diye.

    Phir woh phir se spear lekar bhaaga, par Rama ne do teeron se uss spear ko beech se kaat diya. Bada sa weapon bijli se phati chattan ki tarah zameen par gir gaya.

    Ab Rama–Lakshman ne apni talwarein nikaali aur do kaale saap (serpent) ki tarah us rakshas par toot pade. Lekin Viradha bhi bahut shaktishaali tha; usne apne bade bade mukke se dono bhaiyon ko peechhe dhakel diya.

    Fir Viradha ne donon ko zameen se uthane ki koshish ki. Rama ne turant Lakshman se kaha:
    “Lakshman, isse humein uthane do. Yeh wahi raasta ja raha hai jahan humein jaana hai.”

    Viradha, apni shakti par garv karta hua, dono bhaiyon ko apne kandhon par bitha liya — jaise woh sirf do chhote ladke ho. Wo zor se garajta hua jungle ke andar badhta gaya.

    Jungle mein har tarah ke ped, pakshi, lomdi, jangli janwar aur saanp the. Viradha un sab ke beech ek kaale badal (dark cloud) ki tarah dikh raha tha — bhayanak aur vishal.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter4
    with st.expander("Chapter 3.4 – Rama and Lakshmana defeat and kill Viradha"):
        text1 = """
    Jab Viradha dono bhaiyon ko kandhon par le jaa raha tha, Sita unko door jaate dekh kar rote hue sochne lagi:
    “Rama, jo itne satya-vadi aur daya-lo (kind-hearted) hain, unhe ek rakshas le ja raha hai! Main toh ab bhaloo, baagh ya panther ka shikar ban jaaungi!”

    Dar ke maare Sita ne pukaar kar kaha:
    “Hey rakshas, agar chhodna hi hai toh mujhe le jao, par Rama–Lakshman ko mat le jao!”

    Sita ki awaaz sunte hi Rama aur Lakshman ka gussa aur badh gaya. Dono ne ek saath Viradha par hamla kar diya.
    Lakshman ne uska baaya haath tod diya aur Rama ne daaya haath. Viradha ek bade kaale badal (dark cloud) ki tarah dharati par dhad se gir gaya — jaise bijli se peeta hua pahad toot kar girta hai.

    Dono bhaiyon ne usko mukko aur laaton se mar kar phir zameen par pheka. Talwaron se kaatne ke baad, teeron se ghail karne ke baad bhi Viradha nahi mara.
        """
        create_image_text_layout("attached_assets/chapter3/3.4.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
    Rama ne samajh liya ki weapons (shastr) Viradha ko nahi maar sakte — kyunki woh ek boon (divine blessing) se surakshit tha.
    Rama ne Lakshman se kaha:
    “Is rakshas ko humein ek gaddhe (pit) mein dafan karna hoga. Lakshman, ek bada gaddha kholo.”

    Jab Rama Viradha ke gale par pair rakhe khade the, tab Viradha ne dard se par namr (humble) awaaz mein kaha:
    “Hey Rama, mujhe maaf karo. Main tumhe pehchaan nahi paaya. Main asal mein Gandharva (celestial musician) Tumburu hoon. Ek shraap (curse) ki wajah se main rakshas bana. Kuvera ne kaha tha ki jab Rama mujhe hara dega, tab main apne asli swaroop mein vaapas devlok (heavenly realm) jaa sakunga. Aapne mujhe mukti de di.”

    Viradha ne phir unhe bataya:
    “Thoda aage, kareeb chaar-dedh mile door, Rishi Sharabhanga (great sage) rehte hain. Unse zaroor milna.
    Aur mujhe gaddhe mein dafan kar do — shraapit rakshason ka yeh hi niyam hota hai.”

    Itna kehkar Viradha apne sharir ko chhod kar devlok ko chala gaya — ek prakash ki dhaar (beam of light) ki tarah.

    Rama ne phir kaha:
    “Lakshman, ek bada gaddha kholo. Rakshas jaise bade jaanwar ko isi tarah dafan kiya jaata hai.”

    Lakshman ne turant kudali uthai aur ek bada gaddha khod diya. Dono ne milkar Viradha ka shareer usme gira diya. Girte waqt Viradha ne bhayanak cheekh maari, aur poora jungle goonj utha.

    Kyuki unhe pata tha ki weapons kaam nahi karenge, Rama–Lakshman ne apni buddhi (intelligence) se hi is rakshas ka ant kar diya.

    Viradha ko dafan karne ke baad, dono bhai chain ki saans lene lage.
    Jungle unke aas-paas shant lagne laga — jaise aasman mein suraj aur chaand ek saath chamak rahe ho.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter5
    with st.expander("Chapter 3.5 – Rama meets the sage Sharabhanga"):
        text1 = """
    Viradha ko haraane ke baad, Rama ne Sita ko gale lagakar sambhala. Phir Lakshman se bole:
    “Yeh jungle bahut khatarnak hai. Chalo, jaldi se Rishi Sharabhanga (great sage of renunciation) ke ashram chalte hain.”

    Rama, Sita aur Lakshman Sharabhanga ji ke hermitage ki taraf chal diye. Wahan pahunchkar unhone ek adbhut drishya (marvelous sight) dekha.

    Aasmaan mein Indra (King of Gods) ek chamakdar rath par baitha tha. Uske kapde bijli ke jaise chamak rahe the. Uske piche devta, gandharva (celestial musicians) aur mahan rishis unka swaagat kar rahe the.
    Rath ke ghode dhoodhiya (milky-white) rang ke the, aur rath suraj ki tarah chamak raha tha. Do apsarayein (celestial dancers) yak-puchchh ke pankhe hilate hue Indra ko thanda hava kar rahi thi.
        """
        create_image_text_layout("attached_assets/chapter3/3.5.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
    Rama ne Lakshman se kaha:
    “Lakshman, dekh! Yeh Indra ka rath lag raha hai. Jo yuva warriors unke aas-paas khade hain, woh devtaon jaise sundar aur shaktishaali hain. Main dekh kar maanta hoon ki yeh koi mahaan dev yoddha hi hoga.”

    Rama thoda aage badhe. Par Indra ne Sharabhanga se kaha:
    “Rama aa raha hai. Mujhe ab jaana hoga. Jab Rama apna kaarya poora kar lega, tab main usse dobara milunga. Uske liye ek bada kaam tayyar hai.”
    Aur Indra apne rath mein baith kar swarg ko laut gaya.

    Rama, Sita aur Lakshman Sharabhanga ji ke paas gaye. Unke charanon ko sparsh karke baith gaye. Rama ne poocha:
    “Indra yahan kisliye aaye the?”

    Sharabhanga ji muskuraye aur bole:
    “Hey Rama, Indra mujhe Brahmaloka (highest heavenly realm) le jaane aaye the. Maine tapasya (penance) se yeh lok paa liya tha. Par main tumhe dekhe bina yahan se jaana nahi chahta tha. Tumse milkar ab main teen upar ke swargon se hota hua Brahmaloka jaaunga.
    Yeh sab sundar lok jo maine tapasya se jeete hain, main tumhe dene ki ichha rakhta hoon, Rama.”

    Rama ne vinamr hokar jawab diya:
    “Rishi ji, main bhi sab lok jeet sakta hoon, par apni pratigya ke karan mujhe yeh vanvaas poora karna hai.”

    Sharabhanga ji bole:
    “Thik hai Rama. Par ab tumhe Rishi Sutikshna (wise sage) ke paas jaana chahiye. Woh tumhe agla raasta batayenge.
    Phoolon se bhari Mandakini nadi ke kinare kinare jao — unka ashram mil jayega.
    Par thoda ruk jao — main apna shareer tyag karne ki tayyari kar raha hoon, jaise saanp apni purani khaal chhod deta hai.”

    Phir Sharabhanga ji ne yagya ki aag jalayi, usme ghee chadhaya, aur mantron ka uchcharan karte hue aag mein pravesh kar gaye.
    Unka vriddh (old) shareer aag mein jal gaya — baal, charbi, haddiyan, sab.

    Aur fir ek tejomay (radiant) aur yuva roop mein, woh aag se upar uthte gaye — bilkul jalti hui laa (flame) ki tarah.
    Swarg ki raahon se guzar kar, woh Brahma ji ke lok mein pahunch gaye.

    Wahan Brahma ji ne unka swaagat kiya:
    “Tumhara swaagat hai, Sharabhanga.”

    Iss tarah Rama aur Lakshman ki Rishi Sharabhanga se pavitra mulaqat poori hui.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter6
    with st.expander("Chapter 3.6 – The sages ask Rama to protect them"):
        text1 = """
Sharabhanga ji ke Brahmaloka jaane ke baad, bahut saare rishi–muni (sages) Rama ke paas aaye. Yeh sab alag-alag tarah ki tapasya (penance) karne wale yogi the—

koi sirf chandni ki roshni par jeeta tha,

koi bas paani ya hawa se jeeta tha,

koi poore saal dhup-mein khada rehta tha,

koi paanch aagon ke beech tapasya karta tha,

koi nange zameen par sota tha,

koi sirf mantr jap (continuous chanting) karta rehta tha.

Yeh sab mahaan sages, jo yoga aur tapasya mein sthir (steady) the, Sharabhanga ke ashram mein ek saath jama hue—sirf Rama se milne ke liye.
        """
        create_image_text_layout("attached_assets/chapter3/3.6.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Unhone prem aur aadar se Rama se kaha:
“Hey Ikshvaku vansh ke Rama, aap hum sage logon ke rakshak ho. Tinke Maharaja jaise ho.
Aap teenon lok (three worlds) mein bahaduri aur dharma ke liye prasiddh ho. Humein kshama karo ki hum aapse apni binti rakhne aaye hain.

Raja apni praja se jo hissa (tax) leta hai, uska farz hota hai unki raksha karna. Jo raja apne logon ko apne bacchon ki tarah bachata hai, woh Brahmaloka tak pahunch sakta hai.

Par hum sages ka haal bahut bura hai, Rama. Rakshas log humein jungle mein mar rahe hain. Pampa Lake, Mandakini nadi aur Chitrakoot ke aaspaas kitne hi tapasvi mare pade hain. Unke shareer yahan bikhre padi hain—kisi ko maar diya, kisi ko kha liya. Hum ab aur bardasht nahi kar sakte.

O Rama! Humari raksha karo. Humare paas duniya mein koi aur sahara nahi hai.”

Rama ne shaant par majboot awaaz mein jawab diya:
“Rishiyon, aap mujhe kyun vinati karte ho? Main toh pehle hi aapka sevak hoon. Main yahaan aapki raksha karne hi aaya hoon. Yeh mera dharm hai aur mere pita ka aadesh bhi.
Main rakshason ka ant karunga. Aap sab mera aur Lakshman ka yuddh dekhoge.”

Rama ki baat sunkar sab rishi khush ho gaye. Unke saath saath Rama aur Lakshman Rishi Sutikshna (a gentle and wise sage) ke ashram ki taraf badhne lage. Aspas chalne wale sab sages Rama ko bada adar aur samman de rahe the.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter7
    with st.expander("Chapter 3.7 – Rama meets Sage Sutikshna"):
        text1 = """
Rama, Lakshman, Sita aur saath mein chal rahe sages bahut door tak chalne ke baad ek sundar parvat ke paas pahunche—jo Meru Parvat (mythical golden mountain) jitna uncha lag raha tha.

Us parvat ke peechhe ek ghana jungle tha, jismein har tarah ke phoolon aur phalon se lade hue ped the. Us jungle ke beech Rama ko ek shant sa ashram dikhai diya—jismein patton ki mala aur bark cloth se sajaavat thi.

Wahin, ek akela kona mein, Rishi Sutikshna (gentle, wise sage) padmasan (lotus posture) mein baithkar tapasya kar rahe the. Unke baal jataon mein bandhe hue the, shareer thoda dhool se dhaka hua tha.
        """
        create_image_text_layout("attached_assets/chapter3/3.7.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Rama ne vinamr awaaz mein kaha:
“Hey maharishi, main Rama hoon. Aapko darshan karne aaya hoon. Kripya mujhe ashish (blessing) dein.”

Rishi Sutikshna ne aankhen kholi, Rama ko dekha aur turant unhe gale laga liya.
Woh bole:
“Swagat hai, Rama! Ab is ashram ko ek sachcha rakshak mil gaya. Main tumhare aane ka intezaar kar raha tha. Isliye main ab tak apna shareer tyag kar swarg nahi gaya. Indra bhi yahan aaye the aur unhone mujhe bataya ki maine apni tapasya se sab lok jeet liye hain.
Par main yeh saari punya (spiritual merit) tumhare liye rakhna chahta hoon — tum, Sita aur Lakshman inka aanand lo.”

Rama ne shant ho kar jawab diya:
“Rishi ji, maine bhi sab lokon ko jeet chuka hota, par mujhe apne pita ji ka aadesh aur apna dharm nibhana hai. Sharabhanga rishi ne bhi kaha tha ki mujhe logon ki bhalai ke liye vanvaas poora karna chahiye.”

Rishi Sutikshna ne prem se kaha:
“Rama, tum chaaho toh is ashram mein reh sakte ho. Yahaan sab rituon mein phal-mool milte hain, hiran ka jhund shanti se aata-jata hai, aur sab sages achche se rehte hain. Yahaan sirf hiran ki sharartein hoti hain — aur koi nuksaan nahi.”

Rama ne apna dhanush uthate hue kaha:
“Rishi ji, yeh mere liye dukh ki baat hogi agar mere teer se in nirdosh (innocent) hiranon ko chot lage. Isliye main yahan zyada din nahi rahoonga.”

Rama ne shaam ki pooja ki, phir Sita aur Lakshman ke saath raat guzaarne ki tayyari ki.
Raat hote hi Rishi Sutikshna ne apne haathon se Rama, Lakshman aur Sita ko hulled grain (saaf kiya hua anaaj, ascetics ka bhojan) prasad ke roop mein diya.

Is tarah Rama ne ek aur pavitra rishi ka ashirvaad paaya aur ashram mein ek shaant raat bitai.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter8
    with st.expander("Chapter 3.8 – Rama says goodbye to Sutikshna"):
        text1 = """
Rama aur Lakshman ne Rishi Sutikshna ke ashram mein ek shaant raat bitai. Subah hote hi wah dono Sita ke saath thandi aur kamal sugandhit (lotus-fragrant) paani mein snaan karne gaye.

Phir unhone Agni aur devataon ki pooja ki. Jab suraj poori tarah ug aaya, to Rama vinamr hokar Rishi Sutikshna ke paas gaye aur bole:

“Rishi ji, aapne humein bahut samman diya. Ab hum aapse vidai lena chahte hain, kyunki saath chal rahe sages aage badhna chahte hain.
Hum iss Dandaka Forest ke sab ashramon ka darshan karna chahte hain — un sab rishiyon ka, jo tapasya (penance) se pavitra ho gaye hain.”
        """
        create_image_text_layout("attached_assets/chapter3/3.8.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Rama ne yeh bhi kaha:
“Hum garam dhoop tezz hone se pehle nikalna chahte hain.”

Rama, Lakshman aur Sita ne jakar Sutikshna ji ke charanon mein pranam kiya.
Rishi Sutikshna ne unhe uthaya, prem se gale lagaya aur ashirwad diya:

“Rama, Lakshman, Sita — tum teeno surakshit jao.
Dandaka Forest ke un sundar sthal dekho jahan pavitra rishi rehte hain.
Wahan tumhe phal-phool se bhare van, hiran ke jhund, pyari chidiya, kamal ke phool, shant talab, pahaadon se girti jal-dhara (waterfalls) aur moron ki awaaz se gunjti ghatiyan milengi.
Aur jab tum sab dekh lo, toh mere paas wapas zaroor aana.”

Rishi ke shabdon ko sunkar Rama aur Lakshman bole:
“Rishi ji, aisa hi hoga.”

Unhone rishi ka pradakshina (circumambulation) kiya aur chalne ki tayyari ki.
Sita ne pyaar se unke quiver (tera-bharne ka tokra), dhanush aur chamakte talwaren unhe pakraayi.

Is tarah Rama, Lakshman aur Sita — teeno apna yatra ka agla padav shuru karte hue — Dandaka ke gahre van ki aur nikal pade.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter9
    with st.expander("Chapter 3.9 – Sita asks Rama not to fight the demons"):
        text1 = """
Rama jab Rishi Sutikshna se vidai lekar aage badh rahe the, tab Sita ne pyar aur namr (gentle) awaaz mein unse kaha:

“Rama, aap hamesha pavitra aur sahi raaste par chalne wale ho. Par kabhi kabhi chhoti si galti dheere-dheere badh kar badi ban jaati hai.
Ichchha (desire) se paida hone wali teen buri baatein hoti hain:

jhooth bolna,

kisi doosri ki patni par nazar rakhna,

bina wajah hinsa (violence) karna.

Aap ne kabhi jhooth nahi bola, aur na hi kabhi dusri aurat ke baare mein socha. Aap apne dharm, satya aur pitaji ke aadesh par poori tarah chalne wale ho. Aapne hamesha apne man ko niyantrit (controlled) rakha hai.”
        """
        create_image_text_layout("attached_assets/chapter3/3.9.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Sita ne halka sa saans liya aur phir boli:

“Par Rama, teesri buri baat — bina wajah hinsa — mujhe ab thodi chinta de rahi hai. Aapne rishiyon se wada kiya hai ki aap rakshason ko maarenge. Par main sochti hoon ki kya yeh sahi hoga?

Jab aap dhanush-baan lekar Dandaka ke jungle mein jaaoge, toh kahi rakshas ko dekhte hi teer na chala do. Jaise lakdi ki guchchhi aag ko badha deti hai, waise hi hathiyar ek yoddha ke gusse aur shakti ko badha dete hain.”

Sita ne ek purani kahani sunayi:

“Ek baar ek pavitra rishi tapasya kar rahe the. Tab Indra ne unki tapasya bigaadne ke liye ek talwar (sword) unke paas rakh di. Rishi ne socha—‘Mujhe iska dhyan rakhna hoga.’
Dheere-dheere woh har jagah talwar lekar jaane lage—phal lene, jadh-bhooti lene, sab jagah.
Talwar pakadte-pakadte unke man mein hinsa aa gayi. Unhe hinsa achchi lagne lagi.
Dheere-dheere unki tapasya toot gayi aur woh patan (fall into wrongdoing) mein gir gaye.

Isliye kehte hain, Rama—hathiyaar man ko badal dete hain.”

Sita ne Rama ka haath pakadkar kaha:

“Main aapko sikhane nahi aayi hoon. Bas patni hone ke nate chinta ho rahi hai.
Kripya bina wajah rakshason ko na maarna, Rama.
Yoddha ka dharm hota hai ki bina baat ke hinsa na kare.

Aap yahan vanvaas mein ho, ek tapasvi (ascetic) ki tarah rehna chahte ho. Jaisa maine suna hai—duty (kartavya) par chalne se hi sachchi khushi milti hai.

Ayodhya lautne par aap phir se apne yoddha-dharma ko poora kar sakte ho.
Par abhi, shanti aur dhairya (patience) hi sahi marg (right path) hai.”

Sita ne neeche dekh kar dheere se kaha:

“Aur Rama… yeh sab main isliye keh rahi hoon kyunki main aapse prem karti hoon.
Aakhir mein, jo bhi sahi lage, wahi kijiye. Aap hi sabse achche samajhdaar ho.”
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter10
    with st.expander("Chapter 3.10 – Rama reminds Sita about his promise to protect the sages"):
        text1 = """
Sita ki pyaar aur chinta se bhari baaton ko sun kar Rama ne shaant par majboot awaaz mein kaha:

“Sita, tumne jo kaha, woh prem (love) aur dayaluta (kindness) se hi nikla hai.
Par tumne khud hi ek baat kahi thi —
‘Yoddha apna dhanush isliye rakhte hain ki anyaay (oppression) kabhi duniya mein na ho.’

Main Dandaka Forest isliye aaya hoon kyunki yahaan ke rishi–muni (ascetics) mere paas madad maangne aaye the.
Yeh bechare phal–mool par jeene wale tapasvi rakshason ke dar se chain se reh nahi paate.
Rakshas un par hamla karte hain, unke yagya bhang karte hain, aur kabhi kabhi unhe kha bhi jaate hain.”
        """
        create_image_text_layout("attached_assets/chapter3/3.10.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Rama ne yaad kiya kaise sages unke charanon mein gir pade the:

“Unhone mujhe pukaar kar kaha—
‘Rama, humein bachao!
Dandaka ke rakshas hamein vardaan ke bal par sata rahe hain.
Hum unhe shaap dekar mita sakte hain, par hum apni tapasya ka phal khona nahi chahte.’

Sita, unki aankhon mein dard tha.
Unki awaaz ka compan (trembling) sun kar hi maine wada kiya—
‘Dar mat karo. Main tumhari raksha karunga.’

Ab main unka diya hua wada kaise toda?
Rama ne dridh (firm) awaaz mein kaha:

“Sita, main apni jaan de sakta hoon,
tumhe bhi kho sakta hoon,
Lakshman tak ko de sakta hoon…

par ek baar brahminon se diya hua pratigya (vow) kabhi nahin tod sakta.

Agar mainne unse wada na bhi kiya hota,
tab bhi unki raksha mera kartavya (duty) hota.
Par ab to maine vachan diya hai.”

Phir Rama ne naram hokar Sita se kaha:

“Tumne jo kaha, woh tumhari pavitra soch ki wajah se hai.
Main jaanta hoon tum prem se hi mujhe rokna chah rahi ho.
Isliye tum meri praan se bhi zyada pyari ho.”

Itna kehkar Rama ne apna dhanush uthaya,
Sita ka haath pakda,
aur Lakshman ke saath Dandaka ke ghane, sundar, par khatarnak van mein aage badhte rahe.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter11
    with st.expander("Chapter 3.11 – Rama visits many ashrams and hears about Sage Agastya"):
        text1 = """
Rama aage chal rahe the, unke piche Sita, aur sabse piche Lakshman, apna dhanush pakde hue.
Teeno jungle ke beech pahadon, khuli maidaanon, phoolon se bhare ped, shant nadiyon aur kamal se lade hue talaabon ko dekhte aage badhte gaye. Jahan jahan jaate, hiran, hans, bagule, bhaloo, jangli bhaise aur bade bade aane wale haathi nazar aate.

Ek din suraj dhalne ke waqt, woh ek bada sa sundar jheel par pahunche—Panchapsara (lake created by penance).
Jheel mein kamal the, hans the, aur vanya hathi bhi. Paani bilkul shant tha. Par sabse ajeeb baat yeh thi ki wahan sangeet (music) baj raha tha, par koi dikh nahi raha tha!
        """
        create_image_text_layout("attached_assets/chapter3/3.11.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Rama ne ek rishi, Dharmabhrit (pious sage), se poocha:
“Hey rishi, yeh madhur sangeet kis ka hai?”

Rishi ne ek dilchasp kahani sunayi:
“Yeh jheel Sage Mandarkini ki tapasya se bani hai.
Woh hazaron saal tak paani mein khade rehkar bas hawa par jeete rahe.
Devtayon ko dar hua ki woh unke barabar na ho jaye, isliye unhone paanch sundar apsarayein (celestial nymphs) bheji.
Apsaraon ne rishi ka man mohit kar diya.
Phir woh aur apsarayein is jheel ke neeche banaaye hue ek gupt sthal mein rehte hain.
Unka sangeet hi aap sun rahe ho.”

Rama ne yeh kahani suni aur apne safar par aage badhe.
Teeno—Rama, Sita, Lakshman—alag-alag ashramon mein jaate, rishiyon se milte, kuch mahine unke saath rehte.
Kabhi 10 mahine, kabhi 4, kabhi ek-saadhai (one and a half), kabhi saal bhar bhi.
Aise hi 10 saal nikal gaye, bina kisi jaldi ke.

Phir Rama Rishi Sutikshna ke paas wapas aaye.
Wahan ek din unhone kaha:
“Rishi ji, log kehte hain ki Rishi Agastya yahin jungle mein rehte hain. Unka ashram kahan hai? Hum unse milna chahte hain.”

Rishi Sutikshna khush hokar bole:
“Rama, main bhi tumhe Agastya ji ke paas bhejna chahta tha.
Sunno — yahan se lagbhag chaar kos (about 4 miles) dakshin taraf unke bhai ka ashram hai.
Wahan phal-phool se bhare ped, kamal ke jheel, hans aur mitti ki meethi khushboo tumhe milegi.
Wahan ek raat aram karke, phir agle subah chaar kos aur aage jao — tumhe Rishi Agastya ka asli ashram mil jayega.
Sita, tum aur Lakshman wahan bahut khush rahoge.”

Rama, Lakshman aur Sita Sutikshna se vidai lekar path par chal pade.
Raaste mein har taraf:

Phoolon se lade ped,

janglon ko cheer kar nikalti nadia,

jheelon mein khelte hans aur batakh,

pedon par latakte creepers,

aur haathi jo ped tod kar raasta banate the.

Jab Rama ne Agastya ke bhai ka ashram dekha, woh bole:
“Lakshman, dekh! Pedon ke jhoolte phal, ripe fig ki khushboo, dhuaan uthta yagya, sab kuch wahi hai jaisa Sutikshna ne kaha tha.”

Fir Rama ne purani kahani sunai:
“Yahin par do rakshas — Vatapi aur Ilvala — brahminon ko dhokha dekar maarte the.
Ilvala ek sage ka roop lekar vatapi ko ek bakre ki tarah paka kar brahminon ko khila deta tha.
Phir woh chilata — ‘Vatapi, bahar aao!’
Aur Vatapi brahminon ke sharir cheer kar bahar aa jata.
Hazaron brahmin mare gaye.

Phir devtaon ke kahne par Agastya rishi ne us bhojan ko khalas kar diya.
Jab Ilvala ne ‘Vatapi, bahar aao!’ kaha, tab Agastya ji hans kar bole —
‘Woh bahar nahi aa sakta — woh mere pet mein pacha chuka hai.’
Ilvala gusse mein Agastya ji par jhapa, par unke dridh tapasya ke tej se vah bhi bhasm ho gaya.”

Rama, Lakshman aur Sita ne raat wahan bitayi, phal-mool khakar.
Subah Rama ne rishi ko pranam kiya aur kaha:
“Humein Rishi Agastya ke paas jaana hai.”

Rama ne phir Lakshman se kaha:
“Lakshman, hum bilkul paas aa gaye hain!
Pedon ki chamak, hilte hue panchhi, aur hiranon ka shant swabhav bata raha hai ki Agastya ji ka ashram yahin hai.
Unka ashram hamesha shuddh aur rakshason se mukt rehta hai.
Agastya rishi ke tej se Vindhya parvat tak ruk gaya tha!

Chalo, andar chalte hain.
Lakshman, Sita aur main — teeno milkar Agastya rishi ko apni aamad (arrival) ki soochna dein.”
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter12
    with st.expander("Chapter 3.12 – Agastya welcomes Rama to his hermitage"):
        text1 = """
Lakshman ashram ke darwaaze par Rishi Agastya ke ek shishya (disciple) ko mile.
Unhone vinamr tareeke se kaha:

“Main Lakshman hoon, Raja Dasharath ka chhota beta. Mere bade bhai Rama aur bhabhi Sita yahan Rishi Agastya ko pranam karne aaye hain. Hum teenon apne pita ji ke aadesh se is gahan jungle mein aaye hain.
Kripya Rishi ko humare aane ki soochna de dijiye.”

Shishya ne haath jodkar kaha:
“Thik hai.”
Woh turant aag ke kund ke paas baithen Agastya Rishi ke paas gaya aur bola:

“Rama, Lakshman aur Vaidehi (Sita) aaye hue hain.
O Maharishi, woh aapka darshan chahte hain.”
        """
        create_image_text_layout("attached_assets/chapter3/3.12.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Agastya ji yeh sunkar khush ho gaye:

“Ah! Bahut achha. Mujhe hamesha se Rama se milne ki ichchha thi.
Jao, unhe turant andar lao! Ab tak unhe yahan le kyon nahi aaye?”

Shishya wapas gaya aur Lakshman se poocha:
“Kaun hai Rama?”

Lakshman ne Rama aur Sita ko dikhaya, aur phir Rama ko ashram ke andar le gaye.

Rama ka ashram darshan

Ashram ke andar tame deer (palat sakne wale hiran), yagya-vedi, aur alag-alag devtaon ke sthaan the:

Brahma

Agni

Vishnu

Indra

Varuna

Vayu

Soma

Garuda

Nagas
aur bahut saare anya devta.

Jungle shant tha, aur ashram tapasya (penance) ke tej se chamak raha tha.

Phir ek roshni jaisa tej aaya—
Rishi Agastya khud prakat hue.

Rama ne Lakshman se halka sa kaha:
“Lakshman, dekh! Woh mahatejasvi Agastya ji hain. Inke charanon mein pranam karna mere liye gaurav ki baat hai.”

Rama turant unke charanon mein jhuk gaye.
Sita aur Lakshman bhi pranam karke khade ho gaye.

Agastya ji ne unhe gale lagaya, paani diya, baithne ko asan diya, aur jungle ki parampara ke hisaab se swagat kiya.

Woh bole:
“Rama, yahan aana mere liye bahut bada samman hai.
Jo tapasvi (ascetic) mehmaan ka dhang se satkar nahi karta, use agle janm mein dukh bhogna padta hai.
Par tum mere pyaare atithi ho.”

Phir Agastya ji ne bahut saare phal, phool, paani aur mool (roots) Rama ko arpan kiye.

Rishi Agastya ka maha-uphaar

Agastya Rishi ne muskura kar kaha:

“Rama, tum bahadur ho, isliye tumhe yuddh ke kuchh divya aayudh (divine weapons) deta hoon:

Vishnu ka divya dhanush (celestial bow) — sone aur heere se sajaya hua.

Brahmadatta shakti (divine dart) — suraj jaisi chamak wali.

Do akshay quiver (never-ending arrow cases) — jisme teer kabhi khatam nahi hote.

Chandi ka scabbard (weapon holder) aur sona-jadi talwar.

Agastya ji bole:
“Is dhanush se hi Vishnu ne maha-asura ko maara tha.
Yeh sab vijay ke prateek (symbols of victory) hain.
Rama, inhe apnao— jaise Indra apna vajra (thunderbolt) uthata hai.”

Agastya ji ne yeh sab Rama ko diya—
aur Rama ne shraddha se sir jhukakar prasad ki tarah accept kiya.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter13
    with st.expander("Chapter 3.13 – Agastya guides Rama to stay in Panchavati"):
        text1 = """
Rishi Agastya ne pyaar se Rama, Lakshman aur Sita ki taraf dekha aur bole:

“Rama, tum teenon yahan aaye — isse mujhe bahut khushi hui.
Itna lamba safar karte hue tum zaroor thak gaye hoge,
aur Maithili (Sita) ka halka sa saans lena batata hai ki woh bhi thak gayi hai.

Sita ek komal aur shaalin (gentle, refined) rajkumari hai.
Phir bhi woh tumhare saath mushkil raaste se guzri — sirf prem ke karan.”

Agastya ne phir muskurakar kaha:
“Rama, aam taur par striyan aasani se ghabra jaati hain —
par tumhari Sita bilkul alag hai.
Woh Arundhati (symbol of loyalty) ki tarah pavitra aur nishtha-vaan (faithful) hai.
Jahan tum, Lakshman aur Sita rahoge,
woh jagah hamesha pavitra mana jayega.”
        """
        create_image_text_layout("attached_assets/chapter3/3.13.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Rama ne haath jodkar kaha:
“Rishi ji, aapka ashirvad paakar hum dhanay ho gaye.
Kripya batayein humein kahan rehna chahiye —
jahan ped-paudhe ho, paani ho, aur hum shanti se reh sakein.”

Rishi Agastya thodi der soch kar bole:
“Rama, yahan se aath kos (about 8 miles) door ek jagah hai — Panchavati.
Wahaan phal-mool, paani, aur hiran bahut milte hain.
Tum Lakshman ke saath wahan ek chhota sa ashram bana sakte ho.
Maithili ko woh sthal bahut pasand aayega.

Woh Godavari nadi ke paas hai —
sundar, shaant, aur pavitra.
Tumhara kartavya hai sab rishiyon ki raksha karna;
Panchavati iske liye bilkul uchit (perfect) jagah hai.”

Agastya ne aur bataya:
“Yahan se tum Madhuka ke ped dekh rahe ho na?
Unhe paar karke pahadiyon ke kinare se jao —
tumhe phoolon se bhara Panchavati mil jayega.”

Rama ne rishi ko pranam kiya,
Lakshman aur Sita ne bhi unke charan chhuye.
Teeno ne rishi ka pradakshina ki,
aur unke aashirvad lekar Panchavati ki raah pakdi.

Teeno — Rama, Lakshman, Sita —
dhanush uthaye,
quiver baandhe,
aur Agastya ne bataye hue raaste par
dridh sankalp (firm resolve) ke saath nikal pade.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter14
    with st.expander("Chapter 3.14 – Jatayu tells Rama about his family"):
        text1 = """
Rama, Sita aur Lakshman Panchavati ki taraf ja hi rahe the ki unhone ek bahut bada aur shaktishaali gidh (vulture) dekha.
Rama aur Lakshman ko shak hua ki shayad yeh koi rakshas ho jo roop badal kar aaya ho.

Unhone poocha:
“Tum kaun ho?”

Tab woh pakshi ne bohot komal, pyaar se bhari awaaz mein kaha:
“Beta, main tumhare pita Dasharath ka dost hoon.”

Yeh sunkar Rama ne turant unke charanon ko chhua aur bola:
“Kripya apna naam aur vansh batayein.”
        """
        create_image_text_layout("attached_assets/chapter3/3.14.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Tab gidh ne apni lambi kahani shuru ki — ek purani pauranik (mythological) kahani:

“Rama, pehle kalp mein bahut saare Prajapati (creators) hue—Kardama, Vikrita, Shesha, Marichi, Atri, Angira, Pulaha, Daksha, Kashyapa… aur bhi bahut.
Daksha ki bahut si betiyan thi.
Kashyapa ne inmein se kuchh se vivaah karke alag-alag praja (creatures) ka janm diya.”

Phir unhone bataya kaise duniya ki alag-alag praja paida hui:

Aditi se devta (gods)

Diti se daityas (powerful demons)

Danu se danavas

Kalika se Naraka aur Kalaka

Tamra se pakshi jaati:

Kraunchi → ullu (owls)

Bhasi → vultures

Shyeni → hawks & eagles

Dhritarashtri → swans & flamingos

Shuki → Nata → Vinata (later mother of Garuda)

Aur yahin se Jatayu ki kahani judti hai:

“Main Aruna ka beta hoon, aur Sampati mera bada bhai.
Mera naam Jatayu hai.
Main Shyeni vansh ka hoon, hawks aur eagles ka vansh.”

Phir Jatayu ne bohot prem se kaha:

“Rama, agar tum chaho, to main yahin tumhare paas rahunga.
Tum jab van mein shikar ya rishiyon ki raksha mein jaoge,
main Sita ki dekhbhaal karunga.”

Rama ke chehre par khushi chamak uthi.
Unhone Jatayu ko gale lagaya aur kaha:

“Tumne hamare pita ka dosti nibhaya —
ab tum hamare bhi apne ho.”

Jatayu unke saath Panchavati ki taraf ud kar chal diya.
Rama ne apni dincharya (daily devotion) poori ki,
aur teeno milkar apne naye ghar ki taraf badhne lage—
dil mein ek dridh sankalp ke saath:
rakshason ka vinash aur rishiyon ki raksha.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter15
    with st.expander("Chapter 3.15 – Rama makes his home in Panchavati"):
        text1 = """
Rama, Sita aur Lakshman jab Panchavati pahunche — jaisa Agastya Rishi ne bataya tha — to jungle hariyali, hiran, pakshi aur phoolon se bharpoor tha.

Rama ne Lakshman se kaha:
“Lakshman, yeh wahi sundar jagah hai jiska rishi ne varnan kiya tha.
Chalo, koi achchi si jagah dhoondhte hain jahaan hum teenon shanti se reh sakein —
nadi ke paas, phoolon aur phal se bhare pedon ke beech.”

Lakshman haath jodkar bole:
“Bhaiya, main sadaiv aapka sevak hoon.
Aap bas jagah bataiye — main turant ashram bana doonga.”
        """
        create_image_text_layout("attached_assets/chapter3/3.15.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Rama ne Sita aur Lakshman ko ek khula, sundar sthal dikhaya aur bola:
“Yahin, Lakshman!
Yahaan ek nadi beh rahi hai — Godavari — jisme kamal khilte hain, hans aur jal-pakshi (water birds) tairte hain, aur hiran pani peene aate hain.
Jungle ki pahadiyan moron ki awaaz se goonj rahi hain.
Aur dekho — itne saare ped:
Sala, Tamala, Panasa, Ashoka, Champaka, Chandana, Khadira…
Yeh hamara ghar banane ke liye bilkul sahi jagah hai.
Jatayu bhi yahin aas-paas rahega.”

Lakshman ne ek sundar ashram bana diya

Lakshman ne bina deri kiye kaam shuru kar diya.
Unhone:

lambe bamboo ke lakdi ke khambe lagaye,

deeware mitti se banayi,

छत (roof) शमी के पत्तों, बेलों और घास से ढकी,

andar ki zameen ko saman aur saaf kiya.

Jald hi ek sundar, sookhi pattiyon wali kutia tayyar ho gayi.

Phir Lakshman Godavari nadi par gaye —
snan kiya, kamal ke phool aur phal ikattha kiye,
aur ghar ki shanti ke liye parampara wale puja-vidhi ki.

Rama ki khushi

Jab Rama aur Sita ne woh hut dekhi,
to Rama ke chehre par ek barson baad wali sukoon ki chamak aa gayi.

Rama ne Lakshman ko gale lagaya aur kaha:

“Lakshman, tumne kamaal kar diya.
Tumhari seva, tumhari shiddat (dedication) aur tumhara prem —
yeh sab dekhkar mujhe lagta hai ki
jab tak tum zinda ho, humare pita Dasharath ji bhi hamare saath hi jeevit hain.”

Lakshman ne sharmate hue muskuraya.

Is tarah Rama, Sita aur Lakshman —
Jatayu ke saath, phal-phool aur shanti se bhare Panchavati mein —
bilkul devtaon ki tarah anand se rehne lage.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter16
    with st.expander("Chapter 3.16 – Lakshmana describes the winter season"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.16.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter17
    with st.expander("Chapter 3.17 – Shurpanakha arrives at their hut"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.17.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter18
    with st.expander("Chapter 3.18 – Shurpanakha is punished and injured"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.18.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter19
    with st.expander("Chapter 3.19 – Shurpanakha complains to her brother Khara"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.19.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter20
    with st.expander("Chapter 3.20 – Rama kills the demons sent by Khara"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.20.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter21
    with st.expander("Chapter 3.21 – Shurpanakha tells Khara to attack Rama"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.21.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter22
    with st.expander("Chapter 3.22 – Khara marches with his huge demon army"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.22.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter23
    with st.expander("Chapter 3.23 – The demon army moves forward with scary signs"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.23.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter24
    with st.expander("Chapter 3.24 – Rama begins battle with the demons"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.24.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter25
    with st.expander("Chapter 3.25 – The battle between Rama and the demons continues"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.25.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter26
    with st.expander("Chapter 3.26 – Rama destroys the demons and kills Dushana"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.26.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter27
    with st.expander("Chapter 3.27 – Rama fights Trishiras and wins"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.27.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter28
    with st.expander("Chapter 3.28 – Rama fights the demon leader Khara"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.28.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter29
    with st.expander("Chapter 3.29 – Rama and Khara challenge each other"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.29.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter30
    with st.expander("Chapter 3.30 – Khara is killed by Rama"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.30.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # chapter30
    with st.expander("Chapter 3.10 – Rama reminds Sita about his promise to protect the sages"):
        text1 = """
        """
        create_image_text_layout("attached_assets/chapter3/3.10.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # chapter31
    with st.expander("Chapter 3.11 – Rama visits many ashrams and hears about Sage Agastya"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.11.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # chapter32
    with st.expander("Chapter 3.12 – Agastya welcomes Rama to his hermitage"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.12.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # chapter33
    with st.expander("Chapter 3.13 – Agastya guides Rama to stay in Panchavati"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.13.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # chapter34
    with st.expander("Chapter 3.14 – Jatayu tells Rama about his family"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.14.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # chapter35
    with st.expander("Chapter 3.15 – Rama makes his home in Panchavati"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.15.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # chapter36
    with st.expander("Chapter 3.16 – Lakshmana describes the winter season"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.16.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # chapter37
    with st.expander("Chapter 3.17 – Shurpanakha arrives at their hut"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.17.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # chapter38
    with st.expander("Chapter 3.18 – Shurpanakha is punished and injured"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.18.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # chapter39
    with st.expander("Chapter 3.19 – Shurpanakha complains to her brother Khara"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.19.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter20
    with st.expander("Chapter 3.20 – Rama kills the demons sent by Khara"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.20.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter21
    with st.expander("Chapter 3.21 – Shurpanakha tells Khara to attack Rama"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.21.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter22
    with st.expander("Chapter 3.22 – Khara marches with his huge demon army"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.22.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter23
    with st.expander("Chapter 3.23 – The demon army moves forward with scary signs"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.23.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter24
    with st.expander("Chapter 3.24 – Rama begins battle with the demons"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.24.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter25
    with st.expander("Chapter 3.25 – The battle between Rama and the demons continues"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.25.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter26
    with st.expander("Chapter 3.26 – Rama destroys the demons and kills Dushana"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.26.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter27
    with st.expander("Chapter 3.27 – Rama fights Trishiras and wins"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.27.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter28
    with st.expander("Chapter 3.28 – Rama fights the demon leader Khara"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.28.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter29
    with st.expander("Chapter 3.29 – Rama and Khara challenge each other"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.29.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter30
    with st.expander("Chapter 3.30 – Khara is killed by Rama"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.30.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter31
    with st.expander("Chapter 3.31 – Ravana hears about Khara’s death and becomes furious"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.31.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter32
    with st.expander("Chapter 3.32 – Shurpanakha tells Ravana to take revenge on Rama"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.32.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter33
    with st.expander("Chapter 3.33 – Shurpanakha warns Ravana about Rama"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.33.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter34
    with st.expander("Chapter 3.34 – Shurpanakha tells Ravana to kill Rama and marry Sita"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.34.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter35
    with st.expander("Chapter 3.35 – Ravana visits the demon Marica again"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.35.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter36
    with st.expander("Chapter 3.36 – Ravana tells Marica his plan"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.36.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter37
    with st.expander("Chapter 3.37 – Marica tries to stop Ravana from doing wrong"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.37.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter38
    with st.expander("Chapter 3.38 – Marica tells Ravana how he once met Rama"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.38.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter39
    with st.expander("Chapter 3.39 – Marica again tries to stop Ravana"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.39.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter40
    with st.expander("Chapter 3.40 – Ravana becomes angry"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.40.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter41
    with st.expander("Chapter 3.41 – Marica gives Ravana more advice"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.41.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter42
    with st.expander("Chapter 3.42 – Marica becomes a golden deer and goes near Rama’s hut"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.42.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter43
    with st.expander("Chapter 3.43 – Sita becomes attracted to the beautiful deer"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.43.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter44
    with st.expander("Chapter 3.44 – Rama kills Marica, the fake deer"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.44.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter45
    with st.expander("Chapter 3.45 – Sita sends Lakshmana to help Rama"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.45.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter46
    with st.expander("Chapter 3.46 – Ravana comes near Sita"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.46.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter47
    with st.expander("Chapter 3.47 – Ravana and Sita talk"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.47.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter48
    with st.expander("Chapter 3.48 – Sita bravely refuses Ravana"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.48.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter49
    with st.expander("Chapter 3.49 – Ravana kidnaps Sita"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.49.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter50
    with st.expander("Chapter 3.50 – Jatayu tries to stop Ravana"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.50.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter51
    with st.expander("Chapter 3.51 – Jatayu fights Ravana bravely"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.51.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter52
    with st.expander("Chapter 3.52 – Jatayu is wounded and Ravana flies away"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.52.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter53
    with st.expander("Chapter 3.53 – Sita scolds Ravana for his evil act"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.53.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter54
    with st.expander("Chapter 3.54 – Ravana reaches Lanka with Sita"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.54.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter55
    with st.expander("Chapter 3.55 – Ravana asks Sita to marry him"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.55.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter56
    with st.expander("Chapter 3.56 – Demon women guard Sita"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.56.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter57
    with st.expander("Chapter 3.57 – Rama sees bad signs and becomes worried"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.57.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter58
    with st.expander("Chapter 3.58 – Rama cries for Sita"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.58.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter59
    with st.expander("Chapter 3.59 – Rama gets angry at Lakshmana in sadness"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.59.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter60
    with st.expander("Chapter 3.60 – Rama and Lakshmana begin searching for Sita"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.60.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter61
    with st.expander("Chapter 3.61 – Rama expresses his sorrow"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.61.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter62
    with st.expander("Chapter 3.62 – Rama feels deep despair"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.62.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter63
    with st.expander("Chapter 3.63 – Rama continues to cry for Sita"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.63.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter64
    with st.expander("Chapter 3.64 – Rama becomes angry at the situation"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.64.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter65
    with st.expander("Chapter 3.65 – Lakshmana tries to calm Rama"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.65.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter66
    with st.expander("Chapter 3.66 – Lakshmana gives courage to Rama"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.66.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter67
    with st.expander("Chapter 3.67 – Rama finds the injured Jatayu"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.67.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter68
    with st.expander("Chapter 3.68 – Jatayu dies after telling Rama what happened"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.68.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter69
    with st.expander("Chapter 3.69 – Rama and Lakshmana meet Ayomukhi and Kabandha"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.69.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter70
    with st.expander("Chapter 3.70 – Rama and Lakshmana cut off Kabandha’s long arms"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.70.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter71
    with st.expander("Chapter 3.71 – Kabandha tells his story"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.71.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter72
    with st.expander("Chapter 3.72 – Kabandha tells Rama how he can find Sita"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.72.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter73
    with st.expander("Chapter 3.73 – Kabandha gives final advice to Rama"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.73.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter74
    with st.expander("Chapter 3.74 – Rama meets Shabari"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.74.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter75
    with st.expander("Chapter 3.75 – Rama reaches the beautiful Lake Pampa"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.75.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")
