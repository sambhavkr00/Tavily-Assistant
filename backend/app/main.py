import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.agent import create_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    prompt: str

agent_executor = create_agent()

@app.post("/invoke/")
async def invoke_agent(query: Query):
    """
    Invokes the agent with a given prompt.
    """
    try:
        response = agent_executor.invoke({"input": query.prompt})
        return {"output": response.get("output")}
    except Exception as e:
        return {"error": "An unexpected error occurred. Please try again later."}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tavily Assistant API"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
