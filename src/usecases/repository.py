from .abc import ABCUseCaseRepository
from .command import CommandUseCase
from .nlp import NLPUseCase


class UseCaseRepository(ABCUseCaseRepository):
    command: CommandUseCase = CommandUseCase()
    nlp: NLPUseCase = NLPUseCase()
