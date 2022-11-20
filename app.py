import streamlit as st
from chatbot_creation_wizard import *

# Create a streamlit app
header = st.container()
faq_extraction = st.container()

with header:
    st.title("FAQ Generation wizard")

# #create an input box for the user to enter a link 
with faq_extraction:
    bot = dict
    link = st.text_input("Enter a URL")
    if st.button("Generate FAQs"):
        st.header("Generated content")
        bot = generate_faq_bot(link)
    
        st.subheader(f"Company name: {bot['name']}")
        st.write(f"**Sector**: {bot['sector']}")

        st.write(f"**FAQ 1**: {bot['questions'][0]}")
        st.write(f"**Answer**: {bot['answers'][0]}")
        st.write(f"**Answer (hyped)**: {bot['hyped'][0]}")
        
        st.write(f"**FAQ 2**: {bot['questions'][1]}")
        st.write(f"**Answer**: {bot['answers'][1]}")
        st.write(f"**Answer (hyped)**: {bot['hyped'][1]}")

        st.write(f"**FAQ 3**: {bot['questions'][2]}")
        st.write(f"**Answer**: {bot['answers'][2]}")
        st.write(f"**Answer (hyped)**: {bot['hyped'][2]}")


