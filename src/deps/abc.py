from abc import ABCMeta, abstractmethod


class ABCDepsRepository(metaclass=ABCMeta):
    @abstractmethod
    def use_case(self):
        raise NotImplementedError
