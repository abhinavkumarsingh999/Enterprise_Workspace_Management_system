import logging
import shutil
from pathlib import Path

import pytest

from src.core.logger import get_logger, system_diagnostics, CRITICAL_WARNING_LEVEL

TEST_LOG_DIR = Path("./test_logs_tmp")

@pytest.fixture(autouse=True)
def cleanup_logs() :
    yield
    logger = logging.getLogger("test_logger")
    for handler in logger.handlers[:] :
        handler.close()
        logger.removeHandler(handler)
    if TEST_LOG_DIR.exists() :
        shutil.rmtree(TEST_LOG_DIR, ignore_errors=True)
    logging.Logger.manager.loggerDict.pop("test_logger", None)
    
def test_get_logger_creates_handlers() :
    logger = get_logger("test_logger", log_dir=TEST_LOG_DIR, level="DEBUG")
    assert logger.level == logging.DEBUG
    assert len(logger.handlers) == 2  # Console and file handlers
    
def test_get_logger_is_idempotent() :
    logger1 = get_logger("test_logger", log_dir=TEST_LOG_DIR, level="DEBUG")
    logger2 = get_logger("test_logger", log_dir=TEST_LOG_DIR, level="DEBUG")
    assert logger1 is logger2
    assert len(logger1.handlers) == 2  # No duplicate handlers
    
def test_log_file_created_and_written() :
    logger = get_logger("test_logger", log_dir=TEST_LOG_DIR, level="DEBUG")
    logger.info("Test log entry.")
    
    for handler in logger.handlers :
        handler.flush()
        
    log_file = TEST_LOG_DIR / "test_logger.log"
    assert log_file.exists
    assert "Test log entry" in log_file.read_text()
    
def test_critical_warning_tier_registered() :
    assert logging.getLevelName(CRITICAL_WARNING_LEVEL) == "CRITICAL_WARNING"
    
    
def test_critical_warning_emits_at_correct_level(caplog) :
    logger = get_logger("test_logger", log_dir=TEST_LOG_DIR, level="DEBUG")
    logger.addHandler(caplog.handler)
    
    with caplog.at_level(CRITICAL_WARNING_LEVEL, logger = "test_logger") :
        logger.critical_warning("severe but non-fatal")
        
    assert any(r.levelno == CRITICAL_WARNING_LEVEL for r in caplog.records)
    
    
def test_system_diagnostics_keys() :
    diag = system_diagnostics()
    assert {"platform", "python_version", "processor", "cwd"} <= diag.keys()
    assert isinstance(diag["python_version"], str)