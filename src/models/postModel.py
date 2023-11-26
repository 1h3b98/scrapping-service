from pydantic import BaseModel
from datetime import datetime


class PostData(BaseModel):
    page_id: str
    data : str
