import re
import logging
from data_ingestion import read_csv_web

class WeatherDataProcessor:
    def __init__(self, config_params, logging_level='INFO'):
        self.weather_url = config_params['weather_url']
        self.patterns = config_params['regex_patterns']
        self.weather_df = None
        self.initialize_logging(logging_level)
    
    def initialize_logging(self, logging_level):
        logger_name = __name__ + ".WeatherDataProcessor"
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
    
    def weather_station_data(self):
        try:
            self.weather_df = read_csv_web(self.weather_url)
            self.logger.info("Weather data loaded successfully.")
        except Exception as e:
            self.logger.error(f"Error loading weather data: {e}")
            raise e
    
    def extract_measurement(self, message):
        for key, pattern in self.patterns.items():
            match = re.search(pattern, message)
            if match:
                self.logger.debug(f"Extracted {key} from message: {message}")
                return key, float(next((x for x in match.groups() if x is not None)))
        
        self.logger.warning(f"No measurement found in message: {message}")
        return None, None
    
    def process_messages(self):
        if self.weather_df is not None:
            result = self.weather_df['Message'].apply(self.extract_measurement)
            self.weather_df['Measurement'], self.weather_df['Value'] = zip(*result)
            self.logger.info("Processed weather messages to extract measurements.")
        else:
            self.logger.warning('Weather DataFRame is not loaded. Cannot process messages.')
        return self.weather_df
    
    def calculate_average(self):
        if self.weather_df is not None:
            averages = self.weather_df.groupby(by=['Weather_station_ID','Measurement'])['Value'].mean()
            self.logger.info("Calculated average values for each measurement.")
            return averages.unstack()
        else:
            self.logger.warning('Weather DataFrame is not loaded. Cannot calculate averages.')
            return None
        
    def process(self):
        self.weather_station_data()
        self.process_messages()
        averages = self.calculate_average()
        if averages is not None:
            self.logger.info("Weather data processing completed successfully.")