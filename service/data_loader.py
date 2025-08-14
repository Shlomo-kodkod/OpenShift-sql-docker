import mysql.connector



class DataLoader:
    @staticmethod
    def get_db():
        return mysql.connector.connect(
               host="mysql",  
            user="sql-project",
            password="sqldbpass",
            database="names"
        )
            
    