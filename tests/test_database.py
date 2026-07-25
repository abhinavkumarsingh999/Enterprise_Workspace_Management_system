import pytest
import os

from src.database.connection import get_connection, close_connection

@pytest.mark.skipif(
    os.getenv("GITHUB_ACTIONS") == "true",
    reason="Skip database test on GitHub Actions"
)
def test_database_connection():
    """
    Test the database connection and ensure it can be established and closed properly.
    """
    connection = get_connection()
    
    assert connection is not None 
    
    close_connection(connection)