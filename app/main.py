from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.auth import get_role_from_token
from app.agent import EnterpriseAgent
from app.config import RATE_LIMIT_PER_MINUTE

app = FastAPI(title="Enterprise Agent Platform")

#對外 API
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

security = HTTPBearer()

class AgentRequest(BaseModel):
    message: str
    session_id: str

@app.post("/agent/run")
@limiter.limit(f"{RATE_LIMIT_PER_MINUTE}/minute")
async def agent_run(
    request: AgentRequest,
    credentials: HTTPAuthorizationCredentials = Depends(security),
):

    role = get_role_from_token(credentials.credentials)

    agent = EnterpriseAgent(role, request.session_id)

    result = agent.run(request.message)

    return {
        "role": role,
        "result": result
    }
