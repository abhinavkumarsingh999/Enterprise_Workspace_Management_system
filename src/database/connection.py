import sqlite3
from src.config.settings import DATABASE_NAME

def get_connection() :
    """
    Establishes a connection to the SQLite database.
    
    Returns:
        sqlite3.Connection: A connection object to the SQLite database.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None
    
def close_connection(connection) :
    """
    Closes the given database connection.
    
    Args:
        connection (sqlite3.Connection): The connection object to be closed.
    """
    if connection:
        try:
            connection.close()
        except sqlite3.Error as e:
            print(f"Error closing the database connection: {e}")