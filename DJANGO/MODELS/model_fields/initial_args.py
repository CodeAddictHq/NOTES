# Model Field Optional Args

1.null=True
# allow to store NULL in row

2.default='str'/Number
# default value if nothing provided

3.unique=True            
# no duplicate values allowed can use this field in Model.objects.get(this_field=val)

4.db_index=True          
# create DB index for field (used of faster query 

5.primary_key=True       
# make this field primary key

6.blank=True            
# allow empty value in forms/admin

7.choices=[(...)]        
# restrict values to fixed options

8.validators=[...]     
# custom validation rules

9.error_messages={...} 
# custom error messages

# Admin / UI behavior

10.verbose_name="..."   
# readable name in admin panel

11.help_text="..."      
# hint text in forms/admin

12.editable=False        
# field cannot be edited in admin/forms
