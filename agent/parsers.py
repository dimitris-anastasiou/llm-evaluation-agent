from typing import List, Any
from langchain_core.pydantic_v1 import BaseModel, Field


# City recommendation model
class CityRecommendation(BaseModel):
    cities: List[str] = Field(description="Name of the city")

# Evaluation score model
class EvaluationScore(BaseModel):
    score: float = Field(description="Evaluation score")

# Product recommendation model
class ProductRecommendation(BaseModel):
    products: List[str] = Field(description="Names of recommended products")

# Performance evaluation model
class PerformanceEvaluation(BaseModel):
    score: float = Field(description="Performance evaluation score")
    remarks: str = Field(description="Remarks on the performance")

# General feedback model
class Feedback(BaseModel):
    user_id: str = Field(description="ID of the user providing feedback")
    comments: str = Field(description="Feedback comments")
    rating: int = Field(description="Rating out of 5")

# Example of a factory function to create models
def create_model(model_name: str, **fields: Any) -> BaseModel:
    """
    Dynamically creates a Pydantic model based on provided fields.
    
    Args:
        model_name (str): Name of the model to create.
        fields (Any): Key-value pairs of field names and their types.
    
    Returns:
        BaseModel: A dynamically created Pydantic model.
    """
    return BaseModel.construct(name=model_name, **fields)
