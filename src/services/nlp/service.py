from fastapi_cache.decorator import cache

from src import schemas
from src.common.cache import CacheManager
from src.config import settings
from src.nlp import NLPSearch

from ..core import CoreService
from .utils import NLPServiceUtils


class NLPService(CoreService):
    utils: NLPServiceUtils = NLPServiceUtils()

    @staticmethod
    @cache(**CacheManager.service(expire=settings.cache.NLP_SEARCH_EXPIRE_SECONDS))
    async def nlp_search_response(query: str) -> schemas.NLPSearch:
        return schemas.NLPSearch(response=NLPSearch.response(query))
