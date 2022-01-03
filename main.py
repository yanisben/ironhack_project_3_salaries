import pandas as pd
import sqlalchemy as db
import pymysql

pymysql.install_as_MySQLdb()

USER = "root"
PASSWORD = "sql_password_123"
DB_NAME = "project_3_ironhack"
TABLE_NAME = "another_table"
DATAFRAME_PATH = "/Users/bene/Downloads/5 - Salaries_Data_final_non_encoded.csv"

# Creating connection, and initializing new database

engine = db.create_engine(f'mysql://{USER}:{PASSWORD}@localhost')  # connect to server
engine.execute(f"CREATE DATABASE {DB_NAME}")  # create db
engine.execute(f"USE {DB_NAME}")

# Creating a sql table based on the finalized dataframe

df = pd.read_csv(f"{DATAFRAME_PATH}")
df.to_sql(TABLE_NAME, con=engine)  # Reading the csv into a sql table named TABLE_NAME


