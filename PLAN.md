# Plano para: Implementar calcular_roi_association com máscaras do rembg

## 1. Resumo da tarefa

- Implementar o cálculo real da métrica de associação à ROI utilizando as máscaras segmentadas de referência (GT) e as máscaras produzidas por cada modelo via `rembg` usando `only_mask=True`.
- Ajustar o fluxo para que o nome do modelo seja propagado até o cálculo da métrica, permitindo abrir o arquivo correto dentro de `dados/fotos geradas/<modelo>/masks/`.
- Adaptar `main.py` para salvar também a máscara do modelo, sem alterar a lógica atual de salvar a imagem recortada.

## 2. Arquivos afetados

- `script/main.py` — usar `remove(..., only_mask=True)` para gerar e salvar a máscara da predição em `dados/fotos geradas/<modelo>/masks/<image_name>`.
- `script/classes/metrica.py` — adicionar utilitário para carregar máscara binária, implementar `calcular_roi_association` com Dice/IoU usando as máscaras GT e predita, e atualizar `metrificar` para receber `model_name`.
- `script/classes/avaliacao.py` — propagar `model_name` ao chamar `metrificar`.

## 3. Mudanças detalhadas por arquivo

### 3.1 `script/main.py`

- [ ] Importar `io` (se necessário) e utilizar `remove(foto_original, session=session, only_mask=True)` para obter a máscara binária da predição.
- [ ] Salvar a máscara retornada pelo `rembg` em `dados/fotos geradas/<modelo>/<NOME_SUBDIR_MASCARAS>/<image_name>`, onde `<NOME_SUBDIR_MASCARAS>` vem de uma constante definida em `config.py` (ex.: `MASKS_SUBDIR_PATH = os.path.join(OUTPUT_MODEL_DIR, '{model_name}', 'masks')`), mantendo o salvamento atual da imagem recortada em `dados/fotos geradas/<modelo>/<image_name>`.
- [ ] Garantir que o diretório `dados/fotos geradas/<modelo>/<NOME_SUBDIR_MASCARAS>/` seja criado com `os.makedirs(..., exist_ok=True)`.

Trecho(s) de código aproximado(s):

```python
mask_dir = MASKS_SUBDIR_PATH.format(model_name=modelo)
mask_output_path = os.path.join(mask_dir, foto)
os.makedirs(os.path.dirname(mask_output_path), exist_ok=True)

with open(input_path, "rb") as arquivo_entrada:
    foto_original = arquivo_entrada.read()

    foto_sem_fundo = remove(foto_original, session=session)
    with open(output_path, "wb") as arquivo_saida:
        arquivo_saida.write(foto_sem_fundo)

    mask_bytes = remove(foto_original, session=session, only_mask=True)
    with open(mask_output_path, "wb") as arquivo_mask:
        arquivo_mask.write(mask_bytes)
```

### 3.2 `script/classes/metrica.py`

- [ ] Importar `os`, `numpy` e os caminhos relevantes de `config` (`SEGMENTED_PHOTOS_DIR`, `MASKS_SUBDIR_PATH`).
- [ ] Utilizar helper `carregar_mascara_binaria` (definido em um módulo de utilitários de imagem separado) para carregar as máscaras GT e predita.
- [ ] Atualizar `calcular_roi_association` para aceitar `image_name` e `model_name`, abrir as duas máscaras (GT e previsão) de:
  - GT: `os.path.join(SEGMENTED_PHOTOS_DIR, image_name)`
  - predição: `os.path.join(MASKS_SUBDIR_PATH.format(model_name=model_name), image_name)`
  calcular Dice Coefficient e IoU, combiná-los (usar Dice como métrica principal e IoU apenas para desempate) e retornar o valor (fallback para 0 quando não houver interseção relevante). Tratar o divisor do Dice para não dividir por zero.
- [ ] Atualizar `metrificar` para receber `model_name` e repassar ao `calcular_roi_association`; demais métricas permanecem placeholders.

Trecho(s) de código aproximado(s):

