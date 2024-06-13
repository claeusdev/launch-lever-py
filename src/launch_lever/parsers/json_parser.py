from toggle import Toggle
from parsers.parser import FileParser


class JSONParser(FileParser):
    def parse(self):
        import json

        toggles = None
        with open(self.filename, "r") as f:
            data = json.load(f)
            toggles = [
                Toggle(
                    name=toggle["name"],
                    description=toggle["description"],
                    status=toggle["status"],
                )
                for toggle in data
            ]

        return toggles
