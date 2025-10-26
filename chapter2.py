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
    create_image_text_layout("attached_assets/chapter2/chapter2.jpg", layout="full")
    create_image_text_layout("attached_assets/chapter2/banner2.jpg", layout="full")


    text0 = """
    <h2>Chapter 2: Ayodhya-kanda</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")


    # Chapter1
    with st.expander("Chapter 2.1 - King Dasaratha wants to make Rama the next king"):

        text1 = """
Raja Dasharatha ke chaaron putra – Rama, Lakshmana, Bharata aur Shatrughna – unke hriday (heart) ke chaar hisson jaise the. Lekin sabse zyada priya (dear) the Shri Rama, jo apne gunon (virtues) aur prem se sabka man jeet lete the.

Us samay Bharata aur Shatrughna apne nana Raja Ashvapati ke paas gaye hue the. Dono vahaan bahut prem aur aadar (respect) se rahe, lekin roz apne pita Raja Dasharatha ko yaad karte the.

Ayodhya mein, Raja Dasharatha apne sab putron se prem karte the, par Shri Rama unke aankhon ka taara the. Rama na keval unke bete the, balki Bhagwan Vishnu ka avatar (divine incarnation) the, jo dharti par aaye the Ravana jaise asur (demon) ko maarne ke liye.

        """
        create_image_text_layout("attached_assets/chapter2/2.1.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Rani Kaushalya apne putra Rama se itna prem karti thi jaise Aditi ne apne putra Indra se kiya tha. Rama bahut sundar (handsome), veer (brave) aur dayalu (kind-hearted) the.
Wo kabhi kisi ke baare mein bura nahi bolte the, hamesha mitha (sweet) bolte the, aur agar koi unse galti karta, to wo use turant maaf (forgive) kar dete the.

Rama bade vidwan (wise) aur vinamra (humble) the. Unhone apne Guru se Veda (holy knowledge) aur rajneeti (politics) dono seekhe the.
Wo Brihaspati (guru of gods) ke barabar vidya mein, aur Indra ke barabar shaurya (valor) mein the.
Prja (people) unse itna prem karti thi jaise wo unke apne pran (life) ho.

Rama sada dharm (righteousness) ka palan karte, buzurgon ka samman karte, aur gareebon ke prati daya dikhate.
Unke andar gyaan (wisdom), dharma (virtue) aur sahas (courage) teeno gun samaye hue the.

Raja Dasharatha roz Rama ke gunon ko dekh kar sochne lage –

“Main ab vriddh (old) ho gaya hoon, aur apni zindagi ka adhikansh hissa rajya karte beet gaya hai. Ab main chahta hoon ki apne jeevan mein hi Rama ko Ayodhya ka yuvaraj (crown prince) bana doon.”

Ye vichaar unke mann mein din-b-din badhta gaya. Unhone socha:

“Rama badalon ki tarah sab par daya barsata hai, sabse pyara hai, aur mujhse bhi adhik gunwaan (virtuous) hai. Agar main use rajya de doon, to mujhe sukh aur swarg dono milenge.”

Phir Raja Dasharatha ne apne mantriyon (ministers) ko bulaya aur kaha ki wo Rama ko yuvaraj ghoshit karna chahte hain.
Sabhi mantri aur praja (citizens) is baat se khush ho gaye, kyunki Rama sabke priya the.

        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Tab Raja Dasharatha ne sab rajaon aur nagarvasiyon ko Ayodhya mein bulaya. Rajmahal sajaya gaya, aur sabko uphaar (gifts) diye gaye.
Sirf Kaikeya desh (Bharata ke nana ka rajya) aur Mithila ko abhi soochit nahi kiya gaya, kyunki baad mein unhe batana tha.

Sab rajaon ke beech baithkar Raja Dasharatha aise dikh rahe the jaise Prajapati (Lord of Creation) apne devtaon ke madhya virajmaan (seated) ho.
Aur sab man mein yehi soch rahe the —

“Ab Ayodhya ka bhavishya surakshit hai, kyunki uska bhavishya Rama ke haathon mein hai.”
        """
        create_image_text_layout("attached_assets/chapter2/2.1.2.jpg", text3, layout="side", image_position="right")

    # Chapter2
    with st.expander("Chapter 2.2 - Everyone in Ayodhya happily agrees to make Rama the prince"):

        text1 = """
Raja Dasharatha ne apne sabhi mantriyon, budhijeevi (wise elders) aur rajaon ko bulaya aur apni baat itni madhur (sweet) aur prabhavshali (powerful) dhvani mein kahi ki jaise damru ki thaap ya garajne ka shor, lekin shabd pyare aur raj-tantra ke anukool (kingly) the.

Raja ne kaha:

“Mere poorvajon (ancestors) ne is samrajya ko sambhala, aur main unke charanon par chal kar isey aaj tak surakshit rakha. Ab meri umr badh gayi hai, sharir thak gaya hai aur rajya ke bojh ko uthana kathin ho gaya hai. Isliye main chahta hoon ki mera bada putra Shri Rama, jo sabhi gunon se sampann (full of virtues) hai, rajya ka yuvaraj (regent) bane.

Rama, mere priyatam putra, Indra ke saman shaurya aur sabhi dushmanon ka vinash karne mein samarth hai. Main chahta hoon ki wo rajya ka palan kare aur main chintamukt (free from worry) ho jaun. Agar aap log bhi is baat ko uchit (right) samjhein, to mujhe apna sujhav bataein.”

        """
        create_image_text_layout("attached_assets/chapter2/2.2.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Jab Raja Dasharatha ne ye kaha, to sabhi mantri, raja aur budhijeevi ek saath bole:

“Shresth! Shresth!”

Ye shabd aise ghoonj uthe jaise door se garajne ka shor, ya barish ke samay mor ka raag.

Phir sabhi brahmin, mantri aur nagar ke budhijeevi milkar manan-vichar (deliberation) ke baad Raja se bole:

“Mahan Raja, aapne hazaron varsh rajya kiya aur ab vriddh ho gaye hain. Isliye humari icchha hai ki Shri Rama ko yuvaraj banaya jaye. Hum sab chahte hain ki hum unhe rajya ki gaddi par baithte, haathi par sawar hote dekhein.”

Raja ne pucha:

“Aap log sach mein kyon chahte hain ki Rama ko yuvaraj banaya jaye? Kya maine kabhi galti ki hai ya dharma ka palan nahi kiya?”

Tab budhijeevi aur mantriyon ne jawab diya:

“Raja, aapka putra Shri Rama sabhi gunon se sampann hai. Uska dharm aur satya ke prati prem Indra ke saman hai.
Uska charitra prakashit karta hai ki dharma aur samriddhi dono ko kaise banaya jaye. Wo sabhi logon ke hit mein sochta hai, shaktishaali hone ke bawajood vinamra hai, hamesha daya aur kshama ka palan karta hai.

        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Wo hamesha apne praja ki bhalaayi karta hai, durbhiksha (misery) mein sahara deta hai, aur unki khushi mein khush hota hai. Uska vyavhaar sabke liye madhur aur upyogi hai.
Rama, Vishnu ke saman, sabke liye dayalu aur snehpoorna hai. Uski mahima itni hai ki poori dharti usko apna raja maan ti hai.

Isliye Mahan Raja, aap apni ichchha se Shri Rama ko turant yuvaraj ghoshit karein. Humari prarthana hai ki wo hamesha safal, dharmpalak aur praja ke priya rahen.”

Sabhi mantriyon aur budhijeevi ki baatein sunkar Raja Dasharatha ke hriday (heart) ko sukh aur santosh (joy) mila. Sab log is faisle se khush ho gaye, aur Shri Rama ko yuvaraj banane ki prakriya shuru karne ka samay aa gaya.
        """
        create_image_text_layout("attached_assets/chapter2/2.2.2.jpg", text3, layout="side", image_position="right")

    # Chapter3
    with st.expander("Chapter 2.3 - The king decides Rama will be crowned"):

        text1 = """
Jin logon ne apne haath jod kar prarthana ki thi, Raja Dasharatha ne vinamrata se jawab diya:

“Aaj main sach mein anandit aur saubhagyashali hoon, kyunki log chahte hain ki mera putra, Shri Rama, yuvaraj ghoshit ho.”

Raja ne apne sabhi praja ke samne Shri Vasishtha, Vamadeva aur anya rishiyon se kaha:

“Is Citra maas mein, jab van phoolon se sukhad aur sundar lagte hain, kripya sab vyavastha karein ki mera putra Shri Rama ko yuvaraj sthapit kiya ja sake.”

Jab Raja ne yah kaha, to praja ne zor se taliyan bajayi aur shor-sharaba hua. Phir Raja ne Shri Vasishtha se kaha:

        """
        create_image_text_layout("attached_assets/chapter2/2.3.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“O Dharmagya Rishi, aap hi vyavastha karen ki yuvaraj sthapana ki poori vidhi sahi se ki jaaye.”

Tab Shri Vasishtha ne mantriyon ko aadesh diya ki sab kuch prastut karein: sone, ratna, sugandhit tel, malayein, bhune hue chawal, shahad aur ghee alag-alag bartanon mein; naye vastra, rath, shastra aur pura sena; durbal na hone wale haathi; safed jhanda, shital chhatra, sona ke sau bartan, gaye sunehre singh ke saath, sher ki chamdi aur anya aavashyak vastu.

Rishi ne aage kaha:

“Rajmahal ke pravesh dwaron aur niyamit kakshon ko malai aur chandan se sajao, sugandhit dhup jalao, aur brahminon ke liye sneh aur ann ka vyavastha karo. Subah shanti mantra uchcharit kiya jaaye, aur brahminon ke liye suvidhaayein sahi tareeke se prastut ho.”

Shri Vasishtha aur Shri Vamadeva ne sab kuch poori tarah vyavasthit kiya aur raja ko suchit kiya. Tab Raja Dasharatha ne pradhan mantri Sumantra se kaha:

“Yuva shaktishaali Shri Rama ko turant yahaan le aao.”

Sumantra ne raja ke aadesh ka palan kiya aur Shri Rama ko raaj rath mein laya. Raghunandan, apni pratibha aur shaurya ke saath, sabhi rajyon ke rajaon se ghira hua tha. Raja Dasharatha usse dekh kar Indra ke saman lag rahe the, jaise devtaon ke beech Indra ho.

Shri Rama, sundar, shaktishaali, haath lamba, nishchint aur veer, haathi ki tarah prabhavshali kadam rakhte hue, chandrama ke saman prakashit ho rahe the. Sab log unke gun aur daya se mohit ho gaye.

Raja Dasharatha apne pyare putra ko dekh kar anand se bhar gaye. Shri Rama Sumantra ke saath raja ke paas aaye, apne shaktishaali charitra aur vinamrata dikhayi, aur rajmahal ke sone aur ratna se sajaye gaye singhasan par baith gaye. Raghunandan us samay Sumeru par ubharte surya jaise prakashmaan lag rahe the.

Raja Dasharatha ne Shri Rama se kaha:

“Mere putra, aap meri mukhya rani ke santan ho aur atyant priye ho. Aapke gunon se mere praja ka jeevan prakashit hua hai. Ab aap yuvaraj ke pad ko svikar karein. Apni krur bhavnaon, kaam aur krodh ko door rakhein; rajya ke ghatnayen dhyan se dekhein; apne praja ko khushi aur sukh-prasanna rakhein; apne mitron aur dushmanon ko nyay se dekhein.”

        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Raja ke is sandesh ko sun kar Raja Kaushalya ko bhi khushi hui aur unhone achhi khabar pahunchane wale rashton ko gau aur ratna diye.

Shri Rama ne vinamrata se jawab diya, “Yatharth, jaisa aap ne aadesh diya,” aur raja ko pranam karte hue raaj rath mein chhode. Log unhe dekh kar khushi se jhoom uthe.

Log raja ke faisle se santusht ho gaye aur apne ghar jaakar apne devtaon ki pooja ki, taki Shri Rama ki yuvaraj sthapana mein koi badha na aaye.
        """
        create_image_text_layout("attached_assets/chapter2/2.3.2.jpg", text3, layout="side", image_position="right")

    # Chapter4
    with st.expander("Chapter 2.4 - Rama and Sita get ready for the big ceremony"):

        text1 = """
Nagarpatiyon ke chale jaane ke baad, Raja Dasharatha ne apne mantriyon se phir salah-mashwara kiya:

“Kal Pushya nakshatra shubh sthiti mein hai, main aadesh deta hoon ki lotus-nayan Rama ko tabhi mera uttaradhikari ghoshit kiya jaaye.”

Mantriyon ko bhejne ke baad, raja ne Sumantra ko aadesh diya ki Shri Rama ko dobara unke paas laaye. Sumantra turant raja ke aadesh par Rama ke mahal gaya.

Rama ne darwaze par mantri ko dekh kar poocha,

“Kya kaam hai aapka?”

Sumantra ne jawab diya:

“Raja aapko dekhna chahte hain.”

Shri Rama turant apne raja-pita ke mahal gaye. Raja Dasharatha apne niji kaksh mein baith kar Shri Rama ka swagat kiya.

        """
        create_image_text_layout("attached_assets/chapter2/2.4.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Raja ne apne pyare putra ko gale lagaya aur aashish dete hue kaha:

“Mere putra, ab main vriddh ho gaya hoon aur rajya ka bhoj sambhalte-sambhalte thak gaya hoon. Maine anek yagnas kiye, brahminon ko daan diye, Veda ka adhyayan kiya. Ab mujhe sirf tumhari yuvaraj sthapana karni hai.

“Mere putra, mujhe raat mein kuch bhayankar sapne aaye hain, bijli ki ghoonj aur aakash se padte meteors ke saath, jo kuch vipatti ka sanket dete hain. Aaj Purnavasu nakshatra shubh tha, par kal Pushya nakshatra tumhari rajyabhishek ke liye shubh hai. Tumhari sthapana kal hogi. Ab se tum apni patni Sita ke saath vrat rakhoge, kusha ke chatai par sone aur pathar ko takiya bana kar raat guzaroge. Tumhare mitra tumhari raksha karenge. Aise karmo mein kai badhaayein aati hain.

“Bharata tumhare saath nahi hai, par main chahta hoon ki tumhare yuvaraj ghoshit ho jao. Tumhara bhai, Bharata, dharmic aur shisht hai, par manushya ka man kabhi sthir nahi hota. Kal tumhara rajyabhishek hoga, ab apne mahal laut jao.”

Raja ke aadesh ke baad Shri Rama apne mahal gaye. Apni patni Sita ko raja ke faisle se avagat karane ke liye, Rama Raja Kaushalya ke mahal gaye. Wahan Raja Kaushalya, Sita aur Lakshmana ke saath, mann se pooja aur niyam anusar vrat mein lagi hui thi.

Shri Rama ne apni mata ko pranam kiya aur khushi se kaha:

“O Mata, mere pita ne aadesh diya hai ki main praja ki seva karun aur kal rajya ka bojh uthaunga. Shri Vasishtha aur anya rishi ne aadesh diya hai ki raat ko Princess Sita ke saath vrat rakhun, aur subah dono pooja aur shubh vidhi anusar rajyabhishek karenge.”

        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Raja Kaushalya, apni khushi ke aansuon ke saath, boli:

“O priye putra Rama, tum lambi umar pao aur tumhare shatru vinash ho. Rajya paakar tum apne mitron, rishtedaron aur Queen Sumitra ko khushi do. Tum sach mein shubh nakshatra mein janme ho, kyunki tumhare gunon se tumhare pita ka hriday khush hua.”

Shri Rama, mata ke shabdon ko sun kar, Lakshmana se bole:

“O Lakshmana, rajya ki seva mere saath karo, tum meri doosri aatma ho, rajya tumhara bhi hai. Main tumhare liye jeevan aur rajya chahta hoon.”

Phir Shri Rama, dono raniyon ko pranam kar, unki anumati se Sita ke saath apne mahal chale gaye.
        """
        create_image_text_layout("attached_assets/chapter2/2.4.2.jpg", text3, layout="side", image_position="right")

    # Chapter5
    with st.expander("Chapter 2.5 - Sage Vasishtha tells Rama and Sita to keep a fast"):

        text1 = """
Raja Dasharatha ne apne putra Rama ko unke yuvaraj ghoshit hone ki khabar dekar, apne guru, Shri Vasishtha ko bulaya aur kaha:

“O Muni, jinki sampatti keval tapasya hai, Shri Rama ke paas jao aur unhe aadesh do ki ve apni patni Sita ke saath vrat rakhen, taaki unka rajyabhishek shubh ho.”

Shri Vasishtha ne kaha,

“Jaise aapne kaha, Vaise hi hoga,”

aur khud Shri Rama ke mahal ki or chale. Do ghodon se khinchi hui rath par sawar hokar, ve mahal ke teen dwar se pravesh karke Raghava ke mahal gaye, jo badal ke jaisa safed aur prakashmaan tha.

        """
        create_image_text_layout("attached_assets/chapter2/2.5.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Shri Rama ne guru ke aagman ki khabar sun kar turant unka swagat kiya. Guru ko haath pakad kar rath se utarne mein sahayata ki aur unki kruti aur swasthya ki jaankari li.

Guru Vasishtha ne kaha:

“O Rama, tumhare pita tum par kripalu hain. Kal tumhara rajyabhishek hoga. Aaj tum aur Sita vrat rakhte ho. Jaise Nahusha ne Yayati ko apna rajya diya, vaisa hi tumhare pita tumhe kal rajyabhishek denge.”

Ye shabdon ke baad, guru ne Rama aur Sita se raat ka vrat rakhne ka aadesh diya.

Shri Rama ne guru ko shraddha se pranam kiya, aur guru apni aashirwad dete hue apne aashram ko chale gaye.

Shri Rama apne mitron se khushi se baat karte hue, unke aagrah par, antaral kaksh mein chale gaye. Raghava ka mahal, khushi se bhare purush aur mahilao se ghira hua tha, jaise kamal se bhare talab mein anek pakshi aate hain.

Shri Vasishtha mahal se bahar nikal kar dekha ki Ayodhya ki sadke logon se bhari hui hain, har koi Rama ke rajyabhishek ko dekhne ke liye utsuk tha. Shehar ki sadke saaf aur paani se chhidki gayi thi, dono taraf phoolon ki malaen latki hui, har ghar mein jhande aur patake sajaye gaye. Purush, mahila, bachche aur vriddh, sab subah ka intezaar kar rahe the, taaki ve is mahan utsav ka darshan kar saken.

Shri Vasishtha ne bheed bhari sadkon se bachkar ant mein raja ke mahal pahuncha. Safed badal jaise balcony par charh kar, unhone raja ko pranam kiya jaise Brihaspati Indra ko pranam karte hain.

        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Guru ke aane ko dekh kar, raja utha aur poocha ki Shri Rama ne kya kaha. Shri Vasishtha ne jawab diya:

“Sab kuch tayyar hai.”

Raja ne apni kursi se uth kar sabko vishranti ki anumati di. Pura sabha guru ko samman dete hue khada ho gaya.

Guru ke prashansa bhare prativedan ke baad, raja ne sabha ko vishram dene ka aadesh diya aur apne niji kaksh mein chale gaye, jaise sher apne gufa mein pravesh karta hai. Wahan unka mahal Indra ke mahal ke saman aur raja khud chand ki tarah aakaash mein taira hua lag raha tha.
        """
        create_image_text_layout("attached_assets/chapter2/2.5.2.jpg", text3, layout="side", image_position="right")

    # Chapter6
    with st.expander("Chapter 2.6 - Ayodhya is decorated beautifully for the celebration"):

        text1 = """
Guru Shri Vasishtha ke chale jaane ke baad, Shri Rama aur unki patni Sita, dono ne pavitr snan karke apne man ko Bhagwan Narayana ki bhakti mein lagaya. Unhone havan (sacred fire) mein ghee chadhaya aur Narayana ko mantr ke saath pranam kiya. Jo prasadam (holy offering) bacha, uska bhag le kar, dono ne shubh soch ke saath kusha (sacred grass) par baith kar dhyan kiya.

Us raat dono ne maun (silence) rakha aur mandir ke andar hi soye, man mein pavitrta aur shanti lekar. Raat ke teen peher (three hours) baad, jab subah hone lagi, to Shri Rama aur Sita ne apne sevakon se mahal saaf karwaya aur phoolon se sajwaya.

Phir dono ne Rajvansh ke geet (dynastic songs) sune jo unhe bahut anand dene lage. Subah ke snan aur Gayatri mantra jap karne ke baad, dono ne sooraj dev (Sun God) ko pranam kiya aur brahminon (priests) se Shanti path (Peace Chant) aur anya vedic prarthnayein karne ko kaha.

        """
        create_image_text_layout("attached_assets/chapter2/2.6.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Brahminon ke shanti path ke geet aur nagaron (drums) ke sur mil kar poori Ayodhya nagri mein goonj uthe. Nagar ke logon ko jab pata chala ki Rama aur Sita vrat (fast) rakh kar Bhagwan ki puja kar rahe hain, to sabka man khushi se bhar gaya.

Subah ke samay, nagar ke logon ne bargad ke ped (banyan trees) laakar sadanon (streets and gates) ko sajaya. Bade-bade mandir (temples) jo Himalaya ki choti jaisey lagte the, unhe rang-birangi patakon (flags) se saja diya gaya.

Bazaar, rajmahal, sadkon ke kinare, aur rajdarbar ke har kona phoolon, deepakon aur jhandon se chamak raha tha. Gharon ke bahar bache khelte hue bhi ek hi baat kar rahe the —

“Aaj Shri Rama ka rajyabhishek hone wala hai!” 🌸

Sheher ke har kone mein nartak (dancers) aur sangeetkar (musicians) logon ko nach-gane se khushi de rahe the. Raste phoolon se dhake hue, dhoop (incense) ki sugandh se suganhit the, aur jagah-jagah deep (lamps) jal rahe the taaki agar raja ka shobha yatra (royal procession) raat ko guzre, to roshni bana rahe.

Log sab sabha sthal (public assemblies) aur uchcha manch (raised tribunes) par khade hokar pratiksha kar rahe the. Har jagah awaaz aa rahi thi:

“Raja Dasharatha sach mein dharm ke rakhwale hain! Unhone apni budhapa (old age) mein swayam apne putra Rama ko rajya dekar kitni dayalu bhavna dikhayi hai. Bhagwan Shri Rama sada hamare raja bane rahein!”

        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Log unki prashansa karte hue keh rahe the —

“Rama vinamra (humble) hain, vidwan (learned) hain, dharm ke path par chalne wale aur apne bhaiyon se prem karne wale hain. Raja Dasharatha amar rahein, jinki daya se hum aaj Rama ko singhasan (throne) par dekhne ja rahe hain.”

Ye khabar sun kar door-daraz ke log bhi Ayodhya ki or chal pade, taaki Rama ka rajyabhishek apni aankhon se dekh saken.

Poore Ayodhya mein jan-samudra (sea of people) umad pada. Logon ki awaaz aur utsah ka shor samudra ke garjan (roar of the ocean) jaisa lag raha tha. Ayodhya us din Amravati nagar (heavenly city) jaise chamak rahi thi — aur Shri Rama ka rajyabhishek dekhne ke liye har man khushi se bhar gaya. 🌺
        """
        create_image_text_layout("attached_assets/chapter2/2.6.2.jpg", text3, layout="side", image_position="right")

    # Chapter7
    with st.expander("Chapter 2.7 - Everyone waits for Rama’s coronation (rajyabhishek)"):

        text1 = """
Rani Kaikeyi ke paas ek dasī (maid) thi jo uske maayka (parents’ home) se uske saath aayi thi. Uska naam tha Manthara — ek kubdi (hunchback) aur chatur (clever) aurat, jo hamesha Kaikeyi ke paas rehti thi.

Ek din, rajmahal (royal palace) ki balkoni (balcony) par chadkar jab Manthara ne Ayodhya nagri dekhi, to woh hairan reh gayi. Poora sheher saj gaya tha — phoolon ki malaon (garlands) se, sadke pani se dhoyi gayi, aur ghar ke upar jhande (flags) lahr rahe the. Har taraf logon ka utsah (excitement) tha, bajon (trumpets) ki awaaz thi, aur brahmin (priests) shubh uphar (auspicious gifts) lekar khade the taaki Shri Rama ko den.

Mandir safed rang se chamak rahe the, aur nagar mein veena aur dhol (instruments) ki dhun goonj rahi thi. Hathi, ghode aur gaiyaan (elephants, horses, and cows) bhi apne-apne tarike se khushi dikhate hue nazar aa rahe the.

        """
        create_image_text_layout("attached_assets/chapter2/2.7.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Yeh sab dekhkar Manthara ko bada ashcharya hua. Tab usne Rama ki dayaa maa (nurse) ko dekha jo safed silk ke kapde pehne hue thi. Manthara ne poocha —

“Aaj yeh sab utsav (celebration) kis liye ho raha hai? Rani Kaushalya itna dhan (wealth) daan mein kyun de rahi hai? Raja Dasharatha kya karne ja rahe hain?”

Nurse khushi se bhari hui boli —

“Arre Manthara! Kya tujhe nahi pata? Kal subah Pushya nakshatra (lucky constellation) ke samay Shri Rama ka rajyabhishek (coronation) hone wala hai! Raja Dasharatha apne bade putra Rama ko Yuvaraj (crown prince) bana rahe hain!”

Yeh sunte hi Manthara ke chehre ka rang badal gaya. Uske andar jalan (jealousy) aur krodh (anger) ki aag jal uthi. Wo tezi se mahal ke neeche utar gayi aur seedha Rani Kaikeyi ke kaksh (chamber) mein pahunchi.

Usne Kaikeyi ko sote hue dekha aur zor se bola —

“Hey rani! Tum abhi tak so rahi ho? Tumhe apne upar aane wale khatre (danger) ka bilkul ehsaas nahi hai! Tumhari saari khushiyan jaldi hi dhoop mein sookhi nadi (dried-up river) jaise khatam ho jayengi!”

Kaikeyi, jo abhi-abhi jaagi thi, hairan hokar boli —

“Manthara, kya hua? Tum itni udaas kyun ho? Kuch bura hua kya?”

Tab Manthara ne dikhawa karte hue (pretending sadly) kaha —

“Hey Devi, tumhare saath bahut bada anyay (injustice) hone wala hai! Raja Dasharatha kal Shri Rama ko rajya dene wale hain. Mujhe tumhara dukh apna dukh lagta hai, isiliye main tumhe bachane aayi hoon.”

Usne jhoothi chinta dikhate hue bola —

“Raja Dasharatha tumhe dhokha de rahe hain! Bahar se sach bolne wale lagte hain, par andar se chalak aur swarthi (selfish) hain. Tumhari saaf dil (honest heart) hi tumhara dukh ban gaya hai. Tumne apne hi haathon se apni dushman (enemy) Kaushalya ke bete Rama ko god (lap) mein paala hai, jaise koi aurat galti se saanp (snake) ko apne bachche samajh kar gale laga le!”

        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Usne aur kaha —

“Raja Dasharatha Rama ko rajya dekar tumhe aur tumhare bete Bharata ko barbaad kar denge. Agar tumne abhi kuch nahi kiya, to tumhara parivar dukh ke samundar mein doob jaayega!”

Manthara ke yeh kathor (cruel) shabd sunkar Kaikeyi pehle to ghabra gayi, lekin uske chehre par hairani aur muskaan aa gayi. Usne apne gale ka ek keemti gehna (precious ornament) utar kar Manthara ko de diya aur khushi se boli —

“Arre Manthara, tum to mujhe achhi khabar (good news) de rahi ho! Mujhe Rama aur Bharata mein koi farq nahi lagta. Mujhe to bas yeh sun kar hi khushi ho rahi hai ki Rama ka rajyabhishek hone wala hai! Jo tum chaho, wo main tumhe inaam (reward) mein doongi.”

Par Manthara ke mann mein kuch aur hi tha... aur usi pal se Ayodhya ki taqdeer (fate) badalne lagi. 🌑
        """
        create_image_text_layout("attached_assets/chapter2/2.7.2.jpg", text3, layout="side", image_position="right")

    # Chapter8
    with st.expander("Chapter 2.8 - Maid Manthara tricks Queen Kaikeyi"):

        text1 = """
Manthara, jo ek kubdi (hunchback) aur chalak (clever) dasi (maid) thi, gusse se apna gehna (jewel) zameen par fekh kar boli:
“O bevakoof (foolish) Rani! Aaj tum khush ho rahi ho, par ye khushi tumhare liye dukh (sorrow) ka samundar ban jayegi. Main tumhari moorkhta (folly) par chup-chaap hasta hoon. Tum jis wajah se khush ho, us par aansu bahane chahiye.”

Kaikeyi hairan hokar boli:
“Manthara, tum itne bhaari shabd kyun keh rahi ho? Kya sach mein kuch bura hone waala hai?”

Manthara ne chalak chehra banaya aur dhire se boli:
“O Devi, tum nahi samajh rahi. Raja Dasharatha kal Pushya nakshatra (auspicious star) mein Rama ko yuvaraj (crown prince) ghoshit (proclaim) kar denge. Tab Kaushalya ki shaan badhegi aur tum aur tumhara beta Bharata nichhe ho jayenge. Tumne apne godh (lap) mein Rama ko paala — par socho, kya tumne ek saap ko apne bachche samajh kar gale laga liya ho?

        """
        create_image_text_layout("attached_assets/chapter2/2.8.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“Bharata ka bhi ussi rajya par haq (right) hai. Dharohar (tradition) ke mutabik bada beta pehle milta hai, magar agar chhota beta gunwaaan (virtuous) ho to use bhi adhikar mil sakta hai. Ab jab Rama rajya le lega, to Bharata ka kya hoga? Kya wo sadak par asahaya (helpless) nahi reh jayega?

“Lakshmana hamesha Rama ka saathi hai aur Shatrughna Bharata ka. Dono jode hamesha ek doosre ko bachayenge. Rama apne bhai Lakshmana ke liye sab karega. Par Bharata ko wo apna pratishodh (rival) maanega. Isliye mera mashwara ye hai — Bharata ko forest (van) bhej do. Usko wahan surakshit rakho aur use rajya dilao. Agar Rama ko rajya mil gaya, to tum aur tumhara parivaar sharminda (dishonoured) ho jayega. Main ye tumhare bhale ke liye keh rahi hoon.”

Queen Kaikeyi ne dheere se jawab diya:
“Manthara, mujhe Rama aur Bharata dono se pyaar hai. Rama to bada hi dharmic (righteous) aur sabka palan karne wala hai. Use yuvaraj banana theek hai. Bharata ko bhi mera prem kam nahi. Tum kyun itna darr paida kar rahi ho?”

Manthara ne zor se kahaa:
“Tum galat soch rahi ho! Jab Rama raja ban jayega to kaun uska uttaradhikari (successor) hoga — Bharata ya uska putra? Bharata hamesha bina rajya ke reh jayega. Jab kisi ghar mein ek hi gaddi (throne) hoti hai, sab betey nahin baith sakti. Agar Rama rajya pai to tumhari izzat ka kya? Kaushalya jab pradhan (chief queen) ho jayegi to tum chhoti si ban jaogi. Kya tum chahogi ki tumhara beta gareeb aur beizzat ho?

“Agar tum sach mein apne bachche ka bhala chahati ho, to Rama ko banished (vanvas — exile) karwa do aur Bharata ko rajya dewa do. Tab tumhara parivaar aur tum surakshit rahoge.”

Manthara ki baat sun kar Kaikeyi dheere-dheere dar se bhar gayi. Usne socha, “Kya sach mein Rama ke rajya se hamari izzat khatre mein aa jayegi?”

        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Manthara ne apne chal se Kaikeyi ko aage khinch kar kahaa:
“Tum socho. Main tumhare hi hit mein keh rahi hoon. Agar tum chaaho to main sab taiyar kar dungi. Bas ek baar tum haan kar do.”

Kaikeyi ab jhukti nazar aayi. Uske mann mein sankat (doubt) aur sujhav (suggestion) dono uthane lage. Manthara ne seedha seedha kaha:
“Rama ko vanvas bhejo aur Bharata ko rajya do. Jaldi faisla karo, samay tumhara dost nahin.”

Kaikeyi ki aankhon mein ab shi-shi umad aayi — manthan (inner struggle) chal raha tha. Manthara ne apna plan dhire-dhire samjhaya, aur Kaikeyi dheere-dheere maan gayi.

Us pal se Manthara ne kaam shuru kar diya — Ayodhya ke bhaavishya ko badalne wala ek chal (scheme) tayyar ho gaya.
        """
        create_image_text_layout("attached_assets/chapter2/2.8.2.jpg", text3, layout="side", image_position="right")

    # Chapter9
    with st.expander("Chapter 2.9 - Queen Kaikeyi decides to do something bad"):

        text1 = """
Kaikeyi ka chehra gusse se laal ho gaya tha. Gehri saans lete hue usne Manthara se kaha,
“Manthara, aaj main Rama ko vanvas (exile) bhej kar hi rahungi aur Bharata ko rajya ka yuvaraj (regent) banaungi. Batao, kaise ho sakta hai ye?”

Manthara, jise Rama se nafrat thi, muskurai aur boli,
“Sun rani Kaikeyi, main tujhe ek aisa raasta bataungi jisse sirf Bharata hi rajya kaadhikar (rule) paayega. Yaad hai, ek baar tune mujhe bataya tha ke Raja Dasharatha ne tujhe do vachan (boons) diye the?”

Kaikeyi ne uth kar kaha, “Haan Manthara, batao, kaise un vachan ka upyog karke Bharata ko rajya mile aur Rama ko dukh?”

        """
        create_image_text_layout("attached_assets/chapter2/2.9.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Manthara boli, “Ek samay tha jab Raja Dasharatha devtaon (gods) ke paksh mein asuron (demons) se yudh (battle) kar rahe the. Tum bhi unke saath thi. Jab raja yudh mein ghayal (wounded) ho gaye, tumne apni samajh aur sahas (courage) se unki jaan bachai. Us samay raja tumse khush ho kar bola tha — ‘Do vachan maang lo,’ aur tumne kaha tha ‘Jab zarurat hogi tab maangungi.’

Ab wahi samay aa gaya hai. Pehla vachan maango — Bharata ko rajya mile.
Aur doosra vachan maango — Rama ko 14 saal ke liye vanvas bhej diya jaye.

Itne saalon mein log Rama ko bhool jaayenge aur Bharata ka rajya mazboot ho jayega.”

Manthara ne aur chalak (clever) tareeke se samjhaya,
“Ab tum Raja ke ‘kop bhavan’ (anger chamber) mein jao. Purane kapde pehno, zameen par so jao, aur jab raja aaye to unse baat mat karo. Sirf roti raho, taaki unka dil pighal jaye. Raja tumse itna prem (love) karte hain ki tumhara aansu bhi nahi dekh sakte.

Jab wo poochein kya hua, tab unse yaad dilao un do vachanon ka. Aur tab daant kar kaho —
‘O Maharaj, Rama ko 14 saal ke liye vanvas bhejo aur Bharata ko Ayodhya ka rajya do.’”

Kaikeyi ne Manthara ki baatein dhyaan se suni aur khush ho gayi. Usne kaha,
“Manthara, tu sach mein meri sachchi dost hai. Sab viklang (deformed) logon mein tu sabse samajhdar (wise) hai.”

Kaikeyi ne Manthara ki tareef karte hue kaha,
“Jab Bharata raja banega, main teri kubad (hump) par sona chadhwaungi. Tere gale mein sona pehnauga, aur tujhe itna sajaungi ki sab raniyan tujhe dekh kar jalan mehsoos karengi.”

Manthara muskura kar boli,
“Rani, waqt haath se nikalne se pehle kaam kar lo. Jaao, abhi Raja ke kop bhavan mein jao.”

Kaikeyi ne turant uski baat maani. Manthara ke saath wo kop bhavan gayi, apne gehne (jewels) tod kar zameen par phenke, aur boli,
“Ya to Rama vanvas jaayega aur Bharata raja banega,
ya phir Raja Dasharatha ko meri maut ki khabar milegi.
Jab tak Rama raja banne ki taiyari chalti rahegi, main na gehne pehnungi, na khana khaungi.”

        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Manthara ne uske dukh ko aur badhaya aur kaha,
“Rani, agar Rama raja ban gaya, to tum aur tumhara beta dono dukh paayenge. Isliye abhi kadam uthao.”

Kaikeyi ka mann pura bhadak gaya. Usne kaha,
“Ya to Rama vanvas jaayega, ya main zinda nahi rahungi!”

Ye kehkar Kaikeyi ne apne gehne zameen par phenke aur zameen par gir gayi — jaise koi pari (fairy) apne pankh tod kar gir gayi ho.
Uska chehra gusse se lal tha, aur bina gehno ke wo aise lag rahi thi jaise raat ka aasmaan bina taare ke. 🌙
        """
        create_image_text_layout("attached_assets/chapter2/2.9.2.jpg", text3, layout="side", image_position="right")

    # Chapter10
    with st.expander("Chapter 2.10 - King Dasaratha becomes very sad"):

        text1 = """
Manthara ke kehne par, Rani Kaikeyi zameen par lott rahi thi jaise zeher bhara teer uske dil ko chhoo gaya ho. Chalak (clever) rani ab apna bura plan dhire-dhire Manthara ke saath poora bana rahi thi. Manthara ko andar se sukoon mila — uska dushit (evil) iraada ab Kaikeyi ke zariye sach hone ja raha tha.

Kaikeyi ne gusse aur jalan (jealousy) mein apne gehne tod kar zameen par phelnay shuru kar diye. Uske kapde gande ho gaye the, baal bikhar gaye the, aur wo aise lag rahi thi jaise koi apsara (celestial nymph) apne swarg (heaven) se gir gayi ho.

Udhar Raja Dasharatha, Shri Rama ke rajyabhishek (coronation) ki tayari puri kar chuke the. Ab wo khush ho kar apni raniyon ko yeh khushkhabri dene aaye. Sabse pehle wo apni sabse pyari rani Kaikeyi ke mahal gaye.

        """
        create_image_text_layout("attached_assets/chapter2/2.10.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Raja jaise chand (moon) andhere badal ke baad nikalta hai, waise hi chamak rahe the. Mahal ke bagiche (garden) mein mor, tota, hans (swans) aur saras (cranes) ghoom rahe the. Har jagah sugandhit phool, champa aur ashok ke ped khile hue the. Mahal ke andar sona-chandi ke aasans, sugandhit paani ke chhote jharne, aur mehenga bhojan sab kuch tha — jaise Ayodhya ka mahal ek swarg ban gaya ho.

Lekin jab raja Kaikeyi ke kaksh (room) mein pahunche, wo wahan nahi thi. Unhone bulaya, par jawab nahi mila. Wo chintit ho gaye. Ek dasi (maid) ne dar ke saath kaha,
“Prabhu, Rani Kaikeyi to ‘kop bhavan’ (anger chamber) mein chali gayi hain.”

Yeh sunte hi Raja Dasharatha ka dil ghabra gaya. Wo turant wahan daude. Aur jaise hi unhone Kaikeyi ko dekha — zameen par bikhri hui, gehno se mukt, kapdon mein dhool lagi hui — unka dil toote hue sheeshe jaise chhinn (broken) ho gaya.

Unhone Kaikeyi ko dekha — jaise koi tooti hui daali (broken branch), ya swarg se gira hua devduti (angel). Wo apni sabse chhoti rani se itna prem karte the ki uska dukh unse dekha nahi ja raha tha.

Wo uske paas baithe, uska haath pakad kar bole,
“Priye Kaikeyi, kya hua tumhe? Kisne tumhe dukh diya? Mujhe batao! Tum zameen par kyun leti ho, meri pyari rani? Tum to meri pran (life) se bhi badhkar ho. Agar tum beemar ho, to main turant desh ke sabse ache vaidya (physicians) bula loon. Agar kisi ne tumhe apmaanit (insult) kiya ho, to main use dand (punishment) doonga.”

Unki awaaz pyaar aur dard se bhari thi.
“Main tumhare liye kuch bhi kar sakta hoon — chahe kisi nirdosh (innocent) ko maarna ho, ya doshi ko chhodna ho. Main ek gareeb ko ameer bana sakta hoon, ya ameer ko sadak pe laa sakta hoon. Kaikeyi, bas itna batao tum chahti kya ho. Tum jaanti ho na, main tumse kitna prem karta hoon.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Raja ne haath jod kar kaha,
“Main kasam khata hoon, tum jo chaaho, main wahi karunga. Puri duniya ke raj mere adheen (under rule) hain — Dakshin (south), Sindhu, Kashi, Magadh, Koshal — sab. Bas tum batao, kya chahiye tumhe? Kis baat se tumhara dukh door ho sakta hai?”

Raja Dasharatha ke prem aur laachari (helplessness) bhare shabd sun kar bhi Kaikeyi chup rahi.
Wo thoda shaant dikh rahi thi, par andar se uska man abhi bhi zeher (poison) se bhara tha.
Aur tab, apne pati ko aur dukh dene ke liye, Kaikeyi ne kathor (harsh) shabdon mein baat karni shuru ki...
        """
        create_image_text_layout("attached_assets/chapter2/2.10.2.jpg", text3, layout="side", image_position="right")

    # Chapter11
    with st.expander("Chapter 2.11 - Kaikeyi reminds Dasaratha of two promises he made"):

        text1 = """
Kaikeyi ne Raja Dasharatha se kaha, “Main beemar nahi hoon aur kisi ne mujhe apmaan (insult) nahi diya. Mujhe ek ichchha (wish) hai jo aap poori kar sakte ho. Agar aap taiyaar ho, to mujhe apna vachan (boon/promise) do, main bataungi kya maangti hoon.”

Raja, jo Rama se bahut prem karta tha, usne kaan uthaya, Kaikeyi ka sir apne haathon mein uthaya aur muskura kar kaha, “Kaikeyi, mujhe maloom hai tum mera kitna priya ho. Main Rama ko bhi usse zyada pyar karta hoon. Main tumhari baat manunga. Tum jo maangogi, main poora karunga.”

        """
        create_image_text_layout("attached_assets/chapter2/2.11.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Manthara ki salah par, Kaikeyi ne ab apna lakshya (goal) poora karne ka faisla kar liya. Usne kathor (harsh) dhang se kaha:
“Raja, pehle yaad karo jab yuddh (battle) mein tum ghayal ho gaye the aur maine tumhari raksha ki thi? Tab aapne mujhe do vachan diye the. Aaj main wahi do vachan maangti hoon.”

Kaikeyi ne sabhi devtaon, rituon aur rishiyon (sages) ko gawah (witness) batate hue kaha:
“Pehla vachan: Rama ke rajyabhishek (coronation) ki taiyari rok do, aur mere putra Bharata ko rajyapal (regent) ghoshit (proclaim) karo.
Doosra vachan: Shri Ramacandra ko 14 saal ke liye vanvas (exile) bhej do — vanvas mein wo baal-kes (matted hair) aur boota (bark) ke kapde pehnega, jaise sanyasi (hermit) rehta hai. Tab mera beta Bharata bina badha ke raj karega.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Kaikeyi ne apni iccha drirh (firm) tareeke se rakhi. Raja Dasharatha ne suna, socha aur usne apna vachan dene ki kasam khayi. Raja ka dil dukh aur prem se bhara tha. Kaikeyi ke bolne ke baad mahal mein andhera (sadness) chhane laga.

Manthara khush thi. Kaikeyi ne apna lakshya paa liya. Ayodhya ki kismet ab badalne wali thi.
        """
        create_image_text_layout("attached_assets/chapter2/2.11.2.jpg", text3, layout="side", image_position="right")

    # Chapter12
    with st.expander("Chapter 2.12 - The king feels great pain and sorrow"):

        text1 = """
Rani Kaikeyi ke kathor (harsh) shabdon ne Raja Dasharatha ke dil ko gehra dukh pahunchaya. Raja sochne lage — “Kya main sapna dekh raha hoon? Kya main pagal ho gaya hoon? Kya kisi bure grah (inauspicious planet) ka prabhav hai? Ya main kisi rog (disease) se grast hoon?”

Thodi der baad Raja shaant hue, par unka mann fir se bechain ho gaya. Kaikeyi ke maange yaad aate hi, wo uss hiran (deer) ki tarah ghabra gaye jo sherni ke samne khada ho. Zameen par baith kar wo gehri saansein lene lage, jaise zahreela saanp kisi mantra ke jaal mein phans gaya ho. “Haye mujhe kya ho gaya!” kah kar wo behosh ho gaye.

        """
        create_image_text_layout("attached_assets/chapter2/2.12.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Thodi der baad hosh aaya, to Raja Kaikeyi par krodh (anger) se bhar gaye. Unki aankhen jaise aag ugal rahi ho.
Unhone kaha —
“Hey papi (sinful) Kaikeyi! Tumne Rama jaise pavitra (pure) putra aur mujhe kis paap (sin) ki saza di? Rama to hamesha tumhe apni maa samajhkar samman deta hai. Maine socha tha tum raja ki beti ho, par tum to zahreeli saanp nikli. Main Kaushalya, Sumitra, rajya (kingdom), sab kuch chhod sakta hoon, par Rama ko kabhi nahi. Duniya bina suraj ke reh sakti hai, fasal bina paani ke ug sakti hai, par main Rama ke bina ek pal nahi jee sakta.”

Dasharatha ne apna sir Kaikeyi ke charanon (feet) mein rakh diya aur bole —
“Daya karo, Kaikeyi. Yeh krodh (anger) chhod do. Agar tumhe Bharata ke liye mera prem (love) dekhna hai, to parakh lo, par Rama ko vanvas (exile) mat bhejo.”

Lekin Kaikeyi ke mann mein daya (mercy) nahi aayi. Usne kathin (harsh) awaaz mein kaha —
“Rajan, agar tum apne diye hue vachan (promise) tod doge, to duniya tumhe kapati (hypocrite) kahegi. Tumhare vansh (dynasty) ke Raja Shivya ne apna maans (flesh) diya tha apna vachan nibhane ke liye. Tum bhi apna vachan nibhao — chahe Rama ko vanvas dena pade.”

Raja Dasharatha ne dukh aur rosh (rage) se kaha —
“Hey Kaikeyi, tum pe kis dusht (evil) ne kabza kar liya hai? Tum pehle aisi nahi thi. Tum kaise soch sakti ho ki Rama jaise dayalu (kind), satyavaadi (truthful) aur maryada-purushottam (the most righteous man) ko jungle bhej diya jaye? Rama to sabka rakshak (protector) hai — wo kisi ko dukh nahi deta. Main budha (old) ho gaya hoon, kripya mujhe dukh se bachao.”

Kaikeyi ne chupchap dekha aur kaha —
“Rajan, agar aapne apna vachan toda, to main vish (poison) pee kar mar jaungi. Mujhe sirf ek cheez chahiye — Rama ka vanvas aur Bharata ka rajtilak (coronation).”

Yeh sunkar Raja Dasharatha fir se behosh ho gaye. Jab hosh aaya, to unhone dard bhare shabdon mein kaha —
“Kaikeyi, tum meri sabse badi galti (mistake) ho. Main tumhe apne ghar laya, aur aaj tumne mera vansh mita diya. Tumne mujhe dhokha diya jaise shikari (hunter) geet se hiran ko fasata hai. Log kahenge — ‘Raja Dasharatha ne moh (lust) ke chakkar mein apne bete ko vanvas bhej diya.’”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Unke aansu ruk nahi rahe the.
Unhone kaha —
“Rama, jo bachpan se satya (truth) aur tapasya (penance) mein laga raha, ab jungle mein phal-mool (fruits and roots) kha kar jeeyega. Jisne kabhi kathin shabd (harsh words) nahi bole, uske liye tum itna kathor (cruel) faisla kaise le sakti ho, Kaikeyi?”

Ant mein, Raja Dasharatha girte hue bole —
“Hey Kaikeyi, main tumhare charanon mein girta hoon, daya karo. Rama ko mat bhejo. Main uske bina jee nahi sakta.”

Lekin Kaikeyi ka dil pathar (stone) ban gaya tha. Aur bechara Raja Dasharatha, apni patni ke pairon ke paas, tootey hue dil ke saath, behosh ho gaya.
        """
        create_image_text_layout("attached_assets/chapter2/2.12.2.jpg", text3, layout="side", image_position="right")

    # Chapter13
    with st.expander("Chapter 2.13 - Kaikeyi ignores the king’s sadness"):

        text1 = """
Raja Dasharatha zameen par pade the, jaise Raja Yayati, jise svarg (heaven) se gira diya gaya ho. Unka sharir thak chuka tha, par Kaikeyi abhi bhi apni zidd (stubbornness) par tikki thi. Usne bina daya ke kaha —
“Hey Rajan, aap to hamesha satyavaadi (truthful) aur vachan ke pakke (faithful to promises) hone ka daawa karte ho, phir mere diye hue var (boons) kyun nahi nibha rahe?”

Raja Dasharatha, dukh aur krodh (anger) se bhar kar bole —
“Hey paapi (sinful woman)! Jab main mar jaunga aur Rama vanvas (exile) chala jaayega, tab tum apna uddeshya (purpose) poora kar lena. Swarg ke devta mujhse poochhenge — ‘Rama kaisa hai?’ Kya main keh doon ki maine use Kaikeyi ko khush karne ke liye vanvas bheja? Ye jhoot (falsehood) koi nahi maanega!

        """
        create_image_text_layout("attached_assets/chapter2/2.13.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Mainne kitne varsh tak beta paane ke liye tapasya (penance) ki thi, fir Rama jaise gunvaan (virtuous) putra ke hone ke baad, main use kaise chhod doon?”

Raja ne aansuon ke saath kaha —
“Rama, jo veer (brave), vidwan (wise), aur dayaalu (kind-hearted) hai, jiske nayan (eyes) kamal jaise hai, main use jungle kaise bhej doon? Uska rang neel kamal (blue lotus) jaisa hai, aur mann pavitra (pure). Us jaise putra ko dukh mein dekhna mujhe marne se bhi bada kasht (pain) deta hai.”

Raja fir ro kar bole —
“Hey nirdayi (cruel) Kaikeyi, tune mujhe aur mere satya (truth) dono ko mitaa diya. Agar main bina Rama ko dukh mein dekhe mar jaata, to mujhe swarg mein sukh milta. Par ab main duniya bhar mein apmaanit (dishonoured) ho jaunga.”

Raat ho gayi thi. Chand utra, sitare (stars) chamak rahe the, par Raja ko unmein koi sukh nahi mil raha tha. Wo asmaan ki taraf dekh kar bole —
“Hey raat, tum subah mat ban jaana. Main tumse binti (request) karta hoon, mujhe Kaikeyi ka chehra dobara na dekhna pade.”

Fir unhone Kaikeyi se haath jod kar kaha —
“Hey su-mukh (beautiful-faced) Kaikeyi, daya karo. Main ek dharmik (virtuous) raja hoon, sabke saamne maine Rama ko yuvaraj (prince regent) ghoshit (declared) kiya tha. Kripya, Rama ko rajya (kingdom) do. Isse tumhara naam aur samman (honour) dono badhega. Rama, Bharata, aur poori praja (people) tumhe dhanya (blessed) kahenge.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Yeh keh kar Raja Dasharatha ro padey. Unki aankhen laal ho gayi thi, unke aansu ruk nahi rahe the. Par Kaikeyi ka dil pathar (stone) jaise tha — na usne unke shabd sune, na unka dukh dekha.

Ant mein Raja behosh ho kar zameen par gir pade. Raat bhar wo karahte (groaning) rahe, bechain aur vyakul (restless and suffering).

Subah jab raj-sangeetkar (royal musicians) unhe jagane aaye, to Raja Dasharatha ne dard bhari awaaz mein kaha —
“Chup raho... aaj koi sangeet nahi.”
        """
        create_image_text_layout("attached_assets/chapter2/2.13.2.jpg", text3, layout="side", image_position="right")

    # Chapter14
    with st.expander("Chapter 2.14 - Dasaratha cries; Kaikeyi calls Rama to the palace"):

        text1 = """
Kaikeyi ne dekha ki Raja Dasharatha dukh aur kasht (suffering) se bikul bikhar gaye the — jaise machhli (fish) bina paani ke tadap rahi ho. Fir usne krodh aur thodi shanti se kaha,
“Rajan, yeh dukh kyu? Tumne mujhe do vardaan (boons) diye the — kya ab apne vaade se mukar jaoge? Satya (truth) hi dharma ka saar (essence) hai. Tum bas apna vaada nibhao, apne hit (good) ke liye. Purano mein Raja Shibi ne apna sharir (body) tak de diya tha ek baaz ke liye, taaki satya bana rahe. Raja Alarka ne apni aankhein (eyes) nikal kar andhe brahmin ko di thi. Samudra dev bhi apni seema (boundary) paar nahi karta kyunki wo satya ka paalan karta hai. Satya hi Brahman hai, aur satya se hi mann pavitra (pure) hota hai. Isliye, Raja, agar tum sach ko dharma mante ho, to mujhe mere vardaan do — Shri Rama ko vanvaas (exile) bhej do. Main teen baar kehti hoon, agar tumne yeh nahi kiya, to main tumhare saamne apni jaan de dungi.”

        """
        create_image_text_layout("attached_assets/chapter2/2.14.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Raja Dasharatha yeh sunkar jaise bandhan (trap) mein phans gaye. Unka chehra peela pad gaya, mann ghabra gaya — wo bilkul bechain (restless) the, jaise bail (bullock) juaal aur pehre ke beech phans gaya ho. Unhone dard bhari aawaaz mein kaha,
“Hey paapi (sinful) nari, jab humari shaadi hui thi, mainne agni ke saamne tera haath pakda tha. Lekin aaj main tujhe aur tere putra Bharat ko tyag (reject) karta hoon! Subah hone wali hai, guru aur mantri mujhe Shri Rama ka rajyabhishek (coronation) karne ko kahenge. Main chahta hoon yeh sab tayyari meri antim kriya (funeral rites) ke liye ho. Kaikeyi, tu iss rajyabhishek mein bhaag na le, kyunki tu hi uska virodh (oppose) kar rahi hai. Ab main logon ke samne kaise jaaun, jo Rama ke rajtilak ke liye khush hain? Unke chehre pe dukh dekh kar mera dil toot jaayega.”

Raat beet gayi, aur subah hone lagi. Kaikeyi, jo ab bhi apni zidd (stubbornness) par thi, gusse se boli,
“Rajan, yeh kya beemari jaisi baatein kar rahe ho? Shri Rama ko bulao. Mera putra Bharat rajya sambhale aur Rama ko van bhejo. Tabhi tum apna kartavya (duty) pura karoge.”

Raja Dasharatha ne bhaari mann se kaha, “Main dharma ke jaal mein phans gaya hoon. Mujhe bas apna bada beta Rama ek baar dekh lena hai.”

Subah ho chuki thi. Surya (sun) ug gaya tha aur Pushya nakshatra ka shubh samay chal raha tha. Mahaan Guru Vasishtha apne shishyon (disciples) ke saath sabh items lekar aae — Ganga ka pavitra jal (holy water), sona ke bartan (golden vessels), mithi (honey), dahi (curds), ghee (clarified butter), phool (flowers), doodh (milk), aur anek uphaar (gifts). Rajmahal ke bahar saara Ayodhya sheher saj gaya tha — galiyan jhaadi gayi thi, patake (flags) lahr rahe the, phoolon ke haar latak rahe the, aur hawa mein chandan (sandalwood) ki sugandh thi. Sab log utsahit (excited) the, Shri Rama ke rajyabhishek ka intezaar kar rahe the.

Guru Vasishtha ne rath ke saarathi (charioteer) Sumantra se kaha, “Raja ko batao ki Rama ka abhishek Pushya nakshatra mein hona chahiye.”

Sumantra turant mahal mein gaya aur bola, “Jai ho Maharaj Dasharatha ki!” Par jaise hi usne Raja ko dekha — wo to toot chuke the, aankhein laal thi aur sharir kamzor. Raja ne kaha,
“Hey Sumantra, teri prashansa (praise) mere dil ko chhed rahi hai.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Sumantra hairan ho gaya, samajh nahi paaya ki Raja itne dukhi kyun hain. Tab Kaikeyi ne jhoot bol kar kaha,
“Raja poori raat khushi ke maare so nahi paaye, ab neend le rahe hain. Jaao, Shri Rama ko bula lao. Unhe yahan bulana zaruri hai.”

Sumantra ne socha — “Raja ne shayad ab Shri Rama ko rajyabhishek ke liye bulaya hoga.”
Khushi se wo Rama ke mahal ki taraf gaya — jo samundar ke beech ek sundar dweep (island) jaisa lag raha tha. Mahal ke bahar rajkumar, senapati (chiefs), aur anek log khade the, sab apni-apni jagah par, utsav ki apeksha (expectation) mein.
        """
        create_image_text_layout("attached_assets/chapter2/2.14.2.jpg", text3, layout="side", image_position="right")

    # Chapter15
    with st.expander("Chapter 2.15 - Minister Sumantra rushes to Rama’s home"):

        text1 = """
Subah hone par, brahmin aur raja ke purohit (priests) jo Vedo (ancient scriptures) mein nipun the, mahal ke dwar (gate) par ikattha hue. Unke saath senapati (chiefs), mantri (counsellors), aur vyapari (merchants) bhi aaye — sab Shri Rama ke rajyabhishek (coronation) ko dekhne ke liye utsuk (eager) the.

Surya dev ug chuke the, Pushya nakshatra ka shubh samay chal raha tha — wahi samay jab Shri Rama ka janm hua tha. Brahmin log sona ke bartan (gold vessels) mein Ganga–Yamuna ke sangam ka jal (holy water) lekar aaye. Unhone pavitra nadion, sarovaron aur samudron (seas) ka paani ikattha kiya, jismein kamal ke phool (lotus blooms) tair rahe the. Gular aur bargad (banyan) ke patton se usme pavitrata ka sparsh (touch of purity) diya gaya.

        """
        create_image_text_layout("attached_assets/chapter2/2.15.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Madh (honey), dahi (curds), ghee (clarified butter), kush grass, aur phool (flowers) sab taiyaar the. Gaane wali sundar mahilayen (singing women) bhi saj-sawarkar maujood thi. Sunehre hathiyon ke baalon se bane chamaron (royal fans), chand jaise chhatra (canopy), safed ghoda, ek jawan hathi, aur aath kanyaen (virgins) bhi samaan ke roop mein laye gaye.

Vina (musical instrument) bajate kalakar, veer gathayein (heroic songs) sunate bards — sab kuch Ikshvaku vansh ke ek raja ke abhishek ke layak (worthy) tha. Parantu, jab sab kuch taiyaar ho gaya, tab sabne dekha — Raja Dasharatha to aaye hi nahi! Log bole, “Surya ug gaya hai, sab kuch tayyar hai, par raja ab tak nahi nikle. Kaun unhe bulayega?”

Tab anubhav se bhare hue Sumantra ne aage badhkar kaha,
“Raja ke aadesh (order) se main Shri Rama ko bulane ja raha hoon. Main lautkar aap sabko bataunga ki vilamb (delay) ka kaaran kya hai.”

Sumantra, bina kisi ghoshna (announcement) ke, mahal ke andar gaya. Usne Raghu vansh (dynasty) ki prashansa (praise) karte hue raja ke kaksh (chamber) tak pahunch gaya, jahan Dasharatha zameen par pade the. Usne parda hatakar kaha,
“Hey Maharaj, Surya, Kuvera, Varuna, Agni, aur Indra aapko vijay (victory) dein. Raat ja chuki hai, prabhat (dawn) ho gayi hai, uth jaiye, hey simhon ke raja! Brahmin, senapati aur mantri sab aapke darshan ke liye aaye hain.”

Raja ne aankhein kholkar dheere se kaha,
“Sumantra, turant Shri Rama ko bulao. Der mat karo. Main so nahi raha, jaldi jao aur use lekar aao.”

Sumantra ne pranam karke turant aadesh maan liya. Uske mann mein khushi thi — use laga Raja Dasharatha ab Rama ke rajyabhishek ke liye tayyar hain.

Wo khushi-khushi rath (chariot) par chad kar nikal gaya. Sadkein patakon (flags) aur haaron (garlands) se sajaayi gayi thi. Har taraf log Shri Rama ke naam ki baatein kar rahe the — “Aaj humare Rama ka rajtilak (coronation) hoga!”

Jab Sumantra thoda aage badha, usne Rama ka mahal dekha — safed aur chamakdaar jaise Kailash parvat ka shikhar (peak), Indra ke swarg (heaven) jaisa sundar. Mahal ke minar (turrets) sunehre pratimon (golden idols) se sajae gaye the, aur deewar par motiyon aur mani (jewels) ke haar latak rahe the. Sandal aur ambar (ambergris) ki sugandh (fragrance) hawa mein thi.

Andar ke kamre sher (lion), bagh (tiger), aur bhediye (wolf) ke rangin chitr (paintings) se sajae gaye the. Mahal ke bahar hiran (deer) aur mor (peacock) khel rahe the, jaise prakriti (nature) bhi Rama ki khushi mana rahi ho.

Door-daraz deshon ke log apne haath mein uphaar (gifts) lekar aaye the, Shri Rama ke darshan ke liye. Mahal ke andar chhoti-kad ke sevak (attendants) nishthaa (dedication) se seva kar rahe the.

Sumantra apne rath se utar kar andar gaya. Usne Rama ke mitron aur sevakon ko pranam kiya, sabse pyaar se baat ki, aur Rama ke gunon (qualities) ki baatein sun kar khush hua. Mahal ke andar usne bada sundar dwaar (door) dekha — jaise Meru parvat ka shikhar, jahan se prakash (light) chamak raha tha.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Wahan usne ek bada hathi dekha — pahaad jaisa uncha, kale badal (dark cloud) jaisa rang, jiska naam tha Shatrunja. Us hathi ne kabhi ankus (goad) ka dard nahi jhela tha, aur wo Rama ko le jaane ke liye taiyaar tha.

Aage badhte hue Sumantra ne ghodon ke sainik (horsemen), kalakar (artists), aur kavi (poets) dekhe — sab Rama ke rajyabhishek ke liye utsuk the.

Ant mein wo Rama ke nij (private) kaksh mein bina rok-tok (unchallenged) pahunch gaya — jaise ek magar (crocodile) motiyon se bhare samundar mein ghus jaata hai.
        """
        create_image_text_layout("attached_assets/chapter2/2.15.2.jpg", text3, layout="side", image_position="right")

    # Chapter16
    with st.expander("Chapter 2.16 - Rama quickly rides his chariot to see the king"):

        text1 = """
Sumantra aage badhe aur ek aur darwaze tak pahunche, jahan logon ka jamghat tha. Wahan unhone dekha kai yuva sainik — sajag (alert), wafadar, aur apne swami ke prati samarpit — dhanush aur talwaron ke saath khade the. Thoda aage, kuch buzurg sevak laal vastra (cloth) pehne hue, hath mein stambh (staff) liye, raniyon ke kaksh (apartments) ki raksha kar rahe the.

Jab unhone Sumantra ko aata dekha, sab ne samman se pranam kiya. Sumantra ne vinamrta se kaha, “Kripya Shri Ram ko batayein ki Sumantra dwar (door) par prateeksha kar rahe hain.”

        """
        create_image_text_layout("attached_assets/chapter2/2.16.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Woh sevak, jo hamesha Shri Rama ke bhale ke liye prarthana karte the, turant Raja Kumar Rama aur Devi Sita ko unke aagman ki soochna di. Rama ne Sumantra ko apne pita Maharaj Dasharatha ke vishwaspatra samajh kar, turant unhe bulwa liya.

Jab Sumantra andar aaye, unhone dekha — Shri Rama sona se bane singhasan (throne) par baithe hain, jaise dhan ka devta Kuvera khud virajman ho. Unka matha sugandhit chandan paste se lepta hua tha, jo lal rang mein chamak raha tha. Unke paas Devi Sita baithi thi — chaand ki tarah komal aur sundar, haath mein chamara (royal fan) liye.

Sumantra ne namrata se pranam kiya. Haath jodkar kaha, “Hey Kaushalya ke putra, Maharaj Dasharatha aapko Rani Kaikeyi ke kaksh mein bulwa rahe hain. Kripya turant padhariye.”

Shri Rama muskuraye aur bole, “Aisa hi ho. Main abhi chalta hoon.” Phir Sita ki or mudkar bole, “Devi, Ma Kaikeyi aur Pitaji ne milkar mere rajyabhishek (coronation) ke baare mein vichar kiya hai. Ma Kaikeyi hamesha mere kalyan ke liye hi sochti hain. Unhone Pitaji ke saath milkar mujhe bulwaya hai. Mujhe poora vishwas hai, aaj hi mujhe yuvaraj (prince regent) banaya jayega. Tum apni saheliyon ke saath khushi se samay bitao.”

Sita, jinke nayan kamal jaise sundar the, pyaar bhari nazar se Rama ko dekhti rahi. Jaate waqt unhone shubh mantra (peace chant) bola aur kaha, “Hey Maharaj, brahmin aapka abhishek usi tarah karenge jaise Brahma ne Indra ka kiya tha. Indra, Yama, Varuna aur Kuvera — chaaro dishaon ke devta — aapki raksha karein.”

Rama ne Sita se vida li aur Sumantra ke saath mahal se bahar nikle. Jaise sher (lion) apni gufa se nikalta hai, waise hi Rama pragat hue. Bahar unke chhote bhai Lakshmana vinamrta se prateeksha kar rahe the.

Madhya dwar (middle gate) par Rama ne apne mitron aur praja ko dekha — sab khushi se unka swagat kar rahe the. Phir Rama apne rath par chadhe, jo sona, moti aur maniyon (gems) se saja tha, jisme tiger skin bicha hua tha. Jab rath chala, uski garjana (roar) bijli ki tarah goonj uthi.

Rath ke ghode bijli ki tarah tez daud rahe the, jaise Indra ke apne ashva (horses). Lakshmana piche khade the, haath mein chamara liye.

Sab or se “Jai! Jai!” ke naare gunj rahe the. Log unka rath dekh kar pushpo ki varsha (flower shower) kar rahe the. Sainik talwaron ke saath aage chal rahe the, peeche geetkar aur vadak (musicians) prashansa ke geet gaa rahe the. Aur mahalon ki jhalkiyon (balconies) se sundar mahilayein phool barsa rahi thi, prarthana kar rahi thi — “Hey Rama, tum apni ma Kaushalya ka gaurav ho. Aaj tumhare rajyabhishek se Ayodhya mein khushi chha gayi hai.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Kuch auratein keh rahi thi, “Devi Sita sabse adbhut (blessed) stree hain, kyunki unhe Shri Rama jaise pativrata pati mile hain — jaise Rohini ne Chandrama se milan paaya tha.”

Rama in sab prashanson ko shant muskaan ke saath sun rahe the, aur Ayodhya ki saj-sajakar sadkon se rajmahal ki or badhte gaye — unka rath surya ki tarah chamak raha tha, aur log unka naam le kar prem se pukar rahe the.
        """
        create_image_text_layout("attached_assets/chapter2/2.16.2.jpg", text3, layout="side", image_position="right")

    # Chapter17
    with st.expander("Chapter 2.17 - People cheer as Rama enters the palace"):

        text1 = """
Shri Rama apni rath (chariot) mein baithe hue Ayodhya nagar aur apne khush mitron ko dekh rahe the. Poora sheher safed badal (white cloud) ki tarah chamak raha tha, jahan har jagah patake aur jhandiyan (flags and banners) hawa mein lehra rahi thi. Hawaa sugandhit thi, kyunki har gali mein dhoop (incense) aur chandan (sandalwood) ki khushboo faili hui thi.

Raaste ke dono taraf sundar dukanein thi, jahan reare perfumes, kapde, moti (pearls), aur chamakdaar ratne (gems) sajaye gaye the. Food aur drink ke stalls bhi lage the, jaise kisi devlok (heaven) ka bazaar ho.

        """
        create_image_text_layout("attached_assets/chapter2/2.17.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Rajpath (royal road) itna sundar sajaya gaya tha jaise devtaon ka raasta ho — curd (dahi), chawal (rice), chandan, bhune hue dane (parched grain), aur doodh se shubh nishaan banaye gaye the. Phool aur sugandhit vastuon se saje chowk (cross-roads) se guzarte hue, Shri Rama sabka namaskar aur aashirwad vinamrta (humility) se sweekar kar rahe the.

Buzurg log prarthana kar rahe the —
“O Rajkumar! Aaj tumhara rajyabhishek (coronation) hai. Tumhara raj aise ho jaise tumhare dada aur pardada ka tha. Tab hum sab khush the, aur phir se waise hi sukh paayen. Humein duniya ya swarg ke sukh ki chinta nahi — bas Shri Ramachandra ka rajyabhishek dekh kar hi humara jeevan safal ho jayega!”

Shri Rama sabke beech shaant (calm) aur prasann (serene) roop se aage badh rahe the. Sabki nazar un par thi, jaise suraj par hoti hai. Jin logon ko unka darshan nahi mila, unhe khud par hi sharm (reproach) aa gayi.

Dayaal (compassionate) Shri Rama sab varnon (castes) ke logon par ek saman drishti (equal view) se nazar daalte the. Har koi unse apni shraddha ke hisaab se prem karta tha.

Mandiron, pavitra vanon (sacred groves) aur mandap (pavilions) ke paas se guzarte hue, Shri Rama ne sabko pranam kiya aur unka parikrama (circumambulation) kiya.

Aakhir unhone rajmahal (royal palace) dekha — jo safed badal jaise lag raha tha. Uske minar (towers) Mount Kailash ki barfili choti (snow-capped peaks) jaise chamak rahe the, aur uske balcony (balcony) aasmaan tak pahunchti dikh rahi thi. Ratan (precious gems) se saja hua pura mahal Indra ke swarg se bhi adhik sundar lag raha tha.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Pitaji Dasharatha ke mahal ke paas pahunchkar, Shri Rama ne teen dwar (gateways) paar kiye — jin par dhanushdhari (archers) prahari khade the. Chauthe aur paanchve parisar (enclosure) tak wo paidal gaye.

Vahan apne sevakon ko chhodkar, Shri Rama raja ke antahpura (private chamber) mein pravesh (entered) hue.

Bahut saare nagrik (citizens) unhe dekh kar anand (joy) se bhar gaye, aur unka wapas aana usi tarah prateekshit (awaited) kar rahe the jaise samundar (sea) poornima ke chand (full moon) ka intezaar karta hai.
        """
        create_image_text_layout("attached_assets/chapter2/2.17.2.jpg", text3, layout="side", image_position="right")

    # Chapter18
    with st.expander("Chapter 2.18 - Rama sees his father upset and speechless"):

        text1 = """
Shri Rama jab raja ke antahpura (private chamber) mein gaye, toh unhone dekha — Raja Dasharatha bistar par baithe hain, unka chehra udaas aur peela pad gaya hai. Unke paas Maa Kaikeyi baithi thi.

Rama ne pehle apne pita ke charanon mein matha teka (bowed down), phir Maa Kaikeyi ko pranam kiya.

Raja Dasharatha ki aankhen aansuon (tears) se bhari hui thi, gala ruka hua tha — unke muh se sirf ek shabd nikla: “Rama…”

Rama ke dil mein ek ajeeb sa dar (fear) uth gaya — jaise kisi aadmi ka dil kaamp jaaye jab wo galti se saanp (serpent) ko chhu le.

        """
        create_image_text_layout("attached_assets/chapter2/2.18.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Raja Dasharatha dukh aur pachtave (remorse) se hil gaye the, gehri saansein le rahe the. Wo samundar jaise lag rahe the — jo shaant (calm) toh hota hai, par tufaan (storm) aate hi bechain ho jaata hai.

Rama sochne lage:
“Pitaji mujhe dekh kar khush kyu nahi hue? Pehle jab naraz hote the, mujhe dekh kar shaant ho jaate the. Par aaj to wo aur zyada dukhi lag rahe hain. Aisa kya ho gaya hai?”

Wo Maa Kaikeyi ki taraf mud kar bole:
“Hey Mata! Agar mujhse anjane mein koi galti ho gayi ho jisse pitaji dukhi hain, toh aap unhe shaant kar dijiye. Mujhe batayiye, kya unhe sharirik ya manasik (mental) dukh hai? Kya Bhai Bharat, Shatrughna, ya Maaon (mothers) se koi galti hui hai? Main ek pal bhi nahi jeena chahta agar Pitaji mujhse naraaz hain. Mata-pita to hamare jeevit devta (living gods) hote hain, unka aadesh hi dharm hai.”

Rama ne vinamrta (humility) se pucha,
“Maa, sach batayiye, ye dukh ka karan kya hai?”

Tab Kaikeyi — jisme ab sharam (shame) naam ki koi baat nahi rahi thi — apne swarth (selfishness) ko chhupate hue, ghamand (arrogant) se boli:
“Rama, Raja tumse naraaz nahi hain, na hi unhe koi rog (illness) hai. Unke mann mein ek baat hai jo wo tumse keh nahi pa rahe, kyunki wo tumse bahut prem karte hain. Unhone mujhe do var (boons) diye the, aur ab wo apne vachan (promise) par pachhta rahe hain.

Rama, sachchai (truth) dharma ki jad (root) hoti hai. Raja apne vachan se peeche nahi hat sakte. Agar tum sach mein unke aadesh ka paalan karne ko tayyar ho, toh main sab batati hoon.”

Rama ne turant kaha:
“Hey Mata! Aise shabd kehkar mujhe sharminda mat kijiye. Main pita ke aadesh par kuch bhi kar sakta hoon — chahe aag (fire) mein kudna ho, ya vish (poison) peena ho, ya samundar mein doobna ho. Aap bas batayein, Pitaji kya chahte hain. Main apna vachan deta hoon — Rama kabhi jhooth nahi bolta.”

Tab Kaikeyi ne kathor (cruel) shabd mein sach bataya:
“Rama, bahut pehle Raja Dasharatha ne asuron (demons) se yudh (war) kiya tha. Jab wo ghaayal (wounded) hue, tab maine unki raksha ki. Us waqt unhone mujhe do var dene ka vachan diya tha.

Ab main un varon ka daan maangti hoon —
Pehla: Bharat ka rajyabhishek (coronation) ho.
Doosra: Tum dandaka van (Dandaka forest) mein 14 saal ke liye vanvaas (exile) jao.

Rajya, dhan, haathi, ghode — sab Bharat ke honge. Tum rajyabhishek ke kapde utaar kar, matted hair (jata) aur mriga-chhal (deer skin) pehen kar jungle mein raho.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Raja isi baat se dukh mein hain, isiliye wo tumse aankh nahi mila pa rahe. Ab jao, unka aadesh maano, aur unki pratigya (oath) ko sach karo.”

Kaikeyi ke ye kathin shabd sunkar bhi Shri Rama ke chehre par shanti bani rahi. Par Raja Dasharatha ka dil to toot gaya — unhone apne bete ke dukh ka bhavishya (future suffering) dekh liya tha.
        """
        create_image_text_layout("attached_assets/chapter2/2.18.2.jpg", text3, layout="side", image_position="right")

    # Chapter19
    with st.expander("Chapter 2.19 - Rama stays calm and decides to go to the forest"):

        text1 = """
Jab Kaikeyi ne apne kathin (harsh) shabd kahe, toh Shri Rama — shatrujit (slayer of enemies) aur dharma ke rakshak (protector of righteousness) — un baaton ko sahan (endure) kar gaye, jaise veer aadmi dard ko seh leta hai.

Unhone shaant swar mein kaha:
“Aisa hi ho! Raja ne jo vachan (promise) diya hai, uska samman (honour) rakhne ke liye main turant van (forest) jaunga — jata (matted hair) aur valkala (bark clothes) pehen kar. Par main yeh samajhna chahta hoon ki Maharaj mujhse khud baat kyu nahi kar rahe? Hey Mata, nishchint rahiye — main apne pita ka aadesh (command) bina deri ke poora karunga. Aap khush ho jaiye.”

        """
        create_image_text_layout("attached_assets/chapter2/2.19.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Phir Rama ne vinamrta (humility) se kaha:
“Mujhe dukh sirf ek baat ka hai — Raja swayam mujhe kyu nahi keh rahe ki Bharat ka rajyabhishek (coronation) ho raha hai? Main apne bhai Bharat ko apna rajya hi nahi, balki apni Sita, apni dhan-daulat (wealth), aur apni jaan (life) tak de sakta hoon. Agar isse Pitaji ka vachan sach hota hai, toh main khushi khushi van jaunga. Kripya unhe samjha dijiye, Maa.”

Rama ne fir kaha:
“Turant sandeshvaahak (messengers) bhejiye, jo ghode par baith kar Bharat ko chacha ke ghar se bula lein. Tab tak main bina kisi virodh (resistance) ke 14 saal ke vanvaas (exile) ke liye Dandaka van chala jaunga.”

Kaikeyi Rama ke in shabd se khush ho gayi. Usne kaha:
“Thik hai Rama! Turant chalte bano. Bharat ko bula liya jayega. Raja sharm (shame) ke maare tumse keh nahi pa rahe, par tum deri mat karo. Jab tak tum van nahi jaate, Raja na snan (bath) karenge, na bhojan (food) grahan karenge.”

Ye sunkar Raja Dasharatha dukh se cheekh uthe — “Haaye! Haaye!” — aur be-hosh (unconscious) hokar sone ke singhasan (golden couch) par gir gaye.

Rama ne pitaji ko sambhala (lifted up) aur Kaikeyi ke kathor (cruel) shabdon ke baad bhi shaant man se bola:
“Maa, mujhe rajya paane ki ichha kabhi nahi thi. Main sirf dharma ke palan (preservation) ke liye rajyabhishek swikaar kar raha tha. Pitaji ki seva (service) karna hi mera sabse bada dharm hai — yadi apni jaan dekar bhi main unka hit (wellbeing) kar sakta hoon, toh yeh mere liye sabse bada punya (virtue) hai. Aap mujhe maa ke roop mein jaanti hain, par shayad mera swabhav (nature) nahi samjhi. Agar jaanti hoti, toh aapko Raja se salah (consultation) karne ki zarurat hi nahi padti.”

Phir Rama bole:
“Ab main Maa Kaushalya ke paas jaunga, unhe bataunga ki main van ja raha hoon. Aur Sita ko bhi sambhalna hoga. Bharat rajya sambhale — wo dharma ke anusaar (according to righteousness) raj kare, aur hamare Pitaji ki seva kare. Yahi ek sachha putra (true son) ka kartavya (duty) hai.”

Ye shabd sunkar Raja Dasharatha fir aansuon se bhar gaye, kuch bol na paaye. Rama ne pitaji ke charanon mein pranam kiya, phir Maa Kaikeyi ke bhi charan chhuye. Unke charon or parikrama (circumambulation) karke, wo bahar aaye.

Darwaze par unke mitra (friends) khade the — sabhi ke chehre udaas the. Lakshmana, jinke aankhon mein aansu aur hriday mein krodh (anger) tha, turant Rama ke peeche chal diye.

Rama ne rajyabhishek ke liye rakhe sab pavitra vastuon (holy items) — jaise doodh, dahi, phool, aur vastra — ke paas jaakar pranam kiya aur kaha:
“Ab yeh sab Bharat ke abhishek ke liye upyog (use) kiye jaayein.”

Aur bina peeche dekhe, Rama dheere-dheere wahan se nikal gaye.

Unke chehre par ek bhi chhaya (trace) dukh ki nahi thi. Unki prakashmaan (radiant) soorat ussi tarah thi jaise poornima (full moon) apni roshni kam nahi karti.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Rama ne rajsi chhata (royal canopy) aur chamara (royal fan) tyag (abandon) kar diye, aur sabko prem aur samman (respect) se alvida kaha. Fir apne mann ko sthir (steady) karke Maa Kaushalya ke mahal ki or chale gaye, jahan unhe apni maa aur Sita ko yeh dukhbhari khabar deni thi.

Lakshmana, jo hamesha bhai ke sukh-dukh ke saathi (companion) rahe, unke peeche-peeche chale.

Aur is tarah, Rama apne dil mein shanti aur chehre par prakash (calm glow) liye, vanvaas ki or badh gaye — ek satya, ek maryada aur ek dharma ke pratik (symbol) ke roop mein.
        """
        create_image_text_layout("attached_assets/chapter2/2.19.2.jpg", text3, layout="side", image_position="right")

    # Chapter20
    with st.expander("Chapter 2.20 - Queen Kaushalya is heartbroken"):

        text1 = """
Jab Shri Ram (the noble prince) apne pitaji ke kaksh (chamber) se haath jodkar bahar nikle, toh mahal ki sab mahilaayein zor zor se rote hue boli —
“Hey Ram! Kya sach mein aaj tum vanvaas (forest exile) ja rahe ho? Tumne kabhi humse kuch maanga nahi, humare sab sapne poore kiye bina baat maane. Tum sabka sahara ho, sabka pyaara ho — kya aaj tumhe humse door bheja jayega?”

Unhone yaad kiya kaise Ram kabhi kisi se krodh (anger) nahi karte the, hamesha sabko pyaar aur samman dete the. Rani Kaushalya ke saath unka vyavahar (behavior) hamesha maa-bete jaisa hi tha. Sab dukh se ro padi jaise gaiyan apne bachchon ko kho baithi ho.

        """
        create_image_text_layout("attached_assets/chapter2/2.20.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Raja Dasharatha ne jab unki rote hue awaaz suni, toh sharm aur dukh se gir pade — unka dil Ram ke liye tootta ja raha tha.

Shri Ram, apne mann mein bhaari dukh lekar, apne bhai Lakshman ke saath maa Kaushalya ke kaksh mein gaye. Har dwar (gate) par log unhe “Jai Ram!” kehkar pranam kar rahe the. Brahman, striyan (women), aur bachche unhe aashirvad (blessing) de rahe the.

Tab Rani Kaushalya Bhagwan Vishnu ki pooja mein vyast (engaged) thi. Unhone poori raat jag kar Ram ki bhalaai ke liye yagya (sacrifice) kiya tha. Safed kapdon mein, kamzor sharir (weak body) lekin vishwas bhare dil ke saath woh havan kar rahi thi.

Jab unhone Ram ko dekha, toh maa ka dil bhar aaya — woh apne bete ki taraf daudi, jaise ek ghodi apne bachche ko dekh kar daudti hai. Usne Ram ko gale lagaya, aansuon se bhari aankhon se boli:
“Hey beta, tum sada dharmic (righteous) raho, lambi umar pao, aur apne vansh (lineage) ko gaurav do. Aaj tumhare pitaji tumhe rajya-abhishek (coronation) dene wale hain, jao unke paas jao.”

Phir unhone Ram ko khaane ke liye meetha diya, par Ram ne usse haath jodkar mana kar diya. Bahut vinamr (humble) hokar bole:
“Hey Maa, ab tak aapko pata nahi ki hum par kitni badi vipatti (calamity) aa gayi hai. Mujhe van (forest) jana padega — dandaka van mein 14 saal tak rehna hoga. Sita aur Lakshman mere saath honge. Main patton aur phalon par jeevan bitaunga. Pita ji ne mujhe vanvaas diya hai aur Bharata ko rajya.”

Yeh sunkar Kaushalya maa jaise bijli se dagi gayi — woh behosh hokar zameen par gir gayi, jaise ped ka toda hua daali (branch) dharti par girti hai. Ram ne turant maa ko utha kar palang par bithaya aur apne haathon se unka chehra saaf kiya.

Aansuon se bhari maa boli:
“Hey Ram, agar mujhe tum jaise putra (son) ka sukh nahi milta, toh shayad main itna dukh na bhogti. Be-santaan (childless) rehna is dukh se behtar hota. Mujhe lagta tha tumhare hone se mujhe garv (pride) milega, par ab main sabse neeche ho gayi hoon. Kaikeyi mujhe apni dasi (servant) samjhegi, aur sab log mera mazak banayenge.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Unhone dard bhare shabdon mein kaha:
“17 saal beet gaye jab tumne upanayan sanskar (holy thread ceremony) liya tha. Tabse main tumhare rajya-abhishek ka intezaar kar rahi thi. Main ne kitne vrat (fasts) aur poojaen ki, lekin sab bekaar gayi. Lagta hai mera hriday (heart) pathar ka bana hai, jo ab tak toota nahi. Kyon mrityu (death) mujhe lene nahi aati? Agar main mar jaaun toh yeh dukh khatam ho jaaye. Main tumhare bina jee nahi paungi. Main tumhare peeche van jaungi, jaise gai apne bachche ke peeche jaati hai.”

Aise dukh aur prem se bhari Rani Kaushalya roti rahi — ek maa ke dard se, apne Ram ke vanvaas ke soch se, aur apne toot chuke sapnon ke saath.
        """
        create_image_text_layout("attached_assets/chapter2/2.20.2.jpg", text3, layout="side", image_position="right")

