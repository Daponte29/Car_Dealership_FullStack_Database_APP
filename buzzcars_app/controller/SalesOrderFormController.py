from model.UserModel import UserModel
from model.CustomerModel import CustomerModel
from model.SaleModel import SaleModel

class SalesOrderFormController:
    def __init__(self, view):
        #self.model = model
        self.view = view
        self.view.set_controller(self)

    # Search next to Business Clicked
    def execute_search_business(self):
        try:
            # Try to use the top entry
            tin_entry = self.view.top.tin_entryS
            business_name_entry = self.view.top.business_name_entryS
        except AttributeError:
            # If top entry doesn't exist, use the regular entry
            tin_entry = self.view.tin_entryS
            business_name_entry = self.view.business_name_entryS

        tin = tin_entry.get()
        business_name = business_name_entry.get()

        customer_model = CustomerModel()

        # Pass the values to the search_business method
        business_list = customer_model.search_business(tin=tin, business_name=business_name)

        self.view.update_business_search_results(business_list)

    def execute_add_business(self, A=True):
        try:
            # Try to use the top entry
            tin_entry = self.view.top.tin_entry if A else self.view.tin_entry
            business_name_entry = self.view.top.business_name_entry if A else self.view.business_name_entry
            first_name_entry = self.view.top.first_name_entryB if A else self.view.first_name_entryB
            last_name_entry = self.view.top.last_name_entryB if A else self.view.last_name_entryB
            title_entry = self.view.top.title_entry if A else self.view.title_entry
            email_entry = self.view.top.email_entryB if A else self.view.email_entryB
            postal_code_entry = self.view.top.postal_entryB if A else self.view.postal_entryB
            state_entry = self.view.top.state_entryB if A else self.view.state_entryB
            city_entry = self.view.top.city_entryB if A else self.view.city_entryB
            street_entry = self.view.top.street_entryB if A else self.view.street_entryB
            phone_number_entry = self.view.top.phone_entryB if A else self.view.phone_entryB
        except AttributeError:
            # If top entry doesn't exist, use the regular entry
            tin_entry = self.view.tin_entry
            business_name_entry = self.view.business_name_entry
            first_name_entry = self.view.first_name_entryB
            last_name_entry = self.view.last_name_entryB
            title_entry = self.view.title_entry
            email_entry = self.view.email_entryB
            postal_code_entry = self.view.postal_entryB
            state_entry = self.view.state_entryB
            city_entry = self.view.city_entryB
            street_entry = self.view.street_entryB
            phone_number_entry = self.view.phone_entryB

        tin = tin_entry.get()
        business_name = business_name_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        title = title_entry.get()
        email = email_entry.get()
        postal_code = postal_code_entry.get()
        state = state_entry.get()
        city = city_entry.get()
        street = street_entry.get()
        phone_number = phone_number_entry.get()

        customer_model = CustomerModel()

        # Pass the values to the add_business method
        business_list = customer_model.add_business(
            tin=tin,
            business_name=business_name,
            first_name=first_name,
            last_name=last_name,
            title=title,
            email=email,
            postal_code=postal_code,
            state=state,
            city=city,
            street=street,
            phone_number=phone_number
        )

        self.view.update_business_search_results(business_list)

    def execute_search_individual(self):
        try:
            # Try to get values from the current view structure
            license_number = self.view.license_number_entryS.get()
            email = self.view.email_entryS.get()
        except AttributeError:
            # If the current structure doesn't have these attributes, try the alternative structure
            license_number = self.view.top.license_number_entryS.get()
            email = self.view.top.email_entryS.get()

        customer_model = CustomerModel()

        # Pass the values to the search_individual method
        individual_list = customer_model.search_individual(license_number=license_number, email=email)

        self.view.update_individual_search_results(individual_list)

    def execute_add_individual(self):
        license_number = self.view.license_number_entry.get()  # Get the value from the licesne_number entry field
        first_name = self.view.first_name_entry.get()
        last_name = self.view.last_name_entry.get()
        email = self.view.email_entry.get()  # Get the value from the email entry field
        postal_code = self.view.postal_entry.get()
        state = self.view.state_entry.get()
        city = self.view.city_entry.get()
        street = self.view.street_entry.get()
        phone_number = self.view.phone_entry.get()

        customer_model = CustomerModel()

        individual_list = customer_model.add_individual(license_number = license_number, first_name = first_name, last_name = last_name, email = email, postal_code = postal_code, state = state, city = city, street = street, phone_number = phone_number)

        self.view.update_individual_search_results(individual_list)

    def confirm_sale(self, sale_price, sale_date, userID, vin, customerID):
        # Perform actions with the provided values
        print(f"Controller received values: Sale Price={sale_price}, Sale Date={sale_date}, UserID={userID}, VIN={vin}, Customer ID={customerID}")

        sale_model = SaleModel()

        success = sale_model.insert_sale(sale_price, sale_date, userID, vin, customerID)
        if success == "Sale information inserted successfully." :
            return "Sale Inserted Successfully!"
        else:
            return "Failed to Insert Sale."


