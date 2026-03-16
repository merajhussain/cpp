from abc import ABC,abstractmethod
class Ilist:

    @abstractmethod
    def append(self,item):
        pass
    @abstractmethod
    def deleteNode(self,item):
        pass
    @abstractmethod
    def to_string(self):
        pass
    @abstractmethod
    def prepend(self,item):
        pass
