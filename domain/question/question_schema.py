import datetime

from pydantic import BaseModel, validator


class Question(BaseModel):
    subject: str
    content: str
    imgUrl = str
    userImgUrl = str
    brandName = str
    productName = str
    option = str
    date = str
    price = int
    isPhotoReviewed = bool
    create_date: datetime.datetime

    class Config:
        orm_mode = True

class QuestionCreate(BaseModel):
    subject: str
    content: str
    imgUrl = str
    userImgUrl = str
    brandName = str
    productName = str
    option = str
    date = str
    price = int
    isPhotoReviewed = bool

    @validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v