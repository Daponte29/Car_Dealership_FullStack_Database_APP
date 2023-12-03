from model.repository.CustomerRepository import CustomerRepository


class CustomerModel:
    def __init__(self):
        self.repository = CustomerRepository()

    def search_business(self, tin=None, business_name=None):
        return self.repository.get_all_business(tin=tin, business_name=business_name)

    def search_individual(self, license_number = None, email =None):
        return self.repository.get_all_individual(license_number=license_number, email= email)

    def add_individual(self, license_number = None, first_name = None, last_name = None, email = None, postal_code = None, state = None, city = None, street = None, phone_number = None):
        return self.repository.add_individual(license_number = license_number, first_name = first_name, last_name = last_name, email = email, postal_code = postal_code, state = state, city = city, street = street, phone_number = phone_number)

    def add_business(self, tin = None, business_name = None, first_name = None, last_name = None, title = None, email = None, postal_code = None, state = None, city = None, street = None, phone_number = None):
        return self.repository.add_business(tin = tin, business_name = business_name, first_name = first_name, last_name = last_name, title = title, email = email, postal_code = postal_code, state = state, city = city, street = street, phone_number = phone_number)

    def purchase_vehicle(self, purchase_price, purchase_date, condition, customer_id, user_id, vin,
                         model_name, model_year, fuel_type, mileage, description, manufacturer, vehicle_type):
        # Validate that required parameters are not None b/c cant be Null for this INSERT
        if None in [purchase_price, purchase_date, condition, customer_id, user_id, vin,
                    model_name, model_year, fuel_type, mileage, description, manufacturer, vehicle_type]:
            raise ValueError("All purchase parameters must have valid values.")

        return self.repository.insert_purchase(purchase_price, purchase_date, condition, customer_id, user_id, vin,
                                               model_name, model_year, fuel_type, mileage, description, manufacturer,
                                               vehicle_type)

