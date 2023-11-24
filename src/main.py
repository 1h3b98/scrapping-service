from src import FastAPI,MongoClient,routers

app = FastAPI()
client = MongoClient("localhost", 27017)
db = client['posts']

app.include_router(routers.fbScrapper.router)

@app.get("/")
async def root():
    return "Welcome to facebook scrapper"
