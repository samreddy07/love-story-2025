import streamlit as st
import datetime
import time
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Our Love Story ❤️", layout="wide")

# ---------- PASSWORD ----------

def check_password():

    def password_entered():
        if st.session_state["password"] == "ourlove2025":
            st.session_state["password_correct"] = True
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:

        st.title("🔒 Private Love Website")

        st.text_input(
            "Enter our secret password ❤️",
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


# ---------- INTRO SCREEN ----------

def intro():

    if "intro" not in st.session_state:
        st.session_state.intro = False

    if not st.session_state.intro:

        st.markdown("""
        <style>

        .intro{
        height:100vh;
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
        background:linear-gradient(135deg,#ff758c,#ff7eb3);
        color:white;
        text-align:center;
        font-family:cursive;
        }

        .intro h1{
        font-size:80px;
        }

        .intro p{
        font-size:28px;
        }

        </style>

        <div class="intro">
        <h1>Our Love Story ❤️</h1>
        <p>2025 – The Most Beautiful Year</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Enter Our Story 💕"):
            st.session_state.intro = True
            st.rerun()

        st.stop()


# ---------- CSS ----------

def load_css():

    st.markdown("""
    <style>

    .stApp{
    background:linear-gradient(135deg,#ff9a9e,#fad0c4);
    }

    .title{
    text-align:center;
    font-size:60px;
    color:white;
    font-family:cursive;
    }

    .subtitle{
    text-align:center;
    color:white;
    font-size:24px;
    margin-bottom:40px;
    }

    .card{
    background:rgba(255,255,255,0.4);
    padding:25px;
    border-radius:20px;
    margin:25px 0;
    backdrop-filter:blur(10px);
    box-shadow:0 10px 30px rgba(0,0,0,0.2);
    }

    .love{
    background:white;
    padding:40px;
    border-radius:20px;
    font-size:20px;
    line-height:1.8;
    }

    </style>
    """, unsafe_allow_html=True)


# ---------- MEMORIES ----------

def get_memories():

    return [

{"title":"First Time We Met","date":"31 Dec 2024",
"description":"We met during New Year celebrations. I still remember thinking how beautiful you looked.",
"image":"photos/photo1.jpg"},

{"title":"First Date","date":"8 Feb 2025",
"description":"Our first date at Ironhill where we talked about life and dreams.",
"image":"photos/photo2.jpg"},

{"title":"You Proposed","date":"12 Apr 2025",
"description":"You proposed to me and that night felt peaceful.",
"image":"photos/photo3.jpg"},

{"title":"First Kiss","date":"1 May 2025",
"description":"Our first kiss and favourite Meghana biryani day.",
"image":"photos/photo4.jpg"},

{"title":"Kodaikanal Trip","date":"16 May 2025",
"description":"Exploring Guna caves together.",
"image":"photos/photo5.jpg"},

{"title":"Birthday Pondy","date":"19 May 2025",
"description":"Celebrating my birthday with you.",
"image":"photos/photo6.jpg"},

{"title":"Sakleshpur Trip","date":"30 Aug 2025",
"description":"One of our best trips together.",
"image":"photos/photo7.jpg"},

{"title":"Goa Trip","date":"12-15 Dec 2025",
"description":"Reels, drinks and laughter.",
"image":"photos/photo8.jpg"},

{"title":"End Of 2025","date":"31 Dec 2025",
"description":"Ending the best year together.",
"image":"photos/photo9.jpg"}

]


# ---------- MAIN ----------

def main():

    load_css()

    intro()

    st.markdown("<div class='title'>Our Love Story ❤️</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>2025 – The Best Year Of My Life</div>", unsafe_allow_html=True)

    # relationship counter

    start = datetime.date(2024,12,31)
    today = datetime.date.today()

    st.metric("Days Together ❤️",(today-start).days)

    # photo slider

    st.header("📸 Our Beautiful Moments")

    photos = list(Path("photos").glob("*"))

    if photos:

        idx = st.slider("Slide through memories ❤️",0,len(photos)-1,0)

        img = Image.open(photos[idx])
        st.image(img,use_container_width=True)

        if st.button("▶ Auto Play Memories"):

            for p in photos:
                image = Image.open(p)
                st.image(image,use_container_width=True)
                time.sleep(2)

    # memories section

    st.header("❤️ Our Memories")

    memories = get_memories()

    for m in memories:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        col1,col2 = st.columns([1,1])

        with col1:

            if Path(m["image"]).exists():
                img = Image.open(m["image"])
                st.image(img,use_container_width=True)

        with col2:

            st.subheader(m["title"])
            st.write("📅",m["date"])
            st.write(m["description"])

        st.markdown("</div>", unsafe_allow_html=True)

    # love letter

    if st.button("💌 Open Love Letter"):

        st.balloons()

        st.markdown("""
        <div class='love'>

        My Love ❤️

        Looking back at 2025, I realize something very special happened in my life.

        I met you.

        Our trips, conversations, laughs and even our small fights
        made this the most beautiful year of my life.

        Thank you for being part of my story.

        Forever yours ❤️

        </div>
        """, unsafe_allow_html=True)


if check_password():
    main()
