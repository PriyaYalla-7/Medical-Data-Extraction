import abc
class MedicalDoc_parse(metaclass=abc.ABCMeta):
    def __init__(self,text):
        self.text = text
    @abc.abstractmethod
    def parse(self):
        pass