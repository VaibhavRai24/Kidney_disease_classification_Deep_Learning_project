from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_eval_mlflow import ModelEvaluation
from cnnClassifier import logger

STAGE_NAME = "Evaluation_stage"


class EvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = ModelEvaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_mlflow()
        
        
        
if __name__ == "__main__":
    try:
        logger.info("Evaluation stage has started")
        pipeline = EvaluationPipeline()
        pipeline.main()
        logger.info("Evaluation stage has completed")
    except Exception as e:
        logger.error(f"Error in Evaluation stage: {str(e)}")
        raise e