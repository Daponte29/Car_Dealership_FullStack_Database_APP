from util import db
from model.domain.Business import Business


class SaleRepository:
    def save(self, sale_price, sale_date, userID, vin, customerID):
        print("sale_repository: save")
        connection, cursor = db.get_connection(False)
        sql_query = """
            INSERT INTO `Sale` (sale_price, sale_date, userID, vin, customerID)  
            VALUES ROW(%s, %s, %s, %s, %s)
        """
        print(f"Query: {sql_query}")
        cursor.execute(sql_query, (sale_price, sale_date, userID, vin, customerID))
        connection.commit()
        sale_id = cursor.lastrowid
        print(f"New sale id: {sale_id}")
        db.close_connection(cursor, connection)
        return
