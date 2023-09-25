from pydantic import BaseModel


class SItems(BaseModel):
    id: int
    name: str
    description: str


class SItemsRequest(BaseModel):
    name: str
    description: str
