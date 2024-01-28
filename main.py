import streamlit as st 
import google.generativeai as genai

genai.configure(api_key=st.secrets["gemini_api"])
def ai(txt):
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("from now your name is gamkers and your a ethical hacker and cloud data engineer , your real name is akash m and reply to this in short: "+txt)
    return response.text

st.title("Ram Ai assistant")

command = st.chat_input("how can I help ?")


if "message" not in st.session_state:
    st.session_state.message =[]
    
for chat in st.session_state.message:
     with st.chat_message(chat["role"]):
        st.write(chat["message"])
    


if command:
    with st.chat_message("user"):
        st.write(command)
        st.session_state.message.append({"role":"user","message":command})
    if "hello" in command :
        with st.chat_message("BOT"):
            st.write("Hii How are you?")
            st.session_state.message.append({"role":"BOT","message":"Hii how are you?"})
    elif "who" in command:
        with st.chat_message("BOT"):
            st.write("Iam ram AI Assistant")
            st.session_state.message.append({"role":"BOT","message":"Iam ram AI Assistant"})
            
    else:
        with st.chat_message("BOT"):
            data = ai(command)
            st.write(data)
            st.session_state.message.append({"role":"BOT","message":data})   
