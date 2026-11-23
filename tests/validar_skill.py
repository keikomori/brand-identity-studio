"""Validação estrutural da skill visual-identity.

Verifica o SKILL.md, os arquivos de referência, os modelos e os casos de teste.
Não executa o modelo: verifica estrutura, carregamento sob demanda, orçamento
de tokens e coerência do texto.

Uso:
    python3 -I tests/validar_skill.py
"""

import os
import re
import sys

try:
    import yaml
except ImportError:
    print("Requer PyYAML: pip install pyyaml --break-system-packages")
    sys.exit(2)

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKILL = os.path.join(RAIZ, "SKILL.md")
CASOS = os.path.join(RAIZ, "tests", "casos-de-teste.md")

ORCAMENTO_SKILL_CHARS = 8000  # carregado a cada acionamento

resultados = []


def check(nome, ok, detalhe=""):
    resultados.append((nome, ok, detalhe))


def ler(caminho):
    with open(caminho, encoding="utf-8") as f:
        return f.read()


texto = ler(SKILL)

# 1. Frontmatter
partes = texto.split("---")
try:
    fm = yaml.safe_load(partes[1])
    check("frontmatter YAML válido", True)
except Exception as e:  # noqa: BLE001
    fm = {}
    check("frontmatter YAML válido", False, str(e))

check("name é 'visual-identity'", fm.get("name") == "visual-identity")
desc = fm.get("description", "")
check("description com até 1024 caracteres", 0 < len(desc) <= 1024, f"{len(desc)} caracteres")
check("description sem colchetes angulares", "<" not in desc and ">" not in desc)
check("description com termo negativo ('Não use para')", "Não use para" in desc)

# 2. Orçamento de tokens do SKILL.md
tamanho = len(texto)
check(
    f"SKILL.md dentro do orçamento de {ORCAMENTO_SKILL_CHARS} caracteres",
    tamanho <= ORCAMENTO_SKILL_CHARS,
    f"{tamanho} caracteres",
)

# 3. Seções obrigatórias do SKILL.md (mapa)
obrigatorias = [
    "## Regras de ouro",
    "## Modos de trabalho",
    "## Condução do briefing",
    "## Formato de cada portão",
    "## Trilhas",
    "## Fases",
    "## Fora do escopo",
    "## Limites",
    "## Recursos sob demanda",
]
for secao in obrigatorias:
    check(f"seção presente: {secao}", secao in texto)

# 4. Arquivos de referência e modelos existem
arquivos_obrigatorios = [
    "references/fases-1-3.md",
    "references/fases-4-7.md",
    "references/trilha-enxuta.md",
    "references/design-md.md",
    "references/revisao.md",
    "references/fontes.md",
    "templates/briefing.md",
    "templates/revisao.md",
    "templates/roteiro-manual.md",
    "templates/checklist-entrega.md",
    "examples/briefing-exemplo.md",
    "tests/casos-de-teste.md",
]
for arq in arquivos_obrigatorios:
    check(f"arquivo existe: {arq}", os.path.exists(os.path.join(RAIZ, arq)))

# 5. Carregamento sob demanda: o SKILL.md deve apontar para cada referência
for ref in ["references/fases-1-3.md", "references/fases-4-7.md", "references/design-md.md",
            "references/revisao.md", "references/trilha-enxuta.md", "references/fontes.md"]:
    check(f"SKILL.md aponta para {ref}", ref in texto)

# 6. Recursos citados no SKILL.md existem
referencias = set(re.findall(r"`((?:templates|examples|tests|references)/[^`]+\.(?:md|py))`", texto))
for ref in sorted(referencias):
    check(f"recurso citado existe: {ref}", os.path.exists(os.path.join(RAIZ, ref)))

