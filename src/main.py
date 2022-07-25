import os
import sys
import time

from config.config import config
from utils.csvUtil import processData, readData
from utils.logger import log
from utils.outputUtil import writeOutput

# print(sys.path)


def run():
    start = time.time()
    log('-------------Fairmatic Assignment-------------')
    log('-------------------Start-------------------')

    log('Reading data......')
    readData()
    log('Reading data completed at', round(time.time() - start, 2), 'sec')

    log('Processing Order data......')
    processData()
    log('Processing Order data completed at', round(time.time() - start, 2), 'sec')

    log('Writing output data......')
    writeOutput()
    log('Writing data completed at', round(time.time() - start, 2), 'sec')

    end = time.time()

    log("Programme execution time : ", round(end - start, 2), 'sec')
    log('--------------------End--------------------')


def checkOrCreateDir():
    try:
        os.mkdir(config.getPath('inputfilePath'))
        log('Input Folder structure created.')
    except:
        pass

    try:
        os.mkdir(config.getPath('outputFilePath'))
        log('Output Folder structure created.')
    except:
        pass


if __name__ == "__main__":
    log('Please check the config file for setup in src/config/config.py')
    checkOrCreateDir()
    run()
