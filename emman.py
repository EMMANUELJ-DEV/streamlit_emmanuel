import streamlit as st

st.write("Hello, I am Emmanuel")

uploaded_file = st.file_uploader("Upload your file")

if uploaded_file is not None:
    st.write(f"File name: {uploaded_file.name}")
    st.success(f"Nice to meet you! Your file '{uploaded_file.name}' has been uploaded.")
