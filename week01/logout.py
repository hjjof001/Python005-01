#!/usr/bin/env python

import os
from datetime import datetime
import logging
import time
import pathlib


now_date = datetime.strftime(datetime.now(), "%Y-%m-%d")
LOG_DIR = pathlib.Path('/var/log').joinpath('python-{}'.format(now_date))
logfile = LOG_DIR.joinpath('xxxx.log')

def logToFile(logfilename=logfile):
    if not LOG_DIR.is_dir():
        try:
            os.makedirs(LOG_DIR)
        except OSError as err:
            print('Create log directory failed: {}'.format(err))

    logging.basicConfig(filename=logfile, 
                    level="DEBUG",
                    datefmt='%Y-%m-%d %X',
                    format="%(asctime)s %(name)s %(levelname)s [line: %(lineno)d] %(message)s"
                        )
    
    logging.info("The function logToFile is called.It's called in: {}".format(time.ctime()))


    
if __name__ == "__main__":
    logToFile()