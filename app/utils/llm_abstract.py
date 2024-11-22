from abc import ABC, abstractmethod


class LLMAbstract(ABC):
    @abstractmethod
    def get_chain(self):
        """
        Returns the `Chain` to be used when querying the LLM.

        The chain should be configured with the prompt template returned by
        `get_prompt_template` and the language model to be used.

        Returns:
            Chain: The chain to be used when querying the LLM.
        """

    @abstractmethod
    def invoke(self, results: str):
        """
        Invokes the LLM using the chain returned by `get_chain` and the
        results of the previous intent.

        Args:
            results (str): The results of the previous intent.

        Returns:
            str: The invocation results.
        """
