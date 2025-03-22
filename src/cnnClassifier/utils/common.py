import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import joblib
import json
import base64
from typing import Any
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations

@ensure_annotations
def read_yaml(file_path:str)->ConfigBox:
    """
    Read yaml file and return as dictionary
    """
    try:
        with open(file_path, 'r') as stream:
            return ConfigBox(yaml.safe_load(stream))
        logger.info(f"Yaml file read successfully: {file_path}")
    except BoxValueError:
        logger.error(f"Might possible yaml file is empty: {file_path}")
        raise 
    

@ensure_annotations
def create_directories(path:list, verbose=True):
    """
    Basically ye directores create krega diye hue path pe
    
    """
    for paths in path:
        os.makedirs(paths, exist_ok= True)
        if verbose:
            logger.info(f"Directory is created successfully at the :{path}")
            
@ensure_annotations
def save_json(path:Path, data:dict):
    """
    Saves the json data on the specified path
    
    """
    try:
        with open(path, 'w') as file_to_save:
            json.dump(data, file_to_save, indent=4)
        logger.info(f"Json has been saved at {path}")
        
    except Exception as e:
        raise 
    
@ensure_annotations
def load_json(file_path:Path) -> ConfigBox:
    """
    Loads the specifed json path
    
    """
    try:
        with open(file_path) as file:
            content = json.load(file)
        logger.info(f"json file has been loaded successfully")
        return ConfigBox(content)
    except Exception as e:
        raise 
    
@ensure_annotations
def save_bin(data:Any, path:Path) :
    """
    Saves out the binary file 
    
    """
    joblib.dump(value=data, filename= path)
    logger.info(f"Binary format file has been saved into the {path}")
    

@ensure_annotations
def load_bin(file_path:Path) -> Any:
    """
    Basically it loads out the bin format file
    
    """
    data = joblib.load(file_path)
    logger.info(f"Binary file format has been loaded out ")
    return data


@ensure_annotations
def get_size(path:Path) ->str:
    """
    Basically it gets the size in the kb
    
    """
    size_of_file_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_of_file_in_kb} KB"



def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())