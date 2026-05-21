===========================================================
DJANGO GENERIC CLASS-BASED VIEWS (GCBV) - MASTER NOTES
===========================================================

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

1. ListView
Used to show a list of multiple objects (e.g. all blog posts)
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"
    paginate_by = 5
    ordering = ["-id"]
    # Use queryset instead of model when you need filtering
    queryset = Post.objects.filter(published=True).select_related("author")
    # Control which objects come from the database (optional)
    def get_queryset(self):
        # get_queryset() is preferred over queryset attribute
        # when logic depends on request (user, search, filters)
        queryset = Post.objects.filter(published=True)

        # Filter by search query from URL ?q=something
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(title__icontains=query)

        # Filter by category from URL ?category=django
        category = self.request.GET.get("category")
        if category:
            queryset = queryset.filter(category__slug=category)

        return queryset.select_related("author").order_by("-created_at")
    # Add extra variables to send to the template (optional)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Always call super() first - it builds the base context with object_list, page_obj etc.
        context["page_title"] = "All Posts"
        context["total_count"] = self.get_queryset().count()
        context["search_query"] = self.request.GET.get("q", "")
        return context
    # Override template name dynamically (optional)
    def get_template_names(self):
        if self.request.headers.get("HX-Request"):  # htmx request
            return ["post_list_partial.html"]
        return ["post_list.html"]

Important Attributes:
    model- Which model to fetch from the database
    queryset- Custom queryset (wins over model if both are set)
    template_name- Which HTML template to render
    context_object_name - Variable name used in template (default: object_list)
    paginate_by- How many objects to show per page
    ordering- How to sort results (use - for descending, e.g. "-id")
    paginate_orphans - Minimum items allowed on the last page before merging with previous
    allow_empty - If False, returns 404 when queryset is empty (default: True)
Important Methods:
    get_queryset()- Control which objects come from the database
    get_context_data()      - Add extra variables to send to the template
    get_template_names()    - Return list of template names to try (first found is used)
    get_paginate_by()       - Return paginate_by dynamically (e.g. from URL param)
    get_ordering()          - Return ordering dynamically
    dispatch()              - Entry point, runs before get/post
    setup()- Runs before dispatch, sets request/args/kwargs

    # Dynamic paginate_by example:
    def get_paginate_by(self, queryset):
        return self.request.GET.get("per_page", 10)

    # Dynamic ordering example:
    def get_ordering(self):
        return self.request.GET.get("sort", "-created_at")
Built-in Template Variables:
    {{ posts }}                           - Your list of objects (or object_list by default)
    {{ object_list }}                     - Same list, always available regardless of context_object_name
    {{ page_obj }}                     - Current page info (when pagination is on)
    {{ page_obj.number }}                 - Current page number
    {{ page_obj.has_next }}               - True if next page exists
    {{ page_obj.has_previous }}           - True if previous page exists
    {{ page_obj.next_page_number }}       - Next page number (check has_next first)
    {{ page_obj.previous_page_number }}   - Previous page number (check has_previous first)
    {{ page_obj.start_index }}            - Index of first item on page
    {{ page_obj.end_index }}              - Index of last item on page
    {{ paginator }}                       - Full paginator object
    {{ paginator.num_pages }}             - Total number of pages
    {{ paginator.count }}                 - Total number of objects across all pages
    {{ paginator.page_range }}            - Range of page numbers e.g. [1, 2, 3, 4]
    {{ is_paginated }}                    - True if there is more than one page
Interview Questions:
    Q: What is the default context_object_name in ListView?
    A: object_list. Your custom context_object_name is added alongside it, not replacing it.

    Q: How does Django know which page to show?
    A: It reads the ?page= GET parameter automatically. You don't have to do anything.

    Q: What happens if paginate_by is not set?
    A: All objects are returned in one page. is_paginated will be False.




