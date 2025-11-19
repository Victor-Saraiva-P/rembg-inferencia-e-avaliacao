# Caminho relativo ao arquivo 'run.db'
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, 'run.db')
ORIGINAL_PHOTOS_DIR = os.path.join(BASE_DIR, 'dados', 'fotos originais')
SEGMENTED_PHOTOS_DIR = os.path.join(BASE_DIR, 'dados', 'fotos segmentadas')
OUTPUT_MODEL_DIR = os.path.join(BASE_DIR, 'dados', 'fotos geradas')
MASKS_SUBDIR_PATH = os.path.join(OUTPUT_MODEL_DIR, '{model_name}', 'masks')
MODELS_DIR = os.path.join(BASE_DIR, 'modelos')

MODELOS_PARA_AVALIACAO = [
    'u2net',
    'u2netp',
    'u2net_human_seg',
    # 'u2net_cloth_seg', este não vai entrar porque é específico para roupas e altera a resolução da imagem
    'silueta',
    'isnet-general-use',
    'isnet-anime',
    'sam',
    'birefnet-general',
    'birefnet-general-lite',
    'birefnet-portrait',
    'birefnet-dis',
    'birefnet-hrsod',
    'birefnet-cod',
    'birefnet-massive'
]
