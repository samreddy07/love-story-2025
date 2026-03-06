import streamlit as st
import datetime
from PIL import Image
from pathlib import Path
import base64
import time

st.set_page_config(
    page_title="Our Love Story ❤️",
    page_icon="💕",
    layout="wide"
)

# ---------- PASSWORD ----------
def check_password():

    def password_entered():
        if st.session_state["password"] == "ourlove2025":
            st.session_state["password_correct"] = True
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:

        st.title("🔒 Private Love Website")
        st.write("Only for you ❤️")

        st.text_input(
            "Enter our secret password",
            type="password",
            on_change=password_entered,
            key="password"
        )
        return False

    elif not st.session_state["password_correct"]:

        st.error("Wrong password 💔")
        st.text_input(
            "Enter password",
            type="password",
            on_change=password_entered,
            key="password"
        )
        return False

    else:
        return True


# ---------- CSS ----------
def load_css():
    st.markdown("""
<style>

.stApp {
background: linear-gradient(135deg,#ff9a9e,#fad0c4);
}

/* title */

.title{
font-size:70px;
text-align:center;
color:white;
font-family:cursive;
animation:fade 2s ease-in;
}

.subtitle{
text-align:center;
font-size:25px;
color:white;
margin-bottom:40px;
}

/* glass cards */

.card{
background: rgba(255,255,255,0.25);
backdrop-filter: blur(10px);
border-radius:20px;
padding:25px;
margin:20px 0;
color:#333;
box-shadow:0 8px 32px rgba(0,0,0,0.2);
transition:0.3s;
}

.card:hover{
transform:scale(1.03);
}

/* floating hearts */

.hearts{
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
pointer-events:none;
font-size:30px;
animation:hearts 10s linear infinite;
opacity:0.3;
}

@keyframes hearts{
0%{transform:translateY(-100px);}
100%{transform:translateY(100vh);}
}

.gallery img{
border-radius:15px;
transition:0.3s;
}

.gallery img:hover{
transform:scale(1.05);
}

</style>
""", unsafe_allow_html=True)


# ---------- MEMORIES ----------
def get_memories():

    memories = [

        {
        "title":"The Night We First Met",
        "date":"31 Dec 2024 - New Year Night",
        "description":"We met for the first time at the mall during New Year celebrations. I still remember thinking how posh and beautiful you looked. I liked you instantly. That moment felt special, and I felt blessed that our story started on such a beautiful night.",
        "image":"photos/photo1.jpg"
        },

        {
        "title":"Our First Date",
        "date":"8 Feb 2025 - Ironhill Bangalore",
        "description":"Our first official date at Ironhill. This was the day we decided to move our relationship forward. We talked about our past, life experiences, dreams, and future while enjoying crafted beer. Ironhill slowly became our favorite place in Bangalore.",
        "image":"photos/photo2.jpg"
        },

        {
        "title":"You Proposed to Me",
        "date":"12 Apr 2025",
        "description":"You proposed to me on Snapchat. That night I slept peacefully knowing there is someone so lovely and caring in this world who truly wants to take care of me. After my birthday, I happily accepted you in my life.",
        "image":"photos/photo3.jpg"
        },

        {
        "title":"Our First Kiss",
        "date":"1 May 2025",
        "description":"This day will always stay in my heart. We shared our first kiss and spent hours talking about everything. We also enjoyed our favorite Meghana Foods biryani. A simple day but full of love and happiness.",
        "image":"photos/photo4.jpg"
        },

        {
        "title":"Kodaikanal Trip",
        "date":"16 May 2025",
        "description":"One of our most beautiful trips together. We visited the famous Guna caves in Kodaikanal, enjoyed the cool weather, the views, and every moment together. That trip felt magical.",
        "image":"photos/photo5.jpg"
        },

        {
        "title":"My Birthday in Pondicherry",
        "date":"19 May 2025",
        "description":"Celebrating my birthday with you in Pondicherry was unforgettable. We explored the city, walked around, laughed a lot, and created beautiful memories together.",
        "image":"photos/photo6.jpg"
        },

        {
        "title":"Your Birthday Night",
        "date":"21 May 2025",
        "description":"On your birthday we had a small fight and I left you alone after office. But later we sorted everything out and went to Mazie & Malt Restobar. We had beer, good food, talked for hours and ended the day happily.",
        "image":"photos/photo7.jpg"
        },

        {
        "title":"Office Team Outing - NUSA",
        "date":"25 June 2025",
        "description":"During the office outing at NUSA I wasn't in a good mood, but you made everything better. I was a little possessive because you were talking with others. Later we spoke openly and understood each other. That day made me believe we can handle misunderstandings and still move forward together.",
        "image":"photos/photo8.jpg"
        },

        {
        "title":"Temple Visit Together",
        "date":"28 June 2025 - Anantapur",
        "description":"We went together to the temple in Anantapur and later I dropped you at your home in Bellary. Praying together felt peaceful and meaningful.",
        "image":"photos/photo9.jpg"
        },

        {
        "title":"The Long Drive",
        "date":"29 June 2025",
        "description":"We had another small argument earlier that day, but later everything became normal. We had lunch, did some shopping for house opening items and during the long drive we shared a sweet kiss in the back seat of the car.",
        "image":"photos/photo10.jpg"
        },

        {
        "title":"Sweet Home Memory",
        "date":"1 July 2025",
        "description":"A small but very special moment for us. Sometimes the simplest moments together become the sweetest memories.",
        "image":"photos/photo11.jpg"
        },

        {
        "title":"ABV Restobar Night",
        "date":"12 July 2025",
        "description":"We went to ABV Restobar and watched a random movie. You were wearing a red dress that day and honestly I fell for you even more.",
        "image":"photos/photo12.jpg"
        },

        {
        "title":"HP Wedding",
        "date":"16 Aug 2025",
        "description":"We attended HP's marriage together. Watching a wedding together made me imagine our future and it felt really special being there with you.",
        "image":"photos/photo13.jpg"
        },

        {
        "title":"Sakleshpur Trip",
        "date":"30 Aug 2025",
        "description":"One of the best trips we had together. Even though we had a small fight because of my workaholic nature, we still enjoyed the trip, the views, the weather and each other's company.",
        "image":"photos/photo14.jpg"
        },

        {
        "title":"Ironhill Again",
        "date":"12 Sep 2025",
        "description":"We again visited Ironhill for my mama's marriage party. We talked for hours that night and it reminded me how special our conversations always are.",
        "image":"photos/photo15.jpg"
        },

        {
        "title":"Tirumala Temple Visit",
        "date":"15 Nov 2025",
        "description":"We visited Tirumala temple together and prayed for our future. It was a peaceful and meaningful day for both of us.",
        "image":"photos/photo16.jpg"
        },

        {
        "title":"Office Memory",
        "date":"18 Nov 2025",
        "description":"One of our best photos together was taken in the office area. A simple moment but a beautiful memory.",
        "image":"photos/photo17.jpg"
        },

        {
        "title":"First Flight Together",
        "date":"11 Dec 2025",
        "description":"A big milestone moment — the first time you traveled in a flight. Sharing that experience together made it even more special.",
        "image":"photos/photo18.jpg"
        },

        {
        "title":"Goa Trip",
        "date":"12–15 Dec 2025",
        "description":"Our Goa trip was unforgettable. We made reels, drank together, laughed a lot and I still remember the people upstairs in the resort singing loudly the whole night while we laughed watching them.",
        "image":"photos/photo19.jpg"
        },

        {
        "title":"Ending The Year Together",
        "date":"31 Dec 2025",
        "description":"Ending the year together at a restobar party felt perfect. Looking back, 2025 truly became the best year of my life because of you.",
        "image":"photos/photo20.jpg"
        }

    ]

    return memories


