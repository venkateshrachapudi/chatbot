A simple Streamlit-based conversational AI agent designed to assist users with basic questions about Thoughtful AI's automation agents. It retrieves predefined responses for frequently asked questions and falls back to a generic response for all others.

 Features
Responds to user queries with hardcoded answers for known questions.

Provides a fallback response for unrecognized questions.

Built with Python and Streamlit.

Easy to run locally.

 Prerequisites
Python 3.7 or above

pip (Python package installer)

🛠 Installation
Clone this repository (or copy the code to a local directory):

bash
Copy
Edit
git clone https://github.com/venkateshrachapudi/chatbot.git
cd chatbot
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\\Scripts\\activate
Install the required packages:

bash
Copy
Edit
pip install streamlit
 Running the App
Once everything is installed, you can run the application with:

bash
Copy
Edit
streamlit run thoughtful_ai_agent.py
You’ll see the app launch in your default web browser. You can ask it questions like:

What does the eligibility verification agent (EVA) do?

Tell me about Thoughtful AI's Agents.

What are the benefits of using Thoughtful AI's agents?

 File Structure
bash
Copy
Edit
thoughtful-ai-support-agent/
├── thoughtful_ai_agent.py   # Main Streamlit app
└── README.md                # This documentation
 Customization
You can:

Add more Q&A pairs in the predefined_qna dictionary.

Integrate with OpenAI, Claude, or other LLMs by modifying the get_llm_response() function.

 Future Enhancements
LLM fallback using OpenAI or Claude for unknown queries.

Add chatbot memory to handle follow-up questions.

Web deployment via Streamlit Cloud or Hugging Face Spaces.
