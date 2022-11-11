"""
Tokenizer
"""
import abc


class Tokenizer(abc.ABC):
    """
    Interface to generate and verify auth tokens
    """

    @abc.abstractmethod
    def encode(self, payload: dict) -> str:
        """
        Encodes a payload into an encoded string
        """
        raise NotImplementedError

    @abc.abstractmethod
    def decode(self, token: str) -> dict:
        """
        Decodes an encoded string into a payload
        """
        raise NotImplementedError
