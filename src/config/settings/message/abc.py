from abc import ABCMeta, abstractmethod


class ABCMessageSettings(metaclass=ABCMeta):
    @abstractmethod
    def nlp(self):
        raise NotImplementedError

    @abstractmethod
    def command(self):
        raise NotImplementedError

    @abstractmethod
    def interaction(self):
        raise NotImplementedError
