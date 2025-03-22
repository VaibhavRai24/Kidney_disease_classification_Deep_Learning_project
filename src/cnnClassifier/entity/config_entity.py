from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen= True)
class DataIngestionConfigEntity:
    root_dir: Path
    source_URL: str
    local_data_file_path: Path
    unzip_dir: Path
    