import json


class ALOCSpecReader:
    def __init__(self, path) -> None:
        with open(path) as json_file:
            self.__data = json.load(json_file)
