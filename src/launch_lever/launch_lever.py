from parsers.json_parser import JSONParser


class Condition:
    def __init__(self, role):
        self.required_role = role


class LaunchLever:
    def __init__(self, filename="./toggles.json"):
        self.filename = filename
        self._toggles = []

    @property
    def toggles(self):
        return self._toggles

    def from_file(self, filename="./toggles.json"):
        self._toggles = JSONParser(self.filename).parse()

    def get(self, toggle_name):
        for toggle in self._toggles:
            if toggle.name == toggle_name:
                return toggle

    def is_enabled(self, toggle_name):
        toggle = self.find(toggle_name)
        return toggle.is_enabled


# lever = LaunchLever("./toggles.json")
# lever.from_file()
# print(lever.is_on("pfx_223"))
