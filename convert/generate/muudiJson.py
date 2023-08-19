"""Muudi JSON generator
MuudiJson is a simple json template that is used as an agnostic go-between when generating documents.
Documnentation and disambiguation can be found in the muudiJson.md file in the top level of this repo.
"""


import logging

logger = logging.getLogger(__name__)

class muudiJSON:
    def __init__(self, filename):
        self.filename = filename + ".json"
        self.doc = []

    def __str__(self):
        return "".join(self.doc)
    
    def paragraph(self, text):
        self.doc.append({";pa": text})

    def title(self, text):
        self.doc.append({";ti": text})

    def heading(self, text):
        self.doc.append({";he": text})

    def subheading(self, text):
        self.doc.append({";sh": text})

    def subsubheading(self, text):
        self.doc.append({";ssh": text})

    def horizontal_rule(self):
        self.doc.append({";hr": "-----"})

    def code_block(self, text):
        self.doc.append({";cb": text})

    def bullet_list(self, items):
        self.doc.append({";bl": items})

    def numbered_list(self, items):
        self.doc.append({";nl": items})

    def new_line(self):
        self.doc.append({";nu": ""})

    def save_and_close(self):
        with open(self.filename, "w") as f:
            f.write(str(self))
