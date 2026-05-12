# We can use built-in forms to do common authentication in Django (Python web framework)

1. AuthenticationForm()
# This is Django auth form used for. It has 2 fields. it internally cheks if user is valid and authenticated
Fields:
- username
- password
#if user remains valid we can get user by 
form.get_user()

2. UserCreationForm()
# This is used for signup (create user)
Fields:
- username
- password1
- password2


3. PasswordChangeForm(user, ..)
# Used to change password (when user is logged in)

Fields:
- old_password
- new_password1
- new_password2


4. PasswordResetForm(user, ..)
# Used for forgot password (email based reset)

Fields:
- email


5. SetPasswordForm(user, ..)
# Used to set new password after reset link

Fields:
- new_password1
- new_password2


# Core Summary

AuthenticationForm   → login
UserCreationForm     → signup
PasswordChangeForm    → change password
PasswordResetForm     → forgot password
SetPasswordForm      → reset password final step