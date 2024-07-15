# LLM Evaluation Agent

## Overview

LLM Evaluation Agent is a versatile tool leveraging a Large Language Model (LLM) to evaluate system performance. Designed for broad applicability, it offers easy integration and extension capabilities.

## Features

- **LLM-Powered Evaluation**: Use LLMs for robust evaluation tasks.
- **Versatile Design**: Suitable for a wide range of applications.
- **Easy Integration**: Simple to incorporate into existing projects.
- **Local Execution**: Supports running locally with HuggingFace models or Ollama.

### Note:
- **Ollama**: While lighter and more efficient, Ollama may not perform as well on complex tasks.
- **Customization**: Adapt the agent to your needs by modifying the input/output prompts and data formats.

## Installation

To set up the LLM Evaluation Agent, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/dimitris-anastasiou/llm-evaluation-agent.git

2. Navigate to the project directory:
   ```sh
   cd llm-evaluation-agent

3. Install the necessary dependencies:
   ```sh
   pip install numpy pandas requests torch transformers ollama langchain langchain-community pydantic huggingface_hub

## Downloading Ollama

Visit the [Ollama website](https://www.ollama.com/) to download the latest version of Ollama. Follow the installation instructions specific to your operating system.

## Setting Up Hugging Face

1. Create an account on [Hugging Face](https://huggingface.co/).
2. Install the `transformers` library:
   ```sh
   pip install transformers
3. Configure your Hugging Face API token:
   ```sh
   huggingface-cli login
4. Follow the prompts to enter your Hugging Face credentials.

## Usage

After installation, you can start using the LLM Evaluation Agent by configuring the input and output prompts to suit your specific requirements. Detailed documentation and examples are available in the repository to help you get started quickly.
