from aiogram.types import Message

from src.config import settings

from ..core import CoreMessageFilter


class InteractionGoodbyeFilter(CoreMessageFilter):
    _interaction_goodbye_msg_list: str = settings.message.interaction.GOODBYE_LIST

    async def __call__(self, message: Message) -> bool:
        return message.text.lower() in self._interaction_goodbye_msg_list
