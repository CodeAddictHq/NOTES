#Some genric class based views (Shortcuts) We use this by inheritting this class  in views heres code 

1. ListView
#Used to show all objects of a model at once (list page)
class PostListView(ListView):
    model = Post  #Decides which model data to show
    template_name = "post_list.html"  #Template for list page
    context_object_name = "posts"  #Name of queryset in template
    paginate_by = 5  #Pagination (5 items per page)
    ordering = ["-id"]  #Newest first (descending order)


2. DetailView
#Used to show single object details (single item page) 
class PostDetailView(DetailView):
    model = Post  #Which model object to show
    template_name = "post_detail.html"  #Detail page template
    context_object_name = "post"  #Single object name in template
#You have to send <pk/slug> in url route otherwise it wont work

3. CreateView
#Used to create new object using built-in form
class PostCreateView(CreateView):
    model = Post  #Model to create object
    template_name = "post_form.html"  #Form template
    fields = ["title", "content"]  #Form fields
    success_url = "/"  #Redirect after success



4. UpdateView
#Used to edit/update existing object
class PostUpdateView(UpdateView):
    model = Post  #Model to update
    template_name = "post_form.html"  #Form template
    fields = ["title", "content"]  #Editable fields
    success_url = "/"  #Redirect after update


5. DeleteView
#Used to delete object with confirmation page
class PostDeleteView(DeleteView):
    model = Post  #Model to delete object
    template_name = "post_confirm_delete.html"  #Confirmation page
    success_url = "/"  #Redirect after delete


6. TemplateView
#Used to render simple static page (no model logic)
class HomePageView(TemplateView):
    template_name = "home.html"  #Only renders template