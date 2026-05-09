#define a url 
from django.urls import path, include
from app.views import views
app_name = "app_name"
urlpatterns = [
    path('home/', views.fun, name='home'),
    path('about/', views.Class.as_view(), name='about'),
    path('api/', include('app.urls')),
    path('name/<str:name>/', views.name_view),
]


#1.path fun
"""
to define a url we call path() in out list
#path takes 3 pers 
1. Url url route 
2. A function or class which dones some work for getting req at that url
  # for fun we simply pass fun name without ()
  #for class we add .as_view() which is as_view() class method 
3. a name , whith a name we can use this url in template or in other files(if we add app name we have to use it like 'app_name:url_name')
"""

#2.include fun
"""path fun can take 2 pers 1 is url and 2
is a other function include() include
function takes 1 per (a app level url file
) 
#অন্য app-এর urls.py file কে main project URL file-এর সাথে connect করে দেয়।
"""
#3.dynamic URL
"""
we can make url dynamic by defining like this <data_type:name> whenever a user hits this url this data(name) will go to our view fun as per and we can give out put based on given data
data_types can be = int, str, slug, uuid, path
"""