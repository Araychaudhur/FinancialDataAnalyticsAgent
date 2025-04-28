from langchain_core.messages import HumanMessage
from typing import List
from dataclasses import dataclass

@dataclass
class InputData:
    variable_name: str
    data_path: str
    data_description: str

class PythonChatBot:
    def __init__(self):
        super().__init__()
        self.reset_chat()

    def user_sent_message(self, user_query, input_data: List[InputData]):
        self.chat_history.append(HumanMessage(content = user_query))
        self.input_data = input_data
    
    def reset_chat(self):
        self.chat_history = []
        