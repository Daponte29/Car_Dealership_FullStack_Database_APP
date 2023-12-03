from util import db
from model.domain.Vendor import Vendor


class PartOrderRepository:

    def get_vendor(self, vendor_name):
        print("part_order_repository: get_vendor_data")
        connection, cursor = db.get_connection(False)

        try:
            if vendor_name:
                # SQL query to select vendor data based on vendor_name
                query = """
                    SELECT *
                    FROM Vendor
                    WHERE vendor_name LIKE %s
                """
                params = (f"%{vendor_name}%",)
            else:
                # SQL query to select all vendor data
                query = """
                    SELECT *
                    FROM Vendor
                """
                params = None

            cursor.execute(query, params)
            result_set = cursor.fetchall()

            vendor_data_list = []
            if cursor.rowcount > 0:
                for row in result_set:
                    vendor_data = Vendor(row[0], row[1], row[2], row[3], row[4], row[5])
                    vendor_data_list.append(vendor_data)
            else:
                print("get_vendor_data returned empty result")

            return vendor_data_list

        except Exception as e:
            # Handle exceptions, rollback the transaction, and print the error
            print(f"Error getting vendor data: {e}")
            return []

        finally:
            # Close the database connection
            db.close_connection(cursor, connection)

    def get_previousPO(self, vin):
        print("part_order_repository: get_previousPO")
        print(f" VIN : {vin}")
        connection, cursor = db.get_connection(False)

        try:
            query = """
                SELECT purchase_order_number
                FROM PartsOrder
                WHERE vin = %s
                ORDER BY CAST(SUBSTRING_INDEX(purchase_order_number, '-', -1) AS SIGNED) DESC
                LIMIT 1
            """
            params = (vin,)

            cursor.execute(query, params)
            result_set = cursor.fetchall()

            if cursor.rowcount > 0:
                # Extract the purchase_order_number from the result
                purchase_order_number = result_set[0][0]
                return purchase_order_number
            else:
                print(f"No previous purchase order found for VIN {vin}")
                return None

        except Exception as e:
            print(f"Error getting previous purchase order: {e}")
            return None

        finally:
            db.close_connection(cursor, connection)