# 7. Portão em cada fase, nos arquivos de fase
fases_1_3 = ler(os.path.join(RAIZ, "references", "fases-1-3.md"))
fases_4_7 = ler(os.path.join(RAIZ, "references", "fases-4-7.md"))
todas_fases = re.split(r"\n(?=## )", fases_1_3 + "\n" + fases_4_7)
blocos_fase = [b for b in todas_fases if b.startswith("## Fase") or b.startswith("## Etapa condicional")]
sem_portao = [b.splitlines()[0] for b in blocos_fase if "Portão:" not in b]
check(
    "8 blocos de fase (incl. naming), todos com 'Portão:'",
    len(blocos_fase) == 8 and not sem_portao,
    f"encontrados: {len(blocos_fase)}; sem portão: {sem_portao}",
)

# 8. Formatos DESIGN.md
design = ler(os.path.join(RAIZ, "references", "design-md.md"))
check("design-md.md usa css-tailwind", "`--format css-tailwind`" in design)
check(
    "--format tailwind aparece só como aviso",
    design.count("`--format tailwind`") == 1,
    f"ocorrências: {design.count('`--format tailwind`')}",
)

# 9. Checklist de entrega
checklist = ler(os.path.join(RAIZ, "templates", "checklist-entrega.md"))
itens = re.findall(r"^- \[ \] ", checklist, flags=re.MULTILINE)
check("checklist com pelo menos 15 itens", len(itens) >= 15, f"{len(itens)} itens")

# 9b. Exemplos novos
design_exemplo = ler(os.path.join(RAIZ, "examples", "DESIGN-exemplo.md"))
check("DESIGN-exemplo.md começa com front matter na primeira linha",
      design_exemplo.startswith("---\n"))
manual_exemplo = ler(os.path.join(RAIZ, "examples", "manual-exemplo.md"))
secoes_manual = re.findall(r"^## (\d+)\. ", manual_exemplo, flags=re.MULTILINE)
check("manual-exemplo.md tem as 10 seções do roteiro", secoes_manual == [str(n) for n in range(1, 11)],
      f"seções: {secoes_manual}")

# 9d. Correções da execução de casos
check("descrição cobre tokens para código (C11)", "tokens de design para IA ou código" in desc)
check("Limites cobrem atividades reguladas (C03)", "atividades reguladas" in texto)
check("briefing pergunta atividade regulada (C03)",
      "Atividade regulada?" in ler(os.path.join(RAIZ, "templates", "briefing.md")))

# 9c. Referência de DESIGN.md: tailwind é alias de json-tailwind
check("design-md.md declara tailwind como alias de json-tailwind",
      "alias fixo de `json-tailwind`" in design)

# 10. Termos que não devem voltar
proibidos = ["defensável juridicamente", "Três direções conceituais com racional\n"]
corpus = texto + fases_1_3 + fases_4_7
for termo in proibidos:
    check(f"termo proibido ausente: {termo.strip()[:40]!r}", termo not in corpus)

# 11. Casos de teste
casos = ler(CASOS)
secao_casos, _, secao_resultado = casos.partition("## Resultado da verificação estática")
ids = re.findall(r"^\| (C\d{2}) \|", secao_casos, flags=re.MULTILINE)
check("13 casos de teste (C01 a C13)", ids == [f"C{n:02d}" for n in range(1, 14)], f"ids: {ids}")
linhas_resultado = re.findall(r"^\| (C\d{2}) \| ([^|]+?) \|", secao_resultado, flags=re.MULTILINE)
mapa = dict(linhas_resultado)
pendentes = [i for i in ids if mapa.get(i) != "Coberto"]
check("todos os casos marcados como cobertos na verificação estática", not pendentes, f"pendentes: {pendentes}")

# Relatório
falhas = 0
for nome, ok, detalhe in resultados:
    marca = "PASS" if ok else "FAIL"
    if not ok:
        falhas += 1
    extra = f" ({detalhe})" if detalhe else ""
    print(f"[{marca}] {nome}{extra}")

print()
print(f"{len(resultados) - falhas} de {len(resultados)} verificações passaram.")
sys.exit(1 if falhas else 0)
