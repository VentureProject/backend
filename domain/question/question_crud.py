from datetime import datetime

from domain.question.question_schema import QuestionCreate
from models import Question
from sqlalchemy.orm import Session


def get_question_list(db: Session):
    question_list = db.query(Question)\
        .order_by(Question.create_date.desc())\
        .all()
    return question_list


def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question

def create_question(db: Session, question_create: QuestionCreate):
    db_question = Question(subject=question_create.subject,
                           content=question_create.content,
                           imgUrl=question_create.,
                            userImgUrl = question_create.,
                            brandName = question_create.,
                            productName = question_create.,
                            option = question_create.,
                            date = question_create.,
                            price = question_create.,
                            isPhotoReviewed = question_create.,
                           create_date=datetime.now())
    db.add(db_question)
    db.commit()