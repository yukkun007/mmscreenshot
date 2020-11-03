import pathlib
from dotenv import load_dotenv


def load_env(dotenv_path: str) -> bool:
    env = pathlib.Path(dotenv_path)
    if not env.exists():
        print(".env file is not found. : [{}]".format(dotenv_path))
        return False

    load_dotenv(override=True, verbose=True, dotenv_path=dotenv_path)

    return True
