# AI Research Report

AI-powered tool that generates clean, professional research summaries based on any topic using real-time articles and Google Gemini. Ideal for students, researchers, analysts, or content creators who want quick insights.

## Features

- Live Web Scraping – Fetches latest news/articles about your topic  
- AI Summarization (Gemini) – Uses Google Gemini to summarize each article  
- PDF Report Generation – Combines all summaries into a downloadable PDF  
- Built with Streamlit – Fast, interactive frontend  
- Secure API Key Handling – Uses `.env` file for Gemini API key  

## Tech Stack

- Python  
- Streamlit  
- Gemini API (via google.generativeai)  
- duckduckgo-search  
- newspaper3k  
- fpdf  
- dotenv  

## How to Run

1. Clone this repository:

2. Install the dependencies:

```
pip3 install -r requirements.txt
```

3. Add your Gemini API key to a `.env` file:

```
GEMINI_API_KEY=your-api-key-here
```

1. Run the app locally:

```
streamlit run app.py
```

## Example Output

The app generates summaries and displays them in the browser, and also lets you download a clean PDF file with all the AI-generated content.

## Contributing

Pull requests are welcome. You can contribute with features, improvements, or bug fixes.

## License

This project is open source and available under the [MIT License](https://www.hafeezbaig.in/docs/MITLicense). 

**Crafted with ❤️ by Hafeez**
