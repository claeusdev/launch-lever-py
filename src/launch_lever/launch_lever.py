from parsers.json_parser import JSONParser


class LaunchLever:
    def __init__(self, filename="./toggles.json"):
        self.filename = filename
        self._toggles = []

    @property
    def toggles(self):
        return self._toggles

    def load_toggles(self):
        self._toggles = JSONParser(self.filename).parse()

    def find(self, toggle_name):
        for toggle in self._toggles:
            if toggle.name == toggle_name:
                return toggle

    def is_on(self, toggle_name):
        toggle = self.find(toggle_name)
        if not toggle:
            return False
        return toggle.status == "on"


# lever = LaunchLever("./toggles.json")
# lever.load_toggles()
# print(lever.is_on("pfx_223"))
