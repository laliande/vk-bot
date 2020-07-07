class InvalidData(Exception):
    def __init__(self, message='Please provide the correct token, group id and API version'):
        self.message = message
        super().__init__(self.message)


class BadMimetype(Exception):
    def __init__(self, message='please send data in json format'):
        self.message = message
        super().__init__(self.message)
