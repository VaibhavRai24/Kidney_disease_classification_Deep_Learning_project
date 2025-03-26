# Kidney-Disease-Classification-MLflow-DVC

## Workflows

1. Update `config.yaml`
2. Update `secrets.yaml` [Optional]
3. Update `params.yaml`
4. Update the entity
5. Update the configuration manager in `src/config`
6. Update the components
7. Update the pipeline 
8. Update `main.py`
9. Update `dvc.yaml`
10. Train and evaluate the model

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/your-repo/Kidney-Disease-Classification
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n kidney_cls python=3.8 -y
```

```bash
conda activate kidney_cls
```

### STEP 02- Install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03- Train the model
```bash
python src/train.py
```

### STEP 04- Evaluate the model
```bash
python src/evaluate.py
```

## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)
- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### Command to start MLflow UI
```bash
mlflow ui
```

### dagshub
[dagshub](https://dagshub.com/)

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/your-user/Kidney-Disease-Classification-MLflow-DVC.mlflow
export MLFLOW_TRACKING_USERNAME=your-username
export MLFLOW_TRACKING_PASSWORD=your-password
```

Run the script:
```bash
python script.py
```

### DVC Commands

1. `dvc init`
2. `dvc repro`
3. `dvc dag`

## Model Building with Deep Learning

- Preprocess data using `src/preprocessing.py`
- Define deep learning architecture in `src/model.py`
- Train the model with `src/train.py`
- Evaluate model performance with `src/evaluate.py`
- Log experiments using MLflow
- Tune hyperparameters with `src/hyperparameter_tuning.py`

### Deep Learning Architecture:
- Convolutional Neural Networks (CNN) for feature extraction
- Fully Connected Layers for classification
- Dropout and Batch Normalization for regularization
- Optimizer: Adam
- Loss Function: Cross-Entropy
- Metrics: Accuracy, Precision, Recall

## Tracking Experiments with MLflow
- Track loss and accuracy
- Log model artifacts
- Compare different architectures and hyperparameters

## Versioning with DVC
- Track dataset changes
- Maintain model version history
- Reproduce experiments efficiently

