import json

from typing import Any, Dict, List, Callable


# Data Processor
class DataProcessor:
    def __init__(self, data_file_path: str, settings_file_path: str) -> None:
        """
        Initializes the DataProcessor with paths to the data and user settings files.

        Args:
            data_file_path (str): Path to the JSON file containing the data to be evaluated.
            settings_file_path (str): Path to the JSON file containing the user-specific settings.
        """
        self._data_file_path = data_file_path
        self._settings_file_path = settings_file_path

    def load_data(self) -> Dict[str, Any]:
        """
        Loads the data to be evaluated from the JSON file.

        Returns:
            Dict[str, Any]: The data loaded from the JSON file.
        """
        with open(self._data_file_path, "r") as file:
            data = json.load(file)
        return data

    def load_user_settings(self) -> Dict[str, Any]:
        """
        Loads the user-specific prompt settings from the JSON file.

        Returns:
            Dict[str, Any]: The settings loaded from the JSON file.
        """
        with open(self._settings_file_path, "r") as file:
            settings = json.load(file)
        return settings

    def convert_user(self, process_function: Callable[[dict], str]) -> str:
        """
        Converts user settings into a prompt string using a provided processing function.

        Args:
            process_function (Callable[[dict], str]): A function that processes the user settings dictionary and returns a string.

        Returns:
            str: The processed user prompt string.
        """
        user_settings = self.load_user_settings()
        return process_function(user_settings)

    def convert_response(self, process_function: Callable[[dict, int], List[Any]], topn: int) -> List[Any]:
        """
        Converts the response data using a provided processing function.

        Args:
            process_function (Callable[[dict, int], List[Any]]): A function that processes the response data dictionary and returns a list.
            topn (int): The number of top items to return.

        Returns:
            List[Any]: The list of top processed items.
        """
        response_data = self.load_data()
        return process_function(response_data, topn)
