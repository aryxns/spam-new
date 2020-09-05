import streamlit as st
import antispam

query = st.text_input("Enter a sentence to test for spam: ")
train = st.button("Test")
if train:
    answer = antispam.is_spam(query)
    if answer == True:
        st.write("Spam")
    elif answer == False:
        st.write("Not Spam")
            