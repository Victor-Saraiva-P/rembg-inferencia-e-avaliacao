# Plano para: Atualizar AGENTS com links para docs do rembg

## 1. Resumo da tarefa

- Expandir a seção "Docs" de `AGENTS.md` inserindo referências diretas aos arquivos novos `docs/rembg/rembg-readme.md` e `docs/rembg/rembg-usage.md`.
- Garantir que o documento principal oriente outras pessoas a encontrarem rapidamente essas fontes detalhadas.

## 2. Arquivos afetados

- `AGENTS.md` — adicionar duas entradas na lista "Docs" apontando para `docs/rembg/rembg-readme.md` e `docs/rembg/rembg-usage.md` com breves descrições do conteúdo.

## 3. Mudanças detalhadas por arquivo

### 3.1 `AGENTS.md`

- [ ] Manter o texto existente e acrescentar duas linhas na lista de docs indicando:
  - `docs/rembg/rembg-readme.md`: resumo da documentação original do rembg (instalação, requisitos, CLI, docker, modelos).
  - `docs/rembg/rembg-usage.md`: exemplos rápidos de uso da função `remove` (código Python, sessões, alpha matting etc.).

Trecho(s) de código aproximado(s):

```markdown
- `docs/rembg/rembg-readme.md`: referência completa do rembg (requisitos, instalação, CLI/serviços, modelos e docker).
- `docs/rembg/rembg-usage.md`: snippets de uso da função `remove`, criação de sessões e parâmetros úteis.
```

## 4. Fluxo de dados

- Um novo colaborador abre `AGENTS.md` → encontra a lista "Docs" → identifica rapidamente os arquivos `docs/rembg/...` → consulta os detalhes no repositório original conforme necessário.

## 5. Estratégia de testes

- Apenas revisão visual: `cat AGENTS.md` para conferir se as novas linhas da lista aparecem formatadas corretamente e com descrições claras.
