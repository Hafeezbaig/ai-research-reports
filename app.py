import streamlit as st
from gemini_summarizer import generate_summary
from scraper import get_articles
from report_generator import generate_pdf

st.set_page_config(page_title="AI Research Report Generator", layout="centered")
st.title("🧠 AI Research Report Generator")
st.write("Generate clean research reports using AI and real-world sources.")

topic = st.text_input("Enter a topic:", placeholder="e.g., AI in Healthcare 2025")

if st.button("Generate Report", key="generate_btn"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Fetching articles and generating report..."):
            articles = get_articles(topic, max_results=3)
            if not articles:
                st.error("No articles found. Try a different topic.")
            else:
                summaries = []
                for article in articles:
                    summary = generate_summary(article["content"])
                    summaries.append(f"### {article['title']}\n{summary}\n")
                final_report = "\n\n".join(summaries)
                st.success("Done!")

                # Show markdown
                st.markdown(final_report)

                # Generate PDF and offer download
                pdf_path = generate_pdf(final_report)
                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="📄 Download Report as PDF",
                        data=f,
                        file_name="ai_research_report.pdf",
                        mime="application/pdf",
                        key="download_pdf_btn"
                    )
