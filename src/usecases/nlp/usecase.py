from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src import schemas
from src.common.keyboard import KeyboardManager
from src.common.state import StateManager
from src.config import settings
from src.keyboards import KeyboardRepository
from src.loader import BotLoader
from src.services import ServiceRepository

from ..core import CoreUseCase


class NLPUseCase(CoreUseCase):
    services: ServiceRepository = ServiceRepository()
    keyboards: KeyboardRepository = KeyboardRepository()

    _bot: Bot = BotLoader.get_bot()

    _interaction_welcome_msg: str = settings.message.interaction.WELCOME
    _interaction_goodbye_msg: str = settings.message.interaction.GOODBYE

    _nlp_searching_msg: str = settings.message.nlp.SEARCHING

    async def welcome_msg(self, message: Message, state: FSMContext) -> None:
        user_id = message.from_user.id
        state_data = await StateManager.get_data(state)

        if state_data.last_inline_keyboard_message_id is not None:
            await KeyboardManager.remove_last_inline_keyboard(
                user_id=user_id,
                last_inline_keyboard_message_id=state_data.last_inline_keyboard_message_id,
            )
            await StateManager.update_data(
                state=state,
                data=schemas.StateData(last_inline_keyboard_message_id=None),
            )

        await self._bot.send_message(
            chat_id=user_id,
            text=self._interaction_welcome_msg,
        )

    async def goodbye_msg(self, message: Message, state: FSMContext) -> None:
        user_id = message.from_user.id
        state_data = await StateManager.get_data(state)

        if state_data.last_inline_keyboard_message_id is not None:
            await KeyboardManager.remove_last_inline_keyboard(
                user_id=user_id,
                last_inline_keyboard_message_id=state_data.last_inline_keyboard_message_id,
            )
            await StateManager.update_data(
                state=state,
                data=schemas.StateData(last_inline_keyboard_message_id=None),
            )

        await self._bot.send_message(
            chat_id=user_id,
            text=self._interaction_goodbye_msg,
        )

    async def nlp_search_msg(self, message: Message, state: FSMContext) -> None:
        user_id = message.from_user.id
        state_data = await StateManager.get_data(state)

        if state_data.last_inline_keyboard_message_id is not None:
            await KeyboardManager.remove_last_inline_keyboard(
                user_id=user_id,
                last_inline_keyboard_message_id=state_data.last_inline_keyboard_message_id,
            )
            await StateManager.update_data(
                state=state,
                data=schemas.StateData(last_inline_keyboard_message_id=None),
            )

        await self._bot.send_message(
            chat_id=user_id,
            text=self._nlp_searching_msg,
        )

        nlp_search_response = await self.services.nlp.nlp_search_response(
            query=message.text
        )
        await self._bot.send_message(
            chat_id=user_id,
            text=nlp_search_response.response,
        )
