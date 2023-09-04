import logging

def log():

    _filename = '../logs/logfile.log'
    _format = '%(asctime)s: %(levelname)s: %(message)s'
    _datefmt = '%m/%d%Y %I:%M:%S %p'

    logging.basicConfig(filename= _filename,format= _format, datefmt=_datefmt,level=logging.INFO)
    logger = logging.getLogger()
    return logger


