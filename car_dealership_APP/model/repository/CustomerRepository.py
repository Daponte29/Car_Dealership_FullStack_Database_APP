from util import db
from model.domain.Business import Business
from model.domain.Individual import Individual
from datetime import datetime

class CustomerRepository:
    def get_all_business(self, tin, business_name):
        print("customer_repository: get_all_business")
        connection, cursor = db.get_connection(False)

        # Define the base SQL query
        sql_query = """
            SELECT *
            FROM Business NATURAL JOIN Customer
        """
        conditions = []
        params = []

        # Check if TIN is provided and add the condition to the query
        if tin:
            conditions.append("tin LIKE %s")
            params.append(f"%{tin}%")

        # Check if Business Name is provided and add the condition to the query
        if business_name:
            conditions.append("business_name LIKE %s")
            params.append(f"%{business_name}%")

        # Add the WHERE clause if there are conditions
        if conditions:
            sql_query += " WHERE " + " AND ".join(conditions)

        print(f"Query: {sql_query}")
        cursor.execute(sql_query, tuple(params))
        result_set = cursor.fetchall()
        print(f"Result Set: {result_set}")
        business_customer_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                business_customer = Business(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                             row[9], row[10], row[11])
                business_customer_list.append(business_customer)
        else:
            print("get_all_business returned empty result")
        db.close_connection(cursor, connection)
        return business_customer_list
    def get_all_individual(self, license_number, email):
        print("customer_repository: get_all_individual")
        connection, cursor = db.get_connection(False)

        # Define the base SQL query
        sql_query = """
            SELECT *
            FROM Individual NATURAL JOIN Customer
        """
        conditions = []
        params = []

        # Check if TIN is provided and add the condition to the query
        print(f" license: {license_number}")
        if license_number:
            conditions.append("license_number LIKE %s")
            params.append(f"%{license_number}%")

        # Check if Business Name is provided and add the condition to the query
        if email:
            conditions.append("email LIKE %s")
            params.append(f"%{email}%")

        # Add the WHERE clause if there are conditions
        if conditions:
            sql_query += " WHERE " + " AND ".join(conditions)

        print(f"Query: {sql_query}")
        print(f"Column Names: {cursor.description}")
        print(f"Params: {params}")

        cursor.execute(sql_query, tuple(params))
        result_set = cursor.fetchall()
        print(f"Result Set: {result_set}")

        individual_customer_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                individual_customer = Individual(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                                 row[9])

                individual_customer_list.append(individual_customer)
        else:
            print("get_all_individual returned empty result")
        db.close_connection(cursor, connection)
        return individual_customer_list


    # adds Individual and returns list of the newly added person for the treeview in SalesOrderForm
    def add_individual(self, license_number, first_name, last_name, email, postal_code, state, city, street, phone_number):
        print("customer_repository: add_individual")
        connection, cursor = db.get_connection(True)  # Use True for autocommit

        try:
            # Insert into Customer table
            insert_customer_query = """
                INSERT INTO Customer (email, postal_code, state, city, street, phone_number)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            customer_values = (email, postal_code, state, city, street, phone_number)
            cursor.execute(insert_customer_query, customer_values)

            # Retrieve the last inserted customerID
            cursor.execute("SELECT LAST_INSERT_ID()")
            last_customerID = cursor.fetchone()[0]

            # Insert into Individual table using the retrieved customerID
            insert_individual_query = """
                INSERT INTO Individual (license_number, first_name, last_name, customerID)
                VALUES (%s, %s, %s, %s)
            """
            individual_values = (license_number, first_name, last_name, last_customerID)
            cursor.execute(insert_individual_query, individual_values)

            # Commit the transaction
            connection.commit()
            print("Individual added successfully.")

            # Get the newly added individual
            get_individual_query = """
                SELECT *
                FROM Individual NATURAL JOIN Customer
                WHERE customerID = %s
            """
            cursor.execute(get_individual_query, (last_customerID,))
            result_set = cursor.fetchall()

            individual_customer_list = []
            if cursor.rowcount > 0:
                for row in result_set:
                    individual_customer = Individual(row[0], row[1], row[6], row[5], row[4], row[3], row[2], row[7], row[8], row[9])
                    individual_customer_list.append(individual_customer)
                return individual_customer_list #RETURN the 1 Individual to traceback to adding to the SalesOrderForm Treeview

        except Exception as e:
            # Handle exceptions, rollback the transaction, and print the error
            connection.rollback()
            print(f"Error adding individual: {e}")

        finally:
            # Close the database connection
            db.close_connection(cursor, connection)

    def add_business(self, tin, business_name, title, first_name, last_name, email, postal_code, state, city, street,
                     phone_number):
        print("customer_repository: add_business")
        connection, cursor = db.get_connection(True)  # Use True for autocommit

        try:
            # Insert into Customer table
            insert_customer_query = """
                INSERT INTO Customer (email, postal_code, state, city, street, phone_number)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            customer_values = (email, postal_code, state, city, street, phone_number)
            cursor.execute(insert_customer_query, customer_values)

            # Retrieve the last inserted customerID
            cursor.execute("SELECT LAST_INSERT_ID()")
            last_customerID = cursor.fetchone()[0]

            # Insert into Business table using the retrieved customerID
            insert_business_query = """
                INSERT INTO Business (tin, business_name, first_name, last_name, title, customerID)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            business_values = (tin, business_name, first_name, last_name, title, last_customerID)
            cursor.execute(insert_business_query, business_values)

            # Commit the transaction
            connection.commit()
            print("Business added successfully.")

            # Get the newly added business
            get_business_query = """
                SELECT *
                FROM Business NATURAL JOIN Customer
                WHERE customerID = %s
            """
            cursor.execute(get_business_query, (last_customerID,))
            result_set = cursor.fetchall()

            business_customer_list = []
            if cursor.rowcount > 0:
                for row in result_set:
                    business_customer = Business(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                                                 row[8], row[9], row[10], row[11])
                    business_customer_list.append(business_customer)
                    print(business_customer_list)
                return business_customer_list  # RETURN the 1 Business to traceback to adding to the SalesOrderForm Treeview

        except Exception as e:
            # Handle exceptions, rollback the transaction, and print the error
            connection.rollback()
            print(f"Error adding business: {e}")

        finally:
            # Close the database connection
            db.close_connection(cursor, connection)

    def add_sale(self, vin, sales_date, sales_price, userID, customerID):
        print("customer_repository: add_sale")
        connection, cursor = db.get_connection(True)  # Use True for autocommit

        try:
            # Parse and format the sales_date
            # Parse and format the sales_date
            formatted_sales_date = datetime.strptime(sales_date, "%m-%d-%Y").strftime("%Y-%m-%d")

            # Insert into Sale table
            insert_sale_query = """
                INSERT INTO Sale (vin, sale_date, sale_price, userID, customerID)
                VALUES (%s, %s, %s, %s, %s)
            """
            sale_values = (vin, formatted_sales_date, sales_price, userID, customerID)
            cursor.execute(insert_sale_query, sale_values)

            # Commit the transaction
            connection.commit()
            print("Sale added successfully.")

        except Exception as e:
            # Handle exceptions, rollback the transaction, and print the error
            connection.rollback()
            print(f"Error adding sale: {e}")

        finally:
            # Close the database connection
            db.close_connection(cursor, connection)

    def sale_exists(self, vin):
        # Check if a sale with the given VIN already exists
        connection, cursor = db.get_connection(False)  # Adjust based on your database connection logic

        try:
            # Example SQL query to check if a sale with the given VIN exists
            check_sale_query = "SELECT COUNT(*) FROM Sale WHERE vin = %s"
            cursor.execute(check_sale_query, (vin,))
            sale_count = cursor.fetchone()[0]

            return sale_count > 0  # Return True if a sale exists, otherwise return False

        except Exception as e:
            # Handle exceptions (e.g., log the error)
            print(f"Error checking if sale exists: {e}")
            return False

        finally:
            # Close the database connection
            db.close_connection(cursor, connection)

    def insert_sale(self, sale_price, sale_date, userID, vin, customerID):
        # Parse and format the sales_date
        try:
            formatted_sales_date = datetime.strptime(sale_date, "%m-%d-%Y").strftime("%Y-%m-%d")
        except ValueError as e:
            print(f"Error parsing sales_date: {e}")
            return False  # Return False if there's an error in parsing the date

        connection, cursor = db.get_connection(False)  # Adjust based on your database connection logic

        try:
            # Check if a sale with the given VIN already exists
            if self.sale_exists(vin):
                print(f"A sale with VIN {vin} already exists.")
                return False  # Return False if a sale with the given VIN already exists

            # Example SQL query to insert the sale information into the Sale table
            insert_sale_query = """
                INSERT INTO Sale (sale_price, sale_date, userID, vin, customerID)
                VALUES (%s, %s, %s, %s, %s)
            """
            # Use a tuple to pass parameters to cursor.execute
            params = (sale_price, formatted_sales_date, userID, vin, customerID)
            cursor.execute(insert_sale_query, params)

            # Commit the transaction
            connection.commit()

            print("Sale information inserted successfully.")
            success = "Sale information inserted successfully."
            return success  # Return True to indicate successful insertion

        except Exception as e:
            # Handle exceptions (e.g., log the error)
            print(f"Error inserting sale information: {e}")
            return False  # Return False to indicate failure

        finally:
            # Close the database connection
            db.close_connection(cursor, connection)
    #Two functions to insert the Vehicle and then get the vin and insert Purchase
    def insert_vehicle(self, vin, model_name, model_year, fuel_type, mileage, description, manufacturer, vehicle_type):
        print("customer_repository: insert_vehicle")
        connection, cursor = db.get_connection(True)  # Use True for autocommit

        try:
            # Insert into Vehicle table
            insert_vehicle_query = """
                INSERT INTO Vehicle (vin, model_name, model_year, fuel_type, mileage, description, manufacturer, type)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            vehicle_values = (vin, model_name, model_year, fuel_type, mileage, description, manufacturer, vehicle_type)
            cursor.execute(insert_vehicle_query, vehicle_values)

            # Commit the transaction
            connection.commit()
            print("Vehicle added successfully.")

        except Exception as e:
            # Handle exceptions, rollback the transaction, and print the error
            connection.rollback()
            print(f"Error adding vehicle: {e}")
            return None

        finally:
            # Close the database connection
            db.close_connection(cursor, connection)

        return vin  # Return the VIN of the inserted vehicle

    def insert_purchase(self, purchase_price, purchase_date, condition, customer_id, user_id, vin):
        print("customer_repository: insert_purchase")
        connection, cursor = db.get_connection(True)  # Use True for autocommit

        try:
            # Parse and format the purchase_date
            try:
                formatted_purchase_date = datetime.strptime(purchase_date, "%m-%d-%Y").strftime("%Y-%m-%d")
            except ValueError as e:
                print(f"Error parsing purchase_date: {e}")
                return None  # Return None if there's an error in parsing the date

            # Insert into Purchase table
            insert_purchase_query = """
                INSERT INTO Purchase (purchase_date, condition_at_purchase, purchase_price, userID, vin, customerID)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            purchase_values = (formatted_purchase_date, condition, purchase_price, user_id, vin, customer_id)
            cursor.execute(insert_purchase_query, purchase_values)

            # Commit the transaction
            connection.commit()
            print("Purchase added successfully.")

        except Exception as e:
            # Handle exceptions, rollback the transaction, and print the error
            connection.rollback()
            print(f"Error adding purchase: {e}")
            return None

        finally:
            # Close the database connection
            db.close_connection(cursor, connection)

        return cursor.lastrowid  # Return the ID of the inserted purchase

    #End Purcahse Quiery functions
