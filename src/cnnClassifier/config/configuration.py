from cnnClassifier.constants import *
import os
from cnnClassifier.utils.common import read_yaml, create_directories, save_bin, save_json
from cnnClassifier.entity.config_entity import (DataIngestionConfigEntity)

class ConfigurationManager:
    def __init__(self, config_file_path= CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])
        
    
    def get_data_ingestion_config(self) ->DataIngestionConfigEntity:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfigEntity(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file_path= config.local_data_file_path,
            unzip_dir= config.unzip_dir
        )
        
        return data_ingestion_config
    
    
    