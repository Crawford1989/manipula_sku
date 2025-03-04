from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

def connect_postgresql():
    try:
        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")
        host = os.getenv("POSTGRES_HOST")
        port = os.getenv("POSTGRES_PORT")
        db = os.getenv("POSTGRES_DB")

        password = quote_plus(password)

        engine = create_engine(
            f"postgresql://{user}:{password}@{host}:{port}/{db}"
        )
        conn_pg = engine.connect()
        print("Conexão ao PostgreSQL com sucesso!")
        return conn_pg
    except Exception as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        
        


if __name__ == "__main__":
    connect_postgresql()
