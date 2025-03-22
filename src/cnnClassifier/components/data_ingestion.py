import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfigEntity
from cnnClassifier.exception import MyException
import sys


class DataIngestion:
    def __init__(self, config:DataIngestionConfigEntity):
        self.config = config
        
    def download_files(self) ->str:
        """
        Basically it downloads the data file from the gdrive from the given url
        
        """
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file_path
            os.makedirs("artifacts/data_ingestion", exist_ok= True)
            logger.info(f"Downloading the dataset from the  {dataset_url} into file {zip_download_dir}")
            
            file_id = dataset_url.split("/")[-2]
            prefix_id = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix_id+file_id, zip_download_dir)
            logger.info(f"Downloaded data from the {dataset_url} successfully")
            
        except Exception as e:
            raise MyException(e, sys)
        
        
        
    def extract_zip_file(self):
        """
        zip_file_path:str
        Exctracts the zip file into the data directory
        
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok= True)
        with zipfile.ZipFile(self.config.local_data_file_path, 'r') as zip_file_tobe:
            zip_file_tobe.extractall(unzip_path)