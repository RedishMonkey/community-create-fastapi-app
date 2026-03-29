from fastapi import FastAPI


from src.routes import router


app = FastAPI()

app.include_router(router=router)

@app.get("/")
async def root():
    return {"message": "you reached the root of a fast api backend"}

@app.get("/health")
async def healthcheck():
    return {"message": "api working"}
