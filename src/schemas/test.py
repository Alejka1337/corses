from typing import List, Optional, Union

from pydantic import BaseModel

from src.enums import QuestionTypeOption


class TestAnswerBase(BaseModel):
    a_text: str
    is_correct: bool
    image_path: Optional[str] = None


class TestMatchingBase(BaseModel):
    right_text: str
    left_text: str


class TestQuestionBase(BaseModel):
    q_text: str
    q_number: int
    q_score: int
    q_type: QuestionTypeOption
    hidden: Optional[bool] = False
    image_path: Optional[str] = None
    answers: List[Union[TestAnswerBase, TestMatchingBase]]


class TestConfigUpdate(BaseModel):
    score: Optional[int] = None
    attempts: Optional[int] = None


class TestQuestionUpdate(BaseModel):
    q_text: Optional[str] = None
    q_number: Optional[int] = None
    q_score: Optional[int] = None
    hidden: Optional[bool] = False
    image_path: Optional[str] = None


class TestAnswerUpdate(BaseModel):
    a_text: Optional[str] = None
    is_correct: Optional[bool] = False
    image_path: Optional[str] = None


class TestMatchingUpdate(BaseModel):
    right_text: Optional[str] = None
    left_text: Optional[str] = None
