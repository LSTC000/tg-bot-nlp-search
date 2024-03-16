from functools import lru_cache

from .abc import ABCSettings
from .bot import BotSettings
from .cache import CacheSettings
from .command import CommandSettings
from .keyboard import KeyboardSettings
from .log import LogSettings
from .message import MessageSettings
from .project import ProjectSettings
from .redis import RedisSettings
from .token import TokenSettings


class Settings(ABCSettings):
    log: LogSettings = LogSettings()
    bot: BotSettings = BotSettings()
    project: ProjectSettings = ProjectSettings()
    redis: RedisSettings = RedisSettings()
    token: TokenSettings = TokenSettings()
    command: CommandSettings = CommandSettings()
    message: MessageSettings = MessageSettings()
    keyboard: KeyboardSettings = KeyboardSettings()
    cache: CacheSettings = CacheSettings()


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
