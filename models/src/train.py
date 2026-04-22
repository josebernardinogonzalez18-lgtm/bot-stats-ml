import pandas as pd
import yaml
import joblib
import logging
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

logging.basicConfig(level=logging.INFO)

def train_model(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    logging.info('Cargando dataset procesado...')
    df = pd.read_csv(config['data']['processed_path'])
    
    X = df[['goal_diff']] # Variables independientes
    y = df['target_home_win'] # Variable dependiente
    
    logging.info('Entrenando algoritmo XGBoost...')
    model = XGBClassifier(**config['model']['params'])
    model.fit(X, y)
    
    predictions = model.predict(X)
    acc = accuracy_score(y, predictions)
    logging.info(f'Precisión en entrenamiento: {acc:.4f}')
    
    save_path = config['data']['model_save_path']
    joblib.dump(model, save_path)
    logging.info(f'Modelo serializado correctamente en {save_path}')

if __name__ == '__main__':
    train_model('configs/model_config.yaml')