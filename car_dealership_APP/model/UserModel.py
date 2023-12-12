from model.repository.UserRepository import UserRepository
from util.SessionValues import SessionValues


class UserModel:
    def __init__(self):
        self.repository = UserRepository()

    def validate_user_credentials(self, username, password):
        authenticated_user = self.repository.get_user_by_username_with_role_data(username)
        if authenticated_user:
            if authenticated_user.password == password:
                SessionValues.add_value("authenticated_user", authenticated_user)
                return True

        SessionValues.remove_value("authenticated_user")
        return False

    def logout(self):
        SessionValues.remove_value("authenticated_user")

    def get_all_users(self):
        return self.repository.get_all_users()
