import os
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

def get_tavily_search_tool():
    """
    Returns a Tavily search tool.
    """
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if not tavily_api_key:
        raise ValueError("TAVILY_API_KEY environment variable not set.")
    
    search = TavilySearch(max_results=10, tavily_api_key=tavily_api_key)
    return search
