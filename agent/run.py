from typing import List
from parsers import CityRecommendation, EvaluationScore
from data_processor import DataProcessor
from agent import Agent


# Define processing functions
def process_user_settings(settings: dict) -> str:
    prompt = (
        f"The user is interested in {', '.join(settings['user_interests'])}. "
        f"They prefer a {settings['preferred_climate']} climate with a population range between "
        f"{settings['population_range']['min']} and {settings['population_range']['max']}. "
        f"Must-have features include: {', '.join(settings['must_have_features'])}."
    )
    return prompt

# Preprocess data
def process_evaluation_data(data: dict, topn: int) -> List[str]:
    sorted_data = sorted(data['data'], key=lambda x: x['population'], reverse=True)
    return [item["city"] for item in sorted_data[:topn]]

def main():
    # Initialize the DataProcessor
    data_processor = DataProcessor(
        data_file_path="data_to_evaluate/data.json",
        settings_file_path="user-payload/user_prompt_setting.json"
    )

    # Initialize the Agent
    agent = Agent(llm_name="model_name", data_processor=data_processor)

    # Generate recommendations
    recommendations = agent.llm_recommendation(
        process_user_settings=process_user_settings,
        output_model=CityRecommendation,
        template="Recommend cities based on {user_input}"
    )

    # Evaluate the recommendations
    evaluation = agent.evaluate(
        process_evaluation_data=process_evaluation_data,
        evaluation_model=EvaluationScore,
        template="Evaluate the following cities {data_to_evaluate} based on user preferences {user_input}",
        topn=3
    )

    # Output the results
    print("Recommendations:", recommendations)
    print("Evaluation:", evaluation)

if __name__ == "__main__":
    main()
