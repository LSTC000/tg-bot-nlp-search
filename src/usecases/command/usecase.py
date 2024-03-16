from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src import schemas, states
from src.common.keyboard import KeyboardManager
from src.common.state import StateManager
from src.config import settings
from src.keyboards import KeyboardRepository
from src.services import ServiceRepository

from ..core import CoreUseCase


class CommandUseCase(CoreUseCase):
    services: ServiceRepository = ServiceRepository()
    keyboards: KeyboardRepository = KeyboardRepository()

    _cmd_start_msg: str = settings.message.command.START

    async def start(self, message: Message, state: FSMContext) -> None:
        user_id = message.from_user.id
        state_data = await StateManager.get_data(state)

        if state_data.last_inline_keyboard_message_id is not None:
            await KeyboardManager.remove_last_inline_keyboard(
                user_id=user_id,
                last_inline_keyboard_message_id=state_data.last_inline_keyboard_message_id,
            )

        await StateManager.clear(state)

        send_message = await message.answer(
            text=self._cmd_start_msg,
            reply_markup=self.keyboards.inline.command.start(),
        )

        await StateManager.update_data(
            state=state,
            data=schemas.StateData(
                last_inline_keyboard_message_id=send_message.message_id
            ),
        )
        await StateManager.set_state(
            state=state, next_state=states.CommandStatesGroup.START
        )
