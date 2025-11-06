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

    # Chapter21
    with st.expander("Chapter 2.21 - Rama prepares to leave Ayodhya"):

        text1 = """
Lakshman apne dil mein dukh aur gussa lekar Maa Kaushalya se bole —
“Hey Mata, kya aapko yeh theek lagta hai ki Raja Dasharatha, jo ab Kaikeyi ke vaash mein (under her control) ho gaye hain, Ram bhaiya ko vanvaas (forest exile) bhej rahe hain? Raja ab budhape (old age) mein apne hosh kho baithe hain, unki soch dhundli ho gayi hai. Ram bhaiya ne kabhi kisi ko dukh nahi diya, sabka bhala kiya — fir bhi unhe van bhejna kaisa nyay (justice) hai? Kaun sa gunah unhone kiya hai?”

Phir Lakshman ne Ram se kaha —
“Hey Bhaiya, jab tak logon ko yeh khabar nahi mili, aap rajya sambhal lijiye (take the throne). Main aapke saath hoon, talwar aur dhanush lekar. Jo bhi aapke raste mein aayega, main use rokh dunga. Agar Raja Dasharatha bhi Kaikeyi ke kehne par dushman ban gaye, toh main unse bhi lad jaunga! Koi bhi Bharata ko rajya dene ki himmat nahi karega jab main aapke saath hoon.”

        """
        create_image_text_layout("attached_assets/chapter2/2.21.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Lakshman ke in kathin (harsh) shabdon se Maa Kaushalya aur zyada dukhi ho gayi. Unhone Ram se kaha —
“Hey Beta, tu apni maa ko itna dukh dekar kaise ja sakta hai? Agar tu sach mein dharm (righteousness) mein vishwas karta hai, toh yahin ruk jaa. Maa ki seva se bada dharm koi nahi hota. Main tujhse agrah karti hoon — van mat ja, mere saath yahin reh. Agar tu chala gaya, toh main bhojan tyag kar dungi (stop eating) aur apni jaan de dungi. Uske baad tera paap (sin) hoga.”

Rama ne maa ke aansuon bhare chehre ki taraf dekha aur bahut shaant (calmly) hokar bola —
“Hey Maa, main pita ke aadesh (command) ko nahi taal sakta. Dharma ke anusar pita ka vachan (word) sabse bada hota hai. Jaise Kandu Rishi ne apne pita ke kehne par paap hone ke bawajood ek gau (cow) ko maara, aur unhe uska dosh nahi laga. Parasurama ne bhi apne pita ke aadesh se apni maa Renuka ka sir kaata (cut off), aur apne pita ke vachan ko nibhaya. Main bhi wahi kar raha hoon — apne pita ka aadesh maanna mera kartavya (duty) hai.”

Phir Rama ne Lakshman se kaha —
“Hey Lakshman, mujhe teri shakti aur prem dono ka pata hai. Par tu gusse mein maa ke dukh ko aur badha raha hai. Hamara kartavya hai dharma ka palan karna (follow righteousness). Pitaji ke shabd hi dharma hain, aur main unka paalan karunga. Khoon-kharaba (bloodshed) se koi laabh nahi milega. Agar tu sach mein mujhe prem karta hai, toh mere saath van chalo, bina hinsa ke.”

Phir Ram maa Kaushalya ke paas gaya, haath jodkar bola —
“Hey Maa, mujhe vanvaas jaane ki anumati (permission) dijiye. Main 14 saal ke baad wapas aaunga, pita ji ka vachan poora karke. Jaise Raja Yayati ne apne karm ke baad fir se swarg (heaven) prapt kiya, waise hi main bhi laut aunga. Aap pita ji ka dhyaan rakhiyega, unhe santvana (comfort) dijiye. Main aap sabka seva phir se karunga jab laut aaunga.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Maa Kaushalya roti hui boli —
“Hey Ram, agar tu sach mein dharma jaanta hai, toh yaad rakh — maa bhi pita ke barabar hoti hai. Tu mujhe chhodkar kaise ja sakta hai? Tere bina mujhe zameen, swarg, sab vyarth (meaningless) lagte hain. Bas tera saath hi mera sukh hai.”

Rama ne maa ke shabdon ko dhairya (patience) se suna, par apni niyati (decision) par adig (firm) raha.
Unhone maa ko samjhaya —
“Hey Maa, pita ke vachan todna adharm (sin) hoga. Raja hamare pita hi nahi, hamare guru (teacher) aur raja bhi hain. Main unka aadesh nahi taal sakta. Aap mujhe aashirvad (blessing) dijiye taaki main apna dharm poora kar saku. Mujhe rajya ki lalach nahi, mujhe sirf satya aur dharm chahiye.”

Yeh kehkar Ram ne maa Kaushalya ke charan (feet) chhuye, unke charon or (around her) parikrama (circumambulate) ki, aur mann mein vanvaas ke liye nikalne ka sankalp (resolve) liya.
        """
        create_image_text_layout("attached_assets/chapter2/2.21.2.jpg", text3, layout="side", image_position="right")

    # Chapter22
    with st.expander("Chapter 2.22 - Rama tells Lakshmana not to be sad"):

        text1 = """
Shri Rama ne apne bhai Lakshman ki taraf dekha. Lakshman ka mann gusse se bhara tha — unki aankhein laal thi, saans tez chal rahi thi, jaise ek gussa hua hathi. Unka dil Kaikeyi ke liye krodh (anger) se bhar gaya tha.

Tab Shri Rama ne pyaar aur shaanti se kaha —
“Hey Bhai Lakshman, apna gussa aur dukh chhod do. Dhairya (patience) rakho. Mujhe ab van (forest) ke liye tayyar hona hai, jaise tum mere rajyabhishek (coronation) ke liye hue the. Ab tum wahi utsaah (enthusiasm) van jaane ki tayyari mein lagao.”
        """
        create_image_text_layout("attached_assets/chapter2/2.22.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Rama ne samjhaya,
“Kaikeyi maa ke mann mein kuch shanka (doubt) hai. Unhe lagta hai tum bal (force) se mujhe raja bana doge. Mujhe unka dukh bardasht nahi hota. Mujhe yaad nahi ki maine kabhi pita aur mata ko apne haath se dukh diya ho. To chalo, hum unka mann shaant karte hain.”

“Bhai, agar maine rajyabhishek ki ichha nahi chhodi, to pita Maharaj Dasharath ke vachan (promise) ka ullanghan (breaking) hoga — aur unka dukh mere jeevan bhar ka bojh ban jaayega. Isliye main bina deri ke van jaane ka nishchay karta hoon.”

“Kaikeyi maa tabhi shaant hongi jab main mrigcharm (deer skin) pehankar, jata (matted hair) baandhkar van chala jaunga. Unka dil tabhi sukoon (peace) paayega. Mujhe unhe dukh nahi dena.”

“Bhai Lakshman, yeh rajya meri kismet (destiny) mein nahi tha. Agar vidhi (fate) chahti, to Kaikeyi mujhe kabhi van nahi bhejti. Main kabhi teenon maton (mothers) mein farq nahi karta tha, aur Kaikeyi ne bhi mujhe Bharata se alag nahi maana tha. Lekin aaj, bhagya (destiny) ke likhe se, unhone kathor (harsh) aur nirdai (cruel) shabd bole.”

“Yeh sab daiva (God’s will) hai. Agar aisa nahi hota, to ek rajkumari jaise sanskaari (cultured) aur komal (gentle) swabhav ki Kaikeyi aise kathin shabd kaise bolti? Jo baat manushya nahi samajh sakta, use daiva ka niyam (divine rule) samajhna chahiye. Brahma ji bhi apne karma (past actions) se bacha nahi sakte.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
“Har sukh-dukh, dar, krodh, jeevan, mrityu — sab kuch hamare apne karmon ka phal (result) hai. Bade se bade rishi bhi apne karmon ke karan bhatak jaate hain. Jo kuch aaj hua — mera rajyabhishek ruk gaya — yeh bhi karma ka phal hai. Isliye mujhe isme dukh nahi.”

“Bhai, tum bhi shok (grief) chhod do. Mujhe van mein jaane do. Yeh pavitra jal (sacred water) jo mere rajyabhishek ke liye rakha gaya tha, ab usi se main apna tapasya (penance) jeevan shuru karunga.”

“Raja banna aur van mein rehna, dono mein bahut bada antar nahi hai — bas drishti (perspective) ka farq hai. Kaikeyi maa ko dosh (blame) mat do; yeh sab karma aur daiva ki leela (divine play) hai.”
        """
        create_image_text_layout("attached_assets/chapter2/2.22.2.jpg", text3, layout="side", image_position="right")

    # Chapter23
    with st.expander("Chapter 2.23 - Lakshmana wants to go with Rama"):

        text1 = """
Jab Shri Rama ne van jaane ka nishchay (decision) kiya, to Lakshman ka dil dukh aur gusse se bhar gaya. Uska sir jhuka hua tha, aankhein lal, aur saans tez jaise kisi gusse wale saanp (snake) ki. Wo apne bhai ke saamne khada tha — kadam se hilta hua, jaise ek gussa hua sher (lion) ya hathi apni soond (trunk) hila raha ho.

Lakshman ne apne bade bhai se kaha,
“Hey Rama bhaiya, aap to dharm ke gyaani ho, par aaj aap galat samajh rahe ho. Yeh kehna ki pita ke vachan (promise) ka virodh karna adharma (wrong) hai — yeh samay galat hai aisa kehne ka! Aap ek veer (warrior) ho, apni kismet (fate) khud likh sakte ho. Phir aap itne kamzor kyun ban rahe ho?”

        """
        create_image_text_layout("attached_assets/chapter2/2.23.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“Rama, kya aapko nahi lagta ki Raja Dasharath aur Kaikeyi ne dhokha (deception) kiya hai? Agar yeh vachan sach tha, to phir rajyabhishek (coronation) ki taiyari pehle hi kyun hui? Yeh sab unka swarth (selfishness) hai. Kaise ho sakta hai ki chhota bhai (Bharat) bade bhai (Rama) se pehle rajgaddi (throne) sambhale? Main yeh kabhi nahi hone dunga!”

Lakshman ka gussa badhta gaya —
“Yeh dharm ki baat mujhe samajh nahi aati, Bhaiya. Aap itne shaktishaali (powerful) hote hue bhi Kaikeyi ke anyaay (injustice) ko kyun maan rahe ho? Aap kyun unke jhoothe vachan ke aage jhuk rahe ho? Aap keh rahe ho yeh sab bhagya (fate) hai — par main maanta hoon ki veer (brave) log apna bhagya khud likhte hain!”

“Main dekhta hoon aaj, daiva (destiny) jeet ta hai ya purusharth (effort)! Agar bhagya aapke rajyabhishek ko rok raha hai, to main apni shakti se us bhagya ko tod doonga!”

Lakshman ne apna dhanush (bow) uthaya aur bola —
“Chahe devtaon (gods) ke raja Indra hi kyun na rukawat ban jayein, main unhe bhi haar doonga! Jo bhi aapka rajyabhishek roke, main unhe mitti mein mila doonga. Mera talwar (sword) sajaavat ke liye nahi, dushmanon ke liye bani hai! Mera dhanush aur baan (arrows) in anyayon (injustices) ko mita dene ke liye hai.”

“Bas aap ek baar aadesh (command) dijiye, Rama bhaiya. Bataiye kaun hai dushman, main use apne baanon se cheer (pierce) daalunga. Aaj hi main sabko dikha doonga ki aapka rajya koi chheen nahi sakta. Yeh dono haath jo sada daan (charity) aur raksha (protection) mein lage rahe, aaj aapke viruddh khade hone walon ka vinash (destruction) karenge!”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Lakshman ke shabd bijli jaise the — bhakti aur krodh (anger) dono se bhare hue.

Tab Shri Rama ne shaant hote hue, muskaan ke saath kaha —
“Hey Lakshman, mere pyaare bhai, mera sabse bada veerata (bravery) yudh jeetna nahi, balki pita ke vachan ko nibhana (fulfil) hai. Sachcha dharm wahi hai jo pita ke aadesh ko maanata hai, chahe uske liye van hi kyun na jaana pade.”
        """
        create_image_text_layout("attached_assets/chapter2/2.23.2.jpg", text3, layout="side", image_position="right")

    # Chapter24
    with st.expander("Chapter 2.24 - Rama stays strong in his decision"):

        text1 = """
Jab Shri Rama ne apne pita ke aadesh (command) ko maanne ka dridh (firm) sankalp liya, to Mata Kaushalya ke aankhon mein aansu bhar aaye. Unka gala bhavnaon se ruk gaya tha. Unhone pyaar aur dukh bhare swar mein kaha —

“Hey Rama, mere lal, tu to kabhi kasht (hardship) nahi dekha. Raja Dasharath ka vanshaj (descendant) aur meri kokh ka phal, tu hamesha sabse madhur (sweet) aur vinamra (humble) baat karta raha. Tu jo sada ghee-makhan khaata tha, wo ab van mein phal-mool (fruits and roots) kha ke kaise rahega? Log kya sochenge jab jaanenge ki Raja Dasharath ne apne sabse sadgunwan (virtuous) bete ko vanvaas (exile) bhej diya?”

        """
        create_image_text_layout("attached_assets/chapter2/2.24.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“Agar aise putra ko bhi banaya gaya, to nishchit (surely) sab kuch bhagya (fate) ke adheen hai. Mere dil mein jo dukh ka agni jal rahi hai, wo teri judai (separation) ki hawa se aur bhadakti ja rahi hai. Yeh aansuon ka dhuaan mujhe jala dega, jaise jungle ki aag sab kuch raakh kar deti hai. Rama, jaise gai apne bachde (calf) ke peeche daudti hai, waise main bhi tere peeche chal padungi.”

Tab Rama ne shaant aur vinamra swar mein kaha —
“Hey Mata, pita Maharaj Dasharath pehle hi dukh se toote hue hain. Agar aap bhi mujhe van tak saath chalengi, to unka hriday (heart) is dukh ko nahi sah paayega. Patni ka sabse bada kartavya (duty) hai apne pati ki seva karna. Jab tak pita ji jeevit hain, aapka dharm (duty) unki seva karna hi hai.”

Mata Kaushalya ne aansuon ke beech kaha —
“Putra, tu sahi keh raha hai. Tere vachan sach aur dharmik (righteous) hain.”

Rama ne fir kaha —
“Hey Devi, humein dono ko apne pita ka aadesh maanana chahiye. Ve hamare guru (teacher), pita (father), aur aapke pati (husband) hain — hum sab ke swami (lord) hain. Main choudah varsh van mein rahkar tapasya (penance) karunga, aur phir lautkar aapki seva karunga.”

Mata Kaushalya roti hui boli —
“Hey beta, main apne pratidvandvi (rival) ranion ke beech kaise jee paungi? Agar tu jaane par dridh hai, to mujhe bhi apne saath le chal. Main bina tere kaise jeeyungi?”

Rama ne pyaar se kaha —
“Hey Mata, jab tak patidev (husband) jeevit ho, stri (woman) ko unki seva hi karni chahiye. Raja Dasharath hum sabke swami hain. Aur Bharat bhai bhi punya-aatma (virtuous) hain, wo kabhi aapka apmaan nahi karenge. Jab main van jaaun, to pita ji ka dukh aur na badhne paaye — aap unka dhyaan rakhiye. Jo stri apne pati se viraag (neglect) karti hai, use punya (merit) nahi milta, par jo stri apne pati ke prati nishtha (devotion) rakhti hai, wo svarg (heaven) paati hai.”

“Yeh patiseva (service of husband) hi stree ka param dharm hai — Vedo aur shastraon (scriptures) ne bhi yahi kaha hai. Aap devtaon ki seva karna, brahmanon ko bhojan aur daan dena, aur apni shuddh dincharya (pure daily routine) banaye rakhna. Jab main lautunga, sab theek ho jaayega.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Mata Kaushalya ne aansuon bhari aankhon se kaha —
“Hey putra, tera van jaane ka nishchay pakka hai, aur main tujhe rokh nahi sakti. Jo likha hai, wahi hota hai. Ja beta, bhagwan tera raksha kare. Tu sukh se wapas aaye — yahi meri prarthana (prayer) hai.”

Ant mein, Mata Kaushalya ne apne haath uthakar ashirvaad diya —
“Ja mere beta, Rama — tujhe van mein bhi shanti, samman aur suraksha mile. Jab tu lautega, teri maa fir se jeevan paayegi.”
        """
        create_image_text_layout("attached_assets/chapter2/2.24.2.jpg", text3, layout="side", image_position="right")

    # Chapter25
    with st.expander("Chapter 2.25 - Kaushalya blesses her son Rama"):

        text1 = """
Mata Kaushalya ne apne dukh ko sambhalte hue, haath se kuch pavitra paani liya aur apne mann ko shant karte hue Shri Rama ke liye ashirvaad (blessing) dene ka sankalp liya. Unhone kaha,
“Hey mere putra, Raghu vansh ke veer, main tumhe rok nahi sakti. Tum jao, aur jab wapas aao to sada dharm (righteous path) par chalna. Tumne hamesha sachchai aur maryada (righteous conduct) ka palan kiya hai — wahi tumhara raksha kare.”

Mata ne prarthana ki, “Tumhe sab devta aur rishi (sages) ka ashirvaad mile. Tumhe Maharishi Vishwamitra dwara diye gaye astra-shastra (divine weapons) hamesha surakshit rakhein. Pahad, nadiyan, ped-paudhe, pakshi aur sabhi prani tumhe apni shakti se bachayein. Brahma, Indra, Surya, Chandra aur sab graha (planets) tumhe mangal aur raksha dein.”

        """
        create_image_text_layout("attached_assets/chapter2/2.25.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Phir Mata Kaushalya ne kaha, “Jungle mein tumhe koi rakshas (demon), pishach (evil spirit), ya jangli janwar haani na pahunchayein. Tumhe hamesha fal, mool (roots), aur bhojan milta rahe. Tumhara har kadam safal aur shubh ho. Agni (fire), Vayu (wind) aur sab pavitra mantr (sacred chants) tumhara raksha karein.”

Iske baad Mata ne brahminon ke saath hawan (sacred fire ritual) kiya. Unhone ghee, phool, aur chandan se devtaon ki puja ki aur Rama ke kalyan ke liye mantr ucharan karaye. Brahminon ne bhi Rama ke liye ashirvaad diye —
“Jaise Indra ne Vritrasur ko jeet kar shanti paayi, jaise Garuda ne amrit (nectar of immortality) lekar vijay paayi, waise hi Rama tum bhi vijayi aur surakshit raho.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Ant mein, Mata Kaushalya ne Rama ke sir par chawal chhidka, chandan lagaya aur Vishalya Karini (healing wood) di, taaki unhe koi chot na lage. Fir unhone Rama ko gale lagaya, maathe par pyaar kiya aur kaha,
“Beta, ab jao. Apne pita ke aadesh (command) ko poora karo aur swasth wapas aana. Mera sukh tabhi poora hoga jab main tumhe Ayodhya ka raja bante dekhoongi.”

Aansuon se bhari aankhon se Mata ne apne putra ka parikrama (circumambulation) kiya, aur Rama ne unke charan sparsh karke viday li, Sita ke mahal ki or chal diye.
        """
        create_image_text_layout("attached_assets/chapter2/2.25.2.jpg", text3, layout="side", image_position="right")

    # Chapter26
    with st.expander("Chapter 2.26 - Rama tells Sita about going to the forest"):

        text1 = """
Apni maa se viday lekar, Shri Rama, jo sada dharm (righteousness) ke palak the, Ayodhya ki bheed bhari sadkon se guzar rahe the. Unka chehra shaant tha, aur unki vinamrata (humility) sabke dilon ko shanti de rahi thi.

Iss samay Rajkumari Sita, jo sabhi devtaon ki pooja mein lagi thi, apne mann mein khushi se bhari thi. Unhe laga Rama ka rajyabhishek (coronation) hone wala hai, isliye wo apne pati ke aane ka intezaar kar rahi thi — aankhon mein sapne aur hriday mein garv.

        """
        create_image_text_layout("attached_assets/chapter2/2.26.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Lekin jab Rama mahal mein aaye, to unka roop sada ke jaise tha — bina shringar ke, sad aur chintit (worried). Unhe dekh kar Sita ka mann hil gaya. Wo turant uth gayi aur ghabra kar boli,
“Hey Prabhu, aaj to Pushya nakshatra aur Chandrama dono shubh yog (auspicious alignment) mein hain. Brahmin ne aaj hi aapka rajyabhishek tay kiya tha. To fir aapka chehra udaas kyu hai? Main kyun nahi dekh rahi wo raj chhatra (royal canopy) jo aapke sir ke upar hona chahiye tha? Kyu nahi dikh rahe wo chamara (white fans) ya wo haathi aur ghode jo aapke saath hone chahiye the?”

Sita ne bechain hokar pucha,
“Prabhu, sab kuch taiyaar tha — brahmin, mantra, aur pooja — fir aap itne shant aur dukhi kyu hain?”

Rama ne gahri saans li aur dheere se bola,
“Sita, mere pita Maharaj Dasharatha ne mujhe vanvaas (exile) jaane ka aadesh diya hai. Bahut pehle unhone Rani Kaikeyi ko do vachan (boons) diye the. Aaj unhone wahi maang liye hain — ek mein mujhe choudah (14) saal ke liye van mein bhejna hai, aur doosre mein Bharat ko raja banana hai.”

Rama ne aage kaha,
“Main ab Dandaka van (forest) jaane ja raha hoon. Main tumhe alvida kehne aaya hoon. Jab main chala jaoon, tum Raja Bharat ke adheen (under his rule) rehna. Wo ab rajya ke adhipati (ruler) hain, aur unka samman karna tumhara dharm hai.”

Phir Rama ne pyaar aur samajh bhare shabdon mein kaha,
“Sita, tum meri maa Kaushalya ka seva karna. Wo mere jaane se dukh mein hain, unka mann sambhalna. Meri doosri maayen bhi mujhe apne bachhe ki tarah chahti hain — unka bhi adar (respect) karna. Bharat aur Shatrughna ko apne bhai samajhna, kabhi unhe krodhit (angry) mat karna. Raja ka hriday (heart) pavitra hai, lekin agar koi usse naraaz kare, to wo apne apno se bhi door ho jaata hai.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Ant mein Rama ne kaha,
“Meri priye, tum Ayodhya mein reh kar sabka samman karna, aur dhairya (patience) rakho. Main van ja raha hoon, lekin mera hriday tumhare saath hai. Jab main tapasya (penance) poori karke lautunga, tab hum phir milenge.”

Sita chupchaap Rama ko dekhti rahi — aankhon mein aansu, lekin hriday mein garv aur prem bhara hua tha.
        """
        create_image_text_layout("attached_assets/chapter2/2.26.2.jpg", text3, layout="side", image_position="right")

    # Chapter27
    with st.expander("Chapter 2.27 - Sita says she will go with him"):

        text1 = """
Jab Shri Rama ne Sita ko kaha ki wo Ayodhya mein hi rahe, to Sita, jo prem aur maryada (virtue) se bhari thi, unki baatein sun kar dukhi ho gayi. Lekin us dukh ke saath unke mann mein ek majboot sankalp (strong resolve) bhi tha.

Sita ne narm (gentle) lekin dridh (firm) swar mein kaha,
“Hey Arya (noble one), yeh kya keh rahe ho aap? Aapka yeh vachan to aise lagta hai jaise koi mazak ho! Patni ka jeevan to pati ke saath juda hota hai — jaise sharir aur aatma (body and soul) ek hote hain. Aap jahan bhi jaayein, mujhe bhi wahan jaane ka adhikaar (right) hai. Agar aapko vanvaas mila hai, to mujhe bhi uss vanvaas ka hissa banna hi hoga.”

        """
        create_image_text_layout("attached_assets/chapter2/2.27.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Wo aage boli,
“Ek stri (woman) ka sukh uske pati ke saath hi hai. Na pita, na maa, na putra — koi bhi uska sahara nahi hota, na is janm mein, na agle mein. Uska sab kuch to uska pati hi hota hai. Agar aaj aap van ja rahe ho, to main aapke pehle chal kar kaante aur kusha (thorny grass) hataungi, taaki aapka raasta saaf ho.”

Sita ka swar ab aur gahra ho gaya:
“Prabhu, mujhme aisa kya dosh (fault) hai jo mujhe Ayodhya mein akele rehna pade? Rajmahal ke sukh, ya devlok ke anand bhi, us sukh ke saamne kuch nahi, jo mujhe aapke seva (service) mein milta hai. Mujhe pita ne stridharma (duties of a wife) sikhaye hain, mujhe aur seekhne ki zarurat nahi. Main aapke saath van jaungi — jahan jangli jaanwar, pahad aur nadia (rivers) hain — aur wahan main utni hi khushi se rahungi jitni Ayodhya ke rajmahal mein.”

Usne hasi ke saath kaha,
“Main aapke saath fal aur mool (fruits and roots) khaungi, aur kabhi aapko chinta nahi karne dungi. Mujhe to bas aapka sang (company) chahiye, bas wahi mera swarg (heaven) hai. Main aapke saath nadion aur sarovaron (lakes) ke kinare chalungi, jahan hans (swans) aur kamal (lotus) khile honge. Wahan main aapke saath snaan (bath) karungi, khelungi, aur apni poori zindagi khushi se bitaungi.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Phir Sita ne gehri bhavnaon se kaha,
“Hey Ram, aapke bina mujhe swarg bhi sukh nahi dega. Agar aap van ja rahe ho, to mujhe bhi le chaliye. Aapke charanon ki seva karte hue, main wahin van mein jeevan bitaungi. Aapse juda rehkar to main jeeti hi nahi reh sakti. Kripya mujhe saath le chaliye — main aapke liye bojh (burden) nahi banungi.”

Sita ke ye narm aur vinamr shabd (humble words) sun kar Shri Rama ka hriday (heart) pighal gaya, lekin wo abhi bhi use van ke kathin jeevan (hard forest life) ke baare mein samjha kar manaane ka prayas kar rahe the.
        """
        create_image_text_layout("attached_assets/chapter2/2.27.2.jpg", text3, layout="side", image_position="right")

    # Chapter28
    with st.expander("Chapter 2.28 - Rama tries to stop her"):

        text1 = """
Shri Rama, jo satyavaadi (truthful) aur dharma-parayan (virtuous) the, Sita ke prem bhare anurodh (plea) ke baad bhi use van jaane ki anumati dene ke liye tayyar nahi the. Unhone socha, “Van ka jeevan bahut kathin hai — aur Sita jaise komal (delicate) aur bhole hriday wali ko wahan takleef hi milegi.”

Isliye, Rama ne pyaar bhare lekin dridh (firm) shabdon mein kaha:
“Hey Sita, tum ek rajkumari ho, gunvaan (virtuous) ho, aur dharma ka paalan karti ho. Tumhe Ayodhya mein rehkar maryada ke saath apna kartavya (duty) nibhaana chahiye. Van mein sukh nahi, sirf dukh aur kasht (pain) hai.”

        """
        create_image_text_layout("attached_assets/chapter2/2.28.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Wo aage bole,
“Jis van ko ‘Antara’ kaha gaya hai, uska arth hi hai ‘jo manushya ke rehne yogya nahi (unfit for living)’. Wahan pahaadon se nikalti nadiyan bahut kathin hoti hain paar karne ke liye. Singh (lions) garajte hain, jangli haathi idhar-udhar ghoomte hain, aur har kadam khatra hota hai. Isliye tum yahin raho, van tumhare liye nahi bana.”

Phir Rama ne van ke sankat (dangers) samjhaaye:
“Van ke raste kaante, zehri le creepers aur keechar (mud) se bhare hain. Wahan na komal takiye (soft pillows) milte hain, na shayan ke liye bistar — bas sukhaye hue patton (dry leaves) par sona padta hai. Wahan khana bhi sirf pedon se girte hue phal hote hain — na roti, na pakwan. Har din bhookh aur kathin tapasya (penance) se guzarna padta hai.”

Rama ne use vanvaasi jeevan ke niyam bhi bataye:
“Wahan log bark ki vastra (bark clothes) pehente hain, jata (matted hair) banate hain, aur roz teen baar snan (bathing) karte hain. Devata aur pitron (ancestors) ko puja karni hoti hai, aur mehmaan aaye to seva karni hoti hai — chahe apne paas kuch bhi na ho. Aur jab hawayein tez chalti hain, to din mein bhi andhera chha jaata hai.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Rama ka swar bhari bhavnaon se bhar gaya:
“Hey priye (beloved), van mein saanp, vishdhar (poisonous snakes), bichoos (scorpions), madhu-makkhiyan (hornets), aur machhar (mosquitoes) ka dukh hamesha satata hai. Jangli ghaas aur tedhe-medhe ped raste rokte hain. Sharir kamzor ho jaata hai, bhookh lagti hai, aur sukh shanti kahin nahi milti.”

Ant mein unhone kaha,
“Hey Sita, van mein rehne wala apna krodh (anger) aur lobh (greed) sab chhod deta hai, tapasya karta hai, aur har bhay (fear) ko tyag deta hai. Tumhare jaise komal aur sundar rajkumari ke liye wahan sirf kasht hi hai. Kripya van jaane ka vichar (thought) chhod do — main sirf tumhe surakshit (safe) rakhna chahta hoon.”

Is tarah Rama ne Sita ko samjhaane ki poori koshish ki, par Sita ka hriday (heart) apne pati ke saath jaane ke sankalp se hil nahi saka. Wo aansuon se bhare nayanon (eyes) ke saath Rama ko jawab dene lagi.
        """
        create_image_text_layout("attached_assets/chapter2/2.28.2.jpg", text3, layout="side", image_position="right")

    # Chapter29
    with st.expander("Chapter 2.29 - Sita keeps asking lovingly to go"):

        text1 = """
Jab Shri Sita ne Rama ke kathin (hard) shabdon ko suna, unka hriday dukh aur prem se bhar gaya. Aansu unke gaalon (cheeks) par beh rahe the, aur komal swar (gentle voice) mein unhone kaha:

“Hey Rama, tumne jo van ke dukh (sufferings) bataye, mere liye wo sab tumhare saath sukh (joy) ban jaayenge. Van ke jangli jaanwar — hiran (deer), bhalu (bears), sher (lions), haathi (elephants), aur pakshi (birds) — tumhara mukh dekhkar hi bhay (fear) se door bhag jaayenge. Tumhara tej (divine radiance) sab par prabhav daalta hai, hey Prabhu! Jab tak main tumhare paas hoon, mujhe koi nuksaan nahi pahucha sakta, na Indra dev bhi.”

        """
        create_image_text_layout("attached_assets/chapter2/2.29.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Sita ne yaad dilaya:
“Tumne hi mujhe sikhaya tha ki patni (wife) ko apne pati se kabhi alag nahi hona chahiye. Aur mujhe bachpan mein hi mere pita ke mahal mein ek jyotishi (astrologer) ne bataya tha ki mujhe ek din van mein rehna padega — par apne pati ke saath! Tab se main us din ka intezaar kar rahi hoon, aur ab jab samay aa gaya hai, mujhe rokna mat.”

Phir unhone madhur aur dridh (firm yet loving) bhavna se kaha:
“Hey Arya (noble one), mujhe van jaane ki anumati do — ye mera dharm (duty) hai aur meri prarthana bhi. Tumhare saath van mein rehkar seva karna mere liye sabse bada sukh hoga. Tumhare saath dukh bhi sukh lagta hai. Main jaanti hoon van mein kathinaiyan (hardships) hain, lekin jo apne man ko jeet leta hai, uske liye sab kuch aasaan ho jaata hai. Mujhe tumhare saath jane do, taaki main bhi apne punya (virtue) kamaa sakoon.”

Unhone apni bhavna aur adhik prakat ki:
“Hey Rama, bachpan mein maine apni maa ke saamne ek tapasvini (pious woman) se suna tha ki main tumhare saath van mein rahungi. Mujhe us bhavishvani (prophecy) ko satya (true) karna hai. Maine pehle bhi tumse kaha tha ki main tumhare saath van mein khelna chahti hoon — ab wahi samay aa gaya hai. Kripya mujhe saath le chalo.”

Phir Sita ne bhakti aur prem se bhare shabdon mein kaha:
“Main tumhare saath van mein jaakar sab paap (sins) se mukta ho jaungi. Tum mere liye devata se bhi badhkar ho — agar main mar bhi gayi, to bina tumhare mujhe swarg (heaven) bhi sukh nahi de sakta. Mujhe pata hai, jo patni apne pati ko dharm ke niyam (law) ke anusaar di jaati hai, wo uske saath har janm aur har lok (world) mein bandhi rehti hai. Isliye main tumse alag nahi reh sakti.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Ant mein Sita ne dridh pratigya (firm vow) li:
“Hey Rama, agar tum mujhe saath nahi loge, to main apni jaan de dungi — chahe zeher kha kar ya nadi mein doob kar. Tumse alag rehna mere liye jeevan se bhi kathin hai.”

Rama ne jab Sita ke aansuon ko zameen par girte dekha, unka hriday karuna (compassion) se bhar gaya, par wo abhi bhi use rokne ka prayas kar rahe the. Sita ka prem aur nischay (determination) dono aur gehra hote ja rahe the…
        """
        create_image_text_layout("attached_assets/chapter2/2.29.2.jpg", text3, layout="side", image_position="right")

    # Chapter30
    with st.expander("Chapter 2.30 - Rama agrees to take Sita with him"):

        text1 = """
Shri Rama ne phir Sita ko samjhaya ki vanvaas (forest life) bahut kathin (difficult) hoga.
Unhone kaha — “Jungle mein jangli jaanwar hain, tez garmi aur thand hai, aur khana bhi sirf jhad ke phal aur jad (roots) milenge.”
Par Sita ne apna mann nahi badla.
Woh thodi si dari hui thi, par unke prem (love) aur garv (pride) ne unhe majboot banaya.

Sita muskura kar boli, “Prabhu Rama, agar mere pita Raja Janaka jaante ki aap sirf roop se purush (man) hain, par hriday (heart) se kamzor, to unhone mujhe kabhi aapke saath nahi diya hota.”
Unke shabd teekhe the, par unme sachcha prem tha.

        """
        create_image_text_layout("attached_assets/chapter2/2.30.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Sita boli, “Log kehte hain aap surya (sun) ke samaan chamakte hain, par mujhe to aaj wo tej nahi dikh raha. Aap kyun ghabra rahe hain? Mujhe chhodkar kyun ja rahe hain? Main to aapki patni (wife) hoon, aapki saathi hoon. Jaise Savitri ne apne pati Satyavan ke saath har dukh saha, waise hi main bhi aapke saath rahungi.”

Uski aankhon mein aansu aa gaye.
Woh boli, “Mainne kabhi kisi aur purush ko nazar tak nahi uthai. Main un mahilaon jaise nahi hoon jo apne kul (family) ka samman bhool jaati hain. Isiliye mujhe saath le chaliye. Mujhe Bharata ke paas kyun chhodna chahte hain? Main to aapke saath har janm rahungi. Chahe aap tapasvi (ascetic) banein ya devlok (heaven) chale jaayein, main saath chalungi.”

Sita ne kaha, “Aapke saath chal kar jungle ke kaante bhi mujhe mridul (soft) lagenge. Jo dhool mere sharir par lagegi, woh mujhe chandan (sandalwood paste) jaisi lagegi. Aap jo bhi phal, mool (roots) ya patte laayenge, woh mujhe amrit (nectar) jaise lagenge. Aapke saath jungle bhi swarg (heaven) lagega, par aapke bina yeh mahal narak (hell) ban jaayega. Agar aap mujhe saath nahi le jaayein, to main jee nahi paungi. Main aapke bina jeevan nahi chahti.”

Yeh kehkar Sita ro padi.
Woh Shri Rama ko gale laga kar bilakhne lagi, jaise ek ghaayal (wounded) hathi apne saathi se bichhad gaya ho.
Uski aankhon se moti jaise aansu gir rahe the, jaise kamal ke phool se paani ke bindu (drops) phisal jaate hain.
Uska mukh (face), jo pehle poornima ke chand jaisa tha, dukh ke aag se murjha gaya tha.

Rama ne use apni baahon mein sambhala aur pyar se kaha,
“O Devi (Goddess), agar tumhe dukh ho, to mujhe swarg (heaven) bhi sukh nahi de sakta. Mujhe kisi baat ka dar nahi hai. Main to tumhe surakshit rakhne ke liye mana kar raha tha. Par ab jab tumhara dridh sankalp (firm resolve) dekh liya hai, to main tumhe kabhi nahi chhod sakta.”

Unhone kaha, “Main van mein apni marzi se nahi ja raha, par pitaji ke aadesh (command) se ja raha hoon. Putra ka kartavya (duty) hota hai ki woh apne mata-pita aur Guru (spiritual teacher) ki seva kare. Jo apne mata-pita ki seva karta hai, use swarg, dhan (wealth) aur gyaan (wisdom) sab milta hai. Sita, tumne apna prem aur sahas (courage) sabit kar diya hai. Ab tum meri jeevan saathi ban kar mere kartavya mein saath dogi.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Rama muskuraye aur bole,
“Ab tayyar ho jao. Apne gehne (jewels) aur vastra (clothes) brahminon aur garibon mein baant do. Jo bache, naukron mein vibhajit (distribute) kar do. Ab hume der nahi karni.”

Sita ke chehre par khushi chamak uthi.
Usne bina vilamb (delay) sab kuch daan (charity) mein de diya — gehne, kapde, aur dhan.
Uska mann ab shaant aur prasann (happy) tha — kyunki ab woh apne priyatam (beloved) Rama ke saath vanvaas jaane wali thi, jahan woh unka dukh aur duty dono mein saath degi.
        """
        create_image_text_layout("attached_assets/chapter2/2.30.2.jpg", text3, layout="side", image_position="right")

    # Chapter31
    with st.expander("Chapter 2.31 - Lakshmana also decides to join them"):

        text1 = """
Jab Shri Lakshman ne Rama aur Sita ki baatein suni, uska dil bhar aaya. Wo zor se roya aur bola,
“Bhaiya, agar aap jungle (forest) ja rahe ho jahaan bahut jangli jaanwar aur haathi ghoomte hain, toh main apne baan (bow) aur teen (arrows) lekar aapke saath chalunga. Main aapke saath us sundar van (forest) mein rahunga, jahan hiran (deer) aur pakshi (birds) ki madhur aawaz hoti hai. Bin aapke, mujhe devlok (heaven) mein bhi rehna pasand nahi — na mujhe amaratva (immortality) chahiye, na rajya (kingdom).”

Rama ne pehle use mana karne ki koshish ki. Par Lakshman ne lagi raho—
“Bhaiya, jab aapne pehle mujhe saath chalne ki ijazat (permission) di thi, toh ab kyon rok rahe ho? Mera mann udas hai.”

        """
        create_image_text_layout("attached_assets/chapter2/2.31.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Rama ne samjhaaya,
“Lakshman, main tumhe bahut pyaar karta hoon. Tum mera chhota bhai, sevak (servant) aur mitra ho. Par agar tum mere saath chale gaye, to kaun Mata Kaushalya aur Sumitra ka dhyaan rakhega? Kaikeyi ka man badal sakta hai; jab Bharata uski prabhav (influence) mein hoga, shayad woh unki seva na kare. Isliye tum yahin rukkar maaon ki seva karo. Isi mein tumhara bahut punya (merit) hai.”

Lakshman ne pyaar bhare andaz mein jawab diya,
“Bhaiya, agar Bharata apni jimmedari (responsibility) nibhata hai, toh main wapas aa kar uski raksha karunga. Par agar woh anyaay kare, main use rok dunga. Main aapka sevak ban kar jungle mein aapke liye phal, roots aur aahaar (food) ikattha karunga. Main aapka rakhwala (protector) rahunga — sochiye mat, mujhe saath le lijiye.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Rama khush hua aur bola,
“Thik hai Lakshman. Jaakar apni maa Sumitra se anugya (permission) le lo. Aur Shri Vasistha ke ghar se woh dhanush (bow), kavach (armor) aur teer-dani (quiver) le aao jo Janaka ne mujhe di thi.”

Lakshman ne sab ko vidaa dekar, Shri Vasistha ke ghar se phool laga kar astra-shastra (weapons) lekar aaye aur Ram ko samarpit (present) kiya.
Rama ne hansi se kaha, “Ab hum brahminon aur tapasvinon (ascetics) ko daan (charity) karenge. Suyajna — Vasishtha ka putra — ko bulao aur sab pavitra (sacred) karyo ko poora kar ke hum nikalenge.”

Aur is tarah, Lakshman ne apni nischay (resolve) dikhaya — bhai ke saath, saath chalne ko taiyaar.
        """
        create_image_text_layout("attached_assets/chapter2/2.31.2.jpg", text3, layout="side", image_position="right")

    # Chapter32
    with st.expander("Chapter 2.32 - Rama gives away his gold and wealth"):

        text1 = """
Jab Shri Rama ne vanvaas (forest exile) jaane ka faisla liya, unhone Lakshman ko kaha ki woh Rishi Suyajna ke paas jaayein. Lakshman turant gaye aur dekha ki rishi apne yagya mandap (sacrificial pavilion) mein baithe hain. Unhone pranam karke kaha,
“Hey Maharishi, Shri Rama rajya tyag kar van mein ja rahe hain. Kripya unse milne jaldi chaliye.”

Rishi ne apna sandhya vandan (evening prayer) kiya aur Lakshman ke saath Shri Rama ke sundar mahal mein aaye. Shri Rama aur Sita ne unka swagat bahut adar se kiya — dono haath jod kar, charanon mein pranam karke.

        """
        create_image_text_layout("attached_assets/chapter2/2.32.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Phir Shri Rama ne unhe daan diya — sundar gehne, motiyon ke haar, sone ke kangan, mukut, kundal, aur anek anmol ratna. Shri Sita ke kahne par, Rama ne kaha,
“Hey Shant Rishi, Sita ji chahti hain ki aapki patni in sone ke gehno aur haar ko apnayein. Iske saath hi yeh komal shayya (soft couch) bhi swikar karein, jisme moti aur heere lage hain. Yeh haathi ‘Shatranjaya’, jo mujhe mere mama ne diya tha, aur iske saath ek hazaar sone ke sikke bhi, main aapko pradan karta hoon.”

Rishi Suyajna ne sab daan svikar karke Rama, Lakshman aur Sita ko ashirwad diya.

Uske baad Rama ne Lakshman se kaha,
“Hey Lakshman, Rishi Agastya aur Rishi Vishwamitra ke putron ko bulao aur unhe ratnon ka daan do. Har ek ko ek hazaar gaayen, sona, chandi, gehne aur vastra do. Un brahminon ko bhi daan do jo roj maa Kaushalya aur Sumitra ko ashirwad dete hain — unhe rath, silk ke kapde aur dasiyan (maid servants) do, taaki ve santusht rahein.”

“Apne salahkar Citaratha ko bhi dhan aur gehne do. Aur jo brahmachari (students) mere saath Veda ka adhyayan karte the, unhe bhi ek hazaar gaayen aur bahut saare daan do. Har ek ko assee (80) oont ratnon se lade hue, ek hazaar bail anaaj ke saath, aur do sau bail kheti ke liye dena. Maa Kaushalya ke seva karne wale brahmachariyon ko bhi ek hazaar gaayen aur sone ke sikke dena, taaki maa humse prasann rahein.”

Lakshman ne bhai ke sab aadesh poore kiye. Jaise dhan ke devta Kuber daan dete hain, waise hi Lakshman ne sab brahminon ko dhan-dolat se bhar diya.

Phir Rama ne apne naukaron ko dekha jo aansuon se ro rahe the. Rama ne unhe jeevan bhar ke liye paryapt dhan diya aur kaha,
“Main jab tak vanvaas se wapas na aa jaun, mere aur Lakshman ke mahal ki dekhbhal tum sab karna.”

Rama ne khajana mangwaya aur sona-chandi ka pahaad unke samne rakha gaya. Phir unhone budhon, bimaron aur garibon mein sab dhan baant diya.

Isi samay ek brahmin aaya, jiska naam Trijata tha — Garga kul se tha, lekin bahut garib tha. Din bhar van mein phal-phool ikattha karta, taaki apne parivar ka pet bhar sake. Uski patni ne usse kaha,
“Hey praan nath, aaj apna hal aur bel chhodkar Shri Rama ke paas jaaiye. Mujhe vishwas hai, aapko kuch zarur milega.”

Brahmin apne purane faate kapdon mein, Shri Rama ke mahal pahunch gaya. Rama ne muskurate hue kaha,
“Hey Brahmin, mere paas abhi bhi kai hazaar gaayen baaki hain. Apni laathi yahan se fenk do — jitni door girti hai, utni gaayen main tumhe de dunga.”

Trijata ne poori shakti se laathi feki, aur woh Sarayu nadi ke doosre kinaare jaake giri — jahan hazaron gaayen char rahi thi! Rama ne turant aadesh diya ki sab gaayen Trijata ke ashram tak pahunchai jaayein.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Phir unhone kaha,
“Hey Brahmin, maine tumse mazak kiya tha, lekin tumhari shakti dekhkar main prasann hoon. Jo chaaho maango, main sab dunga. Mujhe sabse adhik sukh daan dene se milta hai.”

Trijata khushi se bhar gaya, apni patni ke saath gaayen lekar gaya, aur Rama ko ashirwad dete hue bola,
“Hey Shri Rama, tumhara yasha (glory) sada amar rahe.”

Ant mein Rama ne apne sab mitron, sevakon, aur garibon ko bhi dhan daan karke sammanit kiya. Us samay Ayodhya mein koi bhi vyakti — na brahmin, na sevak, na bhikhari — aisa nahi tha jise Shri Rama ne daan na diya ho. 💫
        """
        create_image_text_layout("attached_assets/chapter2/2.32.2.jpg", text3, layout="side", image_position="right")

    # Chapter33
    with st.expander("Chapter 2.33 - Rama, Sita, and Lakshmana go to meet the king"):

        text1 = """
Apna saara dhan-daulat brahminon aur garibon ko daan karne ke baad, Shri Rama, Sita aur Lakshman Raja Dasharath se milne nikal pade. Unke peeche sevak chal rahe the — haath mein phoolon aur chandan se sajaye hue hathiyaar le kar.

Jab Ayodhya ke logon ko pata chala, toh sab log unhe dekhne ke liye unche mahalon aur saat-manjila imaraton ki chhat par chadh gaye. Lekin sab ke dil dukhi the.

Kuch log keh rahe the —
“Dekho, pehle Shri Rama ke saath chaaron sena vibhag (army divisions) chalti thi, aur aaj unke saath sirf Sita aur Lakshman hain.”

        """
        create_image_text_layout("attached_assets/chapter2/2.33.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Doosre log bole —
“Shri Rama, jo rajya ke sab sukh bhog chuke hain, aaj apne pita ke vachhan ko poora karne ke liye sab kuch tyag rahe hain. Jo praja ke liye dhan daan karta tha, wahi Rama aaj banvaas (exile) ke liye ja raha hai. Aur dekho, Sita — jise kabhi aam logon ne nahi dekha tha — aaj sabke saamne sarak par chal rahi hai.”

Ek ne kaha —
“Raja Dasharath par to jaise koi dusht atma chha gayi hai, tabhi unhone apne itne priya putra ko vanvaas bhej diya!”

Dusra bola —
“Arre, kisi ne kabhi apraadhi (traitor) ko bhi is tarah nahi nikala, phir Rama to sabse nyayapriya aur dayalu hain! Ve nirdosh, satyavaadi, vidwan aur vinamra hain. Puri praja unse itni prem karti hai ki unka jaane ka dukh sabko sukhahin kar raha hai — jaise garmi ke mausam mein jal bina pankhi tadapta hai.”

Ek aur bola —
“Rama to dharma ke mool (root) hain, aur hum log unke phool-patte. Agar ve chhod diye jaayein, to hum bhi murjha jaayenge. Chalo, hum sab apne khet, ghar, aur shehar chhodkar unke saath van mein chalein.”

Sab kehne lage —
“Jab Rama nahi honge, to Ayodhya bhi veeran (deserted) ho jaayegi. Na koi puja, na snan, na safai — bas mitti aur andhera reh jaayega. Gharoon mein devta nahi, bas chuhe daudte dikhenge. Phir is jhoot aur paap se bhare mahal ka bhog Kaikeyi aur uska putra karein.”

Ek aur ne kaha —
“Hum prarthna karte hain ki Ayodhya jungle ban jaaye aur jahan Rama rahenge, wahi nagar ban jaaye! Saap apne bil chhod dein, hiran aur pakshi pahaadon se utar aayein, sher aur haathi bhi van chhodkar Rama ke paas aa jaayein!”

Rama sab ye baatein sun rahe the, lekin unka man bilkul shant tha. Unka chalna ek yuva haathi ke jaise gambheer aur shaan bhara tha. Dheere-dheere ve Raja Dasharath ke mahal ke paas pahuche — jo Meru parvat ki tarah bhavya (grand) tha.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Mahalon ke dwar par pahredaar aur sainik khade the, aur wahan Sumantra bhi khada tha — udas aur chintit. Rama ne use muskura kar dekha, phir shok mein doobe logon ke beech se nikalte hue, pitaji ke kaksh (chamber) ki or badhe.

Raja Dasharath ke kamre ke bahar ruk kar, Rama ne Sumantra se kaha —
“Hey Sumantra, kripya Raja Dasharath ko batayein ki main Sita aur Lakshman ke saath unse milne aaya hoon.”

Vanvaas ke liye pratigya karke, Rama ab apne pita se antim ashirwad lene ke ichhuk the.
        """
        create_image_text_layout("attached_assets/chapter2/2.33.2.jpg", text3, layout="side", image_position="right")

    # Chapter34
    with st.expander("Chapter 2.34 - King Dasaratha blesses them with love and tears"):

        text1 = """
Shyaam varna (dark-complexioned) aur kamal-nayan (lotus-eyed) Shri Ram ne apne mantri Sumantra ko kaha ki ve Raja Dasharath ko unke aane ki suchna dein.

Sumantra jaise hi raja ke antahpura (royal chamber) mein gaye, unhone dekha — Raja Dasharath bahut dukhi baithe the. Aise lag rahe the jaise suraj par grahan lag gaya ho, ya aag raakh ke neeche dab gayi ho, ya talab bina paani ka ho gaya ho.

Haath jodkar Sumantra ne kaha —
“Jai ho Maharaj! Aapka putra Shri Rama, jo naron mein sher saman (lion among men) hain, dwar par khada hai. Usne apna saara dhan brahminon aur sevakon ko daan kar diya hai. Ab ve van (forest) jaane se pehle aapse milna chahte hain. Kripya unhe milne ka aashirvaad dijiye.”

        """
        create_image_text_layout("attached_assets/chapter2/2.34.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Raja Dasharath, jo dharma ke gyaata aur samudra jaise gambheer the, bole —
“Sumantra, sab ranivas ki mahilaon ko bulao, main Rama ko unke saamne dekhna chahta hoon.”

Sumantra ne jaake raniyon se kaha —
“Raja aap sabko turant bulawa bhej rahe hain.”

Phir Queen Kaushalya ke aaspaas 350 raniyan — sab ke sab ro-ro kar aankhen laal kar chuki thi — dheere-dheere raja ke paas aayiं.

Jab sab aa gayi, to Raja Dasharath ne kaha —
“Sumantra, ab Rama ko andar le aao.”

Thodi der baad Sumantra ne Shri Rama, Lakshman aur Sita ko le aaya. Raja Dasharath jaise hi Rama ko dekhte hain, turant khade ho jaate hain, lekin dukh ke maare behosh hokar zameen par gir jaate hain.

Rama aur Lakshman ne turant unhe sambhala aur apni baahon mein utha kar shayya (couch) par bithaya. Mahal mein har taraf ek hi dhvani goonjne lagi — “Rama! Rama!”
Sab mahilayein zor zor se rote hue chillane lagiं, unke gehno ki chhankar bhi unke vilap (lamentation) mein kho gayi.

Thodi der baad Raja Dasharath hosh mein aaye. Rama ne vinamrata se kaha —
“Pitashri, main ab Dandaka van ke liye nikal raha hoon. Kripya aashirvaad dein. Lakshman aur Sita bhi mere saath chalne ke liye dridh nishchay (firm resolve) kar chuke hain.”

Raja Dasharath ne karuna bhari nazar se dekha aur bole —
“Rama, main Kaikeyi ke kapat (deceit) ka shikar ho gaya hoon. Tu mujhe hata kar rajya le le, beta.”

Rama ne nivedan bhare shabd mein kaha —
“Pitashri, aap sahasra (thousand) varsh tak raj karein. Main apne vachhan (promise) ke anusar 14 varsh van mein rahunga. Phir laut kar aapki seva karunga.”

Raja Dasharath, satya ke bandhan mein baddhe hue, rote hue bole —
“Putra, main kuch nahi kar sakta. Tu ja, lekin shanti aur dhairya se ja. Tujhe kisi prakaar ka bhay na ho. Mujhe dukh hai, par tu satya ke path par chal raha hai.”

Phir vinati karte hue bole —
“Beta, aaj raat yahin ruk ja, kal subah ja. Tere jaane ka dukh main seh nahi sakta. Main Kaikeyi ke kapat jaal (trap) mein fas gaya hoon, par tu kyun dukh sahe?”

Rama ne shant aur dhairya bhari aawaz mein kaha —
“Pitashri, agar main aaj ruk gaya, to kal aur kathin hoga. Aap kripya rajya Bharat ko de dijiye. Mujhe vanvaas jaane dijiye, main aapka aadesh maanta hoon.
Mujhe na rajya chahiye, na sukh, na Janaki, na swarg (heaven), na jeevan — mujhe sirf satya aur aapke vachhan ka samman chahiye.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Unhone jhuke hue shabd mein kaha —
“Main jaanta hoon, pita hi devtaon ke devta hain. Aapka aadesh mera dharma hai. Main 14 varsh van mein phal-mool kha kar rahunga, par aapke satya ko toda nahi jaayega.”

Ye kehkar Rama ne apne pitaji ke charan chhuye. Raja Dasharath ne unhe gale lagaya aur phir se behosh ho gaye.

Poora mahal ro padta hai. Rani Kaushalya aur sab mahilayein vilap karti hain — sirf Kaikeyi chup baithi rehti hai.
Sumantra bhi apne aasu rok nahi paata.
Poora mahal “Rama! Rama!” ki karun dhvani (sorrowful cry) se goonj uthta hai.
        """
        create_image_text_layout("attached_assets/chapter2/2.34.2.jpg", text3, layout="side", image_position="right")

    # Chapter35
    with st.expander("Chapter 2.35 - Sumantra scolds Queen Kaikeyi for her actions"):

        text1 = """
Jab Sumantra hosh mein aaya, uska gussa aasmaan chhoo gaya. Uski saanse tez chalne lagi, daant kas liye, haath moadte hue, sir pe maarte hue — aankhein laal ho gayi aur chehra badal gaya. Uske andar dukh aur gussa dono ubhar aaye the. Jab usne dekha ki Rani Kaikeyi ne Raja Dasharatha ka pyaar kho diya hai, tab usne usse aise teekhe shabd kahe jaise teer dil ke paar chale jaate hain.

Sumantra bola, “Hey Rani Kaikeyi! Tumne apne pati ko chhod diya — jo sabka palanhar (protector and nourisher) tha. Tumne duniya mein aisa koi bure kaam nahi chhoda jo na kiya ho. Tum apne pati ki hatyara (murderess) aur apne vansh (family) ki naash karne wali ho. Tumhare bure kaamon se Raja Dasharatha — jo Indra jaise shaktishaali (powerful) aur pahaad jaise dridh (firm) the — tut gaye hain.”

        """
        create_image_text_layout("attached_assets/chapter2/2.35.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Phir usne kaha, “Kaikeyi, apne vriddh (aged) pati ka apmaan mat karo. Ek pativrata (devoted wife) ke liye apne pati ke prati bhakti (devotion) hazaar beto ke prem se zyada honi chahiye. Hamare vansh ki parampara (tradition) hai ki sabse bada beta rajya sambhale. Tum us parampara ko tod kar apne bete Bharata ko raja banana chahti ho, jabki Raja abhi zinda hain. Thik hai, tumhara beta rajya kare — hum sab Rama ke saath van (forest) chale jaayenge. Jo koi bhi achhe charitra wala hai, wo tumhare bete ke saath nahi rahega, kyunki tumne itihas ke niyam (ancient law) ko tod diya hai.”

Sumantra ne tikhhe shabdon mein kaha, “Mujhe hairani hai ki dharti (earth) tumhe nigal kyun nahi jaati tumhare paap (sins) ke liye. Tumhari buraiyon par to rishi (sages) bhi chup hain! Kaun bewakoof (fool) meetha aam ka ped kaatkar uske jagah kadva neem (bitter tree) lagata hai, chahe usse doodh se paani de? Neem se to kabhi bhi shahad (honey) nahi nikalta! Tum apni maa jaisi hi ho — buri aur dhokebaaz (deceitful).”

Phir Sumantra ne uske parivaar ka raaz khol diya: “Tumhare pita, Raja Kaikeya, ek yogi (sage) ke vardaan (boon) se sab praniyon (creatures) ki bhaasha samajh sakte the. Ek din, jab wo rajdhani laut rahe the, unhone do cheenti (ants) ko baat karte suna aur hans diye. Tumhari maa ko laga ki raja us par hans rahe hain, to usne jidd (stubbornly) ki — ‘Mujhe batao kyu hase!’ Raja ne kaha, agar main sach bataunga, to meri maut ho jayegi. Par tumhari maa boli — ‘Chahe tum mar jao, mujhe sach batao!’”

“Phir Raja Kaikeya yogi ke paas gaye. Yogi ne kaha, ‘Raja, ya to apni patni ko uske pita ke ghar bhej do ya use marne do, par sach mat batao.’ Aur raja ne apni patni ko tyag (abandon) diya aur aazad ho gaye jaise dhan ke devta Kubera. Hey Paapi (sinful) Kaikeyi, tum bhi apni maa ke raste par chal rahi ho, jhooth aur dhokhe ka raasta.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Sumantra ne aakhri baar kaha, “Suna hai — beta pita jaise aur beti maa jaise hoti hai. Par tum apni maa jaise mat bano, apne pati ki baat mano. Raja tumhara rakshak (protector) hai — uske shabd ka samman karo. Usse bura kaam mat karvao. Raja apne vaachan (promise) se peeche nahi hat sakta. Par tum Raja se vinti (request) karo ki Shri Rama ko hi rajya do — kyunki wo sabse bada, sabse dayalu (kind), dharm-nisth (righteous) aur sab praniyon ka rakshak hai. Agar Rama van chala gaya, to poori duniya tumhe doshi (blame) karegi. Apna man shaant karo, aur Rama ka rajyabhishek hone do. Agar koi aur raja bana, to tumhe sukh nahi milega. Agar Rama raja ban gaya, to Raja Dasharatha bhi parampara ke anusar van ko chale jayenge.”

Sumantra ne itne kathor (harsh) shabd sabke saamne Kaikeyi ko kahe, par Kaikeyi par koi asar nahi hua. Na uske chehre par pachtava (regret) tha, na uski aankhon mein aansu — wo patthar (stone) ki tarah shaant baithi rahi.
        """
        create_image_text_layout("attached_assets/chapter2/2.35.2.jpg", text3, layout="side", image_position="right")

    # Chapter36
    with st.expander("Chapter 2.36 - Kaikeyi does not listen to anyone"):

        text1 = """
Raja Dasharatha apne vaachan (promise) ke dukh mein doob gaye the. Aansu rokte hue unhone ro rahe Sumantra se kaha, “Hey Sumantra, chaar sena-vibhag (four divisions of army) taiyaar karo, jinmein dhan (wealth) ho — taaki wo Shri Rama ke saath ja sakein. Khoobsurat aur madhur bolne wali mahilayein (women), vaapari (merchants), aur dhanwan vyapari (rich traders) bhi saath chalein, jo Rama ke liye zaroori saamaan ka store banayen. Jo log Rama ke priya sevak (beloved attendants) hain, unhe bhi dhan de kar saath bhejo. Ayodhya ke achhe nagrik (citizens) bhi uske saath jaayein — hathiyaar, rath (chariots), aur jungle ke raste jaane wale logon ke saath.”

        """
        create_image_text_layout("attached_assets/chapter2/2.36.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Raja ne aage kaha, “Rama jungle mein hiran (deer) aur haathi ka shikar karega, nadiyon ke paas madhur shahad (honey) pi kar prakriti (nature) ka aanand lega, aur kabhi-kabhi hum sabko yaad karega. Mere sab dhan aur anna (grain) bhi uske saath bhej do, taaki wo van mein rahat se rahe. Wo rishi-muni (sages) ke saath yagya (sacrifices) karega, daan (alms) dega, aur wahan shanti se jeeyega. Yahan Bharata logon ka palan karega, aur Rama apna vanvaas (exile) sukh se bitayega.”

Kaikeyi ne jab ye suna, to uske chehre ka rang ud gaya. Uska gala sookh gaya, haath kaanpe lage. Ghabrahat se usne kaha, “Hey Maharaj, Bharata to aise rajya ko kabool (accept) nahi karega jo dhan, logon aur shaan (prosperity) se khaali ho — aise rajya ka kya fayda?”

Raja Dasharatha ka chehra laal ho gaya, aur unhone gusse mein kaha, “Hey papi (wicked) Kaikeyi! Tum itna dukh mujhe aur kyu dena chahti ho? Jab tumne Rama ko vanvaas bhejne ko kaha tha, tab to tumne nahi kaha tha ki wo bina kuch liye jaaye!”

Kaikeyi aur bhi krodhit (furious) ho gayi aur boli, “Tumhare vansh (dynasty) ke Raja Sagara ne bhi apne bete Asumanjas ko vanvaas bheja tha — Rama ko bhi waise hi bhejo!”

Ye sunkar Raja Dasharatha chillaye, “Haye Ram!” — aur poora mahal sharm aur dukh se bhar gaya. Par Kaikeyi bilkul shaant thi, jaise kuch mehsoos hi na ho.

Tab Raja ke pradhan mantri (chief minister) Siddhartha, jo satyavaan aur Raja ke bahut priya the, ne Kaikeyi se kaha, “Hey Rani, Asumanjas ne bachchon ko sadak se pakad kar Sarayu nadi (river) mein pheka tha — isliye wo paapi (evil) mana gaya. Nagar ke log usse ghin (disgust) karte the aur Raja Sagara se bole, ‘Humari raksha karo, ya Asumanjas ko rakho!’ Jab Raja ne poochha kyun, to logon ne kaha, ‘Asumanjas pagal ho gaya hai, bachchon ko paani mein dubota hai aur khushi manata hai!’

Tab Raja Sagara ne use vanvaas bhej diya — use kapde aur rath (chariot) dekar, patni ke saath jungle bhej diya. Asumanjas ne apne paapon ka phal (fruit) wahan bhugta. Par Rani Kaikeyi, Rama ne to koi paap nahi kiya! Usmein to chand (moon) jaisa bhi daag nahi! Agar tumhe Rama mein koi dosh (fault) dikhta hai, to sabke saamne batao — warna ye anyaay (injustice) hai.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Mantri ne aage kaha, “Hey sundar mukha wali Rani, bina wajah ek satya-path (path of truth) par chalne wale ko tyag dena adharma (unrighteous act) hai — aise kaam se to Indra ki tejas (splendor) bhi chali jaati hai. Tum Rama ki khushi ko naash mat karo aur logon ke liye apmaan (shame) ka kaaran mat bano.”

Siddhartha ke in satya bhare shabdon ke baad, Raja Dasharatha ne dukh se kaampte hue Kaikeyi se kaha, “Hey paapi Kaikeyi, kya tum mere mantri ki baat bhi nahi maanti? Kya tumhe apne aur mere bhale (welfare) ka kuch khayal nahi? Kya tum bas bure raaste (evil path) par hi chalna chahti ho? Theek hai, main apna dhan, sukh aur mahal sab chhodkar Rama ke peeche jaunga. Tum yahan Bharata ke saath aaram (comfort) se rajya karo — hamesha ke liye.”
        """
        create_image_text_layout("attached_assets/chapter2/2.36.2.jpg", text3, layout="side", image_position="right")

    # Chapter37
    with st.expander("Chapter 2.37 - Sita still wishes to go to the forest"):

        text1 = """
Jab Shri Rama ne apne pita aur mantri Siddhartha ke shabd sune, to ve vinamr (humble) hokar bole —
“Hey Maharaj, maine sab sukh aur aishwarya (luxury) tyag diya hai jungle mein rehne ke liye. Ab mujhe dhan, sena ya aur kisi cheez ki zarurat nahi. Jo haathi chhod chuka hai, use uske howdah ki rassi se kya matlab? Main aise hi hoon — mujhe jungle ke liye bas ek kassi (spade), ek tokri (basket), aur thoda khana chahiye. Mujhe turant yatra par nikalna hai.”

Ye sunkar Rani Kaikeyi uth khadi hui. Usne bark ke kapde (tree bark clothes) laakar sabke saamne bina sharmaye kaha —
“Rama, ye kapde pehno.”

        """
        create_image_text_layout("attached_assets/chapter2/2.37.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Shri Rama ne bina kuch kahe apne rajsi vastra (royal clothes) utaar diye aur bark ke vastra pehen liye.
Lakshmana ne bhi wahi kiya — apne sundar rajkapde utaar kar tapasvi (ascetic) jaise bark ke vastra pehene.

Jab Sita ji ne ye dekha, unhone apna sundar resham ka saari pehna hua tha. Jab unke saamne bark ke kapde laakar rakhe gaye, to wo ek pal ke liye ghabra gayi — jaise ek hiran (deer) shikari ka jaal dekh kar chauk jata hai.

Thodi sharm aur dukh ke saath, Sita ji ne wo kapde liye. Anjaani thi wo iss reeti (custom) se, isliye puchha —
“Prabhu, ye bark ke kapde kaise pehne jaate hain?”

Shri Rama ne unhe dekha aur khud unke kapde sahi karne lage — unke silken saari ke upar bark ke vastra bandh diye.
Ye dekh kar mahal ki sab mahilayen ro padi. Unhone kaha —
“Hey Rama, Rajarshi Dasharatha ne to Sita ji ko vanvaas (forest exile) ki anumati nahi di. Aap jaaiye, lekin Janaki ko yahin chhod jaiye. Hum unka mukh (face) dekhkar jeevan safal samjhenge. Lakshmana aapke saath jaaye, par Sita ji jungle ke kathin jeevan (harsh life) ke liye nahi bani.”

Par Shri Rama jaante the ki Sita bina unke nahi rukengi. Unhone unki baat nahi maani, aur Sita ji ko bark ke vastra pehnane mein madad ki.

Tab Rishi Vasishtha ji, jo Rajguru the, unhone krodh (anger) se Kaikeyi se kaha —
“Hey Kaikeyi, tu apne vansh (dynasty) ka vinash kar rahi hai! Tune Raja ko dhokha diya hai. Ye vanvaas ka vachan sirf Rama ke liye tha, Sita ke liye nahi. Sita to Rama ka ardhangini (half of the husband) hai — jahan Rama ka adhikar, wahan uska bhi. Agar Sita Rama ke saath jungle jaayegi, to hum sab — nagarik (citizens), sainik (soldiers), aur Bharat-Shatrughna bhi — sab uske peeche jaayenge. Tab Ayodhya jungle ban jaayegi aur jungle Ayodhya.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Vasishtha ji ne kaha —
“Bharat kabhi bhi ye rajgaddi (throne) nahi lega jab tak Rama jeevit hain. Tu apne putra ko rajgaddi dena chahti hai, lekin use to dukh hi milega. Kaikeyi, Sita ko ye bark ke kapde mat pehnne de, use rajsi vastra mein hi Rama ke saath bhej.”

Lekin sabke rokhne ke baad bhi, Shri Sita ne bark ke vastra pehne aur kaha —
“Main apne prabhu ke bina nahi reh sakti. Jahan ve jaayenge, main bhi wahan jaungi — chahe wo van hi kyu na ho.”

Aur is tarah, sabke mana karne ke baad bhi, Sita ji ne vanvaasi roop (ascetic form) mein Rama ke saath van yatra (forest journey) par jaane ka sankalp liya. 🌿
        """
        create_image_text_layout("attached_assets/chapter2/2.37.2.jpg", text3, layout="side", image_position="right")

    # Chapter38
    with st.expander("Chapter 2.38 - Rama asks the king to take care of his mother"):

        text1 = """
Jab logon ne dekha ki Sita ji, jinke pati jeevit hain, phir bhi ek vidhwa (widow) jaise bark ke kapde pehni khadi hain — to sab log Raja Dasharatha ko dosh dene lage.
Unke shabd sun kar Raja Dasharatha ka man dukhi (saddened) ho gaya — unka jeevan, dharm (virtue), aur yash (fame) sab jaise chhin gaya ho. Gehri saans lete hue, unhone Kaikeyi se kaha —

“Hey Kaikeyi, Sita ka jungle jaana aur ye tapasvi ke kapde pehna bilkul uchit (proper) nahi hai. Hamare Guru Vasishtha ji ne bilkul sahi kaha — Sita jaise komal (delicate) aur pavitra (pure) rajkumari van ke kathin jeevan ke layak nahi. Janaka ki beti ne kisi ka kya bigaada hai, jo aaj sabke saamne bark ke vastra pehne chup khadi hai, jaise koi sanyasini (female ascetic)? Mainne to kabhi ye vachan nahi diya tha ki Sita ko bhi ye vanvaas saha padega.”

        """
        create_image_text_layout("attached_assets/chapter2/2.38.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Raja ne kaampa hua swar (trembling voice) mein kaha —
“Sita ko rajsi vastra (royal clothes) aur alankaron (ornaments) ke saath, shubh roop mein van ko jaana chahiye, na ki is tarah ke kapdon mein. Hey Kaikeyi, meri mrityu (death) ab door nahi. Tumhare diye hue vachan mujhe andar se jala rahe hain — jaise baans (bamboo) apne phool se jal jaata hai. Agar tumhe lagta hai Rama ne tumse koi paap (wrong) kiya hai, to batao, Janaki ne kya kiya? Us masoom rajkumari ne, jiske netra (eyes) hiran jaise komal hain, tumhara kya bigaada?”

Phir Dasharatha ji ne krodh (anger) se kaha —
“Hey papi Kaikeyi! Tune bina wajah Rama ko vanvaas bhej diya, isliye tu nishchit (surely) narak (hell) ko prapt karegi. Jab Rama rajyabhishek ke liye tayyar tha, tab tune usse roka aur vanvaas ka hukum diya. Main chup raha, aur meri yahi chup mere liye vish (poison) ban gayi. Ab tu Sita ko bhi sanyasini jaise kapde pehna kar usse bhi dukh dena chahti hai? Ye paap tujhe narak ke aur ghehraai mein le jaayega.”

Itna keh kar Raja Dasharatha dukh aur laachari (helplessness) se behosh jaise ho gaye — zameen par gir pade.

Tab Shri Rama, jinka sir vinamrta se jhuka tha, aage badhe aur bole —
“Hey Pitashree, meri ek prarthana (request) hai. Jab main van jaunga, meri maa Kaushalya, jo hamesha vinamr (humble), dayalu (kind), aur sada satya bolne wali hai, mere bina atyadhik dukh (deep sorrow) mein doob jaayegi. Unhone kabhi dukh nahi dekha, aur ab meri judai (separation) unke liye asahniya (unbearable) hogi.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Aap, jo sabse poojya (honoured) hain, meri maa ka dhyaan rakhiye. Unhe apne sneha (affection) aur sahara (support) se sambhaliye, taaki wo dukh se toot na jaayein.

Hey Chakravarti Raja (great emperor), aap Indra ke samaan (equal to Indra) shaktishaali hain — kripya meri maa Kaushalya ki raksha kijiye, taaki meri anupasthiti (absence) mein unka jeevan shanti se beet sake.”

Aur is tarah Shri Rama ne, apne vanvaas par jaane se pehle, apni maa ke liye pitashree se karuna bhari vinanti (pleading request) ki. 🌿💛
        """
        create_image_text_layout("attached_assets/chapter2/2.38.2.jpg", text3, layout="side", image_position="right")

    # Chapter39
    with st.expander("Chapter 2.39 - Everyone in the palace cries loudly"):

        text1 = """
Jab Raja Dasharatha ne Shri Rama ke shabd sune aur unhe tapasvi (ascetic) ke roop mein dekha, to unka hosh udd gaya. Maharaniyan (queens) bhi dukh se munh pher kar ro padin. Raja Dasharatha itne vyakul (distressed) hue ki wo na Rama ko dekh sake, na kuch keh paaye — kuch der tak to wo behosh jaise pade rahe.

Thodi der baad jab unhe hosh aaya, to unhone dukh bhare swar mein kaha —
“Ab mujhe samajh aa gaya hai ki pichle janmon (previous births) mein maine bahut saare bachhon ko unki maa se alag kiya hoga, ya nirdosh jeevon (innocent beings) ka jeevan liya hoga — tabhi mujhe aaj yeh bhari dukh bhogna pad raha hai. Kaikeyi ke zulm (cruelty) se main jeete jee mar raha hoon, phir bhi mrityu (death) mujhe apne paas nahi bulati. Dekho, mera tejomay (radiant) beta Rama — jo aag ke saman chamak raha hai — rajsi vastra (royal clothes) chhod kar sanyasi ke kapde pehne khada hai. Kaikeyi ki chal (trick) aur apne swarth (selfishness) ke chakkar mein poora rajya dukh mein doob gaya hai.”

        """
        create_image_text_layout("attached_assets/chapter2/2.39.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Raja ke aankhon se aansu behne lage aur gala ruddh (choked) ho gaya — wo bas “Rama… Rama…” keh kar chup ho gaye. Thodi der baad unhone Sumantra se kaha —
“Hey Sumantra, turant sabse acchhe ghodon (best horses) ko jodo aur Rama ko rajdhani ke bahar le jao. Ab to mujhe spasht (clearly) samajh aaya hai — satpurush (virtuous man) hona bhi kabhi kabhi dukh ka kaaran ban jaata hai. Jo itna buddhimaan (wise) aur veer (brave) beta hai, use apne mata-pita hi vanvaas bhej rahe hain.”

Sumantra ne raja ke aadesh (order) ke anusar turant sona sajja hua rath (golden chariot) tayyar kiya aur Rama ke saamne aakar bola, “Prabhu, rath tayyar hai.”

Phir Raja Dasharatha ne apne vishwasniya (trustworthy) khajanchi (treasurer) ko bulaya aur kaha —
“Janaki ke liye chaudah varsh ke vanvaas (exile) ke liye sundar vastra (beautiful clothes) aur abhushan (ornaments) le aao.”
Aadesh paate hi khajanchi ne sab saman Sita ji ko laakar de diya.

Sita ji ne rajsi poshaak (royal dress) aur gehne pehne — aur jab wo tayyar hui, to poora mahal unki tej (radiance) se jagmaga utha, jaise suryoday (sunrise) se aakash roshan ho jaata hai.

Tab Rani Kaushalya ne Sita ji ko gale lagakar kaha —
“Hey priya putravati (beloved daughter-in-law), duniya mein bahut si patniyan (wives) hoti hain jo apne pati ke dukh mein saath nahi deti. Jab sukh hota hai tab sab saath rehti hain, par dukh aate hi mooh mod leti hain. Par tum unse alag ho. Tum jaise satya-vrata (truthful) aur pativrata (devoted wife) mahila bahut kam hoti hain. Isliye, mere bete Rama ke prati kabhi krodh (anger) mat rakhna. Use devata (deity) samajhna — chahe sukh ho ya dukh.”

Sita ji ne vinamrta (humility) se jhuk kar kaha —
“Hey Mata, aapka aadesh main hamesha maanungi. Mujhe bhi maloom hai ki patni ka kartavya (duty) hai apne pati ki seva karna. Mera janm bhi isi dharm (righteous duty) ko nibhaane ke liye hua hai. Main kabhi apne pati ka tyag (abandon) nahi karungi — jaise suraj apni roshni ko nahi chhodta. Jaise veena bina taar ke bekaar hai, aur rath bina pahiyon ke nahi chal sakta — waise hi patni apne pati ke bina adhoori hai, chahe uske sau (hundred) putra hi kyu na ho.”

“Pita, mata ya putra (father, mother or son) thoda sukh dete hain, par pati hi patni ke jeevan ka asli aanand (true joy) hota hai. Main janti hoon, pati patni ke liye bhagwan (god) samaan hota hai — main kabhi unka apmaan nahi karungi.”

Kaushalya ji ne aansuon ke saath Sita ko aashirvaad diya aur unke satya aur prem se bhare shabd sunkar thoda shaant ho gayin.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Phir Shri Rama apni maa se bole —
“Hey Mata, jab main van mein rahunga, tab Pitashree ko kabhi krodh bhari drishti (angry look) se mat dekhna. Yeh chaudah saal sapne (dream) jaise beet jaayenge. Phir aap mujhe apne pita ki seva karte hue dekhenge.”

Uske baad Rama ne raja ki doosri 350 patniyon (consorts) ki taraf dekha, jo sab ro rahi thi, aur kaha —
“Hey Matao, agar kabhi main bachpanne (in childishness) ya agyaan (ignorance) mein koi bhool ki ho, to mujhe kshama (forgive) kar dijiye.”

Unke yeh namr (humble) aur dharm se bhare shabd sunkar sab raaniyan aur mahilayen phoot-phoot kar ro padin — unka rodan (weeping) aise lag raha tha jaise krouncha pakshiyon (crane birds) ki dukhi pukar ho.

Jo mahal pehle nagade (drums) aur shankh (conch) ki goonj se bhara rehta tha, aaj wahi mahal raniyon ke shok (grief) bhare vilap (lament) se goonj utha. 💔🌙
        """
        create_image_text_layout("attached_assets/chapter2/2.39.2.jpg", text3, layout="side", image_position="right")

    # Chapter40
    with st.expander("Chapter 2.40 - All Ayodhya cries as Rama’s chariot leaves"):

        text1 = """
Jab Shri Rama ko vanvaas (exile) ke liye jana pada, unka dil dukh se bhar gaya. Unhone apne pita Maharaj Dasharatha ke charan (feet) chhue, phir Lakshmana aur Sita ke saath unke charo taraf parikrama (circumambulation) ki. Phir Rama ne apni maa Kaushalya ke charan chhuke aur unhe pranam kiya.

Lakshmana ne bhi apni maa Sumitra ke charan chhue. Maa Sumitra ro padi aur apne bete ko aashirvaad (blessing) dete hue boli,
“Mere beta, Shri Rama duniya ki raksha (protection) ke liye paida hue hain, aur tu unki seva (service) ke liye. Hamesha unke saath rehna, unka saath kabhi mat chhodna. Sukh ho ya dukh, Rama ko hi apna jeevan samajhna. Yehi hamare vansh (lineage) ki parampara (tradition) hai — bade buzurgon ka samman (respect), daan (charity), yagna (sacrifice), aur apni zimmedari nibhana.”

        """
        create_image_text_layout("attached_assets/chapter2/2.40.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Phir maa Sumitra ne kaha,
“Beta, jab tu Rama ke saath jungle jaaye, to unhe apne pita Dasharatha samajhna, Sita ko mujhe samajhna, aur us van ko (forest) Ayodhya ke barabar samajhna.”

Tab Sumantra, Raja ka saarathi (charioteer), namrata se bola,
“Hey Rajkumar, kripya rath par baithiye. Main aapko wahan le jaata hoon jahan aap chahein. Aaj se hi aapka vanvaas shuru hota hai.”

Janak Nandini (daughter of King Janaka) Sita, apne sundar gehno (jewels) se saja hua roop lekar, khushi se rath par chadh gayi. Rama aur Lakshmana bhi usme baith gaye. Rath sona (gold) aur shastron (weapons) se saja tha.

Raja Dasharatha ne Sita ko vanvaas ke liye kapde, gehne, aur raksha ke liye mantra-yukt astr-shastra diye the. Jab sab taiyar ho gaye, to Sumantra ne rath chala diya. Ghode hawa ki tarah tez bhaagne lage. Jaise hi Rama van ke liye nikle, poori Ayodhya — chhote, bade, auratein, jawaan — sab log udaas ho gaye. Sab unke peeche daudne lage, rone aur chillane lage.

Log Sumantra se pukarne lage,
“Hey saarathi, dheere chalao! Hume Rama ka chehra ek baar aur dekhne do!”
Kuch log bol rahe the,
“Kaushalya maa ka dil lohe ka hoga jo itna dard dekh kar bhi nahi toota! Aur dekho Sita ji, apne pati ke saath har sukh-dukh mein saaya (shadow) ban kar ja rahi hain. Lakshmana sach mein dhanya (blessed) hai, jo apne bhai ki seva ko apna dharm samajhta hai!”

Sab log rath ke peeche rote hue daud rahe the. Maharaj Dasharatha bhi bina jute ke, raniyon ke saath palace se nikal aaye, chillate hue —
“Mujhe apne bete ko ek baar phir dekhna hai!”

Rama ne peeche dekha, to apne maa-pita ko nange pair, rokar daudte hue dekha. Unka dil bhar aaya, par dharm (duty) ke bandhan mein bandhe hone ke karan unhone apni nazar hata li. Unhone Sumantra se kaha,
“Tez chalao!”
Aur rath aage badh gaya. Raja Dasharatha aur Rani Kaushalya roti reh gayi, jaise maa apne bachche ke pukarne par daudti hai.

Logon ke aansuon (tears) se rath ke pahiye (wheels) ke dhool dhul gayi. Poora Ayodhya shok (grief) mein doob gaya. Mahilayen aur praja (people) “Rama! Rama!” chillate hue rote rahe.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Rama ne Sumantra se kaha,
“Jab Raja poochein ki tune meri baat kyu nahi maani, to kehna — rath ke ghumo (wheels) ki aawaz ke beech main sun nahi paaya.”

Ant mein, Dasharatha thak kar ruk gaye. Unhone apne mann se Rama ki parikrama ki aur palace laut aaye. Unke mantri bole,
“Jo chaahta hai ki uska mitra (friend) wapas aaye, use zyada door tak nahi chhodta.”

Raja Dasharatha pasine se bheeg gaye, unka mann toota hua tha, aur wo Rama ke door jaate rath ko dekhte reh gaye.
        """
        create_image_text_layout("attached_assets/chapter2/2.40.2.jpg", text3, layout="side", image_position="right")

    # Chapter41
    with st.expander("Chapter 2.41 - The whole world feels sad for Rama"):

        text1 = """
Jab veer (brave) aur vinamra (humble) Shri Ramachandra Ayodhya se chale gaye, to mahal ke andar se ek dard bhari cheekh (cry of sorrow) sunai di. Sab raniyan aur mahal ki mahilayen rote hue boli,

“Hamare Rama kahan chale gaye? Wahi Rama jo anath (orphaned), kamzor (weak), aur dukhiyon ke sahare (support) the. Wahi Rama jo kabhi gussa nahi karte the, hamesha sabke dukh ko apna dukh samajhte the. Wo Rama kahan hain, jo sabse pyar se baat karte the, aur hamesha sabka man shant (peaceful) rakhte the? Kaikeyi ne unhe vanvaas (exile) bhej diya, aur Raja Dasharatha ne bhi unhe rok nahi paaye… Haye, Raja ka dil itna kathor (hard) kaise ho gaya?”

        """
        create_image_text_layout("attached_assets/chapter2/2.41.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Mahal ki sab auratein un gaayon (cows) ki tarah ro rahi thi, jinke bachche unse alag kar diye gaye ho. Unke rote hue swar (voices) sun kar Raja Dasharatha ka dukh aur badh gaya.

Ayodhya ka har kona udaasi (sadness) se bhar gaya tha.
Na kisi brahmachari ne agni-puja (fire ceremony) ki,
na kisi grihasth (householder) ne bhojan (food) banaya.
Sab log bas dukh mein doob gaye.

Haathi ne apne shringar (decorations) utaar diye,
gaaye apne bachchon ko doodh pilaane se inkaar kar rahi thi,
aur maaon ko apne bachchon ko dekh kar bhi khushi nahi ho rahi thi.

Asmaan (sky) bhi jaise dukh mein doob gaya tha.
Chand ke paas manhoos (inauspicious) grah — Mangal (Mars), Shani (Saturn), Brihaspati (Jupiter) aur Shukra (Venus) — ikattha ho gaye the. Taare (stars) apni chamak kho baithe, Vishakha nakshatra (constellation) bhi dhundhla (dim) pad gaya.

Achanak tez hawa chali, badal (clouds) ek doosre se takraane lage, aur zameen kampne (earthquake) lagi. Aas-paas andhera chha gaya, suraj (sun) ki roshni kam ho gayi, aur sab dishaayein udaas ho gayin.

Ayodhya ke log bhooke-pyaase, bechain (restless) aur dukhi the. Kisi ne us din bhojan nahi kiya, na kisi ke ghar se hansne ki awaaz aayi. Sadkon (streets) par log rote hue chal rahe the — na hawa thandi chal rahi thi, na chandni (moonlight) chamak rahi thi.

Sab log bas ek hi baat keh rahe the —
“Hamare Rama chale gaye…”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Putra apne pita ka dhyaan nahi rakh rahe the,
pati apni patni se door jaise lag rahe the,
aur bhaiyon ke beech ka pyaar bhi kho gaya tha.

Rama ke mitra (friends) bina neend ke, bas unki yaad mein rote rahe.
Ayodhya bina Rama ke aise lag rahi thi jaise dharti (earth) bina paani ke — sookhi aur dukhi.

Har ghar se rote hue logon ki awaaz aa rahi thi,
aur haathi, ghodon (horses) aur sainikon (soldiers) ke cheekhne ki dhwani (sound) poore nagar (city) mein goonj rahi thi.
        """
        create_image_text_layout("attached_assets/chapter2/2.41.2.jpg", text3, layout="side", image_position="right")

    # Chapter42
    with st.expander("Chapter 2.42 - The king can’t sleep without Rama"):

        text1 = """
Jab tak Rama ke rath (chariot) ke pahiyon (wheels) se uthi dhool (dust) nazar aati rahi, tab tak Raja Dasharatha apni nazar us raaste se hata nahi paaye. Jab tak unhe apne pyare aur dharmparayan (virtuous) putra Shri Ramachandra ka darshan (sight) hota raha, tab tak wo bas usi disha (direction) mein dekhte rahe. Lekin jaise hi wo dhool hawa mein gayab ho gayi, Raja Dasharatha ka dil tut gaya — wo zameen par gir pade, behosh (unconscious) ho gaye.

        """
        create_image_text_layout("attached_assets/chapter2/2.42.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Rani Kaushalya ne turant unka daahina haath pakda aur Rani Kaikeyi ne baaya haath sambhala. Hosh mein aate hi Raja Dasharatha ne Kaikeyi ki taraf dekha aur dard bhare swar mein bole,
“Hey paapi (wicked) Rani, mujhe haath mat lagao! Main tumhe apni patni nahi maanta. Na main tumse koi rishta rakhna chahta hoon. Tumhare naukar ab mere nahi, aur main unka swami (master) nahi. Tumne apne pati (husband) ke prati apna kartavya (duty) chhod diya hai. Jo haath maine vivaah (marriage) ke samay agni ke saamne pakda tha, aaj usse main tyagta (renounce) hoon. Agar tumhara beta Bharat rajgaddi se santusht ho, to yaad rakhna — usse mere antim sanskaar (funeral rites) karne ki bhi zarurat nahi.”

Rani Kaushalya ne roti hui Raja Dasharatha ko uthaya, unke kapde dhool se bhare hue the. Unhe rath mein bitha kar mahal ki taraf le gayi. Dasharatha ka dukh aisa tha jaise kisi ne apne jeevan se adhik pyare vyakti ko khoya ho. Har kadam par wo peeche mud kar Rama ke jaane wale raaste ko dekhte rahe. Unka chehra suraj ke grahan (eclipse) ke samay jaisa feeka (pale) lag raha tha.

Wo rote hue bole,
“Main to ab sirf un ghodon (horses) ke nishaan dekh sakta hoon, jinse mere Rama ka rath joda gaya tha… lekin mere Rama nahi dikh rahe. Haye mera beta! Jo pehle chandan (sandalwood) se sugandhit hokar komal takiye (soft pillows) par sota tha, aaj zameen par ped ke neeche pathar (stone) ka takiya bana kar so raha hoga. Subah jab wo uthta hoga, uska tan (body) mitti se lipta (covered) hoga, aur wo gehri saans (deep sighs) leta hoga jaise koi dukhi bail (bull). Jungle ke log ab usse ek anath (orphan) jaise bhatakta dekhenge.”

Raja ka dard aur badh gaya jab unhone Sita ke baare mein socha:
“Janak ki beti Sita, jo hamesha khushiyon ki haqdaar (deserving) thi, ab kaanton (thorns) se bhare raaste par chal rahi hogi, jangli janwaron (wild animals) ki dahad (roar) sunkar daregi. Hey Kaikeyi, tumhara manokamna (ambition) poora ho gaya — ab raj sambhalo, lekin yaad rakhna, main bina Rama ke jee nahi sakta.”

Aise rote hue Raja Dasharatha Ayodhya wapas aaye, jaise koi apne sabse pyare vyakti ka antimsanskar karke laut raha ho. Nagar (city) viran (empty) lag raha tha — bazaar band the, mandir (temples) sune (silent) the, aur sadkon par sirf budhe aur roti awaz waale log the. Unhone jab ye sab dekha to aur bhi ro pade. Mahal mein ghuste hue wo aise lag rahe the jaise suraj badal (cloud) ke andar chhup gaya ho.

Ab unhone kamzor (weak) aur kanpte (trembling) swar mein kaha,
“Mujhe turant Rani Kaushalya ke mahal le chalo. Sirf wahi jagah hai jahan mujhe thoda sukoon (peace) mil sakta hai.”

Sevakon (attendants) ne Raja ko Kaushalya ke mahal le jaakar palang (couch) par bithaya, lekin unka mann fir bhi ashant (restless) raha. Mahal Rama, Lakshmana aur Sita ke bina unhe aise lag raha tha jaise aakash (sky) bina chand (moon) ke.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Raja ne apne haath upar uthaye aur pukara,
“Hey mere beta Rama! Kya tum mujhe chhod kar ja rahe ho? Kitne bhagyashali (fortunate) honge wo log jo tumhe wapas laut kar gale lagayenge!”

Raat gehri aur andheri thi, jaise maut (death) ka sama ho. Raja ne madhyaraatri (midnight) mein Kaushalya se kaha,
“Hey Kaushalya, mujhe tum dikh nahi rahi… meri drishti (sight) to Rama ke saath chali gayi hai. Kripya apna haath mere haath par rakho, taaki mujhe tumhara sparsh (touch) mehsoos ho.”

Kaushalya ne apne patidev (husband) ki haalat dekhi, wo bhi rote hue unke paas baith gayi. Dono bas ek hi naam le rahe the —
“Rama…”
        """
        create_image_text_layout("attached_assets/chapter2/2.42.2.jpg", text3, layout="side", image_position="right")

    # Chapter43
    with st.expander("Chapter 2.43 - Queen Kaushalya cries in sorrow"):

        text1 = """
Jab Raja Dasharath apne shok (grief) mein doobe hue bistar par pade the, tab Rani Kaushalya, apne putra Shri Ram ke virah (separation) se dukhi hokar boli —

“Hey Maharaj, us dusht (evil) Kaikeyi ne jaise zeher (poison) ugal diya ho, waise hi usne humare ghar ki shanti mita di. Ab wo bina kisi sharam ke, ek saamp (snake) ki tarah apna purana chilka (slough) utaar kar, azaadi se ghoom rahi hai. Usne apne man ka vish (venom) nikal kar, hamare Ram ko vanvas (exile) bhej diya. Mujhe wo hamesha ek zahreeli naagin ki tarah bhay (fear) degi.

        """
        create_image_text_layout("attached_assets/chapter2/2.43.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Kaash usne yeh kaha hota ki Ram yahin nagar mein bhiksha (alms) maang kar rahe, ya phir uska daas (servant) ban jaaye — yeh vanvas se to behtar hota! Par usne to Ram ko is prakar nikal diya jaise yagna (sacrifice) ke dauran asuron (demons) ke liye diya gaya bali (offering) door phenka jaata hai.

Mera lamba, dhanush-dhari (bow-wielder) beta Ram, jo hamesha ek gajraj (elephant king) ki tarah chalne wala hai, ab tak Sita aur Lakshman ke saath van mein pahunch gaya hoga. Hey Raja, sochiye — aapka wahi beta, jise kabhi dukh ka sparsh (touch) bhi nahi hua, aapke hi kehne par Kaikeyi ke prerna (instigation) se vanvas gaya hai.

Bataiye, bina dhan (wealth) ke, jawani mein, jab raj-sukh (royal comfort) milna chahiye tha, tab Ram kaise van mein mool (roots) aur phal (fruits) khaa kar jeevan bitayega? Kya kabhi wo din aayega jab main Ram, Lakshman aur Sita ko phir se dekh paungi — mere is virah ka ant (end) hoga?

Kya kabhi Ayodhya phir se us din ko dekhegi, jab gali-gali jhanda (flag) aur pushp (flowers) se saja hoga, jab nagar-vaasi (citizens) khushi se jhoomenge Ram ke swagat mein? Jab log chaand ke purnima jaise khil uthenge Ram ke lautne ki khabar sunkar?

Kab wo shubh ghadi aayegi jab Shri Ram, apni Sita ke saath, nagar mein pravesh (enter) karenge, bilkul us bail (bull) ki tarah jo sham ke samay apni gaiyon (cows) ke jhund ke aage aage chalta hai? Kab nagar ke log, apne haathon mein chawal lekar, Ram par barasayenge aur sadkon par bheed (crowd) lagayenge?

Mere dono putra — Ram aur Lakshman — dono pahaadon ki shikhar (peaks) ki tarah tejomay (radiant) hain. Kya main unhe phir se Ayodhya aate dekh paungi, kaan mein kundal (earrings) pehne, haath mein talwar aur dhanush liye hue? Kab wo Janaki ke saath nagar ka parikrama (circumambulation) karenge, aur log unhe phal-phool arpan (offer) karenge?
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Mera Ram, gunon ka sagar (ocean of virtues), sab shastra (scriptures) mein nipun (learned) hai. Uske bina main kaise jeeyu? Mera hriday (heart) uske virah ke agni (fire) se jal raha hai, jaise garmi ke dhoop (summer sun) mein dharti jalti hai. Kaikeyi ke karan meri mamta (motherly love) aur badh gayi hai — main us gau (cow) ki tarah ho gayi hoon jiska bachha sher (lion) le gaya ho.”

Kaushalya ke shabdon mein maa ka dard tha — ek aisi maa jiska putra dharm ke liye sab kuch chhod gaya, aur jo apne sansaar ko uske bina suna (empty) mehsoos karti hai. 💔
        """
        create_image_text_layout("attached_assets/chapter2/2.43.2.jpg", text3, layout="side", image_position="right")

    # Chapter44
    with st.expander("Chapter 2.44 - Queen Sumitra consoles Kaushalya"):

        text1 = """
Jab Rani Kaushalya apne putra Ram ke virah (separation) mein ro rahi thi, tab Rani Sumitra — jo hamesha dharm aur shanti ki moorat (embodiment) thi — unke paas aayi aur bahut samajhdari (wisdom) se boli:

“Hey Devi Kaushalya, aap itna vilap (lament) kyun kar rahi hain? Aapka beta Shri Ram sabse uttam purush (chief of men) hai, gunon (virtues) ka khazana hai. Wo to van mein gaya hai apne pita Maharaj Dasharath ka naam roshan (illustrious) karne — satya (truth) aur dharm ke path (path) par chalne ke liye.

Ram ne apne pita ka aadesh (command) maan kar, sabse bada kartavya (duty) nibhaya hai. Aapko shok (grief) nahi, garv (pride) karna chahiye. Lakshman ke liye bhi chinta na karein — wo pavitra (pure), dayaalu (compassionate) aur sada apne bhai ke seva mein laga hua hai. Aur Sita — wo to swyam Lakshmi ka roop (form) hai — apne pati ke saath van gayi hai, to Ram ke paas sada sukh-shanti rahegi.
        """
        create_image_text_layout("attached_assets/chapter2/2.44.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Rani, Ram ke van jaane se dukh nahi hona chahiye — wo to sab praniyon (beings) ke rakshak (protector) aur dharm ke palak (upholder) hain. Unka tejas (glory) teenon lokon (three worlds) mein phail gaya hai. Sochiye, Ram itne pavitra (pure) hain ki suraj (sun) bhi unhe jala nahi sakta, aur van ke garam vaayu (hot winds) bhi unhe thandak (coolness) denge, jaise basant (spring) ki hawa.

Jab Ram van mein soenge, to chaand (moon) pita ki tarah apni sheetal kirnon (cool rays) se unka aashray (comfort) karega. Wo hi Ram jinko Vishwamitra ne divya astr-shastra (celestial weapons) diye the — veer (valiant) aur shatrunashak (foe-destroyer) — van mein bhi waise hi nischint (fearless) rahenge jaise apne mahal mein.

Dharti maa (Mother Earth) khud unka sahara (support) degi, aur Ram, apni shakti (strength) aur sahas (courage) se, apna rajya (kingdom) zaroor wapas paayenge. Ram wahi hain jo surya ko tej (light) dete hain, agni ko prakash (splendour) dete hain, aur sab rajao ke raja (supreme ruler of rulers) hain. Jahan Ram hain — chahe van ho ya nagar — wahi unka rajya hai.

Aapka beta Ram, Sita aur Lakshman ke saath, jaldi hi apna vanvas pura karke Ayodhya lautega. Aur tab aap apne putra ko dekhengi — wo aapke charanon (feet) mein sir rakhkar pranam karega, aur aapki aankhon se khushi ke aansu (tears of joy) behenge. Tab aapka Ram, singhasan (throne) par virajmaan (seated) hoga, aur Ayodhya punah sukh aur sampannata (prosperity) se bhar jayegi.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Hey Devi, aap dhairya (patience) rakhiye — main kehti hoon, koi bhi durbhaagya (inauspicious sign) Ram ke liye nahi hai. Jaldi hi aap Ram ko Sita aur Lakshman ke saath dekhengi, jaise sawan (rainy season) ke baadal apni barkha (rain) lekar lautte hain. Us samay aapki aankhen us par barish ke baadalon ki tarah aansuon se bhar jayengi, aur aap apne putra ko apne aanchal (motherly embrace) mein samet lengi.”

Sumitra ke in madhur (sweet) aur shantikar (soothing) shabdon ne Kaushalya ke hriday ko shaant kar diya. Unka dukh jaise sharad ritu ke baadal (autumn clouds) ki tarah dheere-dheere vilin (disappeared) ho gaya.
        """
        create_image_text_layout("attached_assets/chapter2/2.44.2.jpg", text3, layout="side", image_position="right")

    # Chapter45
    with st.expander("Chapter 2.45 - The sages and people cry for Rama"):

        text1 = """
Jab Shri Ram van ki or ja rahe the, tab Ayodhya ke log — jo unse gehri bhakti (deep devotion) rakhte the — unke rath ke peeche-peeche daudte ja rahe the. Maharaj Dasharath to mantriyon (ministers) ke kehne par wapas mahal laut aaye, par nagar ke log apne Ram ko chhod nahi pa rahe the. Unke aansu ruk nahi rahe the — sab kehte the, “Rama, hamare rakshak (protector), hamare dayaalu rajkumar, laut aaiye!”

Par Shri Ram ne apne pita ke vachan (promise) ko satya (true) rakhne ka sankalp liya tha. Wo van ke disha (direction) mein aage badhte rahe, aur piche se rote hue nagarvasi (citizens) unhe dekhe ja rahe the jaise koi pyasa vyakti paani ko dekhta hai. Ram ne un sab ko pyaar se sambodhit (address) karte hue kaha:

        """
        create_image_text_layout("attached_assets/chapter2/2.45.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“Hey Ayodhya ke prajano (people), main tumse ek vinti (request) karta hoon — jaisa sneha (affection) aur samman (honour) tum mujhe dete ho, usse bhi adhik (even more) Bharata ko dena. Wo tumhare liye dayaalu (kind), vinamra (gentle) aur bahadur (brave) hoga. Jab main van mein rahunga, tab tum sab uski seva (serve) aur aadesh (obey) karo, jaise tum meri karte ho. Isse mujhe khushi milegi.”

Par Ram jitna logon ko raja Bharata ko apnane ko kehte, utna hi unka man (heart) Ram ko apna raja dekhne ko tadapta (yearn) jaata tha. Ayodhya ke log jaise kisi prem ke bandhan (bond of love) se bandh gaye ho, waise Ram aur Lakshman ke peeche chalne lage.

Budh (elderly) brahman, jinke sir safed (white) aur haath kaap rahe the, door se pukarne lage:
“Hey tez ghodon (swift horses), ruk jao, wapas mud jao! Hamare Ram ko van mat le jao. Tum sab sun sakte ho, humari vinati (plea) suno. Hamare swami (master) ka hriday (heart) komal (gentle) hai, unhe mat le jao.”

Ram ne jab un vridh (aged) brahmanon ke dukh bhare shabd sune, to unka hriday karuna (compassion) se bhar gaya. Unhone Sumantra se kaha rath roko, aur Ram, Lakshman aur Sita sab rath se utar kar pairon se van ki or chalne lage. Brahman log unke peeche chal rahe the, kuch bohot piche reh ja rahe the, par ruk nahi rahe the.

Brahman rote hue bole:
“Hey Ram, aap to hum brahmanon ke mitra (friend) ho! Dekho, hum sab apni aarti ke pavitra agni (sacred fire) kandhon par le ja rahe hain. Ye chhatra (canopies) humne yajna (sacrifice) ke dauran prapt kiye the — ab inke chhaye (shade) se hum aapko suraj ki garmi (heat) se bachayenge. Aap pehle Veda (sacred knowledge) ke adhyayan (study) mein lage rehte the, aur ab vanvas ke liye chal pade ho! Agar aap hi dharm se mukh (turn away) ho jaoge, to aur kaun uska paalan karega?”

Unhone jhuk kar Ram ko pranam (salutation) kiya, aur bola:
“Hamare kuch yajna (sacrifices) aapke ashish (blessing) se hi poore honge. Sirf hum nahi, ped-paudhe (trees), pakshi (birds), aur sab prani (creatures) aapko lautne ke liye vinati kar rahe hain. Dekhiye, ped ke jad (roots) unhe rok rahe hain, par unki shaakhaayein (branches) aapki or jhuk kar prarthana kar rahi hain. Pakshi bhi apna bhojan (food) chhod kar aapko dekh rahe hain — unki aankhen bhi prarthana kar rahi hain: ‘Hey Ram, mat jao!’”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Aise hi vilap karte hue sab log nadi Tamasa ke kinare pahunche. Nadi jaise khud Ram ke raaste ko rokh rahi ho, jaise keh rahi ho — “Ruko Ram, mat jao.”

Tab Sumantra ne thake hue ghodon ko khula chhod diya — unhone mitti par lot kar thakan door ki, aur phir Tamasa ke thande paani mein nahakar apna sharir thoda sukhaya. 
Ayodhya ke log, brahman aur prani sabhi — sab ka dukh ek hi tha: “Ram se bichhadna.”
        """
        create_image_text_layout("attached_assets/chapter2/2.45.2.jpg", text3, layout="side", image_position="right")

    # Chapter46
    with st.expander("Chapter 2.46 - Rama rides toward the forest"):

        text1 = """
Jab Shri Rama, Sita aur Lakshmana nadi Tamasa ke sundar kinare (riverbank) par pahunche, to Rama ne Sita ko dekha aur pyar se Lakshmana se bole —
“Hey Lakshmana, yeh hamare vanvaas (exile) ki pehli raat hai. Fikr ki koi baat nahi. Jungle shaant aur udaas lag raha hai, sab pashu (animals) aur pakshi (birds) so gaye hain. Shayad Ayodhya ke log aur hamare pita Maharaj Dasharatha hamare jaane se dukhi honge. Pita ji hamesha hamse bahut prem karte the.”

Phir Rama ne gaharai se kaha —
“Mujhe dar hai, kahin pita ji aur maa ke aankhon se aansu ruk na jayein. Par mujhe bharosa hai ki Bharata, jo sada dharmik (righteous) aur dayalu hai, unhe sambhal lega. Lakshmana, tumhare saath hone se mujhe sukoon hai. Agar tum nahi hote, to mujhe Sita ki suraksha (safety) ki chinta rehti.”

        """
        create_image_text_layout("attached_assets/chapter2/2.46.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Rama ne aage kaha —
“Yahan jungle mein phal, mool (roots) aur ber (berries) mil jayenge, lekin aaj raat main sirf paani hi piyunga.”

Phir Rama ne Sumantra se kaha —
“Hey mitra (friend), ghodon ka dhyan se khayal rakhna.”
Surya ast (sunset) hone ke baad, Sumantra ne ghodon ko ped se baandha aur unke saamne narm ghaas rakhi. Phir Lakshmana ke saath milkar Rama ke liye patton ka ek komal (soft) bichhauna (bed) banaya. Rama, Sita aur Lakshmana wahan Tamasa ke kinare aram se so gaye.

Jab sab so rahe the, Lakshmana ne apni jagah chhod kar Sumantra se Rama ke gunon (virtues) ke baare mein baatein ki. Dono puri raat Rama ke charitra (qualities) par charcha karte rahe.

Subah hone par, Rama ne dekha ki Ayodhya ke log jo unke saath aaye the, pedon ke neeche so rahe hain. Rama bole —
“Dekho Lakshmana, ye log apna ghar aur sukh chhod kar hume lautane aaye hain. Shayad ye mar jaana pasand karenge, par apni pratigya (vow) nahi todenge. Isliye hum unke jaagne se pehle nikalte hain. Agar hum chupke se chale gaye, to unhe takleef nahi hogi.”

Lakshmana ne turant kaha —
“Hey Prabhu, aapka vichar (decision) bilkul sahi hai. Aaiye, abhi rath (chariot) par chadhte hain.”

Rama ne Sumantra se kaha —
“Jaldi rath taiyaar karo, hume van (forest) ki aur badhna hai.”

Sumantra ne ghodon ko baandha aur bola —
“Prabhu, rath taiyaar hai. Kripya Sita ji aur Lakshmana ke saath chadh jaiye. Aapka yatra mangalmay (auspicious) ho.”

Rama ne apna dhanush (bow), tarkash (quiver) aur shastra (weapons) liye aur rath par chadh gaye. Unhone Tamasa nadi ko paar kiya aur kathin, kaanton (thorns) se bhari raah se guzarte hue ek seedha aur surakshit raasta pakad liya.

Logon ko gumrah (mislead) karne ke liye Rama ne kaha —
“Sumantra, pehle rath ko dakshin (south) disha mein chalao, phir wapas mud kar aana, taaki humare nishaan (tracks) koi na pehchan sake.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Sumantra ne aadesh (order) ke anusaar pehle dakshin ki aur chalaya, phir wapas mudkar bola —
“Prabhu, ab kis disha mein chalein?”

Rama bole —
“Ab Tapovana ki aur badho.”

Aur is tarah Shri Rama, Sita aur Lakshmana apni van yatra (forest journey) par nikal pade — shaant, majboot aur dhairya (patience) se bhare hue. 🌿
        """
        create_image_text_layout("attached_assets/chapter2/2.46.2.jpg", text3, layout="side", image_position="right")

    # Chapter47
    with st.expander("Chapter 2.47 - The people following him stop and cry"):

        text1 = """
Subah hone par jab suraj ug gaya, to Ayodhya ke nagrik (citizens) jaage — par jab unhone dekha ki Shri Rama wahan nahi hain, to sab ke dil bhar aaye. Unhe samajh hi nahi aaya kya karein. Aansu se bhari aankhon se unhone har jagah talaash (search) ki, par koi nahi jaanta tha ki Rama kis raaste (path) se gaye hain.

Dukh se peele pad gaye log rote hue bole —
“Shraap (curse) hai us neend ko, jisne hume andha bana diya! Agar hum jaagte rehte, to aaj Rama ko jaane nahi dete. Ab hum unka sundar, komal (gentle) aur bade aankhon wala chehra kabhi nahi dekh paayenge.”
        """
        create_image_text_layout("attached_assets/chapter2/2.47.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Ek ne kaha —
“Hamari bhakti (devotion) bekaar gayi! Rama ne hume apne mitra (friends) samjha tha, phir bhi hume chhod kar van (forest) chale gaye. Hum ya to yahin mar jayenge, ya Himalaya ki barf mein jaakar apna ant (end) kar lenge. Rama ke bina jeena bekaar hai.”

Dusra bola —
“Chalo, lakdi jama karte hain, aur aag jala kar apni zindagi khatam kar dete hain. Hum kaise palat kar sabko batayenge ki humne Rama jaise satyavaadi (truthful) aur dayalu (kind) rajkumar ko akela chhod diya?”

Sab rote hue bole —
“Jab hum Ayodhya lautenge bina Rama ke, to sheher ke log, mahilayein (women), bachche aur bude sab dukh se bhar jayenge. Humne apna ghar chhod kar Rama ka saath dene ki kasam (vow) khayi thi, ab unke bina wapas jaane ka mooh kaise dikhayein?”

Aise rote aur haath utha kar vilap (cry) karte hue log, usi tarah lag rahe the jaise bachchon se vichhadi hui gaayen (cows separated from calves).

Unhone rath ke pahiyon (chariot wheels) ke nishaan (marks) pe chalne ki koshish ki, par jab wo nishaan gum ho gaye, to sab zameen par gir kar rote hue bole —
“Haaye! Hum kya karein? Kismat (fate) humare khilaaf hai!”
Aur phir sab nirash (hopeless) hokar Ayodhya wapas laut gaye.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Jab Rama nahi lautey, to Ayodhya ke logon ke mann bechain (restless) ho gaye. Jab unhone dekha ki nagri (city) suni-suni aur udaas lag rahi hai, to sab ne milkar kaha —
“Rama ke bina Ayodhya apni chamak (glory) kho baithi hai. Ye sheher us sukhad nadi jaise lagta hai jisme paani sookh gaya ho. Jaise asmaan bina chaand ke, ya samundar bina paani ke, waise hi Ayodhya ab feeki (lifeless) lagti hai.”

Log apne bade-bade mahalon (palaces) mein gaye, par itne dukh se bhare hue the ki apne parivaar (family) aur paraye (strangers) mein bhi farq nahi kar pa rahe the. 💔
        """
        create_image_text_layout("attached_assets/chapter2/2.47.2.jpg", text3, layout="side", image_position="right")

    # Chapter48
    with st.expander("Chapter 2.48 - Ayodhya looks empty without Rama"):

        text1 = """
Ayodhya ke log ab itne dukh se bhar gaye the ki unki aankhen aansuon (tears) se beh rahi thi. Har kisi ka mann bas ek hi baat soch raha tha — kaash hum apni jaan de dein. Jo log Rama ke saath van (forest) tak gaye the, ab laut kar bilkul udaas aur bejaan (lifeless) lag rahe the.

Ghar wapas aakar, patniyon (wives) aur bachchon ke saath sab rote rahe. Koi khush nahi tha. Koi apne bachchon ko sajaata (decorate) nahi tha, aur mahilayein (women) bhi apne gehne nahi pehenti thi. Kisi ghar ki chulha (hearth) nahi jal rahi thi. Agar kisi ko khoi hui daulat (wealth) mil bhi gayi, to bhi usme khushi nahi thi. Pehli baar ghar aaya beta bhi maa ke liye sukh ka karan nahi tha. Har ghar se sirf rote hue logon ki awaaz aa rahi thi.
        """
        create_image_text_layout("attached_assets/chapter2/2.48.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Jab pati Rama ke bina lautey, to patniyon ne unhe kathin (bitter) shabdon se dant diya — jaise haathi ko uska mahavat (driver) angochhe se maar kar chalata hai. Har taraf log kehte sunai diye —
“Rama ke bina humare ghar, dhan (wealth), bachche, sab bekaar hain. Sirf Lakshmana hi sach mein dharmic (virtuous) hai — jo Rama aur Sita ke saath van gaya.”

Ek ne kaha —
“Kitne bhagyashali (fortunate) hain wo jheel (lake) aur nadiyan (rivers), jinme Rama nahate hain — kyunki unse to pavitrata (purity) badh jaati hai! Aur wo jungle, pahaad (mountains), aur nadi ke kinare — Rama ki upasthiti (presence) se aur bhi sundar lagte honge.”

Dusra bola —
“Ped bhi apne phool aur kaliyan (buds) Rama ko arpan (offer) kar rahe honge. Pahaad apni dhara (stream) Rama ke liye behate honge. Jahaan Rama hote hain, wahan koi bhay (fear) ya dukh nahi hota. Chalo, hum bhi unke peeche chalein — unke charan (holy feet) ki seva (service) se bada sukh aur kahin nahi.”

Ayodhya ki mahilayein, dukh se bhari hui, apne patiyon se boli —
“Chalo hum bhi Rama ke peeche chalte hain. Hum Sita ji ki seva karenge, aur tum log Rama ji ke sevak ban jao. Jahan wo honge, wahan hume bhi sukh (peace) milega. Agar Kaikeyi ne rajya (kingdom) apne haath mein le liya, to humare jeevan ka kya arth (meaning) bacha? Wo na Raja Dasharatha ke prati wafadar (loyal) rahi, na apne bete Rama ke — to humare prati kya dayaa (compassion) rakhegi?”

Sab boli —
“Hum apne bachchon ki kasam (oath) kha kar kehte hain — jab tak zinda hain, hum Kaikeyi ki daasi (servant) nahi banenge! Usne to Rama jaise pavitra (pure) aur dayalu rajkumar ko van mein bhej diya. Uske raaj mein Ayodhya tabah (ruined) ho jaayegi.”

Kisi ne kaha —
“Ab Raja Dasharatha bhi Rama ke bina zyada din nahi jeeyenge. Aur jab wo chale gaye, to poora rajya (kingdom) bikhar jaayega. Hamara punya (good karma) khatam ho gaya hai — isliye hum sab dukh mein hain. Chalo, ya to zeher (poison) kha lein, ya Rama ke saath chalein, ya phir kisi anjaan jagah jaakar chup chaap jeeyein.”

Sab milkar rote hue kehte rahe —
“Rama, jo poornima ke chaand (full moon) jaise prakashmaan (radiant) hain, jinke aankhen kamal (lotus) jaise hain, aur jinka swabhav itna dayalu aur satyavaadi (truthful) hai — wo jahaan bhi ja rahe hain, us van ko sundar bana rahe hain.”

Rama se vichhad kar Ayodhya ki mahilayein aise ro rahi thi jaise kisi apne priya (beloved) ke marne par dost rote hain. Raat gir gayi — na kahin yagya (sacrifice) ka dhuaan utha, na kisi brahmin ne Veda ya Puran ka paath (recitation) kiya. Kisi ghar mein diye (lamps) nahi jale.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Ayodhya ab bilkul suni lag rahi thi — jaise taaron (stars) ke bina akash, ya paani ke bina samundar. Dukhi aur vyakul (distressed) mahilayein Rama ke liye rote hue boli —
“Rama humare liye apne bachchon se bhi zyada pyare the.”

Sheher mein na geet (songs) the, na sangeet (music), na nritya (dance). Vyapaari (merchants) bhi apna maal (goods) chhod kar udaas baithe the.

Aise Ayodhya, bina Rama ke, ek sookhe samundar (dry ocean) ki tarah viran (desolate) lag rahi thi. 💔
        """
        create_image_text_layout("attached_assets/chapter2/2.48.2.jpg", text3, layout="side", image_position="right")

    # Chapter49
    with st.expander("Chapter 2.49 - The chariot crosses the border of Koshala"):

        text1 = """
Raat bhar chalne ke baad, subah hone par bhi Shri Rama ne apne pita ka aadesh (command) yaad rakhte hue apna safar jaari rakha. Suraj ugte hi unhone apni prarthna (morning prayer) ki aur rath ko aage badhaya. Dheere-dheere wo Koshala desh ki dakshini seema tak pahunch gaye.

Rath tez ghodon (horses) se kheench raha tha. Rama raaste mein kheton, phoolon se bhare van (forests) aur sugandhit (fragrant) pedon ko dekh kar prasann (happy) hue. Par unhone raste mein gaon ke logon ki baatein bhi suni —

        """
        create_image_text_layout("attached_assets/chapter2/2.49.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Ek bola, “Haye! Raja Dasharatha kitne kamzor ho gaye moh (attachment) ke aage. Aur wo Kaikeyi — uska dil to pathar (stone) ka lagta hai! Usne to sab maryada (tradition) tod kar itna bada paap (sin) kar diya. Usne apne hi ghar ke deepak (light) ko van mein bhej diya — Rama jaise dayalu (compassionate) aur vidwan (learned) putra ko!”

Dusra bola, “Aur Sita ji? Janak Raja ki beti, jo rajmahal mein sukh se pali, wo van ke kathin (hard) jeevan ko kaise sahegi? Raja Dasharatha agar sach mein Rama se prem karte, to wo unhe kabhi vanvas (exile) nahi dete.”

In baaton ko sun kar Shri Rama ka mann kuch dukh se bhar gaya, par wo chup rahe aur rath ko aur tez chalwaya. Jaldi hi unhone Koshala ki seema paar kar li. Phir unhone pavitra (pure) Vedasruti nadi ko paar kiya aur dakshin disha (south direction) ki or badhe.

Thodi door jaane par wo Gaumati nadi tak pahunche, jiske kinare gaayen (cows) chain se char rahi thi. Rama ne ghodon ko sambhalte hue nadi paar ki, phir Syandika nadi tak gaye, jahan mor (peacocks) aur hans (ducks) ki madhur awaaz sunai de rahi thi.

Rama ne Sita ji ko dikhaya — “Dekho Sita, ye wahi bhoomi (land) hai jo Maharishi Manu ne Ikshvaku vansh ko di thi. Kitni vistrit (vast) aur sundar jagah hai ye.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Phir Rama ne apne mitra aur saarathi (charioteer) Sumantra se muskurate hue kaha —
“Hey Sumantra, kab wo din aayega jab main apne mata-pita ke saath vanvaas (exile) poora karke wapas lautunga, aur Sarayu ke kinare phoolon se bhare jungle mein shikar (hunting) karunga? Rajrishiyon (royal sages) ka to yahi dharm (duty) hota hai — prakriti ke beech rehkar dharm aur veerta dono ka palan (balance) karna.”

Aise hi meethi baatein karte hue, Rama, Sita, Lakshmana aur Sumantra ji van ki or badhte gaye — poori shanti aur dridh nishchay (firm resolve) ke saath. 🌿
        """
        create_image_text_layout("attached_assets/chapter2/2.49.2.jpg", text3, layout="side", image_position="right")

    # Chapter50
    with st.expander("Chapter 2.50 - Guha, the boatman chief, meets Rama"):

        text1 = """
Koshala ki seema paar karne ke baad, Shri Rama ne apna chehra Ayodhya ki or modha, haath jodkar kaha —
“Hey Ayodhya nagari, Ikshvaku vansh ke rajaon dwara surakshit sundar shahar, main tumhe pranam karta hoon. Tumhare saath rahne wale sab devtaon ko bhi vandan karta hoon. Jab main apne pita ka aadesh (command) poora kar loonga, tab vanvaas (exile) se lautkar tumhe aur apne mata-pita ko fir se dekhunga.”

Phir Rama ne dono haath upar uthaye, aankhon se aansu behte hue kaha —
“Hey Ayodhya ke prajano (citizens), tumne mujhe hamesha apne swami (master) ke jaise samman (respect) aur prem diya hai. Par ab tum apne ghar wapas jao, apni grihastha (household duties) sambhalo. Mera saath aur dukh dekhkar tum aur pareshaan ho jaoge.”

        """
        create_image_text_layout("attached_assets/chapter2/2.50.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Log rone lage, sab ne Rama ko pranam kiya, unke charo or parikrama (circumambulate) ki, aur phir wapas chale gaye — bar-bar ruk kar piche mudke unhe dekhte hue, aansu pochhte hue. Rama ne unki dasha (state) dekhkar Sumantra se kaha, “Rath tez chalao.”
Jaise suraj ast (sets) hote hue aankhon se ojhal (disappear) ho jaata hai, waise hi Rama unki nazron se door ho gaye.

Aage badhte hue Rama ne sundar gaon aur shahron ko dekha — har jagah mandir (temples), yagna-stambh (sacrificial pillars), sadhu-sant, aur dharmik log. Kheton mein gaayen char rahi thi, bagiche aam (mango) ke pedon se bhare the, aur raaste saf aur sajhe hue the. Har jagah Veda ke paath (chant) sunai de rahe the.

Dheere-dheere Rama Ganga ji ke tat (bank) tak pahunche. Unhone us pavitra (holy) nadi ko dekha, jismein thandi, teeno dishaon mein behne wali dhara (current) thi. Ganga ke kinare rishi-muni ke ashram (hermitages) the, jahan pavitra jal ke kund (ponds) aur kamal (lotus) se bhare talab the.

Shri Ganga nadi ko dekhkar Rama ke man mein shanti aa gayi. Wo nadi itni sundar thi jaise koi gehno se saja hua stree (woman). Safed jhag (foam) se uska paani chamak raha tha, jaise kisi kanya ke baalon mein chamak ho. Kabhi uska paani laal kamal ke pankhudi (petals) se laal dikhai deta, jaise laal saari pehni ho. Har jagah hans (swans), saras (cranes) aur chakor pakshi ki awaazein gunj rahi thi.

Rama ne kaha, “Hey Sumantra, chalo, hum yahan Ganga ke tat par rukein. Us Ingudi ke ped ke neeche aaram karenge. Ye pavitra nadi sab devtaon, danavon, pashuon aur pakshiyon dwara poojit hai. Yahan hum snan (bath) karke prarthna karenge.”

Sumantra aur Lakshmana ne kaha, “Jaisa aap kahen.” Unhone rath ko us ped ke neeche roka. Rama aur Lakshmana neeche utare. Sumantra ne ghodon ko kholkar unhe aaram diya.

Us desh ke raja the Nishadraj Guha — Rama ke priya mitra, jaise bhai. Wo nishad (ferryman) jaati ke the, par unke paas apni sena (army) aur rajya (kingdom) tha. Jab unhe pata chala ki Rama unke kshetra (region) mein aaye hain, to wo apne mantri aur mitron ke saath turant milne aa gaye.

Rama ne unhe door se dekha aur Lakshmana ke saath aage badhkar swagat (welcome) kiya. Guha ne unhe tapasvi (ascetic) ke vastr (clothes) mein dekha to unka dil dukh se bhar gaya. Wo jhuke aur bole —
“Hey Rajkumar, ye chhoti si bhoomi (land) ab aapke liye Ayodhya samaan hai. Aapka yahan swagat hai. Main aapka daas (servant) hoon. Aap jo kahenge, wahi hoga.”

Guha ne unke liye bhojan (food), arghya (welcome water), aur aaram ke palang (beds) lagwaya aur bola —
“Hey Prabhu, ye mera rajya, ye bhojan, ye sab aapka hi hai. Kripya sweekar (accept) karein.”

Rama ne pyaar se kaha —
“Hey mitra Guha, tumne jo prem se paanv chal kar mujhe milne aaye, wahi mera samman (honour) hai. Main santusht hoon.”
Phir unhone Guha ko gale lagaya aur kaha —
“Main tapasvi ke roop mein vanvaas par hoon. Main na bhojan le sakta hoon, na uphaar (gifts). Main sirf fal (fruits) aur mool (roots) par jeevan bitata hoon. Mujhe sirf ghodon ke liye chara (grass) aur paani chahiye — bas wahi mera satkar (welcome) hoga.”

Guha ne turant apne sevakon ko aadesh diya ki ghodon ke liye chara aur paani laaya jaye.
Shaam ko Rama ne bark (tree bark) ke vastr pehne, apni sandhya prarthna ki, aur Lakshmana ne unke liye paani laakar diya.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Rama aur Sita ji Ingudi ped ke neeche so gaye. Lakshmana dhanush-baan (bow and arrow) lekar unki raksha (protection) karte hue paas hi baith gaye. Guha aur Sumantra bhi unke paas baithe aur dharm aur bhakti ki baatein karte rahe.

Wo raat shaant aur pavitra (holy) thi. Rama — Dasharatha ke putra, jo sukh ke hakdaar the, phir bhi zameen par so rahe the — phir bhi unka mann bilkul shant tha. Unhone poori raat sukh aur santulan (peace and balance) ke saath bitayi. 🌙
        """
        create_image_text_layout("attached_assets/chapter2/2.50.2.jpg", text3, layout="side", image_position="right")

    # Chapter51
    with st.expander("Chapter 2.51 - Rama spends the night near the river"):

        text1 = """
Raat gehri ho chuki thi. Ganga ji ke kinare thandi hawa chal rahi thi, aur chandni (moonlight) pedon ke patton par chamak rahi thi. Rama aur Sita Ingudi ke ped ke neeche shant neend mein the, unke paas Lakshmana dhanush-baan (bow and arrows) lekar jagte hue pehra de rahe the. Tabhi Nishadraj Guha, jo Rama ke mitra aur bhakt the, dheere se Lakshmana ke paas aaye aur kaha —

        """
        create_image_text_layout("attached_assets/chapter2/2.51.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“Hey Mitra, aap bhi thoda aaram kar lijiye. Ye naram bistar humne aapke liye tayyar kiya hai. Hum van ke log hain, hume jungle ki raaton ki aadat hai. Aap to rajmahal (royal palace) ke sukh-samaan mein pale-badhe ho, thoda chain se so jaiye. Hum sab milkar poori raat Shri Rama ki raksha (protection) karenge. Is dharti par koi bhi unse zyada mujhe priya (dear) nahi hai. Main kasam khata hoon, main unke liye apni jaan tak de sakta hoon. Aaj raat hum sab apne dhanush-baan ke saath yahan pehra denge. Mujhe is jungle ka har kone, har awaaz, har dariya ka raasta yaad hai. Agar koi dushman (enemy) bhi aa gaya to main use yahan ek kadam bhi badhne nahi doonga.”

Lakshmana ne shant par dridh (firm) swar mein jawab diya —
“Hey Guha, mujhe tumhari veerta aur prem par poora vishwas hai. Main jaanta hoon, Rama aapke saath surakshit hain. Par dharma (duty) mujhe sukh se baithne ya sone nahi deta. Jab tak Rama aur Sita is thandi zameen par so rahe hain, tab tak main kaise aankh band kar loon? Jab tak wo vanvas (exile) ki kasht (suffering) mein hain, mujhe bhi jagte rehna hoga.”

Lakshmana ne apni aankhen Rama par tikaye rakhi aur dheere se bola —
“Hey Nishad, dekho! Ye wahi Shri Rama hain, jinse koi rajya ka shatru (enemy) tak ladne ki himmat nahi karta tha. Aaj wahi Rama tinke (straw) ke bistar par so rahe hain. Jo Raja Dasharatha ne tapasya (penance) aur daan (charity) ke punya (merit) se prapt kiya tha, wahi putra aaj van ke dhool (dust) mein so raha hai. Mujhe dar hai, Raja Dasharatha apne priya putra ke bina zyada din nahi jeeyenge. Jab unhe pata chalega ki Rama ne jameen par so kar raat bitayi, unka hriday (heart) ye dard nahi saha payega.”

Uske baad Lakshmana ka swar dheere-dheere dukh se bhar gaya —
“Main sochta hoon, ab tak Ayodhya ki raniyaan — Kaushalya, meri maa Sumitra aur sab log — rote rote thak gaye honge. Shayad rajmahal ab bilkul sannata (silence) mein dooba hoga. Mujhe dar hai, Mata Kaushalya ye raat jeevi nahi rahegi. Shatrughna unhe sambhalega, par Kaushalya Maa ka dard Rama ke bina kam nahi hoga. Aur jab Raja Dasharatha unka antim sanskar (last rites) dekhenge, wo bhi apna praan (life) chhod denge. Tab Ayodhya, jo sukh aur dhan (prosperity) se bhari thi, shok (grief) mein doob jaayegi.”

Lakshmana ki aankhon mein aansu aa gaye. Usne asmaan ki or dekha, jaise Bhagwan se prarthna kar raha ho —
“Hey Parmeshwar, hum bas itna chahte hain ki Raja Dasharatha tab tak jeete rahein jab tak hum van se wapas laut kar unhe dekh sakein. Hume fir se Ayodhya ki galiyon mein chalne do — wo sundar rajdhani jisme rath (chariots), ghode (horses), hathi (elephants) aur veena (musical instrument) ki dhun gunjti hai. Jahan mandir (temples) ke gumbad suraj ki roshni mein chamakte hain, aur log haste-khelte hain. Kab fir se hum wahan lautenge?”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Guha ne ye sab suna aur unke dil mein bhi gahra dukh umad aaya. Wo chup ho gaye, unki aankhon se aansu tapakne lage — jaise kisi haathi ke dukh bhare ghoongh (cries) ho. Unka hriday Rama ke dukh se hil gaya tha.

Us pavitra raat, jab Ganga ki lehron ki dhun asmaan mein goonj rahi thi aur sitaare (stars) jaise Rama par pehra de rahe the — Lakshmana, Rama ke charanon ke paas baith kar poori raat jaagte rahe. Wo na neend mein the, na thakaan mein — bas apne bhai ke liye prem aur dharma se bhare hue the. 🌙
        """
        create_image_text_layout("attached_assets/chapter2/2.51.2.jpg", text3, layout="side", image_position="right")

    # Chapter52
    with st.expander("Chapter 2.52 - Sumantra is told to return to Ayodhya"):

        text1 = """
Subah hone par Shri Rama ne apne bhai Lakshmana se kaha —
“Dekho Lakshmana, raat (night) khatam ho gayi hai aur suraj (sun) ugne wala hai. Jungle mein pakshi (birds) jaag gaye hain — koel (cuckoo) aur mor (peacock) ki awaaz suno. Chalo, pavitra (holy) Bhagirathi nadi ko paar karte hain.”

Lakshmana ne turant Guha aur Sumantra ko bulaya. Guha samaj gaya ki Shri Rama nadi paar karna chahte hain. Usne apne mantriyon (ministers) se kaha, “Jaldi ek majboot aur achhi nauka (boat) le aao.”

        """
        create_image_text_layout("attached_assets/chapter2/2.52.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Thodi der baad boat tayyar thi. Guha ne haath jodkar Rama se kaha, “Prabhu, boat aa gayi hai, ab aap kya aadesh dete hain?”
Rama bole, “Guha, tumne sab kuch prabandh kar diya. Ab apna samaan (baggage) boat par rakh lo.”

Tab Sumantra, jinka sir jhuka hua tha, vinamr (humble) bhaav se bola, “Prabhu, ab mera kya kartavya (duty) hai?”
Rama ne pyaar se uske kandhe par haath rakha aur kaha,
“Sumantra, ab tum Ayodhya wapas jao. Raja Dasharatha ki seva (service) karo. Mujhe ab tumhari zarurat nahi hai. Main aur Lakshmana ab jungle (forest) mein pairon se chal kar jaayenge.”

Yeh sunkar Sumantra ka dil dukh se bhar gaya. Aansu rok kar bola,
“Prabhu, poore rajya mein koi nahi chahta tha ki aap Sita aur Lakshmana ke saath vanvaas (exile) jao. Aap jaise dayalu (kind) aur pavitra (pure) vyakti ko dukh mein dekhkar sabka mann ro raha hai. Aapka vanvaas teenon lokon ko jeetne jaise mahima (glory) dega, par hum jaise log, jo aapse door hain, wo to shraapit (cursed) hain.”

Rama ne use dhairya (comfort) diya aur kaha,
“Sumantra, Raja Dasharatha ab buddhe (aged) aur dukhi hain. Unka man bahut udaas hai. Tum unka dhyan rakho aur unhe mere sandesh (message) de do:
‘Rama, Lakshmana aur Sita van mein shanti se hain. Choudah saal ke baad hum sab wapas aayenge.’

Meri maa Kaushalya ke charanon mein pranam kehna, aur kehna ki hum teeno swasth (healthy) hain. Raja ko kehna ki Bharata ko bula kar use rajyabhishek (coronation) kara dein, taki unka dukh kam ho.”

Phir Rama ne kaha, “Bharata ko kehna ki wo sab maaon (mothers) ko ek samaan samman (equal respect) de, jaise Raja Dasharatha dete the. Agar wo pita ke kehne par rajya swikaar (accept) karega, to use dono lokon (worlds) mein sukh aur kirti (fame) milegi.”

Sumantra ro pad gaya aur bola,
“Prabhu, maaf kijiye agar meri baat kuch adhik (too much) lage, par main aapse alag nahi reh sakta. Ayodhya bina aapke shav (corpse) jaisi lagti hai. Log rath (chariot) ko akele dekhkar royenge. Main maa Kaushalya se kya kahunga? Kaise kahu ki maine aapko jungle mein chhod diya? Mujhse jhoot bhi nahi bola jaayega, aur sach kehne ki himmat bhi nahi.”

“Yeh ghode (horses) bhi bina aapke nahi chalenge. Mujhe bhi apne saath jungle le chaliye. Agar aap mujhe mana karenge, to main rath ke saath agni (fire) mein pravesh kar jaunga. Main aapka rakshak (protector) ban kar chalna chahta hoon. Jungle mein aapki seva karna mere liye swarg (heaven) se bhi badhkar hai.”

Rama ne shant swar (calm voice) mein kaha,
“Sumantra, mujhe pata hai tumhara prem (love) sachcha hai. Lekin agar tum Ayodhya wapas jaoge, to maa Kaikeyi samjhegi ki maine sach mein vanvaas svikaar kiya. Usse santosh (peace) milega, aur wo Raja Dasharatha ko dosh (blame) nahi degi. Mujhe chahta hai ki wo bhi sukh se rahe aur Bharata raj kare. Isliye, meri khushi ke liye, tum laut jao.”

Phir Rama ne Guha se kaha,
“Guha, main tumhare sheher ke paas nahi reh sakta. Main ek aur jagah par patton aur lakdiyon se kutiya (hut) bana kar rahunga. Yeh vanvaas mere pita ki atma-shanti (soul’s peace) ke liye hai. Ab mujhe bhurja vriksha (birch tree) ka doodh (sap) la do.”

Guha ne vah doodh laya aur Rama ne usse apne aur Lakshmana ke baalon (hair) par dala. Dono ne jata (matted hair) bana li aur valkal (bark clothes) pehni. Ab dono tapasvi (ascetics) jaise lag rahe the. Rama ne kaha,
“Guha, apne praja (people) aur sainya (army) ka dhyan rakhna. Rajya mehnat aur satarkta (alertness) se chalta hai.”

Guha se vidai lekar Rama, Sita aur Lakshmana Ganga ke kinare pahunch gaye. Rama ne kaha,
“Lakshmana, boat ko pakad kar rakho aur pehle Sita ko chadha do.”
Lakshmana ne pehle Sita ji ko aur phir Rama ko chadhaya. Guha ne nauka chalane ka aadesh diya.

Boat ke beech pahunch kar Sita ne haath jodkar kaha,
“Hey Maa Ganga, Dasharatha ke putra Rama jo pitaji ke aadesh (command) se van gaye hain, unki raksha (protection) karna. Choudah saal baad hum sab surakshit (safe) wapas aayein, tab main aapka pooja karungi. Aapko gau (cows), anna (grain), aur vastra (clothes) daan (donation) karungi. Tab tak humein apna aashirvaad (blessing) do.”

Is prarthana (prayer) ke baad nauka paar ho gayi. Rama, Sita aur Lakshmana ne paavitra (holy) Ganga ko pranam kiya aur van ki or chal diye.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Rama ne kaha,
“Lakshmana, tum aage chal kar Sita ji ki raksha karna. Main peeche chalunga taki tum dono surakshit raho. Ab se Sita ko bhi van ke kathin jeevan (hard forest life) ki aadat daalni hogi.”

Lakshmana ne haan mein sir hilaya aur Sita ke saath aage badh gaya. Rama peeche unka raksha karte hue chalte rahe.

Us paar kinare par Sumantra unhe door jaata dekhte hue ro pada. Aansu uske gaalon par beh rahe the. Rama, Sita aur Lakshmana ne Ganga paar kar li thi — unka vanvaas ab sach mein shuru ho gaya tha.
        """
        create_image_text_layout("attached_assets/chapter2/2.52.2.jpg", text3, layout="side", image_position="right")

    # Chapter53
    with st.expander("Chapter 2.53 - Rama, Sita, and Lakshmana start their exile life"):

        text1 = """
Shaam hone par Shri Rama ne ek ped ke neeche baith kar apni Sandhya vandan (evening prayer) ki. Phir unhone Lakshmana se kaha,
“Lakshmana, aaj raat hamari pehli raat hai jungle mein — bina Sumantra ke. Udaas mat ho. Ab se hum dono mein se ek raat mein jaagega, taki Sita ki raksha (protection) ho sake. Chalo, patte (leaves) aur ghaas jama karte hain, aur apna bistar bana lete hain.”

Us raat, jo Rama hamesha rajsi (royal) singhasan aur sukhad shayya (comfortable bed) par sota tha, usne zameen par sona svikaar (accepted) kiya. Zameen thandi thi, lekin uska mann shant tha. Baatein karte hue Rama bola,

        """
        create_image_text_layout("attached_assets/chapter2/2.53.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“Lakshmana, ho sakta hai pitaji Dasharatha ne aaj chain se na soya ho. Par Kaikeyi — jisne apna ichchha (desire) pura kar liya — wo to ab sukh se so rahi hogi. Mujhe dar hai ki wo rajya ke lobh (greed for kingdom) mein pitaji ko dukh pahunchaye, shayad unki jaan le le, Bharata ke lautne se pehle.

Pitaji ab kamzor (weak) aur Kaikeyi ke adheen (under her control) hain. Unka mann ab vasna (desire) se bhara hai. Unka aisa patan (downfall) dekhkar lagta hai ki moh (lust) dhan aur dharma (wealth and virtue) se bhi zyada balwan (powerful) hai. Kaunsi murkh (foolish) vyakti hoga jo ek agyakari (obedient) putra jaise mujhe tyag dega — bas ek stree (woman) ke kehne par?

Bharata to sach mein bhaagyashali (fortunate) hai, jise Ayodhya mil gayi. Raja Dasharatha ka jeevan ab ant ke kareeb hai, aur main jungle mein hoon. Jo vyakti dharma (righteousness) chhod kar sirf apni ichchhaon ke peeche bhaagta hai, wo aakhir dukh (sorrow) hi paata hai.”

Phir Rama ne dukh bhare swar mein kaha,
“Mujhe lagta hai Kaikeyi hamare ghar mein isliye aayi thi — Raja ko nash karne, mujhe vanvaas bhejne, aur Bharata ko rajya dene ke liye. Mujhe dar hai ki wo apni shakti (power) ke ghamand (pride) mein Maa Kaushalya aur Maa Sumitra ko sataye. Lakshmana, agar tum Ayodhya laut jao, to maa Kaushalya ki raksha ho jayegi. Main aur Sita Dandaka van (forest) chale jayenge. Kaikeyi jaise durbhavna (malicious intent) rakhne wali stree se un dono maaon ka surakshan (protection) tumhare haath mein hoga.”

Rama ne bhari saans lekar kaha,
“Lakshmana, shayad kisi purvajanma (previous birth) mein meri maa ne kisi anya stree ka putra chheen liya hoga, tabhi aaj wo iss dukh ka phal (fruit) bhugat rahi hain. Mujhse bada durbhaagyashali (unfortunate) putra koi nahi, jo apni maa ko rota chhod kar khushi se jeena chahta hai. Koi stree kabhi mere jaisa beta paida na kare — jo apni maa ke liye itna dukh ka kaaran bane.

Ek samay, maine apni palit (pet) maina ko sikhaya tha: ‘Shatru (enemy) ke muh mein hote hue uske pair par kaat (bite) lena.’ Aaj meri maa bhi us shatru (Kaikeyi) ke muh mein hai, aur main kuch nahi kar sakta. Bechari maa, uska dukh samundar jaisa gehra (deep) hai.”

Rama ne fir kaha,
“Lakshmana, agar main chaahoon to apne krodh (anger) se poori duniya jeet sakta hoon, par dharma (righteousness) ke liye main apni shakti (power) nahi dikhata. Agar main rajya zabardasti le lunga, to paap (sin) lagega, aur meri aatma (soul) dukh paayegi.”

Aise karte karte, Rama ke aankhon se aansu behne lage. Usne apni shakti aur santulan (restraint) chhod diya, aur raat bhar dukh mein roye.

Lakshmana chupchaap Rama ko dekhta raha — jaise bujha hua agni (fire) ya shaant samundar (calm sea). Phir usne pyar bhare shabd mein kaha,
“Bhaai, Ayodhya bina aapke raat ke bina suraj jaise ho gayi hai. Par aapko aise dukhi nahi hona chahiye, kyunki aapka dukh Sita aur mujhe bhi kamzor karega. Hum machhli (fish) ki tarah hain — bina aapke paani ke hum ek pal bhi nahi jee sakte. Mujhe na pita chahiye, na maa, na Ayodhya — mujhe bas aapke saath rehna hai.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Lakshmana ke yeh prerna bhare (encouraging) shabd sun kar Rama ne aansu ponchhe, aur Sita ke paas patton ke bistar (leaf bed) par baith gaya.

Us samay, Rama ne apna man pura dhairya (courage) se bhara aur kaha,
“Ab se hamara vanvaas (exile) sach mein shuru hota hai.”

Us din se, Raghu vansh (dynasty) ke do veer putra — Rama aur Lakshmana — apni pativrata (devoted) Sita ke saath, shant aur nirdar (fearless) roop se jungle mein rehne lage — jaise do shers (lions) pahaad ke shikhar (mountain peak) par virajmaan (residing) ho.
        """
        create_image_text_layout("attached_assets/chapter2/2.53.2.jpg", text3, layout="side", image_position="right")

    # Chapter54
    with st.expander("Chapter 2.54 - They visit Sage Bharadvaja’s hermitage"):

        text1 = """
Agle subah jab suraj bina badal ke nikla, Shri Rama, Sita aur Lakshman ne apni pehli raat ek bade bargad ke ped ke neeche bitayi thi. Phir teeno ne apna yatra (journey) jaari rakha, aur wo pohonche us jagah jahan Ganga aur Yamuna nadi milti hain — Prayag. Jaise jaise wo van (forest) ke andar badhte gaye, unhe prakriti (nature) ke bahut sundar drishya (scenes) dikhai diye — khilte hue ped, gunjti chidiyaan, aur nadiyon ki shant dhwani.

Sham hone lagi thi tab Shri Rama ne Lakshman se kaha,
“Hey Lakshman, dekho, udhar se dhuan (smoke) uth raha hai — lagta hai Rishi Bharadvaj ka aashram paas hi hai. Aur suno, wo zor se paani ki awaz — Ganga aur Yamuna ke milne ki hai. Hum nischay (surely) se Sangam pahunch gaye hain.”

        """
        create_image_text_layout("attached_assets/chapter2/2.54.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Thodi der baad, suraj dhalte hue, wo dono dhanurdhari (archers) Sangam aur Rishi Bharadvaj ke aashram tak aa gaye. Rama ne kuch door ruke hue, bade samman se Rishi ko pranam kiya aur dheere se andar gaye. Wahan unhone dekha — Rishi Bharadvaj apne shishyon (disciples) ke saath yagya kar rahe the.

Rama, Sita aur Lakshman ne unke charan chhu kar namaskar kiya. Rama ne kaha,
“Hey Muni (sage), hum Raja Dasharath ke putra hain — main Rama, ye mera bhai Lakshman, aur ye meri patni Sita, Janak ji ki beti. Pitaji ke agya se hum vanvaas (exile) mein aaye hain, aur dharm palan karte hue fal-mool (fruits and roots) se jeevan bitayenge.”

Rishi Bharadvaj ne bade prem aur samman se unka swagat kiya — pehle unhe madhuparka (honey-milk offering) diya, paani se unke pair dhulwaye, aur phir fal-mool khilaye. Rishi ne Rama se kaha,
“Hey Ram, tumhe bahut dinon baad dekha. Suna hai tumhe bina kisi dosh (fault) ke vanvaas diya gaya. Ye pavitra sthal (holy place) Ganga-Yamuna sangam par hai — yahan tum kuch din aaram se raho.”

Rama ne muskurakar kaha,
“Hey Muniwar, ye jagah to bahut pavitra hai, par yahan se manushya (people) ke gaon paas hain. Log humse milne baar-baar aayenge. Kripya hume aisi jagah bataiye jo shant aur door ho, jahan Sita sukhi rahe sake.”

Tab Rishi Bharadvaj ne madhur swar (gentle tone) mein kaha,
“Hey Ram, yahan se das kos (around ten miles) door ek sundar parvat (mountain) hai — Chitrakoot. Wahan kai rishi-muni tap (penance) karte hain. Wahan bandar (monkeys), bhalu (bears) aur anek prani (creatures) khule ghoomte hain. Ye parvat Gandhamadan jaisa manohar (beautiful) hai. Jo bhi Chitrakoot ke shikhar (peaks) dekhta hai, use punya (spiritual merit) milta hai. Wahan rehkar man pavitra ho jata hai. Tum Sita ke saath wahan sukh se reh sakte ho.”

Us raat Shri Rama, Sita aur Lakshman ne Prayag mein Rishi Bharadvaj ke aashram mein shanti se raat bitayi. Rishi ke saath unhone purane yugon ki kahaniyaan suni aur vanvaas ke pehle din ki thakan door ki.

Subah hone par Rama ne Rishi ke paas jaakar pranam kiya aur kaha,
“Hey Muni, humne aapke aashram mein bahut shanti se raat bitayi. Ab kripya hume vidya (permission) dijiye, taaki hum Chitrakoot ke liye prasthaan (depart) kar sakein.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Rishi Bharadvaj ne ashirwad dete hue kaha,
“Hey Ram, jao Chitrakoot parvat par — wahan madhumakhiyon ka madhur ras (honey), fal, aur jad (roots) milenge. Wahan haathi (elephants), mor (peacocks) aur anek pakshi (birds) baste hain. Wahan Sita ke saath jalprapaton (waterfalls), pahaadiyon aur gufaon ke paas tumhara man prasann (happy) rahega. Tumhara vanvaas ka samay wahan sukhmay (peaceful) bitaayega.”

Aur is prakar, Rishi Bharadvaj ke ashirwad se Shri Rama, Sita aur Lakshman Chitrakoot ke liye nikal pade. 🌿
        """
        create_image_text_layout("attached_assets/chapter2/2.54.2.jpg", text3, layout="side", image_position="right")

    # Chapter55
    with st.expander("Chapter 2.55 - They cross the Yamuna River"):

        text1 = """
Prayag mein raat bitakar, subah hone par Shri Rama aur Lakshman ne Rishi Bharadvaj ko pranam kiya aur unke aashirvad lekar Chitrakoot ki ore nikal pade. Rishi Bharadvaj ne pita ke jaise apne putron ko aashirvad dete hue kaha,
“Hey Ram, Ganga aur Yamuna ke sangam se thoda paschim (west) taraf jao. Wahan Yamuna ke kinare ek purani naav (boat) milegi. Tum usse paar ja sakte ho — usme dono kinare par ulte matke (pitchers) bandhe hue hain, jo use paani mein sambhalte hain. Dusri taraf ek bada hara bhara bargad (fig tree) milega, jiske aas-paas aur bhi ped hain. Us ped ke neeche tum Janaki ke saath prarthana (pray) karna, taaki tumhara yeh vanvaas (exile) safal ho. Thoda aaram karke aage badhna — wahan se ek kos (mile) door Nilvan naam ka sundar van hai. Wahan se Chitrakoot jaane ka rasta hai. Ye rasta bahut manohar (beautiful), bina kaanton ke, aur vanagni (forest fire) se surakshit hai.”

        """
        create_image_text_layout("attached_assets/chapter2/2.55.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Itna batakar Rishi Bharadvaj apne aashram laut gaye. Rama ne unhe pranam kiya aur Lakshman se kaha,
“Hey Bhai, hum kitne dhanya (fortunate) hain jo itne pavitra rishi ne hume apna aashirvad diya.”

Chalte hue wo teeno — Rama, Sita, aur Lakshman — Yamuna ke kinare pahunch gaye. Nadi tez beh rahi thi, isliye unhone milkar kuch lakdi aur sukhe baans (bamboo) jod kar ek naav (raft) bana li. Lakshman ne Sita ke liye jamun aur vetas ke pedon ki shaakhaon se ek chhoti si baithak (seat) bana di. Phir Rama ne pyaar se Sita ka haath pakda, use naav par bithaya, aur uske gehne aur vastra (clothes) rakh diye.

Naav ke beech pahunchkar Sita ne dono haath jod kar Yamuna Devi se prarthana ki:
“Hey Devi Yamuna, kripya humein kshama karo (forgive us) jo hum tumhe paar kar rahe hain. Mere prabhu Shri Rama ka vanvaas bina kisi badha ke poora ho. Jab hum lautenge, tab main tumhe hazaar gau (cows) daan (donation) karungi.”
Aur phir kaha, “Hey Ikshvaku vansh ke Swami, aap Ayodhya shahar mein surakshit laut kar jaiye.”

Jab wo Yamuna ke dakshin (southern) tat (bank) par pahunch gaye, to unhone naav chhod di aur van ke andar kadam rakha. Wahan ek bada hara bargad ka ped tha, jiske neeche Sita ne haath jod kar kaha,
“Hey Vriksha Devta, kripya mere prabhu ke sankalp (vow) ko poora hone dijiye, taaki main phir se Maa Kaushalya aur Maa Sumitra ka darshan kar sakoon.”
Phir Sita ne us ped ki parikrama (circumambulation) ki.

Rama ne muskurakar Lakshman se kaha,
“Hey Lakshman, Sita ko aage le jao — ye sada vinay (humble), nirdosh (innocent) aur meri praan (life) se bhi pyaari hai. Uska man prasann (happy) rahe, isliye jo bhi phool ya phal wo chahe, tum uske liye tod lena.”

Is prakar Sita beech mein, aur dono Rajkumaar uske dono taraf chal rahe the — jaise ek komal haathi (female elephant) ke saath do majboot dantwala (tusked) haathi chalein. Sita van ke naye-naye drishya dekhkar har ped-paudhe ke baare mein Rama se sawal karti. Lakshman har bar uske liye sundar phool tod laata. Nadi ke kinare hans (swans) aur bagule (cranes) ko dekhkar Sita ke chehre par khushi chha gayi.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Kuch door badhne par Rama aur Lakshman ne shikar ke liye kuch hiran (deer) maare, taaki bhojan (food) mile. Phir teeno ne apni yatra jaari rakhi — wo van pakshiyon ke geet, moron ke naach, aur haathiyon ke swar se goonj raha tha.

Ant mein jab unhe ek shant aur sundar sthal mila jo Sita ko pasand aaya, to wahan teeno ne apna naya aashray (shelter) banaya aur bina bhay (fear) ke vahan raat bitayi. 🌿
        """
        create_image_text_layout("attached_assets/chapter2/2.55.2.jpg", text3, layout="side", image_position="right")

    # Chapter56
    with st.expander("Chapter 2.56 - Rama, Sita, and Lakshmana reach Chitrakoot"):

        text1 = """
Subah hone par, Shri Rama ne dheere se Lakshman ko jagaya aur bola,
“Hey Lakshman, suno, kitni madhur (sweet) awaaz mein tota, koel, maina aur aur bhi pakshi (birds) gaa rahe hain! Yeh subah ka samay hai, chalo, hum apni yatra jaari rakhein.”

Lakshman ne neend chhodi, nadi Yamuna mein snan (bath) karke dono bhaiyon ne apna pratah-sandhya (morning prayer) kiya. Phir teeno ne palash (palasa) ke pedon se bhare van ka rasta pakda, jaise Rishi Bharadvaj ne bataya tha.

        """
        create_image_text_layout("attached_assets/chapter2/2.56.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Chalte hue Rama ne muskurakar Sita se kaha,
“Hey Janak-nandini (daughter of Janaka), dekho, yeh palash ke pedon par kitne sundar laal-phool khile hain, jaise agni (fire) ke sholay chamak rahe ho. Wahan dekho bilva ke ped, jinhe kisi manushya ne nahi chhua. Yahan hum araam se phal-mool pa sakte hain. Dekho Lakshman, in pedon par kitne bade madhumakkhiyon ke chhatte (beehives) lage hain, aur unka gungunana kitna madhur hai! Pakshi gaa rahe hain, mor unke geet ka jawab de rahe hain — aur zameen phoolon se dhak gayi hai. Wahaan dekho, Chitrakoot ke unche shikhar (peaks) — sundar pakshiyon aur gajon (elephants) se bhare hue. Mujhe lagta hai un pahaadiyon ke beech koi shant aur sunder sthal hoga, jahan hum apna nivas (home) bana sakte hain.”

Chalte-chalte teeno Chitrakoot par pahunch gaye — ek manohar parvat, jahan sab kuch shant, hara-bhara aur pavitra tha. Wahan meetha paani tha, phal-mool the, aur aas-paas anek pakshi aur mriga (deer) ghoom rahe the. Rama ne kaha,
“Hey Lakshman, yeh jagah kitni sundar hai — pedon, belon aur phalon se bhari hui. Yahan hum shanti se reh sakte hain, bina kisi dar (fear) ke. Yeh tapasviyon (sages) ke liye bhi upyukt sthal hai.”

Teeno phir Rishi Valmiki ke aashram gaye. Rishi ne unka swagat karte hue kaha,
“Swagat hai tumhara, Hey Raghuvanshi putra!”
Rama ne vinamrta se pranam kiya aur apne vanvaas (exile) ka karan bataya. Phir Lakshman se bola,
“Hey Bhai, kuch mazboot lakdiyaan le aao, hum yahan ek sundar kutir (hut) banaenge. Mujhe yahi rehna acha lagega.”

Lakshman ne bade utsaah (eagerness) se kaam shuru kiya. Unhone lakdiyaan kaat kar, patton aur shaakhon se ek chhoti si par sunder jhopdi (hut) banai, jismein ek darwaza bhi tha. Rama ne dekha to muskurakar bola,
“Hey Lakshman, ab hum is griha (home) mein pravesh karne se pehle is sthal ke Devtaon ko shanti-puja (peace ritual) karte hain. Tum ek kala hiran (black deer) laao, taaki hum yagya (ritual offering) kar sakein.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Lakshman ne jald hi hiran laaya, uska maans (meat) agni mein pakaaya, aur Rama ne Vedic mantron ke saath sab Devtaon — Vishnu, Rudra aur Prithvi ke Devtaon — ko ahuti (offering) di. Uske baad unhone Shanti Paath (peace chant) kiya aur nadi mein snan karke kutir mein pravesh kiya.

Jungle ke pakshiyon aur janwaron ki awaazon ke beech, patton se bani apni jhopdi mein Rama, Sita aur Lakshman shanti aur anand se rehne lage. 🌿

Chitrakoot ke nirmal vaayu, nadiyon aur phoolon se ghirkar, Rama apne dukh bhool gaye — unhe na Ayodhya yaad rahi, na vanvaas ka dard. Sirf ek sukoon bhari shanti thi unke man mein. 🌸
        """
        create_image_text_layout("attached_assets/chapter2/2.56.2.jpg", text3, layout="side", image_position="right")

    # Chapter57
    with st.expander("Chapter 2.57 - Sumantra returns to sad Ayodhya"):

        text1 = """
Jab Shri Rama ne Ganga paar kar li, tab Guha bahut udaas ho gaya. Usne der tak Sumantra se baatein ki, phir jab Rama ko usne dusre kinaare tak pahunchte dekha, to wo wapas laut gaya.

Sumantra, jo Rama ka rath chalata tha, use Shringverpur ke logon se pata chala ki Rama ne Prayag me Rishi Bharadvaj se milkar Chitrakoot ki or yatra shuru kar di hai. Tab Sumantra ne Guha ko alvida kaha aur dil me dukh lekar Ayodhya wapas nikal pada.

Teen din tak wo phoolon se bhare jungle, nadiyon aur gaonon ke beech se guzra. Jab shaam hui, tab wo Ayodhya nagri ke paas pahunch gaya. Lekin Ayodhya ab pehle jaisi nahi thi — sab kuch shaant tha, jaise poori nagri dukh se jam gayi ho.

        """
        create_image_text_layout("attached_assets/chapter2/2.57.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Sumantra ne socha, “Kya Raja Dasharatha aur poori Ayodhya shok (grief) ke aag me jal gayi hai Rama ke bichhadne ke dukh me?”

Jab wo rath lekar sheher me ghusa, log turant uske aas-paas aa gaye aur poochhne lage —
“Rama kaha hai?”
“Rama kaha hai?”

Sumantra ne aansuon bhari awaaz me kaha, “Rama ne mujhe Ganga ke kinaare se wapas bhej diya… unhone nadi paar kar li hai.”

Ye sunte hi sab log rote hue chillane lage —
“Haay Rama! Hamara rakshak, hamara priya rajkumar chala gaya! Ab hum kiske darshan karenge?”

Jab Sumantra mahal ke paas pahunchaa, usne suna ki har ghar ke andar aurton ki roti hui awaaz aa rahi thi. Sab kah rahi thi, “Rama ke bina Ayodhya suna lagta hai.”

Mahal ke andar pahunchte hi, Rani Kaushalya, Rani Sumitra, aur anya raniyan use dekh kar rote hue boli:
“Sumantra akela wapas aa gaya… to phir Rama kaha hai? Kya Kaushalya mata ab tak zinda hain bina Rama ke?”

Ant me Sumantra raja ke paas gaya. Raja Dasharatha bahut kamzor ho chuke the, unka chehra peela aur aankhein aansuon se bhari thi. Sumantra ne Rama ka sandesh diya — par Dasharatha kuch na bol sake. Dukh se unka dil bhar gaya aur wo behosh hokar gir pade.
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Rani Kaushalya aur Rani Sumitra ne raja ko uthaya aur rote hue boli:
“Hey Maharaj! Rama ka sandesh sun kar aap kyun chup hain? Ab to Kaikeyi yahan nahi hai, darne ki koi baat nahi. Kripya kuch to kahiye!”

Par Raja kuch na keh sake. Tab Kaushalya bhi dukh se behosh ho gayi.
Sab raniyan aur mahal ke log zor zor se rote rahe.
Poora Ayodhya nagar fir se us din ki tarah ro padi — jaise us din royi thi jab Rama ne nagri chhodi thi. 💔
        """
        create_image_text_layout("attached_assets/chapter2/2.57.2.jpg", text3, layout="side", image_position="right")

    # Chapter58
    with st.expander("Chapter 2.58 - He gives Rama’s message to the king"):

        text1 = """
Thodi der baad jab Raja Dasharatha hosh me aaye, unhone Sumantra ko bulaya.
Bechare raja ka dil dukh se bhaari tha — wo aise saans le rahe the jaise koi naya pakda gaya haathi, dukh me phansa ho.

Sumantra dhool se bhara hua, aansuon se laal aankhon ke saath, haath jod kar raja ke saamne khada ho gaya.
Raja ne dukh bhari awaaz me kaha:

“Hey Sumantra, mera Rama, jo har sukh ke laayak hai, ab jungle me kisi ped ke neeche aaraam kar raha hoga.
Wo kya khata hoga? Wo kaise sote honge — wo jo rajgaddi par sona chahiye tha, ab zameen par mitti me so raha hoga.
        """
        create_image_text_layout("attached_assets/chapter2/2.58.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Mujhe soch kar dukh hota hai ki mere veer bete, Rama aur Lakshmana, aur meri komal (delicate) Sita, sab jungle me bina chappal ke chal rahe honge, jahan saanp aur jangli janwar ghoomte hain.

Hey Sumantra, tum to dhanay ho — tumne un dono bhaiyon ko dekha, jo apni tej (divine glow) me jaise Ashwini Kumar devtaon jaise lagte hain.
Batao, jab wo jungle me gaye to Rama ne kya kaha? Lakshmana ne kya kaha? Aur Sita ne kya kaha? Mujhe sab batao — unki baatein sun kar hi mera jeevan thoda aur tik sakta hai.”

Sumantra ka gala roop gaya tha, aansuon se awaaz toot rahi thi. Phir bhi wo bola:

“Hey Maharaj, Shri Rama, jo dharm (righteousness) ka rakshak hai, ne haath jod kar kaha tha —

‘Pitaji ko mera pranaam kehna. Unhe kahna ki main theek hoon.
Aur sab raniyon ko bhi meri taraf se vandan kehna, jaise unki maryada (respect) ke laayak ho.
Mata Kaushalya se kehna — dharm ka palan karein, aur yajna (sacrifice) ke sab kaam dhyaan se karte rahein.
Unhe kehna: “Hey Mata, Raja Dasharatha ko Bhagwan jaisa maan kar seva karein. Apne raj gharane ka abhimaan (pride) chhod kar, sab doosri raniyon ke prati bhi sneha aur samman rakhein.
Kaikeyi pitaji ki priya hai — unki bhi seva karein, jaise pitaji ki karti hain.”’

Phir Rama ne kaha tha —

‘Mere bhai Bharata se kehna, wo sab maaon ke saath nyay (justice) karein.
Jab tak pitaji zinda hain, wo swayam raja na banein.
Unka kartavya hai pitaji ki seva karna, aur rajya unke liye sambhalna, lekin apna adhikar na jatana.’

Aur fir Rama ki aankhon me aansu aa gaye. Unhone dard bhari awaaz me kaha —

‘Bharata se kehna, wo meri maa Kaushalya ko apni maa jaisi samjhein.’

Itna keh kar Rama zaar zaar ro diye.”

Tab Lakshmana ne gusse aur dukh me kaha:

“Hey Raja! Aapne to anyaay (injustice) kiya hai! Rama ne kya galti ki thi?
Sirf Kaikeyi ke moorkh (foolish) vachan sun kar, aapne Rama jaise pavitra (pure) putra ko vanvaas bhej diya!
Agar devtaon ne bhi Rama ko vanvaas dene ka faisla kiya hota, to bhi mujhe iska karan samajh na aata.
Aapne bina soch samjhe ye kathin (harsh) faisla liya hai — aur iska dukh aapko bhi sehna padega.

Rama sabka hit chahne wala, sabka priya hai. Aise pavitra putra ko vanvaas dena — kya ye raja ka dharm hai?
Jo apne logon ke virodh me jaakar aise kaam kare, wo raja kaise ho sakta hai?”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Ye sab sun kar raja ka dil phat gaya.
Aur jab Sumantra ne Sita ke baare me bataya, to sabki aankhon me aansu aa gaye —

Sumantra ne kaha:

“Hey Maharaj, Sita ji kuch bol nahi paayi.
Wo bas Rama ke chehre ko dekhti rahi, jahan aansu gir rahe the.
Unka gala sukh gaya tha, aankhen sukh chuki thi, par aansu rukte nahi the.
Jab Rama rath me baithe mujhe vidai de rahe the, to Sita bas chup-chaap mujhe dekhti rahi…
Jaise unki aankhen keh rahi ho — ‘Unka khayal rakhna, Sumantra.’” 😢
        """
        create_image_text_layout("attached_assets/chapter2/2.58.2.jpg", text3, layout="side", image_position="right")

    # Chapter59
    with st.expander("Chapter 2.59 - The king cries for Rama day and night"):

        text1 = """
Sumantra ne raja se kaha,
“Hey Maharaj, jab Shri Rama van (forest) mein pravesh (entered) kar gaye, tab main wapas laut aaya. Ghoṛe thake hue the, isliye ruk gaye aur dukhi lag rahe the. Mainne dono rajkumaron ko pranam kiya aur apne dukh ko rok kar rath ko aage badhaya. Kuch din main Guha ke saath ruka, is asha mein ki shayad Shri Rama mujhe wapas bula lein.”

“Hey Rajan, jab main wapas aane laga, to mujhe laga jaise van ke ped-paudhe bhi udaas ho gaye ho! Unke phool aur patte murjha gaye the, nadiyon ka paani kam ho gaya tha, aur janwar chup the. Hathi bhi idhar-udhar ghoomna band kar chuke the. Aisa lagta tha jaise poora van bhi Rama ji ke virah (separation) mein dukh mein doob gaya ho. Pokharo ka paani ganda ho gaya tha, kamal (lotus) ke phool paani ke neeche chhupe hue the, jaise ve bhi dukh se jhuk gaye ho. Machhliyan aur pankhi (birds) apni jagah chhod chuke the. Pedon ke phal aur phool ka swaad aur khushboo sab kho gaya tha. Bagiche bhi soone aur bejaan lag rahe the.”
        """
        create_image_text_layout("attached_assets/chapter2/2.59.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“Jab main Ayodhya ke paas aaya, to koi bhi khush nahi tha. Nagar ke logon ne jab rath dekha lekin Rama nahi dekhe, to sab rote hue saans le rahe the. Mahilayein apni khidkiyon aur chhaton se rath ko dekhti rahi aur rote hue kehne lagi, ‘Haye! Yeh rath to hai, par hamare Rama nahi!’ Unki aankhon ka kajal aansuon se dhul gaya tha. Sab log, hathi, ghode—sabhi udaasi se bhare hue the. Ayodhya aisi lag rahi thi jaise Kaushalya maa apne putra (son) ke bina akeli ho.”

Yeh sab sun kar Raja Dasharatha ka mann kamp utha. Unhone kanpte hue Sumantra se kaha,
“Hey Sumantra, mujhe bahut pachtava ho raha hai. Maine bina soch-vichar aur bina apne mantriyon se salah liye, Kaikeyi ko vachan de diya. Us samay main Manthara ke bharam (influence) mein tha. Yeh sab durbhagya (misfortune) meri hi galti hai. Ab yeh poora Ikshvaku vansh (family line) dukh mein doob gaya hai.”

“Hey Sumantra, agar maine kabhi tumhara bhala kiya ho, to mujhe Rama ke paas le chalo. Mera praan (life) ab nikalta ja raha hai. Ya phir tum jaakar use bula lao — agar wo ab bhi mujhe apna pita samajhta hai. Agar wo door chala gaya ho, to mujhe turant uske paas le chalo. Main usse ek baar dekhna chahta hoon. Rama, jiske daant kamal (water lily) jaise safed hain, jiska mukh prakashit hai, usse dekhe bina main jee nahi sakta.”

“Hey Rama! Hey Lakshman! Hey dhairyavaan (patient) Sita! Tumhe pata nahi, main yahan tumhare virah mein mar raha hoon.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Raja ne ro-ro kar kaha,
“Hey Kaushalya! Rama ke bina yeh dukh samundar jaise gehra ho gaya hai. Sita se alag hone ka dukh uska kinara (shore) hai, mere aansu uske lehron jaise hain, Manthara ke shabd (words) uske magar (crocodiles) hain, aur Kaikeyi us samundar ke andar jalti aag hai. Main is samundar mein doob raha hoon, bina Rama ke main isse paar nahi kar sakta.”

Aisa kehkar Raja Dasharatha behosh hokar apne shayan (bed) par gir pade. Unka sharir thak gaya tha aur mann bilkul tut gaya tha. Kaushalya maa ne yeh sab suna to unka hriday (heart) bhi kamp utha — wo bhay (fear) aur dukh se bhar gayin.
        """
        create_image_text_layout("attached_assets/chapter2/2.59.2.jpg", text3, layout="side", image_position="right")

    # Chapter60
    with st.expander("Chapter 2.60 - Sumantra tries to comfort Queen Kaushalya"):

        text1 = """
Rani Kaushalya zameen par giri hui thi, poori tarah kaanp rahi thi — jaise pran (life) nikal gaye ho ya koi bura saaya unpe chhaya ho. Dard bhari aawaaz mein unhone Sumantra se kaha,
“Hey Sumantra! Mujhe us jagah le chalo jahan mere Rama, Lakshman aur Janaki (Sita) rehte hain! Unke bina ek pal jeena bhi bekaar lagta hai. Tum turant rath le jao — ya to main unke saath rahungi, ya fir is jeevan ko chhod dungi (I will die)!”
        """
        create_image_text_layout("attached_assets/chapter2/2.60.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Sumantra ro padiye, par unhone Rani ko sambhalte hue kaha,
“Hey Devi, apna mann shant rakhiye. Dukh aur chinta chhodiye. Shri Rama van mein bilkul sukh se rahenge. Rajkumar Lakshman apne bade bhai ki seva mein, dharm ke marg (path of virtue) par chal kar, apne liye shubh bhavishya bana rahe hain. Aur Janaki (Sita) to apne pati ke prati poori bhakti se van mein rehti hain, bina kisi bhay (fear) ke — jaise wo apne ghar mein hi ho.”

“Sita ke mann mein koi bhay nahi hai. Lagta hai jaise wo van mein rehne ke liye hi paida hui ho. Jaise pehle wo Ayodhya ke baagon (gardens) mein ghoomti thi, ab waise hi van ke phool-paudhon ke beech khush rehti hai. Uska chehra poornima ke chand (full moon) jaisa chamak raha hai. Uska mann poora Rama mein basa hai. Uske liye van bhi Ayodhya ke bagiche se kam nahi lagta.”

“Wo Rama ke saath ped, nadi, aur gaon dekhkar unse puchhti hai — ‘Ye kaunsa ped hai, iska naam kya hai?’ Jaise chhoti si bachchi utsukta (curiosity) se sab jaanna chahti ho. Van uske liye ek sundar upvan (garden) ban gaya hai. Mujhe Sita ke sab shabd yaad hain... par jo usne Kaikeyi ke baare mein kaha tha, wo ab yaad nahi aa raha.”

Sumantra ne turant apni galti chhupai, taki Kaushalya maa ka dukh aur na badhe. Phir unhone pyar se kaha,
“Hey Devi, Janaki ka chehra safar ki thakan, dhoop, ya jungle ke pashuon (animals) ke dar se bilkul nahi badla. Uske pairon se laal alta (red dye) mita gaya hai, lekin wo ab bhi kamal (lotus) jaise hi khoobsurat lagte hain. Wo apne ghunghru (anklets) pehne khushi-khushi chalti hai, uski chal dekhkar to hans (swans) bhi sharmayein!”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
“Shri Rama ki shakti par bharosa karke, Sita ko sher ya bagh dekhkar bhi koi dar nahi lagta. Hey Devi, aapko na to Raja ke liye, na Rama, Lakshman, ya Sita ke liye chinta karni chahiye. Shri Rama ne apne pita ka aadesh (command) maan kar jo vanvaas (exile) liya hai, wo poori duniya ke liye ek adarsh (inspiration) banega, jab tak suraj aur chand rahenge.”

“Rama ne apna dukh tyag diya hai, aur ab wo rishiyon (sages) ke raste par chal rahe hain — sirf phal aur jangal ke fal-bhoot khakar. Wo apne pita ka vachan pura kar rahe hain.”

Sumantra ke itne kehne par bhi Rani Kaushalya ka mann shaant nahi hua. Unke aankhon se aansu behte rahe, aur wo rote hue kehti rahi —
“Hey mere lal! Hey mere putra! Hey Rama!”

Aur unka dukh poore mahal mein goonj utha.
        """
        create_image_text_layout("attached_assets/chapter2/2.60.2.jpg", text3, layout="side", image_position="right")

    # Chapter61
    with st.expander("Chapter 2.61 - Kaushalya gets angry at the king"):

        text1 = """
Shri Rama — jo sada dharm (righteousness) ka palan karte the — jab van ko chale gaye, to Rani Kaushalya ka dil toot gaya. Aansu unki aankhon se ruk hi nahi rahe the. Dukh bhari aawaaz mein unhone Raja Dasharatha se kaha:

“Hey Maharaj, aapka naam teenon lokon (heaven, earth, underworld) mein bada aur pavitra (pure) mana jata hai. Aap dayaalu (kind), daanveer (charitable) aur komal vachana (gentle-spoken) ke roop mein jane jaate hain. Phir batayiye, aapke do bete — jo sada sukh aur aaram mein pale — ab Sita ke saath van ki kathin (difficult) zindagi kaise jhelenge?”

“Wo komal (delicate) Sita, jo hamesha sukh mein rahi, wo jungle ki garmi aur thand kaise sahegi? Jisne hamesha rasoi ke kushal rasoiyon (skilled cooks) ka bana bhojan khaya, wo van ke jangal ke daale aur jangli daal (wild lentils) kaise khayegi? Jisne hamesha madhur sangeet (sweet music) suna, wo ab sher aur baghon ke dahad (roar) kaise sune?”
        """
        create_image_text_layout("attached_assets/chapter2/2.61.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“Wo dono Rajkumar — Rama aur Lakshmana — jin ke baahu indradhanush (rainbow) jaise majboot aur sundar hain, ab zameen par sir apne haath par rakhkar kaise soyenge? Hey Raja, kab fir main Rama ka wo padma jaisa chehra (lotus-like face) dekh paungi, jiske baal badal ki jaisi sundar laten (locks) hain, jinki aankhen kamal (lotus) jaisi aur saans sugandhit (fragrant) hai?”

“Mujhe lagta hai mera hriday (heart) pathar (stone) se bhi kathor (hard) hai, tabhi to Rama ke bina toot kar bikhar nahi gaya. Hey Raja, aapne apne bachchon ko van bhej kar bahut nirmam (cruel) kaam kiya hai. Jo sukh ke yogya (worthy) the, wo ab bina disha (aimless) ke van mein bhatak rahe hain.”

“Aur batao, agar Rama chaudah saal baad wapas aayega, to kya Bharat sach mein rajya (kingdom) aur dhan usse wapas karega? Mujhe to shak (doubt) hai! Jaise yagna (sacrifice) mein agar pehle apne gareeb rishtedaaron ko khilaya jaaye aur baad mein brahmanon (priests) ko, to wo bhojan svikaar (accept) nahi karte — waise hi Rama bhi doosre ke upbhog (used) kiya hua rajya nahi lega.”

“Ek sher (lion) doosre ke maara hua shikar nahi khata. Waise hi Rama bhi Bharat ke bhoga hua rajya nahi le sakta. Jaise yagya mein ghee, kush (holy grass), aur stambh (pillars) ek baar use hote hain aur dobara nahi, waise hi Rama bhi us rajya ko nahi sweekarega jo uske bina chalaya gaya ho.”

“Rama apmaan (insult) bardasht nahi kar sakta — jaise sher apni poonch pakadna bardasht nahi karta. Kya sabhi log usse yudh (battlefield) mein nahi darte? Wo swayam dharm ka path dikhata hai, wo kabhi zabardasti rajya nahi lega. Agar chahe to apne teer (arrows) se samundar sukhakar sab kuch nasht (destroy) kar de — par wo aisa kabhi nahi karega.”

“Hey Raja, agar aapne dharm shastra (sacred laws) aur rishi-muni (sages) ke updesh (teachings) ko maana hota, to aapka pavitra putra kabhi vanvaas (exile) nahi jaata.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
“Ek stree (woman) ke liye pehla sahara uska pati hota hai, doosra uska putra (son), teesra uske sambandhi (relatives). Par chautha koi nahi! Aapne mujhe patni ke roop mein tyag diya, mere putra Rama ko van bhej diya, aur mujhe uske saath jaane se bhi roka. Hey Maharaj, aapne mujhe poori tarah barbaad kar diya!”

“Aapne apne mantriyon, prajaa (people), aur poore rajya ko dukh ke samundar mein doobha diya. Aaj main, mera putra, aur poori Ayodhya — sab kuch vinash (ruin) ho gaya hai.”

Itna kehkar Rani Kaushalya vilap (weeping loudly) karne lagi. Raja Dasharatha ne unke ye kathin (bitter) shabd sune, to unka hriday dukh se bhar gaya.
Wo sochne lage apne kiye hue paap (sins) ke baare mein, aur shok (grief) ke samundar mein doobkar behosh (fainted) ho gaye.
        """
        create_image_text_layout("attached_assets/chapter2/2.61.2.jpg", text3, layout="side", image_position="right")

    # Chapter62
    with st.expander("Chapter 2.62 - The king is weak and full of sorrow"):

        text1 = """
Rani Kaushalya ke kathin (harsh) shabdon ko sunkar Raja Dasharatha ka mann to bilkul toot gaya.
Wo andar se hil gaye, aur unka sharir kampne laga. Kuch der baad jab unhe hosh aaya, to unhone gehri saans li aur apne purane paap (sin) ko yaad kiya — wo bhayanak ghatna jab unhone jungle mein galti se ek jawan tapasvi (young ascetic) ko apne shabd-vedhi baan (sound-seeking arrow) se maar diya tha.

Ab Raja Dasharatha ke mann mein do bade dukh the —
ek purana paap ka bojh,
aur doosra Rama ke vanvaas (exile) ka dard.

Unka sir jhuka hua tha, aankhen aansuon se bhari thi. Dheere se unhone Rani Kaushalya se kaha:
        """
        create_image_text_layout("attached_assets/chapter2/2.62.1.jpg", text1, layout="side", image_position="left")


        text2 = """
“Hey Kaushalya, tum to hamesha dushmanon (enemies) par bhi daya (compassion) karti ho.
Main haath jod kar tumse prarthana karta hoon — mujhe nafrat (hatred) bhari nazar se mat dekho.
Stri ke liye pati hamesha devata (god) hota hai — chahe wo punya (virtuous) kare ya paap (sin).
Tum gyaani (wise) ho, dharm aur adharma (right and wrong) dono samajhti ho.
Aise kathor (wounding) shabd tumhe nahi kehne chahiye the.”

Yeh sunte hi Rani Kaushalya ke aansu barish ki boondon ki tarah girne lage.
Unhone Raja Dasharatha ke haath apne haath mein pakad liye aur kaha:

“Hey Maharaj, aap dukh mat kijiye, shaant ho jaaiye.
Dekhiye, main apna sir aapke charanon (feet) mein rakh kar maafi maangti hoon.
Mujhse galti ho gayi, main shabd samhal nahi paayi.
Ek achhi stree kabhi yeh nahi chahti ki uska pati use haath jod kar manaye — yeh to uske liye mrityu (death) samaan hota hai.
Main jaanti hoon patni ka kartavya (duty) kya hota hai, aur main yeh bhi jaanti hoon ki aap dharm ke premi (lover of virtue) hain.”

“Maine jo kaha, wo mere bete ke dukh mein anjaane mein nikal gaya.
Dukh (grief) sabr (patience) ko tod deta hai, sochne ki shakti (understanding) ko chheen leta hai — dukh se bada koi shatru (enemy) nahi.
Kisi ajnabi ke vaar (attack) ka dard seh sakte hain, par apne dukh ka bojh nahi.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
“Bas paanch raat hi to hui hain Rama ke van jaane ki —
par mujhe lagta hai jaise paanch saal beet gaye ho!
Dukh ne meri sab khushiyan chheen li hain,
aur har pal mera mann Rama ki yaadon se hil jaata hai —
jaise tez dhara (swift current) samundar ke paani ko hila deti hai.”

Jab Rani Kaushalya ye sab keh rahi thi, tab tak suraj dhal chuka tha aur raat ho gayi thi.
Unke sambhalne wale shabdon (consoling words) ko sunkar Raja Dasharatha ka mann thoda shaant hua.
Par dukh aur thakan (weariness) se thake hue Raja kuch der baad neend mein chale gye…
wo neend, jisse phir kabhi wo jaage nahi. 🌙
        """
        create_image_text_layout("attached_assets/chapter2/2.62.2.jpg", text3, layout="side", image_position="right")

    # Chapter63
    with st.expander("Chapter 2.63 - The king remembers an old mistake he made"):

        text1 = """
Raja Dasharatha bahut der tak be-hosh pade rahe. Jab hosh aaya, unka mann dukh se bhar gaya. Unhone sochne ki koshish ki, par dukh ke bojh se unka mann andhera ho gaya tha. Wo Indra ke samaan shaktishaali the, par ab maut (death) unke kareeb mehsoos ho rahi thi — jaise Rahu sooraj ko nigal leta hai.

Rama ke vanvaas (exile) ke chhatthe din, raja ko apni ek purani bhool yaad aayi — ek paap (sin) jo ab unke dukh ka kaaran bana. Bahut pashchatap (regret) ke saath unhone Rani Kaushalya se kaha:

“Hey Kalyani (auspicious one), duniya mein jo bhi karm (actions) insaan karta hai — chahe wo acha ho ya bura — uska phal (result) usse zarur milta hai. Jo apne karmon ka soch-vichar kiye bina kaam karta hai, wo nishchit roop se agyaan (ignorant) hota hai.

Jaise koi aadmi palasha (a red-flowered tree) ke laal phool dekhkar uske paas wale aam ke ped ko kaat deta hai, par baad mein aam khane ki ichha karta hai — to jab palasha phal deta hai, usse aam nahi milta. Waise hi maine bhi apna sukh khud kaat diya. Rama ko vanvaas bhejna meri sabse badi bhool thi.”
        """
        create_image_text_layout("attached_assets/chapter2/2.63.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Phir raja bole, “Jawani ke dinon mein, ek din mujhe dhanurvidya (archery) mein mahir banna tha. Tab maine ek bhayanak (terrible) galti ki — maine shabd se nishana lagaya aur ek nirdosh (innocent) tapasvi (ascetic) putra ko maar diya. Us din ke paap ka phal aaj main bhugat raha hoon. Jaise ek bachcha anjaane mein vish (poison) pee leta hai, waise hi maine apni khushi ko apne haath se mita diya.”

Raja ne apni kahani Kaushalya ko batani shuru ki:

“Us samay barsaat ka mausam aane wala tha. Suraj tez chamak raha tha, zameen sukhi thi, aur badal dheere-dheere asmaan mein chha rahe the. Maine apna dhanush (bow) aur baan (arrow) liya aur shikar ke liye Sarayu nadi ke kinare gaya.

Wahan raat ke samay, andhere mein maine ek awaaz suni — jaise koi ghada (pitcher) paani se bhar raha ho. Mujhe laga wo hathi hai, to maine apne tarquash (quiver) se ek zeher (poison) laga teer nikaala aur awaaz ki disha mein chhoda.

Par turant hi mujhe ek dard bhari cheekh (cry) suni. Ek naujawan chillaya — ‘Mujhe kisne maara? Main ek tapasvi ka beta hoon, jo fal aur mool (roots) par jeeta hoon. Maine kisi ka kuch nahi bigaada! Mera kya kasoor tha?’”

Wo ladka apne antim (last) shabdon mein bola —

“Main mar jaunga, par mere budhe maa-baap ka kya hoga? Wo dono andhe (blind) hain, kamzor hain, aur sirf mujhe sahara (support) maante hain. Mera marna unke liye maut ke barabar hai.”

Raja Dasharatha ka dil dukh se bhar gaya. Unke haath se dhanush gir gaya. Wo turant us naujawan ke paas gaye. Uska shareer khoon aur mitti se bhara tha, aur wo zameen par pada tha. Usne raja ko dekha aur kaha:

“Rajan (O King), maine tumhara kya bigaada tha? Main to sirf apne andhe maa-baap ke liye paani lene aaya tha. Tumne mujhe maar kar unhe bhi maar diya. Ab jao, mere pita (father) ke paas jaakar unhe sach batao, nahi to wo tumhe shraap (curse) denge. Mera baan nikaal do — yeh mujhe bahut kasht (pain) de raha hai.”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Raja ne socha, agar baan nikala to wo mar jaayega, aur agar rehne diya to wo peeda (pain) mein rahega. Tab us tapasvi ke putra ne kaha:

“Rajan, ghabrao mat. Tumne koi brahman (priest) ko nahi maara. Main ek shudra maa aur vaishya pita ka beta hoon. Tumhara paap bhale hi bada hai, par tumne dharm (righteous law) ke viruddh brahm-hatya nahi ki.”

Phir usne antimsans (last breath) lete hue apni aankhen bandh kar li aur praan (life) chhod diye.

Raja Dasharatha ne Kaushalya se kaha,

“Hey Devi, us samay main us bachche ke shareer ko dekh kar toot gaya tha. Uski mrityu (death) ne meri aatma ko hila diya. Us din jo dukh maine dekha, wahi dukh aaj mujhe Rama ke door hone par mehsoos ho raha hai.”
        """
        create_image_text_layout("attached_assets/chapter2/2.63.2.jpg", text3, layout="side", image_position="right")

    # Chapter64
    with st.expander("Chapter 2.64 - Dasaratha dies with Rama’s name on his lips"):

        text1 = """
Raja Dasharatha apne bete Shri Rama ke virah (separation) mein dukh se toot chuke the. Unhone Rani Kaushalya ko apni purani galti yaad karte hue bataya — ek samay unhone galti se ek jawan tapasvi (young ascetic) ko maar diya tha.

Dasharatha ne kaha, “Hey Kaushalya, kabhi main van mein shikar kar raha tha. Mujhe laga maine haathi ya sher ki aawaaz suni hai, aur main ne apne teer se us disha mein nishana lagaya. Par jab main wahan pahucha, to dekha — ek tapasvi ladka paani bharne gaya tha, aur mera teer uske hriday (heart) mein lag gaya. Wo dharmik ladka dard se karah raha tha, aur marne se pehle bola — ‘Mere andhe maa-baap meri raah dekh rahe honge.’ Main bahut pachtaya, aur uske maa-baap ke paas gaya, unse maafi maangi.”
        """
        create_image_text_layout("attached_assets/chapter2/2.64.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Raja Dasharatha ne bataya ki wo budhe pitaji aur maa bahut dukhi hue. Unhone kaha, “Raja, tune hamara beta chheen liya. Jis tarah tu ne hamara dukh diya hai, waisa hi dukh tujhe bhi apne bete ke virah se milega.”
Aur fir dono tapasvi pitaji-maata ne agni mein pravesh karke apna praan tyag diya.

Raja Dasharatha bole, “Hey Kaushalya, ab mujhe samajh aaya — us rishi (sage) ka shraap (curse) ab sach ho raha hai. Main bhi apne bete ke virah se hi mar raha hoon.”

Unka shareer kamzor ho gaya tha, aankhon ke samne andhera chha gaya. Unhone kaha, “Hey Kaushalya, main apne Ram ko dekh nahi pa raha. Kaash wo ek baar mujhe chhu leta, to main fir se jeevit ho jata. Mujhe lagta hai Yama ke dhoot (messengers of death) mujhe bula rahe hain. Hey Sumitra, meri Kaushalya, main ja raha hoon… Hey Kaikeyi, tune mere vansh (family) ki shanti tod di…”
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
Aise rote hue, apne Ram ke virah mein tadap kar, Raja Dasharatha ne raat ke beech apna praan de diya.

Mukhya bhaav (main message):
Dasharatha ka dukh unke purane paap ka phal tha. Jaise unhone ek pita ko bete ke virah ka dukh diya tha, waisa hi dukh unhe bhi mila. Par unki mrityu (death) ek pita ke dil se hui — jo apne Ram ke bina jeena nahi chahata tha. 💔
        """
        create_image_text_layout("attached_assets/chapter2/2.64.2.jpg", text3, layout="side", image_position="right")

    # Chapter65
    with st.expander("Chapter 2.65 - The palace fills with crying and sadness"):

        text1 = """
Subah hone par, raja ke mahal mein pehle jaise hi parampara (tradition) ke anusar geet-sangeet shuru hua. Rajgayak (royal singers), veer geet (heroic songs) gawanewale aur sangeet mein nipun (skilled) kalakar aaye. Unhone raja Dasharatha ke gunon aur veerata (bravery) ka gaan (praise) shuru kiya. Unki madhur awaaz mahal ke har kone mein gunj uthi.

Bahaar pedon par baithay pakshi (birds) aur pinjron mein band toote hue pankh wale parinde bhi gaane lage. Vina (a string instrument) ki dhun, brahmanon ke shubh mantron (holy chants), aur rajkavi (court poets) ke geeton ki goonj milkar mahal ko jeevit sa bana rahi thi.

Raj seva mein lage naukar aur eunuchs (royal attendants) sab apne apne kaam mein tayyar the — kisi ke haath mein sugandhit (fragrant) paani ke sunehre ghade the, koi tel, lep (ointment), aaine (mirrors), kangi aur kapde lekar khada tha. Sab soch rahe the, “Raja ab tak uthe kyun nahi?”
        """
        create_image_text_layout("attached_assets/chapter2/2.65.1.jpg", text1, layout="side", image_position="left")


        text2 = """
Jab suraj nikal aaya, sabne aapas mein kaha —

“Ajeeb baat hai, raja ab tak jaage nahi?”

Phir raja ke paas jaane wali kuch dasiyan (maidservants) — Kaushalya ke alawa — andar gayin, jaise wo roz jaati thi. Unhone pyar aur sambhal ke saath raja ka sharir (body) chhua… par kuch mehsoos nahi hua. Na koi saans (breath), na koi dhadkan (heartbeat).

Unke haath kaanpte hue peeche hat gaye. Wo samajh gayin — Raja Dasharatha ab nahi rahe. Unka sharir thanda tha, jaise jeevan ka prakash (light of life) bujh gaya ho.

Wo mahilayein kampne lagi, jaise hawa mein hilta hua nargis (reed) ka ghaas. Dheere-dheere sach samajh mein aaya — unka raja chala gaya.

Mahal mein ro-ne ki aawaz gunjne lagi. Rani Kaushalya aur Rani Sumitra, jo pehle se hi Rama aur Lakshmana ke vanvaas ke dukh se tuti hui thi, ab be-hosh (unconscious) pad gayin. Unke chehre pehla sa tej (radiance) kho chuka tha. Wo do sitaron (stars) ki tarah lag rahi thi — jo badalon ke peeche chhup gaye ho.

Jab dasiyon ne dekha ki dono ranian behosh hain aur raja nishpran (lifeless) padhe hain, to wo zor zor se rote hue chillane lagi. Unki cheekhon (cries) ne mahal ko hila diya.

Unki aawaz sun kar Rani Kaushalya aur Sumitra hosh mein aayin. Dono ne raja ka thanda sharir chhua, aur ro kar bole —
        """
        create_image_text_layout(text_content=text2, layout="full")

        text3 = """
“Hey Swami (my lord)! Hey Maharaj!”

Kaushalya zameen par gir gayin, unka sharir mitti se dhak gaya — wo aise lag rahi thi jaise aasman se koi tara (star) toot kar zameen par aa gira ho.

Baaki ranian, samet (including) Rani Kaikeyi, bhi dukh se be-hosh ho gayin. Mahal ke andar aur bahar, sab taraf ro-na, cheekhna, aur karuna (sorrow) ki goonj thi.

Poora rajmahal ab utsav (celebration) ka nahi, shok (mourning) ka ghar ban gaya tha. Har kone mein aansuon aur dukh ka samundar tha. Raniyan raja ke shareer se chipak kar rote hue keh rahi thi —

“Hey Maharaj, humse door kyun chale gaye? Humein akela kyun chhod diya?”

Mahal bhar gaya tha unke dukh bhare swaron (sounds of sorrow) se — jaise poori Ayodhya ro rahi ho.
        """
        create_image_text_layout("attached_assets/chapter2/2.65.2.jpg", text3, layout="side", image_position="right")
