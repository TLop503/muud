"""Class for generating markdown files. Currently does not use double-space newlines."""

class Markdown:
    def __init__(self, filename):
        self.filename = filename + ".md"
        self.doc = []

    def __str__(self):
        return "\n".join(self.doc)

    def print(self):
        print(str(self))

    def paragraph(self, text):
        self.doc.append(text)
        self.doc.append("\n")

    def title(self, text):
        self.doc.append(f"# {text}\n")

    def heading(self, text):
        self.doc.append(f"## {text}\n")

    def subheading(self, text):
        self.doc.append(f"### {text}\n")

    def subsubheading(self, text):
        self.doc.append(f"#### {text}\n")

    def horizontal_rule(self):
        self.doc.append("-----\n")

    def code_block(self, text):
        self.doc.append(f"```\n{text}\n```\n")

    def bullet_list(self, items):
        for item in items:
            self.doc.append(f"* {item}\n")
        self.doc.append("\n")

    def numbered_list(self, items):
        index = 1
        for item in items:
            self.doc.append(f"{index}. {item}\n")
            index += 1
        self.doc.append("\n")

    def new_line(self):
        self.doc.append("\n")

    def save_and_close(self):
        with open(self.filename, "w") as f:
            f.write(str(self))
