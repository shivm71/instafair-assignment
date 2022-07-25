import sys

from config.config import config, getPath
from utils.filter import depts, outputDto
from utils.logger import log


def writeOutput():
    orig_stdout = sys.stdout
    f = open(getPath('outputFilePath') + config.get('outputFileName'), 'w')
    sys.stdout = f
    try:
        for daykey, day in outputDto.items():
            print('day: ' + str(daykey))
            for hourkey, hour in day.items():
                print('   hour: ' + str(hourkey))
                total = sum(hour.values())
                for deptKey, dept in hour.items():
                    print('      ' + str(deptKey) + '. ' +
                          str(depts[deptKey + 1]).title() + ' -> ' + str(int((int(dept) / total) * 100)) + '%')
    except:
        raise Exception
    sys.stdout = orig_stdout
    log('Please check files/output/' + config.get('outputFileName') + " for output file.")
    f.close()
