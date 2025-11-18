# Configuração do Ambiente e Comandos Principais

- `python -m venv .venv && source .venv/bin/activate` — cria/ativa o ambiente virtual.
- `pip install -r requirements.txt` — instala dependências (rembg, onnxruntime, SQLAlchemy).
- `python -m script.main` — processa todas as imagens em `dados/fotos originais` para cada modelo em `MODELOS_AVALIACAO`, salvando saídas em `dados/fotos geradas/<modelo>/`.
