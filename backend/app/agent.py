import os
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from app.tavily_tool import get_tavily_search_tool
from dotenv import load_dotenv

load_dotenv()

def create_agent():
    """
    Creates a LangChain agent with a Tavily search tool.
    """
    tools = [get_tavily_search_tool()]
    
    prompt_template = """
    Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do. If you need to use a tool, your next output should be 'Action: [tool_name]'.
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

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
    
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
    
    return agent_executor
