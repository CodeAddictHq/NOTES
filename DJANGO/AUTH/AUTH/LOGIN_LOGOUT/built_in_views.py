#In django.contrib.auth.views app there is some views built in for us, heres they are 
1.LoginView()
#they all does everything for us we just jave to make a folder for this views and make template called 'login.html' and we have to use form there and done
#Success url set if log in (settings.py)
LOGIN_REDIRECT_URL = 'route'

2.LogoutView(next_page="url name")
#Doesnt needs any template if this url hits session autpmetically clears , url name is mandetory for redirectiom

3.PasswordChangeView()
#same like LoginView everything is done by django we just need to define template in  'registration/password_change_form.html' file autometically calls PasswordChangeDoneView and finds password_change_done, if Doesnt remain set PasswordChangeDoneView   

4.PasswordChangeDoneView()
#autometically redirects in this 'password_change_done.html' after success of PasswordChangeView


#PASS RESET FLOW (SKIPPING FOR NOW )
"""
5.PasswordResetView()
6.PasswordResetDoneView()
7.PasswordResetConfirmView()
8.PasswordResetCompleteView()
"""