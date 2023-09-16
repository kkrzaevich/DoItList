from pydantic import BaseModel


class UserAuth(BaseModel):
    name: str
    password: str
