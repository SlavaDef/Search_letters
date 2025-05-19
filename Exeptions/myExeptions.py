class CredentialsError(Exception):
    pass


class SQLError(Exception):
    def __init__(self, message: str, original_error: Exception = None):
        self.message = message
        self.original_error = original_error
        super().__init__(self.message)


class DatabaseConnectionError(Exception):
    """Власне виключення для помилок з'єднання з базою даних"""
    def __init__(self, message: str, original_error: Exception = None):
        self.message = message
        self.original_error = original_error
        super().__init__(self.message)

