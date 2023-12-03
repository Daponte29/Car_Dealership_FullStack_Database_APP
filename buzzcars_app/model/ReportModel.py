from model.repository.ReportRepository import SellerHistoryRepository, AverageTimeInInventoryRepository, PricePerConditionRepository, PartStatisticsRepository, MonthlySalesRepository

class ReportModel:
    def __init__(self):
        self.seller_history_repo = SellerHistoryRepository()
        self.avg_time_inv_repo = AverageTimeInInventoryRepository()
        self.price_per_cond_repo = PricePerConditionRepository()
        self.part_stats_repo = PartStatisticsRepository()
        self.monthly_sales_repo = MonthlySalesRepository()

    def get_seller_history(self):
        return self.seller_history_repo.get_seller_history()

    def get_avg_time_invt(self):
        return self.avg_time_inv_repo.get_avg_time_invt()

    def get_price_per_cond(self):
        return self.price_per_cond_repo.get_price_per_cond()

    def get_part_stats(self):
        return self.part_stats_repo.get_part_stats()

    def get_monthly_sale_summ(self):
        return self.monthly_sales_repo.get_monthly_sale_summ()

    def get_year_month_drilldown(self, sale_date, sale_month):
        return self.monthly_sales_repo.get_year_month_drilldown(sale_date, sale_month)