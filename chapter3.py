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
Panchavati mein kuch samay beet chuka tha.
Sharad ritu (autumn) ab samaapt ho gayi thi,
aur dheere-dheere sheet ritu (winter) aa rahi thi.

Ek subah, jab aasman bas halka sa safed ho raha tha,
Rama apne roz ke niyam ke mutabik Godavari nadī ki taraf gaye
taaki apne snan (ablutions) kar sakein.
Sita aur Lakshman unke peeche-peeche chal rahe the.
Lakshman ke haath mein ek kamandalu (water pot) tha.

Us ne pyaar aur vinamrta se kaha:
        """
        create_image_text_layout("attached_assets/chapter3/3.16.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
🌨 Lakshman ka Sheet Ritu ka Varnan

“Prabhu, woh ritu aa gayi hai
jo aapko hamesha ati-priya hoti hai.
Ab poora saal jaise apne upar
barf sa shwet alankaar pehen leta hai.

Zameen par pala (frost) jam gaya hai,
aur paani ab peene mein sukhad nahi lagta.

Is samay log pitron aur devataon ko bali dete hain,
aur un ke paap dur hote hain.
Gharon mein doodh, dahi aur makhan ki bharmaar hoti hai.

Raja log, yudh ki ichchha rakhte hue,
apne abhiyan par nikal padte hain.
Surya dakshin disha ki taraf sarak chuka hai,
aur uttari pavan ab barf jaisi thandi ho gayi hai.

Himvan parvat—
ab bilkul apne naam ke anuroop—
hamesha barf se dhaka rehta hai.

Din to suhavne lagte hain
jab thodi si dhoop milti hai,
par ab dhoop kamzor hai,
aur sardi teekhi.

Ratriyan lambi ho gayi hain—
aap khule aasman ke neeche nahi so sakte.
Pushya nakshatra, jo rasta dikhata tha,
ab barfili hawaon mein dikhai nahi deta.”

❄️ Prakriti par sardi ka prabhav

“Chandamaama bhi jaise
apni chamak kho baitha ho,
jaise kisi ne hawa phoonk kar
aaina dhundhla kar diya ho.

Pashchim ki hawa
apni saans tak jamaye hue hai.

Jungle dhundh mein lipta pada hai,
gehun-jataon par shabnam (dew) ki chamak hai.
Shyen, bagule, hans— sab
apni pukar se pata chalte hain,
warna unki safed pankh barf mein kho jaati.”

“Haathi jab thande jaldhar (frozen streams) ko
sundh se chhoote hain,
to turant piche kheech lete hain.

Kamale murjha gaye hain—
sirf unke dand (stalks) reh gaye hain.”

❤️ Lakshman ki Bharata ke liye chinta

Phir Lakshman ka mann bhavuk ho gaya.
Usne kaha:

“Hey Ram,
isi sardi mein, isi ghadi, Bharata
Ayodhya mein tapasya kar raha hoga.

Usne rajya aur sukh sab chhod diya hai—
sirf aapki seva aur pratigya ke liye.

Wo itna komal, itna sukh-palit tha…
main sochta hoon woh
Sarayu ke barf jaisey paani ko
kaise jhel pata hoga?

Bharata—
jo nayan se kamal sa,
hriday se komal,
vani se madhur,
vishayon se virakta,
aur dharma ka sacha palak hai—

vo aapke bina ek pal bhi sukh nahi le raha.

Kehte hain beta maa par jaata hai…
to agar aisa hai,
to Kaikeyi jaisi kathor kaise uski maan ho sakti hai?”

🤎 Rama ka Lakshman ko Uttar

Lakshman ke kathor shabdon se Rama ka hriday dukhi ho gaya.
Wo apni maata Kaikeyi ki ninda nahi sun sakte the.

Rama ne shant swar mein kaha:

“Lakshman,
Kaikeyi ko dosh mat do.
Jo hua, usme bhi hum sabka bhala hi chhupa tha.

Tum Bharata ki hi baat karo.”

Phir Rama ka swar bhavuk ho gaya.

“Lakshman,
main chahta hoon ki main
Bharata aur Shatrughna ko dubara dekh paun.
Unke madhur shabd mujhe yaad aate hain—
amrit se bhi madhur.”

Unka hriday bhaavnaon se bhar utha.

🌅 Dev-pujan aur snan

Is chintan mein ve
Godavari tak pahunch gaye.
Teeno ne milkar snan kiya,
pitron aur devataon ko jal arpit kiya,
aur Surya aur Narayana ki pooja ki.

Snan ke baad teeno—
Rama, Sita aur Lakshman—
aise dikh rahe the jaise:

Shiv ji Nandi ke saath,
aur Parvati ji unke paas.

Divya, shuddha,
aur prakash se mandit.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter17
    with st.expander("Chapter 3.17 – Shurpanakha arrives at their hut"):
        text1 = """
Godavari mein snan karne ke baad
Rama, Sita aur Lakshman
apne Panchavati ke hut ko laut aaye.

Rama aur Lakshman ne
apni pratah-sandhya, japa aur dev-pujan kiya,
aur phir teeno apni patra-chhaya (leaf hut) mein pravisht hue.

Wahan, Sita ke saath baithe,
Rama aise lag rahe the jaise
Chandra dev Citra nakshatra ke saath chamak raha ho.

Sab kuch shaant tha…
tabhi ek din, jab Rama
Vedic mantron ka paath kar rahe the,
koi ajeeb sa saaya unke paas se guzarne laga.
        """
        create_image_text_layout("attached_assets/chapter3/3.17.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Woh koi aur nahi,
Rakshasi Shurpanakha thi—
Ravana ki behen.

🌑 Shurpanakha ka Rama ko dekhkar mohit ho jana

Jaise hi Shurpanakha ne Rama ko dekha,
uska hriday bas pighal gaya.

Usne Rama ko is tarah dekha:

sundar, tejasvi, dev tulya

neel kamal jaisa rang

gahri nayan, mastak par jataayein

uncha, balshali, veer

sundar madhur awaz

rajsi swaroop aur shaant prakriti

Aur phir apne aap ko dekha:

bhayanak sharir, vikrit roop

tilted, laal aankhen

bhadday baal

kathor mukha, asundar awaz

vriddh, krodhit swabhav

Phir bhi, visham tej uske mann ko roka nahi saka.
Woh avasar dekhte hi Rama ke paas aa pahunchi.

🗣 Shurpanakha ka pehla prashn

Usne rāga bhari aawaz mein poochha:

“Hey veer purush…
jungle mein dhanush-baan lekar, jataayein baandh kar,
aur is sundar stri (Sita) ko saath lekar
tum yahan kya kar rahe ho?

Yeh rakshason ka kshetra hai.
Tum yahan kyun aaye ho?”

🗣 Rama ka parichay dena

Rama ne seedhe, vinamr shabdon mein uttar diya:

“Main Dasharatha ka putra Rama hoon.
Yeh mera chhota bhai Lakshman hai.
Aur yeh meri patni, Sita, Videha ki rajkumari.

Pita ke vachan nibhaane ke liye
hum jungle mein vanvaas kar rahe hain.

Par tum kaun ho?
Kis kul se aayi ho?
Tumhara roop to rakshasi jaisa lagta hai.”

❤️ Shurpanakha ka prem-prastav

Rama ke shabdon ne
uski ichchha aur tez kar di.

Woh bol uthi:

“Suno Rama!
Main Shurpanakha hoon— ek rakshasi.
Main apna roop badal sakti hoon,
hawaa ki tarah jungle-jungle ghoomti hoon.

Mere bhai hain—
Ravana, Lanka ka raja,
Kumbhakarna,
Vibhishana (jo dharmi hai),
aur veer Khara aur Dushan.

Main sabse shaktishaali hoon!

Aur tumhe dekhkar…
mujhe tumse prem ho gaya hai.
Tum mere pati ban jao!

Yeh Sita… tumhare laayak nahi.
Main tumhari sundari patni ban sakti hoon—

Mujh jaisi sundari, tum jaisa sundar!
Is manushya stri ko main abhi kha jaungi
aur tumhare bhai Lakshmana ko bhi!

Phir hum dono
Dandaka ka pura van
saath-saath ghoomte hue raj karenge!”

Usne Rama ki taraf
bhari kamna aur laalasa se dekha.

😊 Rama ka haskar uttar

Rama ne sab kuch sun kar,
muskurate hue ek chatur uttar diya…
(jise agle adhyay mein padhte hain).
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter18
    with st.expander("Chapter 3.18 – Shurpanakha is punished and injured"):
        text1 = """
Shurpanakha ke prem-bhare shabdon ko sun kar
Rama halka sa muskura diye.
Unki muskuraahat mein thodi mazaak bhi thi.

Woh bole:

“Suno Shurpanakha…
main to pehle se vivaahit hoon.
Aur yeh meri priya patni Sita mere saath hai.
Do patniyon ki beech mein jo jhagda hota hai,
woh tum bardasht nahi kar paogi!”

Phir Rama ne chalaki se kaha:

“Lekin mera chhota bhai Lakshman…
vah abhi kawaarā (unmarried) hai.
Woh bhi sundar, veer aur komal hriday (soft-hearted) hai.
Tum usse shaadi kyun nahi karti?
Uske saath tum bina kisi pratiyogita (competition) ke reh sakti ho.”
        """
        create_image_text_layout("attached_assets/chapter3/3.18.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
💘 Shurpanakha ko Lakshman par bhram ho jana

Rama ki baat sun kar
Shurpanakha turant Lakshman ki taraf mud gayi.
Woh madhur andaz mein boli:

“Lakshman!
Meri sundarta tumhare laayak hai.
Aao, hum dono milkar Dandaka ka pura jungle ghoomte hain.”

😄 Lakshman ka mazaak-bhara uttar

Lakshman ne uski baat sun kar
mazak karte hue kaha:

**“Main to ek daas (servant) hoon, Rama ka.
Mere paas kuch bhi apna nahi.
Tum jaisi lotus-rang (lotus-colored) aur sundar rakshasi,
mere jaise sevak ko kyun chune?

Tum Rama ko apna pati banao.
Woh tumhare jaise sundar aur adbhut roop ka mol le sakte hain.
Sita jaise sadharan (ordinary) stri ko chhodkar,
woh tumhe hi chunenge.”**

Shurpanakha itni andhi ho chuki thi prem mein
ki usse samajh hi nahi aaya
ki Lakshman mazaak kar raha hai.

Usne Lakshman ki baat ko sach maan liya.

🔥 Shurpanakha ka Sita par hamla

Phir woh phir se Rama ke paas aayi.
Iss baar uski aankhon mein krodh aur jalan thi.

Woh cheekhti hui boli:

**“Tum is badsurat, kamzor aur budi stri
Sita ke liye mujhe thukra rahe ho?

Aaj ke din main ise tumhare saamne kha jaungi!
Phir tum sirf mere rahoge!”**

Yeh keh kar Shurpanakha
badi gati se Sita par jhapat padi,
jaise ek ulka (meteor) Rohini nakshatra par toot padti ho.

⚔ Rama ka Lakshman ko aadesh

Rama ne turant Sita ko sambhala
aur krodh se bole:

**“Lakshman!
Dushton ko chhedna achha nahi hota.
Ab dekho — Sita khatre mein hai!

Is rakshasi ko turant dand do.
Iske haath-pair mat kaatna,
sirf isko bekaar kar do (maim).
Jaldi!”**

⚔ Lakshman ka Shurpanakha ko saza

Lakshman ne bina jhijhak
apni talwar nikali.

Ek tezi bhari chaap ke saath
Lakshman ne Shurpanakha ki naak aur kaan kaat diye.

Rakshasi zor se cheekhti hui
Khoon se labalab bheeg gayi.
Uski cheekh poore jungle mein goonj uthi
jaise baarish ke mausam ka toofan.

Dar aur dard se behaal Shurpanakha
chillati hui jungle ki gehraai mein bhaag gayi.

🏃‍♀ Shurpanakha ka Khara ke paas shikayat le jaana

Khoon mein lipti aur bilkul badhaali mein
Shurpanakha seedha apne bhai
Khara ke paas pahunchi —
jo Janasthaan mein apne rakshason ke saath baitha tha.

Woh zameen par gir padhi
jaise aasmaan se patthar (meteorite) toot kar gir jaye.

Halka pad chuki saanson aur ghabrahat mein,
usne Khara ko bataya:

Rama ka aagman

Sita aur Lakshman ka saath hona

Apni naak aur kaan ka kaat diya jana

Aur woh badle ki aag mein jalne laga…
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter19
    with st.expander("Chapter 3.19 – Shurpanakha complains to her brother Khara"):
        text1 = """
Shurpanakha khoon se bhari, zameen par padi thi.
Uski naak aur kaan kategaye the.
Yeh dekh kar uska bhai Khara gusse se kaamp utha.

Woh garajte hue bola:

**“Utho Shurpanakha!
Kya hua tumhare saath?
Kisne tumhe is haal mein pahunchaya?

Kaun wo murakh (fool) hai
jisne aaram se pade ek zehreeli saanp ko
apne pair se chhed diya?

Usne to maut ka phanda (noose)
apne hi gale mein daal diya hai!”**
        """
        create_image_text_layout("attached_assets/chapter3/3.19.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Khara phir bola:

**“Tum to shaktishaali ho.
Tum hawa ki tarah kahin bhi ja sakti ho.
Phir tum is tarah pareshaan kaise ho gayi?

Devta, Gandharva, mahan rishi—
koi bhi tumhe chot nahi pahucha sakta!
Kaun aisa himmatwala hai
jise ne tumhe vikrit (disfigure) kar diya?

Aaj main usko apne baanon se maar daalunga.
Uska khoon iss dharti par bahega.
Aur giddh (vultures)
uske sharir ko cheer kar khayenge!”**

Khara ka krodh aur badh gaya:

“Na Devta, na Gandharva,
na Pisach (evil spirits), na Rakshas—
koi bhi usko bachaa nahi sakta.
Shanti se batao,
kaun hai woh dusht (wicked one)?”

😡 Shurpanakha ki roti hui kahani

Aansu pochte hue
Shurpanakha ne kaha:

**“Do bahut sundar aur shaktishaali yuva aaye hain.
Unki aankhen kamal jaisi hain.
Woh valkal (tree-bark robe) aur krishna-mriga-chhal (black antelope skin) pehen kar rahe hain.
Phal-mool khate hain.
Aur brahmacharya (self-discipline) ka palan karte hain.

Woh hain Raja Dasharatha ke do putra—
Rama aur Lakshmana.
Unke beech ek komal kamar wali
sundar kanya bhi thi— Sita.

Usi ladki ke kaaran
mera yeh haal hua!

Main chahti hoon ki
main donon bhaiyon ka
aur us stri ka
khoon pi jaun!”

⚔ Khara ka pratishodh

Khara yeh sunkar
bilkul pagal jaisa gussa ho gaya.

Usne chaudah balwaan rakshason ko bulaaya—
jo shakti mein Antaka (god of death) ke barabar the.

Woh garja:

**“Do aadmi aur ek aurat
hamare Dandaka van mein aa gaye hain.
Tum sab turant jao
aur unhe maar daalo!

Meri behen unka khoon peena chahti hai.
Uski yeh sabse badi ichchha hai.
Jao!
Apni shakti dikhakar
un donon bhaiyon ko gira do!”**

Chaudah rakshas turant chale gaye.
Shurpanakha bhi unke saath bhaagi—
jaise aandhi ke saath badal uddh jaate hain.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter20
    with st.expander("Chapter 3.20 – Rama kills the demons sent by Khara"):
        text1 = """
Shurpanakha bade gusse aur dard mein
Rama ke hermitage (forest home) tak aa pahunchi.
Usne un chaudah rakshason ko
Rama, Lakshmana aur Sita ka ghar dikhaya.

Rakshason ne dekha—
Rama apni patni Sita ke saath
patton ki jhopdi mein baithe the.
Lakshmana unke paas khade the.

Rama ne Shurpanakha ko dekha
aur uske saath aaye rakshason ko bhi.
Phir woh Lakshmana se bole:

“Lakshmana, tum Sita ke paas hi raho.
Main in rakshason ko rokun.”

Lakshmana ne haath jod kar kaha:

“Aap jaise chaahein, waise hi hoga.”
        """
        create_image_text_layout("attached_assets/chapter3/3.20.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
⚔ Rama ka rakshason ko chetavani dena

Rama ne apna bada sa dhanush (bow)
jo sona-jadit (gold-embellished) tha, khinch liya.
Phir unhone rakshason se kaha:

**“Hum Raja Dasharatha ke bete hain—
main Rama hoon aur yeh mere bhai Lakshmana.
Sita ke saath hum yahan vanvaas (forest exile) ke liye aaye hain.

Hum brahmacharya (self-discipline) aur tapasya (penance) karte hain.
Hum kisi ko pareshaan nahi karte.
Phir tum humein nuksaan pahunchane kyun aaye ho?

Sage logon ne humein bulaya hai
taaki hum rakshason ki durvyavhaar (evil deeds) rokein.
Isliye mai tumhe chetavani deta hoon—
agar zinda rehna chahte ho to
yahin se laut jao!”**

😈 Rakshason ka ghamand

Chaudah rakshas garajne lage:

**“Humare swami Khara naraaz hain!
Tumne unka apmaan kiya hai.

Aaj tum ek akela aadmi
chaudah rakshason se lad kar nahi bach sakte!
Hum tumhari talwar, dhanush sab kuch gira denge.
Aaj tumhari maut nishchit hai!”**

Rakshason ne apne bhalon (spears), gadaon (maces)
aur bhari hathiyaaron ko ghumaya
aur ek saath Rama par toot pade.

⚡ Rama ka adbhut yudh

Par Rama ne turant
chaudah teer chodh diye—
har teer ek bhaley ko beech se kaat gaya!

Rakshas gusse se garajte rahe,
par Rama ne phir teer nikale—
pathar par tez kiye hue,
sunehre nok wale.

Unko dhanu par rakhte hi
Rama ne unhe bijli ki tarah chhoda—
jaise Indra apna vajra (thunderbolt) chhodta hai.

Teer rakshason ke seene ko chhed kar
zameen mein aise ghus gaye
jaise saanp anthill (vaar) mein ghus jaata hai.

Ek-ek karke
sabhi chaudah rakshas gir pade—
kati hue vriksh (trees) ki tarah.
Khoon se lapetey hue,
nishpran (lifeless).

😱 Shurpanakha ki nayi cheekh

Apne sabhi saathiyon ko
ise halat mein dekh kar
Shurpanakha phir se cheekh uthi.

Khoon phir se behne laga.
Uska sharir gum se kaanp raha tha.
Woh vaapis Khara ke paas daudi
aur uske samne gir padi—
roti, chillati, aansuon mein doobi hui.

Usne Khara ko
rakshason ki maut
ek-ek karke batayi.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter21
    with st.expander("Chapter 3.21 – Shurpanakha tells Khara to attack Rama"):
        text1 = """
Shurpanakha zameen par gir-gir kar ro rahi thi.
Woh gusse, dard aur sharm se paagal si ho gayi thi.
Khara ne apni behen ko is haalat mein dekha
to usne kathor lekin uljhe hue shabdon mein kaha:

**“Shurpanakha!
Maine tumhare liye apne veer rakshason ko bheja tha.
Voh sab maans khane wale, balvaan aur wafadar the.
Woh kabhi mera aadesh nahi taal sakte.
Phir tum ab bhi kyun ro rahi ho?

Main tumhara rakshak hoon.
Tum is tarah zameen par kyon latpat ho?
Jaise koi saap thudak raha ho!

Utho!
Aise aansu mat bahaao.”**

Khara ne aise kahkar usse sambhalne ki koshish ki.
Tab Shurpanakha ne apni aankhon se aansu poonche
aur roti hui boli:
        """
        create_image_text_layout("attached_assets/chapter3/3.21.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
😢 Shurpanakha ka dard

**“Bhaiya… jab main tumhare paas aayi thi
tab mera naak-kaat diya gaya tha,
mere kaan kaat diye gaye the.
Mere sharir se khoon nadi ki tarah beh raha tha.

Tumne mujhe sambhala.
Aur mujhe khush karne ke liye
chaudah veer rakshas bheje
taaki woh Rama aur Lakshmana ko maar dein.

Par Rama ne un sab ko ek pal mein gira diya!
Unke teer bijli ki tarah girte hain.
Maine apni aankhon se dekha.
Main dar se kaanp uthi.

Meri jaan ghutan jaati hai,
har taraf khatra dikh raha hai.
Isliye phir se tumhare paas bhaag aayi hoon.”**

😰 Shurpanakha ki vinati

**“Bhaiya, ab tumhi mujhe bachaa sakte ho.
Jis tarah Rama ke teeron ne
mere saath aaye rakshason ko gira diya,
waise hi woh humein bhi gira sakta hai.

Agar tum mujhe pyaar karte ho,
aur apni sena se sacha prem rakhte ho,
to Rama ko aaj hi roko!

Woh hamare liye kaanta ban gaya hai—
hamari shanti bigaad raha hai.
Agar tumne use na maara,
to main tumhare saamne hi
pran chhod doongi.”**

Shurpanakha phir cheekhne lagi:

**“Sach to yeh hai, bhai…
tum Rama ka saamna kar hi nahi sakte!
Tum apne aap ko mahan yoddha samajhte ho,
par yeh sirf bhram hai.

Agar himmat nahi hai
to turant Janasthana chhod do!
Yeh tumhare jaise logon ke rehne ki jagah nahi hai.

Rama sachmuch shoorveer hai.
Uska bhai Lakshmana bhi
bade zor se ladta hai.
Isi liye unhone mujhe is haalat mein pohchaaya!”**

💔 Shurpanakha be-hosh ho jaati hai

Yeh sab keh kar
Shurpanakha zor-zor se chillaayi,
apne seene par haath maarne lagi
aur be-hosh ho kar gir padi.

Thodi der baad
woh hosh mein aayi,
par dard, gusse aur sharm ne use phir se rula diya.
Woh lagataar apna seena peetti rahi
aur rote hue apna dukh sunati rahi.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter22
    with st.expander("Chapter 3.22 – Khara marches with his huge demon army"):
        text1 = """
Shurpanakha ki teekhi baaton ko sun kar
Khara ka gussa phoot pada.
Apne rakshas yodhon ke beech baithe hue
woh garaj kar bola:

**“Tumhari ninda (insult) se mera khoon khol raha hai.
Main ise bardasht nahi kar sakta.
Rama mere liye kuch bhi nahi—
main use aaj hi khatam samajhta hoon.

Apne aansu rok lo.
Main Rama aur Lakshmana ko aaj yama-lok (world of death) bhej dunga.
Aur tum… tum unka khoon peeneki baat kar rahi thi—
to aaj tumhari ichchha poori ho jayegi.”**

Shurpanakha, yeh sun kar itni khush hui
ki turant apne bhai Khara ki tareef karne lagi.
Pehle usne uski ninda ki thi,
ab achanak uski prashansa (praise) karne lagi —
yeh sab uske andhe gusse aur mooh-baaji ka natija tha.
        """
        create_image_text_layout("attached_assets/chapter3/3.22.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
⚔️ Khara ka aadesh

Khara ne apne senapati Dushana ko bulaya
aur kathor swar mein bola:

**“Dushana!
Tayyar karo — choudah hazaar rakshas!
Sab ladayi mein maahir,
kabhi peeche na hattne wale,
garajti aandhi ki tarah darawne aur kathor.

Saath hi mera rath bhi lekar aao.
Teer-dhanush, chamakte talwar,
bhaale (spears), chakram (discus), sab taiyaar karo.
Main khud sena ka netritva (leadership) karunga
aur us ahankari (proud) Rama ko sabak sikhaoonga!”**

Dushana ne turant bada rath taiyaar kar diya.
Rath sone se sajaya hua tha,
uske chakra hara-panna (emerald) se chamak rahe the.
Us par jhanda, ghante aur shubh-chinh (good symbols) lage hue the—
machhli, phool, pakshi, sitare—jaise kisi rajsi yatra ka rath ho.

Khara rath par chadha aur gusse se dahad utha.

🌩️ Rakshas Sena ki march

Uske aadesh par,
choudah hazaar rakshas ek saath nikle.
Unke hathiyaar tez chamak rahe the—
barsi, talwar, gada, trishul, chakram,
aur bade dhanush.

Unki dahad se poora Janasthana ka jungle goonj utha.
Woh sab tezi se bhaage,
jaise kaale badal tufaan se bhare ho.

Khara ne unhe josh se dekhte hue kaha:

“Chalo! Aage badho!”

Poora sena aage daud padhi,
aur Khara ka rath peeche se garajta hua aaya,
uska saarathi (charioteer) ghodon ko tez daudata hua.

Khara baar-baar garaj kar kehta:

“Tez! Aur tez!
Main Rama ko khud maanta hoon!”

Uski dahad aise lag rahi thi
jaise badal barfili aandhi barsaane ke liye tayyar ho.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter23
    with st.expander("Chapter 3.23 – The demon army moves forward with scary signs"):
        text1 = """
Khara apni bhari-bharkam rakshas sena ke saath aage badh hi raha tha
ki aas-paas ajeeb aur darawne ashubh sanket (bad omens) dikhne lage.

Achaanak kaale badalon se laal khoon jaisi boondein tapakne lagin.
Khara ke rath ke tez ghode achanak seedhe raaste par ladkhada gaye.
Suraj pe ek kala daag aa gaya,
jaise angaar (burning coal) ki laal si seema usse gher rahi ho.

Rath ke sone ke jhanda par
ek bada sa gidh (vulture) aa baitha—
mand mand garajta hua.

Janasthaan ke aas-paas
kaale pakshi aur jangli jaanwar
tez cheekhne lage.
Bhediye, suar, aur darawne lomdi
aisi cheekh maarne lagin
jaise kisi ne dard se unhe jaga diya ho.

