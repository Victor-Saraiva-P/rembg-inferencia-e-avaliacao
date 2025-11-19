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
- `docs/rembg/rembg-readme.md`: referência original do rembg cobrindo requisitos, instalação, subcomandos CLI, uso via docker e catálogo de modelos.
- `docs/rembg/rembg-usage.md`: exemplos práticos de uso da função `remove` (sessões, alpha matting, somente máscara, bg customizado) para scripts Python.

## Fluxo de trabalho

- Receber a solicitação (prompt/problema).
- Planejar em `PLAN.md` (raiz), registrar passos propostos e alinhar ajustes na conversa.
- Implementar conforme plano aprovado.
- Revisar o que foi feito e rodar testes relevantes.
- Preparar commits baseado em `diretrizes-commit-pr.md` e entregar.
