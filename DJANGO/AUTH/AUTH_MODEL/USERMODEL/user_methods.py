#There is some usefull methods wuth user model (Thats the benifit)

1.user.set_password("str")
#sets new users pass

2.user.check_password("str")
#returns True if pass is correct 

3.user.has_perm('app_name.permission_name')
#Returns True if user has permission 

4.user.create_user()
#used to create user with normal create pass doesnt remain hashed

5.user.create_superuser()
#used to create superuser with normal create pass doesnt remain hashed
