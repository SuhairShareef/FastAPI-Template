import uvicorn
from endpoints import app


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
