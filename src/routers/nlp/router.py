from typing import Annotated

from aiogram import F, Router
from aiogram3_di import Depends
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src import filters, states
from src.deps import DepsRepository
from src.usecases import UseCaseRepository


router = Router()


@router.message(
    StateFilter(states.NLPStatesGroup.search),
    F.text,
    filters.InteractionWelcomeFilter(),
)
async def welcome_msg(
    message: Message,
    state: FSMContext,
    use_case: Annotated[UseCaseRepository, Depends(DepsRepository.use_case.get)],
) -> None:
    await use_case.nlp.welcome_msg(message=message, state=state)


@router.message(
    StateFilter(states.NLPStatesGroup.search),
    F.text,
    filters.InteractionGoodbyeFilter(),
)
async def goodbye_msg(
    message: Message,
    state: FSMContext,
    use_case: Annotated[UseCaseRepository, Depends(DepsRepository.use_case.get)],
) -> None:
    await use_case.nlp.goodbye_msg(message=message, state=state)


@router.message(
    StateFilter(states.NLPStatesGroup.search),
    F.text,
)
async def nlp_search_msg(
    message: Message,
    state: FSMContext,
    use_case: Annotated[UseCaseRepository, Depends(DepsRepository.use_case.get)],
) -> None:
    await use_case.nlp.nlp_search_msg(message=message, state=state)
