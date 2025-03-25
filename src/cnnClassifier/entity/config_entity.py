from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen= True)
class DataIngestionConfigEntity:
    root_dir: Path
    source_URL: str
    local_data_file_path: Path
    unzip_dir: Path
    
    
    
@dataclass(frozen= True)
class PrepareBaseModelConfigEntity:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
    
    
@dataclass(frozen= True)
class TrainingConfigEntity:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size : int
    params_image_size : list
    params_is_augmentation : bool
    
    
@dataclass(frozen= True)
class EvaluationConfigEntity:
    path_of_the_model: Path
    training_data: Path
    params: dict
    mlflow_tracking_uri: str
    params_image_size: list
    params_batch_size: int
    