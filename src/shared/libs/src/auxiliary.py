from typing import Union


def convert_data(data:Union[int, float]):
    if isinstance(data, int) or isinstance(data, float):
        return str(data)
    return data