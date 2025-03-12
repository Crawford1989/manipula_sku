"""from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

def connect_mssql():
    try:
        user = os.getenv("MSSQL_USER")
        password = os.getenv("MSSQL_PASSWORD")
        host = os.getenv("MSSQL_HOST")
        port = os.getenv("MSSQL_PORT")
        db = os.getenv("MSSQL_DB")
        
        password = quote_plus(password)
        
        engine = create_engine(
            f"mssql://{user}:{password}@{host}:{port}/{db}?driver=ODBC+Driver+17+for+SQL+Server"
        )
        conn_mssql = engine.connect()
        print("Conexão ao MSSQL com sucesso!")
        return conn_mssql
    except Exception as e:
        print(f'Erro ao conectar ao MSSQL: {e}')
        
        
        
        
if __name__ == "__main__":
    connect_mssql()"""