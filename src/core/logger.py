""" This is a simple logger helper for diagnostics scripts.
Logs to both console and a log file.
"Critical Warning" between warning and error.
"""

import logging
import os
import sys
import platform
from logging.handlers import RotatingFileHandler
from pathlib import Path

# creating new logging level -> CRITICAL_WARNING
CRITICAL_WARNING_LEVEL = 35
logging.addLevelName(CRITICAL_WARNING_LEVEL, "CRITICAL_WARNING")

class AppLogger(logging.Logger) :
    # new method adding called critical_warning to logger
    def critical_warning(self, msg, *args, **kwargs) :
        if self.isEnabledFor(CRITICAL_WARNING_LEVEL) :
            self._log(CRITICAL_WARNING_LEVEL, msg, args, **kwargs)
            
            
# applogger class is used instead of normal one        
logging.setLoggerClass(AppLogger)

# format of log when gets printed
LOG_FORMAT = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def get_logger(name = "enterprise_app", log_dir = "./logs", level = "INFO") :
    logger = logging.getLogger(name)
    
    if logger.handlers :
        return logger
    
    logger.setLevel(level.upper())
    
    formatter = logging.Formatter(LOG_FORMAT, datefmt = DATE_FORMAT)
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # create log directory if it doesn't exist
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    
    file_handler = RotatingFileHandler(
        Path(log_dir) / f"{name}.log", maxBytes=5*1024*1024, backupCount=5
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    logger.propagate = False
    
    return logger


def system_diagnostics() :
    return {
        "platform" : platform.platform(),
        "python_version" : platform.python_version(),
        "processor" : platform.processor() or "unknown",
        "cwd" : os.getcwd(),
    }