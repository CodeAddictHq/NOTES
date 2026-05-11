#With widget we control what html element gonna be our form field

#this is out arg of form field
#defining a widget 
form_field = forms.FormField(widget=forms.WidgetName())

'Field decides WHAT data and Widget decides HOW UI looks dont validates data much'
#some widget to use 
forms.TextInput()       
# normal single line input box

forms.EmailInput()      
# email input (HTML email type)

forms.NumberInput()    
# number input (HTML number type)

forms.PasswordInput()     
# hidden password input

forms.Textarea()      
# big multiline text box

forms.Select()      
# dropdown select box used with Choiceinput

forms.CheckboxInput()  
# single checkbox

forms.FileInput()     
# file upload input

forms.DateInput()       
# date picker

forms.DateTimeInput()   
# date + time picker

#we can also set html elements attribute with widget arg 
widget=forms.TextInput(attrs={
    "placeholder": "Enter your name",
    "class": "form-control"
})
