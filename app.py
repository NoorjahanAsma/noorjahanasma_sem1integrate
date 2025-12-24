import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Tutor", layout="centered")

st.title("🤖 AI Tutor App")
st.write("Ask anything and get help from AI!")

# Load API key securely
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

question = st.text_input("Ask a question:")

if question:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful tutor."},
                {"role": "user", "content": question}
            ]
        )

        answer = response.choices[0].message.content
        st.success(answer)
