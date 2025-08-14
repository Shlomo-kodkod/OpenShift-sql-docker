import mysql.connector
import logging


logger = logging.getLogger(__name__)


class DataLoader:
    @staticmethod
    def connect_to_db():
        return mysql.connector.connect(
               host="mysql",  
            user="sql-project",
            password="sqldbpass",
            database="porjdb"
        )
    

    def load_data():
        db = DataLoader.connect_to_db()
        try:
            with db.cursor() as cursor:
                cursor.execute("SELECT * FROM Names")
                result = cursor.fetchall()
                if not result:
                    return None
                logger.info("Successfully execute query")
                return result
        except mysql.connector.Error as e:
            logger.info(f"Error while retrieving query: {e}")
            return None
        finally:
            db.close() if db else None
    