from __future__ import annotations
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.logger.logger import get_logger, system_diagnostics

def diagnostics() :
    return system_diagnostics()


def main() :
    logger = get_logger("diagnostics", log_dir="./logs", level="DEBUG")
    
    logger.debug("Diagnostics run starting...")
    logger.info("Collecting system information...")
    
    diagnostics = system_diagnostics()
    for key in diagnostics:
        value = diagnostics[key]
        logger.info(key + ": " + str(value))
        
    logger.warning("This is a standard warning tier example.")
    logger.critical_warning("This is a critical warning tier example.")
    
    try :
        x = 1 / 0
    except Exception as e :
        logger.error("Caught an sample exception during diagnostics.", exc_info=True)
        
        logger.info("Diagnostics run complete.")
        

main()