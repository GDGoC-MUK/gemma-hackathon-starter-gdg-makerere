import streamlit as st

st.set_page_config(page_title="Gemma Hackathon Starter", layout="centered")

st.title("🚀 Gemma Hackathon Starter App")

st.write("This is a simple starter app for building with Gemma models.")

user_input = st.text_area("Enter your prompt:")

if st.button("Generate Response"):
if user_input.strip():
st.success("This is a placeholder response from Gemma.")
st.write("You entered:")
st.write(user_input)
else:
st.warning("Please enter a prompt first.")
