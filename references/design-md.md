# Sistema visual para agentes de IA (DESIGN.md)

Leia este arquivo somente quando a marca for usada por ferramentas de IA, ou por desenvolvedores e agências que geram interfaces.

O DESIGN.md é um formato aberto do Google Labs, lançado em abril de 2026 e ainda em alpha. Avise o cliente que ele pode mudar.

1. **Front matter em YAML** com tokens normativos: cores, tipografia, espaçamento e componentes. O arquivo deve começar com `---` na primeira linha. Qualquer texto antes disso faz o CLI ignorar os tokens.
2. **Corpo em markdown** com a justificativa de cada decisão e como aplicar os tokens.
3. **Validação**: `npx @google/design.md lint DESIGN.md` verifica estrutura, referências quebradas e contraste WCAG. Registre a versão do CLI usada (`npx @google/design.md --help` mostra a versão).
4. **Exportação**: escolha o formato conforme o projeto.
   - `--format css-tailwind` para Tailwind v4 (bloco `@theme` em CSS).
   - `--format json-tailwind` para Tailwind v3 (objeto `theme.extend` em JSON).
   - `--format dtcg` para o formato W3C de tokens.
   - `--format css-vars` para variáveis CSS puras, sem Tailwind.
   - Use sempre o nome explícito. `--format tailwind` é alias fixo de `json-tailwind`, ou seja, gera Tailwind v3. Quem quer v4 precisa de `css-tailwind`.
5. **Controle de versão**: `npx @google/design.md diff` detecta regressões entre versões.

Exemplo validado: `examples/DESIGN-exemplo.md` (marca fictícia). Passa no lint sem erros nem avisos na versão 0.4.0 do CLI.
