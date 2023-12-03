from model.repository.VehicleRepository import VehicleRepository


class VehicleModel:
    def __init__(self):
        self.repository = VehicleRepository()

    def get_num_vehicles_for_sale(self):  # Gets number of vehicles for sale where all parts are installed.
        get_all_vehicles = self.repository.get_all_vehicles()
        return len(get_all_vehicles)

    def get_pending_parts_vehicle_count(self):
        return self.repository.get_pending_parts_vehicle_count()

    def get_all_vehicles_list(self):
        return self.repository.get_all_vehicles()

    def search_vehicles(self, search_string, vehicle_type, vehicle_manufacturer, model_year, fuel_type, color, vin,
                        for_purchase_only, include_pending):
        return self.repository.search_vehicles(search_string,
                                               vehicle_type,
                                               vehicle_manufacturer,
                                               model_year,
                                               fuel_type,
                                               color,
                                               vin,
                                               for_purchase_only,
                                               include_pending)

    def search_vehicles_with_sold_filter(self, search_string, vehicle_type, vehicle_manufacturer, model_year, fuel_type,
                                         color, vin,
                                         sold_filter):
        return self.repository.search_vehicles_with_sold_filter(search_string,
                                                                vehicle_type,
                                                                vehicle_manufacturer,
                                                                model_year,
                                                                fuel_type,
                                                                color,
                                                                vin,
                                                                sold_filter)

    def search_vehicles_counters(self, search_string, vehicle_type, vehicle_manufacturer, model_year, fuel_type, color,
                                 vin):
        for_purchase_count = self.repository.search_vehicles_count(search_string,
                                                     vehicle_type,
                                                     vehicle_manufacturer,
                                                     model_year,
                                                     fuel_type,
                                                     color,
                                                     vin,
                                                     True,
                                                     False)
        with_pending_parts_count = self.repository.search_vehicles_count(search_string,
                                                                   vehicle_type,
                                                                   vehicle_manufacturer,
                                                                   model_year,
                                                                   fuel_type,
                                                                   color,
                                                                   vin,
                                                                   True,
                                                                   True)
        result_dict = {}
        result_dict['for_purchase_count'] = for_purchase_count
        result_dict['with_pending_parts_count'] = with_pending_parts_count
        return result_dict

    def get_vehicle_types_as_list(self):
        vehicle_types = self.repository.get_all_vehicle_types()
        vehicle_types_list = []
        for vehicle_type in vehicle_types:
            vehicle_types_list.append(vehicle_type)
        return vehicle_types_list

    def get_vehicle_manufacturers_as_list(self):
        vehicle_manufacturers = self.repository.get_all_vehicle_manufacturers()
        vehicle_manufacturer_list = []
        for vehicle_manufacturer in vehicle_manufacturers:
            vehicle_manufacturer_list.append(vehicle_manufacturer)
        return vehicle_manufacturer_list

    def get_vehicles_model_years(self):
        return self.repository.get_all_model_years()

    def get_vehicles_fuel_types(self):
        return self.repository.get_all_vehicle_fuel_types()

    def get_vehicles_colors(self):
        return self.repository.get_all_vehicle_colors()

    # METHODS FOR VehicleDetailView
    def get_vehicle_details(self, vin):
        # Retrieve vehicle details from the repository based on the VIN
        return self.repository.get_vehicle_details(vin)
    #InventoryClerkVehicleDetails
    def get_inventoryclerk_vehicle_details(self, vin):

        return self.repository.get_inventoryclerk_vehicle_details(vin)

    def get_part_details(self,vin):
        return self.repository.get_part_details(vin)