#When a user hits a reqest it always comes like a class object it has some properties 

request.method
# GET / POST check করার জন্য

request.GET
# URL query params er dict 

request.POST
# body data er dict

request.FILES
# uploaded files

request.user
# Logged in user

request.session
# Session data

request.headers
# Headers access

request.COOKIES
# Cookies

request.path
# Current URL path

request.META
# Request metadata / IP / headers

request.body
# Raw request body (JSON/API)

request.content_type
# Content type check