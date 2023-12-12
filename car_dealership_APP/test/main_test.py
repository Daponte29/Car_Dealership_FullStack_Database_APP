from model.repository.CustomerRepository import CustomerRepository
from model.repository.SaleRepository import SaleRepository
from model.repository.VehicleRepository import *


def main():
    # print("Get all users")
    # users = get_all_users()
    # for user in users:
    #     print(f"userID: {user.userID}, first_name: {user.first_name}, password: {user.password}")
    #
    # print("Get user by first_name")
    # user = get_user_by_user_id(2)
    # print(f"userID: {user.userID}, first_name: {user.first_name}, password: {user.password}")

    # print("Vehicle repository")
    # vr = VehicleRepository()
    # vehicle_list = vr.get_all_vehicles()
    # for vehicle in vehicle_list:
    #     print(f"vin: {vehicle.vin}, model_year: {vehicle.model_year}")

    # print("Business repository")
    # cr = CustomerRepository()
    # business_customers = cr.get_all_business()
    # for business in business_customers:
    #     print(f"customerID: {business.customerID}, email: {business.email}, bname: {business.business_name}")

    "Rivendell"
    cr = CustomerRepository()
    customerID = cr.find_customer_by_name("Rivendell")

    sr = SaleRepository()
    sr.save(1200, '2023-10-12', 1, 'TEST_31581L000001', customerID)


if __name__ == '__main__':
    main()
