"""Utility file that provide the additional method to the main"""
from typing import Callable

def find_item(list_dict: list[dict], cb: Callable) -> tuple[dict, int]:
    """receive a list of item, search through it and return the matching item with  its id"""
    for idx, item in enumerate(list_dict):
        if cb(item):
            return item, idx
    return {}, -1
