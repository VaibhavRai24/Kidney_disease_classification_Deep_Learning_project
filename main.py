from cnnClassifier import logger
# from cnnClassifier.pipeline.stage1 import DataIngestionTrainingPipeline
# from cnnClassifier.pipeline.stage2 import PrepareBaseModelTrainingPipeline
# from cnnClassifier.pipeline.stage03 import ModelTrainingPipeline
from cnnClassifier.pipeline.stage04 import EvaluationPipeline
# STAGE_NAME = "DataIngestionStage"
# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
#     data_ingestion = DataIngestionTrainingPipeline()
#     data_ingestion.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(e)
#     raise e



# STAGE_NAME = "PrepareBaseModel"
# try:
#     logger.info(f"Stage: {STAGE_NAME} started")
#     pipeline = PrepareBaseModelTrainingPipeline()
#     pipeline.main()
#     logger.info(f"Stage: {STAGE_NAME} completed")
# except Exception as e:
#     logger.error(f"Stage: {STAGE_NAME} failed")
#     logger.error(str(e))
        
        
# STAGE_NAME = "ModelTraining"
# try:
#     logger.info(f"Stage: {STAGE_NAME} started")
#     model_trainer = ModelTrainingPipeline()
#     model_trainer.main()
#     logger.info(f"Stage: {STAGE_NAME} completed")
# except Exception as e:
#     logger.error(f"Stage: {STAGE_NAME} failed")
#     logger.error(str(e))
    
    
    
STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e