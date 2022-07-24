import time

from config.config import config
from csvUtil import processData, readData
from logger import log
from outputUtil import writeOutput


# sys.path.append("./src")
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
    try:
        log('Writing output data......')
        writeOutput()
        log('Writing data completed at', round(time.time() - start, 2), 'sec')
    except:
        log('Error while Writing order data.Please check folder permissions.', isExit=True)

    end = time.time()
    log("Programe execution time : ", round(end - start, 2), 'sec')
    log('--------------------End--------------------')


if __name__ == "__main__":
    run()
