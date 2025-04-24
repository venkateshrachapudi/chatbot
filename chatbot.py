import streamlit as st
from difflib import get_close_matches
import openai

# Predefined dataset about Thoughtful AI
predefined_qna = {
    "What does the eligibility verification agent (EVA) do?":
        "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections.",
    "What does the claims processing agent (CAM) do?":
        "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements.",
    "How does the payment posting agent (PHIL) work?":
        "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden.",
    "Tell me about Thoughtful AI's Agents.":
        "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others.",
    "What are the benefits of using Thoughtful AI's agents?":
        "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
}

def get_predefined_answer(user_question):
    # Find closest match among predefined questions
    matches = get_close_matches(user_question, predefined_qna.keys(), n=1, cutoff=0.6)
    if matches:
        return predefined_qna[matches[0]]
    return None

# Uncomment and set your OpenAI key if you want to fallback to OpenAI
# openai.api_key = "your-openai-api-key"
def get_llm_response(prompt):
    # Dummy fallback; replace with OpenAI or any LLM call if needed
    return "I'm not sure about that. Let me get back to you with more information."

# Streamlit UI
st.set_page_config(page_title="Thoughtful AI Support Agent")
st.title("💬 Thoughtful AI Support Agent")
st.write("Ask me anything about Thoughtful AI's automation agents!")

user_input = st.text_input("Your question:", key="input")

if user_input:
    response = get_predefined_answer(user_input)
    if not response:
        response = get_llm_response(user_input)
    st.markdown(f"**Answer:** {response}")
