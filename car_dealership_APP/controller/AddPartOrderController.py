from model.PartOrderModel import PartOrderModel
from model.VehicleModel import VehicleModel
class AddPartOrderController:
    def __init__(self, view):
        self.view = view
        self.part_order_model = PartOrderModel()
        self.vehicle_model = VehicleModel()


    def vendor_search(self, vendor_name):

        vendor_data = self.part_order_model.search_vendor(vendor_name)

        return vendor_data


    def get_previousPO(self,vin):

        previous_PO = self.part_order_model.get_previousPO(vin)

        return previous_PO

