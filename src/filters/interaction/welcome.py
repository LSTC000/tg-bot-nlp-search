from aiogram.types import Message

from src.config import settings

from ..core import CoreMessageFilter


class InteractionWelcomeFilter(CoreMessageFilter):
    _interaction_welcome_msg_list: str = settings.message.interaction.WELCOME_LIST

    async def __call__(self, message: Message) -> bool:
        return message.text.lower() in self._interaction_welcome_msg_list
