import streamlit as st

st.title("My Simple App")
name = st.text_input("Enter your name")
if st.button("Greet"):
    st.write(f"Hello, {name}!")
