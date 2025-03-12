from  select_inicial import executa_query
import pandas as pd

sku_formatado = executa_query()

if sku_formatado:
    df = pd.DataFrame({"SKU Formatado": [sku_formatado]})
    
    df.to_excel("sku_formatado.xlsx", index=False)
    print("Arquivo excel gerado com sucesso!")
else:
    print("Nenhum Sku encontrado!")