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


    # chapter3
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

        """
        create_image_text_layout("attached_assets/chapter3/3.6.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter7
    with st.expander("Chapter 3.7 – Rama meets Sage Sutikshna"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.7.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter8
    with st.expander("Chapter 3.8 – Rama says goodbye to Sutikshna"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.8.jpg", text1, layout="side", image_position="left") 
        
        text2 = """

        """
        create_image_text_layout(text_content=text2, layout="full")

    # Chapter9
    with st.expander("Chapter 3.9 – Sita asks Rama not to fight the demons"):
        text1 = """

        """
        create_image_text_layout("attached_assets/chapter3/3.9.jpg", text1, layout="side", image_position="left") 
        
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
