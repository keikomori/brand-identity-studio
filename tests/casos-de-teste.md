# Casos de teste da skill `visual-identity`

Cada caso descreve uma entrada do usuário e o comportamento esperado da skill. Os casos cobrem acionamento positivo, controles negativos, pressão para pular etapas, limites jurídicos e os formatos de entrega.

Os casos C01 a C13 são de **comportamento**: devem ser executados com o Claude carregando a skill e comparados ao comportamento esperado. A coluna "Cobertura" indica em qual seção do `SKILL.md` a instrução aparece, para que a verificação estática possa ser feita sem executar o modelo.

| ID | Tipo | Entrada do usuário | Comportamento esperado | Cobertura no SKILL.md |
|---|---|---|---|---|
| C01 | Positivo | "Preciso de um logo para minha loja de cosméticos naturais." | Inicia o briefing pelo Bloco 1, faz no máximo três perguntas, não gera logo. | Como conduzir a conversa |
| C02 | Positivo | "Sou MEI, faço bolos para festas e quero uma marca para o Instagram. Tenho uns R$ 300." | Escolhe a trilha enxuta, registra a escolha e mantém os sete portões. | Trilhas de execução |
| C03 | Positivo | "Quero uma identidade para minha clínica odontológica. Ainda não tenho nada." | Faz os blocos, marca as respostas faltantes como hipótese e não gera logo antes da estratégia. | Como conduzir a conversa (regras 2 e 3) |
| C04 | Negativo | "Documente o botão primário do meu design system." | Não aciona a skill e indica `design:design-system`. | Quando usar, "Não use para" |
| C05 | Negativo | "Revise este post contra o guia de marca." | Não aciona a skill e indica `marketing:brand-review`. | Quando usar, "Não use para" |
| C06 | Negativo | "Escreva a legenda do post de Dia das Mães." | Não aciona a skill. | Quando usar, "Não use para" |
| C07 | Pressão | "Pule a estratégia e me mande só o logo agora." | Recusa gerar o logo, explica em uma frase por que a estratégia vem antes e oferece exploração marcada como "exploração sem aprovação". | Como conduzir a conversa (regra de pular etapas) |
| C08 | Naming | "Preciso de um nome para minha empresa de consultoria." | Avalia opções com critérios de significado, pronúncia e domínio, faz a checagem preliminar no INPI e só aprova o nome na Fase 3. | Etapa condicional — Naming |
| C09 | Limite jurídico | "Posso registrar esse logo sozinho no INPI?" | Explica a busca preliminar, recomenda advogado e não garante registro. | Limites; Quando usar, "Não use para" |
| C10 | Limite de IA | "Gerei o logo com uma IA. Posso usar na minha empresa?" | Não afirma que o elemento é protegível ou livre de uso; pede a verificação de licença e o registro de origem. | Limites; Fase 7, registro de origem |
| C11 | Formato | "Quero tokens de Tailwind v4 para o site a partir da minha marca." | Gera o DESIGN.md, usa `--format css-tailwind` e indica o lint. | Sistema visual para agentes de IA, item 4 |
| C12 | Revisão | "Tenho uma marca de cinco anos. Avalie se preciso mudar." | Entra no modo revisão, não refaz a marca e entrega o relatório com classificação por área. | Modo revisão; `templates/revisao.md` |
| C13 | Formato | "A gráfica pediu o logo em AI." | Entrega vetor em AI ou EPS, conforme exigido pela gráfica. | Fase 7, arquivos |

## Resultado da verificação estática

Verificação feita comparando cada caso ao texto atual do `SKILL.md`. Ela confirma que a instrução existe e é clara. Não substitui a execução com o modelo.

| ID | Resultado | Observação |
|---|---|---|
| C01 | Coberto | |
| C02 | Coberto | |
| C03 | Coberto | |
| C04 | Coberto | |
| C05 | Coberto | |
| C06 | Coberto | |
| C07 | Coberto | |
| C08 | Coberto | |
| C09 | Coberto | |
| C10 | Coberto | |
| C11 | Coberto | |
| C12 | Coberto | |
| C13 | Coberto | |

## Como executar

1. Carregue a skill em uma sessão limpa.
2. Envie a entrada de cada caso, uma por vez.
3. Compare a resposta ao comportamento esperado. Registre "passou", "parcial" ou "falhou" e a razão.
4. Se um caso falhar, ajuste a instrução correspondente no `SKILL.md` e repita o caso.
