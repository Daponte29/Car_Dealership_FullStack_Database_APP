class SellerHistoryReport:
    def __init__(self, seller_name, total_vehicles_sold, 
                 avg_purchase_price, avg_part_quantity, 
                 avg_cost_of_parts_per_vehicle):
        
        self.seller_name = seller_name
        self.total_vehicles_sold = total_vehicles_sold
        self.avg_purchase_price = avg_purchase_price
        self.avg_part_quantity = avg_part_quantity
        self.avg_cost_of_parts_per_vehicle = avg_cost_of_parts_per_vehicle