# ---------- MAIN ----------
def main():

    load_css()

    st.markdown("<div class='title'>Our Love Story ❤️</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>A year full of trips, fights, kisses, laughter, and unforgettable memories together.</div>", unsafe_allow_html=True)

    # MUSIC
    try:

        audio = open("music/love_song.mp3","rb")
        audio_bytes = audio.read()

        st.markdown(
        f"""
        <audio autoplay loop>
        <source src="data:audio/mp3;base64,{base64.b64encode(audio_bytes).decode()}">
        </audio>
        """,
        unsafe_allow_html=True
        )

    except:
        pass


    # RELATIONSHIP COUNTER

    start_date = datetime.date(2024,12,31)
    today = datetime.date.today()

    days = (today-start_date).days

    st.metric("Days Together ❤️",days)


    tab1,tab2,tab3 = st.tabs(["📸 Memories","🖼 Gallery","💌 Love Letter"])


    # ---------- MEMORIES ----------

    with tab1:

        memories = get_memories()

        for m in memories:

            st.markdown("<div class='card'>",unsafe_allow_html=True)

            col1,col2 = st.columns([1,1])

            with col1:

                if Path(m["image"]).exists():
                    img = Image.open(m["image"])
                    st.image(img,use_container_width=True)

                else:
                    st.info("Add photo: "+m["image"])

            with col2:

                st.subheader(m["title"])
                st.write("📅",m["date"])
                st.write(m["description"])

                if st.button("❤️ I Love This Memory",key=m["title"]):
                    st.balloons()

            st.markdown("</div>",unsafe_allow_html=True)


    # ---------- GALLERY ----------

    with tab2:

        st.subheader("Our Photo Gallery")

        photos = list(Path("photos").glob("*"))

        cols = st.columns(3)

        for i,p in enumerate(photos):

            with cols[i%3]:

                img = Image.open(p)
                st.image(img,use_container_width=True)


    # ---------- LOVE LETTER ----------

    with tab3:

        if st.button("💌 Open Secret Love Letter"):

            st.balloons()

            st.markdown("""
            ## My Love ❤️

            2025 became the best year of my life because of you.

            We laughed together  
            we travelled together  
            we fought and fixed everything together  

            No matter what happens in life  
            you will always be special to me.

            Forever yours ❤️
            """)


    st.markdown("---")

    st.markdown(
    "<center style='color:white;font-size:22px'>Made with ❤️ for the love of my life</center>",
    unsafe_allow_html=True
    )


if check_password():
    main()

