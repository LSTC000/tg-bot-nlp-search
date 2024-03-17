from .abc import ABCMessageSettings
from .command import MessageCommandSettings
from .interaction import MessageInteractionSettings
from .nlp import MessageNLPSettings


class MessageSettings(ABCMessageSettings):
    nlp: MessageNLPSettings = MessageNLPSettings()
    command: MessageCommandSettings = MessageCommandSettings()
    interaction: MessageInteractionSettings = MessageInteractionSettings()
