from model.repository.CustomerRepository import CustomerRepository

class PurchaseModel:
    def __init__(self):
        self.repository = CustomerRepository()
    #These two function insert vehicle then get the vin and call insert_purchase
    def insert_vehicle(self, vin, model_name, model_year, fuel_type, mileage, description, manufacturer, vehicle_type):
        return self.repository.insert_vehicle(vin, model_name, model_year, fuel_type, mileage, description, manufacturer, vehicle_type)

    def insert_purchase(self, purchase_price, purchase_date, condition, customer_id, user_id, vin):
        return self.repository.insert_purchase(purchase_price, purchase_date, condition, customer_id, user_id, vin)
    #Done insert Purchase
