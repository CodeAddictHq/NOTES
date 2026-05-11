# With widget we control what HTML element is used for the form field

# Field decides WHAT data + validation
# Widget decides HOW UI looks (HTML only, not validation)

# Correct usage
field_name = forms.CharField(widget=forms.TextInput())


# -------------------------
# COMMON WIDGETS (Django)
# -------------------------

forms.TextInput(attrs=None)
# single line text input

forms.EmailInput(attrs=None)
# email input (type="email")

forms.NumberInput(attrs=None)
# number input (type="number")

forms.PasswordInput(attrs=None, render_value=False)
# password field (hidden text)

forms.Textarea(attrs=None)
# multiline text area

forms.Select(attrs=None, choices=())
# dropdown select (needs choices)

forms.CheckboxInput(attrs=None)
# single checkbox

forms.FileInput(attrs=None)
# file upload input

forms.DateInput(attrs=None, format=None)
# date picker input

forms.DateTimeInput(attrs=None, format=None)
# date + time input


# -------------------------
# HTML ATTRIBUTES (IMPORTANT)
# -------------------------

widget=forms.TextInput(attrs={
    "placeholder": "Enter your name",
    "class": "form-control",
    "id": "main_post"
})