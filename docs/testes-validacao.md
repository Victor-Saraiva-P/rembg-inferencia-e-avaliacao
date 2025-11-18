# Testes e Validação

- Não há e nem haverá suíte automática. Foque em:
    - Verificar que `script.main` gera arquivos na pasta correta para um subconjunto de imagens exemplo.
    - Validar mapeamento ORM de `Avaliacao` com SQLite in-memory.
    - Garantir que funções de métrica retornem valores numéricos e lidam com entradas inválidas.
- Antes de abrir PR, rode o fluxo principal com 1–2 imagens e confirme tamanhos/formatos esperados.
