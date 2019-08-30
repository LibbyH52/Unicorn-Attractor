from django.contrib.auth.models import User

#Created with help of Code Institute video lectures

class EmailAuth:
    """
    Authenticate a user by an exact match
    on their email and password
    """

    def authenticate(self, username=None, password=None):
        """
        Returns an instance of User object using that email
        address and verifies the password.
        """
        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Used by the Django authentication system to
        retrieve a User object.
        """
        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
