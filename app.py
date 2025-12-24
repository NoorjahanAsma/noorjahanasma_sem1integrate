import streamlit as st
import requests
from openai import OpenAI

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="AI Academic Tutor",
    layout="centered"
)

st.title("🎓 AI Academic Tutor")
st.write("Real-time AI assistance for postgraduate students")

# ----------------------------
# OpenAI Client (Primary)
# ----------------------------
client = None
try:
    if "OPENAI_API_KEY" in st.secrets:
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception:
    client = None

# ----------------------------
# Hugging Face (Secondary - FREE)
# ----------------------------
HF_API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

def huggingface_response(question):
    payload = {"inputs": question}
    response = requests.post(HF_API_URL, json=payload, timeout=30)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    return "AI service temporarily unavailable."

# ----------------------------
# OpenAI Response
# ----------------------------
def openai_response(question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an academic tutor for postgraduate students."},
            {"role": "user", "content": question}
        ],
        max_tokens=250
    )
    return response.choices[0].message.content

# ----------------------------
# Input
# ----------------------------
question = st.text_input("Ask your academic question:")

if question:
    with st.spinner("Analyzing..."):
        try:
            if client:
                answer = openai_response(question)
                st.caption("Source: OpenAI (Commercial API)")
            else:
                answer = huggingface_response(question)
                st.caption("Source: Hugging Face (Open-source AI)")

        except Exception:
            answer = huggingface_response(question)
            st.caption("Source: Hugging Face (Fallback Mode)")

    st.success(answer)

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("Designed as a real-time, scalable academic AI system with intelligent failover.")
