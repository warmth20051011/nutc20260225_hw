from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Request(BaseModel):
    input: str

@app.post("/run")
def run(req: Request):
    return {"result": f"DB result for: {req.input}"}
