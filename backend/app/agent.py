import os
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from app.tavily_tool import get_tavily_search_tool, get_tavily_crawl_tool
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory

load_dotenv()

def create_agent():
    """
    Creates a LangChain agent with a Tavily search tool.
    """
    tools = [get_tavily_search_tool(), get_tavily_crawl_tool()]

    # Initialize memory
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    prompt_template = """
    Answer the following questions as best you can. You have access to the following tools:

    {tools}

    {chat_history}

    Use the following format:

    Question: the input question you must answer
    Thought: You need to decide which tool to use.
    If the input is a simple greeting or conversational, respond directly with a Final Answer without using any tools.
    If the user provides a URL and wants to get the entire content of the page (e.g., to summarize an article or analyze the full context), use the 'tavily_crawl' tool.
    If the user wants to search for general information, use the 'tavily_search' tool.
    If the tools do not provide a relevant answer, you should try to answer the question yourself.
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: Provide the most comprehensive answer possible, including all relevant details from the tool outputs.

    Begin!

    Question: {input}
    Thought:{agent_scratchpad}
    """
    
    prompt = PromptTemplate.from_template(prompt_template)
    
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set.")
    
    llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-2.0-flash", google_api_key=google_api_key)
    
    agent = create_react_agent(llm, tools, prompt)
    
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True, memory=memory)
    
    return agent_executor