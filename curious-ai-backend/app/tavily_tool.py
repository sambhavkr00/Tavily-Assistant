import os
from langchain_tavily import TavilySearch, TavilyExtract
from dotenv import load_dotenv
from app.credentials import get_credential



def get_tavily_search_tool():
    """
    Returns a Tavily search tool.
    """
    tavily_api_key = get_credential("TAVILY_API_KEY")
    
    search = TavilySearch(max_results=10, include_answer="advanced", include_raw_content="text" , search_depth="advanced", tavily_api_key=tavily_api_key)
    return search

def get_tavily_extract_tool():
    """
    Returns a Tavily extract tool.
    """
    tavily_api_key = get_credential("TAVILY_API_KEY")
    
    extract = TavilyExtract(max_depth=1, extract_depth="advanced", format="text", tavily_api_key=tavily_api_key)
    return extract
