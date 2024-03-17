from pydantic import Field

from ..core import CoreModel


class NLPSearch(CoreModel):
    response: str = Field(..., description="NLP search response")
