from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME = "DATA_INGESTION_STAGE"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config= data_ingestion_config)
        data_ingestion.download_files()
        data_ingestion.extract_zip_file()
        
        
if __name__=='__main__':
    try:
        logger.info(f"--------------------------------------------------------stage {STAGE_NAME} started")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"-----------------------------------------------------------{STAGE_NAME} COMPLETED")
    except Exception as e:
        logger.exception (e)
        raise            
            