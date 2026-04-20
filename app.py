import streamlit as st
import google.generativeai as genai

# API Key
genai.configure(api_key="AIzaSyCRXlPRp_EP5UPdM3T7QMMnttBzhH_dvKg")

# Website ki Setting
st.set_page_config(page_title="HEXA_TECH AI Ultra", page_icon="🌀")
st.title("🌀 HEXA_TECH | Ultra Edition")
st.subheader("Model: Gemini 1.5 Pro (Most Advanced)")
st.markdown("---")

# Sabse naya aur powerful model yahan hai
model = genai.GenerativeModel('gemini-1.5-pro')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Zain bhai, Ultra model ready hai. Kya hukum hai?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.chat_message("assistant"):
            # System instruction with High Intelligence
            response = model.generate_content(f"You are HEXA_TECH, the most advanced AI. Created by Zain. Answer like a genius.\n\nUser: {prompt}")
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error: {e}")
        st.info("Bhai, 1.5 Pro kabhi kabhi heavy hota hai. Agar error aaye toh refresh karna.")
