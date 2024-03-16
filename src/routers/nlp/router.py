from typing import Annotated

from aiogram import Router
from aiogram3_di import Depends
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.deps import DepsRepository
from src.usecases import UseCaseRepository


router = Router()


@router.message()
async def some_msg(
    message: Message,
    state: FSMContext,
    use_case: Annotated[UseCaseRepository, Depends(DepsRepository.use_case.get)],
) -> None:
    await use_case.command.start(message=message, state=state)