Phir bhayanak badal
jaise bade haathi ho,
aasman se khoon ki baarish karne lage,
aur aasman poora andhera ho gaya—
itna andhera ki logon ki rongte (hair standing) khade ho jaayein.
        """
        create_image_text_layout("attached_assets/chapter3/3.23.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Kahin se shaam aa gayi
jabki waqt nahi hua tha.
Suraj dhuan se dhak gaya.
Aise pakshi aur jangli janwar
Khara ka raasta rokne lage
jaise kisi ko chhetavni (warning) de rahe ho.

Jackal (jungle dogs)
aag jaisi laal zubaan dikhate hue
koondne lage.

Ek ajeeb sa sira-kata dhela (headless trunk)
aasman ke paas mandrate dikhayi diya—
bahut hi ashubh drishya.

Suraj ko jaise koi grah (planet) nigal raha ho,
hawa achanak tez chalne lagi,
aur din mein bhi tare jhilmilaane lage.

Kamal ke phool murjha gaye,
lake ka paani andhera ho gaya.
Pedon se phool-phal gir gaye.
Dhoop ke bina khamar jaisa andhera chhane laga.

Toote hue komet (falling stars) dikhayi diye.
Dharti halki si kaanp uthi.

Khara ki sharir mein ashubh sanket

Khara rath par khada hokar garaj hi raha tha
ki uska baaya haath phadphadane (twitching) laga.
Uski awaaz achanak ruk gayi.
Aankhon mein aansu aa gaye.
Sir dard se dhadhak utha.

Yeh sab dekhkar bhi
apne ghamand (arrogance) mein
woh lautna nahi chahta tha.

Khara ka ghamand bhara jawab

Woh hansa aur apni sena se bola:

**“Yeh sab ashubh sanket mujhe dara nahi sakte!
Main itna shaktishaali hoon ki
chaahun to taare tak gira sakta hoon!

Rama aur Lakshmana—
yeh do aadmi mere saamne kya hain?
Main inhe aaj hi mita dunga!
Meri behen Shurpanakha
unke khoon se apni pyaas bujhaayegi!

Main kabhi hara nahi hoon!
Aur agar chaahun to devon ke raja
Indra ko bhi hara sakta hoon—
to yeh do manushya kya cheez hain?”**

Rakshas sena,
jo maut ke muh me jaa rahi thi,
yudh ke liye aur bhi utsaahit ho gayi.

Devatayein aur Rishi aasman se dekhte hain

Sab devta, rishi, gandharva aasman me jama ho gaye
aur ek dusre se bole:

“Dharti, gau, aur brahminon ki raksha ho.
Jaise Vishnu ne asuron ko haraaya,
waise hi Rama bhi in rakshason par vijay paaye.”

Woh sab aasman se
rakshas sena ko dekh rahe the—
jo apne antim vinash ki taraf badh rahi thi.

Sena ki bhayankar aagey-badhai

Khara ne apna rath aage kadh diya.
Uske aas-paas uske 12 shaktishaali senapati chale:

Karaviraksha

Parasha

Kalakarmukha

Hemamalin

Mahamalin

Sarpasya

Shyengamin

Prithugriva

Vajnashatru

Vihangama

Dirjaya

Krudhirashana

Aur unke peeche
Dushana ke saath 4 aur rakshas:

Mahakapala

Sthulaksha

Pramatha

Trishiras

Jaise grah (planets)
suraj aur chaand ki taraf tej gati se badhte hain,
waise hi yeh rakshas
Rama aur Lakshmana ki taraf
jaan hatheli par lekar daud pade.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter24
    with st.expander("Chapter 3.24 – Rama begins battle with the demons"):
        text1 = """
Khara jab apni bhayanak rakshas sena ke saath
Rama ke hermitage ke paas aaya,
to Rama aur Lakshmana ne aas-paas
bahut ashubh sanket (bad omens) dekhe.

Rama ne gahri saans lekar kaha:

“Lakshmana, dekho! Yeh ajeeb badal
jaise gadhe ki chamdi ho,
aasman mein khoon ki boonden barasa rahe hain.
Mere teer se dhuaan nikal raha hai—
jaise ve ladhne ke liye khud excited ho.
Mera sona-jaisa dhanush
khud ba-khud hil raha hai—
jaise yuddh bula raha ho.”

Jungle ke pakshi bhi
kuch alag hi tareeke se cheekh rahe the.
Sita aur Lakshmana ke saath
Rama ko lag gaya
ki bahut bade yuddh (battle) ka samay aa gaya hai.

“Mera baaya baahu phadphada raha hai, Lakshmana—
aur yeh jeet ka sanket hota hai.
Rakshason ki haar nishchit hai.”
        """
        create_image_text_layout("attached_assets/chapter3/3.24.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Phir Rama ne kaha:

**“Lakshmana, Sita ko lekar ek chhupi hui pahaadi gufa (mountain cave)
mein chala jao.
Main chahta hoon ki main yeh poora yuddh
akela ladun.

Tum bahadur ho,
par yeh ladaai main apne aap ladna chahta hoon.”**

Lakshmana ne turant
dhanush-baana uthaye
aur Sita ke saath
gufa ki taraf chal diye.

Rama
apne bhai ki aagya-paalan se khush hua,
aur usne apni tej chamak wali kavach (armour) pehen li.

Armour pehenkar Rama
jaise ek jalti hui jyoti (flame) lag raha tha.
Usne apna dhanush chadhaya
aur uski taanoon ki dhun (bowstring twang)
chaaron dishaon mein goonj uthi.

Devata aur Rishi aasman se yuddh dekhne aaye

Devata, Gandharva, Siddha—
sab aasman se jama ho gaye
aur achchai ki prarthna karne lage:

“Sab praniyon ki raksha ho.
Rama vijayi hon,
jaise kabhi Vishnu ne asuraon ko haraaya tha.”

Par kuch Rishi chintit the:

“Rama akela hai.
Aur saamne 14,000 rakshas!
Yeh kaise sambhav hai?”

Rama ko akele khada dekhkar
sab ka dil ghabra gaya.
Par Rama khud
Rudra (Shiva ka fierce roop) ki tarah
shant aur dridh khada tha.

Rakshas Sena ka Hamla

Tabhi, jungle ko hila dene wali
rakshas sena dikhayi di—
garajne wali aawazein,
dhanush ki tan-tan,
ghodon ki chaap,
aur rakshason ki cheekh:

“Aaj dushman ko mita do!”

Jungle ke jaanwar
darr ke maare bhaag gaye.

Rama ne apna dhanush taana
aur khule maidan ki taraf badh kar
tez awaaz mein garja—
ek awaaz jo rakshason ki vinash ka sanket thi.

Uska roop
jaise duniya ke ant ka agni ho—
tez, bhayankar,
aur rosh se bhara hua.

Rakshas sena
kale baadalon ki tarah
samaan prakat hui—
shastron, dhalon, aur rathon se chamakti hui.

Lekin un sab ke beech
Rama eklauta warrior khada tha,
tayyar—
teer chhodne ke liye,
rakshason ka ant karne ke liye.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter25
    with st.expander("Chapter 3.25 – The battle between Rama and the demons continues"):
        text1 = """
Khara jab apni sena ke saath
Rama ke hermitage ke paas aaya,
to usne Rama ko dekha—
krodh se bhara, dhanush-baana lekar khada,
bilkul ek shant par shaktishaali warrior ki tarah.

Khara ne turant
apne saarathi ko hukm diya:

“Rama tak rath le chalo!”

Saarathi veer ghodon ko
tez daudate hue Rama ke saamne le aaya.
        """
        create_image_text_layout("attached_assets/chapter3/3.25.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Rakshas Sena ka Ghera

Khara ko aage aate dekhkar
dusre rakshas bhi zor-zor se garajne lage
aur Rama ko chaaron taraf se gher liya.
Khara apne rath mein
ek chamakte sitare jaise lag raha tha—
jaise Mangal grah ke aas-paas
chamakate taare hon.

Usne hazaar teer chhode
aur ek bhayanak garajna ki.
Uske saath-saath
sabhi rakshas
apne hathiyaar—
talvaar, gade, bhale, kushli,
sab koi Rama par barsaane lage.

Unke bade-bade shareer
pahaadon ki chotiyon jaise dikh rahe the
jab ve Rama ki taraf
rathon, ghodon, aur haathiyon par chadhkar
tufaan ki tarah toot pade.

Rama ko baar-baar teer lagte hain… par ve hilte bhi nahi

Rakshason ne
Rama par pahaadon ki tarah
inaam ki baarish ki—
jaise baadal parvat par baras rahe hon.

Har taraf se
teeron aur hathiyaaron ki baarish ho rahi thi.
Rama ka poora sharir
teeron se chhed diya gaya,
aur khoon ubal kar nikalne laga—
fir bhi Rama
Himalaya jaise atal khade rahe,
zara bhi nahi hile.

Devata aur Rishi ye sab dekhkar
bahut chintit ho gaye.

Par Rama,
krodh se bhare hue,
apna dhanush tanka kar
ek baar mein sau-sau teer chhoddne lage.

Rama ke teer rakshason ko dhool chata dete hain

Rama ke teer
jaise agni ki laapton ki tarah
rakshason ke shareeron ko chhed kar
aage nikal jaate the.

Khoon se rang chhad gaye teer
aasman mein jalte mashaalon ki tarah
dikhte the.

Unke teeron ne:

rath ke ghodon ko gira diya

saarathiyon ko maar diya

haathiyon aur unke chalakon ko dharashayi kar diya

aur rakshason ke hathiyaar, dhal, dhwaj, sab toot gaye

Rakshason ke bazoo,
pehlu,
janghein,
elephant jaise mote,
sab cut kar zameen par girne lage.

Chaaron taraf sirf cheekh-pukaar hi reh gayi.

Dushana ka hamla aur rakshason ka paagalpan

Kuch rakshas,
krodh me aakar,
bade-bade bhale, trishul, aur pathar lekar
Rama par toot pade.

Par Rama ne turant
unke sir, dhal, aur dhanush
sab teeron se kaat diye.

Ve rakshas yahaan-waahan gir gaye
jaise Garuda ke pankhon ki aandhi
pedon ko girodeti ho.

Jo rakshas bache the
darr ke maare
Khara ke paas bhaag gaye.

Lekin Dushana
unhe dobara jodkar
phir Rama par hamla karne laga.
Rakshas bade saala aur tala pedon ke tan
aur bade pathar uthaakar
Rama ki taraf phenkte gaye.

Yuddh ab bilkul
dahshat bhara ho chuka tha—
kabhi lagta Rama jeet rahe hain,
kabhi rakshas.

Rama ka Gandharva Astra

Jab rakshason ne Rama ko
chaaron taraf se gher liya,
to Rama ne
bahut zor se garajkar
Gandharva Astra
apne dhanush par rakha.

Bas phir kya tha—
ek hi pal mein
hazaar teer aasman mein chamke
aur dason dishaon ko
dhak liya.

Rama itni tezi se teer chhod rahe the
ki rakshas dekh bhi nahi pa rahe the
ki teer nikle kab
aur lage kab.

Aasman andhera ho gaya
jaise surya pe koi chhaa gaya ho.

Rakshas Sena ka Vinash

Hazaaron rakshas
ek saath gir gaye—
koi kaata hua,
koi bheda hua,
koi do tukdon mein baanta hua.

Maidan bhar gaya:

sar pade the, pagdiyon ke saath

bazoo banglon ke saath

ghode aur haathi mare pade

chhatriyan, pankhe, aur dhwaj bikhar gaye

rath tukdon mein toot gaye

Jo rakshas bache
ve bhi Rama ka saamna karne ka
sahas nahi kar paaye.

Rama
us din
Pura Janasthaan ko rakshas-mukt kar diya.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter26
    with st.expander("Chapter 3.26 – Rama destroys the demons and kills Dushana"):
        text1 = """
Rama ke teeron se
jab uski poori sena bikhar gayi,
tab Dushana, bada-bada bahadur rakshas,
aage badha.

Usne paanch hazaar veer rakshason ko bulaya—
aise rakshas jo darte nahi the,
aur jo kabhi peeth dikhakar bhaag nahi sakte the.

Sab rakshas
bhale, talvaar, pathar, aur pedon ke tan (trunk) lekar
chaaron taraf se Rama par toot pade.
Par Rama ko ek bhi ghaav nahi laga.
Ve bilkul shant the,
jaise ek bada sa sandh-bail (bull)
tez baarish bhi aaram se jhel leta ho.
        """
        create_image_text_layout("attached_assets/chapter3/3.26.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Phir Rama ka krodh badh gaya.
Unhone socha:
“Aaj main Khara ki poori sena samaapt kar doonga.”

Aur phir Rama ne
teeron ki aisi barsaat ki
ki Dushana aur uski sena
poori tarah dhak gayi.

Dushana bhi peechhe nahi hataa.
Usne tez bijli-jaisi (thunderbolt-like) shakti wale
hathiyaar phainke.

Par Rama ne turant hi
ek teekh (sharp) teer se uska dhanush kaat diya,
phir uske rath ke
chaaron ghode maar diye,
aur phir ek chand-tulya (crescent-shaped) teer se
uske saarathi ka sir kaat diya.
Uske baad Rama ne
teen teer Dushana ke seene mein utar diye.

Dushana ka Ant

Dard se bhara lekin krodhit,
Dushana ne apni sunehri-gandh wali
badi si gada (mace) uthai.
Ye gada itni bhayanak thi ki
devataon ki sena tak ko mita sakti thi.
Usme lohe ke kaante lage the
aur dushmanon ka khoon laga tha.

Dushana ne us gada ko ghuma kar
Rama par hamla karna chaha.

Par jaise hi woh bhaaga,
Rama ne tez gati se
dono haath kaat diye.
Gada uske haathon se chhootkar
zameen par gir gayi
jaise Indra ka jhanda (flag) gir jaaye.

Donon haath kategaye,
Dushana ek bure haathi ki tarah
dhad se zameen par gir gaya.

Devata, Rishi aur sab prani
jo yuddh dekh rahe the,
khushi se bole:

“Shabash Rama! Bahut achha!”

Teen Bade Senapati ka Aakraman

Tab teen aur bade rakshas—
Mahakapala, Sthulaksha, aur Pramathin—
Rama par toot pade.

Mahakapala ke haath mein bada trishool tha

Sthulaksha ek bada harpoon (barchha) liye hue tha

Pramathin ek bhayanak kulhadi (axe) le raha tha

Rama unki taraf
musafir ko swagat karne jaise
shaant roop se badhe.

Phir Rama ne:

Ek hi teer mein Mahakapala ka sir kaat diya

Pramathin ko bahut saare teeron se gira diya
(jaise gira diya gaya ped)

Aur Sthulaksha ko andha kar diya
uske aankhon mein teekh teer maar kar

Phir krodh se bhare Rama ne
paach hazaar rakshason ko
paach hazaar teeron se dhool chataa di.

Khara ka Krodh

Jab Khara ko pata chala
ki Dushana aur uski saari sena mar chuki hai,
to vah gusse se kaamp uthha.

Khara garja:

“Sab rakshas milkar Rama par toot padho!
Use har hathiyaar se maaro!”

Uske saath
barah bade-bade senapati bhi aaye:
Durjaya, Karaviraksha, Parusha,
Kalakarmuka, Hemamalin, Mahamalin,
Sarpashya, Syengamin, Prithugriva,
Vajnasatru, Vihangama, Rudhinashana.

Sabhi Rama se ladne lage
aur behad achhe teer chhodne lage.

Par Rama ne
apne sone-aur-heere-jaise
chamakdar teer nikale
aur bache hue poore rakshas-dal ko
ek-ek teer se maat de di.

Rama ke teer
aag mein dhue jaise lag rahe the—
dhoomr-lepit (smoke-covered).
Unhone rakshason ko
jaise bijli bade pedon ko kaat deti ho,
waise kaat-kar gira diya.

100 ➝ 100 teer
1000 ➝ 1000 teer
har teer apni nishane par sidha laga.

Rakshason ke dhal, gehne, dhanush, sab toot gaye.
Ve khoon mein dhuul gaye the,
baal bikhre hue,
jaise yagya ke baad
kusha grass (special ritual grass)
chaaron taraf bikhar jaata hai.

Zameen par sirf laashein thi—
aur pura van
narak jaise dikhne laga.

14,000 Rakshas — Ek hi Warrior se haar gaye

Isi yuddh mein
choudah hazaar rakshas
Rama ne akela
aur paidal khada hokar
maar daale.

Sena mein ab bas do hi rakshas bache:

Khara, apne bade rath par

Trishiras, ek tez aur shaktishaali rakshas

Baaki sab ka Ram ne vinash kar diya.

Khara ka Antim Roop

Apni poori sena nasht dekhkar
Khara ne apna sundar,
ratna-jadit (gem-studded) rath chadha
aur Rama ki taraf
badi si mace (gada) uthakar
baarhta gaya.

Yuddh ka sabse khatarnak hissa
ab shuru hone wala tha…
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter27
    with st.expander("Chapter 3.27 – Rama fights Trishiras and wins"):
        text1 = """
Jab Khara gusse se Rama ki taraf badh raha tha,
tab uska sena-pati Trishiras uske paas aaya aur bola:

**“Prabhu, aap ruk jaiye.
Aapko Rama se ladne ki zaroorat nahi.
Mujhe mauka dijiye.
Main kasam khaata hoon apni talvaar ki
ki main Rama ko yahin maar doonga.

Ya to main Rama ka ant banaaunga,
ya woh mera.
Aap bas thoda sabr kijiye
aur yuddh dekhte rahiye.
Agar Rama mar gaya,
to aap vijayi hokar ghar laut sakte hain.
Agar main mar gaya,
tab aap lad lena.”**

Khara, Trishiras ki baaton se uchhal utha.
Usne kaha:
“Jao! Rama se ladho!”
        """
        create_image_text_layout("attached_assets/chapter3/3.27.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Trishiras Yuddh ke Liye Aage Badhta Hai

Trishiras, jo teen-shikhar (three crests) waale pahaad jaisa dikhta tha,
ek damakdaar rath par chadha.
Rath bahut tez aur sundar ghodon se juda hua tha.

Woh ek bade baadal ki tarah
teeron ki baarish karte hue
Rama ki taraf garajta hua badha.

Rama ne usse aate dekh kar
turant apne teekh (sharp) teer chalaaye.
Aur ek bhayanak yuddh shuru ho gaya—
jaise sher aur hathi ka takraav ho.

Teer Rama ke Mathhe Par

Trishiras ne teen barchhe (darts)
Rama ke mathhe par ghusa diye.
Khoon nikla, par Rama krodh se garaj uthhe.

Rama bole:

“O bahadur rakshas!
Tumhare teer main apne mathhe par
phoolon ki mala (wreath) ki tarah dharan kar raha hoon.
Ab tum bhi mere teeron ka swaad (taste) chakho!”

Rama ka Prabal Prati-Hamla

Rama ne chaudah saanp-jaisi teeron (serpentine arrows) se
Trishiras ke seene ko chhed diya.

Fir:

4 teeron se uske rath ke 4 ghode gira diye,

8 teeron se saarathi ko maar diya,

Aur 1 teer se rath ka badaa jhanda kaat diya.

Trishiras ka rath bilkul toot chuka tha.
Jab woh neeche utar raha tha,
Rama ne aur teer uske seene mein utaar diye.
Trishiras behosh jaisa ho gaya.

Phir Rama ne
ek hi jhatke mein
apne tez teeron se
Trishiras ke teenon sir kaat diye.

Khoon dhaar ki tarah behne laga
aur Trishiras ka bada shareer
seedha khada ka khada gir gaya.

Rakshason ka Bhaag Jaanaa

Ye drishya dekh kar
baaki rakshason ka hausla toot gaya.
Woh hiran ke jhund ki tarah
dar kar bhaag gaye.

Khara ne unhe bhaagte dekha
aur uska krodh phir se bhadak utha.

Gusse se kaamp kar
woh Rama par aisa tuta
jaise Rahu grahan ke samay chaand par toot padta hai.

Yuddh ka sabse bhayanak hissa
ab shuru hone wala tha…
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter28
    with st.expander("Chapter 3.28 – Rama fights the demon leader Khara"):
        text1 = """
Dushana aur Trishiras ke mar jaane ke baad,
Khara ne Rama ki shakti dekhi
aur uske man mein dar utthaa.

Woh socha:

“Meri poori sena,
mere do bade sena-pati—Dushana aur Trishiras—
sab Rama ne akela hi maar diye.”

Dar aur gusse ke beech,
Khara ne apna maansik santulan (balance) kho diya
aur woh Rama par toot pada
jaise Namuchi (एक prachin rakshas) Indra par toot padta tha.
        """
        create_image_text_layout("attached_assets/chapter3/3.28.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Khara ka Pratham Hamla

Khara ne apna mahaan dhanush taana
aur khoon peene wale teer (blood-sucking arrows)
Rama par barsa diye.
Teer zehreeli sapolon jaisa dikhta tha.

Rath par khada Khara
charon dishaon mein teer chalata
aur apni yuddh kala (battle skill) dikhata hua
Rama ke aas-paas chakkar kaatne laga.

Rama ka Jawab – Aasmaan Teeron Se Bhar Gaya

Rama ne bhi apna bada dhanush uthaya
aur aag jaisi chamak wale teer chalaaye.
Aasmaan, dhaarti, har disha—
sab teeron se bhar gayi.
Din dopahar mein hi andhera sa chha gaya.

Rama ne Nalika, Naracha,
aur Vikarna (different arrow types) jaise teer chalaaye
aur Khara ko baar-baar maarte rahe.

Khara rath par khada
apne dhanush ke saath
mrityu (death) jaisa lag raha tha.

Khara ne socha Rama thak gaya hai,
lekin Rama bilkul majboot khada tha—
jaise sher ko ek kamzor hiran chhed bhi de
to sher hilega bhi nahi.

Khara Ka Tez Prati-Hamla

Khara ne pura zor laga kar
Rama ke dhanush ko beech mein kaat diya
aur phir 7 gadha-jaisi (mace-like) teer chalaaye
jo Indra ke vajra (thunderbolt) jaise the.
Un teeron se Rama ka kavach (armour) toot kar neeche gir gaya.

Khara garaj kar
1000 teer chalaata raha
aur Rama khoon se dhak gaye
par unki himmat nahi tooti.

Rama aur Vaishnava Dhanush

Rama ne turant doosra dhanush uthaya—
Vaishnava dhanush (a divine bow given by Agastya).

Uske taar ki aawaz se
poora van (forest) goonj utha.

Rama ne sunehre pankh wale teer
Khara par barsa diye
aur uska sunehri jhanda gira diya—
jaise surya grahan ke samay andhera gir padta hai.

Khara ne gusse se Rama ke hriday (heart) mein
4 teer ghusa diye.
Rama khoon se bheeg gaye
jaise baarish mein bheega hathi.

Par Rama ka krodh bhi ab bhadak gaya.

Rama ka Vinashkari Teer-Baaz

Rama ne:

1 teer se Khara ka sir jhatka

2 teeron se uske dono baazu kaategaye

3 crescent-shaped dakshin teeron se uska seena chhed diya

4 teer se rath ke ghode giraaye

1 teer se saarathi gira diya

3 teer se rath ka dhacha (axle) tod diya

1 teer se Khara ka naya dhanush bhi kaat diya

Aur phir
13vaan teer,
jo bijli jaisa chamak raha tha,
seedha Khara ke shareer mein ghus gaya.

Khara ka rath toot gaya,
ghode mare gaye,
saarathi gir gaya—
ab woh sirf ek mace lekar
dharti par akela khada tha.

Devon ka Utsah

Ye drishya dekh kar
Deva, Rishi sab aasmaan mein jama ho gaye
aur bole:

“Wah Rama!
Kya adbhut parakram (extraordinary courage)!
Tumhari jai ho!”

Sab ne haath jod kar
Rama ko pranam kiya.

Yuddh ab apne antim charan mein pravesh karne wala tha…
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter29
    with st.expander("Chapter 3.29 – Rama and Khara challenge each other"):
        text1 = """
Khara ab akela tha—
na rath, na ghode,
sirf ek mace (gada) haath mein.

Rama ne usse kathor (strict) awaaz mein kaha:

Rama Khara ko dant-te hue

“Khara!
Tumhara poora jeevan galat kaam mein gaya hai.
Tumne hathi, ghode, rath aur poori sena ki shakti lekar
dunyā ko dukh hi diya hai.

