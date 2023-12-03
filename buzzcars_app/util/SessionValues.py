from controller.UserLoginController import UserLoginController
from view.LoginView import LoginView


class SessionValues(object):
    session_dict = {}
    user_login_controller = None

    @classmethod
    def add_value(cls, key, value):
        cls.session_dict[key] = value

    @classmethod
    def get_value(cls, key):
        if key in cls.session_dict.keys():
            return cls.session_dict[key]
        else:
            return None

    @classmethod
    def remove_value(cls, key):
        if key in cls.session_dict.keys():
            del cls.session_dict[key]

    @classmethod
    def add_login_component(cls, parent, user_model, search_vehicle_controller, create_report_controller):
        login_view = LoginView(parent)
        cls.user_login_controller = UserLoginController(user_model, login_view, search_vehicle_controller,
                                                        create_report_controller)
        login_view.set_controller(cls.user_login_controller)

    @classmethod
    def get_login_component(cls):
        return cls.user_login_controller
