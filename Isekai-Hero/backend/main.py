from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Isekai-Hero Backend")

@app.get("/")
def root():
    return {"msg": "Backend de Isekai-Hero funcionando 🚀"}

async def start_backend():
    config = uvicorn.Config("backend.main:app", host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()