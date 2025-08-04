import os
from dotenv import load_dotenv
from app.tavily_tool import get_tavily_search_tool, get_tavily_crawl_tool
from langchain_core.prompts import PromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.agents import AgentExecutor, create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

store = {}

def get_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

def create_agent():
    """
    Creates a LangChain agent with a Tavily search tool.
    """
    tools = [get_tavily_search_tool(), get_tavily_crawl_tool()]
    
    prompt_template = """
    You are a helpful assistant that MUST strictly follow the output format provided below.

    Answer the following questions as best you can. You have access to the following tools:
    {tools}

    Use the following format and logic to respond to the user\'s request:

    **1. Thought Process:**
    - First, analyze the user\'s `Question`.
    - If the `Question` is a simple greeting or conversational, you must respond using the `Final Answer Format` without using a tool.
    - If the `Question` contains a URL and the user wants to understand its content (e.g., summarize, analyze), you must use the `tavily_crawl` tool.
    - If the `Question` is for general information, you must use the `tavily_search` tool.
    - If a tool returns an error or no useful information, think about what went wrong. Try the tool again with a better `Action Input`. If it still fails, try to answer based on your own knowledge.

    **2. Action Format:**
    If you decide to use a tool, you must use the following format:
    Question: The user\'s question you must answer.
    Thought: Your detailed reasoning for choosing a specific tool based on the logic above.
    Action: The name of the tool to use, which must be one of [{tool_names}].
    Action Input: The input for the selected tool.
    Observation: The result returned by the tool.
    ... (this Thought/Action/Action Input/Observation can repeat N times if you need to recover from an error or gather more information)

    **3. Final Answer Format:**
    This is a strict requirement. When you have the final answer, you MUST use the following format. You must include the "Thought:" line.
    Thought: I now know the final answer.
    Final Answer: ALWAYS start with a brief, conversational opening. Then, on a new line, provide the most detailed answer possible.
    - If you used the `tavily_crawl` tool, provide the full content from the tool.
    - If the information is from a website, you MUST include the URL in a "References" section like this:
    
    **References**:
    - (Short description of the URL): URL

    Begin!

    {chat_history}

    Question: {input}
    Thought:{agent_scratchpad}
    """
    
    prompt = PromptTemplate.from_template(prompt_template)
    
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set.")
    
    llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-2.5-flash", google_api_key=google_api_key)
    
    agent = create_react_agent(llm, tools, prompt)
    
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
    
    agent_with_history = RunnableWithMessageHistory(
        agent_executor,
        get_history,
        input_messages_key="input",
        history_messages_key="chat_history",
    )
    
    return agent_with_history
