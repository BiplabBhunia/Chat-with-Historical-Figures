import streamlit as st
import google.generativeai as genai

# Configure the Gemini API (you'll need to replace this with your actual API key)
genai.configure(api_key="AIzaSyC3R-X9bl35fusAfg2WMvWtOOC8hklHlhA")

# Set up the model
model = genai.GenerativeModel('gemini-pro')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Streamlit app
st.title("Chat with Historical Figures")

# Dropdown to select historical figure
historical_figure = st.selectbox(
    "Choose a historical figure to chat with:",
    ["Albert Einstein", "William Shakespeare", "Cleopatra", "Leonardo da Vinci"]
)

# Function to generate response
def generate_response(prompt, historical_figure):
    response = model.generate_content(
        f"You are {historical_figure}. Respond to the following message in your unique style and with your knowledge: {prompt}"
    )
    return response.text

# User input
user_input = st.text_input("Your message:", key="user_input")

# Send button
if st.button("Send"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate response
    response = generate_response(user_input, historical_figure)
    
    # Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])