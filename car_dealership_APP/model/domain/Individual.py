from model.domain.Customer import Customer


class Individual(Customer):
    def __init__(self, customerID, email, postal_code, state, city, street, phone_number, license_number, first_name, last_name):
        super().__init__(customerID, email, postal_code, state, city, street, phone_number) # Give attributes of SuperClass that this class inherits from
        self.license_number = license_number
        self.first_name = first_name
        self.last_name = last_name
