import os
import pandas as pd
from agent import Agent
from agent.data_processor import DataProcessor
from parsers import CityRecommendation, EvaluationScore

# Define processing functions
def process_user_settings(settings: dict) -> str:
    prompt = (
        f"The user is interested in {', '.join(settings['user_interests'])}. "
        f"They prefer a {settings['preferred_climate']} climate with a population range between "
        f"{settings['population_range']['min']} and {settings['population_range']['max']}. "
        f"Must-have features include: {', '.join(settings['must_have_features'])}."
    )
    return prompt

def process_evaluation_data(data: dict, topn: int) -> list:
    sorted_data = sorted(data['data'], key=lambda x: x['population'], reverse=True)
    return [item["city"] for item in sorted_data[:topn]]

def save_to_csv(data: dict, filename: str) -> None:
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def save_to_excel(data: dict, filename: str) -> None:
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

# Main function
def main():
    # Define the directory to save results
    save_directory = "data_to_evaluate"
    os.makedirs(save_directory, exist_ok=True)

    # Initialize the DataProcessor
    data_processor = DataProcessor(
        data_file_path=os.path.join(save_directory, "data.json"),
        settings_file_path="user-payload/user_prompt_setting.json"
    )

    # Convert user interests and model response using general processing functions
    user_interests = data_processor.convert_user(process_user_settings)
    cities_from_model = data_processor.convert_response(process_evaluation_data, topn=10)

    # Initialize the Agent with the specific LLM model
    agent = Agent(llm_name="gemma2:9b-instruct-q8_0", data_processor=data_processor)

    # Generate LLM recommendations and evaluate them
    llm_cities = agent.llm_recommendation(
        process_user_settings=process_user_settings,
        output_model=CityRecommendation,
        template="Recommend cities based on {user_input}"
    )
    score = agent.evaluate(
        process_evaluation_data=process_evaluation_data,
        evaluation_model=EvaluationScore,
        template="Evaluate the following cities {data_to_evaluate} based on user preferences {user_input}",
        topn=10
    )

    # Print the results
    print(f"User Interests: {user_interests}\nEvaluation score: {score}")

    # Prepare data to save
    data_to_save = {
        "User Interests": [user_interests],
        "LLM Cities": [", ".join(llm_cities)],
        "Evaluation Score": [score],
    }

    # Define file paths
    csv_file_path = os.path.join(save_directory, "llm_evaluation_results.csv")
    excel_file_path = os.path.join(save_directory, "llm_evaluation_results.xlsx")

    # Save results to a CSV file
    save_to_csv(data_to_save, csv_file_path)

    # Save results to an Excel file
    save_to_excel(data_to_save, excel_file_path)

# Run Main function
if __name__ == "__main__":
    main()
