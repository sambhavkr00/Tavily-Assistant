import os
from langchain_tavily import TavilySearch, TavilyCrawl, TavilyExtract
from pydantic import BaseModel, Field
from typing import List, Union
from langchain.tools import StructuredTool

from dotenv import load_dotenv

load_dotenv()

def get_tavily_search_tool():
    """
    Returns a Tavily search tool.
    """
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if not tavily_api_key:
        raise ValueError("TAVILY_API_KEY environment variable not set.")
    
    search = TavilySearch(max_results=20, include_answer="advanced" ,include_images=True, search_depth="advanced", tavily_api_key=tavily_api_key)
    return search

def get_tavily_crawl_tool():
    """
    Returns a Tavily crawl tool.
    """
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if not tavily_api_key:
        raise ValueError("TAVILY_API_KEY environment variable not set.")
    
    crawl = TavilyCrawl(include_images=True, extract_depth="advanced", include_favicon=True, tavily_api_key=tavily_api_key)
    return crawl