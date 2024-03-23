import setuptools

setuptools.setup(
    name="launch_lever",
    version="1.0.0",
    description="Manage feature toggles(flags) quickly",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
)
