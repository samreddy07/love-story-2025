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

    return [

        {
        "title":"First Time We Met",
        "date":"31 Dec 2024",
        "description":"We met in the mall during New Year celebrations. I instantly liked you and felt something special.",
        "image":"photos/photo1.jpg"
        },

        {
        "title":"First Date",
        "date":"8 Feb 2025",
        "description":"Our first date at Ironhill. We talked for hours about life, dreams and everything.",
        "image":"photos/photo2.jpg"
        },

        {
        "title":"First Kiss",
        "date":"1 May 2025",
        "description":"Our first kiss and Meghana biryani day ❤️",
        "image":"photos/photo3.jpg"
        },

        {
        "title":"Kodaikanal Trip",
        "date":"16 May 2025",
        "description":"Exploring Guna caves together.",
        "image":"photos/photo4.jpg"
        },

        {
        "title":"Goa Trip",
        "date":"Dec 2025",
        "description":"Reels, drinks and lots of laughter.",
        "image":"photos/photo5.jpg"
        }

    ]


# ---------- MAIN ----------
def main():

    load_css()

    st.markdown("<div class='title'>Our Love Story ❤️</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>2025 — The Best Year Of My Life</div>", unsafe_allow_html=True)

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
