from model.PurchaseModel import PurchaseModel
from model.VehicleModel import VehicleModel
class PurchaseController:
    def __init__(self, view, model):
        self.view = view
        self.purchase_model = model  # Instance of PurchaseModel
        self.vehicle_model = VehicleModel()
        # self.fill_manufacturer()
        #^^^causing problems so removed

    def process_purchase(self, purchase_price, purchase_date, condition, customer_id, user_id, vin,
                         model_name, model_year, fuel_type, mileage, description, manufacturer, vehicle_type):
        # Insert into Vehicle table
        inserted_vin = self.purchase_model.insert_vehicle(vin, model_name, model_year, fuel_type, mileage,
                                                          description, manufacturer, vehicle_type)

        if inserted_vin is not None:
            # Insert into Purchase table
            self.purchase_model.insert_purchase(purchase_price, purchase_date, condition, customer_id, user_id, inserted_vin)
            #Create VehicleDetail Page now for Inventory Clerk but in SearchVehicleView where it is called you put the userlogin constraints to show the link and fields
        else:
            print("Error inserting vehicle. Purchase not processed.")


    # def fill_manufacturer(self):
    #
    #     vehicle_manufacturer_list = self.vehicle_model.get_vehicle_manufacturers_as_list()
    #     self.view.fill_vehicle_manufacturer_combobox(vehicle_manufacturer_list)

    #InventoryClerkVehicleDetails
    def get_inventoryclerk_vehicle_details(self, vin):
        """
        Retrieves inventory clerk-specific vehicle details based on VIN.
        Modify this method based on your application's logic.
        """
        # Example: You might have a method in your model like 'get_inventoryclerk_vehicle_details'
        # that fetches details specific to an inventory clerk.
        return self.vehicle_model.get_inventoryclerk_vehicle_details(vin)


    def get_part_details(self, vin):
        return self.vehicle_model.get_part_details(vin)