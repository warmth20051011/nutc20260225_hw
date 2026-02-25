from fastapi import FastAPI, Depends
from pydantic import BaseModel
from app.auth import get_current_user
from app.agent import run_agent

app = FastAPI(title="Enterprise Agent API")

class AgentRequest(BaseModel):
    message: str
    session_id: str

@app.post("/agent/run")
def agent_run(req: AgentRequest, user=Depends(get_current_user)):
    result = run_agent(user, req.message, req.session_id)
    return {"response": result}
