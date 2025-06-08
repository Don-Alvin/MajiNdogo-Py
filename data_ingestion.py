# Data Ingestion Module
# This module provides functions to create a database engine, execute SQL queries,
# and read CSV files from a web URL into a pandas DataFrame.
import pandas as pd
from sqlalchemy import create_engine, text
import logging


# Configure logging
logger = logging.getLogger('data_ingestion')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Function Definitions
# Function to create a database engine
def create_db_engine(db_path):
    """
    Creates and returns a SQLAlchemy database engine from a specified database path.
        
    This function logs the creation process, verifies the connection, and checks for errors.
        
    Parameters:
        db_path (str): The database path or connection string for creating the engine.
    
    Returns:
        sqlalchemy.engine.Engine: A SQLAlchemy engine object for interacting with the database.
            
    Raises:
        ImportError: If SQLAlchemy is not installed.
        Exception: If there is an error in creating the database engine, 
                    a detailed error message is logged and the exception is raised.
    """

    try:
        engine = create_engine(f'sqlite:///{db_path}')
        with engine.connect() as connection:
            # Check if the connection is successful
            pass
        logger.info(f"Database engine created successfully for {db_path}")
        return engine
    except ImportError as e:
        logger.error(f"Error importing SQLAlchemy: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error creating database engine: {e}")
        raise e

def query_to_dataframe(engine, sql_query):
    """
    Executes a SQL query using a provided SQLAlchemy engine and returns the results as a DataFrame.

    This function establishes a connection to the database engine, executes the given SQL query,
    and retrieves the results as a Pandas DataFrame. If the query returns an empty result, an 
    appropriate error is logged and raised.

    Parameters:
        engine (sqlalchemy.engine.Engine): The SQLAlchemy engine used to connect to the database.
        sql_query (str): The SQL query to execute on the database.

    Returns:
        pd.DataFrame: A DataFrame containing the query results.

    Raises:
        ValueError: If the query returns an empty DataFrame.
        Exception: For any other error that occurs during query execution, including connection or query errors.
        
    Logs:
        - Logs a success message if the query executes and returns data successfully.
        - Logs an error if the query returns an empty result or if there is any error during execution.
    """
    try:
        with engine.connect() as connection:
            df = pd.read_sql_query(text(sql_query), connection)
        if df.empty:
            logger.error("Query returned an empty DataFrame.")
        else:
            logger.info(f"Query executed successfully, returned {len(df)} rows.")
        return df
    except ValueError as e:
        logger.error(f"ValueError in query execution: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error executing query: {e}")
        raise e
    
def read_csv_web(url):
    """
    Converts a csv file into a pandas dataframe. 
    
    If the url doest not link to a valid csv file, it logs
    an appropiate error message, otherwise, it logs a success message

    Parameter:
        URL (str): URL link to a csv
    Returns:
        A pandas dataframe
    Raises:
        EmptyDataError: If the URL does not point to a valid csv file .
        Exception: If the dunctions fails to read the csv form the URL provided.
    Logs:
        Logs a success message if the functions successfully reads the csv file.
        Logs error if the url does not link to a valid csv fil or another error occurs.
    """
        
    try:
        df = pd.read_csv(url)
        logger.info(f"CSV file read successfully from {url}, returned {len(df)} rows.")
        return df
    except pd.errors.EmptyDataError as e:
        logger.error(f"EmptyDataError: No data found at {url}.")
        raise e
    except pd.errors.ParserError as e:
        logger.error(f"ParserError: Error parsing CSV file from {url}.")
        raise e
    except Exception as e:
        logger.error(f"Error reading CSV file from {url}: {e}")
        raise e