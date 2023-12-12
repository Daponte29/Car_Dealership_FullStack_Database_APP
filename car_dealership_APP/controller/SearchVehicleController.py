import threading

from model.UserModel import UserModel
from util.Constants import Constants
from util.SessionValues import SessionValues


class SearchVehicleController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Fill Vehicle type combobox
        t1 = threading.Thread(target=self.fill_vehicle_type_list())

        # Fill vehicle manufacturer combobox
        t2 = threading.Thread(target=self.fill_manufacturer())

        # Fill model year combobox
        t3 = threading.Thread(target=self.fill_model_year())

        # Fill fuel type combobox
        t4 = threading.Thread(target=self.fill_fuel_type())

        # Color type combobox
        t5 = threading.Thread(target=self.fill_colors())

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()

        self.fill_sold_status()
        # Update number vehicle for sale Label
        self.update_num_vehicles_label()
        # Set The linked DetailView
        self.detail_view = None  # Attribute for the Detail View

    def fill_colors(self):
        colors_list = self.model.get_vehicles_colors()
        self.view.fill_colors_combobox(colors_list)

    def fill_fuel_type(self):
        fuel_type_list = self.model.get_vehicles_fuel_types()
        self.view.fill_fuel_type_combobox(fuel_type_list)

    def fill_model_year(self):
        model_year_list = self.model.get_vehicles_model_years()
        self.view.fill_model_year_combobox(model_year_list)

    def fill_sold_status(self):
        values = []
        for key in Constants.SOLD_FILTER_MAP.keys():
            values.append(key)
        self.view.fill_sold_status_combobox(values)

    def set_detail_view(self, detail_view):
        self.detail_view = detail_view

    def show_vehicle_details(self, vin):
        # Get details of the selecteed vehicle using the VehicleModel
        vehicle_details = self.model.get_vehicle_details(vin)
        self.view.show_vehicle_details(vehicle_details)
        # self.detail_view.update_details(vehicle_details)
        # Pass Vin to SalesOrderForm

    def execute_search(self, search_string,
                       vehicle_type,
                       vehicle_manufacturer,
                       model_year,
                       fuel_type,
                       color,
                       vin,
                       sold_filter):
        authenticated_user = SessionValues.get_value("authenticated_user")
        is_inventory_clerk = authenticated_user and authenticated_user.is_inventory_clerk
        vehicle_list = []
        if authenticated_user is None:
            vehicle_list = self.model.search_vehicles(search_string,
                                                      vehicle_type,
                                                      vehicle_manufacturer,
                                                      model_year,
                                                      fuel_type,
                                                      color,
                                                      vin,
                                                      True,
                                                      False)
        else:
            if authenticated_user.is_manager:
                sold_filter_value = Constants.ALL
                if sold_filter:
                    sold_filter_value = Constants.SOLD_FILTER_MAP[sold_filter]

                vehicle_list = self.model.search_vehicles_with_sold_filter(search_string,
                                                                           vehicle_type,
                                                                           vehicle_manufacturer,
                                                                           model_year,
                                                                           fuel_type,
                                                                           color,
                                                                           vin,
                                                                           sold_filter_value)
            elif authenticated_user.is_sales_person:
                vehicle_list = self.model.search_vehicles(search_string,
                                                          vehicle_type,
                                                          vehicle_manufacturer,
                                                          model_year,
                                                          fuel_type,
                                                          color,
                                                          vin,
                                                          True,
                                                          False)
            elif authenticated_user.is_inventory_clerk:
                vehicle_list = self.model.search_vehicles(search_string,
                                                          vehicle_type,
                                                          vehicle_manufacturer,
                                                          model_year,
                                                          fuel_type,
                                                          color,
                                                          vin,
                                                          False,
                                                          True)

        self.view.fill_table(vehicle_list)
        count_result = self.model.search_vehicles_counters(search_string,
                                                           vehicle_type,
                                                           vehicle_manufacturer,
                                                           model_year,
                                                           fuel_type,
                                                           color,
                                                           vin)
        print(f"Counts: f{count_result}")
        if count_result:
            self.view.update_counters(count_result["for_purchase_count"], count_result["with_pending_parts_count"])

    def refresh_session(self):
        authenticated_user = SessionValues.get_value("authenticated_user")
        print(f"Auhenticated user: {authenticated_user}")

        # Update number of vehicles for sale label on public search screen(top right corner)
        self.update_num_vehicles_label()
        self.view.refresh_view_widgets()

    def update_num_vehicles_label(self):
        num_vehicles = self.model.get_num_vehicles_for_sale()
        self.view.update_num_vehicles_label(num_vehicles)

    # Show Vehicle Details linked to clicking on a specific Vehicle on the Search Treeview Results on Public Search Screen
    # Then Calls Model Method/Function
    def show_vehicle_details(self, vin):
        # Retrieve vehicle details from the model based on the VIN
        vehicle_details = self.model.get_vehicle_details(vin)  # Get details from the MODEL logic

        # Notify the view to display the details
        self.view.show_vehicle_details(vehicle_details)  # PASS outputs of MODEL to VIEW method.

    def clear_vehicle_details(self):
        if self.detail_view:
            self.detail_view.clear_details()

    # Alvaro changes
    def open_login_view(self):
        # user_model = UserModel()
        # login_view = LoginView(self.view.master)
        # user_login_controller = UserLoginController(user_model, login_view, self)
        # login_view.set_controller(user_login_controller)
        login_controller = SessionValues.get_login_component()
        login_controller.show_view()

    def logout(self):
        user_model = UserModel()
        user_model.logout()
        login_controller = SessionValues.get_login_component()
        login_controller.logout()

    def close_login_view(self):
        login_controller = SessionValues.get_login_component()
        login_controller.hide_login_form()

    def fill_vehicle_type_list(self):
        vehicle_type_list = self.model.get_vehicle_types_as_list()
        self.view.fill_vehicle_types_combobox(vehicle_type_list)

    def fill_manufacturer(self):
        vehicle_manufacturer_list = self.model.get_vehicle_manufacturers_as_list()
        self.view.fill_vehicle_manufacturer_combobox(vehicle_manufacturer_list)
