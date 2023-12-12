from model.repository.PartOrderRepository import PartOrderRepository

class PartOrderModel:
    def __init__(self):
        self.part_order_repository = PartOrderRepository()  # Create an instance of PartOrderRepository

    def search_vendor(self, vendor_name):
        # Call the method in PartOrderRepository to get vendor data
        vendor_data = self.part_order_repository.get_vendor(vendor_name)

        return vendor_data

    def get_previousPO(self,vin):
        previous_PO = self.part_order_repository.get_previousPO(vin)
        return previous_PO