2. DetailView
Used to show full details of a single object (e.g. one blog post)
class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

    # Use slug in the URL instead of pk (optional)
    slug_field = "slug"        # the field name on the model
    slug_url_kwarg = "slug"    # the name used in the URL pattern

    # Custom way to fetch the object (optional)
    def get_object(self):
        # get_object() fetches and returns the single object
        # By default it uses pk or slug from URL kwargs
        # Override when you need custom lookup logic
        obj = Post.objects.get(slug=self.kwargs["slug"])
        # Increment view count as a side effect (common pattern)
        obj.views = obj.views + 1
        obj.save(update_fields=["views"])
        return obj

    # get_queryset() in DetailView acts as a security filter
    # Object must exist in this queryset or 404 is raised
    def get_queryset(self):
        return Post.objects.filter(published=True).select_related("author")

    # Add extra variables to send to the template (optional)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object is the fetched object - available after get_object() runs
        context["related_posts"] = Post.objects.filter(
            category=self.object.category
        ).exclude(pk=self.object.pk)[:5]
        context["comments"] = self.object.comments.all()
        return context
Important Attributes:
    model               - Which model to fetch from the database
    queryset            - Used as base queryset, object must exist in it
    template_name       - Which HTML template to render
    context_object_name - Variable name used in template (default: object)
    slug_field          - The model field used as the slug
    slug_url_kwarg      - The URL keyword argument that holds the slug value
    pk_url_kwarg        - URL kwarg name for pk (default: "pk", change if needed)
Important Methods:
    get_object()            - Fetches and returns the single object
    get_queryset()          - Base queryset the object must exist in (security filter)
    get_context_data()      - Add extra variables to send to the template
    get_template_names()    - Return list of template names to try
    dispatch()              - Entry point for the request

    # get_object_or_404 behavior:
    # If pk/slug doesn't exist in queryset, Django raises 404 automatically
    # You don't need to write try/except in get_object() for basic cases

    # self.object:
    # After get_object() runs, the result is stored as self.object
    # Available in get_context_data() and get_template_names()
Built-in Template Variables:
    {{ post }}          - Your object (or object by default)
    {{ object }}        - Same object, always available
Interview Questions:
    Q: How does DetailView find the object?
    A: It looks for pk or slug in self.kwargs (from the URL), then calls get_object()
       which does get_queryset().filter(pk=pk) or filter(slug=slug).

    Q: What is the difference between get_object() and get_queryset() in DetailView?
    A: get_queryset() defines the allowed pool of objects.
       get_object() picks one specific object from that pool.
       If the object is not in get_queryset(), a 404 is raised.

    Q: How do you show a 404 if a post is unpublished?
    A: Override get_queryset() to filter(published=True).
       DetailView will automatically 404 if the object is not in the queryset.



3. CreateView
Used to show a form to create a new object and save it to the database
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_form.html"
    fields = ["title", "content"]   # which fields to show in the form
    success_url = reverse_lazy("post-list")  # always use reverse_lazy here

    # Use a custom form class instead of fields (optional)
    # form_class = PostForm
    # Note: cannot use both fields and form_class together

    # Customize initial values for the form fields
    def get_initial(self):
        initial = super().get_initial()
        initial["title"] = "Untitled Post"
        # Useful for pre-filling form from GET params
        initial["category"] = self.request.GET.get("category", "")
        return initial

    # Access and modify the form object before validation
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Customize form here e.g. remove a field, add CSS class
        form.fields["title"].widget.attrs["placeholder"] = "Enter post title"
        return form

    # Control what data is passed into the form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # kwargs contains: initial, instance, data (POST), files
        # Useful for passing extra arguments to custom forms
        kwargs["user"] = self.request.user  # if your form __init__ accepts user
        return kwargs

    # Runs when form is valid - good place to set extra data before saving
    def form_valid(self, form):
        form.instance.author = self.request.user  # attach logged-in user
        form.instance.ip_address = self.request.META.get("REMOTE_ADDR")
        # form.save() has NOT happened yet at this point
        # Calling super().form_valid(form) triggers form.save()
        response = super().form_valid(form)
        # After super(), self.object is the saved instance
        # Good place for post-save actions like sending email, logging
        return response

    # Runs when form has errors (optional)
    def form_invalid(self, form):
        # form.errors contains all validation errors
        # super() re-renders the template with the form and its errors
        return super().form_invalid(form)

    # Redirect to the newly created object's detail page
    def get_success_url(self):
        # self.object is available after form_valid saves
        return reverse("post-detail", kwargs={"pk": self.object.pk})
        # use reverse() not reverse_lazy() inside methods

    # Add extra variables to send to the template (optional)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Post"
        context["form_action"] = "Create"
        return context
