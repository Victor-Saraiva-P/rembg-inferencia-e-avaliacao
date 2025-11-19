# Repository Guidelines

## Objetivo do projeto

Este repositório visa avaliar modelos de remoção de fundo em imagens utilizando a biblioteca `rembg` e armazenar os
resultados em um banco de dados SQLite para análise comparativa. O foco está na organização do código, boas práticas de
desenvolvimento e facilidade de uso.
Dentro da pasta `dados/fotos originais`, você encontrará imagens de exemplo para teste e em `dados/fotos segmentadas`,
as imagens previamente segmentadas para referência. As imagens geradas pelo processo de remoção de fundo serão salvas em
`dados/fotos geradas/<modelo>/`, onde `<modelo>` corresponde ao nome do modelo utilizado (ex.: `u2net`, `u2netp`, etc.).

## Docs

> A pasta `docs/` contém arquivos .md para detalhar aspectos específicos do projeto. Consulte:

- `estrutura-projeto.md`: visão dos módulos, responsabilidades e onde vivem principais arquivos.
- `configuracao-ambiente.md`: passos para preparar o ambiente e comandos centrais de execução.
- `estilo-codigo.md`: convenções de nomenclatura, tipagem e organização do código.
- `testes-validacao.md`: checklist de verificação manual antes de abrir PR.
- `diretrizes-commit-pr.md`: padrões para mensagens de commit e descrição de PR.
- `eval-types.md`: critérios de avaliação dos modelos.
- `PLAN-template.md`: modelo obrigatório para escrever planos em `PLAN.md`.
- `docs/rembg/rembg-readme.md`: referência original do rembg cobrindo requisitos, instalação, subcomandos CLI, uso via docker e catálogo de modelos.
- `docs/rembg/rembg-usage.md`: exemplos práticos de uso da função `remove` (sessões, alpha matting, somente máscara, bg customizado) para scripts Python.

## Fluxo de trabalho

1. Receber a solicitação
    - Pode ser: novo recurso, bug, refatoração, ajuste de config, etc.
    - Nunca altere arquivos sem antes escrever um plano em `PLAN.md` e eu aprovar.

2. Escrever um plano **detalhado** em `PLAN.md`.

    - Sempre use **`docs/PLAN-template.md`** como base:
      - Copie o conteúdo de `docs/PLAN-template.md` para `PLAN.md`.
      - Preencha todas as seções do template.
      - O plano DEVE conter:
        - Lista de arquivos afetados.
        - Mudanças detalhadas por arquivo.
        - Trechos de código aproximados em blocos de código Markdown.
        - Descrição do fluxo de dados.
        - Estratégia de testes.

    - Não altere o arquivo `docs/PLAN-template.md`.  
      Ele é apenas o modelo; o plano concreto é sempre `PLAN.md`.

3. Enviar o conteúdo de `PLAN.md` para eu revisar e aprovar **antes** de qualquer alteração nos arquivos.

4. Cenários após revisão
    - Se o plano for aprovado: pode seguir para a implementação exatamente como descrito.
    - Se precisar de ajustes: vamos iterar no `PLAN.md` até ficar claro.

5. Implementação
    - Só então você edita os arquivos conforme o plano aprovado.
    - Se precisar mudar o escopo durante a implementação, atualize `PLAN.md` primeiro e me peça aprovação novamente.

6. Revisão e testes
    - Revisar o que foi feito e rodar os testes listados no plano.

7. Commits
    - Preparar commits baseado em `diretrizes-commit-pr.md` e entregar.
