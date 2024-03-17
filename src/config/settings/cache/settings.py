from ..core import CoreSettings


class CacheSettings(CoreSettings):
    NLP_SEARCH_EXPIRE_SECONDS: int = 60 * 60 * 24
    SERVICE_EXPIRE_SECONDS: int = 60 * 60 * 24
