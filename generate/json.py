import logging

logger = logging.getLogger(__name__)

class Json:
    def __init__(self, filename):
        self.filename = filename + ".json"
        self.doc = []

    def __str__(self):
        return "\n".join(self.doc)