import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def preprocess_data(input_path, output_path):
    logging.info('Cargando datos crudos...')
    df = pd.read_csv(input_path)
    
    logging.info('Aplicando feature engineering...')
    # Calculando diferencia de goles (feature básica de ejemplo)
    df['goal_diff'] = df['goals_home'] - df['goals_away']
    # Target: 1 si gana local, 0 empate/visitante
    df['target_home_win'] = (df['goal_diff'] > 0).astype(int)
    
    df.to_csv(output_path, index=False)
    logging.info(f'Datos procesados guardados en {output_path}')

if __name__ == '__main__':
    preprocess_data('data/raw/sports_data.csv', 'data/processed/sports_data_clean.csv')