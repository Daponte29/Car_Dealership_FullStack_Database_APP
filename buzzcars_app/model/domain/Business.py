from model.domain.Customer import Customer


class Business(Customer):
    def __init__(self, customerID, email, postal_code, state, city, street, phone_number, tin, business_name,
                 first_name, last_name, title):
        super().__init__(customerID, email, postal_code, state, city, street, phone_number)
        self.tin = tin
        self.business_name = business_name
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
