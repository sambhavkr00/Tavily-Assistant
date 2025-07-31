import os
from langchain_tavily import TavilySearch, TavilyCrawl
from dotenv import load_dotenv

load_dotenv()

def get_tavily_search_tool():
    """
    Returns a Tavily search tool.
    """
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if not tavily_api_key:
        raise ValueError("TAVILY_API_KEY environment variable not set.")
    
    search = TavilySearch(max_results=20, include_answer="advanced", include_raw_content= True, search_depth="advanced", tavily_api_key=tavily_api_key)
    return search

def get_tavily_crawl_tool():
    """
    Returns a Tavily crawl tool.
    """
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if not tavily_api_key:
        raise ValueError("TAVILY_API_KEY environment variable not set.")
    
    crawl = TavilyCrawl(max_depth=1, extract_depth="advanced", format="text", tavily_api_key=tavily_api_key)
    return crawl
