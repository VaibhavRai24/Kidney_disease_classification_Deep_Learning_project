from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger


STAGE_NAME = 'PrepareBaseModel'

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(prepare_base_model_config)
        prepare_base_model.downlaod_base_model()
        prepare_base_model.update_base_model()
        
        
if __name__ == '__main__':
    try:
        logger.info(f"Stage: {STAGE_NAME} started")
        pipeline = PrepareBaseModelTrainingPipeline()
        pipeline.main()
        logger.info(f"Stage: {STAGE_NAME} completed")
    except Exception as e:
        logger.error(f"Stage: {STAGE_NAME} failed")
        logger.error(str(e))