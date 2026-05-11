#To show form in our template at first we have to send as a contex from views.py 
#Everything is same like coustom form just we use database field_names


1.{{ form }}
#renders form fields only not with form tag and submit button

2.{{ form.field_name }}
#renders field with label

3.{{ form.field_name.label }}
#label text

4.{{ form.field_name.errors }}  
#returns a dict where keys are field and values are errors 

5.{{ form.field.help_text }}
#returns help text if seted on form 

6.{{ form.as_p }}
#Show form in peragraph style

7.{{ form.as_ul }}
#Show form in table style

8.{{ form.as_table }}
#Show form in list style

9.{{ form.field_name.value }}
#Shows form value 

