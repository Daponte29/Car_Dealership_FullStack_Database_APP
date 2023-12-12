import tkinter as tk
from tkinter import ttk
from controller.SalesOrderFormController import SalesOrderFormController
from controller.PurchaseController import PurchaseController
from view.InventoryVehicleDetailView import InventoryClerkDetailView
from model.PurchaseModel import PurchaseModel
from util.db import start_connection_pool
from controller.SearchVehicleController import SearchVehicleController
from controller.SearchVehicleController import SearchVehicleController
from model.VehicleModel import VehicleModel
from view.VehicleDetailView import VehicleDetailView
#from view.SearchVehicleView import SearchVehicleView
from util.SessionValues import SessionValues

class AddVehicleView(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        # parent.title("Buzzcars")
        self.controller = None
        self.top = tk.Toplevel(parent)
        self.tree = None
        self.columns = ["customerID", "license_number", "first_name", "last_name", "email", "postal_code", "state",
                        "city", "street", "phone_number"]
        #self.search_vehicle_view = SearchVehicleView()
        # Add Vehicle Form label
        title_label = ttk.Label(self.top, text="Add Vehicle Form", font=('TkDefaultFont', 12, 'bold', 'underline'),
                                foreground='green')
        title_label.grid(row=0, column=0, columnspan=6, pady=10, sticky=tk.W)
        # Sales Information label
        title_label = ttk.Label(self.top, text="Purchase Information", font=('TkDefaultFont', 10, 'bold', 'underline'),
                                foreground='blue')
        title_label.grid(row=0, column=7, columnspan=6, pady=10, sticky=tk.W)
        ttk.Label(self.top, text="Purchase Price:", font=('TkDefaultFont', 10)).grid(row=1, column=7, sticky=tk.W, padx=5, pady=2)

        self.purchase_price_entry = ttk.Entry(self.top)
        self.purchase_price_entry.grid(row=1, column=8, padx=5, pady=2)

        ttk.Label(self.top, text="Purchase Date(please enter in form: 02-01-2021:", font=('TkDefaultFont', 10)).grid(row=2, column=7, sticky=tk.W, padx=5, pady=2)

        self.purchase_date_entry = ttk.Entry(self.top)
        self.purchase_date_entry.grid(row=2, column=8, padx=5, pady=2)

        condition_label = ttk.Label(self.top, text="Condition:",
                                        font=('TkDefaultFont', 10))
        condition_label.grid(row=3, column=7, sticky=tk.W, padx=5, pady=2)
        condition_values = ["Excellent", "Very Good", "Good", "Fair"]
        self.condition_combobox = ttk.Combobox(self.top, values=condition_values)
        self.condition_combobox.grid(row=3, column=8, padx=5, pady=2)

        ttk.Label(self.top, text="customerID:", font=('TkDefaultFont', 10)).grid(
            row=4, column=7, sticky=tk.W, padx=5, pady=2)

        self.customerID_entry = ttk.Entry(self.top)
        self.customerID_entry.grid(row=4, column=8, padx=5, pady=2)

        ttk.Label(self.top, text="userID:", font=('TkDefaultFont', 10)).grid(
            row=5, column=7, sticky=tk.W, padx=5, pady=2)

        self.userID_entry = ttk.Entry(self.top)
        self.userID_entry.grid(row=5, column=8, padx=5, pady=2)



        ttk.Label(self.top, text="VIN:", font=('TkDefaultFont', 10)).grid(
            row=6, column=7, sticky=tk.W, padx=5, pady=2)

        self.vin_entry = ttk.Entry(self.top)
        self.vin_entry.grid(row=6, column=8, padx=5, pady=2)

        ttk.Label(self.top, text="Model Name:", font=('TkDefaultFont', 10)).grid(
            row=7, column=7, sticky=tk.W, padx=5, pady=2)

        self.model_name_entry = ttk.Entry(self.top)
        self.model_name_entry.grid(row=7, column=8, padx=5, pady=2)

        ttk.Label(self.top, text="Model Year", font=('TkDefaultFont', 10)).grid(
            row=8, column=7, sticky=tk.W, padx=5, pady=2)

        self.model_year_entry = ttk.Entry(self.top)
        self.model_year_entry.grid(row=8, column=8, padx=5, pady=2)


        ttk.Label(self.top, text="mileage", font=('TkDefaultFont', 10)).grid(
            row=9, column=7, sticky=tk.W, padx=5, pady=2)

        self.mileage_entry = ttk.Entry(self.top)
        self.mileage_entry.grid(row=9, column=8, padx=5, pady=2)

        ttk.Label(self.top, text="Description", font=('TkDefaultFont', 10)).grid(
            row=10, column=7, sticky=tk.W, padx=5, pady=2)

        self.description_entry = ttk.Entry(self.top)
        self.description_entry.grid(row=10, column=8, padx=5, pady=2)

        ttk.Label(self.top, text="Manufacturer", font=('TkDefaultFont', 10)).grid(
            row=11, column=7, sticky=tk.W, padx=5, pady=2)

        self.manufacturer_entry = ttk.Entry(self.top)
        self.manufacturer_entry.grid(row=11, column=8, padx=5, pady=2)

        ttk.Label(self.top, text="Type", font=('TkDefaultFont', 10)).grid(
            row=12, column=7, sticky=tk.W, padx=5, pady=2)

        self.type_entry = ttk.Entry(self.top)
        self.type_entry.grid(row=12, column=8, padx=5, pady=2)

    #

        self.vehicle_manufacturer_var = tk.StringVar()
        self.vehicle_manufacturer_combobox = ttk.Combobox(self.top, textvariable=self.vehicle_manufacturer_var)
        self.vehicle_manufacturer_combobox.grid(row=12, column=7, sticky=tk.NSEW)
    #

        ttk.Label(self.top, text="Fuel Type", font=('TkDefaultFont', 10)).grid(
            row=13, column=7, sticky=tk.W, padx=5, pady=2)

        self.fuel_type_entry = ttk.Entry(self.top)
        self.fuel_type_entry.grid(row=13, column=8, padx=5, pady=2)


        #Confirm Purchase - Write into query and load vehicle Detail View for Inventory Clerk
        style = ttk.Style()
        style.configure('Green.TButton', foreground='black', background='green', font=('TkDefaultFont', 10, 'bold'))
        self.purchase_button = ttk.Button(self.top, text='Purchase Vehicle', style='Green.TButton', command=self.on_purchase_click)
        self.purchase_button.grid(row=15, column=7, sticky=tk.W, padx=5, pady=2)

        # Search Customer label
        search_label = ttk.Label(self.top, text="Search Customer:", font=('TkDefaultFont', 10, 'bold', 'underline'))
        search_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)

        # Business section
        business_label = ttk.Label(self.top, text="Business:", font=('TkDefaultFont', 10, 'bold'))
        business_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)

        # Entry widgets for Business section
        ttk.Label(self.top, text="TIN:", font=('TkDefaultFont', 10)).grid(row=3, column=0, sticky=tk.W, padx=5, pady=2)

        self.top.tin_entryS = ttk.Entry(self.top)  # Store it as self.top.tin_entry
        self.top.tin_entryS.grid(row=3, column=1, padx=5, pady=2)

        ttk.Label(self.top, text="Business Name:", font=('TkDefaultFont', 10)).grid(row=3, column=2, sticky=tk.W,
                                                                                padx=5, pady=2)
        self.top.business_name_entryS = ttk.Entry(self.top)
        self.top.business_name_entryS.grid(row=3, column=3, padx=5, pady=2)
        # Search button to the right of Business Name entry
        search_button = ttk.Button(self.top, text="Search Business",command=self.business_search_button_clicked)
        search_button.grid(row=3, column=4, padx=5, pady=2)
        # Individual Search Widgets
        individual_label = ttk.Label(self.top, text="Individual:", font=('TkDefaultFont', 10, 'bold'))
        individual_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Label(self.top, text="License Number:", font=('TkDefaultFont', 10)).grid(row=5, column=0, sticky=tk.W, padx=5,
                                                                                 pady=2)

        self.top.license_number_entryS = ttk.Entry(self.top)
        self.top.license_number_entryS.grid(row=5, column=1, padx=5, pady=2)
        ttk.Label(self.top, text="Email:", font=('TkDefaultFont', 10)).grid(row=5, column=2, sticky=tk.W, padx=5, pady=2)

        self.top.email_entryS = ttk.Entry(self.top)
        self.top.email_entryS.grid(row=5, column=3, padx=5, pady=2)

        # Search button to the right of Individual Name entry
        search_button = ttk.Button(self.top, text="Search Individual", command=self.individual_search_button_clicked)
        search_button.grid(row=5, column=4, padx=5, pady=2)

        # Add Customer label
        search_label = ttk.Label(self.top, text="Add Customer:", font=('TkDefaultFont', 10, 'bold', 'underline'))
        search_label.grid(row=6, column=0, sticky=tk.W, padx=5, pady=2)
        business_label = ttk.Label(self.top, text="Business:", font=('TkDefaultFont', 10, 'bold'))
        business_label.grid(row=7, column=0, sticky=tk.W, padx=5, pady=2)

        ttk.Label(self.top, text="TIN:", font=('TkDefaultFont', 10)).grid(row=8, column=0, sticky=tk.W, padx=5, pady=2)
        self.top.tin_entry = ttk.Entry(self.top)
        self.top.tin_entry.grid(row=8, column=1, padx=5, pady=2)

        ttk.Label(self.top, text="Business Name:", font=('TkDefaultFont', 10)).grid(row=8, column=2, sticky=tk.W, padx=5,
                                                                                pady=2)
        self.top.business_name_entry = ttk.Entry(self.top)
        self.top.business_name_entry.grid(row=8, column=3, padx=5, pady=2)

        ttk.Label(self.top, text="First Name:", font=('TkDefaultFont', 10)).grid(row=8, column=4, sticky=tk.W, padx=5,
                                                                             pady=2)
        self.top.first_name_entryB = ttk.Entry(self.top)
        self.top.first_name_entryB.grid(row=8, column=5, padx=5, pady=2)

        ttk.Label(self.top, text="Last Name:", font=('TkDefaultFont', 10)).grid(row=9, column=0, sticky=tk.W, padx=5,
                                                                            pady=2)
        self.top.last_name_entryB = ttk.Entry(self.top)
        self.top.last_name_entryB.grid(row=9, column=1, padx=5, pady=2)

        ttk.Label(self.top, text="Title:", font=('TkDefaultFont', 10)).grid(row=9, column=2, sticky=tk.W, padx=5, pady=2)
        self.top.title_entry = ttk.Entry(self.top)
        self.top.title_entry.grid(row=9, column=3, padx=5, pady=2)

        ttk.Label(self.top, text="Email:", font=('TkDefaultFont', 10)).grid(row=9, column=4, sticky=tk.W, padx=5, pady=2)
        self.top.email_entryB = ttk.Entry(self.top)
        self.top.email_entryB.grid(row=9, column=5, padx=5, pady=2)

        ttk.Label(self.top, text="Postal Code:", font=('TkDefaultFont', 10)).grid(row=10, column=0, sticky=tk.W, padx=5,
                                                                              pady=2)
        self.top.postal_entryB = ttk.Entry(self.top)
        self.top.postal_entryB.grid(row=10, column=1, padx=5, pady=2)

        ttk.Label(self.top, text="State:", font=('TkDefaultFont', 10)).grid(row=10, column=2, sticky=tk.W, padx=5, pady=2)
        self.top.state_entryB = ttk.Entry(self.top)
        self.top.state_entryB.grid(row=10, column=3, padx=5, pady=2)

        ttk.Label(self.top, text="City:", font=('TkDefaultFont', 10)).grid(row=10, column=4, sticky=tk.W, padx=5, pady=2)
        self.top.city_entryB = ttk.Entry(self.top)
        self.top.city_entryB.grid(row=10, column=5, padx=5, pady=2)

        ttk.Label(self.top, text="Street:", font=('TkDefaultFont', 10)).grid(row=11, column=0, sticky=tk.W, padx=5, pady=2)
        self.top.street_entryB = ttk.Entry(self.top)
        self.top.street_entryB.grid(row=11, column=1, padx=5, pady=2)

        ttk.Label(self.top, text="Phone Number:", font=('TkDefaultFont', 10)).grid(row=11, column=2, sticky=tk.W, padx=5,
                                                                               pady=2)
        self.top.phone_entryB = ttk.Entry(self.top)
        self.top.phone_entryB.grid(row=11, column=3, padx=5, pady=2)
        # Add Business button
        add_business_button = ttk.Button(self.top, text="Add Business", command=self.business_add_button_clicked)
        add_business_button.grid(row=11, column=4, padx=5, pady=2)
        # Individual Add Widgets
        individual_label = ttk.Label(self.top, text="Individual:", font=('TkDefaultFont', 10, 'bold'))
        individual_label.grid(row=12, column=0, sticky=tk.W, padx=5, pady=2)

        ttk.Label(self.top, text="License Number:", font=('TkDefaultFont', 10)).grid(row=13, column=0, sticky=tk.W, padx=5,
                                                                                 pady=2)
        self.top.license_number_entry = ttk.Entry(self.top)
        self.top.license_number_entry.grid(row=13, column=1, padx=5, pady=2)

        ttk.Label(self.top, text="First Name:", font=('TkDefaultFont', 10)).grid(row=13, column=2, sticky=tk.W, padx=5,
                                                                             pady=2)
        self.top.first_name_entry = ttk.Entry(self.top)
        self.top.first_name_entry.grid(row=13, column=3, padx=5, pady=2)

        ttk.Label(self.top, text="Last Name:", font=('TkDefaultFont', 10)).grid(row=13, column=4, sticky=tk.W, padx=5,
                                                                            pady=2)
        self.top.last_name_entry = ttk.Entry(self.top)
        self.top.last_name_entry.grid(row=13, column=5, padx=5, pady=2)

        ttk.Label(self.top, text="Email:", font=('TkDefaultFont', 10)).grid(row=14, column=0, sticky=tk.W, padx=5, pady=2)
        self.top.email_entry = ttk.Entry(self.top)
        self.top.email_entry.grid(row=14, column=1, padx=5, pady=2)

        ttk.Label(self.top, text="Postal Code:", font=('TkDefaultFont', 10)).grid(row=14, column=2, sticky=tk.W, padx=5,
                                                                              pady=2)
        self.top.postal_entry = ttk.Entry(self.top)
        self.top.postal_entry.grid(row=14, column=3, padx=5, pady=2)

        ttk.Label(self.top, text="State:", font=('TkDefaultFont', 10)).grid(row=14, column=4, sticky=tk.W, padx=5, pady=2)
        self.top.state_entry = ttk.Entry(self.top)
        self.top.state_entry.grid(row=14, column=5, padx=5, pady=2)

        ttk.Label(self.top, text="City:", font=('TkDefaultFont', 10)).grid(row=15, column=0, sticky=tk.W, padx=5, pady=2)
        self.top.city_entry = ttk.Entry(self.top)
        self.top.city_entry.grid(row=15, column=1, padx=5, pady=2)

        ttk.Label(self.top, text="Street:", font=('TkDefaultFont', 10)).grid(row=15, column=2, sticky=tk.W, padx=5, pady=2)
        self.top.street_entry = ttk.Entry(self.top)
        self.top.street_entry.grid(row=15, column=3, padx=5, pady=2)

        ttk.Label(self.top, text="Phone Number:", font=('TkDefaultFont', 10)).grid(row=15, column=4, sticky=tk.W, padx=5,
                                                                               pady=2)
        self.top.phone_entry = ttk.Entry(self.top)
        self.top.phone_entry.grid(row=15, column=5, padx=5, pady=2)
        # Add Individual button
        add_individual_button = ttk.Button(self.top, text="Add Individual", command=self.individual_add_button_clicked)
        add_individual_button.grid(row=15, column=6, padx=5, pady=2)

        # Treeview to display  Customer Search and ADD results that when clicked will add to sale info SalesOrder table to Insert into SALE entity.
        # Add a label for the Treeview title
        tree_title_label = ttk.Label(self.top, text="Customer Link to Purchase Table", font=('TkDefaultFont', 10, 'bold'))
        tree_title_label.grid(row=16, column=0, columnspan=6, pady=5)
        # Treeview is initially hidden
        self.top.tree = ttk.Treeview(self.top, columns=self.columns, show="headings")


        # Define column headings
        for col in self.columns:
            self.top.tree.heading(col, text=col)
            self.top.tree.column(col, width=100)
        self.top.tree.column("#0", anchor=tk.W)

        self.top.tree.grid(row=10, column=0, columnspan=6, pady=10)

        self.top.tree.grid(row=10, column=0, columnspan=6, pady=10, sticky=tk.W)
        self.top.tree.grid_remove()  # Hide the Treeview initially
    def fill_vehicle_manufacturer_combobox(self, vehicle_manufacturer_list):
        if vehicle_manufacturer_list:
            self.vehicle_manufacturer_combobox['values'] = vehicle_manufacturer_list
    def set_controller(self, controller):
        self.top.controller = controller


    def business_search_button_clicked(self):
        self.current_section = "business"
        self.update_treeview_columns()
        # Set the controller for the view
        self.controller = SalesOrderFormController(self)
        self.set_controller(self.controller)

        # Call the execute_search_business method on the controller
        self.controller.execute_search_business()

        # Show the Treeview when the button is clicked
        self.top.tree.grid(row=17, column=0, columnspan=6, pady=10, sticky=tk.W)


    def update_business_search_results(self, business_list):
        # Clear existing items in the Treeview
        # Check if business_list is None
        if business_list is None:
            # Handle the case where business_list is None (e.g., display a message or take appropriate action)
            print("No business data available.")
            return
        for item in self.top.tree.get_children():
            self.top.tree.delete(item)

        # Insert new data into the Treeview
        for business in business_list:
            # Assuming each business is an instance of the Business class
            values = [
                business.customerID,
                business.email,
                business.postal_code,
                business.state,
                business.city,
                business.phone_number,
                business.tin,
                business.business_name,
                business.first_name,
                business.last_name,
                business.title,
                business.street
            ]

            self.top.tree.insert("", "end", values=values)

    # Replace instances of self.tree with self.top.tree
    # ...
    def individual_search_button_clicked(self):
        self.current_section = "individual"
        self.update_treeview_columns()
        # Set the controller for the view
        self.controller = SalesOrderFormController(self)
        self.set_controller(self.controller)
        # Show the Treeview when the button is clicked
        # Call the execute_search_business method on the controller
        self.controller.execute_search_individual()
        self.top.tree.grid(row=17, column=0, columnspan=6, pady=10, sticky=tk.W)
    def update_individual_search_results(self, individual_list): # Add the results to the Treeview Table for Customers(Business or Indvidual depending on search button clickked)
        # Clear existing items in the Treeview
        for item in self.top.tree.get_children():
            self.top.tree.delete(item)

        # Insert new data into the Treeview
        for individual in individual_list:
            # Assuming each individual is an instance of the individual class
            values = [
                individual.customerID,
                individual.email,
                individual.postal_code,
                individual.state,
                individual.city,
                individual.street,
                individual.phone_number,
                individual.license_number,
                individual.first_name,
                individual.last_name
            ]

            self.top.tree.insert("", "end", values=values)
    def business_add_button_clicked(self):
        self.current_section = "business"
        self.update_treeview_columns()
        self.controller =SalesOrderFormController(self)
        self.controller.execute_add_business()
        # Show the Treeview when the button is clicked
        self.top.tree.grid(row=17, column=0, columnspan=6, pady=10, sticky=tk.W)

    def individual_add_button_clicked(self):
        self.current_section = "individual"
        self.update_treeview_columns()
        self.controller = SalesOrderFormController(self)
        self.controller.execute_add_individual()
        # Show the Treeview when the button is clicked
        self.top.tree.grid(row=17, column=0, columnspan=6, pady=10, sticky=tk.W)
    def update_treeview_columns(self):
        # Clear existing columns
        for col in self.top.tree["columns"]:
            self.top.tree.heading(col, text="")
            self.top.tree.column(col, width=0)

        # Determine columns based on the current section
        if self.current_section == "business":
            self.columns = ["customerID", "tin", "business_name", "first_name", "last_name", "email", "postal_code",
                            "state", "city", "street", "phone_number", "title"]
        elif self.current_section == "individual":
            self.columns = ["customerID", "license_number", "first_name", "last_name", "email", "postal_code", "state",
                            "city", "street", "phone_number"]

        # Debugging output
        print(f"Existing Columns: {self.columns}")

        # Configure Treeview with new columns and order
        self.top.tree["columns"] = self.columns  # Set columns directly
        for idx, col in enumerate(self.columns):
            self.top.tree.heading(col, text=col)
            self.top.tree.column(col, width=100)

    # def on_purchase_click(self):
    #     from view.SearchVehicleView import SearchVehicleView
    #     from view.VehicleDetailView import VehicleDetailView
    #
    #     self.search_vehicle_view = SearchVehicleView(parent=self.top)
    #     self.search_vehicle_view.show_vehicle_details(vehicle_details=None)

    def on_purchase_click(self):
        # Create an instance of the controller
        purchase_model = PurchaseModel()
        purchase_controller = PurchaseController(self, model=purchase_model)

        # Get values from entry widgets
        purchase_price = self.purchase_price_entry.get()
        purchase_date = self.purchase_date_entry.get()
        condition = self.condition_combobox.get()
        customer_id = self.customerID_entry.get()
        user_id = self.userID_entry.get()
        vin = self.vin_entry.get()
        model_name = self.model_name_entry.get()
        model_year = self.model_year_entry.get()
        fuel_type = self.fuel_type_entry.get()
        mileage = self.mileage_entry.get()
        description = self.description_entry.get()
        manufacturer = self.manufacturer_entry.get()
        vehicle_type = self.type_entry.get()

    #     # Call the method in the controller to handle the purchase
        purchase_controller.process_purchase(purchase_price, purchase_date, condition, customer_id, user_id, vin,
                                             model_name, model_year, fuel_type, mileage, description, manufacturer,
                                             vehicle_type)
        # After processing the purchase, create and show InventoryClerkDetailView
        inventory_clerk_detail_view = InventoryClerkDetailView(self, vin)
        inventory_clerk_detail_view.geometry("800x600")
        # inventory_clerk_detail_view.mainloop()
        # inventory_clerk_detail_view.show_details()
        # inventory_clerk_detail_view.part_details()





