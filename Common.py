"""
collection of commonly used methods
"""
import os
import pathlib
from tqdm import tqdm


def get_folder_info(path):
    """get folder info for folders containing files"""
    folder_path = pathlib.Path(path)
    folder_info = []
    for root, _, files in os.walk(folder_path):
        if len(files) > 0:
            folder_info.append((root, len(files), files))
    return folder_info


def get_file_counts(folder_info):
    """count files"""
    return map(lambda f: (f[0], len(f[1]), folder_info))


def get_class(path):
    """get name of containing folder"""
    return path.split('\\')[-1]


def get_category(path):
    """get name of folder above containing folder"""
    return path.split('\\')[-2]


def clean_folder(path):
    """clean files, preserve folders"""
    for root, _, files in tqdm(os.walk(path, topdown=False), desc="Folders", leave=True):
        for f in tqdm(files, desc=root, leave=True):
            os.remove(os.path.join(root, f))
