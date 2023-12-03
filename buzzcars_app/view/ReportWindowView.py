import tkinter as tk
from tkinter import ttk

OPTIONS = [
    'Seller History',
    'Average Time in Inventory',
    'Price Per Condition',
    'Part Statistics',
    'Monthly Sales'            
]

class ReportFrameView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None

        self.report_frame = tk.LabelFrame(parent, text='Reports')
        self.report_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.report_window = ttk.Label(self.report_frame, text='Report Options:', anchor='w')
        self.report_window.grid(row=0, column=0)

        self.chosen_option = tk.StringVar(self.report_frame)
        self.report_options = ttk.OptionMenu(self.report_frame, self.chosen_option, OPTIONS[0], *OPTIONS)
        self.report_options.grid(row=0, column=1, sticky=tk.NSEW)

        self.create_report_button = ttk.Button(self.report_frame, text='Create Report', command=self.get_report_data)
        self.create_report_button.grid(row=0, column=2)

    def set_controller(self, controller):
        self.controller = controller

    def get_report_data(self):
        self.chosen_report = self.chosen_option.get()
        self.controller.get_report_details(self.chosen_option.get())

    def create_seller_history(self, seller_list):
        top = tk.Toplevel(self)
        top.geometry('1000x750')
        top.title('Seller History Report')

        table = ttk.Treeview(top, column=('seller_name', 'total_vehicles_sold', 
                                          'avg_purchase_price', 'avg_part_quantity', 
                                          'avg_cost_of_parts_per_vehicle'),
                                            show='headings')
        table.heading('#1', text='Seller Name', anchor=tk.CENTER)
        table.column('#1', minwidth=0, width=200, stretch=tk.YES)
        table.heading('#2', text='Total Vehicles Sold', anchor=tk.CENTER)
        table.column('#2', minwidth=0, width=200, stretch=tk.NO)
        table.heading('#3', text='Average Vehicle Cost', anchor=tk.CENTER)
        table.column('#3', minwidth=0, width=200, stretch=tk.NO)
        table.heading('#4', text='Average Parts Per Vehicle', anchor=tk.CENTER)
        table.column('#4', minwidth=0, width=200, stretch=tk.NO)
        table.heading('#5', text='Average Part Cost Per Vehicle', anchor=tk.CENTER)
        table.column('#5', minwidth=0, width=200, stretch=tk.NO)

        table.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(top, orient=tk.VERTICAL, command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=0, columnspan=4, sticky='ne')

        top.grid_rowconfigure(0, weight=1)

        for row in table.get_children():
            table.delete(row)
        
        for s in seller_list:
            avg_cost = s.avg_cost_of_parts_per_vehicle
            avg_quantity = s.avg_part_quantity
            if (avg_cost != None and avg_cost >= 500) or (avg_quantity != None and avg_quantity >= 5):
                table.insert('', tk.END, values=(s.seller_name, s.total_vehicles_sold, 
                                                 s.avg_purchase_price, s.avg_part_quantity, 
                                                 s.avg_cost_of_parts_per_vehicle), tags=('red_highlight', ))
            else:
                table.insert('', tk.END, values=(s.seller_name, s.total_vehicles_sold, 
                                                s.avg_purchase_price, s.avg_part_quantity, 
                                                s.avg_cost_of_parts_per_vehicle))
        
        table.tag_configure('red_highlight', background='red')
            
            
    def create_avg_time_invt(self, avg_time_invt_list):
        top = tk.Toplevel(self)
        top.geometry('350x175')
        top.title('Average Time in Inventory')

        table = ttk.Treeview(top, column=('type', 'avg_time_inventory'), show='headings')
        table.heading('#1', text='Vehicle Type', anchor=tk.CENTER)
        table.column('#1', minwidth=0, width=150, stretch=tk.NO)
        table.heading('#2', text='Average Time In Inventory', anchor=tk.CENTER)
        table.column('#2', minwidth=0, width=200, stretch=tk.NO)

        table.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(top, orient=tk.VERTICAL, command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=0, columnspan=4, sticky='ne')

        for row in table.get_children():
            table.delete(row)

        for a in avg_time_invt_list:
            table.insert('', tk.END, values=(a.type, a.avg_time_inventory))
        
    def create_price_per_cond(self, price_per_cond_list):
        top = tk.Toplevel(self)
        top.geometry('950x175')
        top.title('Price Per Condition')

        table = ttk.Treeview(top, column=('vehicle_type', 'excellent', 'very_good', 'good', 'fair'), show='headings')
        table.heading('#1', text='Vehicle Type', anchor=tk.CENTER)
        table.column('#1', minwidth=0, width=150, stretch=tk.NO)
        table.heading('#2', text='Excellent Condition', anchor=tk.CENTER)
        table.column('#2', minwidth=0, width=200, stretch=tk.NO)
        table.heading('#3', text='Very Good Condition', anchor=tk.CENTER)
        table.column('#3', minwidth=0, width=200, stretch=tk.NO)
        table.heading('#4', text='Good Condition', anchor=tk.CENTER)
        table.column('#4', minwidth=0, width=200, stretch=tk.NO)
        table.heading('#5', text='Fair Condition', anchor=tk.CENTER)
        table.column('#5', minwidth=0, width=200, stretch=tk.NO)

        table.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(top, orient=tk.VERTICAL, command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=0, columnspan=4, sticky='ne')

        for row in table.get_children():
            table.delete(row)

        for p in price_per_cond_list:
            table.insert('', tk.END, values=(p.vehicle_type, p.excellent, p.very_good, p.good, p.fair))

    def create_part_stats(self, part_stats_list):
        top = tk.Toplevel(self)
        top.geometry('550x400')
        top.title('Part Statistics')

        table = ttk.Treeview(top, column=('vendor_name', 'number_parts_supplied', 'total_amount_spent'), show='headings')
        table.heading('#1', text='Vendor Name', anchor=tk.CENTER)
        table.column('#1', minwidth=0, width=150, stretch=tk.NO)
        table.heading('#2', text='Number of Parts Supplied', anchor=tk.CENTER)
        table.column('#2', minwidth=0, width=200, stretch=tk.NO)
        table.heading('#3', text='Total Amount Spent', anchor=tk.CENTER)
        table.column('#3', minwidth=0, width=200, stretch=tk.NO)

        table.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(top, orient=tk.VERTICAL, command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=0, columnspan=4, sticky='ne')

        top.grid_rowconfigure(0, weight=1)

        for row in table.get_children():
            table.delete(row)

        for v in part_stats_list:
            table.insert('', tk.END, values=(v.name, v.number_parts_supplied, v.total_amount_spent))


    def create_monthly_sale_summ(self, monthly_sale_summ_list):
        top = tk.Toplevel(self)
        top.geometry('850x275')
        top.title('Monthly Sales Summary')

        table = ttk.Treeview(top, column=('sale_year', 'sale_month', 'vehicles_sold', 'total_sales_income', 'total_net_income'), show='headings')
        table.heading('#1', text='Sale Year', anchor=tk.CENTER)
        table.column('#1', minwidth=0, width=150, stretch=tk.NO)
        table.heading('#2', text='Sale Month', anchor=tk.CENTER)
        table.column('#2', minwidth=0, width=150, stretch=tk.NO)
        table.heading('#3', text='Vehicles Sold', anchor=tk.CENTER)
        table.column('#3', minwidth=0, width=150, stretch=tk.NO)
        table.heading('#4', text='Total Sales Income', anchor=tk.CENTER)
        table.column('#4', minwidth=0, width=200, stretch=tk.NO)
        table.heading('#5', text='Total Net Income', anchor=tk.CENTER)
        table.column('#5', minwidth=0, width=200, stretch=tk.NO)

        table.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(top, orient=tk.VERTICAL, command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=0, columnspan=4, sticky='ne')

        top.grid_rowconfigure(0, weight=1)

        for row in table.get_children():
            table.delete(row)

        for ym in monthly_sale_summ_list:
            table.insert('', tk.END, values=(ym.sale_year, ym.sale_month, ym.vehicles_sold, ym.total_sales_income, ym.total_net_income))

        def on_row_click(event):
            item = table.item(table.focus())
            values = item['values']
            sale_year = values[0]
            sale_month = values[1]

            self.controller.get_year_month_drilldown_details(sale_year, sale_month)

        table.bind('<ButtonRelease-1>', on_row_click)
    
    def create_year_month_drilldown(self, year_month_detail_list, sale_year, sale_month):
        top = tk.Toplevel(self)
        top.geometry('750x300')
        top.title(f'Year ({sale_year}) - Month ({sale_month}) Drilldown')

        table = ttk.Treeview(top, column=('first_name', 'last_name', 'vehicles_sold', 'total_sales'), show='headings')
        table.heading('#1', text='First Name', anchor=tk.CENTER)
        table.column('#1', minwidth=0, width=150, stretch=tk.NO)
        table.heading('#2', text='Last Name', anchor=tk.CENTER)
        table.column('#2', minwidth=0, width=150, stretch=tk.NO)
        table.heading('#3', text='Number of Vehicles Sold', anchor=tk.CENTER)
        table.column('#3', minwidth=0, width=250, stretch=tk.NO)
        table.heading('#4', text='Total Sales', anchor=tk.CENTER)
        table.column('#4', minwidth=0, width=200, stretch=tk.NO)

        table.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(top, orient=tk.VERTICAL, command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=0, columnspan=4, sticky='ne')

        top.grid_rowconfigure(0, weight=1)

        for row in table.get_children():
            table.delete(row)

        for sp in year_month_detail_list:
            table.insert('', tk.END, values=(sp.first_name, sp.last_name, sp.vehicles_sold, sp.total_sales))
