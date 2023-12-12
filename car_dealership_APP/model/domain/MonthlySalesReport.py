class MonthlySalesSummaryReport:
    def __init__(self, sale_year, sale_month, 
                 vehicles_sold, total_sales_income, 
                 total_net_income):
        self.sale_year = sale_year
        self.sale_month = sale_month
        self.vehicles_sold = vehicles_sold
        self.total_sales_income = total_sales_income
        self.total_net_income = total_net_income

class YearMonthDrilldownReport:
    def __init__(self, first_name, last_name, 
                 vehicles_sold, total_sales):
        self.first_name = first_name
        self.last_name = last_name
        self.vehicles_sold = vehicles_sold
        self.total_sales = total_sales