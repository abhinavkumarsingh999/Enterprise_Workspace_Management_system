from src.logger.logger import get_logger
from scripts.diagnostics import diagnostics
from src.database.connection import get_connection, close_connection
from src.config.settings import DATABASE_NAME, DEBUG, APP_NAME

def main():
    logger = get_logger("main")
    logger.info("Application Started")
    
    print("\n Application Configuration:")
    print(f"Application Name: {APP_NAME}")
    print(f"Debug Mode: {DEBUG}")
    print(f"Database Name: {DATABASE_NAME}")
    
    print("\n System Diagnostics")
    system_info = diagnostics()
    
    for key, value in system_info.items():
        print(f"{key}: {value}")
        
    print(" \n Database Connection Test")
    try:
        connection = get_connection()
        print("Database connection established successfully.")
        logger.info("Database connection established successfully.")
        close_connection(connection)
        print("Database connection closed successfully.")
        logger.info("Database connection closed successfully.")
        
    except Exception as error:
        print(f"Error occurred while testing database connection: {error}")
        logger.error(f"Error occurred while testing database connection: {error}")
        
    print("\n Application Finished")
    logger.info("Application Finished")
    
if __name__ == "__main__":
    main()