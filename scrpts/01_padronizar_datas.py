def padronizar_data(valor):
    if pd.isna(valor):
        return ""
    valor = str(valor).strip()
    for fmt in ["%d/%m/%Y %H:%M:%S", "%d/%m/%Y", "%Y-%m-%d", "%d%m%Y"]:
        try:
            return pd.to_datetime(valor, format=fmt).strftime("%d/%m/%Y")
        except:
            continue
    return ""

df = pd.read_excel("entrada.xlsx", dtype=str)

colunas_datas = ["DATA DE NASCIMENTO", "DATA DA SOLICITAÇÃO"]

for col in colunas_datas:
    if col in df.columns:
        df[col] = df[col].apply(padronizar_data)

df.to_excel("saida_padronizada.xlsx", index=False)
