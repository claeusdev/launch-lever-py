from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="launch_lever",
    author="Nana Adjei Manu",
    version="1.0.0",
    description="Manage feature toggles(flags) quickly",
    packages=find_packages("src"),
    package_dir={"": "src"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/claeusdev/launch-lever-py"
)
