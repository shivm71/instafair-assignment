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

    try:
        log('Reading data......')
        readData()
        log('Reading data completed at', round(time.time() - start, 2), 'sec')
    except:
        log('Error while reading the data.Please check the input files or download the file from' +
            ' https://www.dropbox.com/s/1ao72uiciov4uxc/instacart_online_grocery_shopping_2017_05_01.tar.gz?dl=0 and place them in '
            + config.get('inputfilePath'), isExit=True)

    try:
        log('Processing Order data......')
        processData()
        log('Processing Order data completed at', round(time.time() - start, 2), 'sec')
    except:
        log('Error while Processing order data.Please check the order input file.', isExit=True)

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
