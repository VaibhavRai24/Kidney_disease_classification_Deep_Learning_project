import os
import urllib.request as request
from zipfile import ZipFile
from pathlib import Path
import tensorflow as tf
import time
from cnnClassifier.entity.config_entity import TrainingConfigEntity


class Training:
    def __init__(self, config: TrainingConfigEntity):
        self.config = config
        
        
    def get_base_model(self):
        self.model =  tf.keras.models.load_model(self.config.updated_base_model_path)
        
        
    def train_valid_generator(self):
        
        datageneator_kwargs = dict(
            rescale = 1./255,
            validation_split= 0.20
        )
        
        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = "bilinear"
        )
        
        valid_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(**datageneator_kwargs)
        
        self.valid_generator = valid_data_generator.flow_from_directory(
            directory= self.config.training_data,
            subset= "validation",
            shuffle= False,
            **dataflow_kwargs
        )
        
        
        if self.config.params_is_augmentation:
            train_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datageneator_kwargs
            )
            
        else:
            train_data_generator = valid_data_generator
            
        self.train_generator = train_data_generator.flow_from_directory(
            directory= self.config.training_data,
            subset= "training",
            shuffle= True, 
            **dataflow_kwargs
        )
        
        
    @staticmethod
    def save_model(path: Path, model: tf.keras.models.Model):
        model.save(path)
        
        
    def train(self):
        self.steps_per_epochs = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size
        
        self.model.fit(
            self.train_generator,
            epochs = self.config.params_epochs,
            steps_per_epoch = self.steps_per_epochs,
            validation_steps = self.validation_steps,
            validation_data = self.valid_generator
        )
        
        
        self.save_model(
            path = self.config.trained_model_path,
            model = self.model
        )