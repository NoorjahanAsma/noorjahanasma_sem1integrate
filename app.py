import streamlit as st
from openai import OpenAI

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Tutor App",
    layout="centered"
)

st.title("🎓 AI Tutor App")
st.write("Ask questions and get help from AI")

# -----------------------------
# Optional OpenAI Client
# (Used only if API is available)
# -----------------------------
client = None
try:
    if "OPENAI_API_KEY" in st.secrets:
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception:
    client = None

# -----------------------------
# Fallback / Mock AI Function
# -----------------------------
def fallback_ai_response(question):
    """
    This function is used when:
    - API key is missing
    - Billing / quota is exceeded
    - Internet is unavailable

    This ensures the app never crashes.
    """
    return (
        f"🔹 Simulated AI Response 🔹\n\n"
        f"You asked: '{question}'\n\n"
        "This response is generated using a fallback mechanism. "
        "In production, a real AI model (OpenAI) will generate the answer."
    )

# -----------------------------
# User Input
# -----------------------------
question = st.text_input("Ask a question:")

# -----------------------------
# Process Question
# -----------------------------
if question:
    with st.spinner("Thinking..."):
        try:
            if client:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a helpful AI tutor."},
                        {"role": "user", "content": question}
                    ],
                    max_tokens=200
                )
                answer = response.choices[0].message.content
            else:
                answer = fallback_ai_response(question)

        except Exception:
            answer = fallback_ai_response(question)

    st.success(answer)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Academic AI assistant")