Important Attributes:
    model               - Which model this form creates
    queryset            - Rarely used in CreateView
    template_name       - Which HTML template to render
    fields              - List of model fields to include in the form
    form_class          - Use a custom ModelForm instead of auto-generating from fields
    success_url         - Where to redirect after object is successfully created
    initial             - Dict of initial values for form fields
    prefix              - HTML name prefix for form fields (for multiple forms on one page)
Important Methods:
    get_form()          - Returns the form instance
    get_form_kwargs()   - Returns dict of arguments passed to the form constructor
    get_form_class()    - Returns the form class to use
    get_initial()       - Returns initial data dict for the form
    form_valid()        - Called when form passes validation - save extra data here
    form_invalid()      - Called when form fails validation - handle errors here
    get_context_data()  - Add extra variables to send to the template
    get_success_url()   - Return redirect URL after successful save (overrides success_url)
    get_template_names() - Return list of template names to try
    dispatch()          - Entry point for the request
Built-in Template Variables:
    {{ form }}          - The form object
    {{ form.as_p }}     - Form rendered as paragraph tags
    {{ form.as_table }} - Form rendered as table rows
    {{ form.as_ul }}    - Form rendered as list items
    {{ form.errors }}   - All form errors
    {{ form.non_field_errors }} - Errors not tied to a specific field
    {{ form.field_name }}       - Individual field
    {{ form.field_name.errors }} - Errors for a specific field
    {{ form.field_name.label }}  - Label for a field
    {{ form.field_name.id_for_label }} - HTML id for the field label
Interview Questions:
    Q: What is the difference between fields and form_class?
    A: fields auto-generates a ModelForm from the model.
       form_class uses your custom ModelForm with full control over validation, widgets etc.
       You cannot use both at the same time.

    Q: When exactly does form.save() get called?
    A: Inside super().form_valid(form). Not before. Not after unless you call it manually.

    Q: How do you attach the logged-in user to the object before saving?
    A: Override form_valid(), set form.instance.author = self.request.user,
       then call super().form_valid(form).



4. UpdateView
Used to show a pre-filled form to edit an existing object
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "post_form.html"   # can reuse the same template as CreateView
    fields = ["title", "content"]
    success_url = reverse_lazy("post-list")

    # Only allow the author to update their own post
    # get_queryset() here acts as BOTH a filter AND a security check
    # If the object is not in this queryset, Django raises 404
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    # Permission check for UserPassesTestMixin
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    # Pre-fill extra initial data not from the instance (optional)
    def get_initial(self):
        initial = super().get_initial()
        initial["category"] = self.object.category if hasattr(self, "object") else None
        return initial

    # Customize the form (optional)
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # e.g. make a field read-only on update
        form.fields["title"].disabled = True
        return form

    # Runs when form is valid (optional)
    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

    # Redirect to the updated object's page
    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.pk})

    # Add extra variables to send to the template (optional)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Post"
        context["form_action"] = "Update"
        # self.object is available here - it's the existing post being edited
        context["post"] = self.object
        return context

Important Attributes:
    model               - Which model to update
    queryset            - Base queryset - object must exist here or 404
    template_name       - Which HTML template to render (can reuse create template)
    fields              - List of model fields to show in the form
    form_class          - Use a custom ModelForm instead of auto-generating from fields
    success_url         - Where to redirect after successful update
    initial             - Extra initial values to add on top of instance values
