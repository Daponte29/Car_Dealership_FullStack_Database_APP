import tkinter as tk
from tkinter import ttk
from util.SessionValues import SessionValues
from controller.SalesOrderFormController import SalesOrderFormController
class SalesOrderForm(tk.Frame):
    def __init__(self, parent, vehicle_detail_view, vin_value="", sales_price = "", userID =""):
        super().__init__(parent)
        self.parent = parent
        self.vehicle_detail_view = vehicle_detail_view
        self.vin_value = vin_value
        self.sales_price = sales_price
        self.userID = userID
        self.controller = None
        self.tree = None
        self.columns = ["customerID", "license_number", "first_name", "last_name", "email", "postal_code", "state",
                            "city", "street", "phone_number"]

        self.create_widgets()

    def set_controller(self, controller):
        self.controller = controller
    def create_widgets(self):
        # Create and place your widgets for the SalesOrderForm

        # Sales Order Form label
        title_label = ttk.Label(self, text="Sales Order Form", font=('TkDefaultFont', 12, 'bold', 'underline'), foreground='green')
        title_label.grid(row=0, column=0, columnspan=6, pady=10, sticky=tk.W)
        # Sales Information label
        title_label = ttk.Label(self, text="Sales Information", font=('TkDefaultFont', 10, 'bold', 'underline'),
                                foreground='blue')
        title_label.grid(row=0, column=7, columnspan=6, pady=10, sticky=tk.W)

        # Search Customer label
        search_label = ttk.Label(self, text="Search Customer:", font=('TkDefaultFont', 10, 'bold', 'underline'))
        search_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)

        # Business section
        business_label = ttk.Label(self, text="Business:", font=('TkDefaultFont', 10, 'bold'))
        business_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)

        # Entry widgets for Business section
        ttk.Label(self, text="TIN:", font=('TkDefaultFont', 10)).grid(row=3, column=0, sticky=tk.W, padx=5, pady=2)

        self.tin_entryS = ttk.Entry(self)  # Store it as self.tin_entry
        self.tin_entryS.grid(row=3, column=1, padx=5, pady=2)

        ttk.Label(self, text="Business Name:", font=('TkDefaultFont', 10)).grid(row=3, column=2, sticky=tk.W,
                                                                                        padx=5, pady=2)
        self.business_name_entryS = ttk.Entry(self)
        self.business_name_entryS.grid(row=3, column=3, padx=5, pady=2)
        # Search button to the right of Business Name entry
        search_button = ttk.Button(self, text="Search Business", command=self.business_search_button_clicked)
        search_button.grid(row=3, column=4, padx=5, pady=2)
        #Individual Search Widgets
        individual_label = ttk.Label(self, text="Individual:", font=('TkDefaultFont', 10, 'bold'))
        individual_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Label(self, text="License Number:", font=('TkDefaultFont', 10)).grid(row=5, column=0, sticky=tk.W,padx=5, pady=2)

        self.license_number_entryS = ttk.Entry(self)
        self.license_number_entryS.grid(row=5, column=1, padx=5, pady=2)
        ttk.Label(self, text="Email:", font=('TkDefaultFont', 10)).grid(row=5, column=2, sticky=tk.W, padx=5,pady=2)

        self.email_entryS = ttk.Entry(self)
        self.email_entryS.grid(row=5, column=3, padx=5, pady=2)

        # Search button to the right of Individual Name entry
        search_button = ttk.Button(self, text="Search Individual", command=self.individual_search_button_clicked)
        search_button.grid(row=5, column=4, padx=5, pady=2)

        # Add Customer label
        search_label = ttk.Label(self, text="Add Customer:", font=('TkDefaultFont', 10, 'bold', 'underline'))
        search_label.grid(row=6, column=0, sticky=tk.W, padx=5, pady=2)
        business_label = ttk.Label(self, text="Business:", font=('TkDefaultFont', 10, 'bold'))
        business_label.grid(row=7, column=0, sticky=tk.W, padx=5, pady=2)

        ttk.Label(self, text="TIN:", font=('TkDefaultFont', 10)).grid(row=8, column=0, sticky=tk.W, padx=5, pady=2)
        self.tin_entry = ttk.Entry(self)
        self.tin_entry.grid(row=8, column=1, padx=5, pady=2)

        ttk.Label(self, text="Business Name:", font=('TkDefaultFont', 10)).grid(row=8, column=2, sticky=tk.W, padx=5, pady=2)
        self.business_name_entry = ttk.Entry(self)
        self.business_name_entry.grid(row=8, column=3, padx=5, pady=2)

        ttk.Label(self, text="First Name:", font=('TkDefaultFont', 10)).grid(row=8, column=4, sticky=tk.W, padx=5, pady=2)
        self.first_name_entryB = ttk.Entry(self)
        self.first_name_entryB.grid(row=8, column=5, padx=5, pady=2)

        ttk.Label(self, text="Last Name:", font=('TkDefaultFont', 10)).grid(row=9, column=0, sticky=tk.W, padx=5, pady=2)
        self.last_name_entryB = ttk.Entry(self)
        self.last_name_entryB.grid(row=9, column=1, padx=5, pady=2)

        ttk.Label(self, text="Title:", font=('TkDefaultFont', 10)).grid(row=9, column=2, sticky=tk.W, padx=5, pady=2)
        self.title_entry = ttk.Entry(self)
        self.title_entry.grid(row=9, column=3, padx=5, pady=2)

        ttk.Label(self, text="Email:", font=('TkDefaultFont', 10)).grid(row=9, column=4, sticky=tk.W, padx=5, pady=2)
        self.email_entryB = ttk.Entry(self)
        self.email_entryB.grid(row=9, column=5, padx=5, pady=2)

        ttk.Label(self, text="Postal Code:", font=('TkDefaultFont', 10)).grid(row=10, column=0, sticky=tk.W, padx=5, pady=2)
        self.postal_entryB = ttk.Entry(self)
        self.postal_entryB.grid(row=10, column=1, padx=5, pady=2)

        ttk.Label(self, text="State:", font=('TkDefaultFont', 10)).grid(row=10, column=2, sticky=tk.W, padx=5, pady=2)
        self.state_entryB = ttk.Entry(self)
        self.state_entryB.grid(row=10, column=3, padx=5, pady=2)

        ttk.Label(self, text="City:", font=('TkDefaultFont', 10)).grid(row=10, column=4, sticky=tk.W, padx=5, pady=2)
        self.city_entryB = ttk.Entry(self)
        self.city_entryB.grid(row=10, column=5, padx=5, pady=2)

        ttk.Label(self, text="Street:", font=('TkDefaultFont', 10)).grid(row=11, column=0, sticky=tk.W, padx=5, pady=2)
        self.street_entryB = ttk.Entry(self)
        self.street_entryB.grid(row=11, column=1, padx=5, pady=2)

        ttk.Label(self, text="Phone Number:", font=('TkDefaultFont', 10)).grid(row=11, column=2, sticky=tk.W, padx=5, pady=2)
        self.phone_entryB = ttk.Entry(self)
        self.phone_entryB.grid(row=11, column=3, padx=5, pady=2)
        # Add Business button
        add_business_button = ttk.Button(self, text="Add Business", command = self.business_add_button_clicked)
        add_business_button.grid(row=11, column=4, padx=5, pady=2)
        #Individual Add Widgets
        individual_label = ttk.Label(self, text="Individual:", font=('TkDefaultFont', 10, 'bold'))
        individual_label.grid(row=12, column=0, sticky=tk.W, padx=5, pady=2)

        ttk.Label(self, text="License Number:", font=('TkDefaultFont', 10)).grid(row=13, column=0, sticky=tk.W, padx=5, pady=2)
        self.license_number_entry = ttk.Entry(self)
        self.license_number_entry.grid(row=13, column=1, padx=5, pady=2)

        ttk.Label(self, text="First Name:", font=('TkDefaultFont', 10)).grid(row=13, column=2, sticky=tk.W, padx=5, pady=2)
        self.first_name_entry = ttk.Entry(self)
        self.first_name_entry.grid(row=13, column=3, padx=5, pady=2)

        ttk.Label(self, text="Last Name:", font=('TkDefaultFont', 10)).grid(row=13, column=4, sticky=tk.W, padx=5,pady=2)
        self.last_name_entry = ttk.Entry(self)
        self.last_name_entry.grid(row=13, column=5, padx=5, pady=2)

        ttk.Label(self, text="Email:", font=('TkDefaultFont', 10)).grid(row=14, column=0, sticky=tk.W, padx=5, pady=2)
        self.email_entry = ttk.Entry(self)
        self.email_entry.grid(row=14, column=1, padx=5, pady=2)

        ttk.Label(self, text="Postal Code:", font=('TkDefaultFont', 10)).grid(row=14, column=2, sticky=tk.W, padx=5,
                                                                              pady=2)
        self.postal_entry = ttk.Entry(self)
        self.postal_entry.grid(row=14, column=3, padx=5, pady=2)

        ttk.Label(self, text="State:", font=('TkDefaultFont', 10)).grid(row=14, column=4, sticky=tk.W, padx=5, pady=2)
        self.state_entry = ttk.Entry(self)
        self.state_entry.grid(row=14, column=5, padx=5, pady=2)

        ttk.Label(self, text="City:", font=('TkDefaultFont', 10)).grid(row=15, column=0, sticky=tk.W, padx=5, pady=2)
        self.city_entry = ttk.Entry(self)
        self.city_entry.grid(row=15, column=1, padx=5, pady=2)

        ttk.Label(self, text="Street:", font=('TkDefaultFont', 10)).grid(row=15, column=2, sticky=tk.W, padx=5, pady=2)
        self.street_entry = ttk.Entry(self)
        self.street_entry.grid(row=15, column=3, padx=5, pady=2)

        ttk.Label(self, text="Phone Number:", font=('TkDefaultFont', 10)).grid(row=15, column=4, sticky=tk.W, padx=5,
                                                                               pady=2)
        self.phone_entry = ttk.Entry(self)
        self.phone_entry.grid(row=15, column=5, padx=5, pady=2)
        # Add Individual button
        add_individual_button = ttk.Button(self, text="Add Individual", command=self.individual_add_button_clicked)
        add_individual_button.grid(row=15, column=6, padx=5, pady=2)





        # Treeview to display  Customer Search and ADD results that when clicked will add to sale info SalesOrder table to Insert into SALE entity.
        # Add a label for the Treeview title
        tree_title_label = ttk.Label(self, text="Customer Link to Sale Table", font=('TkDefaultFont', 10, 'bold'))
        tree_title_label.grid(row=16, column=0, columnspan=6, pady=5)
        # Treeview is initially hidden
        self.tree = ttk.Treeview(self, columns=self.columns, show="headings")


        # Define column headings
        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.column("#0", anchor=tk.W)

        self.tree.grid(row=10, column=0, columnspan=6, pady=10)

        self.tree.grid(row=10, column=0, columnspan=6, pady=10, sticky=tk.W)
        self.tree.grid_remove()  # Hide the Treeview initially
        # Automatically generate customerID for Sale entry based on table click
        self.tree.bind("<Double-Button-1>", self.tree_item_selected)




        # VIN section at the bottom
        vin_label = ttk.Label(self, text="VIN:")
        vin_label.grid(row=1, column=7, sticky=tk.W, padx=5, pady=2)
        vin_label.configure(foreground="blue")
        self.vin_var = tk.StringVar(value=self.vin_value)
        vin_entry = ttk.Entry(self, textvariable=self.vin_var)  # Use the VIN value
        vin_entry.grid(row=1, column=8, padx=5, pady=2)

        # Sales Date entry field
        sales_date_label = ttk.Label(self, text="Sales Date(please enter manually in form 01-03-2021):")
        sales_date_label.grid(row=2, column=7, sticky=tk.W, padx=5, pady=2)
        sales_date_label.configure(foreground="blue")
        self.sales_date_entry = ttk.Entry(self)
        self.sales_date_entry.grid(row=2, column=8, padx=5, pady=2)
        #UserID entry field
        userID_label = ttk.Label(self, text="userID:")
        userID_label.grid(row=3, column=7, sticky=tk.W, padx=5, pady=2)
        userID_label.configure(foreground="blue")
        self.userID_var = tk.DoubleVar(value=self.userID)  # Assuming sales_price is a float
        userID_entry = ttk.Entry(self, textvariable=self.userID_var)
        userID_entry.grid(row=3, column=8, padx=5, pady=2)

        # # Create the Label and Entry for Sales Price
        sales_price_label = ttk.Label(self, text="Sales Price(please enter manually from vehicle detail page:")
        sales_price_label.grid(row=4, column=7, sticky=tk.W, padx=5, pady=2)
        sales_price_label.configure(foreground="blue")
        self.sale_var = tk.StringVar(value=self.sales_price)
        sales_price_entry = ttk.Entry(self, textvariable=self.sale_var)  # Use the sales price value
        sales_price_entry.grid(row=4, column=8, padx=5, pady=2)

        #Chosen customer buying the vehicle userID populated after clicking the Customer on the CustomerLink to Sale Table
        customer_id_label = ttk.Label(self, text="customerID:")
        customer_id_label.grid(row=5, column=7, sticky=tk.W, padx=5, pady=2)
        customer_id_label.configure(foreground="blue")
        self.customerID_entry = ttk.Entry(self)
        self.customerID_entry.grid(row=5, column=8, padx=5, pady=2)
        #Confirm Sale
        style = ttk.Style()
        style.configure("BoldGreen.TButton", font=('TkDefaultFont', 10, 'bold'), foreground='green')

        confirm_sale_button = ttk.Button(self, text="Confirm Sale", style="BoldGreen.TButton", command=self.confirm_sale_button_clicked)
        confirm_sale_button.grid(row=9, column=8, padx=5, pady=2)
        # Label for displaying success message for insert sale
        self.success_label = ttk.Label(self, text="", font=('TkDefaultFont', 10, 'bold'), foreground='green')
        self.success_label.grid(row=10, column=8, columnspan=6, pady=5, sticky=tk.W)

        # "Go Back" button in the top right corner to exit SalesOrderForm
        style = ttk.Style()
        # Configure the style to change the background color of the button
        style.configure("Red.TButton", background="red")
        go_back_button = ttk.Button(self, text="Go Back", command=self.go_back, style="Red.TButton")
        go_back_button.grid(row=9, column=7, sticky=tk.E, pady=10, padx=10)

    def tree_item_selected(self, event): # Function to populate customerID entry for Sale confirmation(could do others as well but dont think needed for Sale Insert.
        # Get the selected item from the Treeview
        selected_item = self.tree.selection()

        if selected_item:
            # Retrieve the values of the selected item
            item_values = self.tree.item(selected_item, "values")

            # Assuming customerID is the first value in the list
            customer_id = item_values[0]

            # Update the customerID entry
            self.customerID_entry.delete(0, tk.END)  # Clear existing text
            self.customerID_entry.insert(0, customer_id)  # Insert the selected customerID

    def go_back(self):
        # Implement logic to go back to the VehicleDetailView
        self.grid_forget()  # Remove the SalesOrderForm from the view
        self.vehicle_detail_view.grid(row=11, column=0, columnspan=2, sticky=tk.W, padx=5, pady=2)

    def business_search_button_clicked(self):
        self.current_section = "business"
        self.update_treeview_columns()
        self.controller.execute_search_business()
        # Show the Treeview when the button is clicked
        self.tree.grid(row=17, column=0, columnspan=6, pady=10, sticky=tk.W)
    def business_add_button_clicked(self):
        self.current_section = "business"
        self.update_treeview_columns()
        self.controller.execute_add_business()
        # Show the Treeview when the button is clicked
        self.tree.grid(row=17, column=0, columnspan=6, pady=10, sticky=tk.W)
    def individual_search_button_clicked(self):
        self.current_section = "individual"
        self.update_treeview_columns()
        self.controller.execute_search_individual()
        # Show the Treeview when the button is clicked
        self.tree.grid(row=17, column=0, columnspan=6, pady=10, sticky=tk.W)

    def individual_add_button_clicked(self):
        self.current_section = "individual"
        self.update_treeview_columns()
        self.controller.execute_add_individual()
        # Show the Treeview when the button is clicked
        self.tree.grid(row=17, column=0, columnspan=6, pady=10, sticky=tk.W)
    def update_business_search_results(self, business_list):
        # Clear existing items in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

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

            self.tree.insert("", "end", values=values)


    def update_individual_search_results(self, individual_list): # Add the results to the Treeview Table for Customers(Business or Indvidual depending on search button clickked)
        # Clear existing items in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

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

            self.tree.insert("", "end", values=values)

    COLUMN_MAPPING = {
        "business": ["customerID", "tin", "email", "phone_number", "street",
                     "city", "state", "postal_code", "title", "last_name",
                     "first_name", "business_name"],
        "individual": ["customerID", "license_number", "first_name", "last_name", "email", "postal_code", "state",
                       "city", "street", "phone_number"]
    }

    # Update the update_treeview_columns method
    def update_treeview_columns(self):
        # Clear existing columns
        for col in self.tree["columns"]:
            self.tree.heading(col, text="")
            self.tree.column(col, width=0)

        # Determine columns based on the current section
        if self.current_section == "business":
            self.columns = ["customerID", "tin", "business_name", "first_name", "last_name",  "email", "postal_code",
                            "state", "city",  "street","phone_number", "title"]
        elif self.current_section == "individual":
            self.columns = ["customerID", "license_number", "first_name", "last_name", "email", "postal_code", "state",
                            "city", "street", "phone_number"]

        # Debugging output
        print(f"Existing Columns: {self.columns}")

        # Configure Treeview with new columns and order
        self.tree["columns"] = self.columns  # Set columns directly
        for idx, col in enumerate(self.columns):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Show the Treeview
        self.tree.grid(row=10, column=0, columnspan=6, pady=10, sticky=tk.W)
        self.tree.grid_remove()  # Hide the Treeview initially
        # Automatically generate customerID for Sale entry based on table click
        self.tree.bind("<Double-Button-1>", self.tree_item_selected)


    #Function to Add Sale
    def confirm_sale_button_clicked(self):
        sale_price = self.sale_var.get()
        sale_date = self.sales_date_entry.get()
        userID = self.userID_var.get()
        vin = self.vin_var.get()
        customerID = self.customerID_entry.get()
        print(
            f"Sale Price: {sale_price}, Sale Date: {sale_date}, UserID: {userID}, VIN: {vin}, Customer ID: {customerID}")
        # Check if the controller is available
        if self.controller:
            # Call a method in the controller and pass the values
            success_message = self.controller.confirm_sale(sale_price, sale_date, userID, vin, customerID)
            self.show_success_message(success_message)
        else:
            # If the controller is not available, create an instance of it
            self.controller = SalesOrderFormController()
            # Call the confirm_sale method
            success_message =self.controller.confirm_sale(sale_price, sale_date, userID, vin, customerID)
            self.show_success_message(success_message)

    def show_success_message(self, message):
        # Update the success label with the provided message
        self.success_label.config(text=message)
        # Show the success label
        self.success_label.grid(row=10, column=8, columnspan=6, pady=5, sticky=tk.W)




