from routers import APIRouter,get_posts
from main import db

router = APIRouter(
        prefix='/scrapper',
        tags=['Web Scrapper']
        )


@router.get("/")
async def scrap_posts(page_id: str, limit_pages: int = 2, storage: bool=False):
    data = {}
    data["result"] = [post for post in get_posts(page_id, pages=limit_pages)]
    
    if storage:
        try: 
            db.posts.insert_many(data["result"])
            return "data saved into database"
        except:
            return "error"
    return data["result"]