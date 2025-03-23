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
    params_leanring_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int