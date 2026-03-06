import streamlit as st
import datetime
from PIL import Image
import base64
from pathlib import Path

# PAGE CONFIG
st.set_page_config(
    page_title="Our Love Story 2025 ❤️",
    page_icon="💕",
    layout="wide"
)

# PASSWORD PROTECTION
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


# LOAD CSS
def load_css():
    st.markdown("""
<style>

.stApp {
background: linear-gradient(135deg,#667eea,#764ba2);
}

/* floating hearts */

.stApp::before{
content:"❤️ 💕 💖 ❤️ 💕 💖 ❤️";
position:fixed;
top:-50px;
left:0;
width:100%;
font-size:30px;
animation:floatHearts 12s linear infinite;
opacity:0.4;
}

@keyframes floatHearts{
0%{transform:translateY(0);}
100%{transform:translateY(120vh);}
}

.main-title{
font-size:60px;
text-align:center;
color:white;
font-family:cursive;
}

.subtitle{
text-align:center;
color:white;
font-size:22px;
margin-bottom:40px;
}

.memory-card{
background:white;
padding:20px;
border-radius:15px;
margin-bottom:30px;
box-shadow:0 10px 25px rgba(0,0,0,0.2);
}

.memory-title{
font-size:28px;
color:#764ba2;
font-weight:bold;
}

.memory-date{
color:#667eea;
margin-bottom:10px;
}

.memory-description{
font-size:17px;
color:#555;
}

.quote{
text-align:center;
font-size:28px;
color:white;
margin:40px;
font-family:cursive;
}

</style>
""", unsafe_allow_html=True)


# MEMORIES DATA
def get_memories():

    memories = [

        {
            "title":"First Time We Met",
            "date":"31 Dec 2024",
            "description":"We first met in the mall during New Year celebrations. I still remember how posh and beautiful you looked. That moment started everything.",
            "image_path":"photos/photo1.jpg"
        },

        {
            "title":"First Date",
            "date":"8 Feb 2025 - Ironhill",
            "description":"Our first official date. We talked about our past, life and dreams while enjoying crafted beer. Ironhill became our favorite place in Bangalore.",
            "image_path":"photos/photo2.jpg"
        },

        {
            "title":"You Proposed",
            "date":"12 Apr 2025",
            "description":"You proposed to me on Snapchat. That night I slept peacefully knowing I have someone so lovely and caring in my life.",
            "image_path":"photos/photo3.jpg"
        },

        {
            "title":"Our First Kiss",
            "date":"1 May 2025",
            "description":"One of the most special days. We had our first kiss and ate our favorite Meghana biryani together.",
            "image_path":"photos/photo4.jpg"
        },

        {
            "title":"Kodaikanal Trip",
            "date":"16 May 2025",
            "description":"We visited Guna caves and enjoyed every moment together in Kodaikanal.",
            "image_path":"photos/photo5.jpg"
        },

        {
            "title":"My Birthday Pondicherry",
            "date":"19 May 2025",
            "description":"Celebrating my birthday with you in Pondicherry was unforgettable.",
            "image_path":"photos/photo6.jpg"
        },

        {
            "title":"Your Birthday Night",
            "date":"21 May 2025",
            "description":"We fought but later fixed everything and enjoyed beer and food at Mazie & Malt Restobar.",
            "image_path":"photos/photo7.jpg"
        },

        {
            "title":"NUSA Outing",
            "date":"25 June 2025",
            "description":"Even when I was in a bad mood, you made everything better.",
            "image_path":"photos/photo8.jpg"
        },

        {
            "title":"Temple Visit",
            "date":"28 June 2025",
            "description":"We went to Anantapur temple together and later I dropped you home.",
            "image_path":"photos/photo9.jpg"
        },

        {
            "title":"Long Drive Kiss",
            "date":"29 June 2025",
            "description":"After lunch and shopping we shared a beautiful kiss during our long drive.",
            "image_path":"photos/photo10.jpg"
        },

        {
            "title":"ABV Restobar",
            "date":"12 July 2025",
            "description":"You wore a red dress that day and honestly I fell for you even more.",
            "image_path":"photos/photo11.jpg"
        },

        {
            "title":"Sakleshpur Trip",
            "date":"30 Aug 2025",
            "description":"One of the best trips of our life together.",
            "image_path":"photos/photo12.jpg"
        },

        {
            "title":"Tirumala Temple",
            "date":"15 Nov 2025",
            "description":"Praying together for our future felt peaceful.",
            "image_path":"photos/photo13.jpg"
        },

        {
            "title":"First Flight",
            "date":"11 Dec 2025",
            "description":"Your first flight experience — a big milestone moment.",
            "image_path":"photos/photo14.jpg"
        },

        {
            "title":"Goa Trip",
            "date":"12-15 Dec 2025",
            "description":"We made reels, drank together and laughed the whole night.",
            "image_path":"photos/photo15.jpg"
        },

        {
            "title":"Ending The Year Together",
            "date":"31 Dec 2025",
            "description":"Ending the year together made 2025 the best year of my life.",
            "image_path":"photos/photo16.jpg"
        }

    ]

    return memories


# DISPLAY MEMORY
def show_memory(memory):

    st.markdown('<div class="memory-card">',unsafe_allow_html=True)

    col1,col2 = st.columns([1,1])

    with col1:

        if Path(memory["image_path"]).exists():
            img = Image.open(memory["image_path"])
            st.image(img,use_container_width=True)

        else:
            st.info("Add photo here: "+memory["image_path"])

    with col2:

        st.markdown(f'<div class="memory-title">{memory["title"]}</div>',unsafe_allow_html=True)
        st.markdown(f'<div class="memory-date">{memory["date"]}</div>',unsafe_allow_html=True)
        st.markdown(f'<div class="memory-description">{memory["description"]}</div>',unsafe_allow_html=True)

    st.markdown("</div>",unsafe_allow_html=True)


# MAIN APP
def main():

    load_css()

    st.markdown('<h1 class="main-title">Our Love Story 2025 ❤️</h1>',unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Every moment with you is my favorite memory</p>',unsafe_allow_html=True)

    # MUSIC
    try:
        audio = open("music/love_song.mp3","rb")
        audio_bytes = audio.read()

        st.markdown(f"""
        <audio autoplay loop>
        <source src="data:audio/mp3;base64,{base64.b64encode(audio_bytes).decode()}">
        </audio>
        """,unsafe_allow_html=True)

    except:
        st.warning("Add music file in music folder")

    st.markdown('<div class="quote">"In all the world, there is no heart for me like yours."</div>',unsafe_allow_html=True)

    tab1,tab2 = st.tabs(["📸 Memories","💌 Love Notes"])

    # MEMORIES
    with tab1:

        memories = get_memories()

        for m in memories:
            show_memory(m)

    # LOVE NOTES
    with tab2:

        with st.form("love_note"):

            title = st.text_input("Title")
            msg = st.text_area("Write something sweet")

            submit = st.form_submit_button("Send ❤️")

            if submit:

                st.balloons()

                st.success("Message saved 💕")

                st.write(title)
                st.write(msg)


    st.markdown("---")

    st.markdown(
    "<center style='color:white'>Made with ❤️ for the love of my life<br>2025 - Best Year Ever</center>",
    unsafe_allow_html=True
    )


if check_password():
    main()