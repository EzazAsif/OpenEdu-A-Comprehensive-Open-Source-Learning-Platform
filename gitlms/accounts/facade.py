# facade.py
from .strategies import RegularUserRegistration, AdminUserRegistration
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

class RegistrationFacade:
    def __init__(self):
        # Initialize strategies for regular users and admins
        self.regular_registration = RegularUserRegistration()
        self.admin_registration = AdminUserRegistration()

    def register(self, data, user_type="regular"):
        """
        A simplified interface for user registration.
        
        Parameters:
            data (dict): User data (email, passw, fname, lname)
            user_type (str): Type of user, can be "regular" or "admin"
            
        Returns:
            User object if registration is successful
        """
        if user_type == "admin":
            return self.admin_registration.register(data)
        return self.regular_registration.register(data)

# User = get_user_model()

class ProfileManager:
    @staticmethod
    def update_profile(user, data, files):
        try:
            # --- 1. Validate Data ---
            if not data.get('first_name') or not data.get('last_name'):
                raise ValidationError("First/Last name cannot be empty!")
            
            if data.get('new_password') and data['new_password'] != data.get('confirm_password'):
                raise ValidationError("Passwords don't match!")
            
            if data.get('new_password'):
                validate_password(data['new_password'])  # Django's built-in validator

            # --- 2. Update Database ---
            user.first_name = data.get('first_name', user.first_name)
            user.last_name = data.get('last_name', user.last_name)
            user.email = data.get('email', user.email)
            
            if 'profile_picture' in files:
                user.profile_picture = files['profile_picture']
            
            if data.get('new_password'):
                user.set_password(data['new_password'])
            
            user.save()

            send_mail(
                'Profile Updated',
                f'Hi {user.first_name}, your profile was updated!',
                'admin@example.com',
                [user.email],
                fail_silently=True,
            )

            return True
        except ValidationError as e:
            return False