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

