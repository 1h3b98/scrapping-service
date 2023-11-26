from pydantic import BaseModel


class PostData(BaseModel):
    page_id: str
    data : str
