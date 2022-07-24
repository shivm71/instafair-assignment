import os
import sys
#  module importing from src
sys.path.insert(0,'./src')

from logger import log
from main import run
from config.config import config


if __name__ ==  "__main__":
    log('Please check the config file for setup')
    try:
        os.mkdir(os.path.join(sys.path[0],config.get('inputfilePath')))
        log('Input Folder created.')
    except:
        pass
    run()