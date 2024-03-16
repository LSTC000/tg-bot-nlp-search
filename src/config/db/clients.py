from redis.asyncio import Redis

from src.config import settings

from .abc import ABCClient


class RedisStorageClient(ABCClient):
    @staticmethod
    def get_client() -> Redis:
        return Redis(
            host=settings.redis.HOST,
            port=settings.redis.PORT,
            db=settings.redis.STORAGE_DB,
            encoding=settings.redis.ENCODING,
            decode_responses=settings.redis.DECODE,
        )


class RedisCacheClient(ABCClient):
    @staticmethod
    def get_client() -> Redis:
        return Redis(
            host=settings.redis.HOST,
            port=settings.redis.PORT,
            db=settings.redis.CACHE_DB,
            encoding=settings.redis.ENCODING,
            decode_responses=settings.redis.DECODE,
        )
