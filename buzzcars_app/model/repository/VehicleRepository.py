from model.domain.Vehicle import Vehicle
from model.domain.VehicleListItem import VehicleListItem
from util import db
from util.Constants import Constants


class VehicleRepository:

    def search_vehicles_count(self, search_string, vehicle_type, vehicle_manufacturer, model_year, fuel_type, color,
                              vin, for_purchase_only, pending_only):
        print(f"vehicle_repository: search_vehicles -- search_vehicles_count: {search_string}")
        connection, cursor = db.get_connection(True)
        sql_query = self._get_search_vehicle_count_sql(pending_only, for_purchase_only)

        # Apply search filters
        if search_string:
            search_string = search_string.lower()
            sql_query += f""" AND (LOWER(v.manufacturer) LIKE '%{search_string}%' 
                          OR LOWER(v.model_year) like '%{search_string}%'
                          OR LOWER(v.model_name) like '%{search_string}%'
                          OR LOWER(v.description) like '%{search_string}%')
            """
        if vehicle_type:
            sql_query += f" AND (v.type = '{vehicle_type}')"

        if vehicle_manufacturer:
            sql_query += f" AND (v.manufacturer = '{vehicle_manufacturer}')"

        if model_year:
            sql_query += f" AND (v.model_year = '{model_year}')"

        if fuel_type:
            sql_query += f" AND (v.fuel_type = '{fuel_type}')"

        if color:
            sql_query += f" AND (color_names like '%{color}%')"

        if vin:
            sql_query += f" AND (LOWER(v.vin) like '%{vin.lower()}%')"

        # Grouping and ordering
        sql_query += """            
                    GROUP BY
                    v.vin, v.model_name, v.model_year, v.fuel_type, v.mileage, v.description, v.manufacturer,
                    v.type
                    ORDER BY v.vin ASC )
                """
        sql_query += """
        select count(*)
        from pre_result
        """

        print(f"Query: {sql_query}")
        cursor.execute(sql_query)
        row = cursor.fetchone()
        if row:
            db.close_connection(cursor, connection)
            return row[0]
        else:
            print("search_vehicles_count returned empty result")
            db.close_connection(cursor, connection)
            return 0
        db.close_connection(cursor, connection)

    def get_all_vehicles(self):
        print("vehicle_repository: get_all_vehicles")
        connection, cursor = db.get_connection(False)
        sql_query = """
                    SELECT 
                        v.vin, 
                        v.model_name, 
                        v.model_year, 
                        v.fuel_type, 
                        v.mileage, 
                        v.description, 
                        v.manufacturer, 
                        v.type, 
                        ((p.purchase_price * 1.25) + COALESCE(SUM(PartCost.total_parts_cost * 1.1), 0)) AS sale_price, 
                        GROUP_CONCAT(vc.color_name SEPARATOR ', ') AS color_names
                    FROM Vehicle v 
                    LEFT JOIN Vehicle_Color vc ON v.vin = vc.vin
                    LEFT JOIN Purchase p ON v.vin = p.vin
                    LEFT JOIN (
                        SELECT
                            vin,
                            SUM(cost_of_part * quantity) AS total_parts_cost
                        FROM Part
                        GROUP BY vin
                    ) AS PartCost ON v.vin=PartCost.vin
                    GROUP BY v.vin, v.model_name, v.model_year, v.fuel_type, v.mileage, v.description, v.manufacturer, 
                             v.type
                    """

        print(f"Query: {sql_query}")
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        vehicle_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                vehicle = VehicleListItem(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                          row[9])
                vehicle_list.append(vehicle)
        else:
            print("get_all_vehicles returned empty result")
        db.close_connection(cursor, connection)
        return vehicle_list

    def search_vehicles(self, search_string, vehicle_type, vehicle_manufacturer, model_year, fuel_type, color, vin,
                        for_purchase_only, include_pending):
        print(f"vehicle_repository: search_vehicles -- search_string: {search_string}")
        connection, cursor = db.get_connection(False)
        sql_query = self._get_search_vehicle_sql(include_pending, for_purchase_only)

        # Apply search filters
        if search_string:
            search_string = search_string.lower()
            sql_query += f""" AND (LOWER(v.manufacturer) LIKE '%{search_string}%' 
                          OR LOWER(v.model_year) like '%{search_string}%'
                          OR LOWER(v.model_name) like '%{search_string}%'
                          OR LOWER(v.description) like '%{search_string}%')
            """
        if vehicle_type:
            sql_query += f" AND (v.type = '{vehicle_type}')"

        if vehicle_manufacturer:
            sql_query += f" AND (v.manufacturer = '{vehicle_manufacturer}')"

        if model_year:
            sql_query += f" AND (v.model_year = '{model_year}')"

        if fuel_type:
            sql_query += f" AND (v.fuel_type = '{fuel_type}')"

        if color:
            sql_query += f" AND (color_names like '%{color}%')"

        if vin:
            sql_query += f" AND (LOWER(v.vin) like '%{vin.lower()}%')"
        # Grouping and ordering
        sql_query += """            
                GROUP BY
                v.vin, v.model_name, v.model_year, v.fuel_type, v.mileage, v.description, v.manufacturer,
                v.type
                ORDER BY v.vin ASC
            """

        print(f"Query: {sql_query}")
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        vehicle_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                vehicle = VehicleListItem(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                          row[9])
                vehicle_list.append(vehicle)
        else:
            print("get_all_vehicles returned empty result")
        db.close_connection(cursor, connection)
        return vehicle_list

    def search_vehicles_with_sold_filter(self, search_string, vehicle_type, vehicle_manufacturer, model_year, fuel_type,
                                         color, vin, sold_filter):
        print(f"vehicle_repository: search_vehicles_with_sold_filter -- search_string: {search_string}")
        connection, cursor = db.get_connection(False)
        sql_query = self._get_search_vehicle_sql_with_sold_filter(sold_filter)

        # Apply search filters
        if search_string:
            search_string = search_string.lower()
            sql_query += f""" AND (LOWER(v.manufacturer) LIKE '%{search_string}%' 
                          OR LOWER(v.model_year) like '%{search_string}%'
                          OR LOWER(v.model_name) like '%{search_string}%'
                          OR LOWER(v.description) like '%{search_string}%')
            """
        if vehicle_type:
            sql_query += f" AND (v.type = '{vehicle_type}')"

        if vehicle_manufacturer:
            sql_query += f" AND (v.manufacturer = '{vehicle_manufacturer}')"

        if model_year:
            sql_query += f" AND (v.model_year = '{model_year}')"

        if fuel_type:
            sql_query += f" AND (v.fuel_type = '{fuel_type}')"

        if color:
            sql_query += f" AND (color_names like '%{color}%')"

        if vin:
            sql_query += f" AND (LOWER(v.vin) like '%{vin.lower()}%')"
        # Grouping and ordering
        sql_query += """            
                GROUP BY
                v.vin, v.model_name, v.model_year, v.fuel_type, v.mileage, v.description, v.manufacturer,
                v.type
                ORDER BY v.vin ASC
            """

        print(f"Query: {sql_query}")
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        vehicle_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                vehicle = VehicleListItem(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                          row[9])
                vehicle_list.append(vehicle)
        else:
            print("get_all_vehicles returned empty result")
        db.close_connection(cursor, connection)
        return vehicle_list

    def _get_search_vehicle_sql(self, include_pending, for_purchase_only):
        sql_query = ""
        if not include_pending:
            sql_query += """
            WITH pending_parts_vins as (
                SELECT DISTINCT po.VIN
                FROM `PartsOrder` po
                     LEFT JOIN `Part` p on po.purchase_order_number=p.purchase_order_number
                WHERE p.part_status != 'Installed' )

                """

        sql_query += f"""                        
                    SELECT 
                        v.vin, 
                        v.model_name, 
                        v.model_year, 
                        v.fuel_type, 
                        v.mileage, 
                        v.description, 
                        v.manufacturer, 
                        v.type, 
                        ((p.purchase_price * 1.25) + COALESCE(SUM(PartCost.total_parts_cost * 1.1), 0)) AS sale_price, 
                        GROUP_CONCAT(vc.color_name SEPARATOR ', ') AS color_names
                    FROM Vehicle v 
                    LEFT JOIN Vehicle_Color vc ON v.vin = vc.vin
                    LEFT JOIN Sale s ON v.vin = s.vin
                    LEFT JOIN Purchase p ON v.vin = p.vin
                    LEFT JOIN (
                        SELECT
                            vin,
                            SUM(cost_of_part * quantity) AS total_parts_cost
                        FROM Part
                        GROUP BY vin
                    ) AS PartCost ON v.vin=PartCost.vin
                    WHERE TRUE """
        if not include_pending:
            sql_query += "AND v.VIN NOT IN(SELECT VIN FROM pending_parts_vins) "
        if for_purchase_only:
            sql_query += " AND s.saleID IS NULL"
        return sql_query

    def _get_search_vehicle_sql_with_sold_filter(self, sold_filter):
        sql_query = f"""                        
                    SELECT 
                        v.vin, 
                        v.model_name, 
                        v.model_year, 
                        v.fuel_type, 
                        v.mileage, 
                        v.description, 
                        v.manufacturer, 
                        v.type, 
                        ((p.purchase_price * 1.25) + COALESCE(SUM(PartCost.total_parts_cost * 1.1), 0)) AS sale_price, 
                        GROUP_CONCAT(vc.color_name SEPARATOR ', ') AS color_names
                    FROM Vehicle v 
                    LEFT JOIN Vehicle_Color vc ON v.vin = vc.vin
                    LEFT JOIN Sale s ON v.vin = s.vin
                    LEFT JOIN Purchase p ON v.vin = p.vin
                    LEFT JOIN (
                        SELECT
                            vin,
                            SUM(cost_of_part * quantity) AS total_parts_cost
                        FROM Part
                        GROUP BY vin
                    ) AS PartCost ON v.vin=PartCost.vin
                    WHERE TRUE """
        if sold_filter == Constants.SOLD:
            sql_query += " AND s.saleID IS NOT NULL"
        elif sold_filter == Constants.UN_SOLD:
            sql_query += " AND s.saleID IS NULL"

        return sql_query

    def _get_search_vehicle_count_sql(self, pending_only, for_purchase_only):
        sql_query = """
        WITH pending_parts_vins as (
            SELECT DISTINCT po.VIN
            FROM `PartsOrder` po
                 LEFT JOIN `Part` p on po.purchase_order_number=p.purchase_order_number
            WHERE p.part_status != 'Installed' ),
        pre_result as (
                    SELECT 
                        v.vin, 
                        v.model_name, 
                        v.model_year, 
                        v.fuel_type, 
                        v.mileage, 
                        v.description, 
                        v.manufacturer, 
                        v.type, 
                        ((p.purchase_price * 1.25) + COALESCE(SUM(PartCost.total_parts_cost * 1.1), 0)) AS sale_price, 
                        GROUP_CONCAT(vc.color_name SEPARATOR ', ') AS color_names
                    FROM Vehicle v 
                    LEFT JOIN Vehicle_Color vc ON v.vin = vc.vin
                    LEFT JOIN Sale s ON v.vin = s.vin
                    LEFT JOIN Purchase p ON v.vin = p.vin
                    LEFT JOIN (
                        SELECT
                            vin,
                            SUM(cost_of_part * quantity) AS total_parts_cost
                        FROM Part
                        GROUP BY vin
                    ) AS PartCost ON v.vin=PartCost.vin
                    WHERE TRUE 
            """
        if pending_only:
            sql_query += "AND v.VIN IN(SELECT VIN FROM pending_parts_vins) "
        else:
            sql_query += "AND v.VIN NOT IN(SELECT VIN FROM pending_parts_vins) "

        if for_purchase_only:
            sql_query += " AND s.saleID IS NULL"

        return sql_query

    def get_all_vehicle_types(self):
        print(f"vehicle_repository: get_all_vehicle_types")

        connection, cursor = db.get_connection(False)
        sql_query = "SELECT type FROM VehicleType"
        print(f"Query: {sql_query}")
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        vehicle_type_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                vehicle_type_list.append(row[0])
        else:
            print("get_all_vehicles_types returned empty result")
        db.close_connection(cursor, connection)
        return vehicle_type_list

    def get_all_vehicle_manufacturers(self):
        print(f"vehicle_repository: get_all_vehicle_manufacturers")

        connection, cursor = db.get_connection(False)
        sql_query = "SELECT manufacturer FROM VehicleManufacturer"
        print(f"Query: {sql_query}")
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        vehicle_manufacturer_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                vehicle_manufacturer_list.append(row[0])
        else:
            print("get_all_vehicle_manufacturers returned empty result")
        db.close_connection(cursor, connection)
        return vehicle_manufacturer_list

    def get_all_model_years(self):
        print(f"vehicle_repository: get_all_model_years")

        connection, cursor = db.get_connection(False)
        sql_query = "SELECT DISTINCT model_year FROM Vehicle order by model_year"
        print(f"Query: {sql_query}")
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        model_year_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                model_year_list.append(row[0])
        else:
            print("get_all_model_years returned empty result")
        db.close_connection(cursor, connection)
        return model_year_list

    def get_all_vehicle_fuel_types(self):
        print(f"vehicle_repository: get_all_fuel_types")

        connection, cursor = db.get_connection(False)
        sql_query = "SELECT DISTINCT fuel_type FROM Vehicle"
        print(f"Query: {sql_query}")
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        fuel_type_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                fuel_type_list.append(row[0])
        else:
            print("get_all_fuel_types returned empty result")
        db.close_connection(cursor, connection)
        return fuel_type_list

    def get_all_vehicle_colors(self):
        print(f"vehicle_repository: get_all_vehicle_colors")

        connection, cursor = db.get_connection(False)
        sql_query = "SELECT DISTINCT color_name FROM Vehicle_Color"
        print(f"Query: {sql_query}")
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        fuel_type_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                fuel_type_list.append(row[0])
        else:
            print("get_all_vehicle_colors returned empty result")
        db.close_connection(cursor, connection)
        return fuel_type_list

    def get_all_colors(self):
        print(f"vehicle_repository: get_all_colors")

        connection, cursor = db.get_connection(False)
        sql_query = "SELECT DISTINCT color_name FROM Color"
        print(f"Query: {sql_query}")
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        fuel_type_list = []
        if cursor.rowcount > 0:
            for row in result_set:
                fuel_type_list.append(row[0])
        else:
            print("get_all_colors returned empty result")
        db.close_connection(cursor, connection)
        return fuel_type_list

    def get_vehicle_details(self, vin):
        print(f"vehicle_repository: get_vehicle_details -- VIN: {vin}")
        connection, cursor = db.get_connection(False)
        sql_query = f"""
                    SELECT 
                        v.vin, 
                        v.model_name, 
                        v.model_year, 
                        v.fuel_type, 
                        v.mileage, 
                        v.description, 
                        v.manufacturer, 
                        v.type, 
                        ((p.purchase_price * 1.25) + COALESCE(SUM(PartCost.total_parts_cost * 1.1), 0)) AS sale_price, 
                        GROUP_CONCAT(vc.color_name SEPARATOR ', ') AS color_names
                    FROM Vehicle v 
                    LEFT JOIN Vehicle_Color vc ON v.vin = vc.vin
                    LEFT JOIN Purchase p ON v.vin = p.vin
                    LEFT JOIN (
                        SELECT
                            vin,
                            SUM(cost_of_part * quantity) AS total_parts_cost
                        FROM Part
                        GROUP BY vin
                    ) AS PartCost ON v.vin=PartCost.vin
                    WHERE v.vin = '{vin}'
                    GROUP BY
                        v.vin, v.model_name, v.model_year, v.fuel_type, v.mileage, v.description, v.manufacturer,
                        v.type
                """
        print(f"Query: {sql_query}")
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        vehicle_details = None
        if cursor.rowcount > 0:
            row = result_set[0]  # Assuming VIN is unique, so there should be only one row
            vehicle_details = {
                'vin': row[0],
                'model_name': row[1],
                'model_year': row[2],
                'fuel_type': row[3],
                'mileage': row[4],
                'description': row[5],
                'manufacturer': row[6],
                'type': row[7],
                'sale_price': row[8],
                'color_names': row[9],
            }
            # vin_get_sales_order_form = row[0] #Test for SalesOrderForm autopopulate VIN
            # print(f"Here vin!: {vin_get_sales_order_form}")
        else:
            print(f"No details found for VIN: {vin}")
        db.close_connection(cursor, connection)
        return vehicle_details
    #InventoryClerkVehicleDetailView
    def get_inventoryclerk_vehicle_details(self, vin):
        print(f"vehicle_repository: get_inventoryclerk_vehicle_details -- VIN: {vin}")
        connection, cursor = db.get_connection(False)
        sql_query = f"""
                    SELECT Purchase.purchase_date, Purchase.condition_at_purchase,
                           Purchase.purchase_price,
                           Vehicle.vin, Vehicle.model_name,
                           Vehicle.model_year, Vehicle.fuel_type, Vehicle.mileage, Vehicle.description,
                           Vehicle.manufacturer, Vehicle.type
                    FROM Purchase
                    JOIN Vehicle ON Purchase.vin = Vehicle.vin
                    WHERE Vehicle.vin = '{vin}'
                """
        print(f"Query: {sql_query}")
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        details = None
        if cursor.rowcount > 0:
            row = result_set[0]  # Assuming VIN is unique, so there should be only one row
            details = {
                'purchase_date': row[0],
                'condition_at_purchase': row[1],
                'purchase_price': row[2],
                'vin': row[3],
                'model_name': row[4],
                'model_year': row[5],
                'fuel_type': row[6],
                'mileage': row[7],
                'description': row[8],
                'manufacturer': row[9],
                'type': row[10],
            }
        else:
            print(f"No details found for VIN: {vin}")
        db.close_connection(cursor, connection)
        return details


    #Get Part Details
    def get_part_details(self, vin):
        print(f"vehicle_repository: get_part_details -- VIN: {vin}")
        connection, cursor = db.get_connection(False)
        sql_query = f"""
                    SELECT 
                       p.part_number,
                       p.description,
                       p.part_status,
                       p.cost_of_part,
                       p.quantity,
                       (p.cost_of_part * p.quantity) AS total_cost_for_part,
                       po.vendor_name,
                       po.purchase_order_number 
                    FROM Part p
                    LEFT JOIN PartsOrder po ON p.purchase_order_number=po.purchase_order_number
                    WHERE po.vin = '{vin}';
                """
        print(f"Query: {sql_query}")
        cursor.execute(sql_query)
        result_set = cursor.fetchall()

        part_details = []
        if cursor.rowcount > 0:
            for row in result_set:
                part_info = {
                    'part_number': row[0],
                    'description': row[1],
                    'part_status': row[2],
                    'cost_of_part': row[3],
                    'quantity': row[4],
                    'total_cost_for_part': row[5],
                    'vendor_name': row[6],
                    'purchase_order_number': row[7],
                }
                part_details.append(part_info)
        else:
            print(f"No part details found for VIN: {vin}")

        db.close_connection(cursor, connection)
        return part_details