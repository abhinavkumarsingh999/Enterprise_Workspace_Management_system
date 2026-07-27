import sqlite3
from src.config.settings import DATABASE_NAME

def get_connection() :
    try:
        connection = None
        
        if connection is None :
            return False, "No database is found"
        
        return True, connection
    except Exception :
        return False, "No databse connection is found" 
    
def close_connection(connection) :
    if connection:
        try:
            connection.close()
        except sqlite3.Error as e:
            print(f"Error closing the database connection: {e}")