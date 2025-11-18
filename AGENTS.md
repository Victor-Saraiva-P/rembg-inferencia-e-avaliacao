# Repository Guidelines

## Objetivo do projeto

Este repositório visa avaliar modelos de remoção de fundo em imagens utilizando a biblioteca `rembg` e armazenar os
resultados em um banco de dados SQLite para análise comparativa. O foco está na organização do código, boas práticas de
desenvolvimento e facilidade de uso.
Dentro da pasta `dados/fotos originais`, você encontrará imagens de exemplo para teste e em `dados/fotos segmentadas`,
as imagens previamente segmentadas para referência. As imagens geradas pelo processo de remoção de fundo serão salvas em
`dados/fotos geradas/<modelo>/`, onde `<modelo>` corresponde ao nome do modelo utilizado (ex.: `u2net`, `u2netp`, etc.).

## Estrutura do Projeto e Organização de Módulos

- O core da configuração do projeto vive em `config.py`, definindo caminhos para origem (`dados/fotos originais`),
  saídas (`dados/fotos geradas`), segmentadas e banco SQLite (`run.db`).
- Processamento do código está em `script/`: `main.py` executa a inferência em lote com `rembg`, `classes/` contém
  modelos ORM (SQLAlchemy) e estruturas de métrica/resolução, `lista_arquivos.py` lista insumos.
- Modelos ONNX são baixados automaticamente pelo `rembg` para `~/.u2net` (ou `modelos/` se você ajustar o `MODELS_DIR`).
  Evite versionar artefatos grandes; `.gitignore` já cobre caches/venvs.

## Configuração do Ambiente e Comandos Principais

- `python -m venv .venv && source .venv/bin/activate` — cria/ativa o ambiente virtual.
- `pip install -r requirements.txt` — instala dependências (rembg, onnxruntime, SQLAlchemy).
- `python -m script.main` — processa todas as imagens em `dados/fotos originais` para cada modelo em
  `MODELOS_AVALIACAO`, salvando saídas em `dados/fotos geradas/<modelo>/`.

## Estilo de Código e Convenções de Nomenclatura

- Python 3; siga PEP 8 (4 espaços, `snake_case` para funções/variáveis, classes em `CamelCase`). Mantenha docstrings
  curtas em PT-BR quando o contexto exigir.
- Tipagem estática já é usada em classes ORM (`Mapped[...]`, dataclasses); preserve e expanda anotações.
- Prefira funções puras em `script/classes/*` e isole efeitos colaterais em camadas de orquestração (ex.: `main.py`).

## Testes e Validação

- Não há e nem haverá suíte automática. Foque em:
    - Verificar que `script.main` gera arquivos na pasta correta para um subconjunto de imagens exemplo.
    - Validar mapeamento ORM de `Avaliacao` com SQLite in-memory.
    - Garantir que funções de métrica retornem valores numéricos e lidam com entradas inválidas.
- Antes de abrir PR, rode o fluxo principal com 1–2 imagens e confirme tamanhos/formatos esperados.

## Diretrizes de Commit e Pull Request

- Siga o histórico existente: mensagens curtas em imperativo/PT-BR (`Adiciona ...`, `Implementa ...`).
- Inclua no PR: o problema ou objetivo, mudanças principais, comandos executados e exemplos de entrada/saída (paths em
  `dados/...`). Anexe tabela ou snippet com métricas se alterar cálculo/armazenamento.
- Não suba arquivos de modelo ou lotes grandes de imagens; se necessário, detalhe como obtê-los no `README.md`.