Jo log doosron ko satate hain,
jo nirdai (cruel) hote hain,
unhe kabhi sukh nahi milta,
chahe woh teenon lokon ka raja kyon na ban jaayein.”
        """
        create_image_text_layout("attached_assets/chapter3/3.29.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Rama fir bole:

“Jo saanp jaisa dusht hota hai,
jo bina soche samjhe logon ko nuksaān pahunchata hai,
woh aakhir mein khud hi barbaad hota hai.”

Rama ne uske bure karmon ko yaad dilaya:

“Tumne Dandaka ke sadehuon ko maar daala—
aur bina wajah!
Aise paap ka phal hamesha kadwa hota hai.”

Rama ne fir doosri misaal di:

“Jaise ped apne samay par phool deta hai,
waise hi bure karm apna phal dete hi dete hain—
aur woh phal bahut kadwa hota hai.”

Rama ne apne teer uthaaye aur kaha:

**“Aaj mere teer tumhare shareer mein aise ghusenge
jaise saamp bill mein ghusta hai.

Tum bhi un sadaiv ke liye chale jaoge
jinhe tumne maar daala.

Woh sab Rishigan,
apne vimaanon (flying chariots) se
neeche dekh kar
tumhe nark mein girta hua dekhenge.”**

Aur phir Rama garje:

“O burai ki misaal Khara!
Aaj main tumhara sir,
taad ke phal ki tarah,
ek hi teer se gira doonga.”

Khara ka gussa—taana maarte hue jawaab

Rama ki baaton se Khara ka khoon khol gaya.
Aankhon se aag nikal rahi thi.

Woh hans kar bola:

**“Rama! Tum ek aam insaan ho.
Bas kuchh chhote-mote rakshason ko maar diya
aur khud ko mahaan samajhne lage?

Asal yoddha kabhi apni tareef nahi karta.
Sirf kamzor log apne aap ko baadh chadha kar batate hain.”**

Khara ne Rama ka mazaak udaya:

“Tumhara yeh ghamand
ussi tarah hai
jaise peetal ko sone jaisi polish kar di jaaye—
aag mein jaa kar asli aukaat pata chal jaati hai.”

Phir woh garja:

“Main yahan pahaad ki tarah mazboot khada hoon.
Mere haath mein gada hai, maut ka phanda!
Aaj tumhe hi nahi,
teenon lokon ko hila dunga!”

Par fir Khara ruk gaya aur bola:

“Bahut hua bolna.
Surya ast hone wala hai.
Aao, yuddh khatam karte hain.
Tumne 14,000 rakshason ko maara—
aaj tumhari maut se unke parivaar ka dard mitt jayega!”

Khara ka Mahan Mace-Hamla

Gusse se bhar kar
Khara ne apni sunehri gada
poori taqat se Rama par phenki.

Gada bijli jaisi chamak rahi thi.
Niche ped-paudhe jalkar raakh ho gaye
jaise woh guzarti hui aayi.

Wo gada bilkul Rama ke upar aakar girne hi waali thi—
jaise maut ka phanda.

Par Rama ne ek second bhi na khoya.

Unhone teer ka taana liya
aur hawaa mein hi
ek ke baad ek arrow chala diye.

Teeron ne us gada ko
tabahi ke dhamaake ke saath
beech mein hi
chur-chur kar diya.

Gada tukdon mein toot kar
aise gir padi
jaise koi zehreela saamp
jadibootiyon ki shakti se mar gaya ho.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter30
    with st.expander("Chapter 3.30 – Khara is killed by Rama"):
        text1 = """
Rama ne Khara ki bada-badi (boasting) aur uski gada (mace) ko
apne teeron se hawa mein hi tod diya tha.

Ab bhi gusse mein the,
par phir bhi halka sa mazaak karte hue बोले:

Rama ka Teekha Jawaab

“Khara!
Bas itni hi shakti thi tummein?
Pehle itna shor, aur ab yeh haal!

Meri teeron ne tumhari gada ko
zameen par tukde-tukde kar diya.
Aur tum keh rahe the
ki tum apne logon ka badla loge?

Yeh sab hawa mein baatein thi.”

Rama fir बोले:
        """
        create_image_text_layout("attached_assets/chapter3/3.30.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
**“Jaise Garuda ne kabhi amrit (nectar of immortality) chura liya tha,
waise hi main tumse aaj tumhari jaan chheen loonga.

Aaj zameen tumhare gale se nikle huye khoon ko pi legi.
Tum mitti par gir jaoge,
haathon ko failaakar,
jaise koi pagal premi apni jeeti hui patni ko gale lagaata hai.”**

Rama fir uske paap yaad dilate hain:

**“Dandaka van aaj azaad hoga.
Sadhus bina darr ke ghoomenge.
Aaj tumhare jaise dushton ka ant hoga.

Tumhari rakshasi patniyan roti hui bhaagengi.
Jinhone dusron ko daraaya,
aaj woh khud dard mehsoos karengi.”**

Khara ka Jawaab — Gusse se Bhara Hua

Rama ki baaton se Khara aur bhi pagal ho gaya.
Usne cheekh kar kaha:

“Rama! Tum ghabra gaye ho.
Maut saamne ho to insaan
sahi-galat bhool jaata hai.
Tumhari zubaan bhi hil rahi hai!”

Khara ne charo taraf dekha
aur paas ka ek bada taad ka ped (palm tree) ukhaad liya.

Poore zor se ped ko ghuma kar
woh Rama par chillaaya:

“Ab tumhari maut pakki hai!”

Rama ka Badla

Par Rama ne turant apna teer uthaya
aur ped ko bhi
hawa mein hi
chote-chote tukdon mein kaat diya.

Ab Rama ke gusse ki seema toot gayi.

Unka shareer paseene (sweat) se bhara tha,
aankhen laal,
par mann bilkul shaant aur tayyar.

Unhone teer pe teer barsa diye.
Khara ke jism se khoon behne laga,
jaise pahad se paani beh raha ho.

Khara khoon ki badboo se aur pagal ho gaya
aur Rama ki taraf dauda.

Rama thoda peechhe hatega,
phir rukkar
ek khaas teer nikaala—

woh teer jo aag ki laal jalti lau jaisa chamak raha tha.

Yeh teer
Rishi Agastya ko Indra ne diya tha,
aur Agastya ne Rama ko.

Rama ne dhyaan se dhanush tana
aur woh teer seedha Khara ke dil par chala diya.

Teer bijli (thunderbolt) ki tarah laga
aur Khara
aag se jala hua
zameen par gira.

Bilkul vaise hi
jaise kabhi Andhaka naam ka rakshas
Shiva ke ghayal drishti (third eye) se jal gaya tha.

Devaon ki Prashansa (Praise)

Khara ki maut ke saath hi
aasmaan phoolon se bhar gaya.

Devta, Gandharv, Caran
sab ne bajaaye nagade
aur bola:

“Rama ne ek pal mein
14,000 rakshason ko maar diya!
Dushana, Trishiras aur Khara sab gaye.
Yeh Rama ki shakti Vishnu jaisi hai.”

Sab Devata wapas chale gaye,
khush aur aashirwaad dete hue.

Rishiyon ka Aashirwad

Rajarishi, Paramarishi
aur Rishi Agastya bhi aaye.

Unhone Rama ko pranam kiya aur bola:

**“Rama, tumhara yeh aana
hamare liye vardaan (blessing) tha.

Ab Dandaka van mein
koi asur rahenge hi nahi.
Sadhus bina dar ke tapasya (penance) kar sakenge.”**

Lakshmana aur Sita ka Milan

Sita aur Lakshmana,
jo pahad ki guha (cave) mein the,
bahar aaye.

Lakshmana ne Rama ko pranam kiya.

Aur Sita—
apne vijayi (victorious) pati ko dekhkar
khushi se unhein gale laga liya.

Rama ne ascetics ka dukh door kiya tha.
Sita ke chehre par shuddh khushi thi.

Woh baar-baar Rama ko apna pyaar jatati rahi—
poori tarah sukh aur shaanti se bhari hui.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter31
    with st.expander("Chapter 3.31 – Ravana hears about Khara’s death and becomes furious"):
        text1 = """
Janasthana se ek rakshas
Akampana
bahut mushkil se bachkar
seedha Lanka pahunch gaya.

Ravana ke saamne aakar woh bola:

“Hey Maharaj,
Janasthana ke saare rakshas mar gaye.
Aur Khara bhi maar diya gaya.
Main kisi tarah jaan bachakar yahaan aaya hoon.”
        """
        create_image_text_layout("attached_assets/chapter3/3.31.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Ravana ka Gussa

Yeh sunte hi
Ravana ki aankhen khoon jaisi laal ho gayi.

Gusse se jalte hue bola:

**“Kaun hai woh?
Kisne mere logon ko chhua tak?
Chhua nahi — maar diya?

Uska jeena mushkil ho jayega.
Indra ho, Vishnu ho, Yama ho—
koi nahi bacha payega.

Main hi samay hoon!
Main hi vinash hoon!”**

Akampana dara hua tha.
Haath jodkar khada raha.

Ravana ne use shaant kiya aur bola:
“Bol. Sach bata.”

Akampana ka Sach — Rama ka Parichay

Akampana ne himmat jutakar bola:

**“Maharaj…
Uska naam hai Rama.

Dasharatha ka beta.
Bahut veer.
Bahut sundar.
Bahut takatwar.

Usne khud hi, akela hi,
Khara aur Dushana ko maar diya.”**

Ravana ne poocha:

“Kya Devta uske saath the?”

Akampana ne jawab diya:

**“Nahi Maharaj,
koi Devta nahi.
Woh akela hi tha.

Uske teer
hawaa mein udkar
jaise paanch sir wale saanp ban rahe the.

Jidhar rakshas bhaagte—
wahan Rama pahle se khada hota.”**

Ravana garja:

“Main jaaunga!
Main khud Rama aur Lakshmana ko maarunga!”

Akampana ki Salah — Rama ko ek hi jagah chot lag sakti hai

Akampana ne dara hua kaha:

**“Maharaj, ek baat suno.
Rama ko koi hara nahi sakta.
Na Devta, na rakshas, na dono milkar bhi.

Par ek raasta hai…

Rama ki patni hai Sita.
Bahut sundar.
Apsaron se bhi zyada.
Agar aap Rama ko jungle mein uljha do
aur Sita ko chura lo—

Rama jee nahi payega.”**

Yeh sunkar
Ravana ko pehli baar
khushi mili.

Woh bola:

“Theek hai.
Kal hi main Sita ko lekar
Lanka laaunga.”

Ravana Marica se Madad Maangne Jaata Hai

Agle din Ravana
apni chamakti hui rath mein baitha
aasmaan sa chamakta hua
Marica ke ashram pahucha.

Marica ne unka swaagat kiya:
khana diya, paani diya,
aur poocha:

“Maharaj, sab theek toh hai?
Aap achanak kaise aa gaye?”

Ravana ne kaha:

**“Rama ne Janasthana me
mere sab log maar diye.

Mujhe Sita ko churaana hai.
Tum madad karo.”**

Marica ki Darbhari Chitavni (Warning)

Marica sunte hi ghabra gaya.
Woh bola:

**“Maharaj!
Jisne aapko yeh salaah di hai,
woh aapka dushman hai —
dost nahi.

Rama ko sehna mushkil hai.
Woh ek soye hue sher jaisa hai.
Aap usse panga loge
toh Lanka khali ho jayegi.

Sita ko churaana
aise hi hai
jaise nange haath se
zehreeli saanp ka daant nikaalna!

Aap laut jaiye.
Rama aur Sita
van mein khush rahein,
aap Lanka mein khush rahein.”**

Ravana ne Marica ki baat toh sun li
par kuch boli nahi.

Phir apne mahal wapas chala gaya…
dil mein ek hi baat lekar—
Sita.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter32
    with st.expander("Chapter 3.32 – Shurpanakha tells Ravana to take revenge on Rama"):
        text1 = """
Jab Shurpanakha ne dekha
ki Rama ne akela hi
chaudah hazaar rakshason ko maar diya—
saath hi Khara, Dushana, Trishiras ko bhi—
toh woh fir se cheekh uthi.

Darr se nahi —
gusse se, dukh se.

Bijli ki tarah garajti hui
woh seedha Lanka ki taraf bhaagi.
        """
        create_image_text_layout("attached_assets/chapter3/3.32.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Ravana apne Raj-Singhasan par

Lanka pahunchkar
Shurpanakha ne apne bade bhai Ravana ko dekha—

Sone ke singhasan par baitha,
chaaron taraf mantri,
aur lag raha tha jaise
Indra apne Dev-mantriyon ke beech ho.

Dus sir, bees baahin,
gehne, mukut,
tez aisi ki aankh chundhiya jaye.

Purane yuddhon ke nishaan—
Vishnu ke chakra ki chot,
Airavata ki daat ke nishaan—
par fir bhi sab thik-thak,
jaise loha ko kuch na ho.

Yeh Ravana wohi tha
jo pahadon ko utha leta tha,
jo suraj-chaand ka raasta rok deta tha,
jo samundar hila deta tha,
jo devlok ki bagiche tod deta tha,
aur jisko dev, danav, saap—
koi maar nahi sakta tha,
kyunki use boons (vardaan) mile the.

Bas…
insaan ka zikr vardaan mein nahi tha.
Usne khud manushyon ko halka samjha tha.

Shurpanakha ka Ravana ke Darbaar mein Aana

Shurpanakha
jo kabhi kisi se nahi darti thi,
ab dar ke maare kaamp rahi thi.

Nose aur ears kategaye the,
chehra barbaad ho chuka tha.

Ravana ki aankhen
aag jaisi chamak rahi thi,
jaise turant kisi ko jala de.

Shurpanakha dheere-dheere
singhasan ke paas gayi—
aur apna dard,
apni beizzati,
apna gussa
sab kuch uske saamne rakh diya.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter33
    with st.expander("Chapter 3.33 – Shurpanakha warns Ravana about Rama"):
        text1 = """
Shurpanakha
gusse se kaamp rahi thi.
Uska chehra bigad chuka tha,
dil dard aur badle se bhara tha.

Ravana,
jo duniya ko sataane wala,
dass sir wala rakshas raja tha—
aaj uske saamne
uski chhoti behen
khadi thi,
aur uski zubaan
tez talwar jaisi thi.
        """
        create_image_text_layout("attached_assets/chapter3/3.33.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Shurpanakha ka gussa phoot padta hai

“O Ravana!
Tu bas mazaa,
naach-gaana,
aur apni ichchha mein hi laga rehta hai.

Tujhe pata bhi hai
kitni badi musibat tere sar par aa rahi hai?

Jo raja
sirf apni chaah mein beh jaaye,
bhog-vilas mein dooba rahe,
usko toh praja
waise hi nafrat se dekhti hai
jaise shav-daan mein jalti aag ko.”

Raja ki zimmedaari bhi hoti hai

“Jo raja
apna kaam waqt par nahi karta,
samay pe dhyaan nahi deta,
wo apne hi raaj ko barbaad kar deta hai.

Jo raja
apni ranion ke kehne pe naachta ho,
gairon ki baaton mein jaldi aa jaata ho,
usse log door bhagte hain—
jaise haathi
kichad bhare nadi ke paani se door hota hai.”

Shurpanakha ka aur bhi dana hua gussa

“Tu
devtaon se dushmani rakh raha hai,
gandharvon se jhagda,
danavo se jhagda,
aur phir bhi khud par garv karta hai?

Arre!
Tu toh bachche jaisa be-soch samajh hai!
Tu kaise raja ban sakta hai?

Ek raja ke paas
jasoos (spies),
buddhi,
dhan,
aur neeti honi chahiye.

Tere paas kya hai, Ravana?”

Sachchai jo Ravana ko chubhi

“Janasthaan mein
chaudah hazaar rakshas
Rama ne akela maar diye!
Khara, Dushana sab khatam!
Rama ne sabhi tapasviyon ka dar mita diya,
jabki tu—
RAJA hoke—
soya hua baitha hai!

Tu bas lalach mein,
sukh-bhog mein uljha hai,
aur tujhe pata bhi nahi
ki tera raaj khatre mein hai!”

Ravana par thokar pe thokar

“Jo raja
matlabi ho,
krodhi ho,
dikhawa karta ho,
aur apni hi tarif karta ho—
usse toh uske apne log hi
kabhi bhi hataa sakte hain.

Jo raja
khatre ke samay aankh bandh kar le,
wo toh tinke ki tarah
apne hi raaj se bahaa diya jaata hai.”

Ant mein Shurpanakha ka kathor faisla

“Dry lakdi ki kuch keemat hoti hai,
mitti ki bhi,
par ek bigda hua raja
kisi kaam ka nahi hota!

Jo raja
samvedansheel ho,
hoshiyaar ho,
hamesha jaagta ho—even jab sota ho—
uska raaj kayam rehta hai.

Par tu, Ravana…
tu ne kuch bhi nahi seekha.

Tu sirf indriyon ka gulaam hai.
Tu sahi- galat samajhne ki akal kho chuka hai.
Aise hi tu
apna raaj gawa dega.
Aur phir khud barbaad ho jaayega.”

Ravana chup… sochta reh gaya

Shurpanakha ke kathor shabdon ne
Ravana ka dil hila diya.

Woh…
darr gaya nahi,
par
soch mein doob gaya.

Bohot gehri,
chubhne wali baatein
usne kabhi nahi suni thi.

Aur iss shabd-vaar (word-attack)
ne uske dimag mein
badle ki chingari bhadka di.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter34
    with st.expander("Chapter 3.34 – Shurpanakha tells Ravana to kill Rama and marry Sita"):
        text1 = """
Ravana,
apni behen ke tez shabdon se
gusse mein aa gaya.
Apne mantriyon ke beech baithkar
usne garajte hue poocha:

“Kaun hai yeh Rama?
Kitna balwan hai?
Kaisa dikhta hai?
Usne kaise jungle ke itne gehre hisse mein
kadmon rakhe?

Aur kaise?
Kaise usne Khara, Dushana, Trishiras ko
akela maar diya?

Aur…
tumhe kisne bigaada?
Tumhari yeh haalat kisne ki?
Sach sach batao!”
        """
        create_image_text_layout("attached_assets/chapter3/3.34.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Shurpanakha ka dard aur gussa phoot padta hai

Shurpanakha,
gusse se kaampti hui,
Ravana ko Rama ka poora kissa sunati hai.

“Rama, Raja Dasharatha ka beta—
wo dekhne mein Kaamdev (God of Love) jaisa sundar hai.
Uske baahu lambi,
ankhien badi aur kamal ke patton jaisi.

Bark ke kapde (tree-bark clothes) pahne hue,
kaale mriga-charm (antelope skin) mein,
sunehri kinari wala dhanush pakde,
wo aisa lagta hai
jaise Indra ka apna dhanush lekar khada ho.

Jab wo teer chhodta hai,
to aawaaz bijli jaisi hoti hai.
Uske teer zehreele saanp (poisonous snakes) lagte hain.”

Rama ki yuddh-shakti ka bayan

“Main ne apni aankhon se dekha,
kaise uske teeron ki baarish
hamare rakshason ko
dhool ki tarah uda rahi thi—
jaise Indra ki oley (hailstorm) ki maar
khet barbaad kar deti hai.

Sirf kuch hi palon mein
Rama ne chaudah hazaar rakshas
akela hi maar diye!
Khara, Dushana—sab khatam!

Jangal ke tapasviyon ko
usne dar se azaad kar diya.”

Lakshmana ka zikr

“Lakshmana—
uska bhai—
bahut veer (brave) aur bahut imaandaar hai.
Woh Rama ke liye
jaan bhi de de.
Tez, buddhimaan,
aur hamesha sajag.
Sach kahun,
wo Rama ki doosri saans (life’s breath) jaisa hai.”

Aur phir… Sita ka varnan

“Par sabse adbhut…
Sita hai.

Uska chehra poornima ke chaand jaisa.
Aankhen badi,
baal komal (soft),
naak shobha-dar (beautiful),
kandhe sundar,
aur chalne ka andaaz
jaise swarg ki koi devika (celestial maiden).

Uski twacha
pighle hue sona (molten gold) jaisi chamakti hai.
Uske naakhun
gulabi aur komal.

Sita jaise sundar stri
na devtaon mein,
na gandharvon mein,
na yakshon mein,
na kinneron (celestial beings) mein—
kahin nahi milti.

Wahi Sita—
Rama ki patni.”

Shurpanakha ki khatarnaak salaah

“Ravana!
Jo bhi Sita ko pa lega,
aur jisey Sita gale lagayegi,
wo duniya ka sabse sukhhi aadmi ban jayega—
Purandara (Indra) se bhi adhik!

Tu aur Sita—
dono ek doosre ke laayak ho.
Uske ghoonghat ke peeche chhupa
chehra dekhkar
tera dil pighal jayega.

Isliye,
agar tu chaahta hai
ki Sita teri ho—
to jaldi se nikal yahan se.
Use chura le!

Main to usse
tere liye hi laane wali thi…
par Lakshmana ne mujhe bigaad diya,
mujhe kaat diya!”

Ant mein Shurpanakha ka bhadkaane wala sandesh

“Ravana!
Rama ne tumhare Janasthaan ke rakshason ko maar diya.
Khara aur Dushana jale padhe hain.

Ab tera farz banta hai
ki tu kuch kare.

Sita ko le aa,
uski khoobsurti ka raj tum dono share karo—
aur Rama ko dard mein tadapne do!”
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter35
    with st.expander("Chapter 3.35 – Ravana visits the demon Marica again"):
        text1 = """
Shurpanakha ki baatein sun kar
Ravana ka badan kaap utha.
Usne turant apne mantriyon ko vidā kar diya
aur akela baithkar sochne laga—
“Kya karna chahiye?
Kya nahi karna chahiye?”

Lambe vichaar (deep thinking) ke baad
uska mann ek hi faisle par aa rukka—
“Yehi karna hoga!”

Aur bina kisi ko bataye,
woh chupke se apne mahaan rath-mandap (royal chariot hall) ki taraf gaya
aur rath-saarthi (charioteer) ko hukm diya:
“Mera rath taiyaar karo!”
        """
        create_image_text_layout("attached_assets/chapter3/3.35.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Ravana ka shandar rath

Charioteer ne pal bhar bhi na lagaya.
Turant ek adbhut, sone se saja hua rath
Ravana ke saamne laa khada kiya—
ek aisa rath jo kahin bhi
mann ki ichha se
uda ke pahunch sakta tha.

Us rath ko khoobsurat mules (strong horse-like animals) khinch rahe the,
jinhe sunehri sajawat mili hui thi
aur unke siron par bhoot-jaisi (goblin-like) shakal bani thi.

Ravana,
apne das sar (ten heads)
aur bees baahein (twenty arms) ke saath,
chupe hue bijli-chamak (lightning) jaise tej se chamak raha tha.
Safed chatra (white royal umbrella),
safed pankhe (chanvaras),
aur neele laajawart (lapis-lazuli) jaisi chamak uske chehron par—
wo ek ajeeb, darawana,
par shahi nazara ban gaya.

Uska rath samundar ke kinare se tez gati se guzarne laga,
aawaz bijli ki ghadghadahat (thunder) jaisi.

Samundar kinare ke drishya

Ravana ne raste mein
bahut sundar aur adbhut drishya dekhe—

bade bade pathar,

phoolon se lade hue vriksh,

saaf paani ke talab,

jahan hansa, bagule, aur jal-pakshi khel rahe the,

coconut, sala, tala, tamala ke jhund,

sandalwood (chandan) ke ghane jungle
jinke jadon se sugandhit ras (fragrant sap) beh rahe the.

Usne un pavitra jagon ko bhi dekha
jahan bade-bade Rishi, Nag, Gandharva,
Kinnera (celestial musicians),
aur tapasvi (ascetics) reh kar tapasya karte the.

Kahin-kahin apsarayein
sangeet aur nritya se sabko mohit (enchant) kar rahi thi.

Ravana ne pahaadon jaise upar uthte
moonga (coral) aur motiyon ke dher,
sunehri kanoon (golden shores)
aur chandi ki chatanen bhi dekhin.

Nyagrodha ka vishal vriksh

Ravana ek aisi jagah par pahucha
jahan samundar ke kinare
ek bahut bada vad vriksh (fig tree) tha,
jisey log Subhadra kehte the.

Yeh wahi vriksh tha
jiski daali Garuda (divine eagle) ne
kabhi ek haathi aur ek kachhua pakad kar
door le jaate hue tod di thi.

Us daali ko udaate hue
Garuda ne anyay se pishe hue Rishiyon ko bachaya tha
aur fir Amrit (nectar of immortality) churaane ka sahas (courage) bhi kiya tha.

Ravana ne iss itihaas-prasiddh (historically famous) vriksh ka darshan kiya
aur aage badha.

Marica ka tapasvi ashram

Samundar ke doosri taraf
Ravana ne ek shaant aur purana ashram dekha—
jungle ke beech ek nirjan (lonely) jagah.

Wahan tha Marica,
tare-tare se door,
kaale mriga-charm (black antelope skin) pehne,
jata-joot (matted hair) baandhe,
aur tapasya mein laga hua.

Ravana ko dekh kar
Marica ne bada satkaar kiya—
pavitra jal,
safed bhojan,
aur param aadar (respect) se bhara swagat.

Phir jhuk kar poocha:

“Lanka mein sab theek hai na, Maharaj?
Aap itni jaldi dobara kyon aaye?”

Ravana ka uttar

Ravana,
apni sehatmand, gajjati (booming) awaaz mein
bada bhari uttar deta hai—

(Jaisa original ka next part keh raha hai.)
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter36
    with st.expander("Chapter 3.36 – Ravana tells Marica his plan"):
        text1 = """
Ravana ne gahri saans li
aur Marica se bola:

“O Marica, dhyaan se suno!
Mere dil par bahut bhaari dukh hai.
Aur tum hi ho jo is dukh ko halka kar sakte ho.”

Janasthana ki baat

Ravana ne kaha:

“Tum Janasthana ko jaante ho.
Wahin mere bhai Khara,
uska sahayak Dushana,
meri behen Shurpanakha,
aur shaktishaali Trishiras,
aur hazaaron rakshas
mere kehne par rehte the.

Woh sab Rishi–muniyon ko
tang karte the,
darate the,
aur jungle ko apni marzi se chalate the.

14,000 rakshas the—
sabke sab bahadur,
shastron (weapons) mein nipun (skilled),
raat ke andhere mein ghoomne wale.

