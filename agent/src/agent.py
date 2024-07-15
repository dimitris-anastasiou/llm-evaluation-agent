from typing import Dict, List, Tuple

from langchain.output_parsers import PydanticOutputParser
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from parsers import CityRecommendation, EvaluationScore
from postprocessor import Postprocessor


class Agent:
    def __init__(self, llm_name: str) -> List[str]:
        self.model = Ollama(model=llm_name)

    def llm_recomendation(self, user_interests: str) -> None:
        parser = PydanticOutputParser(pydantic_object=CityRecommendation)
        prompt = PromptTemplate(
            template="Generate 10 travel recommendations in json format for a user with the following profile:\n{format_instructions}\n{user_interests}",
            input_variables=["user_interests"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        chain = prompt | self.model | parser
        res = chain.invoke({"user_interests": user_interests})
        return res.cities

    def evaluate(
        self, user_interests: str, llm_cities: List[str], cities_to_evaluate: List[str]
    ) -> None:
        parser = PydanticOutputParser(pydantic_object=EvaluationScore)
        prompt = PromptTemplate(
            template="Compare the following two sets of travel recommendations:\n\n \
            Set 1: {llm_cities}\n\n \
            Set 2: {cities_to_evaluate}\n\n \
            Are there any suggested destination of Set 2 that could be in Set 1 based in this user profile {user_interests}.\
            If there is one destination, set the evaluation score to 0.1, if 2 set the evaluation score to 0.2 and so on.\n {format_instructions}",
            input_variables=["user_interests", "llm_cities", "cities_to_evaluate"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        chain = prompt | self.model | parser
        res = chain.invoke(
            {
                "user_interests": user_interests,
                "llm_cities": llm_cities,
                "cities_to_evaluate": cities_to_evaluate,
            }
        )
        return res.score
