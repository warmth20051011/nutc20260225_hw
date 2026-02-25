from fastapi import FastAPI, Header

app = FastAPI()

@app.post("/run")
def run_python(data: dict, x_user_role: str = Header(None)):
    code = data.get("code", "")
    return {
        "result": f"Python executed: {code}",
        "role": x_user_role
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5002)
