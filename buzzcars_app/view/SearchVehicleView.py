import tkinter as tk
from tkinter import ttk

from util.SessionValues import SessionValues
from view.VehicleDetailView import VehicleDetailView  # Import VehicleDetailView
# Nick Start
from view.AddVehicleView import AddVehicleView
from controller.PurchaseController import PurchaseController
from view.InventoryVehicleDetailView import InventoryClerkDetailView


# Nick END

class SearchVehicleView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.controller = None
        # Instance of VehicleDetailView
        # self.detail_view = VehicleDetailView(parent)
        self.detail_view = None
        self.search_label = ttk.Label(parent, text="Search by:", anchor="w")
        self.search_label.grid(row=1, column=0)
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(parent, textvariable=self.search_var, width=30)
        self.search_entry.grid(row=1, column=1, sticky=tk.NSEW)

        self.buttons_frame = ttk.Frame(parent)
        self.buttons_frame.grid(row=1, column=3)
        self.search_button = ttk.Button(self.buttons_frame, text='Search', command=self.search_button_clicked)
        self.search_button.grid(row=0, column=0)
        self.clear_button = ttk.Button(self.buttons_frame, text='Clear', command=self.clear_button_clicked)
        self.clear_button.grid(row=0, column=1)
        self.add_vehicle_button = ttk.Button(self.buttons_frame, text='Add Vehicle', command=self.open_add_vehicle_view)
        self.add_vehicle_button.grid(row=0, column=2)

        self.search_label_type = ttk.Label(parent, text="Vehicle type:", anchor="w")
        self.search_label_type.grid(row=2, column=0)
        self.vehicle_type_var = tk.StringVar()
        self.vehicle_type_combobox = ttk.Combobox(parent, textvariable=self.vehicle_type_var)
        self.vehicle_type_combobox.grid(row=2, column=1, sticky=tk.NSEW)

        self.search_label_manufacturer = ttk.Label(parent, text="Vehicle manufacturer:", anchor="w")
        self.search_label_manufacturer.grid(row=2, column=2)
        self.vehicle_manufacturer_var = tk.StringVar()
        self.vehicle_manufacturer_combobox = ttk.Combobox(parent, textvariable=self.vehicle_manufacturer_var)
        self.vehicle_manufacturer_combobox.grid(row=2, column=3, sticky=tk.NSEW)

        self.search_label_model_year = ttk.Label(parent, text="Model year:", anchor="w")
        self.search_label_model_year.grid(row=3, column=0)
        self.model_year_var = tk.StringVar()
        self.model_year_combobox = ttk.Combobox(parent, textvariable=self.model_year_var)
        self.model_year_combobox.grid(row=3, column=1, sticky=tk.NSEW)

        self.search_label_fuel_type = ttk.Label(parent, text="Fuel type:", anchor="w")
        self.search_label_fuel_type.grid(row=3, column=2)
        self.fuel_type_var = tk.StringVar()
        self.fuel_type_combobox = ttk.Combobox(parent, textvariable=self.fuel_type_var)
        self.fuel_type_combobox.grid(row=3, column=3, sticky=tk.NSEW)

        self.search_label_color = ttk.Label(parent, text="Color:", anchor="w")
        self.search_label_color.grid(row=4, column=0)
        self.color_var = tk.StringVar()
        self.color_combobox = ttk.Combobox(parent, textvariable=self.color_var)
        self.color_combobox.grid(row=4, column=1, sticky=tk.NSEW)

        self.search_label_vin = ttk.Label(parent, text="VIN:", anchor="w")
        self.search_label_vin.grid(row=4, column=2)
        self.vin_var = tk.StringVar()
        self.vin_entry = ttk.Entry(parent, textvariable=self.vin_var, width=30)
        self.vin_entry.grid(row=4, column=3, sticky=tk.NSEW)

        self.sold_status_var = tk.StringVar()
        self.sold_status_label = ttk.Label(parent, text="Sold status:", anchor="w")
        self.sold_status_label.grid(row=5, column=0)
        self.sold_status_combobox = ttk.Combobox(parent, textvariable=self.sold_status_var)
        self.sold_status_combobox.grid(row=5, column=1, sticky=tk.NSEW)

        self.user_var = tk.StringVar()
        self.user_label = ttk.Label(parent, text="User:", anchor="w")
        self.user_label.grid(row=5, column=2)
        self.user_entry = ttk.Entry(parent, textvariable=self.user_var, width=30, state=tk.DISABLED)
        self.user_entry.grid(row=5, column=3, sticky=tk.NSEW)

        # TREEVIEW FOR VEHICLE SEARCH OUTPUT
        self.table = ttk.Treeview(parent, height=30, column=(
            "vin, model_name, model_year, fuel_type, mileage, description, manufacturer, type, color_name, sale_price"),
                                  show='headings')
        self.table.heading("#1", text="Vin", anchor=tk.CENTER)
        self.table.column("#1", minwidth=0, width=170, stretch=tk.NO)
        self.table.heading("#2", text="Type", anchor=tk.CENTER)
        self.table.column("#2", minwidth=0, width=90, stretch=tk.NO)
        self.table.heading("#3", text="Year", anchor=tk.CENTER)
        self.table.column("#3", minwidth=0, width=80, stretch=tk.NO)
        self.table.heading("#4", text="Manufacturer", anchor=tk.CENTER)
        self.table.column("#4", minwidth=0, width=110, stretch=tk.NO)
        self.table.heading("#5", text="Model", anchor=tk.CENTER)
        self.table.column("#5", minwidth=0, width=110, stretch=tk.NO)
        self.table.heading("#6", text="Fuel", anchor=tk.CENTER)
        self.table.column("#6", minwidth=0, width=80, stretch=tk.NO)
        self.table.heading("#7", text="Colors", anchor=tk.CENTER)
        self.table.column("#7", minwidth=0, width=110, stretch=tk.NO)
        self.table.heading("#8", text="Mileage", anchor=tk.CENTER)
        self.table.column("#8", minwidth=0, width=80, stretch=tk.NO)
        self.table.heading("#9", text="Sale price", anchor=tk.CENTER)
        self.table.column("#9", minwidth=0, width=80, stretch=tk.NO)

        self.table.grid(row=6, column=0, columnspan=4, sticky='nsew')

        self.scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=self.table.yview)
        self.table.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=6, column=0, columnspan=4, sticky='ens')

        # Login Logout buttons
        self.login_button = ttk.Button(parent, text='Login', command=self.login_button_clicked)
        self.login_button.grid(row=7, column=0)
        self.logout_button = ttk.Button(parent, text='Logout', command=self.logout_button_clicked)
        self.logout_button.grid(row=7, column=0)

        self.list_count_frame = ttk.Frame(parent)
        self.list_count_frame.grid(row=7, column=3)
        self.vehicle_count_var = tk.StringVar()
        self.vehicle_count_label = ttk.Label(self.list_count_frame, text="Results:", anchor="w")
        self.vehicle_count_label.grid(row=0, column=0)
        self.vehicle_count_entry = ttk.Entry(self.list_count_frame, textvariable=self.vehicle_count_var, width=4,
                                             state=tk.DISABLED)
        self.vehicle_count_entry.grid(row=0, column=1, sticky=tk.NSEW)

        self.list_pending_count_frame = ttk.Frame(parent)
        self.list_pending_count_frame.grid(row=7, column=2)
        self.pending_count_var = tk.StringVar()
        self.pending_count_label = ttk.Label(self.list_pending_count_frame, text="With pending parts:",
                                             anchor="w")
        self.pending_count_label.grid(row=0, column=0)
        self.pending_count_entry = ttk.Entry(self.list_pending_count_frame, textvariable=self.pending_count_var,
                                             width=4,
                                             state=tk.DISABLED)
        self.pending_count_entry.grid(row=0, column=1, sticky=tk.NSEW)

        self.list_available_count_frame = ttk.Frame(parent)
        self.list_available_count_frame.grid(row=7, column=1)
        self.available_count_var = tk.StringVar()
        self.available_count_label = ttk.Label(self.list_available_count_frame, text="Available for purchase:",
                                               anchor="w")
        self.available_count_label.grid(row=0, column=0)
        self.available_count_entry = ttk.Entry(self.list_available_count_frame, textvariable=self.available_count_var,
                                               width=4,
                                               state=tk.DISABLED)
        self.available_count_entry.grid(row=0, column=1, sticky=tk.NSEW)

        # Hide widgets for not privileged users
        self.refresh_view_widgets()

        # Bind the click event when clicking on vehicle row for details
        self.table.bind('<ButtonRelease-1>', self.on_table_click)

    def on_table_click(self, event):
        authenticated_user = SessionValues.get_value("authenticated_user")
        selected_item = self.table.selection()
        if selected_item:
            # Get the values for all columns in the selected row
            row_values = self.table.item(selected_item, 'values')
            if row_values:
                vin = row_values[0]  # Assuming Vin is the first column
                print(f"Clicked on VIN: {vin}")
                if authenticated_user is not None:

                    if authenticated_user.is_inventory_clerk:
                        inventory_clerk_detail_view = InventoryClerkDetailView(self, vin)
                        inventory_clerk_detail_view.geometry("800x600")

                    elif authenticated_user.is_sales_person or authenticated_user.is_manager:
                        self.controller.show_vehicle_details(vin)
                else:
                    self.controller.show_vehicle_details(vin)
        # def refresh_view_widgets(self):
        #     authenticated_user = SessionValues.get_value("authenticated_user")
        #     if authenticated_user is None or not authenticated_user.is_sales_person:
        #         self.sell_car_label.grid_remove()
        #     elif authenticated_user.is_sales_person:
        #         self.sell_car_label.grid()
        # selected_item = self.table.selection()
        # if selected_item:
        #     # Get the values for all columns in the selected row
        #     row_values = self.table.item(selected_item, 'values')
        #     if row_values:
        #         vin = row_values[0]  # Assuming Vin is the first column
        #         print(f"Clicked on VIN: {vin}")
        #         self.controller.show_vehicle_details(vin)
            # self.controller.

    # Show Vehicle Details
    def show_vehicle_details(self, vehicle_details):
        if not self.detail_view:
            # Create VehicleDetailView as a Toplevel window
            self.detail_view = VehicleDetailView(self.master)
            self.detail_view.set_controller(self.controller)

        # Update the details in the VehicleDetailView
        self.detail_view.refresh_view_widgets()
        self.detail_view.update_details(vehicle_details)
        self.detail_view.deiconify()  # Show the hidden window

    def set_controller(self, controller):
        self.controller = controller

    def update_num_vehicles_label(self, num_vehicles):  # Function to update the number of vehicles for sale in VIEW
        print("update_num_vehicles_label")
        # self.num_vehicles_label.config(text=f"Number of Vehicles For Sale: {num_vehicles}")

    def update_counters(self, for_purchase, with_pending_parts):
        self.pending_count_var.set(with_pending_parts)
        self.available_count_var.set(for_purchase)

    def fill_table(self, vehicle_list):
        print("Fill table")
        try:
            if self.table.get_children():
                for row in self.table.get_children():
                    self.table.delete(row)
        except:
            print("Failed at cleaning treeview")

        if len(vehicle_list) == 0:
            self.table.insert('', tk.END, values=(
                "Sorry, it looks like we ", "don’t have ", "that in", " stock!", "", "", "", "", ""))
        for v in vehicle_list:
            self.table.insert('', tk.END, values=(
                v.vin, v.type, v.model_year, v.manufacturer, v.model_name, v.fuel_type, v.color_names, v.mileage,
                v.sales_price))
        self.vehicle_count_var.set(len(vehicle_list))

    def search_button_clicked(self):
        if self.search_var:
            self.controller.execute_search(self.search_var.get(),
                                           self.vehicle_type_var.get(),
                                           self.vehicle_manufacturer_var.get(),
                                           self.model_year_var.get(),
                                           self.fuel_type_var.get(),
                                           self.color_var.get(),
                                           self.vin_var.get(),
                                           self.sold_status_var.get())

    def fill_vehicle_types_combobox(self, vehicle_type_list):
        if vehicle_type_list:
            self.vehicle_type_combobox['values'] = vehicle_type_list

    def fill_vehicle_manufacturer_combobox(self, vehicle_manufacturer_list):
        if vehicle_manufacturer_list:
            self.vehicle_manufacturer_combobox['values'] = vehicle_manufacturer_list

    def fill_model_year_combobox(self, model_year_list):
        if model_year_list:
            self.model_year_combobox['values'] = model_year_list

    def fill_sold_status_combobox(self, sold_status_list):
        if sold_status_list:
            self.sold_status_combobox['values'] = sold_status_list
            self.sold_status_combobox.current(0)

    def fill_fuel_type_combobox(self, fuel_type_list):
        if fuel_type_list:
            self.fuel_type_combobox['values'] = fuel_type_list

    def fill_colors_combobox(self, color_list):
        if color_list:
            self.color_combobox['values'] = color_list

    def clear_button_clicked(self):
        self.vehicle_type_combobox.set('')
        self.vehicle_manufacturer_combobox.set('')
        self.model_year_combobox.set('')
        self.fuel_type_combobox.set('')
        self.color_combobox.set('')
        self.search_entry.delete(0, tk.END)

        # Clear displayed search results in the Treeview widget
        self.table.delete(*self.table.get_children())

        # Clear details in VehicleDetailView using the controller
        self.controller.clear_vehicle_details()

    # Alvaro changes

    def open_add_vehicle_view(self):
        print("Opening Vehicle view...")
        # Nick Start
        add_vehicle_view = AddVehicleView(self.master)  # assuming `self.top` is the parent Toplevel window
        add_vehicle_controller = PurchaseController(add_vehicle_view)
        add_vehicle_view.set_controller(add_vehicle_controller)
        add_vehicle_view.grid(row=0, column=0, columnspan=6, rowspan=16, sticky='nsew')
        # Nick END

    def refresh_view_widgets(self):
        authenticated_user = SessionValues.get_value("authenticated_user")
        self.sold_status_label.grid_remove()
        self.sold_status_combobox.grid_remove()

        if authenticated_user is None:
            self.vin_entry.grid_remove()
            self.search_label_vin.grid_remove()
            self.add_vehicle_button.grid_remove()
            self.logout_button.grid_remove()
            self.login_button.grid()
            self.user_var.set("Guest")
            self.list_pending_count_frame.grid_remove()
            self.list_available_count_frame.grid_remove()
        elif authenticated_user:
            self.vin_entry.grid()
            self.search_label_vin.grid()
            self.login_button.grid_remove()
            self.logout_button.grid()
            self.user_var.set(authenticated_user.username)
            if authenticated_user.is_inventory_clerk:
                self.add_vehicle_button.grid()
                self.list_pending_count_frame.grid()
                self.list_available_count_frame.grid()
            if authenticated_user.is_manager:
                self.sold_status_label.grid()
                self.sold_status_combobox.grid()
                self.list_pending_count_frame.grid()
                self.list_available_count_frame.grid()

    def login_button_clicked(self):
        print("Open login form")
        self.controller.open_login_view()

    def logout_button_clicked(self):
        print("Logout..")
        self.controller.logout()
