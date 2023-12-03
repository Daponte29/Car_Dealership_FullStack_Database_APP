from model.domain.User import User
from model.domain.AuthenticatedUser import AuthenticatedUser
from util import db


class UserRepository:
    def get_all_users(self):
        print("user_repository: get_all_users")
        connection, cursor = db.get_connection(False)
        sql_query = "SELECT userID, first_name, last_name, password FROM User"

        print(f"Query: {sql_query}")
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        user_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                user = User(row[0], row[1], row[2], row[3])
                user_list.append(user)
        else:
            print("get_all_users returned empty result")
        db.close_connection(cursor, connection)
        return user_list

    def get_user_by_user_id(self, user_id):
        print("user_repository: get_user_by_user_id")
        connection, cursor = db.get_connection(True)
        sql_query = """SELECT userID, first_name, last_name, password 
                    FROM User 
                    WHERE userID = %s"""

        print(f"Query: {sql_query}")
        cursor.execute(sql_query, (user_id,))
        if cursor.rowcount > 0:
            row = cursor.fetchone()
            user = User(row[0], row[1], row[2], row[3])
            db.close_connection(cursor, connection)
            return user
        else:
            print("get_user_by_first_name returned empty result")
            db.close_connection(cursor, connection)
            return

    def get_user_by_username_with_role_data(self, username):
        print("user_repository: get_user_by_username")
        connection, cursor = db.get_connection(True)
        sql_query = """SELECT  u.userID, 
                               u.username,
                               u.password,  
                               (u.userID IN (SELECT userID from InventoryClerk)) AS is_inventory_clerk,
                               (u.userID IN (SELECT userID from SalesPerson)) AS is_sales_person,
                               (u.userID IN (SELECT userID from Manager)) AS is_manager
                        FROM User u
                        WHERE username = %s"""

        print(f"Query: {sql_query}")
        cursor.execute(sql_query, (username,))
        if cursor.rowcount > 0:
            row = cursor.fetchone()
            authenticated_user = AuthenticatedUser(row[0], row[1], row[2], row[3], row[4], row[5])
            db.close_connection(cursor, connection)
            return authenticated_user
        else:
            print("get_user_by_username returned empty result")
            db.close_connection(cursor, connection)
            return
