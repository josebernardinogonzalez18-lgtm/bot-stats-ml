import argparse
import logging
from src.data_ingestion import fetch_sports_data
from src.preprocessing import preprocess_data
from src.train import train_model

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description='ML-TRAINING-BOT: Quantitative Sports Pipeline')
    parser.add_argument('--step', choices=['ingest', 'preprocess', 'train', 'all'], default='all', help='Paso del pipeline a ejecutar')
    args = parser.parse_args()

    if args.step in ['ingest', 'all']:
        logging.info('--- INICIANDO INGESTA ---')
        fetch_sports_data('api_endpoint_dummy', 'data/raw/sports_data.csv')
    if args.step in ['preprocess', 'all']:
        logging.info('--- INICIANDO PREPROCESAMIENTO ---')
        preprocess_data('data/raw/sports_data.csv', 'data/processed/sports_data_clean.csv')
    if args.step in ['train', 'all']:
        logging.info('--- INICIANDO ENTRENAMIENTO ---')
        train_model('configs/model_config.yaml')
        
    logging.info('Pipeline ejecutado con éxito.')

if __name__ == '__main__':
    main()