import os
import sys


config = {
    "inputfilePath" : "files/csv/",
    "maxChunkSize": 1000000,
    "outputFilePath":"files/output/",
    "outputFileName":"output.txt"
}

def getPath(key:str):
    return os.path.join(sys.path[0],config.get(key))
