#Djangos User model is the built-in authentication systems main model, Which stores user related every data

#This is defined in ...here by django 
from django.contrib.auth.models import User

#Some fields User model have ..
1.username
#used for store username this is a uniq field 
2.password
#this field stores pass as hashed password

3.email
#Used to stpre email, validates email before save

4.first_name
#used to stpre first name 

5.last_name
#...

6.is_active 
#Saves bool val if user remains active returns True

7.is_staff
#if remains True grts admin panel access

8.is_superuser 
#if remains True gets full admin power

9.date_joined
#Returns joine date

10.last_login
#...
