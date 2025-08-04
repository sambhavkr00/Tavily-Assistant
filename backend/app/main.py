import uvicorn
from pydantic import BaseModel
from app.agent import create_agent
from app.server import app

class Query(BaseModel):
    prompt: str
    session_id: str

agent_executor = create_agent()

@app.post("/api/invoke/")
async def invoke_agent(query: Query):
    """
    Invokes the agent with a given prompt.
    """
    try:
        response = agent_executor.invoke(
            {"input": query.prompt},
            config={"configurable": {"session_id": query.session_id}},
        )
        output = response.get("output", "")
        if "Final Answer:" in output:
            final_answer = output.split("Final Answer:")[-1].strip()
        else:
            final_answer = output.strip()
        return {"output": final_answer}
    except Exception as e:
        return {"error": "An unexpected error occurred. Please try again later."}

@app.get("/")
def read_root():
    return {"message": "Welcome to the CuriousAI"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
