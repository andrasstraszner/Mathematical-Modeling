import os
import pathlib

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
