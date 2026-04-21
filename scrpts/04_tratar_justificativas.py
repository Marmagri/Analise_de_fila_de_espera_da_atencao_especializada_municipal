import pandas as pd
import re

# === 1. Carregar dados ===
df = pd.read_excel("entrada.xlsx", dtype=str)

col_just = "SOLICITACAO_JUSTIFICATIVA"

# === 2. Função de exclusão ===
def deve_excluir(texto):
    if pd.isna(texto):
        return False

    texto = str(texto).lower().strip()

    # regra 1: muito curto
    if len(texto) < 10:
        return True

    # regra 2: palavras vagas
    avaliacao = any(re.search(p, texto) for p in ['avalia', r'\bav\b', r'\baval\b'])
    conduta = any(re.search(p, texto) for p in [r'\bcd\b', 'condut', 'cdta'])

    return avaliacao and conduta and len(texto) < 20

# === 3. Aplicar filtro ===
mask = df[col_just].apply(deve_excluir)

print(f"Total de registros removidos por justificativa: {mask.sum()}")

df_filtrado = df[~mask]

# === 4. Salvar ===
df_filtrado.to_excel("saida_justificativa_filtrado.xlsx", index=False)
