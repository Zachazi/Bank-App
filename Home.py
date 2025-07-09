import streamlit as st

st.set_page_config(page_title="Bank App", layout="centered")

st.title("🏦 Welcome to Your Bank")
st.subheader("Choose an account type to proceed with")

st.page_link(page="Pages/Current Account Page.py", label="Current account →", icon="💼", use_container_width=True)
st.page_link(page="Pages/Savings Account Page.py", label="Savings account →", icon="💰", use_container_width=True)