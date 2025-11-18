# Estrutura do Projeto e Organização de Módulos

- O core da configuração do projeto vive em `config.py`, definindo caminhos para origem (`dados/fotos originais`), saídas (`dados/fotos geradas`), segmentadas e banco SQLite (`run.db`).
- Processamento do código está em `script/`: `main.py` executa a inferência em lote com `rembg`, `classes/` contém modelos ORM (SQLAlchemy) e estruturas de métrica/resolução, `lista_arquivos.py` lista insumos.
- Modelos ONNX são baixados automaticamente pelo `rembg` para `~/.u2net` (ou `modelos/` se você ajustar o `MODELS_DIR`). Evite versionar artefatos grandes; `.gitignore` já cobre caches/venvs.
