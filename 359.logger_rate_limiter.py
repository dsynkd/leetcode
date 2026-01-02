class Logger:

    def __init__(self):
        self.messages = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messages:
            self.messages[message] = timestamp
            return True
        diff = timestamp - self.messages[message]
        if diff <= 10:
            return False
        else:
            self.messages[message] = timestamp
            return True
