"""Generate RST formatted documets"""

import logging

logger = logging.getLogger(__name__)


class ReStructuredText:
    def __init__(self, filename):
        self.filename = filename + ".rst"
        self.doc = []

    def __str__(self):
        return "\n".join(self.doc)

    def print(self):
        print(str(self))

    def paragraph(self, text):
        self.doc.append(text)
        self.doc.append("\n")

    def title(self, text):
        self.doc.append(f"=====\n{text}\n=====\n")

    def heading(self, text):
        self.doc.append(f"{text}\n=====\n")

    def subheading(self, text):
        self.doc.append(f"{text}\n-----\n")

    def subsubheading(self, text):
        self.doc.append(f"{text}\n~~~~~\n")

    def horizontal_rule(self):
        self.doc.append("-----\n")

    def code_block(self, text):
        self.doc.append(f"::\n{text}\n")

    def bullet_list(self, items):
        for item in items:
            self.doc.append(f"* {item}\n")
        self.doc.append("\n")

    def numbered_list(self, items):
        for item in items:
            self.doc.append(f"#. {item}\n")
        self.doc.append("\n")

    def new_line(self):
        self.doc.append("\n")

    def save_and_close(self):
        with open(self.filename, "w") as f:
            f.write(str(self))
