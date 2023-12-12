import tkinter as tk
from tkinter import ttk
from view.SalesOrderForm import SalesOrderForm
from controller.SalesOrderFormController import SalesOrderFormController
#Nick Start
from util.SessionValues import SessionValues

#Nick END



class VehicleDetailView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        self.detail_labels = []
        # self.create_widgets()
        #Nick Start
        # self.authenticated_user = SessionValues.get_value("authenticated_user")

        #Nick END

        self.table = ttk.Treeview(self, column=(
            "vin, model_name, model_year, fuel_type, mileage, description, manufacturer, type, color_name, sale_price"),
                                  show='headings')
        #Nick Start
        self.title_label = ttk.Label(self, text="Vehicle Detail Page", font=('TkDefaultFont', 12, 'bold', 'underline'),
                                                                                                    foreground='green')

        self.title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.W)
        # Adjust starting row to 1 for the first label
        for i in range(1, 11):  # Assuming you want to show 10 rows
            self.key_label = ttk.Label(self, text="", anchor="w")
            self.key_label.grid(row=i, column=0, sticky=tk.W, padx=5, pady=2)
        #
            self.value_label = ttk.Label(self, text="", anchor="w")
            self.value_label.grid(row=i, column=1, sticky=tk.W, padx=5, pady=2)
        #
        # Store the labels as a tuple in self.detail_labels
            self.detail_labels.append((self.key_label, self.value_label))
        # Sell Car Button hidden at first until login click
        self.sell_car_label = ttk.Label(self, text="Sell Car", foreground="blue", cursor="hand2", font = ("TkDefaultFont",10, "bold"))
        self.sell_car_label.grid(row=13, column=0, columnspan=2, pady=10, sticky=tk.W)
        self.sell_car_label.bind("<Button-1>", self.sell_car)  # Corrected line #Command to open SalesOrderForm
        #Back button
        self.style = ttk.Style()
        self.style.configure("Red.TButton", foreground="red")
        self.back_button = ttk.Button(self, text="Go Back", command=self.hide_view, style="Red.TButton")
        self.back_button.grid(row=0, column=3, columnspan=2, pady=10, sticky=tk.W)
        # Hide widgets for not privileged users
        self.refresh_view_widgets()

    def refresh_view_widgets(self):
        authenticated_user = SessionValues.get_value("authenticated_user")
        if authenticated_user is None or not authenticated_user.is_sales_person:
            self.sell_car_label.grid_remove()
        elif authenticated_user.is_sales_person:
            self.sell_car_label.grid()

        #Add session value to show the Parts Table and Status update and Add Part Order button to open AddPartsOrder view


    # def create_widgets(self):
    #     title_label = ttk.Label(self, text="Vehicle Detail Page", font=('TkDefaultFont', 12, 'bold', 'underline'),
    #                             foreground='green')
    #     title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.W)
    #
    #     # Adjust starting row to 1 for the first label
    #     for i in range(1, 11):  # Assuming you want to show 10 rows
    #         key_label = ttk.Label(self, text="", anchor="w")
    #         key_label.grid(row=i, column=0, sticky=tk.W, padx=5, pady=2)
    #
    #         value_label = ttk.Label(self, text="", anchor="w")
    #         value_label.grid(row=i, column=1, sticky=tk.W, padx=5, pady=2)
    #
    #         # Store the labels as a tuple in self.detail_labels
    #         self.detail_labels.append((key_label, value_label))
    #
    #     # ADD a "SELL CAR" Link Only if SalesPerson
    #     #Nick START
    #     authenticated_user = SessionValues.get_value("authenticated_user")
    #     if authenticated_user and authenticated_user.is_sales_person:
    #         sell_car_label = ttk.Label(self, text="Sell Car", foreground="blue", cursor="hand2", font = ("TkDefaultFont",10, "bold"))
    #         sell_car_label.grid(row=13, column=0, columnspan=2, pady=10, sticky=tk.W)
    #         sell_car_label.bind("<Button-1>", self.sell_car) #Command to open SalesOrderForm
    #     #Nick END
    def update_details(self, vehicle_details):
        # Extract vin_value and store it as an attribute
        self.vin_value = vehicle_details.get('vin', '')
        self.sales_price = vehicle_details.get('sale_price')
        # Assuming vehicle_details is a dictionary
        for i, (key, value) in enumerate(vehicle_details.items()):
            if i >= len(self.detail_labels):
                break  # Limit to the number of labels created

            key_label, value_label = self.detail_labels[i]

            # Check if the key is "vin" and set a red font for that label
            if key.lower() == "vin":
                red_font = ttk.Style().configure("Red.TLabel", font=("TkDefaultFont", 10), foreground="red")
                key_label.config(text=f"{key}:", style="Red.TLabel")
                value_label.config(text=f"{value}")
            elif key.lower() == "description":
                bold_green_font = ttk.Style().configure("BoldGreen.TLabel", font=("TkDefaultFont", 10, "bold"),
                                                        foreground="green")
                key_label.config(text=f"{key}:", style="BoldGreen.TLabel")
                value_label.config(text=f"{value}")
            else:
                # For other keys, use the default font
                key_label.config(text=f"{key}:")
                value_label.config(text=f"{value}")


    def sell_car(self, event):
            # Access vin_value from the attribute
            vin_value = getattr(self, 'vin_value', '')
            sales_price = getattr(self, 'sales_price')
            authenticated_user = SessionValues.get_value("authenticated_user")
            userID = authenticated_user.userID
            # Create an instance of SalesOrderForm and pass the VIN
            sales_order_form = SalesOrderForm(self, self, vin_value=vin_value, sales_price=sales_price, userID=userID)
            scontroller = SalesOrderFormController(sales_order_form)
            sales_order_form.set_controller(scontroller)
            # Show the SalesOrderForm
            # Pass VIN to SalesOrderForm
            sales_order_form.grid(row=11, column=0, columnspan=6, sticky=tk.W, padx=5, pady=2)

    #Nick Start
    def hide_view(self):
        # Hide the current vehicle detail view
        self.withdraw()  # Withdraw the window instead of destroying it

    #Nick End