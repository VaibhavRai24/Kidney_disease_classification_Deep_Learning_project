from cnnClassifier.constants import *
import os
from cnnClassifier.utils.common import read_yaml, create_directories, save_bin, save_json
from cnnClassifier.entity.config_entity import (DataIngestionConfigEntity,
                                                PrepareBaseModelConfigEntity,
                                                TrainingConfigEntity,
                                                EvaluationConfigEntity)

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
    
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfigEntity:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])
        prepare_base_model_config = PrepareBaseModelConfigEntity(
            root_dir= Path(config.root_dir),
            base_model_path= Path(config.base_model_path),
            updated_base_model_path= Path(config.updated_base_model_path),
            params_image_size = self.params.IMAGE_SIZE,
            params_learning_rate= self.params.LEARNING_RATE,
            params_include_top= self.params.INCLUDE_TOP,
            params_weights= self.params.WEIGTHS,
            params_classes= self.params.CLASSES
        )

        return prepare_base_model_config
    
    
    
    def get_training_config(self) -> TrainingConfigEntity:
        training = self.config.training
        prepare_base_model_config = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "kidney-ct-scan-image")
        create_directories([Path(training.root_dir)])
        
        
        training_config = TrainingConfigEntity(
            root_dir= Path(training.root_dir),
            trained_model_path = Path(training.trained_model_path),
            updated_base_model_path= Path(prepare_base_model_config.updated_base_model_path),
            training_data= Path(training_data),
            params_epochs= params.EPOCHS,
            params_batch_size= params.BATCH_SIZE,
            params_image_size= params.IMAGE_SIZE,
            params_is_augmentation= params.AUGMENTATION
        )
        
        return training_config
    
    
    def get_evaluation_config(self) -> EvaluationConfigEntity:
        eval_config = EvaluationConfigEntity(
            path_of_the_model=(r"C:\Users\VAIBHAVRAI\OneDrive\Desktop\kidney_project\kd_pr\artifacts\training\model.h5"),
            training_data=(r"C:\Users\VAIBHAVRAI\OneDrive\Desktop\kidney_project\kd_pr\artifacts\data_ingestion\kidney-ct-scan-image"),
            mlflow_tracking_uri= "https://dagshub.com/VaibhavRai24/Kidney_disease_classification_Deep_Learning_project.mlflow",
            params = self.params,
            params_image_size= self.params.IMAGE_SIZE,
            params_batch_size= self.params.BATCH_SIZE
        )
        
        return eval_config