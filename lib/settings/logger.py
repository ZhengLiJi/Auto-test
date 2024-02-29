import os
import logging
import time
from lib.settings.file_path import FilePath
from loguru import logger as log

start_time = time.strftime('%Y-%m-%d', time.localtime())


def set_file_handler():
    """
    文件handler
    """
    log_path = FilePath.LogPath
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    log_file = os.path.join(log_path, f"log_{start_time}.log")
    log.add(log_file, level=logging.DEBUG, rotation="50 MB", retention="3 days", backtrace=True, diagnose=True)


set_file_handler()

if __name__ == '__main__':
    log.info("asd")
