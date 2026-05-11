#Form feilds are used to valodate data

#Core usages
1.CharField(max_length=int)
#Used to take input limited chars, takes 1 mandetory arg max_length

2.EmailField()
#Used for take input Email autometically validates emails input

3.IntegerField()
#Used to take input Integer

4.BooleanField()
#used to input bool val

5.DateField()
#takes date input 

6.FileField()
#Used to take input Files like pdf/..etc accepts all type of file

7.ImageField()
#accepts only image file


8.ChoiceField(choices=[(), ()...])
#used to tale input choices takes 1 mandetory arg

9.ModelChoiceField(choices=queryset)
#used to take input choice of object from db takes 1 mandetory arg choice 

#less Used

10. DecimalField(max_digits=int, decimal_places=int)
#Used to take decimal numbers like price/money, requires precision control using max_digits and decimal_places


11. URLField()
#Used to take URL input, automatically validates proper website links


12. DateTimeField()
#Used to take combined date and time input (e.g. event time, created_at)


13. MultipleChoiceField(choices=[(), ()...])
#Used to select multiple options from a fixed list, returns list of selected values


14. ModelMultipleChoiceField(queryset=Model.objects.all())
#Used to select multiple objects from database, returns queryset of model instances





#Rare case

15. FloatField()
#Used to take floating point numbers (less strict than DecimalField, no precision control)


16. RegexField(regex="pattern")
#Used to validate input using custom regex pattern (advanced validation cases)


17. SlugField()
#Used to take URL-friendly text (letters, numbers, hyphens), commonly for SEO URLs


18. GenericIPAddressField()
#Used to take IPv4 or IPv6 address input


19. UUIDField()
#Used to take UUID values (unique identifiers for models/objects)


20. JSONField()
#Used to store or accept JSON formatted data (dict/list structure)


21. TimeField()
#Used to take only time input (hour, minute, second without date)


# common arguments 
required=True,
label="Name"
initial="Adib",
max_length=50,
min_length=3,
help_text="Enter your name",
disabled=False,
error_messages={"required": "This field is required"}
choices=[("m", "Male"), ("f", "Female")]
