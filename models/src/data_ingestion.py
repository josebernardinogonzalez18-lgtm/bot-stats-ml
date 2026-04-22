import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def fetch_sports_data(source_url, output_path):
    logging.info(f'Extrayendo datos de {source_url}...')
    # Dummy data - Reemplazar con lógica de API/Scraping (Ej. StatsBomb, API-Football)
    data = {'team_home': ['TeamA', 'TeamC'], 'team_away': ['TeamB', 'TeamD'], 'goals_home': [2, 1], 'goals_away': [1, 1]}
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    logging.info(f'Datos guardados en {output_path}')

if __name__ == '__main__':
    fetch_sports_data('https://api.sportsprovider.com/v1/matches', 'data/raw/sports_data.csv')