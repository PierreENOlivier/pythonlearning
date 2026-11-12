from typing import Literal
import warnings
import httpx

question_categories = {
    "A": {
        "name": "Any",
        "api_code": 0,
    },
    "B": {
        "name": "General Knowledge",
        "api_code": 0,
    },
    "C": {
        "name": "Science and Nature",
        "api_code": 17,
    },
    "D": {
        "name": "Animals",
        "api_code": 27,
    },
    "E": {
        "name": "History",
        "api_code": 23,
    },
    "F": {
        "name": "Geography",
        "api_code": 22,
    },

}

class Question:
    def __init__(self, text: str, answer: bool):
        self.text = text
        self.answer = answer

class OpenTriviaAPI:
    def __init__(
        self,
        length: int = 10,
        difficulty: Literal["easy", "medium", "hard"] = "easy",

    ):
        self.length = length
        self.difficulty = difficulty
        self.type = "boolean"
        self.category = "A"

        self.httpx_client = httpx.Client(
            base_url="https://opentdb.com",
            timeout=10.0,
        )

    def select_category(self):
        print("Select a category of questions from the ones below:")
        for k, v in question_categories.items():
            print(f"{k}: {v["name"]}")

        while (choice := input(f"Choose a category: ")) not in question_categories.keys():
            warnings.warn("Invalid category. Provide a valid category from the list above.")

        self.category = choice

    def request_questions(self):
        parameters = {
            'amount': self.length,
            'difficulty': self.difficulty,
            'type': self.type
        }

        if self.category != "A":
            parameters['category'] = question_categories[self.category]["api_code"]




        response = self.httpx_client.get(
            url="/api.php",
            params=parameters
        )
        response.raise_for_status()

        print(f"Request: {response.url}")

        if response.status_code == 200:
            print("Request successful")
        else:
            print(f"Unexpected error: {response.status_code}")

        if response.json()['results']:
            self.questions = self.process_response(response)

        else:
            warnings.warn("Request returned empty response..")

    @staticmethod
    def process_response(response):
        data = response.json()

        questions = []
        for question in data['results']:
            questions.append(
                Question(
                    text=question['question'],
                    answer=question['correct_answer']
                )
            )
        return questions

