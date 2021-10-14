from setuptools import setup

LIB_NAME = "moz-screenshot"
PACKAGE_NAME = "moz_screenshot"

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    # matadata
    name=LIB_NAME,
    version="0.1.0",
    description="Screen shot a part of html.",
    long_description=readme,
    author="mozkzki",
    author_email="mozkzki@gmail.com",
    url="https://github.com/mozkzki/moz-screenshot",
    liscence="MIT",
    packages=[PACKAGE_NAME],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=["python-dotenv==0.19.1", "selenium==3.141.0", "Pillow==8.3.2"],
)
