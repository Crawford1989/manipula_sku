import connect_mssql, connect_pg
from sqlalchemy import text

def executa_query():
    try:
        escolha = int(input('Escolha a conexão de onde quer puxar a informação: 1- Postgresql, 2- MSSQL'))
        if escolha == 1:
            conn_pg = connect_pg.connect_postgresql()
            print('Conexão com Postgresql')
            conn = conn_pg
        elif escolha == 2:
            conn_mssql = connect_mssql.connect_mssql()
            print('Conexão com o MSSQL')
            conn = conn_mssql
        else:
            print("Opção invalida")
            
        query = input(f"Digite sua query do {escolha}: ")
        
        result = executa_select(conn, query)
        
        if result is not None:
            print("Resultado da consulta: ")
            sku_formatado = " , ".join(f"'{row[0]}'"for row in result)
            print(sku_formatado)
                
        return conn
    
    except Exception as e:
        print(f'Erro: {e}')
        
        
def executa_select(conn, query):
    try:
        result = conn.execute(text(query))
        return result.fetchall()
    except Exception as e:
        print(f'Erro ao executar a query: {e}')
        return None
        
        
        
        
        
if __name__ == "__main__":
    executa_query()
        

        
