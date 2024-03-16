from aiogram import Router

from .abc import ABCRouterRepository
from .command import cmd_router
from .nlp import nlp_router


class RoutersRepository(ABCRouterRepository):
    command: Router = cmd_router
    nlp: Router = nlp_router
