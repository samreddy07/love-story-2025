import streamlit as st
import datetime
from pathlib import Path
from PIL import Image
import base64
import time
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Our Love Story ❤️",layout="wide")

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
            key="password",
        )

        return False

    elif not st.session_state["password_correct"]:

        st.error("Wrong password 💔 Try again")
        st.text_input(
            "Enter password",
            type="password",
            on_change=password_entered,
            key="password",
        )
        return False

    else:
        return True


# ---------------- CSS ----------------

def load_css():

    st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#ff758c,#ff7eb3,#fad0c4);
}

/* floating hearts */

.hearts{
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
pointer-events:none;
background-image:url("https://i.imgur.com/Y8z7FhG.png");
animation:heartsMove 20s linear infinite;
opacity:0.15;
}

@keyframes heartsMove{
0%{background-position:0 0;}
100%{background-position:0 1000px;}
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

<div class="hearts"></div>

""",unsafe_allow_html=True)



# ---------------- MEMORIES ----------------

def get_memories():

    return [

{"title":"First Time We Met","date":"31 Dec 2024",
"description":"We met during New Year celebrations in the mall. I still remember how beautiful and confident you looked.",
"image":"photos/photo1.jpg"},

{"title":"First Date","date":"8 Feb 2025",
"description":"Our first date at Ironhill where we talked about life, dreams and everything.",
"image":"photos/photo2.jpg"},

{"title":"You Proposed","date":"12 Apr 2025",
"description":"You proposed to me on Snapchat and that night I felt so peaceful knowing someone cares so much.",
"image":"photos/photo3.jpg"},

{"title":"First Kiss","date":"1 May 2025",
"description":"A day full of emotions and our favourite Meghana biryani.",
"image":"photos/photo4.jpg"},

{"title":"Kodaikanal Trip","date":"16 May 2025",
"description":"Exploring Guna caves and enjoying the cool weather together.",
"image":"photos/photo5.jpg"},

{"title":"My Birthday Pondy","date":"19 May 2025",
"description":"Celebrating my birthday in Pondicherry with you made it unforgettable.",
"image":"photos/photo6.jpg"},

{"title":"Your Birthday","date":"21 May 2025",
"description":"We fought but later fixed everything and enjoyed the night together.",
"image":"photos/photo7.jpg"},

{"title":"Office Outing NUSA","date":"25 Jun 2025",
"description":"Even when I was upset you made my mood better.",
"image":"photos/photo8.jpg"},

{"title":"Temple Visit","date":"28 Jun 2025",
"description":"We prayed together at Anantapur temple.",
"image":"photos/photo9.jpg"},

{"title":"Long Drive","date":"29 Jun 2025",
"description":"A beautiful drive and sweet memories.",
"image":"photos/photo10.jpg"},

{"title":"ABV Restobar","date":"12 Jul 2025",
"description":"You wore a red dress and I fell for you again.",
"image":"photos/photo11.jpg"},

{"title":"HP Wedding","date":"16 Aug 2025",
"description":"Attending a wedding together felt special.",
"image":"photos/photo12.jpg"},

{"title":"Sakleshpur Trip","date":"30 Aug 2025",
"description":"One of our best trips ever.",
"image":"photos/photo13.jpg"},

{"title":"Ironhill Again","date":"12 Sep 2025",
"description":"Talking for hours and enjoying the night.",
"image":"photos/photo14.jpg"},

{"title":"Tirumala Temple","date":"15 Nov 2025",
"description":"Praying for our future together.",
"image":"photos/photo15.jpg"},

{"title":"Office Memory","date":"18 Nov 2025",
"description":"One of our favourite photos together.",
"image":"photos/photo16.jpg"},

{"title":"First Flight","date":"11 Dec 2025",
"description":"Your first flight experience.",
"image":"photos/photo17.jpg"},

{"title":"Goa Trip","date":"12-15 Dec 2025",
"description":"Reels, drinks, laughter and beautiful nights.",
"image":"photos/photo18.jpg"},

{"title":"End Of 2025","date":"31 Dec 2025",
"description":"Ending the best year of my life with you.",
"image":"photos/photo19.jpg"}

]



# ---------------- MAIN APP ----------------

def main():

    load_css()

    st.markdown("<div class='title'>Our Love Story ❤️</div>",unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>2025 – The Best Year Of My Life</div>",unsafe_allow_html=True)


    # relationship counter

    start_date = datetime.date(2024,12,31)
    today = datetime.date.today()

    st.metric("Days Together ❤️",(today-start_date).days)



    # slideshow

    st.header("📸 Our Favourite Moments")

    photos = list(Path("photos").glob("*"))

    slide = st.empty()

    for img in photos:

        image = Image.open(img)
        slide.image(image,use_container_width=True)

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

    st.header("❤️ Our Journey Timeline")

    timeline = [

("31 Dec 2024","We first met ❤️"),
("8 Feb 2025","Our first date"),
("12 Apr 2025","You proposed"),
("1 May 2025","Our first kiss"),
("16 May 2025","Kodaikanal trip"),
("19 May 2025","Birthday in Pondy"),
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

    st.header("🌍 Places We Explored Together")

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

From the first time we met during the New Year night, everything slowly started becoming beautiful.

Our conversations, our trips, our silly fights, our laughs, our long drives, our memories.

Every moment with you became part of the most beautiful year of my life.

Even when life gets stressful or confusing, knowing that you exist in my world gives me peace.

Thank you for being part of my story.

Forever yours ❤️

</div>
""",unsafe_allow_html=True)



if check_password():
    main()
