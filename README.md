## Launch-Lever 

The easiest way to manage feature toggles in applications.

### Features
- Currently only supports managing feature toggles using JSON
- Should be super fast 💨

### About

`launch-lever` is a simple library for managing your feature toggles. 

Launch-lever is for you if you want:

- A simple locally managed feature toggle.
- Something so simple you don't need to know how to make network calls to use.
- Load a JSON file and toggle away.

### Installation

To add `launch-lever` to your project:

```py
pip install launch-lever
```

### Usage

launch-lever exports a class `LaunchLever`.

```py
from launch-lever import LaunchLever;

# pass a file to the constructor
lever = LaunchLever("./toggles.json")

# load() parses the file and loads the toggles in memory
lever.load()
```
Use your toggle names by simply checking if they're turned `on` with the very handy `is_on` function.
`is_on` accepts the name of a toggle and returns `True` or `False` based on the `status` of the toggle.

```py
# returns true if the toggle is present and status is `on`
if is_on("pfx_223"):
  ## do something if our toggle `pfx_223` is turned on
```

### Contributing and Support

If you're interested in contributing or supporting. Just fork, open a PR.
