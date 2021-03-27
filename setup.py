from setuptools import setup, find_packages

PACKAGE_NAME = "mmscreenshot"

with open("README.md") as f:
    readme = f.read()

with open("VERSION") as f:
    version = f.read()

setup(
    # matadata
    name=PACKAGE_NAME,
    version=version,
    description="screen shot a part of html.",
    long_description=readme,
    author="Yutaka Kato",
    author_email="kato.yutaka@gmail.com",
    url="https://github.com/yukkun007/mmscreenshot",
    # liscence=
    # platform=
    # options
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=["python-dotenv==0.16.0", "selenium==3.141.0", "pillow==8.1.2"],
    entry_points="""
        [console_scripts]
        {app} = {app}.cli:main
    """.format(
        app=PACKAGE_NAME
    ),
)