Important Methods:
    get_object()        - Fetches the object to be updated (pre-fills form)
    get_queryset()      - Security filter - object must be in this queryset
    get_form()          - Returns the form pre-filled with instance data
    get_form_kwargs()   - Returns kwargs including instance for the form
    get_initial()       - Returns extra initial data on top of instance data
    form_valid()        - Called when form passes validation
    form_invalid()      - Called when form fails validation
    get_context_data()  - Add extra variables to send to the template
    get_success_url()   - Return redirect URL after save
Built-in Template Variables:
    {{ form }}          - Form pre-filled with existing object data
    {{ object }}        - The object being updated
    {{ post }}          - Same object (if context_object_name is set)
Interview Questions:
    Q: How does UpdateView pre-fill the form?
    A: get_form_kwargs() passes instance=self.object to the form constructor.
       ModelForm automatically pre-fills fields from the instance.

    Q: What is the difference between UpdateView and CreateView internally?
    A: UpdateView calls get_object() first to get the existing instance.
       It passes instance to the form so form.save() updates instead of creates.
       CreateView passes no instance so form.save() creates a new object.



5. DeleteView
Used to show a confirmation page and delete the object on submit
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy("post-list")

    # Only allow the author to delete their own post
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    # Permission check for UserPassesTestMixin
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    # Override to do soft delete instead of hard delete (optional)
    def form_valid(self, form):
        self.object = self.get_object()
        # Soft delete: mark as deleted instead of removing from db
        self.object.is_deleted = True
        self.object.save()
        return redirect(self.get_success_url())
        # If you want hard delete, just call super().form_valid(form)

    # Add extra variables to send to the template (optional)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Delete Post"
        # Useful to show the object name in the confirmation message
        context["object_name"] = self.object.title
        return context

    def get_success_url(self):
        return reverse_lazy("post-list")

Important Attributes:
    model               - Which model to delete
    queryset            - Security filter - object must be in here
    template_name       - Confirmation page template
    success_url         - Where to redirect after deletion
Important Methods:
    get_object()        - Fetches the object to delete
    get_queryset()      - Security filter - object must exist here
    form_valid()        - Where the actual deletion happens (override for soft delete)
    get_context_data()  - Add extra variables to send to the template
    get_success_url()   - Return redirect URL after deletion
Interview Questions:
    Q: Why must delete use a POST form and not a GET link?
    A: GET requests must be safe and idempotent (no side effects).
       Deleting data is a side effect. Browsers and crawlers can follow GET links
       accidentally causing unintended deletions.

    Q: How do you implement soft delete in DeleteView?
    A: Override form_valid(), set a flag like is_deleted=True, save the object,
       and redirect manually. Do not call super() since that does the hard delete.



6. TemplateView
Used to render a simple page that does not need a model (e.g. homepage, about page)
class HomePageView(TemplateView):
    template_name = "home.html"

    # Add data to the template (optional)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_posts"] = Post.objects.filter(published=True)[:5]
        context["featured_categories"] = Category.objects.all()[:8]
        context["page_title"] = "Homepage"
        context["stats"] = {
            "total_posts": Post.objects.count(),
            "total_users": User.objects.count(),
        }
        return context

    # Handle GET params or do early checks (optional)
    def dispatch(self, request, *args, **kwargs):
        # Example: maintenance mode redirect
        if settings.MAINTENANCE_MODE and not request.user.is_staff:
            return redirect("maintenance")
        return super().dispatch(request, *args, **kwargs)

    def get_template_names(self):
        # Serve different template to mobile (optional)
        if self.request.user_agent.is_mobile:
            return ["home_mobile.html"]
        return ["home.html"]

Important Attributes:
    template_name       - Which HTML template to render
    extra_context       - Dict of extra context to pass without overriding get_context_data()

    # extra_context shortcut (for simple static data):
    class AboutView(TemplateView):
        template_name = "about.html"
        extra_context = {"page_title": "About Us"}

Important Methods:
    get_context_data()      - Add variables to send to the template (no model is auto-loaded)
    get_template_names()    - Return list of template names to try
    dispatch()              - Entry point, good for early redirects
    setup()                 - Runs before dispatch