```python
from config import SEGMENTED_PHOTOS_DIR, MASKS_SUBDIR_PATH
import numpy as np
from script.utils.imagem import carregar_mascara_binaria


def calcular_roi_association(image_name: str, model_name: str) -> float:
    gt_path = os.path.join(SEGMENTED_PHOTOS_DIR, image_name)
    mask_dir = MASKS_SUBDIR_PATH.format(model_name=model_name)
    pred_path = os.path.join(mask_dir, image_name)
    gt_mask = carregar_mascara_binaria(gt_path)
    pred_mask = carregar_mascara_binaria(pred_path)
    inter = np.logical_and(gt_mask, pred_mask).sum()
    dice = (2 * inter) / (gt_mask.sum() + pred_mask.sum()) if (gt_mask.sum() + pred_mask.sum()) else 0.0
    iou = inter / np.logical_or(gt_mask, pred_mask).sum() if np.logical_or(gt_mask, pred_mask).sum() else 0.0
    return round((dice * 0.85) + (iou * 0.15), 4)
```

### 3.3 `script/classes/avaliacao.py`

- [ ] Alterar a chamada para `metrificar` em `__init__` para enviar `model_name` (e ajustar assinatura importada caso necessário).
- [ ] Garantir que nada mais depende da assinatura antiga.

### 3.4 `script/utils/carregador_mascara.py`

- [ ] Criar módulo de utilitários de imagem `script/utils/carregador_mascara.py`.
- [ ] Implementar função `carregar_mascara_binaria(path: str) -> np.ndarray` que:
  - Abre a imagem com `PIL.Image.open`.
  - Converte para escala de cinza (`"L"`).
  - Converte para `numpy.ndarray` e aplica limiar binário (`pixel > 0`) retornando um array booleano.
- [ ] Pensar esse módulo como ponto único para futuras operações genéricas com máscaras/imagens (ex.: normalização, pós-processamento, etc.), evitando poluir `metrica.py` com detalhes de IO.

Trecho(s) de código aproximado(s):

```python
from PIL import Image
import numpy as np


def carregar_mascara_binaria(path: str) -> np.ndarray:
    with Image.open(path) as img:
        mascara = img.convert("L")
        return np.array(mascara) > 0
```

### 3.5 `config.py`

- [ ] Adicionar constante para o nome do subdiretório onde as máscaras serão salvas, por exemplo:

```python
MASKS_SUBDIR_PATH = os.path.join(OUTPUT_MODEL_DIR, "{model_name}", "masks")
```

## 4. Fluxo de dados

1. `script/main.py` executa `remove`, grava o PNG/mascara estimada em `dados/fotos geradas/<modelo>/<imagem>` e instancia `Avaliacao` com `image_name` e `model_name`.
2. `script/main.py` também chama `remove(..., only_mask=True)` e grava a máscara do modelo em `MASKS_SUBDIR_PATH.format(model_name=<modelo>)/<imagem>`.
3. `Avaliacao.__init__` cria a resolução e chama `metrificar(image_name, model_name)`.
4. `metrificar` usa `carregar_mascara_binaria` para obter a ROI manual (`SEGMENTED_PHOTOS_DIR/<imagem>`) e a previsão do modelo (`MASKS_SUBDIR_PATH.format(model_name=<modelo>)/<imagem>`).
4. `calcular_roi_association` calcula Dice e IoU entre as máscaras, retorna um escalar normalizado (0–1) representando a associação à ROI, que é persistido no banco.

## 5. Estratégia de testes

- Criar uma previsão fake copiando `dados/fotos segmentadas/exemplo01.jpg` para `dados/fotos geradas/modelo_dummy/masks/exemplo01.jpg` (simula um caso perfeito) e executar `python3 - <<'PY'` chamando `calcular_roi_association('exemplo01.jpg', 'modelo_dummy')`; o retorno deve ser 1.0.
- Remover o diretório temporário `dados/fotos geradas/modelo_dummy` após o teste para não deixar lixo no repositório.
