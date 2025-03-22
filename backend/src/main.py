from fastapi import FastAPI
from quiz.router import quiz_router
from videos.router import videos_router

import logging

app = FastAPI()

logging.basicConfig(filename='app.log', level=logging.INFO)

@app.get("/")
async def root():
    return {"message": "Hello World!"}



app.include_router(quiz_router, prefix="/quiz", tags=["Quiz"])
app.include_router(videos_router, prefix="/videos", tags=["Videos"])
