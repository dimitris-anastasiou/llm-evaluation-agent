# LLM Evaluation Agent



## Overview

LLM Evaluation Agent is a versatile tool leveraging Large Language Models (LLMs) to evaluate system performance. Designed for broad applicability, it offers easy integration and extension capabilities, making it suitable for a wide range of evaluation tasks.



## Table of Contents
- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [Features](#features)
- [Setting Up Ollama](#setting-up-ollama)
- [Setting Up HuggingFace](#setting-up-huggingface)
- [Installation](#installation)
- [Usage Instructions](#usage-instructions)



## Directory Structure

```plaintext
llm-evaluation-agent/
├── agent/
│   ├── agent.py
│   ├── data_processor.py
│   ├── parsers.py
│   └── run.py
├── data_to_evaluate/
│   └── data.json
├── user-payload/
│   └── user_prompt_setting.json
├── README.md
├── LICENSE
├── Makefile
├── Pipfile
├── Pipfile.lock
├── requirements.txt
└── .gitignore
```



## Features

- **LLM-Powered Evaluation**: Leverage LLMs for robust automated evaluation tasks.
- **Versatile Design**: Adaptable to various applications and domains.
- **Easy Integration**: Simple to incorporate into existing projects with minimal setup.
- **Local Execution**: Supports running locally with Ollama or Hugging Face models for flexible deployment options.

> [!NOTE]
> **Ollama**: While lighter and more efficient, Ollama may not perform as well on complex tasks.



## Setting Up Ollama

To use Ollama, follow these steps:
1. Visit the [Ollama website](https://www.ollama.com/) to download the latest version of Ollama.
2. Follow the installation instructions specific to your operating system.



## Setting up HuggingFace

To use HuggingFace models:
1. Create an account on [Hugging Face](https://huggingface.co/).
2. Install the `transformers` library:

   ```sh
   pip install transformers
   ```

3. Configure your Hugging Face API token:

   ```sh
   huggingface-cli login
   ```

4. Follow the prompts to enter your Hugging Face credentials.

>[!Note]
> You will need to modify the scripts in the agent directory to use Hugging Face models instead of the default setup. This involves updating the Agent class to integrate with the Hugging Face transformers library and configuring the model loading and inference process accordingly.



## Installation

To set up the LLM Evaluation Agent, follow these steps:

1. **Clone the repository**:

   ```sh
   git clone https://github.com/dimitris-anastasiou/llm-evaluation-agent.git
   ```
2. **Navigate to the project directory**:

   ```sh
   cd llm-evaluation-agent
   ```

3. **Install the necessary dependencies**:

   ```sh
   pipenv install
   ```

   If you're not using `pipenv`, you can install the dependencies using:

      ```sh
      pip install -r requirements.txt
      ```



## Usage Instructions

After installing the necessary dependencies, you can start using the LLM Evaluation Agent by following these steps:

1. **Prepare Your Data and Settings**
   - Data to Evaluate: Place the JSON file containing the data you want to evaluate in the `data_to_evaluate` directory. For example, if you are evaluating city data, your file should be named something like `data.json`.
   - User Prompt Settings: Place the JSON file containing the user-specific settings in the `user-payload` directory. This file should be named `user_prompt_setting.json`.

2. **Customize the Agent**
   - Processing Functions: You can customize the `process_user_settings` and `process_evaluation_data` functions in the `run.py` file located in the agent directory. These functions define how the user settings and data are processed to generate prompts and evaluate results.
   - LLM Model: The agent can be configured to use different LLM models by specifying the model name during initialization in the run.py file. For example:

      ```sh
      agent = Agent(llm_name="gemma2:9b-instruct-q8_0")
      ```

3. **Understand the Parsers**
   - **Purpose of Parsers**: The parsers are Pydantic models defined in the parsers.py file. They are used to structure and validate the input and output data processed by the agent. This ensures that the data being handled conforms to the expected format.
   - **Available Parsers**:
      1. `CityRecommendation`: This parser model is used to define the expected structure of the city recommendations generated by the LLM.

         ```sh
         class CityRecommendation(BaseModel):
            cities: List[str] = Field(description="Name of the city")
         ```

      2. `EvaluationScore`: This parser model defines the expected structure of the evaluation score returned by the LLM.

         ```sh
         class EvaluationScore(BaseModel):
            score: float = Field(description="Evaluation score")
         ```

      3. `ProductRecommendation`: This parser model is used to structure the names of recommended products.

         ```sh
         class ProductRecommendation(BaseModel):
            products: List[str] = Field(description="Names of recommended products")
         ```

      4. `PerformanceEvaluation`: This parser model captures the performance evaluation results, including both a score and remarks.

         ```sh     
         class PerformanceEvaluation(BaseModel):
         score: float = Field(description="Performance evaluation score")
         remarks: str = Field(description="Remarks on the performance")
         ```

      5. `Feedback`: This parser model is designed to capture general feedback from users, including user ID, comments, and a rating.

         ```sh
         class Feedback(BaseModel):
            user_id: str = Field(description="ID of the user providing feedback")
            comments: str = Field(description="Feedback comments")
            rating: int = Field(description="Rating out of 5")
         ```

   - **Customizing Parsers**: If you're working with different types of data or need different output formats, you can create custom parsers in the `parsers.py` file by defining new Pydantic models. These models will then be used to validate and structure the input/output data for different LLM tasks.
   - **Dynamic Model Creation**: For more advanced use cases, you can dynamically create custom models using a factory function:

      ```sh
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
      ```

      This function allows you to define and instantiate Pydantic models on the fly, making it easy to adapt the agent to new types of data without needing to modify the existing parser code.

4. **Run the Agent**

   Execute the `run.py` script to start the evaluation process:

   ```sh
   python agent.run.py
   ```

   This script will:
   1. Load and process the user-specific settings from `user-payload/user_prompt_setting.json`.
   2. Load and process the data to be evaluated from `data_to_evaluate/data.json`.
   3. Generate LLM-based recommendations based on the processed user settings.
   4. Evaluate the generated recommendations against the provided data using the appropriate parsers.
   5. Save the evaluation results to `llm_evaluation_results.csv` and `llm_evaluation_results.xlsx` inside the `data_to_evaluate` directory.
   5. Output the evaluation score along with the processed user interests.

5. **Review the Results**

   After running the `run.py` script, the results will be saved in the `data_to_evaluate` directory as both a CSV and an Excel file. This includes the processed user interests and the evaluation score for the recommendations generated by the LLM.
   - `llm_evaluation_results.csv`: Contains the results in CSV format.
   - `llm_evaluation_results.xlsx`: Contains the results in Excel format.

   The script will also print the processed user interests and evaluation score to the console.:

   ```plaintext
   User Interests: Technology, culture, gastronomy
   Evaluation score: 8.5
   ```

6. **Customization and Extensibility**

   - **Adding New Parsers**: If your project involves different data types or evaluation criteria, you can define new parsers in the parsers.py file. These parsers will help ensure that the data is structured correctly for your specific use case.
   - **Adding New Evaluation Criteria**: If you need to evaluate different types of data or use different criteria, simply modify the processing functions in run.py and update your JSON files accordingly.
   - **Switching LLM Models**: You can switch between different LLM models by updating the llm_name parameter in the Agent initialization.
