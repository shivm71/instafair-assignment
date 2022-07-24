import os

def log(*args,isExit = False):
    for log in args:
        print(log,end=' ')
    print()
    if isExit:
        print('Programme closed unexpectedly Please check logs and rerun.')
        print('--------------------End--------------------')
        os.abort()