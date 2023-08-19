import logging
import json

import generate.md_gen as md_gen

# eventually once argparse is implemented this will be updated to take paramaters.
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


#does this need to be a class? More research needed.
class Converter:
    def convert(file_path):
        # instatiate the markdown generator:
        md = md_gen.Markdown()

        # open and read the document:
        with open(file_path, "r") as f:
            data = json.load(f)

        # convert the document:
        for item in data:
            """The key is the type of element, the value is the content of the element.
            Translations for keys can be found in muudiJson.py in the top level of this repo."""
            for key, value in item.items():
                if key == ";pa":
                    md.paragraph(value)
                elif key == ";ti":
                    md.title(value)
                elif key == ";he":
                    md.heading(value)
                elif key == ";sh":
                    md.subheading(value)
                elif key == ";ssh":
                    md.subsubheading(value)
                elif key == ";hr":
                    md.horizontal_rule()
                elif key == ";cb":
                    md.code_block(value)
                elif key == ";bl":
                    md.bullet_list(value)
                elif key == ";nl":
                    md.numbered_list(value)
                elif key == ";nu":
                    md.new_line()
                else:
                    logger.error(f"Unknown key: {key} with value: {value}")
        md.save_and_close()


if __name__ == "__main__":
    Converter.convert("../test.json")
