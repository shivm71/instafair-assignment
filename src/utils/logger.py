import os

from config.config import config


def log(*args, isExit=False, errorCode=None):
    for log in args:
        print(log, end=' ')
    if not isExit:
        print()
    if isExit:
        if errorCode and errorCode in config:
            print(config.get(errorCode))
        print('Programme closed unexpectedly Please check logs and rerun.')
        print('--------------------End--------------------')
        os.abort()
