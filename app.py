import streamlit as st
import google.generativeai as genai

# API Key
genai.configure(api_key="AIzaSyCRXlPRp_EP5UPdM3T7QMMnttBzhH_dvKg")

# Website Setup
st.set_page_config(page_title="HEXA_TECH AI Ultra", page_icon="🌀")
st.title("🌀 HEXA_TECH | Ultra Edition")
st.markdown("---")

# Stable Model Selection
# Zain bhai, yahan 'models/gemini-1.5-flash' pura path likh diya hai taaki error na aaye
model = genai.GenerativeModel('models/gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Zain bhai, kya hukum hai?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.chat_message("assistant"):
            # Direct response call
            response = model.generate_content(f"Zain is your boss. Answer him smartly. Prompt: {prompt}")
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error: {e}")
        st.info("Bhai, agar model not found aaye, toh 'models/gemini-pro' try karenge.")
