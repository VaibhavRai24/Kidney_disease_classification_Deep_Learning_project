import tensorflow as tf
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from cnnClassifier.entity.config_entity import EvaluationConfigEntity
from cnnClassifier.utils.common import read_yaml, create_directories, save_json
import dagshub


mlflow.set_tracking_uri("https://dagshub.com/VaibhavRai/Kidney_disease_classification_Deep_Learning_project.mlflow")
dagshub.init(repo_owner='VaibhavRai', repo_name='Kidney_disease_classification_Deep_Learning_project', mlflow=True)

class ModelEvaluation:
    def __init__(self, config: EvaluationConfigEntity):
        self.config = config
        
    def _valid_generator(self):
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.20
        )
        
        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = "bilinear"
        )
        
        
        validation_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )
        
        self.valid_generator = validation_datagenerator.flow_from_directory(
            directory= self.config.training_data,
            subset= "validation",
            shuffle= False,
            **dataflow_kwargs
        )
        
        
    @staticmethod
    def load_model(path:Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    def evaluation(self):
        self.model = self.load_model(self.config.path_of_the_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()
        
        
    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path = Path("scores.json"), data = scores)
        
    
    def log_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_tracking_uri)
        tracking_uri = urlparse(mlflow.get_artifact_uri()).scheme
        with mlflow.start_run():
            mlflow.log_params(self.config.params)
            mlflow.log_metrics({"loss": self.score[0], "accuracy": self.score[1]})
            if tracking_uri != "file":
                mlflow.keras.log_model(self.model, "model", registered_model_name= " VGG16Model")
            else:
                mlflow.keras.log_model(self.model, "model")
        
        
        
        