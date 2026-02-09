class Logger:
    def __init__(self):
        self.cache = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.cache or timestamp - self.cache[message] >= 10:
            self.cache[message] = timestamp
            return True
        return False