Lekin…
ek din woh sab
Rama se takra gaye.”
        """
        create_image_text_layout("attached_assets/chapter3/3.36.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Rama ka apratima bal (unbelievable strength)

“Ek shabd tak na bole
aur eklaute (single-handed)
aur paidal (on foot) ladte hue
Rama ne sabko mita diya!

Haan Marica,
14,000 rakshas — ek ke baad ek — gir gaye
Rama ke teer lagte hi.

Khara mar gaya.
Dushana mar gaya.
Trishiras bhi mita diya gaya.

Aur iske baad
Dandaka ka jungle shaant ho gaya.”

Ravana ka gussa

Ab Ravana ki aawaz
jale hui lakdi jaisi garam ho gayi—

“Rama…
jisey ek raja ne
naraz hokar vanvaas bhej diya,
wo laayak hi nahi kshatriya (warrior) kehlaane ka!

Wo jhagdalu,
badtameez,
aur sirf apni ichha ka ghulam hai.

Aur usne meri behen—
Shurpanakha—
ke kaan aur naak kaat diye!
Bina kisi wajah ke!”

Ravana ki aankhen lapakti aag jaisi
laal ho gayin.

Ravana ka bhayanak plan

Phir Ravana ne dheere se kaha:

“Isliye main ne faisla kiya hai —
Main Sita ko chura lunga.
Force se.
Zabardasti.

Woh dev-kanyaa jaisi sundar hai.
Aur uska Ram se door hona hi
Rama ki maut banega.”

Ravana ne Marica ki aankhon mein dekh kar bola:

“Marica…
tum jaadu (magic) jaante ho.
Tum bahadur ho.
Tum hoshiyar ho.

Meri madad karo.”

Marica ka kaam — Sunehri Hiran

“Tum ek sunehri hiran
(golden deer) ka roop dharan (take form) karna.

Chamakdar,
khubsurat,
jise dekh kar koi aankh na hata sake.

Sita tumhe dekhegi
aur turant kahegi:
‘Rama, is hiran ko pakdo!’

Tab Rama aur Lakshmana
door chale jayenge.

Aur jab Sita akeli reh jayegi—
main usse le jaaunga
jaise Rahu
chaand ko nigal leta hai.”

Ravana ka chehra
garv aur paagal khushi se chamak raha tha.

Marica ka dar

Yeh sab sunte hi
Marica ka rang udd gaya.
Uski aansu-sookhi zubaan (dry tongue)
honthon par phisal gayi.
Aankhen ek hi jagah jam gayin
jaise kisi mrityu-sann (half-dead) vyakti ki.

Use pata tha
Rama se panga lena
apni maut ko bulaane jaisa hai.

Darr se kaapte hue
haath jod kar
usne Ravana se kaha—
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter37
    with st.expander("Chapter 3.37 – Marica tries to stop Ravana from doing wrong"):
        text1 = """
Marica ne Ravana ki baat dhyaan se suni
aur dheere se bola:

“O Raja, meethi baatein (flattery) karne wale log bohot mil jaate hain,
par sach aur kadvi (bitter) baat kehne wale
bahut kam hote hain.

Aur jo sach main kehne ja raha hoon…
woh tumhe pasand nahi aayega.”

Rama ka asli bal (true power)

Marica ne kaha:

“Tum Rama ko jaante hi nahi,
isliye unhe halka samajh rahe ho.

Rama ki shakti
Indra aur Varuna (rain-god) jaisi hai.

Tumhari jasoosi (spies) bhi kamzor hai.
Issi liye tumhe pata hi nahi
ke Rama ki gussa (wrath)
poori rakshas-jati (demon race) ko khatam kar sakta hai.

Aur Sita...
Sita hi tumhari barbaadi ka kaaran ban sakti hai.”
        """
        create_image_text_layout("attached_assets/chapter3/3.37.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Lanka ka bhavishya (future)

“Ravana,
tum apni ichhaon (desires) ke gulaam ban chuke ho.
Aise raja ka raaj kabhi sukoon se nahi tikta.

Jahan raja hi asantulit (unrestrained) ho,
wahan praja aur raajya
dono khatre mein hote hain.

Tumne Rama ke baare mein jo suna
wo sab jhooth hai.”

Rama ka charitra (character)

“Rama apne pita ki agya (order) se vanvaas gaye.
Woh wafadar (loyal),
dharma-palak (upholder of duty),
aur sabke hit mein rehne wale hain.

Na woh lobhi (greedy) hai,
na hi kathor (cruel).
Woh kabhi bina wajah
kisi ko dukh nahi dete.

Vaidehi, yaani Sita,
apni pavitrata (purity) se
Rama ki raksha karti hai —
jaise Prabha (light) Surya ki raksha karti hai.

Aisi pativrataa (faithful wife),
tum jaise kisi ko
kabhi bhi haath nahi aane wali.”

Rama se dushmani = Atma-ghaat (self-destruction)

“Ravana,
Rama se panga mat lo.

Unka dhanush (bow)
aur unke teer
aag ki laapte (flames) jaise hain.

Tumhare jitne bhi guroor (pride) ho,
Rama se takrana
sirf tumhari maut ko bulana hoga.

Aur Sita ko chherne ki baat…
yeh to bilkul aag me haath dalne jaisa hai.”

Sita ka apaharan (kidnapping) = Nash (destruction)

“Janaka ki beti Sita,
Rama ke jeevan se bhi zyada
unke liye pyari hai.

Tum usse alag nahi kar sakte —
jaise jalti angithi (brazier) se
aag ko alag nahi kiya ja sakta.

Rama tumhe dekh lenge,
toh tumhari Lanka,
tumhara raaj,
tumhari zindagi—
sab mit jayega.”

Marica ki aakhri vinati (final plea)

“Isliye, O Raat ke Raja,
apni jaan,
apna raajya
aur apni khushi bachani hai
toh yeh paagalpan mat karo.

Wise logon se salaah lo—
jisme Bibishana sabse pehle ho.

Socho,
tolo (weigh),
samjho,
phir faisla karo.

Par Rama se ladna…
yeh tumhare hit mein bilkul nahi hai.
Main tumhari bhalai ke liye bol raha hoon.”
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter38
    with st.expander("Chapter 3.38 – Marica tells Ravana how he once met Rama"):
        text1 = """
Marica ne gehri saans li,
aur Ravana ko apna pura purana kissa sunane laga:

Marica ka purana roop

“O Raja,
kisi waqt main bohot shaktishaali tha.
Mera sharir pahaad jaisa bada,
aur mujhme hazaar haathiyon jitni taqat thi.

Meri rangat kaale badal jaise,
haath me golden bracelet,
sar par chamakta mukut (crown),
aur haath me ek bhaari gada (club) hoti thi.

Main Dandaka jungle me ghoomta,
aur tapasviyon (ascetics) ko dara-dhamka kar unka maans (flesh) kha jaata.”
        """
        create_image_text_layout("attached_assets/chapter3/3.38.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Vishvamitra ka dar (fear)

“Ek din,
Maharishi Vishvamitra khud King Dasaratha ke paas gaye
aur bole:

‘Raja,
meri yagya ki raksha sirf Rama hi kar sakta hai.
Mujhe Marica se bohot dar lagta hai.’”

Dasaratha bole:

‘Par Rama to abhi 12 saal ka bhi nahi hua!
Main apni sena lekar jaata hoon!’”

“Rama hi is kaam ke layak hai”

“Lekin Vishvamitra ne kaha:

‘Raja, aap bohot shaktishaali hain,
par Marica jaise raakshason ko
sirf Rama rok sakta hai.
Main Rama ko hi le jaunga.’”

Aur is tarah
chhote Rama ko Rishi apne saath le gaye.

Chhote Rama ka prakash

“Rama, bas ek baccha,
kaale-neele rang ka,
baalon ko jooda (knot) me baandhe hue,
simple vastra (clothes) pehne,
par unki aankhon me chamak…

Dandaka jungle unki roshni se chamakne laga —
jaise naya chand ugha ho.”

Rama ka pehla teer… jo aaj tak yaad hai

“Main dhanush aur taqat ke ghamand (pride) me
hermitage me ghus aaya.
Rama ko bachcha samajhkar
maine unhe nazarandaaz kar diya
aur seedha yagya ki jagah ki taraf badh gaya.

Par Rama ne ek teer nikaala —
patla, tez, bijli jaisa.

Aur woh teer mujhe laga…
aisa laga jaise pralay ki lahar (massive wave) ne dekhte hi dekhte
mujhe samundar me fenk diya.

100 yojan (bahut door!) door samundar me jaa gira!
Main behosh ho gaya.”

Rama ne jaan bakshi — par maar bhi diya

“Rama ne mujhe maara nahi,
par itni zor se uchhala
ki main jeene ki umeed kho baitha.

Main to bach gaya,
par mere saath jo rakhshas aaye the…
wo sab ek bachche Rama ne khatam kar diye.”

“Ravana, agar tum Rama se takraoge…”

Marica ne Ravana ki aankhon me dekha aur bola:

“Raja,
agar tum mujhe chhodkar
khud Rama se ladne jaoge,
toh turant aur bhayanak parinaam (terrible consequence) tumhara intezaar karega.

Lanka ka raaj,
uski imaaratein,
uske mandir…
sab jal kar raakh ho jayenge.

Tumhare raakshas mit jayenge,
unki patniyan roti huin bhatakti rahengi.
Ek balatkaar (wrong, sinful act) —
dusre ki patni ko chhoona —
sabse bada paap hai.

Tumhare paas to hazaaron mahilaayen hain!
Phir Sita par kyun nazar?”

Antim chetavani (final warning)

“Agar tum Sita ka apaharan karoge,
toh Rama apna dhanush uthayega…

Aur uske teer tumhe,
tumhare senapatiyon ko,
tumhari Lanka ko—
seedha Yama (death-god) ke ghar pahucha denge.

Ravana,
main dushman nahi…
tumhara acha chaahne wala hoon.
Meri baat maan lo.

Rama se dushmani = Vinash (destruction).”
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter39
    with st.expander("Chapter 3.39 – Marica again tries to stop Ravana"):
        text1 = """
Marica ka dusra bhayanak anubhav

“O Ravana,
maine tumhe bataya tha ki kaise pehli baar Rama ne mujhe chhod diya.
Ab suno aage kya hua.

Main phir bhi nahi sambhla.
Apni purani aadat par wapas chala gaya.
Do aur raakshason ke saath,
maine ek hiran (deer) ka roop liya
aur Dandaka jungle me ghoomta raha.

Main tapasviyon (ascetics) ka maans khata,
unka khoon peeta,
aur unke yagya (sacrifice rituals) bigaadta.
Main itna kathor (cruel) ban gaya
ki sabhi log mujhe dekh kar kaapte the.

Lekin ek din
main phir Rama, Sita aur Lakshmana se takra gaya.
Woh teenon tapasya (penance) aur dharm ka kaam kar rahe the.”
        """
        create_image_text_layout("attached_assets/chapter3/3.39.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Marica ka ghamand — aur phir darauna sach

“Ihne Rama ko dekha
to maine socha,
‘Yeh to ab sanyasi ban gaya!’
Aur mujhe apni pehli haar yaad aa gayi.
Gusse me aakar,
hiran ke roop me hi
main uspar hamla karne chala gaya.

Par Rama…
Rama to Rama hai!

Usne apna dhanush khicha,
aur teen tez-tez teer
bijli (lightning) ki tarah chhod diye.

Mujhe turant samajh gaya
ki agar main yahin tik gaya,
to yaheen mar jaunga.

Main bhaag nikla.
Bas main hi bach gaya.
Mere dono saathi turant mar gaye.”

Rama ka darr — jo kabhi nahi gaya

“Main bahut mushkil se bachkar yahan aaya,
aur tab se tapasvi (ascetic) bankar reh raha hoon.

Lekin ek baat sach hai:
Rama ka darr mere andar se kabhi nahi gaya.

Ab mujhe har jhaad me Rama dikhai deta hai.
Har ped me Rama.
Har andhera kona Rama.

Sote waqt bhi
Rama mujhe sapne me dikhai deta hai —
teer, dhanush, aur woh kaale-neele roop me.

Main itna dara hua hoon
ki ‘Ra’ se shuru hone wale shabd bhi suntan ghabra jaata hoon.
Jaise ‘Ratna’, ‘Ratha’…
sab mujhe Rama ka yaad dilate hain.”

“Ravana, tum Rama ka saamna nahi kar sakte”

“O Ravana,
Rama ki shakti ko pehchano.
Bali aur Namuchi jaise shaktishaali daanav (demons) bhi usse nahi bach paaye.

Tum Rama se ladoge
to tumhara jeena mushkil ho jayega.

Agar mujhe zinda dekhna chahte ho,
to Rama ka naam bhi mat lena!
Main fir se uss darr me nahi jeena chahta.”

Antim Chetavani

“Ravana,
duniya me bohot ache log hote hain
jo dusron ki galtiyon ki saza bhugat te hain.
Main bhi unme se ek ho jaunga
agar tumhari galtion ke chalte Rama mujhe maar dega.

Isliye
jo sahi lagta hai woh karo,
lekin main tumhare saath nahi jaunga.

Rama tumhare pura klan (family line) aur sabhi raakshason ka vinash (destruction) karega
agar tumne Sita ko chhua bhi.

Khara bhi uski wajah se mara gaya.
Usme Rama ki kya galti?

Maine yeh sab tumhare bhalai ke liye bola.
Agar tumne meri baat na maani—
toh tum, tumhare senapati, aur Lanka ke sabhi raakshas…
Rama ke teeron se samapt ho jaoge.”
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter40
    with st.expander("Chapter 3.40 – Ravana becomes angry"):
        text1 = """
Ravana ne Marica ki baat suni.
Par usne turant mana kar diya.
Usne Marica ki salaah ko thukra diya.
(Woh salaah helpful [faaydemand] thi.)

“Tu moorkh hai!” Ravana garajte hue bola.
“Teri baatein bekaar beej jaisi hain.
Jo zameen banjar (barren) ho uspe boya gaya beej kabhi na ugta.”

Ravana ne taiyaar ho kar kaha:
“Main apna iraada badalunga nahin.
Rama ek chhota aadmi hai.
Uski patni Sita ko main le jaunga.
Chahe Indra ho ya devta, koi rok nahin sakta.”

Phir Ravana ne Marica ko safai (instruction) di:
“Tum sone ka hiran ban jao.
Hiran par chandi ki chamak bhi daal dena.
Us hiran se Sita aakrisht (attracted) hogi.
Sita bolegi: ‘Rama, ise pakdo!’
        """
        create_image_text_layout("attached_assets/chapter3/3.40.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Jab Rama aur Lakshmana duur chale jayenge,
tum unki awaaz ki nakal karna —
‘O Sita! O Lakshmana!’ kehte hue.
Jab dono door honge,
main aakar Sita ko utha lunga.
Phir main tumhe aadha raaj (half the kingdom) dunga.”

Ravana ne zor se kaha:
“Agar tum mere hukm na maane,
to main tujhe turant maar dunga.
Raja ki aagya ke against rehna khatarnaak hai.
Soch le, kya fayda aur kya nuksan hai.
Jo bhi theek lage, woh kar.”

Marica ne dar se sune.
Ravana ka chehra krodh se jalta hua tha.
Usne dhamki di aur apna plan spasht (clear) bata diya.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter41
    with st.expander("Chapter 3.41 – Marica gives Ravana more advice"):
        text1 = """
Ravana ne jab zabardasti Marica ko apne plan mein shamil hone ka hukum diya, toh Marica ne himmat se jawab diya.

“Hey Raja,” Marica bola, “kaun woh bad-naseeb aadmi hai jisne tumhe aisa raasta dikhaya? Yeh raasta tumhari barbadi (destruction) ka raasta hai. Tumhare bachchon, tumhari rajya, tumhare mantriyon — sabki.”

Marica ne kadve, par sach wale shabd bole:

“Jo aadmi tumhe is mushkil mein dhakel raha hai, woh tumhara dushman (enemy) hai. Achhe mantri kabhi raja ko galat raaste par nahi chalne dete. Par tumhare mantri chup hain, isliye woh bhi apradhi (guilty) hain.”

Fir Marica ne samjhaya:
        """
        create_image_text_layout("attached_assets/chapter3/3.41.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
“Raja ka charitra (character) hi poore rajya ka adhaar hota hai. Agar raja kathor, ghamandi aur besabar ho, toh rajya kabhi tik nahi sakta. Aise raja apne logon ko protect nahi kar sakte — jaise ek lomdi (fox) hiranon ke jhund ko bachane ki koshish kare.”

Marica ne Ravana ki aankhon mein dekh kar kaha:

“Mujhe mat ro, Ravana. Tumhara dukh mujhe zyada dikh raha hai. Rama tumhe jald hi maar dega (kill), aur tumhari sena bhi dhal jayegi. Aur agar main tumhari madad karke Sita ko churaane gaya, toh Rama ke haath mein main bhi mar jaunga.”

Usne ant mein kaha:

“Samajh lo, Ravana. Tum Sita ko agar le bhi jaate ho, toh usi pal tumhara ant (end) tai ho jayega—tumhara, Lanka ka, aur sab rakshason ka. Main tumhari bhalai (welfare) ke liye keh raha hoon, par maut (death) ke kareeb aaya aadmi kabhi sahi salah nahi sunta.”
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter42
    with st.expander("Chapter 3.42 – Marica becomes a golden deer and goes near Rama’s hut"):
        text1 = """
Marica ne jab Ravana ko apni kadvi baat keh di, toh woh darr se kaanp raha tha. Fir bhi bola:

“Chalo Raja… main tumhare saath chalunga. Par yaad rakhna—jaise hi main Rama ke saamne jaaunga, mera jeevan samapt (end) ho jayega. Jo Rama ka virodh karta hai, woh kabhi zinda wapas nahi aata. Tumhare liye woh Yamadand (rod of death) banega. Par theek hai… main chalta hoon. Tumhara bhala ho.”

Ravana yeh sun kar bahut khush ho gaya. Usne Marica ko gale lagaya aur meethi awaaz mein bola:

“Ab lagta hai tum sach mein Marica ho. Pehle toh koi aur rakshas jaisa lag raha tha. Chalo, mere saath mere uḍne wale rath (flying chariot) par chadh jao. Tum bas Sita ka dhyaan apni jaal se kheench lo. Baaki main sambhaal loonga.”

“Thik hai,” Marica bola.
        """
        create_image_text_layout("attached_assets/chapter3/3.42.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Ravana aur Marica dono Ravana ke chamakte hue rath par baith gaye—jisme mules the jinke sir bhoot-jaisi shakal (goblin heads) wale the. Rath hawaa ki tarah udd raha tha. Neeche se gaon, nadiyan, pahaad, jungle sab dikh rahe the.

Aakhir woh Dandaka Forest pahunch gaye, jahan Rama ka ashram tha.

Ravana ne neeche utar kar Marica ka haath pakda aur bola:

“Dekho, yahi Rama ka ashram hai. Ab tum woh kaam karo jiske liye hum yahan aaye.”

Marica ne bina deri kiye apni maya ka prayog (magic use) kiya aur ek sundar, chamakdaar, ajeeb-sa golden hiran ban gaya.

✨ Marica ka Badla Hua Roop

Woh hiran bahut hi khoobsurat tha:

uske singh (horns) par chamakte ratna (gems) lage the,

uski twacha (skin) par chandi jaise chhote-chhote spots chamak rahe the,

muh gulabi kamal (red lotus) jaisa,

kaan neele (blue-tinted),

gardan lambi,

sharir par rang-birangi chamak jaise rainbow,

khur (hoofs) hara ratna jaise.

Poora jungle uske roop ki roshni se chamak raha tha.

Woh dhire-dhire ashram ke aas-paas ghoomne laga—kabhi door jaata, kabhi paas aata, kabhi khelta, kabhi jhuk kar ghaas khata. Jungle ke doosre hiran uske paas aaye, par uski ajeeb si khushboo sunkar bhaag gaye.

Marica ne unhe nuksaan nahi pahunchaya—apni asli pehchaan (identity) chhupane ke liye.

✨ Sita ki Nazrein us par padti hain

Iss samay Sita phool tod rahi thi. Karnikara, Ashoka aur Cuta pedon ke beech woh shanti se chal rahi thi.

Tabhi unki nazar us chamakte hue hiran par padi.

Hiran ki twacha moti aur heere jaise chamak rahi thi. Uski aankhon aur roshni ne Sita ka man mohit (captivate) kar liya.

Sita apni jagah ruk gayi.
Aankhein badi ho gayin.
Unhone kabhi itna sundar praani nahi dekha tha.

Woh deer kabhi chhup jata, kabhi saamne aa jata, aur apni sundarta se Sita ka dhyaan kheech raha tha.

Sita bas hairaan hokar use dekhne lagi—jaise koi bachchi ek chamakdaar khilone ko dekh kar khush hoti hai.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter43
    with st.expander("Chapter 3.43 – Sita becomes attracted to the beautiful deer"):
        text1 = """
Sita phool tod rahi thi. Uska rang sona jaisa tha, aur chalna bahut komal.
Tabhi uski nazar us chamakdaar golden-silver hiran par padi.
Woh turant khush ho gayi aur zor se bulaayi:

“Prabhu! Lakshmana! Jaldi aaiye, dekhiye!”

Rama aur Lakshmana ne hiran ko dekha. Dono hairaan reh gaye.

Lakshmana ne turant kaha:

“Bhaiya, yeh pakka rakshas Marica hi hai!
Woh aksar hiran ka roop lekar rajaon ko behlata (tricks) hai…
Yeh asli hiran ho hi nahi sakta. Yeh sab maya (illusion) hai.”

Par Lakshmana baat khatam hi kar raha tha ki Sita pyaar se muskurate hue boli:
        """
        create_image_text_layout("attached_assets/chapter3/3.43.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
“Prabhu, yeh hiran mujhe bahut pasand aa gaya hai.
Aap please ise pakad kar le aaiye.
Aisa sundar praani mainne kabhi nahi dekha.”

Sita ne aur kaha:

“Jungle mein bahut jeev-jantu hote hain…
par is hiran ki chamak, iski naram chaal, iski rang-birangi twacha…
kisi se milti hi nahi.
Agar aap ise zinda pakad kar laaye, toh ashram aur hamare mahal dono saja denge!”

Phir thoda sharma kar bola:

“Agar zinda na ho sake…
toh iska sona-jaisa chamakdar chhal (skin) bhi bahut sundar hoga.
Main us par baithna chaahungi…
Mujhe maaf kijiye Prabhu, agar yeh ichchha thodi kathor (cruel) lagti ho.”

✨ Rama bhi mohit ho jaate hain

Rama bhi us hiran ki roshni dekh kar hairaan ho gaye.

Unhone hansi ke saath Lakshmana se kaha:

“Lakshmana, dekho Sita kitni khushi se ise dekh rahi hai.
Aaj yeh hiran apni sundarta ke kaaran hi apni jaan dega.”

Rama boli:

“Na Nandana van (heavenly forest), na koi aur jagah…
kahin bhi aisa hiran nahi milta.
Agar yeh hiran sach hai, toh hamare liye ek anmol khazana (treasure) hoga.
Aur agar yeh Marica ka jaadu hai…
toh main ise maar dunga.”

Rama ko purana kissa yaad aaya—Rakshas Vatapi ka—
aur unhone kaha:

“Jaise Rishi Agastya ne Vatapi ko khatam kiya,
waise hi Marica ka bhi ant hoga.”

✨ Rama Lakshmana ko Sita ki raksha saunp dete hain

Rama ne Lakshmana se kaha:

“Lakshmana, tum yahin raho.
Sita ki raksha karna.
Main ya toh is hiran ko zinda pakad kar laaunga…
ya phir ise ek teer se gira dunga.
Jatayu (buddhiman pakshi) bhi yahin hai, woh bhi Sita ka khayal rakhega.”

Rama apna dhanush utha kar hiran ke peeche chal pade.
Sita aankhon mein chamak lekar unhe jata dekh rahi thi.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter44
    with st.expander("Chapter 3.44 – Rama kills Marica, the fake deer"):
        text1 = """
Rama ne Lakshmana ko Sita ki raksha karne ko kaha,
phir apni talwar (sword) aur dhanush-baan (bow & arrows) lekar hiran ke peeche nikal pade.

Woh tez kadam chal rahe the, aur saamne woh chamakdaar hiran kabhi dikhai deta, kabhi ghaas mein chup jata.
Kabhi door bhaagta, kabhi itna paas aa jata jaise keh raha ho—“Aao, pakdo mujhe!”

Bilkul waise hi jaise badal (clouds) kabhi chand ko chhupa dete hain aur kabhi dikha dete hain—
waise hi Marica hiran ke roop mein Rama ko bahut door tak le gaya.  
        """
        create_image_text_layout("attached_assets/chapter3/3.44.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
✨ Rama ko shak hone lagta hai

Rama bhaagte-bhaagte gusse mein aa gaye.
Unhone ek teekha, chamakta hua teer (arrow) nikala,
jo aisa lag raha tha jaise aag ka saanp (fiery serpent) ho.

Ek zor ki taan karke Rama ne teer chhod diya.
Teer seedha hiran ke dil par laga.

Hiran uchhal kar gira…
aur dhad se zameen par gira.
Usi pal hiran ka jadoo toot gaya—
aur woh apni asli shakl, rakshas Marica, mein aa gaya.

✨ Marica ka aakhri chaal

Marica marne se pehle ek aakhri chaal (trick) chalna chahta tha.
Ravana ne usse kaha tha ki Sita ko akela chhodna.
Isliye, marne se pehle, Marica ne zor se Rama ki awaaz banakar chillaaya:

“O Sita! O Lakshmana!”

Uski awaaz dard bhari thi, jaise Rama mushkil mein ho.

Marica kuch hi pal baad mar gaya.
Rama ne uska bada rakshas roop zameen par pada dekha aur ghabra gaye.

Unhone socha:

“Yeh toh Marica tha… Lakshmana ne sahi kaha tha.
Sita aur Lakshmana is cheekh ko sun kar kya karenge?
Sita toh bahut ghabra jaayegi…”

Rama ke dil mein ek darr sa uthne laga.

✨ Rama wapas lautne lagte hain

Marica ko maar kar, Rama ne paas hi ek aur hiran ka shikar kiya
taaki Sita ko pashchataap na ho.
Phir woh tezi se ashram ki taraf lautne lage.

Unhe bilkul andaza nahi tha…
ki unki gair-haazri (absence) mein sab kuch badalne wala hai.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter45
    with st.expander("Chapter 3.45 – Sita sends Lakshmana to help Rama"):
        text1 = """
Sita ne door se ek dard bhari cheekh (cry of distress) suni.
Awaaz bilkul Rama ki lag rahi thi.
Dar se kaanpte hue Sita ne Lakshmana se kaha:

“Lakshmana, yeh toh Rama ki awaaz hai! Jaldi jao! Unhe kuch ho gaya hoga!”

