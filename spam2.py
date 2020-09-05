import antispam
import streamlit as st

d = antispam.Detector("my_model.dat")

st.title("Sentii Spam Model Training")

user_query = st.text_input("Enter a sentence here: ")
user_s = st.selectbox(
    'Is this spam>?',
    ('True', 'False'))
start = st.button("Train Model")


if start:
    if user_s == 'True':
        d.train(user_query, True)
    elif user_s == 'False':
        d.train(user_query, False)
    st.write("Added to the model! You can add more sentences for accuracy")

msg = st.text_input("")
result = st.button("Get Results")
 
if result:
    answer = d.is_spam(msg)
    st.write(answer)

#d.train("Looking for startup funding", True)
#d.train("Last Day for the BUILDBOX SUMMER SALE!", True)
#d.train("Customer service annoncement. You have a New Years delivery waiting for you. Please call 07046744435 now to arrange delivery", True)
#d.train("Aryan Sharma, Nifty around 11580, Gains 39 points | Check your Portfolio", True)
#d.train("Hello Aryan", False)
#d.train("Document from Akshat Sharma", False)

#msg1 = "Hello Gaurav?!"
#answer = d.is_spam(msg1)