# Caminho relativo ao arquivo 'run.db'
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, 'run.db')
ORIGINAL_PHOTOS_DIR = os.path.join(BASE_DIR, 'dados', 'fotos_originais')
SEGMENTED_PHOTOS_DIR = os.path.join(BASE_DIR, 'dados', 'fotos_segmentadas')
MODELS_DIR = os.path.join(BASE_DIR, 'modelos')
