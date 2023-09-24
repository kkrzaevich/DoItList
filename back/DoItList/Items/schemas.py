from pydantic import BaseModel


class SItems(BaseModel):
    id: int
    name: str
    description: str
