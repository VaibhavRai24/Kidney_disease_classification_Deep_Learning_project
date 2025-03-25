from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_training import Training
from cnnClassifier import logger

STAGE_NAME = 'Training of the model'

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config= training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
        
        
        
if __name__ == "__main__":
    try:
        logger.info(f" Training pipeline started { STAGE_NAME}")
        run = ModelTrainingPipeline()
        run.main()
        logger.info(f" Training pipeline completed { STAGE_NAME}")
        
    except Exception as e: 
        logger.error(f" Training pipeline failed { STAGE_NAME} {e}")
        raise e
        