Lakshmana ne Rama ka aadnya (command) yaad kiya—
Rama ne kaha tha ki “Sita ki raksha karna.”
Isliye Lakshmana hilay bhi nahi.

Yeh dekh kar Sita gusse aur darr se bhar gayi.
Usne teekhe shabdon mein kaha:
        """
        create_image_text_layout("attached_assets/chapter3/3.45.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
“Lakshmana! Tum Rama se dikhawa wale pyaar karte ho!
Woh takleef mein hai aur tum yahan khade ho?
Kya tum chahte ho woh mar jaye?
Kya tum mujhe paana chahte ho?
Ya Bharata ne tumhe bheja hai?”

Sita ke bhaari-ilzaam (accusations) sunkar Lakshmana ka dil toot gaya.

Shant aur dukh bhari awaaz mein Lakshmana ne kaha:

“Maa Sita, yeh sab theek nahi.
Rama ko na raakshas (demon), na devata (god), koi haar nahi sakta.
Woh toh Indra (king of gods) jaise veer hai.
Jo awaaz aapne suni hai, woh Rama ki nahi.
Rakshas log awaaz badal sakte hain—yeh unki maya (illusion) hai.”

Par Sita pe gusssa aur darr dono ka asar tha.
Usne phir kaha:

“Lakshmana, agar Rama ko kuch ho gaya,
toh main Godavari mein kud jaungi,
ya apni jaan de dungi!
Par main kisi aur ko kabhi nahi apnaungi!”

Sita phoot-phoot kar ro padi.
Uski aankhon se tez aansu beh rahe the.

Lakshmana ne bahut samjhaya,
par Sita chup hi rahi.

Aakhir, Sita ki dukh bhari zid (painful insistence) dekh kar,
Lakshmana ne haath jod kar kaha:

“Devi Sita, aapko sab devta bachayein.
Main bas Rama ko dekh kar wapas aata hoon.”

Woh baar-baar mud kar Sita ko dekhta hua
dukhi dil se ashram chhod kar chala gaya.

Usse bilkul andaza nahi tha
ki jaise hi woh jaayega…
kisi bahut bade sankat (danger) ka darwaza khulne wala hai.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter46
    with st.expander("Chapter 3.46 – Ravana comes near Sita"):
        text1 = """
Lakshmana ko Sita ke kadwe shabdon (bitter words) ne bohot chot pahunchayi.
Dukhi dil ke saath, woh turant Rama ko dhoondhne nikal pada.

Jab Sita bilkul akeli reh gayi, tab Ravana ne mauka pakad liya.
Woh bhikshuk (beggar monk) ka roop bana kar ashram ki taraf chala.
Uske baal jata (matted locks) the, kapde bhagwa (saffron) rang ke,
aur haath me trishul-type lakdi (triple staff) aur kam-daan (wooden bowl).

Shaam ka time tha.
Suraj dhal chuka tha.
Jungle me halka andhera phail raha tha.

Isi waqt Ravana, Sita ke samne ek sadhu jaise aakar khada ho gaya.
Andar se woh asur tha, par bahar se sadaachari brahmin.

Sita use dekh kar ghabra gayi,
lekin woh sada-chaar se bhare roop me tha, isliye Sita ne usse mehmaan samjha.
        """
        create_image_text_layout("attached_assets/chapter3/3.46.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
🌙 Ravana’s False Praise

Ravana, jo Sita ko dekh kar kaam-dev (god of desire) ke teer se ghayal ho gaya tha,
mitha-mitha bolne laga:

“Hey sundari, tumhari chamak to sona-chandi jaisi lagti hai.
Tum kaun ho?
Lakshmi?
Rati (goddess of love)?
Ya koi apsara (heavenly maiden)?

Tumhari aankhen kamal ki pankhudi jaisi hain.
Tumhari chal naram aur komal hai.
Tumhara roop to teenon lokon me nahi milta.”

Phir woh aur meetha jhooth bolta gaya:

“Yahan jungle me akeli rehna tumhare jaise komal roop ke layak nahi.
Yahan bahut khatnaak janwar aur rakshas (demons) rehte hain.
Tum mere saath chalo—rajmahal, sugandhit baag,
sundar kapde, sona-chandi sab tumhe mil sakta hai.”

🌙 Sita’s Hospitality

Sita ko laga yeh ek sadharan brahmin mehmaan hai.
Isliye Sanskrit parampara ke hisaab se
woh turant khadi ho gai aur boli:

“Baithiye, Brahmin.
Kripya paani se apne pair dho lijiye.
Yeh phal aur bhune hue anaj ka prasad grahan kijiye.”

Ravana baith gaya,
par uski drishti Sita ki aur se hatti hi nahi.
Uske mann me ek hi vichaar tha—
Sita ko utha kar le jana.

🌙 Sita Waits for Rama

Sita baar-baar jungle ki or jhaankti rahi—
shayad Rama aur Lakshmana laut aaye hon.
Par gahra hota andhera sirf dar badha raha tha.

Ravana, brahmin ka bhes pehene,
Sita ke saamne baitha tha,
aur apni hi barbaadi ka beej boya ja raha tha.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter47
    with st.expander("Chapter 3.47 – Ravana and Sita talk"):
        text1 = """
Ravana, jo bhikshuk (beggar monk) ka roop liye baitha tha, Sita se meethi–meethi baatein karne laga.
Sita ne socha:

“Yeh mehmaan lagta hai. Agar main jawab na doon, to yeh mujhe shaap (curse) de sakta hai.”

Isliye Sita ne namrata se kaha:

“Hey Brahmin, aapka kalyan ho.
Main Janaka ki beti hoon.
Mera naam Sita hai.
Aur main Rama ki patni hoon.”
        """
        create_image_text_layout("attached_assets/chapter3/3.47.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
🌿 Sita Tells Her Story

Sita ne saaf aur shant awaaz me apni kahani batayi:

“Main 12 saal tak Ayodhya me sukh–shanti se rehti thi.
13ve saal Raja Dasharatha ne Rama ko rajya–abhishek (coronation) dene ka faisla kiya.

Par Kaikeyi ne do var (boons) maang liye—
Rama vanvaas (forest exile) jaye
aur
Bharata ko raja banaya jaye.

Rama ne bina shikayat sab sweekar kar liya.
Lakshmana bhi saath aaye, aur main bhi.”

Sita ne phir us “Brahmin” se puchha:

“Aap kaun ho?
Kahan se aaye ho?
Akele jungle me kyun ghoom rahe ho?”

👹 Ravana Reveals His Truth

Sita ke shabd sun kar Ravana ne apna asli roop dikhaya—
par baahir se abhi bhi brahmin jaise hi lag raha tha.

Woh kadve aur ghamandi shabdon me bola:

“Sita, main Ravana, Lanka ka raja hoon.
Dev, Manushya aur Rakshas sab mujhse darte hain.
Tumhe dekhkar mere man me bas ek hi ichha hai—
tum meri rani bano.”

Phir usne lalach dena shuru kiya:

“Mere mahal me hazaaron sevika tumhari seva karengi.
Lanka samundar ke beech ek sunder shehar hai.
Tum vahaan rani bankar raho.”

🔥 Sita’s Furious Reply

Sita ka gussa sardi ki hawa jaise kaap utha.
Usne Ravana ko tiraskar (contempt) se jawab diya:

“Main Rama ki patni hoon.
Rama pathar jaisa dridh (firm) aur samundar jaisa shant hai.
Unki shakti aur veerta Indra (king of gods) jaisi hai.

Aur tum?
Ek giddh (vulture) ho jo sher ki patni par nazar daal raha hai!”

Sita usse be-dard shabdon me daantne lagi:

“Tum mujhe paane ka sapna dekhte ho?
Yeh to us jaise hai jaise koee:

— Sooraj ko pakadne ki koshish kare,
— Zehreeli saanp ke daant todne jaye,
— Aag ko apni godi me utha le,
— Ya samundar ko pair se rokne ki soch rakhe!

Rama se tumhari tulna?
Sher aur lomdi,
Neelam aur pathhar,
Hamsa aur giddh,
Ussi jaise antar hai.”

Sita ka sharir darr se kaamp raha tha,
par uska man mazboot tha.

👹 Ravana’s Dark Pride

Sita ke saaf–saaf inkaar se Ravana aur bhi bhayanak dikhne laga.
Woh apni shakti, vansh (lineage), aur jitni shadiyan usne ki, sab ka ghamand dikhane laga—
taaki Sita aur dare.

Chapter yahin par samaapt hota hai,
jahan Ravana apni bhayankar shakti ka dikhawa karta hai…
aur Sita Rama ko yaad karte hue akeli kaamp rahi hai.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter48
    with st.expander("Chapter 3.48 – Sita bravely refuses Ravana"):
        text1 = """
Sita ke kadve aur teekhe shabdon se Ravana aur bhi gussa ho gaya.
Uski aankhen angaaron ki tarah chamak uthi.
Woh garjte hue bola:

👹 Ravana Brags Again

“O sundar Sita, sun lo!
Main Dashagriva (ten-headed one) Ravana hoon.
Main Dhan ka Devta Kuvera ka bhai hoon.
Meri shakti se Devta, Gandharva, Nag aur Rakshas sab darr kar bhaagte hain.

Main ne apne hi bhai Kuvera ko yuddh me hara diya.
Uska divya rath Pushpaka Vimana (flying chariot) bhi chheen liya.
Usme baithkar main aasman me ghoomta hoon.”

Ravana apne ghamand me bolta gaya:

“Jahan main jaata hoon, hawa thandi chalne lagti hai.
Suraj ki roshni bhi chandni si ho jaati hai.
Pedon ke patte ruk jaate hain.
Nadi ka paani behna band ho jaata hai.
        """
        create_image_text_layout("attached_assets/chapter3/3.48.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Samundar ke paar meri rajdhani Lanka hai—
ek sundar shehar, sone ki deewaron aur heere-moti ke dwaron se bana hua.”

Phir woh Sita ko phuslane laga:

“Wahaan tum mere saath rani bankar raho.
Swarg jaise sukh paogi.
Rama ko bhool jao—
Woh bas ek insaan hai.
Uski shakti kuch bhi nahi.
Uska ant (end) nazdeek hai.”

Ravana ne Sita ko dhamki dete hue bola:

“Main tum se prem karta hoon.
Agar tumne mujhe thukra diya,
to tumhein pachtana padega.
Rama mujhse takkar nahi le sakta.”

🔥 Sita’s Defiance (Sita ka Dhoomdaar Jawaab)

Sita ki aankhen gusse se chamak uthi.
Akele hote hue bhi uski awaaz sherni ki tarah dhaad rahi thi.

Sita boli:

“Tum Kuvera ke bhai ho to kya hua?
Tumhari harkat ek nich (low) aur adharmi (unrighteous) aadmi ki hai.
Aise swami ke saath saare Rakshas ka vinash (destruction) nischit hai.

Sun Ravana!
Indra ki patni ko chura kar koi bach bhi jaye,
par Rama ki patni ko churaane wala kabhi zinda nahi bachega!”

Sita ka gussa ab bijli ki tarah garajne laga:

“Koi Indra ke var (boon) se amrit (immortality nectar) peeke bach sakta hai,
lekin jo mujhe—Rama ki patni—par haath daale,
uski mrityu (death) pakki hai!”
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter49
    with st.expander("Chapter 3.49 – Ravana kidnaps Sita"):
        text1 = """
Sita ke kathor shabdon ko sun kar Ravana ka gussa fut pada.
Usne zor se apne dono haath takraye.
Phir woh apni asli roop dikhane laga.

👹 Ravana Shows His True Form

Ravana garjte hue bola:

“Lagta hai tumhe meri shakti ka pata hi nahi.
Main itna taqatwar hoon ki zameen ko akela utha sakta hoon.
Samundar ka paani pee sakta hoon.
Suraj ko apne teer se chhed sakta hoon.
Dekho, main apna roop pal bhar me badal sakta hoon.”

Yeh kehkar Ravana ne apna sadhu wala bhesh chhod diya.
Uski aankhen angaaron ki tarah jal rahi thi.
Uske dus sir (ten heads) aur bees haath (twenty arms) chamakne lage.
Laal vastra pehne hue woh Sita ki aur badha.
        """
        create_image_text_layout("attached_assets/chapter3/3.49.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
👹 Ravana Tries to Take Sita Again

Woh bola:

“O sundar Sita, agar tum teenon lokon (Three Worlds) me mashhoor pati chaho,
to mere paas aa jao.
Main tumhari bahut seva karunga.
Rama tumhe kya de payega?
Uska rajya chhin gaya hai.
Woh vanvaasi hai.
Uski takdeer khatam ho chuki hai.”

🔥 Ravana Grabs Sita

Yeh kehkar Ravana, jo ab paap se andha ho chuka tha,
ne Sita ka baal apne ek haath se pakad liya,
aur doosre haath se uski kamar.

Sita cheekh uthi.
Devta bhi darr kar chhupe gaye.

Tabhi Ravana ka sone ka rath—
Pushpaka-vimaan ka ek hissa—
pashuon jaisi aawaz karte khachcharon ke saath aa gaya.

Ravana ne Sita ko zor se uthaya
aur uncha aasman me le kar udd chala.

Sita zor zor se chillane lagi:

“Rama! Rama!
Mujhe bachaao!”

😭 Sita’s Cry for Help

Asmaan me le jaate hue Sita ne pukara:

“O Lakshmana!
Kya tumhe nahi dikhta ki ek dusht rakshas mujhe le ja raha hai?

O Rama!
Aap to sada dharma nibhate ho.
Kya aapko nahi dikh raha ki mujhe le jaaya ja raha hai?
Yeh atyachari apne paap ka phal zaroor payega!”

Phir Sita ne janglon aur nadiyon ko pukara:

“O Janasthana ke pedo!
O Kamikara ke phoolo!
O Godavari nadi!
Rama ko batana
ki Ravana mujhe zabardasti le gaya hai!”

“Jungle ke sab jeev—
pakshi, janwar, nadi, ped—
sab Rama ko batana
ki unki priya patni ko Ravana utha le gaya hai.”

🦅 Sita Calls Jatayu

Gham ke beech Sita ne ek ped par vishal vulture Jatayu ko dekha.

Sita chilla kar boli:

“O mahan Jatayu!
Dekh lo, yeh dusht Ravana mujhe le ja raha hai.
Tum usse lad nahi paoge,
kyunki woh bahut shaktishaali hai.

Par tum ek kaam kar sakte ho—
Rama aur Lakshmana ko sab sach batana.
Ek bhi baat chhupana mat!”
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter50
    with st.expander("Chapter 3.50 – Jatayu tries to stop Ravana"):
        text1 = """
Sita ki cheekh sun kar Jatayu, jo ped par so raha tha, jaag gaya.
Usne dekha ki Ravana Sita ko le ja raha hai.

Jatayu, jo pakshiyon ka raja tha, ped par baitha hua, dheere se bola:

🦅 Jatayu Warns Ravana

“O Dashagriva (Ravana)!
Main Jatayu hoon, giddhon ka raja.
Main dharma ka paalan karta hoon.
Aur tumhari yeh galat harkat main bilkul bardasht nahi karunga.

Tum jise le ja rahe ho vo Sita hai—
Rama ki patni.
Rama, jo sab logon ki raksha karte hain
aur jo Varuna aur Indra jaise devtaon ke barabar shaktishaali hain.”

Jatayu samjhata hua bola:

“Ek sachcha raja kabhi kisi doosre ki patni par nazar nahi daalta.
Tum khud ek raja ho.
Tumhe to doosron ki patniyon ki raksha karni chahiye.
Par tum to khud hi paap kar rahe ho.”
        """
        create_image_text_layout("attached_assets/chapter3/3.50.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
👹 Jatayu Explains the Consequences

“O Ravana,
tum galti se apne gale me maut ki rassi daal rahe ho.
Tum samajh nahi rahe—
Sita ko chhurane ka matlab hai
Rama ka khaufnaak rosh bulana.

Rama ne tumhare desh me kisi ko kuch nahi kiya.
Khara aur Dusht rakshason ko to unhone shurpanakha ke paap ki wajah se mara.
Phir tum kyun Ramanand ki patni ko chura rahe ho?”

Jatayu ne sakht shabdon me chetavani di:

“O Ravana,
Rama ka gussa tumhe bhasm kar dega,
jaise Indra ne vajra se Vritra ko maara tha.”

🦅 Old but Brave – Jatayu Stands Against Ravana

Jatayu bola:

“Main 60,000 saal ka hun.
Bahut budha ho chuka hoon.
Tum yuva ho, shastron se saja ho, rath par ho.
Main kamzor hoon—
par jab tak main zinda hoon,
tum Sita ko lekar nahi ja sakte.

Main tumhare rath ko jhad se tute hue phal ki tarah gira dunga!”

⚔️ Jatayu Challenges Ravana

“Ravana!
Agar zara si bhi sharam bachi hai to ruk jao!
Lado!
Tum bhi Khara ki tarah dharti par giroge!

Tum Sita ko le ja rahe ho
sirf isliye ki tum Rama se darte ho.
Par jab tak main zinda hoon,
main Sita ko bachane ki koshish karunga—
apni jaan dekar bhi.

Ruko!
Ruko Dashagriva!
Yahaan mere saamne bhago mat!”
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter51
    with st.expander("Chapter 3.51 – Jatayu fights Ravana bravely"):
        text1 = """
Jatayu ne Ravana ko rokne ke liye bahaduri se baat ki.
Par Ravana, gusse se laal aankhon wala, sona ke kundal pehne hua, us par toot pada.

Aasmaan me bahut zor ka yudh shuru hua—
jaise do bade pahaad pankh laga kar aapas me takra rahe hon.

🏹 Ravana Attacks First

Ravana ne ek ke baad ek teekhe lohe ke teer (steel arrows) chalaye.
Par Jatayu, pakshiyon ka raja, un teeron ko jhelta raha.

Apne tez panjon (claws) se usne Ravana ko chot pahunchayi.

Ravana aur gussa ho gaya.
Usne bade bhayanak teer nikale—teer jo maut jaise teekhe the.
Ve teer Jatayu ke shareer me ghus gaye.

🦅 Jatayu Breaks Ravana’s Weapons

Jatayu ne dekha ki Sita, aansuon se bhari aankhon ke saath, rath me baithi hai.
Usne teeron ki parwah kiye bina sidha Ravana par hamla kar diya.

Usne apne panjon se Ravana ka teer-kamaan tod diya—
wo kamaan motiyon aur heere se saja hua tha.

Ravana ne doosra kamaan uthaya
aur ek saath hazaron teer barsa diye.
Jatayu teeron ke neeche ek ghosle me chhupi chidiya jaisa lagne laga,
par usne zor se pankh hila kar teer hata diye
aur Ravana ka doosra kamaan bhi tod diya.

Phir Jatayu ne apne bade pankhon se
Ravana ki dhaal (shield) bhi chakhna-choor kar di.
        """
        create_image_text_layout("attached_assets/chapter3/3.51.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
🐎 Jatayu Destroys the Golden Chariot

Jatayu ne Ravana ke rath ko bhi tod diya—
wo rath sone ka tha,
aur usme bhoot-mukhi ghode (demon-headed mules) lage the.

Ek hi jhatke me usne:

rath ke teen dhwaj (standards) gira diye

rath ki chhatri (canopy) tod di

aur rath-sarthi ko bhi gire diya

Ravana neeche gir gaya, Sita ko apni baahon me pakde hue.

Sab log—devta, pakshi, vanaspati—
Jatayu ki jai-jai karne lage.

👹 Ravana Takes to the Sky Again

Ravana ne dekha ki Jatayu bohot budha aur thaka hua hai.
Isliye woh phir se Sita ko god me utha kar aasman me uddne laga.
Ab uske paas sirf talwar (sword) thi.

Par Jatayu ne raasta roka aur bola:

“O moorkh Ravana!
Tum Sita ko chura kar
apni hi barbaadi (destruction) bula rahe ho.

Zehar ko paani samajh kar pee rahe ho.
Jahan bhagoge, maut tumhe pakad legi.
Jise tum pakad kar le ja rahe ho,
uske pati Rama tumhe kabhi nahi chhodenge.”

🦅⚔️ The Final Battle

Ye keh kar Jatayu phir se Ravana par toot pada.
Usne apne panjon se Ravana ka maans phaad diya
aur apne chonch (beak) se uski peeth ko kaat diya.

Ravana ro rage hua,
par Jatayu ne uske das baayein haath ukhaad diye!

Lekin Ravana ke haath turant dobara nikal aaye—
jaise bill mein se saanp (serpents) bahar aa jate hain.

⚔️ Ravana Cuts Down Jatayu

Gusse me Ravana ne Sita ko ek pal ke liye chhod diya
aur Jatayu par hamla kiya.

Ravana ne apni talwar nikali
aur Jatayu ke pankh aur pair kaat daale.

Jatayu zameen par gir gaya—
laal lahu me bheegta hua,
bilkul lade hue senapati ki tarah.

🌙 Sita Cries for the Dying Jatayu

Sita, dard se roti hui,
Jatayu ki taraf daudi.

Usne Jatayu ko apni baahon me sambhala—
jaise vo koi apna hi ho.

Jatayu, pakshiyon ka veer raja,
zameen par pada tha,
bilkul ek bujhe hue mashaal (extinguished torch) ki tarah.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter52
    with st.expander("Chapter 3.52 – Jatayu is wounded and Ravana flies away"):
        text1 = """
Jatayu ko zameen par gira hua dekh kar
Sita bahut dukhi ho gayi.
Uska chehra chand jaise safed ho gaya.

Woh ro kar boli:

“Rama! Lakshmana!
Mere bure sapne, ajeeb shagun (omens) sab sach ho gaye.
Wild animals aur birds bhaag rahe hain.
Kya tum nahi samajh pa rahe?
Mujh par badi musibat aa gayi hai!

Ye bechara Jatayu,
sirf mujhe bachane ki koshish me
apni jaan de raha hai!”

🦋 Sita Runs, Ravana Chases

Sita dara-dara
pedon ko pakad kar
idhar-udhar bhaag rahi thi.

Woh chillati:

“Bachao! Bachao!”

Par Ravana—jo maut (death) jaise bhayanak dikhta tha—
use pakadne ke liye peeche bhaag raha tha.

Rama aur Lakshmana bahut door the.
Sita unka naam pukaar kar ro rahi thi:

“Rama! Rama! Lakshmana!"

Tabhi Ravana ne
Sita ke baalon ko jhatke se pakad liya
aur zor se kheech liya.
        """
        create_image_text_layout("attached_assets/chapter3/3.52.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
⚡ The Whole World Shivers

Jab Ravana ne Sita ko pakda,
tab poori duniya kaanp uthi.

hawa ruk gayi

suraj dhundhla ho gaya

gahan andhera chaa gaya

Devtas aur Rishis ne ye dekha
aur samajh gaye:

“Ab Ravana ka ant (end) nischit hai.
Ye hi wahi ghadi thi jiska intezar tha.”

🔥 Ravana Takes Sita Into the Sky

Ravana Sita ko baahon me utha kar aasman me udd gaya.
Sita peele rang ki sari me
jaise bijli (lightning) chamakti huin lag rahi thi.

Uska dupatta hawa me lahrata,
Ravana ko ek jalte pahad (blazing volcano) jaisa bana raha tha.

Par Sita ka chehra,
jo hamesha khila rehta tha,
ab bilkul murjha gaya tha—
jaise tana se tooti hui kamal ki kali (lotus).

💎 Sita’s Ornaments Fall Like Meteors

Ravana bahut tez udd raha tha.
Isliye Sita ke:

phool

baal

gehne

payal ke moti

sab zameen par girne lage.
Woh bilkul toot-taara (meteor) lag rahe the.

Ek pal me Sita ki haath ki ek badi motiyon wali mala
zameen par chamak kar bikhar gayi—
jaise Ganga swarg se gir rahi ho.

🌳 Nature Cries for Sita

Jungle ke ped hawa me hil kar
Sita ko jaise bol rahe the:

“Daro mat.”

Sarovaron ki murjhai kamal-jal
jaise Sita ke liye ro rahe the.

Pahaad apni unchi chotiyon ko
haath ki tarah utha kar
dukh jata rahe the.

Jangal ke jaanwar—sher, bhaaloo, pakshi—
Sita ke saath saath bhaag rahe the
jaise woh bhi uski raksha karna chahte hon.

Suraj bhi dukhi hokar
apni roshni kho baitha.

😢 Sita’s Last Cry

Sita aasman me le jayi ja rahi thi.
Uske baal hawa me udkh rahe the,
tilak mit chuka tha.

Woh neeche zameen ki taraf dekh kar
dheemi awaaz me bas ek baat bol rahi thi:

“O Rama…
O Lakshmana…”

Sita bilkul akeli
aur bilkul toot chuki thi.

Ravana ko ye sab dekh kar
samajh bhi nahi aa raha tha
ki yehi kaam
uski barbaadi ki shuruaat ban gaya hai.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter53
    with st.expander("Chapter 3.53 – Sita scolds Ravana for his evil act"):
        text1 = """
Aasman me uthai jaate hue,
Sita bahut dar gayi.
Uski aankhen laal ho rahi thi—
gusse, dard aur aansuon se.

Ravana ko dekh kar
woh roh kar boli:

🗣️ Sita’s Brave Words

“O gande aur buzdil (coward) Ravana!
Kya tumhe sharam nahi aati?

Tumne mujhe tab pakda
jab main akeli thi.
Tumne jhoothi maya (illusion) se
hiran ban kar
Rama ko door le jaakar dhokha diya.

