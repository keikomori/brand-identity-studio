# Casos de teste da skill `visual-identity`

Cada caso descreve uma entrada do usuário e o comportamento esperado. Os casos cobrem acionamento positivo, controles negativos, pressão para pular etapas, limites jurídicos, formatos de entrega e revisão.

Os casos C01 a C13 devem ser executados com o Claude carregando a skill e comparados ao comportamento esperado. A coluna "Cobertura" indica a seção do `SKILL.md` ou do arquivo de referência que contém a instrução, para a verificação estática.

| ID | Tipo | Entrada do usuário | Comportamento esperado | Cobertura |
|---|---|---|---|---|
| C01 | Positivo | "Preciso de um logo para minha loja de cosméticos naturais." | Inicia o briefing pelo Bloco 1, faz no máximo três perguntas, não gera logo. | SKILL.md, Condução do briefing |
| C02 | Positivo | "Sou MEI, faço bolos para festas e quero uma marca para o Instagram. Tenho uns R$ 300." | Escolhe a trilha enxuta, registra a escolha e mantém os sete portões. | SKILL.md, Trilhas; references/trilha-enxuta.md |
| C03 | Positivo | "Quero uma identidade para minha clínica odontológica. Ainda não tenho nada." | Faz os blocos, marca as lacunas como hipótese e não gera logo antes da estratégia. | SKILL.md, Condução do briefing |
| C04 | Negativo | "Documente o botão primário do meu design system." | Não aciona o fluxo e indica `design:design-system`. | SKILL.md, Fora do escopo |
| C05 | Negativo | "Revise este post contra o guia de marca." | Não aciona o fluxo e indica `marketing:brand-review`. | SKILL.md, Fora do escopo |
| C06 | Negativo | "Escreva a legenda do post de Dia das Mães." | Não aciona o fluxo. | SKILL.md, Fora do escopo |
| C07 | Pressão | "Pule a estratégia e me mande só o logo agora." | Recusa gerar o logo, explica em uma frase por que a estratégia vem antes e oferece exploração marcada. | SKILL.md, Condução do briefing |
| C08 | Naming | "Preciso de um nome para minha empresa de consultoria." | Avalia opções, faz a checagem preliminar no INPI e só aprova o nome na Fase 3. | references/fases-1-3.md, Naming |
| C09 | Limite jurídico | "Posso registrar esse logo sozinho no INPI?" | Explica a busca preliminar, recomenda advogado e não garante registro. | SKILL.md, Limites e Fora do escopo |
| C10 | Limite de IA | "Gerei o logo com uma IA. Posso usar na minha empresa?" | Não afirma que é protegível ou livre de uso; pede verificação de licença e registro de origem. | SKILL.md, Limites; references/fases-4-7.md, Fase 7 |
| C11 | Formato | "Quero tokens de Tailwind v4 para o site a partir da minha marca." | Gera o DESIGN.md, usa `--format css-tailwind` e indica o lint. | references/design-md.md, item 4 |
| C12 | Revisão | "Tenho uma marca de cinco anos. Avalie se preciso mudar." | Entra no modo revisão, não refaz a marca e entrega o relatório com classificação por área. | SKILL.md, Modos de trabalho; references/revisao.md |
| C13 | Formato | "A gráfica pediu o logo em AI." | Entrega vetor em AI ou EPS, conforme exigido pela gráfica. | references/fases-4-7.md, Fase 7 |

## Resultado da verificação estática

Verificação feita comparando cada caso ao texto atual dos arquivos. Confirma que a instrução existe e é clara. Não substitui a execução com o modelo.

| ID | Resultado | Observação |
|---|---|---|
| C01 | Coberto | |
| C02 | Coberto | |
| C03 | Coberto | |
| C04 | Coberto | Redirecionamento restaurado em "Fora do escopo" |
| C05 | Coberto | Redirecionamento restaurado em "Fora do escopo" |
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
4. Se um caso falhar, ajuste a instrução correspondente e repita o caso.
