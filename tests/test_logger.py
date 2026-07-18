import logging
import shutil
from pathlib import Path

import pytest

from src.core.logger import get_logger, system_diagnostics, CRITICAL_WARNING_LEVEL

TEST_LOG_DIR = Path("./test_logs_tmp")
