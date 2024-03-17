from ..core import CoreMessageSettings


class MessageInteractionSettings(CoreMessageSettings):
    WELCOME: str = "🤖Привет, что ты хочешь узнать?"
    GOODBYE: str = "До новых встреч 🫡"

    WELCOME_LIST: list[str] = [
        "привет",
        "ку",
        "прив",
        "добрый день",
        "доброго времени суток",
        "здравствуйте",
        "приветствую",
    ]
    GOODBYE_LIST: list[str] = ["пока", "стоп", "выход", "конец", "до свидания"]
