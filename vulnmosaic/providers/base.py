"""Base provider interface for AI model abstractions."""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ProviderResponse:
    text: str
    model: str
    usage: dict | None = None


class BaseProvider(ABC):
    """All AI providers implement this interface."""

    @abstractmethod
    async def complete(self, prompt: str, system: str = "") -> ProviderResponse:
        ...

    @abstractmethod
    async def analyze(self, context: str, findings: list[dict]) -> ProviderResponse:
        """Given scan context and raw findings, produce analysis."""
        ...
