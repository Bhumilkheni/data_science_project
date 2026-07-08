import sys

from src.Data_Science_Project.components.data_ingestion import DataIngestion

# from src.Data_Science_Project.components.data_ingestion import DataIngestionConfig
from src.Data_Science_Project.exception import CustomException
from src.Data_Science_Project.logger import logging

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception has been raised")
        raise CustomException(e, sys)