Built-in Template Variables:
    {{ view }}          - The view instance itself (available in all GCBVs)
    # No model-related variables - you add everything manually in get_context_data()


AUTHENTICATION MIXINS
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin   # also available - check below
)

IMPORTANT: Always put mixins BEFORE the view class in the inheritance order.
Reason: Python MRO (Method Resolution Order) reads left to right.
Mixins override dispatch() to check permissions before the view runs.
Wrong order = view runs before permission check = security bug.
---

1.LoginRequiredMixin
    Redirects to login page if the user is not logged in.
    Internally overrides dispatch() to check request.user.is_authenticated.
    class PostCreateView(LoginRequiredMixin, CreateView):
        login_url = "/login/"           # optional: set a custom login page
        redirect_field_name = "next"    # optional: query param name after login
        # Default login_url comes from settings.LOGIN_URL
        ...
    # In settings.py:
    LOGIN_URL = "/accounts/login/"   # default Django login URL
---
UserPassesTestMixin
    Runs a custom test - if it fails, user gets a 403 Forbidden error.
    You must define test_func() - it must return True or False.
    class PostUpdateView(UserPassesTestMixin, UpdateView):
        def test_func(self):
            post = self.get_object()
            return self.request.user == post.author  # only author can edit

        # Optional: customize the behavior when test fails
        def handle_no_permission(self):
            return redirect("home")  # instead of 403, redirect

    # Raise exception instead of redirect (default is redirect to login or 403)
    raise_exception = True   # add as class attribute to always show 403

---

PermissionRequiredMixin
    Checks if user has a specific Django permission.

    class PostCreateView(PermissionRequiredMixin, CreateView):
        permission_required = "blog.add_post"
        # or multiple permissions:
        permission_required = ["blog.add_post", "blog.change_post"]
        raise_exception = True  # 403 instead of redirect

---

MIXIN COMBINATION PATTERN (real project):
    class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        # 1. LoginRequiredMixin: must be logged in
        # 2. UserPassesTestMixin: must pass test_func
        # 3. UpdateView: then do the update
        def test_func(self):
            return self.request.user == self.get_object().author



OVERRIDING METHODS CORRECTLY - RULES
Rule 1: Always call super() in get_context_data()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # builds base context
        context["my_data"] = "value"
        return context
    # Without super(), built-in context vars like object_list, page_obj are missing

Rule 2: Always call super() in form_valid() unless you want to stop default behavior
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)  # this calls form.save() and redirects
    # Without super(), the object is never saved and redirect never happens

Rule 3: Always call super() in dispatch() unless you want to block the request
    def dispatch(self, request, *args, **kwargs):
        if some_condition:
            return redirect("home")  # block early
        return super().dispatch(request, *args, **kwargs)  # continue normally

Rule 4: In get_queryset(), do NOT call super() - just return your queryset
    def get_queryset(self):
        return Post.objects.filter(published=True)  # no super() needed here

Rule 5: In form_valid() you can access self.object AFTER calling super()
    def form_valid(self, form):
        response = super().form_valid(form)  # saves and sets self.object
        send_email(self.object)              # now safe to use self.object
        return response



CONTEXT FLOW - HOW CONTEXT DATA TRAVELS


    1. get_context_data() is called
    2. super().get_context_data() builds base context:
        - ListView adds: object_list, page_obj, paginator, is_paginated
        - DetailView adds: object, post (if context_object_name set)
        - CreateView/UpdateView adds: form
        - All views add: view (the view instance)
    3. You add your own keys to context dict
    4. Context dict is passed to template
    5. Template renders with all context variables available

Mental model:
    context is just a Python dict.
    super() fills in the built-in keys.
    You add your custom keys on top.
    Template receives the final dict.



PERMISSION HANDLING PATTERNS
Pattern 1: Login required only
    class MyView(LoginRequiredMixin, ListView):
        pass
Pattern 2: Login + ownership check
    class MyView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        def test_func(self):
            return self.request.user == self.get_object().author

