import os

LOCATION_PATH = os.path.dirname(__file__)

path_python = f"{LOCATION_PATH}/../python"
path_src = f"{LOCATION_PATH}/../src"


def rename_folder_after():
    try:
        os.rename(path_python, path_src)
        print("Success")
    except Exception as error:
        print(f"The following error has occurred {error}")


rename_folder_after()