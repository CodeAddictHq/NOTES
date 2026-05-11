#Django Shortcut Functions (views)

1. render(request, '.html', {'data':'12'})
"""
It takes 2 required arguments:
1st: request (HttpRequest object)
2nd: template name (HTML file from templates folder)
It also takes an optional 3rd argument:
context (dict) → data passed to template
It returns rendered HTML as HttpResponse
"""



2.redirect(to, *args, **kwargs)
"""
Used to redirect user to another URL.
Can accept:
URL string
view name
model instance (if get_absolute_url is defined)
Returns HttpResponseRedirect internally
"""


3. get_object_or_404(Model, **lookup)
"""
Fetch single object from DB.
If object exists → return object
If not → raise Http404 automatically
"""


4. get_list_or_404(Model, **lookup)
"""
Fetch list/queryset from DB.
If result exists → return list/queryset
If empty → raise Http404
"""


5. HttpResponse(content)
"""
Basic HTTP response.
Used for plain text or HTML response manually.
"""


6. JsonResponse(data_dict)
"""
Returns JSON response.
Automatically converts Python dict → JSON format.
"""


7. HttpResponseRedirect(url)
"""
Redirect response (low-level form of redirect()).
"""


8. raise Http404("message")
"""
Manual exception to return 404 page.
"""


9. FileResponse(file_object)
"""
Used to send files (PDF, images, downloads).Efficient file streaming response.
"""


10. StreamingHttpResponse(streaming_content)
"""
Used for streaming large data in chunks.
Examples:
video streaming
large file generation
real-time output
"""


11. reverse("url_name")
"""
Convert URL name → actual URL string. Used to avoid hardcoding URLs. for pretty url kwargs={'id': 5}
"""


12. reverse_lazy("url_name")
"""
Same as reverse(), but evaluated lazily.
Used in:class-based views
settings files
"""

