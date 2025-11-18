# Estilo de Código e Convenções de Nomenclatura

- Python 3; siga PEP 8 (4 espaços, `snake_case` para funções/variáveis, classes em `CamelCase`). Mantenha docstrings curtas em PT-BR quando o contexto exigir.
- Tipagem estática já é usada em classes ORM (`Mapped[...]`, dataclasses); preserve e expanda anotações.
- Prefira funções puras em `script/classes/*` e isole efeitos colaterais em camadas de orquestração (ex.: `main.py`).
