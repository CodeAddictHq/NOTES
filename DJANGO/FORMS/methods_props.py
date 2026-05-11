#There are some methods to use forms in views 

1.form = FormName(request.METHOD)
#returns the form object 

2.form.is_valid()
#Cheks form validation returns True if form data is valid as difined in Form class

3.form.cleaned_data
#If form remains valid returns datas dict where keys are form field names and values are submited data

4.form.add_error("Field_name", "Custom error message")
#adds error when excuting the code

5.form.errors
#returns all the errors as dict wher field name is key err is val

6.form.fields
#returns a dict where key are field name and val are field types

6.FormName(instance=object)
#fills existing datas of that object from db 

--- only for model form ---
7.obj.save()
#Saves object in db  with this and updates existing one 
save(commit=False)
#we can edit before save 



