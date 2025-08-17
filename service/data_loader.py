import mysql.connector
import logging


logger = logging.getLogger(__name__)


class DataLoader:
    @staticmethod
    def connect_to_db():
        """
        Establish a connection to the MySQL database.
        Returns a MySQL connection object.
        """
        return mysql.connector.connect(
            host="mysql",  
            user="user",
            password="pwd",
            database="sqldb"
        )
    
    @staticmethod
    def load_data():
        """
        Load data from the 'Names' table in the MySQL database.
        Returns a list containing the names and cities.
        If the table is empty or an error occurs, returns None.
        """
        db = DataLoader.connect_to_db()
        try:
            with db.cursor() as cursor:
                cursor.execute("SELECT * FROM Names;")
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
    