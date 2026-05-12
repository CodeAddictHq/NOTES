#we can also use users data in template heres how

1.{{ user }}
#accesses the user as dict we can access other vals with dot .

2.{{ user.property_name }}
#accesses users property like username, etc..

3.{{ user.is_authenticated }}
#Cheks if user logged in 