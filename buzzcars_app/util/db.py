import mysql.connector


def start_connection_pool():
    print("Starting connection pool...")
    dbconfig = {
        'user': 'gtuser',
        'password': 'team099',
        'host': 'cs6400-fa23-team099.ca31t2t0uc39.us-east-2.rds.amazonaws.com',
        'port': 3306,
        'database': 'cs6400-fa23-team099_Demo'
    }
    connection = mysql.connector.connect(pool_name="buzzcars_pool",
                                         pool_size=6,
                                         **dbconfig)
    print("Connection pool started")
    if connection.is_connected():
        connection.close()


# If the query is going to fetch just one result, then use buffered = True
def get_connection(buffered):
    print("Starting connection to db")
    try:
        connection = mysql.connector.connect(pool_name="buzzcars_pool")
        cursor = connection.cursor(buffered=buffered)
        print("Connected successfully")
        return connection, cursor
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    return


def close_connection(cursor, connection):
    print("Closing connection to db")
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection to db closed")