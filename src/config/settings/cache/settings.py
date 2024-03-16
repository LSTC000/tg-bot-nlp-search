from ..core import CoreSettings


class CacheSettings(CoreSettings):
    NLP_EXPIRE_SECONDS: int = 60 * 60 * 24
