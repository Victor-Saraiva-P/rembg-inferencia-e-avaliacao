from __future__ import annotations

from typing import Final

import numpy as np
from PIL import Image

# Limite mínimo para considerar um pixel como pertencente à máscara.
_PIXEL_THRESHOLD: Final[int] = 0


def carregar_mascara_binaria(path: str) -> np.ndarray:
    """
    Lê uma imagem do disco e devolve uma matriz booleana onde pixels > limiar são verdadeiros.

    A função abstrai detalhes de IO das métricas, garantindo que toda máscara seja convertida
    para escala de cinza antes do limiar.
    """
    with Image.open(path) as imagem:
        escala_cinza = imagem.convert("L")
        return np.array(escala_cinza) > _PIXEL_THRESHOLD
