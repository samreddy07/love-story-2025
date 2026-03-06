import streamlit as st
from pathlib import Path
from PIL import Image
import datetime

st.set_page_config(page_title="Our Love Story ❤️", layout="wide")

# ----------- LOVE THEME CSS -----------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&family=Poppins:wght@300;400&display=swap');

.stApp{
background: linear-gradient(135deg,#ff9a9e,#fad0c4,#fad0c4);
font-family:'Poppins',sans-serif;
}

/* floating hearts */

body:before{
content:"❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️";
position:fixed;
top:-50px;
left:0;
width:100%;
font-size:30px;
animation:hearts 20s linear infinite;
opacity:0.2;
}

@keyframes hearts{
0%{transform:translateY(0)}
100%{transform:translateY(120vh)}
}

.title{
text-align:center;
font-family:'Dancing Script',cursive;
font-size:70px;
color:#ffffff;
text-shadow:0px 0px 20px rgba(255,255,255,0.7);
margin-top:20px;
}

.subtitle{
text-align:center;
font-size:24px;
color:white;
margin-bottom:40px;
}

.memory-card{
background:rgba(255,255,255,0.4);
backdrop-filter:blur(10px);
border-radius:20px;
padding:25px;
margin-bottom:30px;
box-shadow:0 10px 25px rgba(0,0,0,0.15);
}

.memory-title{
font-size:28px;
color:#ff4b6e;
font-weight:bold;
}

.memory-date{
color:#555;
margin-bottom:10px;
}

.memory-text{
font-size:17px;
line-height:1.7;
}

.love-letter{
background:white;
border-radius:20px;
padding:40px;
font-size:20px;
line-height:1.8;
box-shadow:0 10px 30px rgba(0,0,0,0.2);
}

</style>
""", unsafe_allow_html=True)

# ----------- HEADER -----------

st.markdown("<div class='title'>Our Love Story ❤️</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>2025 — The Most Beautiful Year Of My Life</div>", unsafe_allow_html=True)

# ----------- DAYS COUNTER -----------

start_date = datetime.date(2024,12,31)
today = datetime.date.today()

days = (today - start_date).days

st.metric("Days Since Our Story Began ❤️", days)

# ----------- PHOTO SLIDER -----------

st.header("📸 Our Beautiful Moments")

photos = list(Path("photos").glob("*"))

if photos:

    index = st.slider("Slide through our memories ❤️",0,len(photos)-1,0)

    img = Image.open(photos[index])
    st.image(img,use_container_width=True)

# ----------- MEMORIES -----------

memories = [

{
"title":"The Night We First Met",
"date":"31 December 2024",
"text":"That New Year night changed everything. We met in the mall while everyone was celebrating. I still remember how beautiful and confident you looked. That moment became the beginning of something very special."
},

{
"title":"Our First Date",
"date":"8 February 2025 — Ironhill",
"text":"Our first date at Ironhill. We talked for hours about life, dreams, and our past. That night felt natural and comfortable, like we had known each other for years."
},

{
"title":"The Day You Proposed",
"date":"12 April 2025",
"text":"You proposed to me and that moment gave me a strange peace in my heart. Knowing someone so kind and caring wanted to be part of my life felt truly special."
},

{
"title":"Our First Kiss",
"date":"1 May 2025",
"text":"One of the sweetest memories. We shared our first kiss and enjoyed our favourite Meghana biryani. A simple day that became unforgettable."
},

{
"title":"Kodaikanal Trip",
"date":"16 May 2025",
"text":"Walking through the misty hills and exploring Guna caves together felt magical. That trip gave us some of our most peaceful memories."
},

{
"title":"Birthday In Pondicherry",
"date":"19 May 2025",
"text":"Celebrating my birthday with you by the sea in Pondicherry made the day unforgettable."
},

{
"title":"Sakleshpur Trip",
"date":"30 August 2025",
"text":"One of the most beautiful trips we had together. Quiet roads, hills, and long conversations."
},

{
"title":"Goa Memories",
"date":"12 – 15 December 2025",
"text":"Goa was full of laughter, reels, drinks, and crazy moments that we will always remember."
},

{
"title":"Ending The Year Together",
"date":"31 December 2025",
"text":"Exactly one year after we first met, we celebrated New Year together again. Looking back, I realised something simple — 2025 became the best year of my life because you were in it."
}

]

# ----------- SHOW MEMORIES -----------

for i,m in enumerate(memories):

    st.markdown("<div class='memory-card'>", unsafe_allow_html=True)

    col1,col2 = st.columns([1,2])

    with col1:

        img_path=f"photos/{i+1}.jpg"

        if Path(img_path).exists():
            image=Image.open(img_path)
            st.image(image,use_container_width=True)

    with col2:

        st.markdown(f"<div class='memory-title'>{m['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='memory-date'>{m['date']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='memory-text'>{m['text']}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ----------- LOVE LETTER -----------

st.header("💌 A Message From My Heart")

if st.button("Open Love Letter ❤️"):

    st.markdown("""
    <div class='love-letter'>

    My Love,

    When I look back at 2025, I don't just remember places or dates.

    I remember moments.

    Our long conversations, our trips, our silly fights, and the way we always found our way back to each other.

    Every memory with you made this year unforgettable.

    The truth is simple.

    This year was special because **you were in it**.

    And no matter where life takes us next,  
    these memories will always stay close to my heart.

    Forever yours ❤️

    </div>
    """, unsafe_allow_html=True)
