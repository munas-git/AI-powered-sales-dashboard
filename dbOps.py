import os
import pyodbc

from dotenv import load_dotenv
load_dotenv()


# db connection details
server = os.environ["server"]
database = os.environ["database"]
db_username = os.environ["db_username"]
password = os.environ["password"]


def query_db(query:str):
    connection_string = f"Driver={{ODBC Driver 17 for SQL Server}};Server=tcp:{server},1433;Database="\
    f"{database};Uid={db_username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

    # Establish connection and create cursor
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Execute the query & fetch result
    cursor.execute(query)
    result = cursor.fetchone()

    conn.close()

    return result