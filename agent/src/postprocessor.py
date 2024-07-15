import json
from typing import List


class Postprocessor:
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path

    def convert_user(self) -> str:

        with open(self._file_path, "r") as file:
            user = json.load(file)

        user_prompt = ""
        for unit in user:
            if user[unit] == 1:
                user_prompt += f" {unit.replace('_', ' ')},"

        return user_prompt[1:-1]

    def convert_response(self, topn: int) -> List:
        with open(self._file_path, "r") as file:
            response = json.load(file)
        return [city["city"] for city in response["data"]][:topn]
