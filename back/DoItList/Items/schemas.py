from pydantic import BaseModel


class SItems(BaseModel):
    name: str
    descriptions: str
