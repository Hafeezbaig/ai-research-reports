import streamlit as st
from gemini_summarizer import generate_summary
from scraper import get_articles
from report_generator import generate_pdf

st.set_page_config(page_title="AI Research Report Generator", layout="centered")
st.title("🧠 AI Research Report Generator")

st.markdown(
    """
    <style>
    .reportview-container {
        padding-top: 2rem;
    }
    .stTextInput > div > input {
        font-size: 16px;
    }
    .footer {
        position: fixed;
        bottom: 10px;
        width: 100%;
        text-align: center;
        font-size: 14px;
        color: #666;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("Generate clean research reports using AI and real-world sources.")

st.markdown("### 🔍 Enter a topic below to generate a research report")

topic = st.text_input("", placeholder="e.g., AI in Healthcare 2025")

if st.button("🚀 Generate Report", key="generate_btn"):
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
                st.success("✅ Report ready!")

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

# Footer
st.markdown(
    '<div class="footer">Crafted with ❤️ by <a href="https://hafeezbaig.in" target="_blank">Hafeez Baig</a></div>',
    unsafe_allow_html=True
)
