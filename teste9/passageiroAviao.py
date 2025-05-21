from abc import ABC, abstractmethod
class PassageiroAviao(ABC):

    @abstractmethod
    def fazer_check_in(self):
        pass

    @abstractmethod
    def passar_pela_seguranca(self):
        pass

    @abstractmethod
    def embarcar(self):
        pass

        