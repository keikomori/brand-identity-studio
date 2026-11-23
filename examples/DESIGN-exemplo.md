---
version: alpha
name: Doceria Exemplo (fictícia)
description: Identidade visual fictícia de uma doceria artesanal de bolos para festas, com encomenda pelo WhatsApp.
colors:
  primary: "#3D2B1F"
  secondary: "#6B5A4E"
  tertiary: "#B5462E"
  neutral: "#FBF7F2"
  on-tertiary: "#FFFFFF"
typography:
  headline-lg:
    fontFamily: Fraunces
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.1
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
rounded:
  sm: 4px
  md: 12px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
components:
  page:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.on-tertiary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: 12px
---

## Overview

A doceria transmite cuidado artesanal e acolhimento de família. O visual deve parecer caseiro sem parecer amador: tons quentes, tipografia com personalidade e pouco ruído.

## Colors

A paleta parte de marrons quentes e de um único acento vermelho-terroso, usado só para ação.

- **Primary (#3D2B1F):** marrom escuro para títulos e texto principal.
- **Secondary (#6B5A4E):** marrom acinzentado para legendas e metadados.
- **Tertiary (#B5462E):** acento usado somente em botões e destaques de ação.
- **Neutral (#FBF7F2):** fundo creme, mais suave que o branco puro.

## Typography

Títulos em Fraunces, texto em Inter. Ambas têm licença aberta (SIL Open Font License) e podem ser usadas em impressos e no digital.

## Layout

Grid de 4 colunas no celular e 12 no desktop. Espaçamento em múltiplos de 4px.

## Elevation & Depth

Sem sombras. Hierarquia por cor e espaço.

## Shapes

Cantos arredondados médios (12px) em cartões e botões. Cantos retos em imagens de produto.

## Components

- **page:** fundo creme com texto marrom escuro. Base de todas as telas.
- **button-primary:** o único botão de destaque em cada tela. Texto branco sobre o acento, com contraste de 5,4:1.

## Do's and Don'ts

- Faça: usar o acento apenas para uma ação por tela.
- Não faça: aplicar o acento em textos longos, em fundos grandes ou em ícones decorativos.
