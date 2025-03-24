import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import PrepareBaseModelConfigEntity


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfigEntity):
        self.config = config
        
    def downlaod_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape= self.config.params_image_size,
            weights= self.config.params_weights,
            include_top= self.config.params_include_top
        )
        
        self.save_model(path = self.config.base_model_path, model = self.model)
        
        
    @staticmethod
    def prepare_full_model(model, classes, frezze_all, freeze_till, learning_rate):
        if frezze_all:
            for layer in model.layers:
                layer.trainable = False
        
        elif (freeze_till is not None) and (freeze_till < len(model.layers)):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False 
                
                
        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(units =classes, activation= 'softmax')(flatten_in)
        
        full_model = tf.keras.models.Model(
            inputs = model.input,
            outputs = prediction
        )
        
        
        full_model.compile(
            loss = tf.keras.losses.CategoricalCrossentropy(),
            optimizer = tf.keras.optimizers.SGD(learning_rate = learning_rate),
            metrics = ['accuracy']
        )
        
        
        full_model.summary()
        return full_model
    
    def update_base_model(self):
        self.full_model = self.prepare_full_model(
            model = self.model,
            classes = self.config.params_classes,
            frezze_all = True,
            freeze_till = None,
            learning_rate = self.config.params_learning_rate
        )
        
        self.save_model(path = self.config.updated_base_model_path, model = self.full_model)
        
    @staticmethod
    def save_model(path: Path, model):
        model.save(path)