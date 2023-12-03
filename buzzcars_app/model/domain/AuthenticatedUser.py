class AuthenticatedUser:
    def __init__(self, userID, username, password, is_inventory_clerk, is_sales_person, is_manager):
        self.userID = userID
        self.is_inventory_clerk = is_inventory_clerk
        self.is_sales_person = is_sales_person
        self.is_manager = is_manager
        self.username = username
        self.password = password
