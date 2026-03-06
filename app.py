import streamlit as st
from pathlib import Path
from PIL import Image
import datetime

st.set_page_config(page_title="Our Love Story ❤️", layout="wide")

# ---------- CSS THEME ----------

st.markdown("""
<style>

.stApp{
background: linear-gradient(180deg,#0f0c29,#302b63,#24243e);
color:white;
}

.title{
text-align:center;
font-size:70px;
font-family:cursive;
color:#ff4b6e;
text-shadow:0px 0px 25px rgba(255,75,110,0.8);
}

.subtitle{
text-align:center;
font-size:25px;
margin-bottom:40px;
color:#f2f2f2;
}

.memory-card{
background:rgba(255,255,255,0.05);
border-radius:20px;
padding:30px;
margin-bottom:30px;
backdrop-filter:blur(10px);
border:1px solid rgba(255,255,255,0.1);
}

.memory-title{
font-size:30px;
color:#ff4b6e;
}

.memory-date{
color:#f3c4cf;
margin-bottom:10px;
}

.memory-text{
font-size:18px;
line-height:1.8;
color:#e8e8e8;
}

.love-letter{
background:rgba(255,255,255,0.05);
padding:40px;
border-radius:20px;
font-size:20px;
line-height:1.9;
border:1px solid rgba(255,255,255,0.1);
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------

st.markdown("<div class='title'>Our Love Story ❤️</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>2025 – The Most Beautiful Year Of My Life</div>", unsafe_allow_html=True)

# ---------- RELATIONSHIP COUNTER ----------

start_date = datetime.date(2024,12,31)
today = datetime.date.today()

days = (today-start_date).days

st.metric("Days Since Our Story Began ❤️",days)

# ---------- PHOTO SLIDER ----------

st.header("📸 Our Beautiful Moments")

photos = list(Path("photos").glob("*"))

if photos:

    index = st.slider("Slide through our memories",0,len(photos)-1,0)

    img = Image.open(photos[index])
    st.image(img,use_container_width=True)

# ---------- MEMORIES ----------

memories = [

{
"title":"The Night We First Met",
"date":"31 December 2024",
"text":"That New Year night changed everything. We met in the mall while everyone was celebrating. I still remember how confident and beautiful you looked. I didn't know then that this moment would start one of the most meaningful chapters of my life."
},

{
"title":"Our First Date",
"date":"8 February 2025 – Ironhill",
"text":"Our first real date at Ironhill. We talked about our past, our dreams, and everything that shaped us. The night felt easy and natural. That place slowly became our favourite spot in Bangalore because it reminds me of the moment our story truly began."
},

{
"title":"The Day You Proposed",
"date":"12 April 2025",
"text":"You proposed to me on Snapchat. I remember sleeping that night with a strange peace in my heart, realizing that someone so kind and caring had chosen me. It felt like I found someone who truly understood me."
},

{
"title":"Our First Kiss",
"date":"1 May 2025",
"text":"One of the most unforgettable days. We spent hours talking, laughing, and enjoying our favourite Meghana biryani. Somewhere in that moment we shared our first kiss. A memory that will always stay close to my heart."
},

{
"title":"Kodaikanal Trip",
"date":"16 May 2025",
"text":"Walking together through the misty hills of Kodaikanal and exploring the Guna caves felt like something out of a movie. That trip was full of laughter, random conversations, and quiet moments that made me appreciate you even more."
},

{
"title":"Birthday in Pondicherry",
"date":"19 May 2025",
"text":"Celebrating my birthday with you in Pondicherry was something I will never forget. The streets, the ocean air, and your presence made the entire day feel perfect."
},

{
"title":"Your Birthday Night",
"date":"21 May 2025",
"text":"Even though we had a small fight that day, we still found our way back to each other. Later we went to Mazie & Malt Restobar, shared drinks, food, and laughter. It reminded me that even our difficult moments bring us closer."
},

{
"title":"Sakleshpur Trip",
"date":"30 August 2025",
"text":"One of the most beautiful trips we had. Even though work stress followed me there, the mountains, the quiet roads, and your company made the trip unforgettable."
},

{
"title":"Goa Memories",
"date":"12 – 15 December 2025",
"text":"Goa was pure chaos and happiness. We made reels, laughed endlessly, drank together, and even spent the night laughing at people singing loudly in the resort upstairs."
},

{
"title":"Ending The Year Together",
"date":"31 December 2025",
"text":"Exactly one year after we first met, we celebrated New Year again together. Looking back at the year, I realized something simple but powerful — 2025 became the best year of my life because you were in it."
}

]

# ---------- DISPLAY MEMORIES ----------

for m in memories:

    st.markdown("<div class='memory-card'>", unsafe_allow_html=True)

    col1,col2 = st.columns([1,2])

    with col1:

        img_path = f"photos/{memories.index(m)+1}.jpg"

        if Path(img_path).exists():

            image = Image.open(img_path)
            st.image(image,use_container_width=True)

    with col2:

        st.markdown(f"<div class='memory-title'>{m['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='memory-date'>{m['date']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='memory-text'>{m['text']}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- LOVE LETTER ----------

st.header("💌 A Message From My Heart")

if st.button("Open Love Letter ❤️"):

    st.markdown("""
    <div class="love-letter">

    My Love,

    When I look back at 2025, I don't just see dates or places.

    I see moments.

    I see our conversations, our long drives, our silly fights,
    the way we always found our way back to each other.

    Every trip we took, every meal we shared, every random laugh —
    they all became pieces of a year that changed my life.

    The truth is simple.

    This year was special because you were in it.

    And no matter where life takes us next,
    these memories will always stay with me.

    Forever yours ❤️

    </div>
    """, unsafe_allow_html=True)
