from pydantic import BaseModel


class Fraudster(BaseModel):
    name: str
    team: str
    position: str
    rating: int
