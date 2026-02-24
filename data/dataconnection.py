import pyodbc

class DataConnection:
    @staticmethod
    def get_connection():
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost,1433;"
            "DATABASE=QuanLyDienThoai;"
            "UID=sa;"
            "PWD=1234;"
        )
        return conn
    
DataConnection.get_connection()
print("ok")