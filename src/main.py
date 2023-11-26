from src import FastAPI, uvicorn
from src.routers import fbScrapper


app = FastAPI()



app.include_router(fbScrapper.router)

@app.get("/")
async def root():
    return "Welcome to facebook scrapper"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)