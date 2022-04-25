from JSONParser import JSONParser
from Static import USER_OBJECT
from auth import Validator


class Auth():
    def __init__(self):
        self.parser = JSONParser()

    def user_exists(self):
        if self.parser.read_json(USER_OBJECT) is None:
            return False
        return True

    def register_user(self, data):
        err = {}

        # check input
        email_result = Validator.validate_email(data['email'])
        if email_result is not None:
            err['email'] = email_result

        username_result = Validator.validate_username(data['name'])
        if username_result is not None:
            err['name'] = username_result

        password_result = Validator.validate_password(data['passwd'])
        if password_result is not None:
            err['passwd'] = password_result

        re_password_result = Validator.validate_confirm_password(data['passwd'], data['re_passwd'])
        if re_password_result is not None:
            err['re_passwd'] = re_password_result

        # if error occurred (err is not empty) return error dict
        if bool(err) is False:
            return err

        # save user in config
        user = {'email': data['email'],
                'name': data['name'],
                'passwd': data['passwd']}

        self.parser.update_json(USER_OBJECT, user)

        return err
