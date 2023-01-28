import os
import pathlib
from tqdm import tqdm

def getFolderInfo(path):
    folderPath = pathlib.Path(path)
    folderInfo = []
    for root, dirs, files in os.walk(folderPath):
        if len(files) > 0:
            folderInfo.append((root, dirs, files))
    return folderInfo

def getClass(path):
    return path.split('\\')[-1]

def getCategory(path):
    return path.split('\\')[-2]


def CleanFolder(path):
    for root, dirs, files in tqdm(os.walk(path, topdown=False), desc="Folders", leave=True):
        for f in tqdm(files, desc=root, leave=True):
            os.remove(os.path.join(root, f))
