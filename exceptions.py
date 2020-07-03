class InvalidData(Exception):
    def __init__(self, message='Please provide the correct token, group id and API version'):
        self.message = message
        super().__init__(self.message)
