from abc import abstractmethod


class FileParser:
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def parse(self):
        pass
