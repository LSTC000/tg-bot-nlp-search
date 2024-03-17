from aiogram.fsm.state import State

from ..core import CoreStatesGroup


class NLPStatesGroup(CoreStatesGroup):
    search = State()
