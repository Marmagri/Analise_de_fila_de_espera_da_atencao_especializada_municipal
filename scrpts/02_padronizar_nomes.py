import pandas as pd
import unicodedata

def padronizar_nome(nome):
    if pd.isna(nome):
        return ""
    nome = unicodedata.normalize("NFKD", nome).encode("ASCII", "ignore").decode("utf-8")
    return " ".join(nome.upper().split())

df = pd.read_excel("entrada.xlsx", dtype=str)

df["NOME"] = df["NOME"].apply(padronizar_nome)

df.to_excel("saida_nomes.xlsx", index=False)
