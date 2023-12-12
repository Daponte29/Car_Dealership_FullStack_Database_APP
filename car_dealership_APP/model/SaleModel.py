from model.repository.CustomerRepository import CustomerRepository


class SaleModel:
    def __init__(self):
        self.repository = CustomerRepository()

    def insert_sale(self, sale_price, sale_date, userID, vin, customerID):
        # Call the repository method to insert the sale information into the database
        return self.repository.insert_sale(sale_price, sale_date, userID, vin, customerID)
