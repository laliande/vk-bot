from exceptions import BadMimetype


class Validation:
    def __init__(self, data):
        if data is None:
            raise BadMimetype
        else:
            self.data = data


class ValidationForGroup(Validation):
    pass


class ValidationForMessages(Validation):
    pass
