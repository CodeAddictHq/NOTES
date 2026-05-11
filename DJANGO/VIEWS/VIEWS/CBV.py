#defining a class based view 

from django.views import View

class ViewName(View):
  def get(self, request):
    #what to done with GET req
  def post(self, request):
    #what to done with POST req
  def put(self, request):
    #what to done with PUT req
  ...

#we can call a class method when a url hits and we can specify the work with what method to be done 