from .abc import ABCServiceRepository
from .nlp import NLPService


class ServiceRepository(ABCServiceRepository):
    nlp: NLPService = NLPService()
