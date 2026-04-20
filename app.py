import streamlit as st
import google.generativeai as genai

# API Key configure karein
genai.configure(api_key="AIzaSyCRXlPRp_EP5UPdM3T7QMMnttBzhH_dvKg")

# Website ki setting
st.set_page_config(page_title="HEXA_TECH AI", page_icon="🌀")
st.title("🌀 HEXA_TECH | Created by Zain")
st.markdown("---")

# System instruction setup
sys_model = genai.GenerativeModel('gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani chat dikhane ke liye
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input box
if prompt := st.chat_input("Zain bhai, kya hukum hai?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # AI se response mangna
        with st.chat_message("assistant"):
            # System instruction ko prompt ke saath jod diya hai
            full_prompt = f"System: You are HEXA_TECH, the ultimate AI built by Zain. You are loyal and smart.\nUser: {prompt}"
            response = sys_model.generate_content(full_prompt)
            
            if response.text:
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            else:
                st.warning("AI ne koi jawab nahi diya, phir se try karein.")
                
    except Exception as e:
        st.error(f"Ek chota sa error aaya hai: {e}")
        st.info("Zain bhai, check karo ki API key active hai ya nahi.")
