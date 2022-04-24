import re


def validate_email(email):
    """
    Method checks if email is valid.

    :param email: Email given in the registration form
    :type email: str
    :return: None if email is valid or error message
    :rtype: None/str
    """

    # email is empty
    if email is None or len(email) == 0:
        return 'Email address is empty'

    # email too long
    if len(email) > 60:
        return 'Email address must be up to 60 characters long'

    # email structure is invalid
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        return 'Email address is invalid'

    return None

def validate_username(username):
    """
    Method checks if username is valid.

    :param username: Username given in the registration form
    :type username: str
    :return: None if username is valid or error message
    :rtype: None/str
    """

    # username is empty
    if username is None or len(username) == 0:
        return 'Username is empty'

    # username too short
    if len(username) < 3:
        return 'Username must be at least 3 characters long'

    # username too long
    if len(username) > 30:
        return 'Username can be up to 30 characters long'

    # username contains whitespaces
    if re.search("\s", username) is not None:
        return 'Username must not contain whitespaces'

    # username contains special characters
    if username.isalnum() is False:
        return 'Username must not contain any non alphanumeric characters'

    return None


def validate_password(password):
    """
    Method checks if password is valid.

    :param password: Password given in the registration form
    :type password: str
    :return: None if password is valid or error message
    :rtype: None/str
    """

    # password is empty
    if password is None or len(password) == 0:
        return 'Password is empty'

    # password is too short
    if len(password) < 8:
        return 'Password must be at least 8 characters long'

    # password is too long
    if len(password) > 40:
        return 'Password can be up to 40 characters long'

    specials = ['$','@','!','%']
    # password contains letters, digits and special characters
    if not any(char.isdigit() for char in password):
        return 'Password must contain at least one digit'

    if not any(char.isupper() for char in password):
        return 'Password must contain at least one uppercase letter'

    if not any(char.islower() for char in password):
        return 'Password must contain at least one lowercase letter'

    if not any(char in specials for char in password):
        return 'Password must contain at least one of following characters: ' + (", ".join(specials))

    return None


def validate_confirm_password(password, re_password):
    """
    Functions checks if password is properly confirmed
    It means it checks if user typed this same password twice

    :param password: Basic password
    :type password: str
    :param re_password: Password confirmation
    :type re_password: str
    :return: None/str
    """

    # password and re_password matches
    if password != re_password:
        return 'Passwords do not match'

    return None
