import sys

from config.config import config, getPath
from filter import depts, outputDto
from logger import log


def writeOutput():
    orig_stdout = sys.stdout
    f = open(getPath('outputFilePath') + config.get('outputFileName'), 'w')
    sys.stdout = f
    for daykey, day in outputDto.items():
        print('day: ' + str(daykey))
        for hourkey, hour in day.items():
            print('   hour: ' + str(hourkey))
            total = sum(hour.values())
            for deptKey, dept in hour.items():
                print('      ' + str(deptKey) + '. ' +
                      str(depts[deptKey + 1]).title() + ' -> ' + str(int((int(dept) / total) * 100)) + '%')
    sys.stdout = orig_stdout
    log('Please check files/output/' + config.get('outputFileName') + " for output file.")
    f.close()
