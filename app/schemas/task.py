from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    user_id: int # TODO: remove hardcoded user_id after auth

class TaskRead(BaseModel):
    id: int
    title: str
    is_completed: bool

    class Config:
        from_attributes = True