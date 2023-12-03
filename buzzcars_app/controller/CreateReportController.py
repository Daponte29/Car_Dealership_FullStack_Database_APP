from model.ReportModel import ReportModel
from util.SessionValues import SessionValues
from view.ReportWindowView import OPTIONS

class CreateReportController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_report_details(self, report_option):
        if report_option == OPTIONS[0]:
            print('seller history')
            seller_history_list = self.model.get_seller_history()
            self.view.create_seller_history(seller_history_list)
        elif report_option == OPTIONS[1]:
            print('Avg Time in Inv')
            avg_time_invt_list = self.model.get_avg_time_invt()
            self.view.create_avg_time_invt(avg_time_invt_list)
        elif report_option == OPTIONS[2]:
            print('price per condition')
            price_per_cond_list = self.model.get_price_per_cond()
            self.view.create_price_per_cond(price_per_cond_list)
        elif report_option == OPTIONS[3]:
            print('part stats')
            part_stats_list = self.model.get_part_stats()
            self.view.create_part_stats(part_stats_list)
        elif report_option == OPTIONS[4]:
            print('monthly sales')
            monthly_sale_summ_list = self.model.get_monthly_sale_summ()
            self.view.create_monthly_sale_summ(monthly_sale_summ_list)

    def get_year_month_drilldown_details(self, sale_year, sale_month):
        print('year-month sales detail')
        year_month_detail_list = self.model.get_year_month_drilldown(sale_year, sale_month)
        self.view.create_year_month_drilldown(year_month_detail_list, sale_year, sale_month)

    def show_reports_frame(self):
        self.view.report_frame.grid()

    def hide_reports_frame(self):
        self.view.report_frame.grid_remove()

    def refresh_view(self):
        authenticated_user = SessionValues.get_value("authenticated_user")
        if authenticated_user is None:
            self.hide_reports_frame()
        else:
            if authenticated_user.is_manager:
                self.show_reports_frame()
            else:
                self.hide_reports_frame()