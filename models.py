from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from db_setup import Base


class Questions(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)


# id_Questions: list
# for x in id:
#     id_Questions = x.vales


class Choices(Base):
    __tablename__ = 'choices'

    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("question.id"))

