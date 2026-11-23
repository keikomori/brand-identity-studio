# Execução dos casos de teste

Registro da execução dos casos C01 a C13 contra o texto atual da skill (`SKILL.md` e `references/`).

**Método:** leitura do texto da skill e comparação de cada caso ao comportamento esperado, citando a instrução que se aplica. Não substitui a execução com uma instância nova do modelo, carregando a skill em um contexto limpo. Essa execução independente continua pendente.

| ID | Resultado | Instrução que se aplica | Observação |
|---|---|---|---|
| C01 | Passa | `SKILL.md`, Condução do briefing | Inicia pelo Bloco 1 e limita a três perguntas. |
| C02 | Passa | `SKILL.md`, Trilhas; `references/trilha-enxuta.md` | MEI com orçamento limitado cai na enxuta. Os sete portões são mantidos. |
| C03 | Passa com lacuna | `SKILL.md`, Condução do briefing | A condução funciona, mas a skill não menciona regras de publicidade de conselhos profissionais, que valem para clínicas odontológicas. Ver item abaixo. |
| C04 | Passa | `SKILL.md`, Fora do escopo | Redireciona para `design:design-system`. |
| C05 | Passa | `SKILL.md`, Fora do escopo | Redireciona para `marketing:brand-review`. |
| C06 | Passa | Descrição e Fora do escopo | Legendas ficam fora do escopo. A seção não nomeia um redirecionamento específico. |
| C07 | Passa | `SKILL.md`, Regras de ouro 1; Condução do briefing | Recusa o logo antes da estratégia e oferece exploração marcada. |
| C08 | Passa | `references/fases-1-3.md`, Naming | Avalia as opções, faz a checagem no INPI e aprova o nome na Fase 3. |
| C09 | Passa | `SKILL.md`, Limites | Orienta a busca preliminar e recomenda advogado. Não garante registro. |
| C10 | Passa | `SKILL.md`, Limites; `references/fases-4-7.md`, Fase 7 | Não afirma que o logo gerado por IA é protegível sem verificar a licença. |
| C11 | Passa com ressalva | `references/design-md.md`, item 4; descrição | O formato está correto. Mas o acionamento depende de "tokens de design para IA" na descrição, e o pedido fala de site, não de IA. Ver item abaixo. |
| C12 | Passa | `SKILL.md`, Modos de trabalho; `references/revisao.md` | Entra no modo revisão e não refaz a marca. |
| C13 | Passa | `references/fases-4-7.md`, Fase 7 | Entrega vetor em AI ou EPS, conforme a gráfica. |

## Resultado

- 11 casos passam sem ressalva.
- 2 casos tinham ressalva (C03 e C11). As duas lacunas foram corrigidas, como descrito abaixo.
- Nenhum caso falha.

## Lacunas encontradas e corrigidas

1. **Publicidade de atividades reguladas (C03).** A skill não mencionava as regras de publicidade de conselhos e ordens profissionais. Correção: a pergunta "Atividade regulada?" entrou no Bloco 2 de `templates/briefing.md`, e uma regra nova entrou em Limites de `SKILL.md`.
2. **Acionamento de tokens para sites (C11).** A descrição associava tokens de design apenas a IA. Correção: a descrição passou a dizer "tokens de design para IA ou código".

## Próximo passo

Executar os 13 casos em uma sessão nova, com a skill carregada e sem o histórico deste projeto, e comparar os resultados com a tabela acima.
