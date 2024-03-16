from abc import ABCMeta, abstractmethod


class ABCServiceRepository(metaclass=ABCMeta):
    @abstractmethod
    def nlp(self):
        raise NotImplementedError
