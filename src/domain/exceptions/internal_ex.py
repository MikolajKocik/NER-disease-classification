class InternalException(Exception):
    """
    General exception type if something went wrong...
    """
    def __init__(self, message: str = "Unexpected server error occurred"):
        self.message = message
        super().__init__(self.message)