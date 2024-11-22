from app.adaptors.chat_open_ai import ChatOpenAIAdapter
from app.services.base_service import BaseService
from app.utils.llm_abstract import LLMAbstract
from app.utils.template_manager import TemplateManager


class LLMService(LLMAbstract, BaseService):
    def __init__(self, chat_model: ChatOpenAIAdapter, template_manager: TemplateManager):
        self.chat_model = chat_model
        self.template_manager = template_manager
        super().__init__()

    def get_chain(self):
        prompt_template = self.template_manager.get_prompt_template()
        return prompt_template | self.chat_model

    def invoke(self, results: str):
        chain = self.get_chain()
        return chain.invoke({
            "results": results
        })
