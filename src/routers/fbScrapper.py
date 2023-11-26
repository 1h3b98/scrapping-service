from fastapi import APIRouter,Depends
from facebook_scraper import get_posts
from contextlib import suppress
from src.database.mongo_db import get_database
from src.models.postModel import PostData


router = APIRouter(
        prefix='/scrapper',
        tags=['Web Scrapper']
        )



@router.get("/")
async def scrap_posts(page_id: str, email: str,password: str ,num_pages: int = 2, storage: bool=False,db=Depends(get_database)):
    data=[]
    posts = get_posts(page_id,
                      pages=num_pages,
                      credentials=(email, password),
                      )
    for post in posts:
        with suppress(Exception) :
            data.append({
                          'time' : (post['time']),
                          'text' : post['text'][:100],
                          'image' : post['image'][:100],
                          'likes' : post['likes'],
                          'comments' : post['comments'],
                          'shares' : post['shares']
                        })
            model_data= PostData(
                page_id=page_id,
                data=data.dict()
            )
             
            if storage:
                result = await db.insert_one(model_data)
                return await db.find_one(result.inserted_id)
            else:
                data.append(data.dict())

    return data


@router.get("/get_all_posts")
async def get_all_posts(db=Depends(get_database)):
    posts = await db.find().to_list(length=1000)
    return posts

