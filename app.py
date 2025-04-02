import streamlit as st
from gemini_summarizer import generate_summary

st.set_page_config(page_title="AI Research Report Generator", layout="centered")

st.title("🧠 AI Research Report Generator")
st.write("Generate clean research reports using AI and real-world sources.")

topic = st.text_input("Enter a topic:", placeholder="e.g., AI in Healthcare 2025")

if st.button("Generate Report"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating report..."):
            result = generate_summary(topic)
            st.success("Done!")
            st.write(result)  # Temporary display
