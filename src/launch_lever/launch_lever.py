from .toggle import Toggle


class LaunchLever:
    def __init__(self, toggle_data, filename=None):
        self.toggles = toggle_data
        self.filename = filename

    @property
    def toggles(self):
        return self._toggles

    @toggles.setter
    def toggles(self, toggles):
        self._toggles = toggles

    def _get_toggle(self, toggle_name):
        toggle = {}
        for t in self.toggles:
            if t["name"] == toggle_name:
                toggle = t
        return Toggle(
            name=toggle["name"],
            description=toggle["description"],
            status=toggle["status"],
        )

    def is_on(self, toggle_name):
        toggle = self._get_toggle(toggle_name)
        if not toggle:
            return False
        return toggle.status == "on"
