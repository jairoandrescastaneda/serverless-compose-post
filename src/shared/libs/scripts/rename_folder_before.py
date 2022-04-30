import os
LOCATION_PATH = os.path.dirname(__file__)

path_python = f"{LOCATION_PATH}/../python"
path_src = f"{LOCATION_PATH}/../src"


def rename_folder_before():
    try:
        os.rename(path_src, path_python)
        print("Success")
    except Exception as error:
        print(f"The following error has occurred {error}")
        exit(1)

rename_folder_before()