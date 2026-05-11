#To login and logout user we have some functions 

1.authenticate(request, users_uniq_properties=val)
#Returns user object if users_uniq_properties are valid else returns none 

2.login(user)
#Starts a session in users browsers 

3.logout(user)
#breaks a session 

#We also use some decoratores for a specific view to restrict user access

@login_required
#gives acces only logged in users