Aur Jatayu—
jo mere sasur ji ka dost tha—
usne mujhe bachane ki koshish me
apni jaan de di!
Isme tumhara kaunsa veerta (bravery) hai?”
        """
        create_image_text_layout("attached_assets/chapter3/3.53.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
💥 “If you’re so strong — stop and fight!”

“O Ravana!
Tum khud ko bahadur bolte ho
par sach me tum ek kaayar (coward) ho.

Agar himmat ho to
ruko ek pal!
Rama aur Lakshmana ke saamne
tum ek second bhi zinda nahi reh paoge.

Unki ek chhoti si teer (arrow)
tumhe jala degi
jaise jungle ki aag
chota sa pakshi ko jala deti hai.”

💔 Sita Declares Her Loyalty

“Mujhe chhod do, Ravana!
Tumhara yeh bura iraada (evil intention)
kabhi poora nahi hoga.

Agar main phir kabhi Rama ko na dekh paun—
to bhi main zinda nahi rehungi.
Main unki bina kuch nahi.”

⚠️ “You’re choosing your own death.”

“O moorkh (fool) Ravana!
Tum apni hi maar chune ja rahe ho.
Tumhe maut ka phanda (noose)
abhi se gale me nazar nahi aa raha?

Tum jald hi
un bhayanak sthano ko dekhoge
jahan paapiyon ki sajaye hoti hain—
jaise
Vaitarani (blood river),
kaante bharay jungle,
aur lohe-ke-kaanto wale ped.”

🗡️ Rama’s Wrath is Coming

“Rama—
jisne akela hi
choudah hazaar rakshas maar diye the—
wo tumhe kaise chhod dega?

Tumne uski patni ko chhua hai!
Ab tumhara anth (end) nishchit hai.”

🦋 Despite Her Pain, Sita Stands Fearless

Sita ro rahi thi,
darr rahi thi,
phir bhi
Ravana ko himmat se dant rahi thi.

Woh uski baahon se chhootne ki koshish karti rahi,
par Ravana bina ruke
aasman me usse lekar
aage uddta gaya…
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter54
    with st.expander("Chapter 3.54 – Ravana reaches Lanka with Sita"):
        text1 = """
Ravana Sita ko aasman me uthaakar le ja raha tha.
Bechari Sita ko koi bachane wala nazar nahi aa raha tha.

Tabhi usne door ek pahad ki choti par
paanch shaktishaali vanar (monkeys) khade dekhe.

🪔 Sita drops a sign

Sita ke mann me ek ummeed jagi.
Usne socha:
“Shayad ye vanar Rama ko khabar pahunchayenge.”

Isliye Sita ne
apni sona-jaise chamak wali odhni
aur apne gehne
paanch vanaron ke beech gira diye.

Ravana, gusse aur ghabrahat me,
ye baat dekh hi nahi paaya—
par vanaron ne sab kuch dekh liya.
        """
        create_image_text_layout("attached_assets/chapter3/3.54.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
🛕 Ravana flies toward Lanka

Dashagriva (ten-headed Ravana)
Sita ko gale me dabaaye,
hawao me tez gati se aage badh raha tha—
jaise koi teer (arrow) hawa me dodta ho.

Jungle, pahaad, nadiyan, jheel,
sab peeche reh gayi.

Samundar (ocean) ke oopar uddte hue,
machhliyan aur bade sapole (serpents)
darr kar hilne lage.

Akaash se Siddha aur Caran (celestial beings)
bhi keh rahe the:
“Ravana ka anth paas aa gaya!”

Par Ravana, jo apni hi barbaadi ko saath le jaa raha tha,
Sita ko baahon me le kar
Lanka nagri me pravesh kar gaya.

🏰 Sita inside Lanka

Lanka ki badi-badi sadhkon me se guzarta hua,
Ravana Sita ko lekar
apne mahal ki andar wali jagah tak chala gaya.

Wahan Sita ko zameen par bithakar,
jaise maya (illusion) ek pal me mit jaati hai,
Ravana ne rakshasi (demon women) se kaha:

“Sun lo!
Meri ijazat ke bina
koi bhi Sita ko dekh nahi sakta!

Use jitne gehne, kapde, moti, laal (rubies) chahiye—
sab de do.
Aur agar koi bhi usse bura bolega…
chahe galti se bhi…
woh apna jeevan kho dega!”

Ravana gusse aur abhimaan (pride) me
vahaan se chal diya.

⚔️ Ravana sends demons to Janasthana

Usne fir
aath bhojan-khane wale rakshas (flesh-eating titans)
ek jagah bulaye.

Unki taareef karte hue bola:

“Jaldi Janasthana jao.
Wahi jagah jahan Khara rehta tha.
Rama ne Khara aur Dushana ko maar diya,
aur hamare saare rakshas vinaash ho gaye.

Mujhe Rama se badla lena hai.
Main usse maar kar hi rahunga.
Tum vahan chhup kar dekhte rehna—
Rama kya karta hai, kahan jaata hai—
sab mujhe batate rehna.
Raat-din lage raho
Rama ki maut lane ki koshish me!”

Ravana ke shabdon par
woh rakshas jhuk kar pranam karte hue
adrishya (invisible) ho gaye
aur tez gati se Janasthana ki taraf nikal pade.

🖤 Ravana’s foolish happiness

Par Ravana—
jinhone Sita ko churaakar
apne sar par Rama ka gussa saaf bulaa liya tha—
fir bhi
apne andar hi andar
bewakoofi bhari khushi me dooba raha.

Use pata hi nahi tha
ki usne apni barbaadi
apne haathon se ghar le aaye hai.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter55
    with st.expander("Chapter 3.55 – Ravana asks Sita to marry him"):
        text1 = """
Aath shaktishaali rakshason ko kaam dekar,
Ravana—jiska buddhi (mind) vasana (desire) se dhundhla gaya tha—
sochne laga ki ab sab tayari ho chuki hai.

Par uske mann me ek hi cheez chal rahi thi—
Vaidehi.
Prem-deva (God of Love) ke teer (arrows) uske dil me lage the.
Isliye woh turant apne shandar mahal ki taraf badha.

🏰 Ravana enters his palace

Mahal me, Ravana ne Sita ko dekha—
dard se jhuki hui,
aasu bhari,
aur rakshasiyon se gheri,
jaise tufaan me doobti hui kashti (ship)
ya tanhai me phasi ek hiran (gazelle) ko shikari dogs gher lein.

Ravana ne Sita ko zor se ek taraf le jaakar
apna swarg-jaisa mahal dikhaya:

Sunehre pillars (golden pillars)

Hathi-dant (ivory) aur crystal ke tukde

Heere-motiyon se sajaye hue kamre

Upar tak jaati hui sundar manzilein (storeys)

Chhaton par panchhi gaate hue

Marble ke floors jo ratnon (gems) se chamak rahe the

Neelkamal (lotus) se bhare talaab aur fountains

Par Sita ka mann dukhi tha—
uski aankhon me in sab ki chamak nahi thi.
        """
        create_image_text_layout("attached_assets/chapter3/3.55.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
💬 Ravana tries to convince Sita

Woh wicked (dushṭ) Dashagriva Sita se bola:

“O Sita,
mere paas das hazaar rakshas (titans) hain,
jo mujhe apna swami mante hain.
Har ek ke paas hazaar sevak bhi hain.

Yeh poora rajya tumhara ho sakta hai.
Tum mere liye pran (life) se bhi zyada pyari ho.”

Phir Ravana ne usse lalach diya:

“Tum meri maharani ban jao.”

“Lanka kabhi jeeti nahi ja sakti—na devta (gods), na Indra.”

“Rama ek aam aadmi hai—vanvaasi, bina dhan-daulat.”

“Main hi tumhare laayak pati hoon.”

Aur baar-baar kehne laga:

“O Maithili, mere sath saari sukh-sauvidhayein pao.
Pushpaka-vimaan (flying chariot) me mere sath ghoomo.
Tumhare ache karmon ka phal yahi Lanka me milega.”

Usne Sita ka chehra dekha—
jo pehle kamal jaisa khilaa tha,
ab dukh se murjha chuka tha.
Sita ne apna chehra dupatte me chhupa liya
aur chup-chap aansu bahane lagi.

🩸 Ravana tries again — shamelessly

Ravana, jo bilkul lajja-shoonya (shameless) tha,
fir bola:

“O Vaidehi,
dharma (righteousness) ka bhay mat rakho.
Humari shaadi Veda (sacred scripture) ke anusaar ho sakti hai.

Main tumhare charanon (feet) par apne sir rakhta hoon.
Kripya mujhe svikaar karo.
Pehli baar Ravana kisi aurat ke saamne jhuk raha hai!”

Sita chup, dukh se bhari,
uski baat sun rahi thi.

🧨 Ravana’s final delusion

Sita ke saare inkaar,
uske aansu,
uska dard—
kuch bhi Ravana ko rok nahi paaya.

Apne aap se hi bola:

“Sita ab meri hai.”

Ravana samajh nahi paaya
ki woh apni kismat ki tabahi (destruction) ko
apne hi hath lekar chal raha tha.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter56
    with st.expander("Chapter 3.56 – Demon women guard Sita"):
        text1 = """
Sita ne Ravana ki dhamkiyan sun kar bhi himmat nahi haari.
Usne apne aur Ravana ke beech ek kaas ka patta (blade of grass) rakh diya — yeh batane ke liye ki Ravana uske nazdeek bhi nahi aa sakta.

Sita ne Ravana se saaf kaha:

Rama, Dasharatha ka beta, dharma ka rakhwala hai.

Rama ek singh (lion) jaisa shaktishaali hai.

Agar Ravana ne Sita ko Rama ke saamne chhua hota, to Rama use turant maar deta — jaise usne Khara ko maara tha.

Lanka, Ravana, aur sab Rakshas — Rama ke teer ke saamne kuch nahi.

Sita ne kaha ki Ravana ki umar ab bahut kam reh gayi hai.

“Tumne mujhe chura kar apna hi nuksan kiya hai. Rama aayega aur tumhari Lanka khali ho jayegi.”

Sita keh rahi thi ki jab kisi ka vinash ka samay aata hai, tab wo paagal jaise kaam karta hai — Ravana bhi wahi kar raha hai.
        """
        create_image_text_layout("attached_assets/chapter3/3.56.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Phir Sita ne kaha:

“Main tumhare saath kabhi nahi rahungi.
Chahe tum mera sharir kaat do — main apmaan nahi seh sakti.”

⚡ Ravana ki dhamki

Ravana gusse me bolta hai:

“Agar 12 mahine me tumhaari marzi nahi badli,
to main tumhe apne subah ke khaane ke liye katwaa dunga.”

👹 Rakshasiyon ko aadesh

Ravana ne bhayankar rakshasiyon ko kaha:

“Sita ka ghamand tod do.”

“Isse Ashoka Vatika me le jaakar kaidi ki tarah rakho.”

“Kabhi darao, kabhi meetha bolo — par iska man tod do.”

🌸 Sita in Ashoka Grove

Rakshasiyan Sita ko kheench kar Ashoka Vatika me le gayi.

Wahan sab jagah phool aur phal the, par Sita ke liye sab andhera tha.

Sita:

bilkul akele thi,

dar se kamzor pad rahi thi,

rakshasiyon se gheri hui thi — jaise ek hiran ko bhediyon ne gher liya ho.

Apne pati Rama aur bhai Lakshmana ko yaad karke,
darr aur dukh ke bhaar se Sita behosh ho gayi.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter57
    with st.expander("Chapter 3.57 – Rama sees bad signs and becomes worried"):
        text1 = """
Maricha ko maar kar — jo hiran ka roop dharan karke Rama ko behka raha tha —
Rama bahut tezi se wapas ashram ki taraf daudte hain, Sita ko dekhne ke liye bechain.

Lekin raste me hi bure shagun shuru ho jaate hain:

Peeche se bhediye/jackals rohkar cheekhne lagte hain.

Rama ka dil kaap uthta hai.

Vo sochne lagta hai:
“Kahin Sita ko rakshason ne kuch toh nahi kar diya?”

Rama ko ab samajh aata hai:

Maricha ne mera awaaz banakar “Lakshmana, mujhe bachao!” kyon pukaara.

Yahi chaal thi taaki Lakshmana Sita ko akela chhod kar bahar aa jaye.

Yahi rakshason ki saazish ho sakti hai.
        """
        create_image_text_layout("attached_assets/chapter3/3.57.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Rama sochta hai:

“Janasthana me maine jo rakshason ko maara, uska badla lene ke liye woh Sita ko nuksan pahuncha sakte hain.”

Rama aur bhi ghabra jaata hai:

Upar se pakshee aur jangli jaanwar unke baaye taraf se cheekh kar bhaag rahe hote hain.

Sab bhoot-pret jaise bura sanket de rahe hote hain.

⚡ Lakshmana ka aana

Tabhi Lakshmana saamne dekhai deta hai —
color urta hua, pareshaan, sharminda.

Rama uska haath pakad kar dukh bhari awaaz me kehte hain:

“Lakshmana! Tum Sita ko akela chhod kar yahan kaise aa gaye?”

“Ye kaise shubh ho sakta hai?”

Rama ka mann tootne lagta hai.

Woh kehte hain:

“Sita shayad rakshason dwara le jaayi gayi hai…”

“Ya shayad… unhone usse maar diya…”

“Ya vo jungle me kho gayi hai…”

“Mera baaya aankh fadak raha hai.
Sab shagun bure hain.
Mera dil ashant hai.”

Maricha ki mrityu se pehle ki accept ki hui sachchai —
“Main rakshas hoon!” —
Rama ko ab yaad aa rahi hai.

Jangal ke har cheez —
panchhi, jaanwar, hawa ki aawaaz —
Rama ko ek hi baat keh rahe the:

"Sita khatre me hai…"
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter58
    with st.expander("Chapter 3.58 – Rama cries for Sita"):
        text1 = """
Lakshmana ko akela, udaas aur vinamra roop me wapas aate dekh kar Rama ka dil toot jaata hai.

Unki pehli hi pukaar:

“Lakshmana! Sita kahaan hai?”

Rama bechain ho kar poochte hain:

“Vaidehi kahan gayi?
Jo mere saath vanvaas me aayi, jo Dandaka jungle me mere dukh-sukh ki saathi thi…
Tum usse akela chhod kar kaise aa gaye?”

“Sita ke bina main ek pal bhi nahi jee sakta.”

“Woh to dev-kanya jaisi komal thi… woh mere jeevan ka praan thi.”

Rama ka dard aur dar badhta jaata hai.
        """
        create_image_text_layout("attached_assets/chapter3/3.58.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
⚠️ Rama ka bhay – Kaikeyi ki jeet

Rama sochta hai:

“Agar Sita mar gayi…
aur main bhi dukh se mar jaaun…
to ye to Kaikeyi ki jeet hogi!”

“Kya Kaushalya phir Kaikeyi ki daasi ban jayegi?
Kya mera vanvaas Kaikeyi ke man ka manorath ban jayega?”

Rama ka swaas rukta hua sa lagta hai.

🌑 Rama ka sankalp

Rama kehte hain:

“Agar Sita zinda mil gayi, main ashram wapas lootaunga.
Par agar woh mari mili…”
“…to main apna jeevan tyag doonga.”

“Agar main ashram lautkar Sita ki muskurati awaaz na sunoon…
to main jee nahi paunga, Lakshmana.”

🩸 Rama ka krodh aur dukh

Rama ab poora sach samajh jaata hai:

“Maricha ki cheekh ne tumhe majboor kiya hoga.
Sita ne ro kar tumse kaha hoga ke jaakar meri raksha karo.”

Phir Rama ka dard bhadak uthta hai:

“Lekin Lakshmana!
Tumse bahut badi chook ho gayi.”

“Tumne Sita ko akela chhod diya…
unhi rakshason ke beech jo Khara ki mrityu ki badla lene ko tadap rahe the.”

Rama ab swayam kaap uthta hai:

“Nishchay hi… woh log Sita ko maar dale honge.
Main dukh ke samudra me doob chuka hoon, Lakshmana…
Ab main kya karoon?”

🏃‍♂️🔥 Rama ka paagalon jaisa doudna

Sita ki chinta me vyakul ho kar Rama aur Lakshmana Janasthana ki taraf bhaagte hain.

Rama Lakshmana ko baar-baar daantte jaate hain—
Lakshmana se guroor aur pratibha sab khatam si ho gayi, vo sirf chup reh kar dukh sahte jaate hain.

Jungle se guzarte hue:

Rama rote hain

unka chehra peela pad jaata hai

thakaan, bhookh, pyaas, sab ko vo bhool jaate hain

sirf Sita… Sita… Sita…

🏚️ Ashram ka suunna hona

Jab Rama ashram pahunchte hain—

Woh poora khaali.
Sita kahin nahi.

Rama pagal ho jaate hain:

kabhi idhar bhaagte

kabhi udhar

jahan-jahan Sita baithi thi, chali thi, hasti thi…
Rama har jagah usse dhoondhte hain.

Unke kaan me Sita ki hansi ghoomne lagti hai.
Unke dil me bhayanak shanka jam jaati hai.
Unke rom-rom khade ho jaate hain.

Rama—mahaveer, chakravarti, dharmaraj—
ab sirf ek toot chuka pati hai.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter59
    with st.expander("Chapter 3.59 – Rama gets angry at Lakshmana in sadness"):
        text1 = """
Ashram se baahar nikalte hi, Rama ka dard phir ubhar aata hai.
Unka gala ruk gaya hai, awaaz halki pad gayi, par ghaav abhi taza hai.

🌑 Rama’s trembling voice

Rama kehte hain:

“Lakshmana… maine apni Sita tumhare hawale ki thi.
Phir tumne usey akela kaise chhod diya?”

“Tumhe akela aate dekh kar mera dil baith gaya.”

“Mera baaya haath, baayi aankh — dono phadakne lage.”

“Mere hriday me aisa kampan hua jaise koi badi vipatti nikal chuki ho.”

Lakshmana ka dil tut jaata hai.
Usey pata hai Rama ka dukh sach hai, aur unki baat be-tehsha sachchai se bhari.

🗣️ Lakshmana explains the truth

Lakshmana, kaampte hue, jawab deta hai:
        """
        create_image_text_layout("attached_assets/chapter3/3.59.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
“Bhaiya… main apni marzi se nahi aaya.
Mujhe Sita ne bheja — majboor karke.”

Phir Lakshmana poora drishya bataata hai:

“Ek cheekh aayi — ‘Lakshmana, bachao!’
Sita ne samjha yeh aapki awaaz hai.”

“Woh rokar, chillakar boli — ‘Jao, abhi jao Lakshmana!’”

Lakshmana yaad karta hai apne shabdon ko:

“Maine usey samjhaya:
‘Aisa koi nahi jo Rama ko dara sake. Yeh unki awaaz nahi.
Koi rakshas hoga jo unki nakal kar raha hai.’”

“Par Sita ka darr nahi gaya.
Aansu girte gaye… uski awaaz toot-ti gayi.”

Tab Lakshmana ke paas ek kathor yathaarth tha, jise batate hue uska chehra jal uthta hai:

🔥 Sita’s harsh accusation

Lakshmana bolta hai:

“Sita ne gusse, darr aur bhram me mujh par ilzaam lagaya—

‘Lakshmana! Tum Rama ki maut chahte ho!’
‘Tum mujh par nazar rakhte ho… isliye madad ko nahi jaa rahe!’
‘Tumhe Bharata ne bheja hai— hamara vinaash karne!’

Main yeh sab sunkar…
mera dil phat gaya.
Main gusse me kaanp utha… aur chala aaya.”

🩸 Rama’s bitter sorrow

Lakshmana ki baat sun kar bhi Rama ka mann shaant nahi hota.

Rama bolte hain:

“Lakshmana… tumne bahut bada paap kiya.”

“Ek स्त्री ke rosh ke aage jhuk kar, tumne apna dharm tod diya.”

“Tum jaante the main kisi rakshas se nahi darta… phir bhi tumne Sita ko akela chhod diya.”

Unki awaaz me teekhi chubhan hai:

“Main ne us mrig-rup rakshas ko maar diya.
Woh marne se pehle meri nakal karke cheekha—
aur tum uss ek jhooti cheekh par sab kuch chhod aaye!”

Rama aur keh nahi paate.
Unke shabd toote hue, bhaari, aur pighalte hue hain—
jaise har shabd ke peeche Sita ka naam jalta ho.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter60
    with st.expander("Chapter 3.60 – Rama and Lakshmana begin searching for Sita"):
        text1 = """
Rama tezi se ashram ki taraf bhaag rahe the.
Unka baaya aankh phadakna shuru ho gaya.
Pair ladkhada gaye. Poora sharir kaanp utha.

Yeh ashubh sanket (inauspicious signs) dekh kar Rama baar-baar puchte:

“Lakshmana… kya Sita theek hogi? Kahin kuch ho toh nahi gaya?”

🏚️ Hermitage Without Sita

Rama jaise-taise ashram tak pahunchte hain—
aur dekhta hi unka dil toot jaata hai.

Ashram khaali. Bilkul sunsaan.
        """
        create_image_text_layout("attached_assets/chapter3/3.60.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Jungle ka mahaul bhi badal gaya:

ped jaise ro rahe hon,

phool murjha gaye hon,

pakshi chup aur udaas,

janwaron ki aankhon me darr.

Rama ko apna ghar kamal ke bina jheel jaisa lagta hai—
bilkul be-rang, be-jaan.

😢 Rama’s Heartbreaking Questions

Rama daudte hain, poora ashram talashte hain,
har kone me jhaankte hain.

Phir cheekh padte hain:

“Sita kahan gayi?
Kya koi unhe utha le gaya?
Kya unka khoon kar diya?
Kya unhe janwaron ne kha liya?
Ya woh kahin phool-phal lene gayi hongi…
ya paani laane?”

Par har jagah… sirf sannata.

🌳 Rama Questions the Trees

Rama ab poora jungle se baat karte hain—
jaise ped-paudon me jaan ho.

“O Kedumbra Tree,
meri priya Sita ko dekha hai?
Wahi Sita jo tumhe pyar karti thi?”

“O Bilva Tree!
Uske kapde resham jaise the.
Uska rang tumhare harae patton jaisa tha.
Kya tumne usey dekha?”

“O Ashoka Tree—
tum dukh door karne wale ho.
Mera dukh kam karo.
Batao Sita kahaan hai…”

Rama, bilkul pagal jaise,
har ped se poochte jaa rahe hain—
Cuta, Nipa, Sala, Panasa,
Vakula, Chandana, Ketaka…

🐅 Rama Questions the Animals

Phir woh janwaron se pukaarte:

“O Hiran (deer),
kya tumne meri Sita dekhi?
Jiski aankhen tumhari jaise thi?”

“O Haathi,
kya tumne usse dekha?
Jiski kamar tumhari soond jaisi thi…”

“O Sher (tiger),
agar tumne meri komal-man ki Sita dekhi ho, toh batao.”

🫢 Rama starts hallucinating

Achanak Rama ko lagta hai Sita chhup rahi hai.

Woh cheekhte:

“Sita! Mujhe dhokha mat do!
Main tumhe dekh sakta hoon!
Tum peeli saari me chhup nahi sakti!”

Par jise woh Sita samajh rahe the…
woh sirf pedon par pada hua saaya tha.

Unki awaaz toot jaati hai:

“Nahi… yeh Sita nahi.
Meri Sita toh mar gayi hogi…
Varna mere dukh se be-asar kaise reh sakti hai?”

💔 Rama imagines the worst

Rama bilkul tut jaate hain.

“Uska moonh chand jaisa tha…
sharbat jaisi komal twacha…
jaise chameli ka phool…
woh sab barbaad ho gaya.”

“Kisi ne uska gala kaat diya hoga.
Bechari… akeli… be-sahaara.”

Phir woh aasmaan ki taraf dekh kar cheekhte hain:

“Indra ki kasam… Sita!
Tum kahan ho?
Mujhe ek baar bula lo!”

🌪️ Like a madman

Rama jungle me daudte rehte hain:

kabhi chakravat (whirlwind) ki tarah,

kabhi deewane ki tarah,

kabhi pahaad chadhte,

kabhi nadiyon me jhaankte,

kabhi pedon ke neeche jhukkar pukaarte.

“Sita! Sitaaaa!”

Aakhir…
itna ro kar, itna bhaag kar, itna dukh jhel kar—
Rama bilkul thak jaate hain.
Unki saansein tezi se chal rahi hoti hain.
Unka sharir hila nahi jaata.

Jungle me unki pukaar goonjti rehti hai,
par jawab koi nahi deta…
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter61
    with st.expander("Chapter 3.61 – Rama expresses his sorrow"):
        text1 = """
Rama aur Lakshmana jab ashram wapas aaye, toh poora jhopdi aur van soona (empty) lag raha tha.
Ghaas ke aasans idhar-udhar bikhar gaye the.
Aur Sita kahi nahi thi.

Rama ne apne dono haath upar uthaye aur dard bhari awaaz me bola:

“Lakshmana! Vaidehi kahan hai?
Kaun usse le gaya?
Kaun meri pyari Sita ko kha gaya ya chhupa liya?”

Rama bechain hokar pukaarne lage:

