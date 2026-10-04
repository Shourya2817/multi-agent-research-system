import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from tavily import TavilyClient
from langchain_core.tools import tool


load_dotenv()


# Tavily setup
tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


# Web Search Tool
@tool
def web_search(query: str):
    """
    Search the web for recent and reliable information on a topic.
    Returns search results containing titles, URLs, content and scores.
    """

    results = tavily.search(
        query=query,
        max_results=5
    )

    out = []

    for r in results["results"]:
        out.append(
            f"{r['title']} ({r['url']})\n"
            f"{r['content']}\n"
            f"Score: {r['score']}"
        )

    return "\n\n".join(out)


# URL Scraping Tool
@tool
def scrape_url(url: str) -> str:
    """
    Scrape the content of a given URL and return the text content.
    """

    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.content,
            "html.parser"
        )

        for tag in soup([
            "script",
            "style",
            "nav",
            "header",
            "footer",
            "aside"
        ]):
            tag.decompose()

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        return text[:1000]

    except requests.exceptions.RequestException as e:
        return f"Error scraping URL: {e}"