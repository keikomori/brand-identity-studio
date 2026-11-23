"""Validação estrutural da skill visual-identity.

Executa verificações automáticas sobre o SKILL.md, os recursos referenciados
e os casos de teste. Não executa o modelo: verifica a estrutura e a coerência
do texto.

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

# 2. Tamanho
linhas = texto.count("\n")
check("SKILL.md com menos de 500 linhas", linhas < 500, f"{linhas} linhas")

# 3. Seções obrigatórias
obrigatorias = [
    "## Modos de trabalho",
    "## Quando usar",
    "## Princípios",
    "## Como conduzir a conversa",
    "## Formato de cada portão",
    "## Trilhas de execução",
    "## Processo",
    "## Sistema visual para agentes de IA",
    "## Modo revisão",
    "## Checklist de entrega",
    "## Limites",
    "## Recursos",
    "## Fontes de referência",
]
for secao in obrigatorias:
    check(f"seção presente: {secao}", secao in texto)

# 4. Portão em cada fase
fases = re.split(r"\n(?=### )", texto)
fases_com_processo = [f for f in fases if f.startswith("### Fase") or f.startswith("### Etapa condicional")]
sem_portao = [f.splitlines()[0] for f in fases_com_processo if "Portão:" not in f]
check(
    "todas as fases têm linha 'Portão:'",
    len(fases_com_processo) == 8 and not sem_portao,
    f"fases encontradas: {len(fases_com_processo)}; sem portão: {sem_portao}",
)

# 5. Recursos referenciados existem
referencias = set(re.findall(r"`((?:templates|examples|tests)/[^`]+\.(?:md|py))`", texto))
for ref in sorted(referencias):
    check(f"recurso existe: {ref}", os.path.exists(os.path.join(RAIZ, ref)))

# 6. Consistência de formatos DESIGN.md
check("usa css-tailwind", "`--format css-tailwind`" in texto)
check(
    "--format tailwind aparece só como aviso",
    texto.count("`--format tailwind`") == 1,
    f"ocorrências: {texto.count('`--format tailwind`')}",
)

# 7. Checklist
itens = re.findall(r"^- \[ \] ", texto, flags=re.MULTILINE)
check("checklist com pelo menos 15 itens", len(itens) >= 15, f"{len(itens)} itens")

# 8. Termos que não devem voltar
proibidos = ["defensável juridicamente", "Três direções conceituais com racional\n"]
for termo in proibidos:
    check(f"termo proibido ausente: {termo.strip()[:40]!r}", termo not in texto)

# 9. Casos de teste
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
