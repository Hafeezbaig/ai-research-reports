from duckduckgo_search import DDGS
from newspaper import Article

def search_articles(topic, max_results=5):
    links = []
    with DDGS() as ddgs:
        results = ddgs.text(topic, max_results=max_results)
        for r in results:
            if "http" in r["href"]:
                links.append(r["href"])
    return links

def extract_article_content(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.title, article.text
    except:
        return None, None

def get_articles(topic, max_results=5):
    urls = search_articles(topic, max_results=max_results)
    articles = []
    for url in urls:
        title, text = extract_article_content(url)
        if text:
            articles.append({"url": url, "title": title, "content": text})
    return articles
