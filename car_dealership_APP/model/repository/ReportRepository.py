from model.domain.SellerHistoryReport import SellerHistoryReport
from model.domain.AvgTimeInvtReport import AvgTimeInvtReport
from model.domain.PricePerCondReport import PricePerCondReport
from model.domain.PartStatisticsReport import PartStatisticsReport
from model.domain.MonthlySalesReport import MonthlySalesSummaryReport, YearMonthDrilldownReport
from util import db

class SellerHistoryRepository:
    def get_seller_history(self):
        print('report_repository: get_seller_history')
        connection, cursor = db.get_connection(False)
        sql_query = '''
                    SELECT 
                        CASE
                            WHEN i.license_number IS NOT NULL THEN CONCAT(i.first_name, ' ', i.last_name)
                            WHEN b.tin IS NOT NULL THEN b.business_name
                        END AS seller_name,
                        COUNT(p.vin) AS total_vehicles_sold,
                        AVG(p.purchase_price) AS avg_purchase_price,
                        (po_pt.total_part_quantity / COUNT(p.vin)) AS avg_part_quantity,
                        (po_pt.total_cost_of_parts / COUNT(p.vin)) AS avg_cost_of_parts_per_vehicle
                    FROM Purchase AS p
                    LEFT JOIN Customer AS c ON p.customerID=c.customerID
                    LEFT JOIN Business AS b ON c.customerID=b.customerID
                    LEFT JOIN Individual AS i ON c.customerID=i.customerID
                    LEFT JOIN (
                        SELECT 
                            po.vin, 
                            SUM(pt.quantity) AS total_part_quantity,
                            SUM(pt.quantity * pt.cost_of_part) AS total_cost_of_parts
                        FROM PartsOrder AS po
                        INNER JOIN Part AS pt ON po.purchase_order_number=pt.purchase_order_number
                        GROUP BY po.vin
                    ) AS po_pt ON p.vin=po_pt.vin
                    GROUP BY seller_name, po_pt.total_part_quantity, po_pt.total_cost_of_parts
                    ORDER BY total_vehicles_sold DESC, avg_purchase_price ASC;
                    '''
        print(f'Query: {sql_query}')
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        seller_history_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                seller_history = SellerHistoryReport(row[0], row[1], row[2], row[3], row[4])
                seller_history_list.append(seller_history)
        else:
            print('seller_history_list returned empty result')
        db.close_connection(cursor, connection)
        return seller_history_list
    
class AverageTimeInInventoryRepository:
    def get_avg_time_invt(self):
        print('report_repository: get_avg_time_invt')
        connection, cursor = db.get_connection(False)
        sql_query = '''
                    SELECT 
                        v.type,
                        CASE
                            WHEN (COUNT(s.saleID) = 0 OR COUNT(s.saleID) IS NULL)THEN 'N/A'
                            ELSE
                                ROUND(
                                    AVG(
                                        CASE
                                            WHEN DATEDIFF(s.sale_date, p.purchase_date) = 0 THEN 1
                                            ELSE DATEDIFF(s.sale_date, p.purchase_date) + 1
                                        END
                                    ),
                                    2
                                )
                        END AS avg_time_inventory
                    FROM Vehicle v
                    LEFT JOIN Purchase p ON v.vin=p.vin
                    LEFT JOIN Sale s ON p.vin=s.vin
                    GROUP BY v.type;
                    '''
        print(f'Query: {sql_query}')
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        avg_time_invt_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                avg_time_invt = AvgTimeInvtReport(row[0], row[1])
                avg_time_invt_list.append(avg_time_invt)
        else:
            print('avg_time_invt_list returned empty result')
        db.close_connection(cursor, connection)
        return avg_time_invt_list
    