“Sita! Agar tum kisi ped ke peeche chhupi ho, toh ab mazaak mat karo.
Main bahut tadap chuka hoon!”
        """
        create_image_text_layout("attached_assets/chapter3/3.61.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Unhone kaha:

“Woh hariniyo (female deer) jinke saath Sita khelti thi,
woh bhi udaas hain.
Main Sita ke bina ek pal nahi reh sakta.”

Phir Rama ne socha:

“Shayad main mar jaaun…
aur apne pita Dasharatha se baad me milun.
Woh mujhe kahenge—
‘Tumne mujhe diya hua vachan (promise) toda,
aur Sita ko akela chhod diya!’”

Is vichaar se Rama aur toot gaye.
Unka dard aisa tha jaise koi bada hathi kichad (marsh) me phas gaya ho.

❤️ Lakshmana ka Santvana (consolation)

Lakshmana ne shaant awaz me kaha:

“Bhaiya, himmat rakho.
Aao, milkar dhundte hain.
Yeh pahaad mein bohot gufaayein (caves) hain.
Ho sakta hai Sita phool lene ya jal bharne gayi ho.
Shayad woh humse mazaak kar rahi ho
aur chhupkar dekh rahi ho ki hum use dhundte hain ya nahi.
Chaliye, bina deri ke use dhundte hain!”

Rama ko thodi tasalli mili.
Dono bhai har taraf gaye—
pedon ke neeche, pahaadon par, nadi kinare, jheelon me,
gufao me, pattharon ke beech…

Par Sita ka ek bhi nishaan nahi mila.

😔 Rama ka tootna

Ant me Rama ne thake hue shabdon me kaha:

“Lakshmana…
maine poora van dekh liya.
Koi chinh (trace) nahi mila.
Meri Vaidehi…
meri praan (life-breath)…
kahi nahi hai…”

Yeh kehte-kehte Rama ka mann toot gaya.
Unhone behoshi jaise dard me swayam ko girne diya.
Unka sharir kaanpta tha.
Unki saansen tez thi.
Aur aankhon me aansu bhar aaye.

Phir bhi woh bas ek hi naam pukarte rahe:

“Sita! Sita!”

Lakshmana unhe sambhalne ki koshish karta raha,
haath jodkar, prem se,
par Rama ne kuch nahi suna.
Unka hriday (heart) sirf Sita ki yaad se bhar gaya tha.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter62
    with st.expander("Chapter 3.62 – Rama feels deep despair"):
        text1 = """
Sita ke bina, kamal-nayan (lotus-eyed) Rama bilkul tut chuke the.
Unka mann dard se bhar gaya tha.
Woh har taraf Sita ko dhoondte, par nahi dekh pa rahe the.
Phir bhi woh usse aise baat kar rahe the jaise Sita saamne ho.

🌿 Rama ka Sita ko pukarna

Rama ne dukhi awaz me kaha:

“Sita! O Sundari!
Ashoka ke phool bhi tumhare roop se kam sundar hain.
Mujhe pareshaan mat karo. Bas saamne aa jao!”

Woh har jhaadi ko dekhkar bolte:

“Tum yahan छुपी ho kya, priye?
Tumhari hansi mujhe dard de rahi hai.”

Phir jor se pukara:

“O vishaal-nayana (large-eyed) Sita!
Tumhara jhopda bilkul akela ho gaya hai…
Wapas aa jao.”

Par Sita nahi mili.
        """
        create_image_text_layout("attached_assets/chapter3/3.62.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
😢 Rama ka dard aur shanka

Rama ne hichkiyon ke saath kaha:

“Lakshmana…
shayad rakshason (demons) ne Sita ko utha liya.
Isliye woh saamne nahi aa rahi.
Sita kabhi mere dukh me mazaak nahi karti.”

Rama ne aas-paas me khade hiranon ko dekha.
Unki aankhon me aansu the, jaise woh kuch kehna chahte ho.

Rama bola:

“Lakshmana, dekho…
ye hiran bhi soch rahe hain ki Sita ko raat-ke-bhayanak yoddha (Rangers of the Night) kha gaye!”

💔 Rama ka sabse bada dar

Rama ne dard me kaaha:

**“Kaikeyi ka sapna poora ho gaya.
Main Sita ke saath van me aaya tha.
Aur ab… akela wapas jaaunga.

Lok kya kahenge?
‘Rama dil-ka-sakht aur kaayar (coward) hai!’”**

Unhone aur bhi kaha:

**“Janak Raja mujhe bina Sita ke dekh kar toot jayenge.
Unka dukh unhe pagal kar dega!
Main Ayodhya bilkul nahi jaaunga.
Bharat raj kare—yeh hi achha hai.

Lakshmana, tum Ayodhya wapas jao.
Apni mataon ko mera pranam kehna.
Aur unhe kahna ki Sita aur Rama… van me hi chale gaye.”**

Is baat ko keh kar Rama phir se ro pade.

😞 Lakshmana ka dard

Lakshmana, jo hamesha mazboot rehta tha,
ab peeche se safed (pale) pad gaya.
Unka mann hil gaya tha.
Woh darte the ki unka bhai unke aankhon ke saamne toot na jaaye.

Aur dono bhai Sita ko dhoondte hue
dukhi van me aage badhte rahe.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter63
    with st.expander("Chapter 3.63 – Rama continues to cry for Sita"):
        text1 = """
Sita ke bina, Rama ka dukh aur zyada gehra hota gaya.
Woh bilkul thak gaye the—mann se, sharir se, umeed se.
Lakshmana ko bhi unki halat dekhkar bahut dard ho raha tha.

🌑 Rama ka dard bhara maan

Rama ne bhari saanson ke saath kaha:

“Lakshmana, is duniya me mujhse zyada dukhi koi nahi.
Ek ke baad ek pareshani meri zindagi me aise gir rahi hai jaise toofaan.
Lagta hai maine pichhle janmon me bahut paap (evil acts) kiye honge.”

Woh apne dukh ko yaad karne lage:

Rajya ka kho jaana

Maa aur parivaar se doori

Vanvaas ki kathin (harsh) zindagi

Rama bole:

“Yeh sab dukh kisi tarah seh liye the…
par Sita ka kho jaana sab dard phir se jaga raha hai.”
        """
        create_image_text_layout("attached_assets/chapter3/3.63.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
💔 Rama ke mann me bhayanak tasveer

Rama ne toot kar kaha:

**“Meri komal, sharmili Sita ko kisi rakshas (demon) ne aasman me utha liya hoga.
Woh darr ke maare cheekh rahi hogi…

Uska khoon… uska peela vastra…
sab zameen ke dhool aur khoon me mil gaya hoga.”**

Unki awaaz phat gayi:

“Sita ki madhur awaaz, uski hanss, uski lachak—
sab rakshason ne cheen liya!”

Rama sochne lage:

**“Shayad uski sundar gardan, jo motiyon ke haar se saja tha,
kisi sunsaan jagah rakshas kaat rahe honge…

Aur meri Sita, usne shayad pukara hoga—
‘Rama! Rama!’
par main wahan nahi tha…”**

🌿 Yaadon ki chot

Rama ne bechain hoke kaha:

**“Lakshmana, yaad hai?
Isi ghaati (valley) me Sita baithi thi.
Mujhe muskura kar baat karti thi…

Ab woh kahaan chali gayi?”**

Phir unhone Godavari nadi ko dekha:

“Kya woh yahan phool todne aayi hogi?
Par nahi… Sita kabhi akeli nahi jaati thi.
Woh akeli van me kadam tak nahi rakhti thi!”

☀️ Surya aur Vayu ko pukarna

Rama ne aasman ki aur haath uthakar kaha:

“O Surya (Sun God), tum sab dekhte ho.
Batao—kya Sita bhatak gayi, ya koi utha le gaya,
ya… woh ab nahi rahi?”

Phir hawa se bole:

“O Vayu (Wind God), tum sab jante ho.
Sita ka kya hua? Batao!
Main is dukh se mar jaaunga!”

💛 Lakshmana ka santvana (consolation)

Lakshmana ne apne raazi-mand (duty-bound) dil se kaha:

“Bhagwan Rama, himmat rakhiye!
Dukh me tootna veeron (heroes) ka swabhav nahi.
Chaliye—hum talash jaari rakhte hain.
Hum Sita ko dhoond nikaalenge!”

Par Rama apne dukh me doob chuke the.
Lakshmana ki baatein unke dil tak nahi pahunchi.
Aur woh phir se rote hue Sita ka naam lene lage.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter64
    with st.expander("Chapter 3.64 – Rama becomes angry at the situation"):
        text1 = """
Sita ke bina dukhi Rama ne toote hue shabdon me Lakshmana se kaha:

“Lakshmana, turant Godavari nadi jao.
Ho sakta hai Sita wahan kamal (lotus) lene gayi ho.”

Lakshmana bina der kiye wahan gaye.
Unhone poori nadi, teerth (holy spots), kinare sab dekh liya.
Par Sita kahin nahi mili.

Wapas aa kar Lakshmana bole:

“Rama, maine sab jagah dekh liya.
Sita kahin nahi hai.”

🌊 Rama ka Godavari ko pukarna

Yeh sunte hi Rama khud nadi ke kinare bhaage aur zor se pukare:

“Sita! Sita! Kahan ho?”

Par Godavari chup rahi.
Jungle ke devata (spirits) bhi kuch nahi bole.
Sab ko pata tha ki Ravana, Lanka ka raja, Sita ko le gaya hai.
Par sab dar rahe the.

Rama bohot dukh se bole:

“Godavari bhi kuch nahi keh rahi…
Ab main kya mooh dikhau Janaka aur Sita ki maa ko?
Main unke saamne kaise jaun Sita ke bina?”
        """
        create_image_text_layout("attached_assets/chapter3/3.64.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
🦌 Jungle ke janwar Rama ko raasta dikhate hain

Rama ne phir deer (hiran) ko dekha.
Woh unko ek tarah se ishara kar rahe the.

Rama ne unse pucha:

“Kya tumne Sita ko dekha?”

Hiran uth kar dakshin ki disha (south direction) me dekhne lage.
Kabhi Rama ko dekhte, kabhi aasman ki aur, phir daud kar aage jaate.

Lakshmana samajh gaye:

“Bhaiya, ye hiran hume dakshin le ja rahe hain.
Chaliye, shayad wahan koi nishaan mile.”

🌺 Rama ko Sita ke pehchane hue phool milte hain

Dakshin jaate hue Rama ko kuch phool zameen par gira hua dikhai diya.

Unhone dard se kaha:

“Lakshmana, ye wahi phool hain jo maine Sita ko diye the.
Woh inhe apne baalon me lagati thi…”

Rama ka dil phat gaya.

🏔️ Rama pahaad aur nadi ko dhamkate hain

Rama ne pahaad se kaha:

“Hey parvat! Kya tumne Sita ko dekha?
Yadi nahi bataya toh main tumhe tora-doonga!”

Par pahaad chup.
Woh bhi Ravana se dar raha tha.

Rama gusse me bole:

“Lakshmana, agar yeh nadi ya pahaad Sita ka pata nahi bataenge,
toh main sab ko sukha dunga… jala dunga… mita dunga!”

Rama ka gussa ab toofan jaisa tha.

👣 Rama ko saboot milta hai

Phir achanak unhe bade kadam (giant footprints) dikhe.
Wahin paas Sita ke chhote kadam bhi the—
idhar-udhar bhage hue, darr ke nishaan.

Phir tootaa hua dhanush, tooti hui rath, khoon ke boonde, giraheni (ornaments)…
Sab kuch pada tha.

Rama ne darr aur gusse se kaha:

“Lakshmana, yeh sab Sita ka hai.
Yahan bhayanak ladaai hui hogi.
Ravana jaise rakshas yeh sab tod kar Sita ko utha le gaye honge!”

🔥 Rama ka maha-krodh (great wrath)

Rama ka chehra bijli ki tarah chamakne laga.

Unhone kaha:

**“Lakshmana, agar devata Sita ko abhi wapas nahi laaye…
toh main teenon lokon ko vinasht (destroy) kar doonga!

Suryadev ruk jaayenge,
chand dikhna band ho jayega,
pahaad toot jayenge,
nadiyaan sukh jayengi!

Meri baan (arrows) aasman bhar denge,
koi bhi bach nahi payega!”**

Lakshmana ne dekha—
Rama ne apna dhanush khinch liya,
aur ek zehrili saanp jaisa teer uthaya.

Rama bole:

“Aaj hi… issi din…
ya toh Sita wapas milegi,
ya main poore brahmand (universe) ko mita dunga!”

Is gusse me Rama Rudra jaisa pralay (doomsday) laane ko tayyar lag rahe the.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter65
    with st.expander("Chapter 3.65 – Lakshmana tries to calm Rama"):
        text1 = """
Sita ke bina dukhi Rama ka gussa pralay aag (end-of-world fire) jaisa ho gaya tha.
Unhone apna dhanush utha liya, jaise ki poori duniya ko jala denge.

Lakshmana ne pehli baar Rama ko itne krodh me dekha.
Unka chehra safed pad gaya.
Hath jodkar woh bole:

🙏 Lakshmana ka Vinamra Updesh

**“Bhaiya Rama…
Aap hamesha komal (gentle), shaant aur sabka bhala karne wale the.
Aaj aap apni asli prakriti (true nature) se kyun hat rahe ho?

Aapka tej (radiance) chaand ki shitalta, suraj ki roshni, hawa ki gati aur dharti ki sahansheelta (forbearance) jaisa hai.
Aisi shaan ko ek rakshas (demon) ki wajah se kyun bigaad rahe ho?”**

Lakshmana ne zameen par pade nishaan dekh kar kaha:

**“Hume pata hi nahi kiski rath yeh thi.
Kaun ladaa, kyun ladaa, kuch bhi to spasht nahi hai.
Yeh toh ek-do logon ki ladaai lagti hai, senaon (armies) ki nahi.

Toh poori duniyan ko mita dena theek kaise ho sakta hai, Bhaiya?”**
        """
        create_image_text_layout("attached_assets/chapter3/3.65.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
🌍 “Rajadharma” ka yaad dilana

Lakshmana ne dheere se samjhaya:

“Raja ka kartavya (duty) daya, nyaay (justice) aur sammata (moderation) se chalna hota hai.
Aap sabka aasra (refuge) ho, sabka sahara.
Kaun sahay karega agar aap hi sabko nasht kar doge?”

Phir Lakshmana ne satya kaha:

“Jo Sita ko le gaya, uska dundh (search) karna humara kaam hai.
Chalo hum dono saath milkar dhundhte hain.
Hum paani, pahaad, jangal, gufa, jheel sab talaashenge.
Hum devta, gandharva sab se poochhenge.”

🏹 Lakshmana ka vachan

Lakshmana ne ant me kaha:

“Bhaiya, pehle daya, vinamrata (humility), buddhi aur shanti se kaam lete hain.
Agar phir bhi Sita na mile…
tab aap apne teer chala kar andhere badal (storm clouds) jaise ghor pralay kar dena.
Main hamesha aapke saath hoon.”
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter66
    with st.expander("Chapter 3.66 – Lakshmana gives courage to Rama"):
        text1 = """
Rama abhi bhi dukh me dooba hua tha.
Jaise koi poori duniya me akela pad gaya ho.
Uska mann toot chuka tha.
Uski saanson me sirf Sita ka dard tha.

Lakshman, jo apne bhai se gehra prem karta tha,
Rama ke pair pakad kar baith gaya.
Unhe dabaane laga—jaise maa apne bachhe ko sambhalti ho.

Phir Lakshman ne pyaar se kaha:
        """
        create_image_text_layout("attached_assets/chapter3/3.66.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
🌿 “Bhaiya, sambhal jao.”

“Bhaiya… Pitaji Dasharatha ne aapko bahut tapasya se paaya tha.
Jaise devtaon ne amrit paaya tha—waise pitaji ne aapko paaya.

Aapke jaise putra ko paa kar
Pitaji khushi khushi swarg chale gaye.
Yeh baat humein Bharata ne batayi thi.

Agar aap jaise veer dukh nahi jhel sakte,
toh aam aadmi kya karega?”

🔥 “Dukh sabko aata hai.”

“Bhaiya, koi bhi jeevan ho—
dikkatein to aati hi hain.

Dukh aag ki tarah aata hai…
Tez, jalta hua…
Phir dheere dheere chala bhi jaata hai.

Is duniya ka niyam hi yeh hai.

Kya Raja Yayati swarg se nahi gira tha?
Kya Vasishtha Muni ke 400 putr ek din me na mare the?

Dharti Maa bhi kabhi kabhi kaanp uthti hai.
Suraj-chand… jo sabko roshni dete hain…
Woh bhi to grahan jhelte hain.”

🌙 “Devta bhi kismat ke aage jhukte hain.”

“Devta bhi takleef se guzarte hain, Bhaiya.
Jab devta tak dukh se bachte nahi—
toh hum manushya kaise bachenge?

Isliye aapko roop badal kar
aam aadmi ki tarah dukh nahi manana chahiye.”

💔 “Chahe Sita devi ki mrityu bhi ho gayi ho…”

Lakshman ne dheere se kaha:

“Bhaiya, chahe Sita ji mar gayi ho…
ya unhe utha kar le gaye ho…
aapko tootna nahi chahiye.

Aap Raja hain.
Jinke dil me samay hota hai,
wo har sthiti me samyak vivek (right judgement) rakhte hain.”

⚔️ **“Aapne mujhe hamesha sikhaya hai—

ki kaam ko waqt par karna chahiye.”**

“Bhaiya, aap hi ne mujhe samjhaya tha
ki kaam chhod dene se parinaam nahi milta.

Aapne hamesha mujhe sikhaaya hai.
Aapko kaun sikha sakta hai?
Brihaspati bhi nahi.

Aapka gyaan devta bhi naap nahi sakte.”

🐯 “Ab uth kar tayyar ho jao!”

Lakshman ne zor se kaha:

“Bhaiya,
Is dukh ne aapke andar ki shakti ko chhupa diya hai.
Main us shakti ko fir jagana chahta hoon.

Devtaon ki shakti dekh lo.
Manushyon ki shakti dekh lo.
Aur apni shakti bhi yaad karo.

Duniya ko jalane se kya milega?
Us ek dusht raatri-char ko dhundho…
aur use samaapt kar do, Bhaiya!

Woh hi hamara dushman hai.
Usi ko maarna hamara dharm hai.”

Lakshman ke shabdon me pyaar bhi tha,
samajh bhi thi,
aur ek veer ka utsaah bhi.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter67
    with st.expander("Chapter 3.67 – Rama finds the injured Jatayu"):
        text1 = """
Lakshman ke buddhi-bhare shabdon ne
Rama ka gussa shaant kar diya.
Rama ne gehri saans li.
Usne apna dhairya fir se sambhala.

Bow par sahara le kar Rama bole:

“Lakshman… ab kya karein?
Kis disha me jaayein?
Sita ko kaise dhundhe?
Sochna hoga.”

Lakshman turant bole:

“Bhaiya, Janasthana chalte hain.
Wahan bahut rakshas rehte hain.
Ghane jungle, gehri gufaayein, pahaadi darre,
aur anek ajeeb jeevon ka raaj hai.
Hum dono mil kar har kona dhoondhenge.”

Rama ne haan me haan milayi.
Dono bhai teer-dhanush lekar
ghane van me ghus gaye.
        """
        create_image_text_layout("attached_assets/chapter3/3.67.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
🌳 Jungle me ek bada sa pakshi pada tha…

Thodi door jaate hi
Rama ne kuch dekha.

Ek vishal pakshi…
Jise dekh kar lagta tha jaise
koi pahaad ka tukda zameen par gir gaya ho.

Woh poori tarah khoon se rangeen tha.
Bina hile lade pada tha.

Rama ka mann phat pada:

“Lakshman! Yeh dekho!
Yeh koi rakshas hoga
jo vulture ka roop banakar
Sita ko kha gaya hoga!

Isne Sita ko maar diya hoga
aur ab araam se so raha hai!
Isse abhi maar daalta hoon!”

Rama ne teer chadha diya.
Gussa unki aankhon me bijli ki tarah chamak raha tha.

Woh pakshi thodi der me bol utha—
Uski awaaz kamzor thi, dard se bhari thi.

🦅 “Rama… ruk jao. Main Jatayu hoon…”

Pakshi bola:

“Rama…
Main tumhare pita ka mitra…
Jatayu hoon.

Sita ko maine apni aankhon se dekha…
Ravana use utha le gaya.”

Rama ka teer haath se gir gaya.
Woh pattar ki tarah jam gaye.

Jatayu bolta gaya:

“Tum dono ke jaane ke baad
Ravana Sita ko kheech kar le ja raha tha.

Main uda…
aur usse rok diya!

Uska rath tod diya…
chhatra gira diya…
aur uska saarathi mar dala.

Par Ravana bahut balwaan tha.
Usne talwar se mere dono pankh kaat diye.

Phir Sita ko le kar asmaan me udd gaya.
Main yahin gir gaya…

Mujhe mat maaro, Rama.
Main tumhara dushman nahi…
Main tumhara pita ka dost hoon.”

💔 Rama ka dil toot gaya

Yeh sunte hi
Rama Jatayu par gir pade
aur use gale laga liya.

Unki aankhon me aansu bhar aaye.

“Lakshman…
dekho meri kismet!

Rajya gaya…
vanvaas mila…
Sita chali gayi…
aur ab pitaji ka mitra
mere saamne mar raha hai.

Meri durdaasha to
samundar ko bhi sookha de.”

Rama baar baar Jatayu ke sharir ko chhoone lage.
Aankhon me prem… dukh… kripa… sab tha.

Phir
Rama ne Jatayu ko apni baahon me uthaya
aur puchha—

“Jatayu…
Sita kahan gayi?
Meri jaan se pyari Sita kahan hai?”

Rama zameen par gir pade.
Lakshman unhe sambhalte rahe.

Jungle me sirf
Rama ke rote hue shabdon ki goonj reh gayi.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter68
    with st.expander("Chapter 3.68 – Jatayu dies after telling Rama what happened"):
        text1 = """
Rama Jatayu ke paas baith gaye.
Jatayu zameen par pada tha…
Khoon me lathpath…
Saans dheemi…
Aankhen dhundhli.

Rama ne dukh bhari awaaz me Lakshman se kaha:

“Lakshman…
Is pakshi ne meri raksha ke liye
apni jaan daal di.
Ravana se ladte-ladte
yeh toot chuka hai.

Uski saansein kat rahi hain.
Aankhen band ho rahi hain.
Woh bol bhi nahi pa raha.

O Jatayu…
Agar bol sakte ho
to batao…
Sita ka kya hua?

Ravana ne use kis liye le gaya?
Us waqt Sita ka chehra kaisa tha?
Usne kya kaha?
Woh rakshas kaisa dikh raha tha?
Kahan rehta hai?
Batao, dost!”
        """
        create_image_text_layout("attached_assets/chapter3/3.68.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
🦅 Jatayu ki akhri baatein

Jatayu ne bahut mushkil se apna sir uthaya.
Uski awaaz toot rahi thi.

“Rama…
Sita ko Ravana le gaya.
Woh rakshaso ka raja hai.
Jadoo jaanta hai…
Toofan jaise bal rakhta hai.

Maine use roka.
Uska rath toda.
Uska saarathi maara.

Par mein thak gaya tha.
Ravana ne apni talwar se
mere dono pankh kaat diye.

Phir Sita ko pakad kar
dakhshan disha me udd gaya…

Rama…
Meri aankhen dhundhla rahi hain.
Main sooraj jaisa peela prakash dekh raha hoon.
Mera waqt aa gaya hai…

Lekin ek baat suno—
Ravana ‘Vindhya kaal’ me Sita ko le jaa raha tha.
Us samay jo cheez kho jaati hai
woh fir mil jaati hai.

Iska matlab…
Ravana ki maut likhi ja chuki hai.

Rama…
Sita tumhe wapas milegi.
Tum jeetoge.
Tum dono fir saath hoge…”

Jatayu ke muh se khoon bahne laga.
Uski saans tez ho gai…
Phir achanak ruk gai.

Ant me usne ek baat boli:

“Ravana… Vishrava ka beta hai…
Vishravana ka bhai…”

Aur phir
Jatayu ki aankhen band ho gayi.
Jaan nikal gayi.

💔 Rama ki cheekh

Rama cheekh uthe:

“Jatayu!!
Aur bolo!
Mat jao!”

Par Jatayu ka shareer thanda ho chuka tha.
Uski aankhen sookh gayi thi.
Uska sar, pair, pankh sab dheele pad gaye.

Rama neeche gir pade.
Unka dil tootta ja raha tha.

“Lakshman…
Yeh pakshi ne saalon tak jungle me jeevan bitaya.
Aaj meri seva me jaan de di.

Apne kul ka raaj chhod diya
sirf isliye ki Sita ko bacha sake.

Lakshman…
Aisi dharm-nishta to insano me bhi mushkil hai!”

Rama ki awaaz kanp rahi thi.

“Sita ke jaane ka dard
itna gehra nahi tha
jitna Jatayu ke marne ka hai.”

🔥 Jatayu ka Antyeshti

Rama ne kaha:

“Lakshman, lakdi lao.
Aaj main apne pita ke mitra ka
swatah antim sanskar karunga.”

Lakshman ne ghee ki lakdiyaan jama ki.
Rama ne Jatayu ko apni baahon me uthaya.
Jaise pita ka shareer utha rahe ho.

Usse chita par rakha.
Aankhon me aansu lekar
agni lagayi.

Aag ke jwalon me
Jatayu ka shareer chamak utha.
Jaise uski atma
aasmaan me oonchi udaan bhar rahi ho.

🥩 Rama ka shraddh–bhoj

Antyeshti ke baad
Rama aur Lakshman ne
kuch mote Rohi hiran mare.

Unke maans ke gol banaye
aur hara ghaas par rakhe:

“Yeh sab Jatayu tumhare liye…
Tum veer the…
Tum ne dharm nibhaya.”

Fir dono bhai
Godavari nadi gaye.
Pani chhoda.
Prarthna ki.

“Jatayu…
Tum dev-lok jao.
Veeron ka sthan tumhara hai.”

Shraddh poora karke
Rama aur Lakshman
dubara jungle me nikal pade.

Unki aankhen laal thi…
Dil me aag thi…

Sita ko dhoondne ka sankalp
aur bhi gehra ho chuka tha.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter69
    with st.expander("Chapter 3.69 – Rama and Lakshmana meet Ayomukhi and Kabandha"):
        text1 = """
Jatayu ki kriya karke
Rama aur Lakshman fir jungle me chale.
Disha thi—dakshin–pashchim.
Raasta jungli, gehra, kaanton se bhara,
ghanaa aur daraavna.

Par dono veer the.
Dono chal padhe.

🌳 Krauncha Jungle

Kuch door chalne ke baad
voh Krauncha van me pahunche—
baarish ke baadal jaisa gehra,
phoolon se bhara,
hiran aur pakshiyon se sajja hua.

Par Rama ka dil halka nahi hua.
Unki nazar har taraf Sita ko dhoond rahi thi.

🏞️ Matanga ka Ashram

