from src.database.connection import get_connection, close_connection

def test_database_connection():
    """
    Test the database connection and ensure it can be established and closed properly.
    """
    connection = get_connection()
    
    assert connection is not None 
    
    close_connection(connection)