import tkinter as tk
from tkinter import ttk
from controller.AddPartOrderController import AddPartOrderController
from util.db import start_connection_pool
class AddPartOrderView(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controller = None
        self.top = tk.Toplevel(parent)
        self.top.title("Add Part Order Form")  # Set the title of the Toplevel window

        # Add Vehicle Form label
        title_label = ttk.Label(self.top, text="Add Part Order Form", font=('TkDefaultFont', 12, 'bold', 'underline'),
                                foreground='green')
        title_label.grid(row=0, column=0, columnspan=7, pady=10)

        # Search Vendor label
        search_label = ttk.Label(self.top, text="Search Vendor:", font=('TkDefaultFont', 10, 'bold', 'underline'))
        search_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)



        # Entry widgets for Business section
        ttk.Label(self.top, text="Vendor Name:", font=('TkDefaultFont', 10)).grid(row=3, column=0, sticky=tk.W, padx=5, pady=2)
        self.top.vendor_name_entryS = ttk.Entry(self.top)  # Store it as self.top.tin_entry
        self.top.vendor_name_entryS.grid(row=3, column=1, padx=5, pady=2)


        # Search button to the right of Individual Name entry
        search_button = ttk.Button(self.top, text="Search Vendor", command=self.vendor_search_button_clicked)
        search_button.grid(row=5, column=4, padx=5, pady=2)


        # Add Vendor label
        search_label = ttk.Label(self.top, text="Add Vendor:", font=('TkDefaultFont', 10, 'bold', 'underline'))
        search_label.grid(row=6, column=0, sticky=tk.W, padx=5, pady=2)



        ttk.Label(self.top, text="Vendor Name:", font=('TkDefaultFont', 10)).grid(row=10, column=0, sticky=tk.W, padx=5,
                                                                                  pady=2)
        self.top.vendor_name_entry = ttk.Entry(self.top)
        self.top.vendor_name_entry.grid(row=10, column=1, padx=5, pady=2)

        ttk.Label(self.top, text="State:", font=('TkDefaultFont', 10)).grid(row=10, column=2, sticky=tk.W, padx=5,
                                                                            pady=2)
        self.top.state_entry = ttk.Entry(self.top)
        self.top.state_entry.grid(row=10, column=3, padx=5, pady=2)

        ttk.Label(self.top, text="City:", font=('TkDefaultFont', 10)).grid(row=10, column=4, sticky=tk.W, padx=5,
                                                                           pady=2)
        self.top.city_entry = ttk.Entry(self.top)
        self.top.city_entry.grid(row=10, column=5, padx=5, pady=2)

        ttk.Label(self.top, text="Street:", font=('TkDefaultFont', 10)).grid(row=11, column=0, sticky=tk.W, padx=5,
                                                                             pady=2)
        self.top.street_entry = ttk.Entry(self.top)
        self.top.street_entry.grid(row=11, column=1, padx=5, pady=2)

        ttk.Label(self.top, text="Phone Number:", font=('TkDefaultFont', 10)).grid(row=11, column=2, sticky=tk.W,
                                                                                   padx=5,
                                                                                   pady=2)
        self.top.phone_entry = ttk.Entry(self.top)
        self.top.phone_entry.grid(row=11, column=3, padx=5, pady=2)

        ttk.Label(self.top, text="Postal Code:", font=('TkDefaultFont', 10)).grid(row=11, column=4, sticky=tk.W,
                                                                                   padx=5,
                                                                                   pady=2)
        self.top.postal_code_entry = ttk.Entry(self.top)
        self.top.postal_code_entry.grid(row=11, column=5, padx=5, pady=2)
        # Add Vendor button
        add_business_button = ttk.Button(self.top, text="Add Vendor", )
        add_business_button.grid(row=12, column=4, padx=5, pady=2)

        # Label for "Previous Vehicle PartOrder"
        previous_partorder_label = ttk.Label(self.top, text="Previous PartOrder:", font=('TkDefaultFont', 10))
        previous_partorder_label.grid(row=13, column=0, sticky=tk.W, padx=5, pady=2)
        self.top.previous_partorder_entry = ttk.Entry(self.top)
        self.top.previous_partorder_entry.grid(row=13, column=1, padx=5, pady=2)
        style = ttk.Style()
        style.configure("RedBold.TLabel", font=('TkDefaultFont', 10, 'bold'), foreground='red')
        previous_partorder_label.configure(style="RedBold.TLabel")
        get_previous_partorder_button = ttk.Button(self.top, text="Get", command=self.get_previous_part_order)
        get_previous_partorder_button.grid(row=13, column=2, padx=5, pady=2)
        # Treeview setup-------------------------------------------------------------------------------------------
        columns = ["Part Number", "Part Status", "Description", "Cost Part", "Quantity", "Purchase Order Number", "VIN",
                   "Vendor Name"]
        self.tree = ttk.Treeview(self.top, columns=columns, show="headings", selectmode="browse")

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)

        # Set column widths (adjust as needed)
        column_widths = [100, 100, 200, 80, 80, 150, 120, 120]  # Adjusted for the "Vendor Name" column
        for col, width in zip(columns, column_widths):
            self.tree.column(col, width=width, anchor=tk.CENTER)

        # Add treeview to the layout
        self.tree.grid(row=18, column=0, columnspan=7, pady=10)

        # # Add some sample data (replace this with your actual data)
        # sample_data = [
        #     ("123", "In Stock", "Sample Part 1", "$50.00", 5, "PO123", "ABC123", "Vendor A"),
        #     ("456", "Out of Stock", "Sample Part 2", "$30.00", 2, "PO456", "XYZ789", "Vendor B"),
        #     # Add more rows as needed
        # # ]
        #
        # for data in sample_data:
        #     self.tree.insert("", "end", values=data)


        # Entry widgets for Part Order section to Add Individual Parts
        ttk.Label(self.top, text="Part Number:", font=('TkDefaultFont', 10)).grid(row=15, column=0, sticky=tk.W, padx=5,
                                                                                  pady=2)
        self.top.part_number_entry = ttk.Entry(self.top)
        self.top.part_number_entry.grid(row=15, column=1, padx=5, pady=2)

        ttk.Label(self.top, text="Description:", font=('TkDefaultFont', 10)).grid(row=15, column=2, sticky=tk.W, padx=5,
                                                                                  pady=2)
        self.top.description_entry = ttk.Entry(self.top)
        self.top.description_entry.grid(row=15, column=3, padx=5, pady=2)

        ttk.Label(self.top, text="Cost Part:", font=('TkDefaultFont', 10)).grid(row=15, column=4, sticky=tk.W, padx=5,
                                                                                pady=2)
        self.top.cost_part_entry = ttk.Entry(self.top)
        self.top.cost_part_entry.grid(row=15, column=5, padx=5, pady=2)

        ttk.Label(self.top, text="Quantity:", font=('TkDefaultFont', 10)).grid(row=15, column=6, sticky=tk.W, padx=5,
                                                                               pady=2)
        self.top.quantity_entry = ttk.Entry(self.top)
        self.top.quantity_entry.grid(row=15, column=7, padx=5, pady=2)

        # Add a button for adding a new Part in treeview row
        add_row_button = ttk.Button(self.top, text="Add Part", command=self.add_part_order_row)
        add_row_button.grid(row=16, column=0, columnspan=8, pady=10)
        style = ttk.Style()
        style.configure("Bold.TButton", font=('TkDefaultFont', 9, 'bold'))
        add_row_button.configure(style="Bold.TButton")

        # Add a button for Completing PartOrder
        add_partorder_button = ttk.Button(self.top, text="Submit Part Order")
        add_partorder_button.grid(row=18, column=0, columnspan=8, pady=10)
        style = ttk.Style()
        style.configure("Green.TButton", foreground="green", font=('TkDefaultFont', 12, 'bold'))
        add_partorder_button.configure(style="Green.TButton")

    def add_part_order_row(self):
        # Retrieve values from the entry widgets
        part_number = self.top.part_number_entry.get()
        description = self.top.description_entry.get()
        cost_part = self.top.cost_part_entry.get()
        quantity = self.top.quantity_entry.get()

        # Set the "Part Status" to "Ordered"
        part_status = "Ordered"

        # Insert a new row into the Treeview
        self.tree.insert("", "end", values=(part_number, part_status, description, cost_part, quantity, "", "", ""))

        # Clear the entry widgets after inserting the row
        self.top.part_number_entry.delete(0, tk.END)
        self.top.description_entry.delete(0, tk.END)
        self.top.cost_part_entry.delete(0, tk.END)
        self.top.quantity_entry.delete(0, tk.END)


    def vendor_search_button_clicked(self): # Get list of Vendors
        # Retrieve the vendor name from the entry widget
        vendor_name = self.top.vendor_name_entryS.get()
        print(f"vendor name: {vendor_name}")

        self.controller = AddPartOrderController(self)
        # Call the execute_search_business method on the controller
        vendor_data = self.controller.vendor_search(vendor_name)
        # Clear existing rows in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert vendor data into the Treeview
        for vendor in vendor_data:
            self.tree.insert("", "end", values=(
                vendor.vendor_name,  # Use the correct attribute names
                vendor.phone_number,
                vendor.street,
                vendor.city,
                vendor.state,
                vendor.postal_code
            ))

        # Show the Toplevel window when the button is clicked
        self.top.geometry("+{}+{}".format(100, 100))

    def get_previous_part_order(self):
        vin = "036EG6XGHFJ822528"

        self.controller = AddPartOrderController(self)
        # Call the execute_search_business method on the controller
        self.controller.get_previousPO(vin)

        # Update the entry widget with the result
        self.top.previous_partorder_entry.delete(0, tk.END)  # Clear previous content
        self.top.previous_partorder_entry.insert(0, result)

# Testing the view
# root = tk.Tk()
# start_connection_pool()
# app = AddPartOrderView(parent=root)
# app.pack()
# root.mainloop()
