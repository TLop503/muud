import logging
import json

import generate.rst_gen as rst_gen

# eventually once argparse is implemented this will be updated to take paramaters.
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class Converter:
    def convert(file_path):
        # instatiate the rst generator:
        rst = rst_gen.RST()

        # open and read the document:
        with open(file_path, "r") as f:
            data = json.load(f)

        for item in data:
            """The key is the type of element, the value is the content of the element.
            Translations for keys can be found in muudiJson.py in the top level of this repo."""
            for key, value in item.items():
                if key == ";pa":
                    rst.paragraph(value)
                elif key == ";ti":
                    rst.title(value)
                elif key == ";he":
                    rst.heading(value)
                elif key == ";sh":
                    rst.subheading(value)
                elif key == ";ssh":
                    rst.subsubheading(value)
                elif key == ";hr":
                    rst.horizontal_rule()
                elif key == ";cb":
                    rst.code_block(value)
                elif key == ";bl":
                    rst.bullet_list(value)
                elif key == ";nl":
                    rst.numbered_list(value)
                elif key == ";nu":
                    rst.new_line()
                else:
                    logger.error(f"Unknown key: {key} with value: {value}")
        rst.save_and_close()

if __name__ == "__main__":
    Converter.convert("../test.json")
