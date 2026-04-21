import pandas as pd

df_fila = pd.read_excel("fila.xlsx", dtype=str)
df_obitos = pd.read_excel("obitos.xlsx", dtype=str)

df_fila["CHAVE"] = df_fila["NOME"] + "|" + df_fila["DATA DE NASCIMENTO"]
df_obitos["CHAVE"] = df_obitos["NOME"] + "|" + df_obitos["DTNASC"]

df_merge = df_fila.merge(df_obitos[["CHAVE", "DTOBITO"]], on="CHAVE", how="left")

df_merge["DATA_SOL"] = pd.to_datetime(df_merge["DATA DA SOLICITAÇÃO"], dayfirst=True, errors="coerce")
df_merge["DTOBITO"] = pd.to_datetime(df_merge["DTOBITO"], dayfirst=True, errors="coerce")

df_obitos_validos = df_merge[
    (df_merge["DTOBITO"].notna()) &
    (df_merge["DTOBITO"] > df_merge["DATA_SOL"])
]

df_final = df_merge.drop(df_obitos_validos.index)

df_final.to_excel("fila_limpa.xlsx", index=False)
df_obitos_validos.to_excel("obitos_identificados.xlsx", index=False)
