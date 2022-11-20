import streamlit as st
from chatbot_creation_wizard import *

# Create a streamlit app
header = st.container()
faq_extraction = st.container()

with header:
    st.title("FAQ Extraction bot creation wizard")

# #create an input box for the user to enter a link 
with faq_extraction:
    st.header("FAQ Extraction")
    bot = None
    link = st.text_input("Enter a link to extract FAQ's from")
    if st.button("Extract FAQs"):
        st.write("FAQs extracted from the link are:")
        bot = generate_faq_bot(link)
    
    st.header(f"Company name: {bot['name']}")
    st.write(f"The sector the company operates is: {bot['sector']}")

    st.write(f"Question 1: {bot['questions'][0]}")
    st.write(f"Answer 1: {bot['answers'][0]}")
    st.write(f"Hyped answer 1: {bot['hyped'][0]}")
    
    st.write(f"Question 2: {bot['questions'][1]}")
    st.write(f"Answer 2: {bot['answers'][1]}")
    st.write(f"Hyped answer 2: {bot['hyped'][1]}")

    st.write(f"Question 3: {bot['questions'][2]}")
    st.write(f"Answer 3: {bot['answers'][2]}")
    st.write(f"Hyped answer 3: {bot['hyped'][2]}")


