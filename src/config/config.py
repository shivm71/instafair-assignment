import os
import sys

config = {
    "inputfilePath": "files/csv/",
    "maxChunkSize": 100000,
    "outputFilePath": "files/output/",
    "outputFileName": "output.txt",
    "fileError": 'Error while reading the data.Please check the input files or download the file from' +
                 ' https://www.dropbox.com/s/1ao72uiciov4uxc/instacart_online_grocery_shopping_2017_05_01.tar.gz?dl=0 and place them in src/files/csv/'

}


def getPath(key: str):
    return os.path.join(sys.path[0], config.get(key))
