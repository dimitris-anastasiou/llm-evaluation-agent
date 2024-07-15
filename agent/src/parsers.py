from typing import List

from langchain_core.pydantic_v1 import BaseModel, Field, validator


class CityRecommendation(BaseModel):
    cities: List[str] = Field(description="Name of the city")


class EvaluationScore(BaseModel):
    score: float = Field(description="Evaluation score")
