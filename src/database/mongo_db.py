from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "scrapers"
COLLECTION_NAME ="posts"

async def get_database():
    client = AsyncIOMotorClient(MONGO_URI)
    database = client.get_database(DATABASE_NAME)
    collection=database.get_collection(COLLECTION_NAME)
    return collection
