import os
import sys
import pathlib
from dotenv import load_dotenv


def load_env(dotenv_path: str) -> bool:
    env = pathlib.Path(dotenv_path)
    if not env.exists():
        print(".env file is not found. : [{}]".format(dotenv_path))
    else:
        load_dotenv(override=True, verbose=True, dotenv_path=dotenv_path)

    __check_env("CHROME_BINARY_LOCATION")
    __check_env("CHROME_DRIVER_LOCATION")

    return True


def __check_env(key: str):
    value = os.environ.get(key)
    if not value:
        print(f"Not found environment variable. key={key}")
        sys.exit(1)
    print(f"env | {key}={value}")
