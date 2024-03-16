from src.keyboards import KeyboardRepository
from src.services import ServiceRepository

from ..core import CoreUseCase


class NLPUseCase(CoreUseCase):
    services: ServiceRepository = ServiceRepository()
    keyboards: KeyboardRepository = KeyboardRepository()
