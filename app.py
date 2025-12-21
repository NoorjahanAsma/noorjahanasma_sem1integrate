import streamlit as st

st.set_page_config(page_title="AI Tutor", layout="centered")

st.title("🎓 AI Tutor App")
st.write("Your Streamlit app is running successfully!")

question = st.text_input("Ask a question:")

if question:
    st.success(f"You asked: {question}")