Pattern 3: Login + Django permission
    class MyView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
        permission_required = "app.add_model"

Pattern 4: Staff only
    class MyView(UserPassesTestMixin, ListView):
        def test_func(self):
            return self.request.user.is_staff

Pattern 5: Owner or staff
    class MyView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        def test_func(self):
            obj = self.get_object()
            return self.request.user == obj.author or self.request.user.is_staff

Pattern 6: Custom handle_no_permission (redirect instead of 403)
    class MyView(UserPassesTestMixin, UpdateView):
        def test_func(self):
            return self.request.user == self.get_object().author
        def handle_no_permission(self):
            return redirect("home")


===========================================================
REUSABLE PATTERNS USED IN REAL PROJECTS
===========================================================

Pattern 1: Attach logged-in user to object on create
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

Pattern 2: Filter queryset to logged-in user's objects
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

Pattern 3: Redirect to detail page after create/update
    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.pk})

Pattern 4: Pass URL kwargs into queryset filter
    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs["category_slug"])

Pattern 5: Search filter in ListView
    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

Pattern 6: Send email after successful create
    def form_valid(self, form):
        response = super().form_valid(form)
        send_notification_email(self.object)
        return response

Pattern 7: Multiple forms in one CreateView
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["profile_form"] = ProfileForm(self.request.POST)
        else:
            context["profile_form"] = ProfileForm()
        return context

Pattern 8: Soft delete in DeleteView
    def form_valid(self, form):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()
        return redirect(self.get_success_url())

Pattern 9: Increment view count in DetailView
    def get_object(self):
        obj = super().get_object()
        obj.__class__.objects.filter(pk=obj.pk).update(views=F("views") + 1)
        return obj

Pattern 10: Dynamic template based on user role
    def get_template_names(self):
        if self.request.user.is_staff:
            return ["admin_post_list.html"]
        return ["post_list.html"]


===========================================================
MOST IMPORTANT METHODS (across all views)
===========================================================

    setup()             - Runs first, sets request/args/kwargs on self
    dispatch()          - Routes to get() or post() based on HTTP method
    get()               - Handles GET requests
    post()              - Handles POST requests (form views)
    get_queryset()      - Control which objects come from the database
    get_object()        - Custom logic to fetch a single object
    get_context_data()  - Add extra variables to send to the template
    get_template_names() - Return list of templates to try
    get_form()          - Return form instance (Create/Update)
    get_form_kwargs()   - Return kwargs for form constructor
    get_form_class()    - Return form class to use
    get_initial()       - Return initial data for form fields
    form_valid()        - Runs when a form passes validation
    form_invalid()      - Runs when a form fails validation
    get_success_url()   - Return redirect URL after success


===========================================================
MOST IMPORTANT ATTRIBUTES (across all views)
===========================================================

    model               - Which model to use
    queryset            - Custom base queryset (overrides model if set)
    template_name       - Which HTML template to render
    context_object_name - Variable name in template for the object/list
    fields              - Form fields to include (Create/Update)
    form_class          - Custom form class (Create/Update)
    success_url         - Redirect URL after success (use reverse_lazy)
    paginate_by         - Items per page (ListView)
    paginate_orphans    - Min items on last page before merging (ListView)
    ordering            - Default ordering for queryset (ListView)
    allow_empty         - Show empty list or 404 (ListView, default True)
    slug_field          - Model field used as slug (Detail/Update/Delete)
    slug_url_kwarg      - URL kwarg name for slug (Detail/Update/Delete)
    pk_url_kwarg        - URL kwarg name for pk (default: "pk")
    extra_context       - Static extra context dict (TemplateView shortcut)
    initial             - Initial values for form fields (Create/Update)
    prefix              - HTML name prefix for form fields
    raise_exception     - Raise 403 instead of redirect (UserPassesTestMixin)
    login_url           - Custom login redirect URL (LoginRequiredMixin)
    permission_required - Required permission string (PermissionRequiredMixin)
