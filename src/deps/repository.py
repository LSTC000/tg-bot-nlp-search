from .abc import ABCDepsRepository
from .usecase import UseCaseDeps


class DepsRepository(ABCDepsRepository):
    use_case: UseCaseDeps = UseCaseDeps()
