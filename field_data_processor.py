import logging
from data_ingestion import create_db_engine, query_to_dataframe, read_csv_web

class FieldDataProcessor:
    def __init__(self, config_params, logging_level='INFO'):
        self.db_path = config_params['db_path']
        self.sql_query = config_params['sql_query']
        self.columns_to_rename = config_params['columns_to_rename']
        self.values_to_rename = config_params['values_to_rename']
        self.weather_map_url = config_params['weather_map_url']

        self.initialize_logging(logging_level)

        self.df = None
        self.engine = None

    def initialize_logging(self, logging_level):
        logger_name = __name__ + ".FieldDataProcessor"
        self.logger = logging.getLogger(logger_name)
        self.logger.propagate = False

        if logging_level.upper() == 'DEBUG':
            log_level = logging.DEBUG
        elif logging_level.upper() == 'INFO':
            log_level = logging.INFO
        elif logging_level.upper() == 'NONE':
            self.logger.disabled = True
        else:
            log_level = logging.INFO
        
        self.logger.setLevel(log_level)

        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def ingest_sql_data(self):
        self.engine = create_db_engine(self.db_path)
        self.df = query_to_dataframe(self.engine, self.sql_query)
        self.logger.info("Loaded data from SQL database.")
        return self.df
    
    def rename_columns(self):
        if self.df is not None:
            self.df.rename(columns=self.columns_to_rename, inplace=True)
            self.logger.info("Renamed columns in DataFrame.")
        else:
            self.logger.error("DataFrame is empty. Cannot rename columns.")
        return self.df
    
    def correct_crop_types(self):
        if self.df is not None:
            self.df['Crop_type'] = self.df['Crop_type'].replace(self.values_to_rename)
            self.logger.info("Corrected crop types in DataFrame.")
        else:
            self.logger.error("DataFrame is empty. Cannot correct crop types.")
        return self.df
    
    def weather_station_mapping(self):
        # Join weather data from csv to the main DataFrame
        weather_df = read_csv_web(self.weather_map_url)
        if weather_df is not None:
            self.df = self.df.merge(weather_df, on='Field_ID', how='left')
            self.logger.info("Joined weather data to the main DataFrame.")
        else:
            self.logger.error("Failed to load weather data from CSV.")
        return self.df  
    
    def process_data(self):
        self.logger.info("Starting data processing...")
        self.ingest_sql_data()
        self.rename_columns()
        self.correct_crop_types()
        self.weather_station_mapping()
        self.logger.info("Data processing completed.")
        return self.df
