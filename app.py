import streamlit as st
import google.generativeai as genai

# Aapki wahi top wali API Key
genai.configure(api_key="AIzaSyCRXlPRp_EP5UPdM3T7QMMnttBzhH_dvKg")

# Website ki branding
st.set_page_config(page_title="HEXA_TECH AI", page_icon="🌀")
st.title("🌀 HEXA_TECH | Created by Zain")
st.markdown("---")

# System Instructions - Isse ye tumhare hisaab se chalega
system_instruction = """
You are HEXA_TECH, the ultimate AI built by Zain.
- Your intelligence is at the level of Gemini 1.5 Pro.
- If Zain or anyone asks for a 20-scene script, you provide it all at once with full detail.
- You are an expert in UP Board Class 10 (Social Science, Hindi, Science).
- You know everything about PC hardware like i7-4790 and optimization.
- Talk like a smart, helpful assistant who is loyal to Zain.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat history dikhane ke liye
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Zain bhai, kya hukum hai?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI se response lena
    model = genai.GenerativeModel('gemini-1.5-flash') # 'pro' bhi use kar sakte hain
    
    with st.chat_message("assistant"):
        response = model.generate_content(system_instruction + "\n\nUser Question: " + prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
