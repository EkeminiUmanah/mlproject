import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    # Configuration class for data ingestion with default file paths
    train_data_path:str=os.path.join('artifacts',"train.csv")
    test_data_path:str=os.path.join('artifacts',"test.csv")
    raw_data_path:str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        # Method to perform data ingestion
        logging.info("Entered the data ingestion method or component")
        try:
            # Read data from 'notebook\data\stud.csv'
            df=pd.read_csv('notebook\data\stud.csv') 
            logging.info("Read the dataset as DataFrame")

            # Create directories for the output files if they don't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            # Save the raw data to a CSV file
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            # Split the data into training and testing sets
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

             # Save the training and testing sets to CSV files
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data ingestion completed")

            return(
                # Return the file paths for the training and testing sets
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            # Raise a custom exception in case of an error
            raise CustomException(e,sys)
        
if __name__=="__main__":
    # If this script is run directly, perform data ingestion and transformation
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr, test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))

