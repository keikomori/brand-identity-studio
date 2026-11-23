<div align="center">

# 🎨 brand-identity-studio

**Skill especialista em identidade visual e marca, com foco no mercado brasileiro.**

[![Claude Skill](https://img.shields.io/badge/Claude%20Skill-SKILL.md-D97757)](./SKILL.md)
[![Idioma](https://img.shields.io/badge/idioma-pt--BR-009C3B)](./SKILL.md)
[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)](./SKILL.md)
[![DESIGN.md](https://img.shields.io/badge/DESIGN.md-alpha-blueviolet)](https://github.com/google-labs-code/design.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)

</div>

---

## Sobre

Esta skill orienta a criação de identidades visuais completas, do briefing ao manual de marca. Ela parte da estratégia antes do desenho e entrega um sistema utilizável no dia a dia, do Instagram ao Mercado Livre.

## Funcionalidades

- 🧭 **Briefing e pesquisa**: auditoria da marca atual e análise competitiva
- 🎯 **Estratégia de marca**: propósito, personalidade, posicionamento, Kapferer e arquétipos
- ✍️ **Naming**: geração de opções e checagem preliminar no INPI
- ✏️ **Logo**: variações, submarca e testes de squint, cor única, escala e contexto
- 🎨 **Sistema visual**: paleta com contraste WCAG, tipografia com licença comercial e grid
- 📘 **Manual de marca**: aplicações prioritárias e arquivos de entrega
- 🤖 **Tokens para IA**: DESIGN.md validado com `@google/design.md`

## Estrutura

```
brand-identity-studio/
├── SKILL.md          # mapa da skill, carregado a cada acionamento
├── references/       # fases, trilha enxuta, DESIGN.md, revisão e fontes (sob demanda)
├── templates/        # briefing, revisão, roteiro do manual e checklist de entrega
├── examples/         # briefing, manual e DESIGN.md fictícios
├── tests/            # 13 casos de teste e validador estrutural
├── README.md
└── LICENSE
```

O `SKILL.md` é curto de propósito. Os demais arquivos são lidos só quando a fase, a trilha ou o entregável pedem, para economizar tokens.

## Como usar

**Com o Claude:** publique a pasta como skill no Claude Skills. Para o pacote de publicação, inclua `SKILL.md`, `references/`, `templates/` e `examples/`.

**Como instrução de sistema:** copie o conteúdo do [`SKILL.md`](./SKILL.md) para o prompt de um projeto. Sem as referências, a skill perde os detalhes de cada fase.

**Validar a estrutura:** `python3 -I tests/validar_skill.py`

**Validar um DESIGN.md:** `npx @google/design.md lint examples/DESIGN-exemplo.md`

## Roadmap

Concluído:

- [x] Processo em sete fases com portões de aprovação
- [x] Trilha completa e trilha enxuta
- [x] Modelos de briefing, revisão, roteiro do manual e checklist em arquivos separados
- [x] Exemplo de manual de marca completo (fictício)
- [x] Exemplo de DESIGN.md validado com `@google/design.md` 0.4.0, sem erros nem avisos

Pendente:

- [ ] Executar os 13 casos de teste com o modelo, comparando o comportamento ao esperado
- [ ] Exemplo de manual de marca de um cliente real, somente com autorização
- [ ] Atualizar o pacote quando o DESIGN.md sair do alpha

## Contribuir

Sugestões e correções são bem-vindas. Abra uma *issue* para discutir mudanças maiores antes de enviar um *pull request*.

## Mantenedor

**keikomori** · [github.com/keikomori](https://github.com/keikomori)

## Licença

Distribuído sob a licença MIT. Veja [`LICENSE`](./LICENSE) para mais detalhes.

---

<div align="center">

Feito para quem precisa de uma marca que funcione de verdade.

</div>
