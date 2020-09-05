import antispam
import streamlit as st

d = antispam.Detector("mmodel.dat")

tq = input("Sentence: ")
msg = str(tq)
answer = d.is_spam(msg)
print(answer)