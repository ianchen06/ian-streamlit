import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.header("Creative Frontend Developer")
    st.subheader("I'm a frontend developer with a passion for design and creativity. I love to create beautiful and user-friendly interfaces that make people's lives easier.")
    st.button("Contact Me")

with col2:
    st.image("images/top.webp", width=400)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header("My Projects")
    st.subheader("Here are some of the projects I've worked on recently.")

with col2:
    cols = st.columns(2)
    with cols[0]:
        st.markdown("""
## AI Sprout: AI business idea evaluation tool

AI Sprout is a tool that helps entrepreneurs evaluate their AI business ideas. It uses a machine learning model to predict the success of an AI business idea based on various factors such as market size, competition, and technology readiness. 
""")
        st.markdown("""
## AI Sprout: AI business idea evaluation tool

AI Sprout is a tool that helps entrepreneurs evaluate their AI business ideas. It uses a machine learning model to predict the success of an AI business idea based on various factors such as market size, competition, and technology readiness. 
""")
        
    with cols[1]:
        st.markdown("""
## AI Sprout: AI business idea evaluation tool

AI Sprout is a tool that helps entrepreneurs evaluate their AI business ideas. It uses a machine learning model to predict the success of an AI business idea based on various factors such as market size, competition, and technology readiness. 
""")
        
st.divider()

cols = st.columns(2)
with cols[0]:
    st.header("About Me")
    st.subheader("I'm a frontend developer with a passion for creating beautiful and accessible web experiences. I love working with the latest web technologies to bring designs to life.")

with cols[1]:
    st.image("images/profile.webp", width=400)
    st.button("Download Resume")
