class ModelUnavailableException(Exception):
    """
    Occur when model is unavailable
    """
    def __init__(self, message: str = "Model service is currently unavailable"):
        self.message = message
        super().__init__(self.message)
