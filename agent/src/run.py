from postprocessor import Postprocessor

from agent import Agent

user_interests = Postprocessor("user-payload/user.json").convert_user()
cities_from_model = Postprocessor("service-responses/cities.json").convert_response(
    topn=10
)

agent = Agent(llm_name="gemma2:9b-instruct-q8_0")
llm_cities = agent.llm_recomendation(user_interests)
score = agent.evaluate(user_interests, llm_cities, cities_from_model)
print(f"User Interests: {user_interests}\nEvaluation score: {score}")
