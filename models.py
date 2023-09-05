from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    imgUrl= Column(String, nullable=False)
    userImgUrl= Column(String, nullable=False)
    brandName= Column(String, nullable=False)
    productName= Column(String, nullable=False)
    option= Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    price= Column(Integer, nullable=False)
    isPhotoReviewed= Column(Boolean, nullable=False)
    create_date = Column(DateTime, nullable=False)


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers")
