# ML-TRAINING-BOT

Sistema de Machine Learning basado en análisis cuantitativo de datos deportivos.

## Estructura
Pipeline automatizado desde la ingesta de datos en crudo, creación de variables dependientes e independientes (Data Preprocessing), hasta el modelado con algoritmos tipo ensamble (XGBoost).

## Setup
1. Crear un entorno virtual e instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecutar el pipeline completo:
```bash
python main.py --step all
```

Para ejecutar pasos individuales, usar `--step ingest`, `--step preprocess` o `--step train`.