Teen kos aur chalne ke baad
voh Matanga Rishi ke ashram ke paas aaye.
Fir unhe ek gufaa dikhai di—
andhera, gehra, daraavna,
jaise zameen ke neeche ka lok.

Usi jagah
ek bhayankar rakshasi saamne aa gayi.
        """
        create_image_text_layout("attached_assets/chapter3/3.69.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Uska chehra daravna.
Sharir bada sa.
Aawaz kadak.
Bade daant.
Bada pet.
Aur voh hansi…

“Idhar aao, sundar veeron,”
rakshasi boli,
“Hamara saath prem se samay bitao.”

Aur turant
Lakshman ka haath pakad liya.

“Main Ayomukhi hoon,”
woh garji,
“Main tumhari hoon—
Lakshman, mera pati ban jao.
Hum dono pahaadon par aur nadiyon ke beech
maze se jeeyenge.”

Lakshman ka khoon khol gaya.

Ek pal me
usne talwar nikali
aur Ayomukhi ke kaan, naak, aur stan kaat diye.

Cheekh maar kar
rakshasi bhaag gayi.

Rama aur Lakshman aur gehre jungle me pravesh kar gaye.

⚠️ Bure Sanket

Lakshman ne dheere se kaha:

“Bhaiya…
Meri baayen baahu phadak rahi hai.
Dil ghabra raha hai.
Har taraf ashubh sanket hai.
Par ek pakshi ki cheekh se lagta hai
jeet humari hogi.”

Rama ne haan me sir hilaaya.

Dono aur andar badhe.

🌪️ Achanak Tez Dhadaka

Achaanak
ek zor ka shor hua.
Jaise aandhi ne pura jungle hila diya ho.

Rama ne dhanush sambhala.
Lakshman ne talwar.

Dono ne aage jaakar dekha…

Aur unka kadam ruk gaya.

🦾 Kabandh – woh be–sar rakshas

Ek raat jaisa kaala,
pahad jaisa bada,
sir–bina rakshas unke saamne tha.

Uska mooh uske pet me tha.
Ek bada, peela eka–ankh uski chhati me chamak raha tha.
Haath itne lambe
ki chaar kos door ka jaanwar pakad le.

Kabandh tedhi hansi hansa
aur dono ko ek hi jhatke me
apni baahoon me pakad liya.

Lakshman karah uthe.
Unka badan kaanp gaya.

“Bhaiya…”
Lakshman boli,
“Mujhe chod do.
Main is rakshas ke hawale ho jaata hoon.
Aap bach jao…
Aap Sita ko pa loge.
Aap Ayodhya laut kar raajyabhishek karwao…
Bas mujhe yaad rakhna.”

Rama ne kathor par shant awaaz me kaha:

“Lakshman, shant ho jao.
Tum jaise veer kabhi ghabraate nahi.”

👹 Kabandh ka swar

Kabandh garja:

“Tum kaun ho?
Tumhari baahen saand jaisi balwaan.
Tumhare paas dhanush–talwar.
Tum mere muh me aa gaye ho.
Tumhari maut nishchit hai.”

Rama ne Lakshman ko dekha.

“Lakshman…
Hum ek musibat se nikle
to ek aur badi musibat aa gayi.

Lagta hai
Sita tak pahunchne se pehle
kismat humari pariksha le rahi hai.

Mujhe lagta hai
aaj hamari jaan bhi ja sakti hai…
Sita se milna…
shayad ab mushkil ho jaaye.”

Rama ne aise kaha—
par unki aankhon me
ab bhi shaanti thi.

Unka mann mazboot tha.

Aur yahin se
Kabandh ka asli kissa shuru hota hai.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter70
    with st.expander("Chapter 3.70 – Rama and Lakshmana cut off Kabandha’s long arms"):
        text1 = """
Kabandh ne dono bhaiyon ko
apni lambe–lambe baahoon me jakkad liya.

Hansi karte hue bola:

“Arre veeron, kya ho gaya?
Tum dono to aaj mere bhojan banne vale ho.
Bhagya ne tumhari buddhi hi chheen li hogi
jo tum mere haath aa gaye.”

🗡️ Lakshman ka sankalp

Lakshman dard me the,
par unhone himmat nahi haari.

Dheere se Rama se bole:

“Bhaiya…
Yeh rakshas hame zinda nahi chhodega.
Iski haath bahut taakatvar hain—
sabko daboch leta hai.

Hum dono ko turant apni talwar se
iske dono baahen kaat deni hongi.

Yeh be-baas bhed ki tarah katne ke liye nahi—
par hum veer hain,
aur veer haath par haath rakhkar nahi marte.”

Rama ne sir hilaaya.
Nishchay ho gaya.
        """
        create_image_text_layout("attached_assets/chapter3/3.70.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
Kabandh dono ko apne muh ki taraf kheech raha tha.

Par usi pal
Rama aur Lakshman ne
ek saath,
tezi se,
poori sharir ki shakti jodkar
vaar kar diya.

Rama ne uska daaya haath kaat diya.

Lakshman ne ek zor daar prahar me baaya haath kaat diya.

Kabandh ke dono baahen
zameen par gir gayin…
rakt dhaara ki tarah behne laga.

Uski cheekh ne
zameen aur aasman
dono ko hila diya.

🩸 Kabandh ka prashna

Dard se karah kar
Kabandh zameen par gir pada.

Dheere, lachar awaaz me bola:

“Tum… tum kaun ho?
Kaun ho tum veeron
jo mere haath kaat gaye?”

🦁 Lakshman ka uttar

Lakshman ne uska prashna suna
aur
Rama ki mahima
batate hue kaha:

“Yeh Rama hain—
Ikshvaku vansh ke veer,
dharma ke rakshak.

Main unka chhota bhai Lakshman hoon.

Kaikeyi ne dhokha dekar
Rama ka rajya chheen liya,
aur hum tino—main, Rama, Sita—
van me rehne aa gaye.

Par ek dusht rakshas
Sita ko chheen le gaya.
Isi liye hum use dhoond rahe hain.

Aur tum?
Tum kaun ho
jo aise daravne roop me jungle me bhatak rahe ho?”

🌟 Kabandh ka roop-ras aur satya

Lakshman ki baat sunte hi
Kabandh ko Indra ke diye shraap yaad aa gaye.

Uski awaaz khushi se bhar gayi:

“Ahh… swagat hai tum dono ka!
Meri mukti ka samay aa gaya.

Tumne mere haath kaat kar
mujhe vardaan diya hai.
Suno—
kaise main is bhayankar roop me gira.”

Aur yahin se
Kabandh apni kahani batane lagta hai…
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter71
    with st.expander("Chapter 3.71 – Kabandha tells his story"):
        text1 = """
Kabandh—jiske baazu Rama–Lakshman ne kaat diye the—
ab dheere-dheere bolne laga.

Uski awaaz me dard bhi tha,
aur sukoon bhi—
jaise kisi ka bojh ab utar raha ho.

🌑 Kabandh ka sach

“Rama…
Main pehle aisa nahi tha.

Main bahut sundar tha.
Teenon lokon me meri shakti aur roop ki charcha thi.
Sooraj, Chandrama, Indra jaisa tej tha mera.

Par main ghamandi ho gaya.
Apna roop badalkar tapasviyon ko daraata tha.
Unhe pareshan karta tha.”

Kabandh ki awaaz me pachtava tha.

“Ek din maine
Rishi Sthulashira ko chidha diya.

Woh phal tod rahe the.
Main unke saamne apni badi, bhayanak shakal le aaya.

Unhone mujhe gusse me shraap de diya:

‘Hamesha isi daravne roop me confine ho jao!’”
        """
        create_image_text_layout("attached_assets/chapter3/3.71.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
🔥 Shraap se mukti ka vachan

Kabandh ne aage kaha:

“Maine Rishi se maafi maangi.
Unhone daya ki—
aur kaha:

‘Jab van me Rama tumhare dono baazu kaat kar
tumhara dahsanskaar karega,
tab tum apna asli roop paoge.’”

Lakshman ki taraf dekhkar woh bola:

“Main Danu-putra hoon.
Sundarta se bhara hua.
Yeh roop mera asli nahi.”

⚔️ Indra ka shraap

Phir Kabandh ne hansi-bhari kasak se kaha:

“Ek shraap aur bhi tha…
Indra ka.

Maine kathin tapasya ki.
Brahma ji ne mujhe amar jeevan ka var diya.

Main garv me bhar gaya.
Soche laga—‘Indra kya bigaad lega?’
Aur maine use lalkar diya.

Indra gusse me aa gaye.
Unhone apna vijra, sau-dhaari gadha,
zor se mujh par phenka.

Uske prahar se
mera sar aur jaanghe
mere sharir ke andar dhans gayi.

Main roya.
Maine kaha—‘Mujhe maar do, Indra.’

Par Indra bole:

‘Brahma ka var jhootha nahi ho sakta.
Tumhe jeena hi padega.’”

Kabandh ne shant swar me kaha:

“Main bola—‘Sar ke bina kaise jeeunga?’

Tab Indra ne
mere haath chaar kos (4 miles) lambe kar diye
aur mera muh mere pet me rakh diya.

Tab se main jungle me ghoom-ghoom kar
janwaron ko haath se pakadkar
pet ke muh me daalta raha.”

🌟 Mukti ki umeed

Kabandh ne gehri saans li.

“Indra ne fir kaha:

‘Jab Rama aur Lakshman tumhare baazu kaat denge,
tab tumhe svarg mil jayega.’”

Kabandh roya nahi,
par awaaz bhar aayi:

“Main tab se bas tum dono ka intezar kar raha tha.
Aakhir tum aa gaye.

Tumhare baazu kaatne se
mera shraap tootne laga hai.

Meri ek antim ichchha hai.
Mera dah sanskaar karo.
Phir main tumhe
ek aisa mitra batane wala hoon
jo tumhari Sita ko khojne me madad karega.”

🔱 Rama ka prashn

Rama ne shant par vyakul swar me poocha:

“Ravana ne meri Sita ko chura liya hai.
Na hum uska roop jaante hain,
na uski shakti,
na uska ghar.

Hum akela bhatak rahe hain.

Agar tum jaante ho—
batao—Sita kahan hai?”

🔮 Kabandh ka uttar

Kabandh dheere se bola:

“Rama…
shraap ke kaaran
mere paas divya drishti nahi hai.

Main Sita ko nahi jaanta.
Par…

jalte hi
apna asli roop paakar
main tumhe ek aisa veer bataaunga
jo sab kuch jaanta hai.

Tinon lok uske gyaan se chhupe nahi hain.

Usse tum dosti karna.
Woh tumhe Sita tak pahunchayega.”

Kabandh ne antim baar kaha:

“Surya doobne se pehle
mujhe
agnikriya
do, Rama.

Tab main tumhara margdarshan karunga.”
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter72
    with st.expander("Chapter 3.72 – Kabandha tells Rama how he can find Sita"):
        text1 = """
Kabandh ki aakhri ichchha poori karne ke liye
Rama aur Lakshman ne ek pahaadi ki taraf jaakar
ek gehra gaddha dhoonda.

Sukhe lakdi ke moote-mote thoonth liye.
Lakshman ne jalti hui mashaal uthai.
Dono bhaiyon ne milkar
Kabandh ka dahsanskaar shuru kiya.

Aag dheere-dheere bhadakti gayi…
zabaan jaise laal phool si phail rahi ho.

Kabandh ka bhayanak sharir,
jo kabhi sabko daraata tha,
ab makhhan ki tarah pighalne laga.

Aur phir—
jaise kisi ne andheron me deep jala diya ho—
uske bhasm me se ek roop nikla…

Chamakta hua, dev-samaan.
Safed vastra. Divya pushpon ki mala.
Sone ke gehne.
Tej aisa ki charon disha chamak uthi.

Ek swan-yukt divya rath aasman me aaya.
Kabandh—ab sundar, shapit roop se mukt—
us par chadhkar aasman me khada ho gaya.

Upar se zameen par khade Rama ko dekhkar bola:
        """
        create_image_text_layout("attached_assets/chapter3/3.72.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
🌟 “Rama, Sita ko kaise dhundo — ab suno.”

“Aap dono bahut dukh me ho.
Aur dukh ka bojh tab halka hota hai
jab koi saath ho.

Par tum dono ka koi saathi nahi…

Isliye pehla raasta—
dosti.”

Kabandh ki awaaz me gyaan tha.

🐒 “Ek vanara tumhari kismat badal dega.”

“Rama,
Pampa sarovar ke paas
Rishyamuk Parvat hai.

Wahaan ek vanara-raj Sugriva rehta hai—
apne chaar veeron ke saath.

Woh Indra ka putra Bali ka bhai hai.
Bahadur. Buddhiman.
Rupa-se-tez.
Dil ka sachcha.
Dharma ka pakka.
Aur apne bhai Bali ke dwara
rajya se nikala hua.”

“Woh tumhara sacha mitra banega, Rama.
Usse milo.
Usse haath milao.
Agni ko saakshi banaakar
mitrata ka bandhan baandho.”

🔱 Sugriva ko kyun?

Kabandh aage bola:

“Sugriva ka gyaan teenon lokon me phaila hua hai.
Asur kahaan chhupe hain,
kis pahaad me, kis gufa me—
use sab pata hai.

Aur jab tumhara mitra banega,
to apne vaanaron ko
chaaron dishaon me bhej dega.

Pahaad, dariya, janglaat,
gufaayein, gehre kuan,
Ravana ka rajmahal—
koi jagah chhodi nahi jayegi.

Chahe Sita
Mount Meru ki choti par ho,
ya paataal ki gehraiyon me band,
Sugriva usse dhoondh hi lega.

Aur agar zarurat padi—
poora raakshas kul mita dega.”

🌄 Kabandh ka antim sandesh

Kabandh ka rath aasman me aur upar uthne laga.

“Aaj se tumhari raah seedhi hai, Rama.
Bas Rishyamuk jao.
Apne baan neeche rakho.
Sugriva tumhe pehchaanega.
Aur tumhari kasht ki raat
khatm karne me madad karega.”

Phir ek komal hansi ke saath bola:

“Main tumhara udhaarimaan hoon.
Par tumhari yatra ab shuru hoti hai.”

Aur prakash ke saath
Kabandh antardhyan ho gaya…
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter73
    with st.expander("Chapter 3.73 – Kabandha gives final advice to Rama"):
        text1 = """
Kabandh ne Sita tak ka raasta bata diya tha…
Ab usne Rama ko ek gehra aur kaam ka updesh diya.

Upar aasman me chamak raha Kabandh—
devi mala pehne, divya roop me—
narm awaaz me bola:

🌳 “Rama, yeh raasta Rishyamuk Parvat tak jaata hai…”

“Yeh raasta paschim (west) ki taraf mudta hai, Rama.

Is par chaloge to hazaaron phoolon se bhare ped milenge:

Jambu

Panasa

Nyagrodha (bargad)

Ashvattha (peepal)

Karnikara

Kadamba

Tilaka

Naktamala

Aur aur bhi bahut saare ped—
jinhe jhukakar tum unke meethay phal kha sakte ho.”

Kabandh ke shabd jaise ek tasveer bana rahe the…
        """
        create_image_text_layout("attached_assets/chapter3/3.73.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
🌺 “Yeh ban Nandana van jaisa hoga…”

“Aage chal kar tum ek aisa vana pahuncho ge
jaisa devtaon ka Nandana Garden.

Har mahine
har mausam ke phal—
saath-saath ugte hain.

Lakshman aasani se ped pe chadh jayega,
ya poora ped jhukakar tumhe phal dega—
jo Amrit (nectar) jaise meethay honge.”

🪷 “Pampa Sarovar pahunchoge…”

“Aakhir me tum dono
Pampa jheel tak jaoge—
jisme padme (lotus) khilte rehte hain.

Wahaan koi patthar, koi gaddha nahi,
paayal jaisi komal mitti.

Hans, batak, bagule, ospreys…
sab meethi awaaz me gaate milenge.
Koi inse shikar nahi karta—
isliye ye darte bhi nahi.”

Kabandh bola:

“Rama, ye moti jaise mote pakshi khana—
ye tumhari taakat badhayenge.”

Aur Lakshman tumhare liye
teer se machhliyan pakad kar
unhe aag par bhun-kar laayega—
ek haddiyon wali, naram aur swaadisht.

Phir tumhe kamal ke patte me
thandi, sugandhit paani pilaayega.

🐒 “Vanar tumhe ye sab jagah dikhaayenge…”

“Sandhya ko, Lakshman tumhe dikhayega
ki kaise vanar (monkeys)
jheel pe paani peene aate hain—
jangli, zor se dahadte hue.”

Phoolon se bhara ban…
Mehakti jheel…
inti sundar drishya
tumhare dukh ko halka kar denge.

🙏 “Wahaan Shabari milegi…”

“Matanga Rishi ka purana ashram wahin hai.
Uske shishya to swarg chuke…
par ek vriddh tapasvini (ascetic woman)
Shabari ab bhi wahaan hai.

Tumhe dekhte hi
woh tumhara swagat karegi
aur phir apne punya ke saath
swarg jaayegi.”

🐘 “Rishyamuk Parvat ke paas…”

“Rishyamuk Parvat Pampa ke saamne hi hai.
Bahut khubsurat, bahut kathin.

Yahaan:

jawaan haathi garajte hain

gehri gufaayein hain

ped phoolon se bhaare hue

neele rang ke hiran jaise manohar prani (creatures) milenge

Unhe dekh kar tumhara dukh aur halka hoga, Rama.”

🦍 “Wahaan Sugriva rahta hai.”

“Ek vishaal gufa
pahaad ke pet me bani hai.
Usi me Sugriva, vanaro ka raja,
apne mitron ke saath rehta hai.

Kabhi gufa me,
kabhi pahaad ki choti par—
par hamesha Pampa aur Rishyamuk ke aasapas.”

🌟 Kabandh ka Antim Vachan

Kabandh aasman me aur ooncha uth gaya,
suraj ki tarah chamakta hua.

Rama aur Lakshman ne neeche se pukara:

“Shubh yatra!”

Kabandh ne muskurakar jawaab diya:

“Jaao, Rama.
Tumhe tumhara lakshya milega.
Sugriva se mitrata banao.
Sita zaroor mil jayegi.”

Aur prakash me lapetkar
Kabandh antardhyan ho gaya…
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter74
    with st.expander("Chapter 3.74 – Rama meets Shabari"):
        text1 = """
Kabandh ke diye gaye raaste par chal kar
Rama aur Lakshman Pampa jheel ki ore badhe.

Raste me unhe pahaadon par ugay hue
phoolon aur phalon se bhaare ped mile—
jaise devlok ka bagicha.

Ek uchchi jagah par raat guzaarne ke baad
woh dono Pampa ke paschim kinare pahunche
aur wahan ek pyara sa ashram dikha…
Shabari ka ashram.

🌿 Rama-Shabari Milap

Jab Rama aur Lakshman ashram ke paas aaye,
to bahut vriddh (very old),
bahut pavitra tapasvini Shabari unhe dekh kar
khushi se khadi ho gayi.

Haste hue, haath jod kar
pehle Rama ke pair chhuye,
phir Lakshman ke.

Phir Shabari ne paramparagat tareeke se
unhe paani diya—
munh dhone ke liye,
pair dhone ke liye.

Rama ne pyaar se pucha:

“Hey tapasvini (ascetic lady),
kya tumhari tapasya (penance) safal ho rahi hai?
Kya tumne apna krodh (anger) aur bhook par niyantran pa liya?
Kya tumne apne Guru ki seva poori shraddha se ki?”
        """
        create_image_text_layout("attached_assets/chapter3/3.74.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
🙏 Shabari ka Dil se Diya Jawaab

Shabari ki aankhon me khushi ke aansu aa gaye.

“Prabhu!” woh boli,
“aaj meri zindagi safal ho gayi!

Aaj meri tapasya,
mera janam,
meri Guru-seva—
sab rang layi.

Mere Gurujan—wo mahaan tapasvi—
jab Chitrakoot par aap aaye,
tab swarg (heaven) ko chale gaye.
Jaate jaate unhone mujhse kaha tha:

‘Rama tumhare ashram aayenge.
Unka satkar karna.
Unhe dekhte hi tumhe
woh lok (world) milega
jahan se koi lautkar nahi aata.’

Isliye maine aapke liye
Pampa ke kinaare se
sare meethe jangli phal ikattha kiye hain, Prabhu.”

🌸 Rama ka Shabari se Anurodh

Rama ne narm awaaz me kaha:

“Shabari, maine tumhare Guru ki mahima suni hai.
Main unke chinh (signs) apni aankhon se dekhna chahta hoon.”

Shabari garv aur bhakti se chamak uthi.
Woh dono bhaiyon ko ashram ke andar le gayi.

🌄 Matanga Rishi ka Pavitra Van

“Dekhiye, Raghunandan,” woh boli,

“Yeh hai Matanga Van—
yeh jangal ab bhi unhi tapasviyon ki shakti se pavitra hai.

Yahaan unhone yagya kiya.
Yahaan unke haathon se chadhaye phool
ab tak murjhaaye nahi.

Yahaan dekhiye—
yeh hai pashchim-disha ko mukh kiya hua vedika (altar),
jahan unhone devtaon ko puja arpan ki.

Aur udhar—
woh saath samudra hain,
jinhne unhone apne dhyaan (meditation) se yahan laaya.
Kyuki budhape (old age) me wo chal nahi paate the.

Woh pedon par latke hue
bark ke kapde abhi tak geele hain…
yeh sab un tapasviyon ki pavitrata ka pramaan hai.”

🔥 Shabari ka Antim Vachan

“Aaj main sab kuch dekh liya,
sun liya…
ab Anumati (permission) dijiye,
ki main apna shareer chhod kar
apne Guru ke paas jaa sakoon.”

Rama ne daya se muskurakar kaha:

“Shabari, tumne humara
poora satkar kiya.
Ab jao, kalyan ho tumhara.”

✨ Shabari ka Swargaarohan

Rama ka aashirvaad milte hi,
Shabari—jute hue baal, valkal vastra,
mriga-charma (deer skin)—
aag me pravesh kar gayi.

Aur turant
woh ek divya roop me aasman me ubhar aayi—

swargiya gehno se saja hua sharir

phoolon ki mala

chandan ki sugandh

swarn jaise tej

Bijli ki chamak jaise
woh aasman ki ore badh gayi—
apne Guruon ke pavitra lok me.
        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter75
    with st.expander("Chapter 3.75 – Rama reaches the beautiful Lake Pampa"):
        text1 = """
Shabari ke swargaarohan (ascension to heaven) ke baad
Rama aur Lakshman kuch der shaant khade rahe.

Unke man me un mahaan tapasviyon (ascetics) ki pavitra shakti
aur unka prabhav ghoom raha tha.

Rama ne dheere se kaha:

“Lakshman, humne un rishiyon ka pavitra ashram dekh liya.
Yahaan hiran, sher, aur anek pakshi rehte hain.

Humne yahan saat pavitra jal-kund (seven sacred waters) me
snan aur pitri-tarpan (offerings to ancestors) bhi kiya.

Mujhe lagta hai, hamare bure karm jal gaye hain.
Mere mann me ek ajeeb shaanti hai.
Aur mujhe vishwas hai—ab humare liye koi acchi baat hone wali hai.”

Phir Rama ne door tak dekhkar kaha:

“Chalo Lakshman!
Pampa Sarovar hame bula raha hai.
Wahi aas-paas Rishyamuka parvat hai…
jahan Sugriva—Surya putra aur vanar-raja—chhupa rehta hai.

Wahi Sugriva…
jo hume Sita ka pata dila sakta hai.”

Lakshman ne turant kaha:

“Bhaiya, chaliye! Mera dil bhi wahan jaane ko bechain hai.”
        """
        create_image_text_layout("attached_assets/chapter3/3.75.jpg", text1, layout="side", image_position="left") 
        
        text2 = """
🌸 Pampa Sarovar ki Taraf Safar

Dono bhai Matanga Rishi ke van se bahar nikle
aur Pampa ki or chal pade.

Raste bhar unhe
pushpit ped, rang-birange phool,
aur chhote chhote talab dikhe
jahan saras (cranes), mor, woodpecker, aur anek pakshi
apni madhur aawaaz se jangal ko jaga rahe the.

Kuch hi der me unhe Matanga jheel ka ek pyara sa tila mila,
jiska paani meetha aur thanda tha.
Wahan kuch pal baith kar dono man hi man dhyaan karne lage.

Par acaanak…

Rama ka mann phir se Sita ki yaad se bhar gaya.
Uska hraday (heart) phir se bhaari ho gaya.

🌺 Pampa Sarovar ka Saundarya

Rama ne Pampa Sarovar ko dekha
aur use pehli nazar me hi laga
jaise koi saji hui dulhan ho.

Jheel ke chaaron taraf the—

Tilaka ped

Ashoka

Punnaga

Vakula

Kadamba

Malati aur Kunda ke jhaad

Mango ke bagichay

Hazaroon rangon ke phool

Hawa me phoolon ki sugandh thi.
Jheel me kamal (lotus) khile hue the.
Neelam jaise neele phool paani me chamak rahe the.
Hiran, pakshi, kinnar (celestial beings), yaksha aur gandharva
kabhi-kabhi yahan dikh jaate.

Rama aur Lakshman ne jheel ke kinare
khade hokar is saundarya ko dekha…

Aur phir Rama ne dard bhari awaaz me kaha:

“Lakshman…
Kab tak Sita mere bina rehti hogi?
Kaise rehti hogi?”

Dukh se bhare ye shabd keh kar
Rama ne dheere se
Pampa jheel me pravesh kiya.

Lakshman bhi unke saath utar gaya.

Shaant, sunder, sugandhit jheel ke paani me
dono bhai kuch der tak khade rahe—
aur Rama ke mann me bas ek hi baat thi:

“Sita ko kaise dhoondhoon?”
        """
        create_image_text_layout(text_content=text2, layout="full")
