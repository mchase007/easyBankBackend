from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

# Get the user model for the current project
UserModel = get_user_model()

# Define a custom authentication backend that allows users to authenticate with either their email or username
class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Try to get the user by their email
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            try:
                # If that fails, try to get the user by their username
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                # If neither email nor username match, return None to indicate authentication failure
                return None
        # Check the password and return the user if it is correct
        if user.check_password(password):
            return user
