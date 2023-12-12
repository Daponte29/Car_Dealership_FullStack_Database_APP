# Controller Imports
from controller.SearchVehicleController import SearchVehicleController
from controller.CreateReportController import CreateReportController
from controller.UserLoginController import UserLoginController
from controller.SalesOrderFormController import SalesOrderFormController

# Model Imports
from model.UserModel import UserModel
from model.VehicleModel import VehicleModel
from model.ReportModel import ReportModel
from model.CustomerModel import CustomerModel

# View Imports
from view.SearchVehicleView import SearchVehicleView
from view.ReportWindowView import ReportFrameView
from view.LoginView import LoginView
from view.SalesOrderForm import SalesOrderForm
from view.VehicleDetailView import VehicleDetailView
from view.SearchVehicleView import SearchVehicleView

# Python Library Imports
import tkinter as tk
from tkinter import ttk

# Util Imports
from util.db import start_connection_pool
from util.SessionValues import SessionValues

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        print("Starting the app.....")
        self.title("Buzzcars")
        start_connection_pool()

        authenticated_user = SessionValues.get_value("authenticated_user")

        # Search vehicle View
        vehicle_search_frame = tk.LabelFrame(self, text='Vehicle Search')
        vehicle_search_frame.grid(row=0, column=0, sticky='nsew')




        vehicle_model = VehicleModel()
        search_vehicle_view = SearchVehicleView(vehicle_search_frame)

        search_vehicle_controller = SearchVehicleController(vehicle_model, search_vehicle_view)
        search_vehicle_view.set_controller(search_vehicle_controller)




        # Report view
        # if authenticated_user:
        # report_frame = tk.LabelFrame(self, text='Reports')
        # report_frame.grid(row=1, column=0, sticky=tk.W)

        report_model = ReportModel()
        create_report_view = ReportFrameView(self)
        create_report_view.grid(row=1, column=0, sticky='s')

        create_report_controller = CreateReportController(report_model, create_report_view)
        create_report_view.set_controller(create_report_controller)
        create_report_controller.hide_reports_frame()
        # else:
            # do nothing / do not render the report label frame
            # pass

        user_model = UserModel()
        SessionValues.add_login_component(self, user_model, search_vehicle_controller, create_report_controller)
        user_login_controller = SessionValues.get_login_component()
        user_login_controller.hide_view()

if __name__ == '__main__':
    print("Starting app....")
    app = App()
    app.mainloop()
