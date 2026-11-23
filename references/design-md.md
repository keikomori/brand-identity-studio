# Sistema visual para agentes de IA (DESIGN.md)

Leia este arquivo somente quando a marca for usada por ferramentas de IA, ou por desenvolvedores e agências que geram interfaces.

O DESIGN.md é um formato aberto do Google Labs, lançado em abril de 2026 e ainda em alpha. Avise o cliente que ele pode mudar.

1. **Front matter em YAML** com tokens normativos: cores, tipografia, espaçamento e componentes.
2. **Corpo em markdown** com a justificativa de cada decisão e como aplicar os tokens.
3. **Validação**: `npx @google/design.md lint DESIGN.md` verifica estrutura, referências quebradas e contraste WCAG. Registre a versão do CLI usada.
4. **Exportação**: escolha o formato conforme o projeto.
   - `--format css-tailwind` para Tailwind v4 (bloco `@theme` em CSS).
   - `--format json-tailwind` para Tailwind v3 (objeto de configuração).
   - `--format dtcg` para o formato W3C de tokens.
   - Não use `--format tailwind` sem especificar a versão. Ele é um alias, e a saída depende da versão.
5. **Controle de versão**: `npx @google/design.md diff` detecta regressões entre versões.
