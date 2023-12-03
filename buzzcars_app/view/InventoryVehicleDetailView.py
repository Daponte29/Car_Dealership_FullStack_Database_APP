import tkinter as tk
from tkinter import ttk
from controller.PurchaseController import PurchaseController
from util.db import start_connection_pool
from model.PurchaseModel import PurchaseModel
from view.AddPartOrderView import AddPartOrderView
class InventoryClerkDetailView(tk.Toplevel):
    def __init__(self, parent, vin):
        super().__init__(parent)
        self.vin = vin
        self.title("Inventory Clerk Detail View")
        print(self.vin)

        # Add Label for Vehicle Detail View (Inventory Clerk)
        label = ttk.Label(self, text="Vehicle Detail View (Inventory Clerk)", font=("Arial", 12, "bold"),
                          foreground="green", underline=True)
        label.pack(pady=10)
        #First Treeview for VehicleDetails

        self.vehicle_tree = ttk.Treeview(self,
                                         columns=["attribute", "value"],show="headings",height=10)

        self.vehicle_tree.heading("attribute", text="attribute")
        self.vehicle_tree.heading("value", text="value")

        self.vehicle_tree.pack(padx=10, pady=10)
        # Create the second Treeview for parts information
        self.parts_tree = ttk.Treeview(self,
                                       columns=[
                                           "Part Number", "Description", "Part Status", "Cost of Part", "Quantity",
                                           "Total Cost for Part", "Vendor Name", "Purchase Order Number"
                                       ],
                                       show="headings", height=10)

        # Define the headings for the columns
        self.parts_tree.heading("Part Number", text="Part Number")
        self.parts_tree.heading("Description", text="Description")
        self.parts_tree.heading("Part Status", text="Part Status")
        self.parts_tree.heading("Cost of Part", text="Cost of Part")
        self.parts_tree.heading("Quantity", text="Quantity")
        self.parts_tree.heading("Total Cost for Part", text="Total Cost for Part")
        self.parts_tree.heading("Vendor Name", text="Vendor Name")
        self.parts_tree.heading("Purchase Order Number", text="Purchase Order Number")

        self.parts_tree.pack(padx=10, pady=10)
        #Part Order Link to go To AddPartOrderView
        add_part_order_button = ttk.Button(self, text="Add Part Order", command=self.open_add_part_order_view)
        add_part_order_button.pack(pady=10)

        # Populate details based on VIN
        self.show_details()
        self.part_details()

    def show_details(self):
        # Get details based on VIN using the SearchVehicleController
        model = PurchaseModel
        controller = PurchaseController(self, model)
        details = controller.get_inventoryclerk_vehicle_details(self.vin)

        # Print details for debugging
        print("Details:", details)

        # Insert details into Treeview
        for attribute, value in details.items():
            self.vehicle_tree.insert("", "end", values=(attribute, value))
            # Add a new row for Total Part Costs
            total_part_costs = 12345.67  # Replace this with the actual total part costs value somehow get from query
            self.vehicle_tree.insert("", "end", values=("Total Part Costs", total_part_costs))

    def part_details(self):
        model = PurchaseModel
        controller = PurchaseController(self, model)
        details = controller.get_part_details(self.vin)

        # Print details for debugging
        print("Details Parts:", details)

        # Insert part details into the Treeview
        for part_info in details:
            self.parts_tree.insert("", "end", values=(
                part_info["part_number"], part_info["description"], part_info["part_status"],
                part_info["cost_of_part"], part_info["quantity"], part_info["total_cost_for_part"],
                part_info["vendor_name"], part_info["purchase_order_number"]
            ))

    def open_add_part_order_view(self):
        # Open the AddPartOrderView when the link is clicked
        add_part_order_view = AddPartOrderView(self)
        add_part_order_view.geometry("600x400")  # Set your desired size


# root = tk.Tk()
# start_connection_pool()
# app = InventoryClerkDetailView(parent=root, vin="2YHAF0V8512939431")
# app.geometry("800x600")  # Set your desired size
# root.mainloop()