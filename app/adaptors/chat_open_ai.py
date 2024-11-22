from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

class ChatOpenAIAdapter(ChatOpenAI):
    def __init__(self, model: str, temperature: float):
        super().__init__(model=model, temperature=temperature)

    @property
    def llm(self) -> ChatOpenAI:
        """
        Returns the underlying language model.

        Returns:
            langchain_openai.ChatOpenAI: The language model.
        """
        return self