class PricePerConditionRepository:
    def get_price_per_cond(self):
        print('report_repository: get_price_per_cond')
        connection, cursor = db.get_connection(False)
        sql_query = '''
                    SELECT
                        vt.type AS vehicle_type,
                        COALESCE(AVG(
                            CASE
                                WHEN p.condition_at_purchase='Excellent' THEN p.purchase_price
                            END
                        ), 0) AS excellent,
                        COALESCE(AVG(
                            CASE
                                WHEN p.condition_at_purchase='Very Good' THEN p.purchase_price
                            END
                        ), 0) AS very_good,
                        COALESCE(AVG(
                            CASE
                                WHEN p.condition_at_purchase='Good' THEN p.purchase_price
                            END
                        ), 0) AS good,
                        COALESCE(AVG(
                            CASE
                                WHEN p.condition_at_purchase='Fair' THEN p.purchase_price
                            END
                        ), 0) AS fair
                    FROM Vehicle AS v
                    RIGHT JOIN VehicleType AS vt ON v.type=vt.type
                    LEFT JOIN Purchase AS p ON p.vin=v.vin
                    GROUP BY vt.type
                    '''
        print(f'Query: {sql_query}')
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        price_per_cond_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                price_per_cond = PricePerCondReport(row[0], row[1], row[2], row[3], row[4])
                price_per_cond_list.append(price_per_cond)
        else:
            print('price_per_cond_list returned empty result')
        db.close_connection(cursor, connection)
        return price_per_cond_list
    
class PartStatisticsRepository:
    def get_part_stats(self):
        print('report_repository: get_part_stats')
        connection, cursor = db.get_connection(False)
        sql_query = '''
                    SELECT
                        v.vendor_name,
                        SUM(pt.quantity) AS number_parts_supplied,
                        SUM(pt.quantity * pt.cost_of_part) AS total_amount_spent
                    FROM Vendor AS v
                    LEFT JOIN PartsOrder AS po ON v.vendor_name=po.vendor_name
                    LEFT JOIN Part pt ON pt.purchase_order_number=po.purchase_order_number
                    GROUP BY v.vendor_name
                    ORDER BY total_amount_spent DESC;
                    '''
        print(f'Query: {sql_query}')
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        part_stats_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                part_stats = PartStatisticsReport(row[0], row[1], row[2])
                part_stats_list.append(part_stats)
        else:
            print('part_stats_list returned empty result')
        db.close_connection(cursor, connection)
        return part_stats_list
    
class MonthlySalesRepository:
    def get_monthly_sale_summ(self):
        print('report_repository: get_monthly_sale_summ')
        connection, cursor = db.get_connection(False)
        sql_query = '''
                    SELECT
                        YEAR(s.sale_date) AS sale_year,
                        MONTH(s.sale_date) AS sale_month,
                        COUNT(s.saleID) AS vehicles_sold,
                        SUM(s.sale_price) AS total_sales_income,
                        SUM(s.sale_price - (p.purchase_price + (pt.quantity * pt.cost_of_part))) AS total_net_income
                    FROM Sale AS s
                    LEFT JOIN Purchase AS p ON s.vin=p.vin
                    LEFT JOIN Vehicle AS v ON v.vin=s.vin AND v.vin=p.vin
                    LEFT JOIN PartsOrder AS po ON v.vin=po.vin
                    LEFT JOIN Part AS pt ON pt.purchase_order_number=po.purchase_order_number
                    WHERE s.sale_price IS NOT NULL
                    GROUP BY sale_year, sale_month
                    ORDER BY sale_year DESC, sale_month DESC;
                    '''
        print(f'Query: {sql_query}')
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        monthly_sale_summ_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                monthly_sale_summ = MonthlySalesSummaryReport(row[0], row[1], row[2], row[3], row[4])
                monthly_sale_summ_list.append(monthly_sale_summ)
        else:
            print('monthly_sale_summ_list returned empty result')
        db.close_connection(cursor, connection)
        return monthly_sale_summ_list
    
    def get_year_month_drilldown(self, sale_year, sale_month):
        print('report_repository: get_month_year_drilldown')
        connection, cursor = db.get_connection(False)
        sql_query = f'''
                    SELECT
                        u.first_name,
                        u.last_name,
                        COUNT(s.saleID) AS vehicles_sold,
                        SUM(s.sale_price) AS total_sales
                    FROM Sale AS s
                    INNER JOIN User AS u ON u.userID=s.userID
                    WHERE YEAR(s.sale_date)='{sale_year}'
                    AND MONTH(s.sale_date)='{sale_month}'
                    GROUP BY u.first_name, u.last_name
                    ORDER BY vehicles_sold DESC, total_sales DESC;
                    '''
        print(f'Query: {sql_query}')
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        year_month_drilldown_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                year_month_drilldown = YearMonthDrilldownReport(row[0], row[1], row[2], row[3])
                year_month_drilldown_list.append(year_month_drilldown)
        else:
            print('year_month_drilldown_list returned empty result')
        db.close_connection(cursor, connection)
        return year_month_drilldown_list