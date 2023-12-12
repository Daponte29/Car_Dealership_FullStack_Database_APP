class UserLoginController:
    def __init__(self, model, view, search_vehicle_controller, create_report_controller):
        self.model = model
        self.view = view
        self.search_vehicle_controller = search_vehicle_controller
        self.create_report_controller = create_report_controller

    def validate_credentials(self, username, password):
        print(f"UserLoginController.validate_credentials....username:{username}")
        is_valid_user = self.model.validate_user_credentials(username, password)
        if is_valid_user:
            self.view.show_success("Valid user.")
        else:
            self.view.show_error("Invalid user, try again.")
        self.search_vehicle_controller.refresh_session()
        self.create_report_controller.refresh_view()

    def show_view(self):
        self.view.top.deiconify()

    def hide_view(self):
        self.view.top.withdraw()

    def logout(self):
        self.model.logout()
        self.search_vehicle_controller.refresh_session()
        self.create_report_controller.refresh_view()
