import streamlit as st
import datetime
import time
import base64
from pathlib import Path
from PIL import Image
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Our Love Story ❤️", layout="wide")

# ---------------- PASSWORD ----------------

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

        st.error("Wrong password 💔 Try again")

        st.text_input(
            "Enter password",
            type="password",
            on_change=password_entered,
            key="password"
        )

        return False

    else:
        return True


# ---------------- INTRO SCREEN ----------------

def intro_screen():

    if "intro_shown" not in st.session_state:
        st.session_state.intro_shown = False

    if not st.session_state.intro_shown:

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
            st.session_state.intro_shown = True
            st.rerun()

        st.stop()


# ---------------- CSS ----------------

def load_css():

    st.markdown("""
    <style>

    .stApp{
    background:linear-gradient(135deg,#ff758c,#ff7eb3,#fad0c4);
    }

    .title{
    font-size:60px;
    text-align:center;
    color:white;
    font-family:cursive;
    }

    .subtitle{
    text-align:center;
    font-size:24px;
    color:white;
    margin-bottom:40px;
    }

    .card{
    background:rgba(255,255,255,0.35);
    padding:25px;
    border-radius:20px;
    margin:25px 0;
    backdrop-filter:blur(15px);
    box-shadow:0 10px 30px rgba(0,0,0,0.2);
    }

    .timeline{
    background:white;
    padding:15px;
    border-radius:12px;
    margin-bottom:10px;
    }

    .love-letter{
    background:white;
    padding:40px;
    border-radius:20px;
    font-size:20px;
    line-height:1.8;
    }

    </style>
    """, unsafe_allow_html=True)


# ---------------- MEMORIES ----------------

def get_memories():

    return [

{"title":"First Time We Met","date":"31 Dec 2024",
"description":"We met during New Year celebrations in the mall. I still remember how beautiful and confident you looked.",
"image":"photos/photo1.jpg"},

{"title":"First Date","date":"8 Feb 2025",
"description":"Our first date at Ironhill where we talked about life and dreams.",
"image":"photos/photo2.jpg"},

{"title":"You Proposed","date":"12 Apr 2025",
"description":"You proposed to me on Snapchat and that night felt so peaceful.",
"image":"photos/photo3.jpg"},

{"title":"First Kiss","date":"1 May 2025",
"description":"Our first kiss and our favourite Meghana biryani day.",
"image":"photos/photo4.jpg"},

{"title":"Kodaikanal Trip","date":"16 May 2025",
"description":"Exploring Guna caves together.",
"image":"photos/photo5.jpg"},

{"title":"Birthday Pondicherry","date":"19 May 2025",
"description":"Celebrating my birthday with you.",
"image":"photos/photo6.jpg"},

{"title":"Your Birthday","date":"21 May 2025",
"description":"We fought but later fixed everything and enjoyed the night.",
"image":"photos/photo7.jpg"},

{"title":"Office Outing","date":"25 Jun 2025",
"description":"Even when I was upset you made me smile.",
"image":"photos/photo8.jpg"},

{"title":"Temple Visit","date":"28 Jun 2025",
"description":"Praying together in Anantapur temple.",
"image":"photos/photo9.jpg"},

{"title":"Long Drive","date":"29 Jun 2025",
"description":"A peaceful drive and beautiful memories.",
"image":"photos/photo10.jpg"},

{"title":"ABV Restobar","date":"12 Jul 2025",
"description":"You wore a red dress and I fell for you again.",
"image":"photos/photo11.jpg"},

{"title":"HP Wedding","date":"16 Aug 2025",
"description":"Attending a wedding together felt special.",
"image":"photos/photo12.jpg"},

{"title":"Sakleshpur Trip","date":"30 Aug 2025",
"description":"One of our best trips.",
"image":"photos/photo13.jpg"},

{"title":"Ironhill Again","date":"12 Sep 2025",
"description":"Talking for hours together.",
"image":"photos/photo14.jpg"},

{"title":"Tirumala Temple","date":"15 Nov 2025",
"description":"Praying for our future.",
"image":"photos/photo15.jpg"},

{"title":"Office Memory","date":"18 Nov 2025",
"description":"One of our favourite photos.",
"image":"photos/photo16.jpg"},

{"title":"First Flight","date":"11 Dec 2025",
"description":"Your first flight experience.",
"image":"photos/photo17.jpg"},

{"title":"Goa Trip","date":"12-15 Dec 2025",
"description":"Reels, drinks and laughter.",
"image":"photos/photo18.jpg"},

{"title":"End Of Year","date":"31 Dec 2025",
"description":"Ending the best year together.",
"image":"photos/photo19.jpg"}

]


# ---------------- MAIN ----------------

def main():

    load_css()

    intro_screen()

    st.markdown("<div class='title'>Our Love Story ❤️</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>2025 – The Best Year Of My Life</div>", unsafe_allow_html=True)

    # relationship counter
    start_date = datetime.date(2024,12,31)
    today = datetime.date.today()
    st.metric("Days Together ❤️",(today-start_date).days)

    # cinematic slider
    st.header("📸 Our Beautiful Moments")

    photos = list(Path("photos").glob("*"))

    slider_index = st.slider("Slide through memories ❤️",0,len(photos)-1,0)

    img = Image.open(photos[slider_index])
    st.image(img,use_container_width=True)

    if st.button("▶ Auto Play Memories"):

        for p in photos:

            image = Image.open(p)
            st.image(image,use_container_width=True)
            time.sleep(2)

    # memories
    st.header("❤️ Our Memories")

    memories = get_memories()

    for m in memories:

        st.markdown("<div class='card'>",unsafe_allow_html=True)

        col1,col2 = st.columns([1,1])

        with col1:

            if Path(m["image"]).exists():
                img = Image.open(m["image"])
                st.image(img,use_container_width=True)

        with col2:

            st.subheader(m["title"])
            st.write("📅",m["date"])
            st.write(m["description"])

        st.markdown("</div>",unsafe_allow_html=True)

    # timeline
    st.header("❤️ Our Journey")

    timeline=[

("31 Dec 2024","We met ❤️"),
("8 Feb 2025","First date"),
("12 Apr 2025","You proposed"),
("1 May 2025","First kiss"),
("16 May 2025","Kodaikanal trip"),
("19 May 2025","Birthday trip"),
("30 Aug 2025","Sakleshpur trip"),
("12-15 Dec 2025","Goa trip"),
("31 Dec 2025","Best year ended together")

]

    for date,event in timeline:

        st.markdown(
        f"<div class='timeline'><b>{date}</b> — {event}</div>",
        unsafe_allow_html=True
        )

    # map
    st.header("🌍 Places We Explored")

    m = folium.Map(location=[12.97,77.59],zoom_start=5)

    folium.Marker([12.97,77.59],tooltip="Bangalore").add_to(m)
    folium.Marker([10.23,77.48],tooltip="Kodaikanal").add_to(m)
    folium.Marker([15.29,74.12],tooltip="Goa").add_to(m)
    folium.Marker([11.93,79.83],tooltip="Pondicherry").add_to(m)

    st_folium(m,width=700,height=500)

    # love letter
    if st.button("💌 Open Love Letter"):

        st.balloons()

        st.markdown("""
<div class='love-letter'>

My Love ❤️

Looking back at 2025, I realize something very special happened in my life.

I met **you**.

Our conversations, trips, silly fights, long drives and laughs
made this the most beautiful year of my life.

No matter what happens in the future,
meeting you will always be one of the best things that ever happened to me.

Forever yours ❤️

</div>
""",unsafe_allow_html=True)



if check_password():
    main()
