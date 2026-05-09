
# DJANGO ORM CORE [the way tp control data in db with django cmds]


# CREATE
Model.objects.create(field="val", field=val)


# READ
Model.objects.all()
"""
retrurns all the objects of model
"""

Model.objects.get(id=int)
"""
retrurns the object with id, int
"""

Model.objects.filter(age=20)
"""
retrurns multiple object with matched field val
"""


Student.objects.exclude(age=20)
"""
retrurns multiple object with unmatched field val
"""

# UPDATE
obj = Student.objects.get(id=1)
obj.name = "New Name"
obj.save() #save is mendatory here

# DELETE
obj = Student.objects.get(id=1)
obj.delete()

# FILTER LOOKUPS
Student.objects.filter(age__gt=18)
# greater than
Student.objects.filter(age__gte=18)
# greater or equal
Student.objects.filter(age__lt=18)        # less than
Student.objects.filter(name__icontains="adib")  
# case-insensitive search
Student.objects.filter(name__startswith="A")
Student.objects.filter(name__endswith="b")

# ORDERING
Student.objects.all().order_by('name')
Student.objects.all().order_by('-age')

# LIMIT
Student.objects.all()[:5]

# COUNT
Student.objects.count()

# EXISTS
Student.objects.filter(name="Adib").exists()
#if object exists returns True

