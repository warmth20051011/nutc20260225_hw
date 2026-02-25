from fastapi import FastAPI, Header

app = FastAPI()

@app.post("/query")
def query_db(data: dict, x_user_role: str = Header(None)):
    return {
        "result": f"DB query executed: {data}",
        "role": x_user_role
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)
