import os


def log(*args, isExit=False,errorCode):
    for log in args:
        print(log, end=' ')
    if not isExit:
        print()
    if isExit:
        print('Programme closed unexpectedly Please check logs and rerun.')
        print('--------------------End--------------------')
        os.abort()
