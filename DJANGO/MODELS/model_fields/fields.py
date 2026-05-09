#model fields (this are bassically classes defined in module called model)


#Text related fields 
1.CharField(max_length=int)
"""
This class defines that limited charecters can be stored in this column , this takes 1 
#mendatory att 
1.(max_length=int) - This defines how much chars can be stored 
"""
2.TextField()
"""
This class defines that unlimited texts can be stored in this column (this has no mendatory att)
"""




#Number related 
3.IntegerField()
"""
This class defines that integers can be stored in this column
"""

4.DecimalField(max_digits=int, decimal_places=int)
"""
This class defines that decimals can be stored in this column
this takes 2 mendatory args
1.max_digits
defines total number of digits (before + after decimal)
2.decimal_places
defines how much digits gonna be remain after . 
"""



#booll val related
5.BooleanField()
"""
This class defines that only bool vals can be stored in this column
"""


#time&data related
6.DateTimeField()
"""
This class defines that date and time can be stored in this column at the same time 
#2 optionam uniq arguments it has 
1.auto_now=True
it stores the created time and always changes time when object is updated 
2.auto_now_add=True
it stores the created time and never this time can be updated 
"""


#Relation to other related
7.ForeignKey(Model, on_delete=models.CASCADE)
"""
This class defines to make relation to only one object it tells that parent object is only one but child object can be unlimited (one to many)
#it takes 2 mandetory arguments
1.a Model
with which models object this objects relation will be created 

2.on_delete= models.options
CASCADE  - delete হয়ে যাবে
SET_NULL - relation breaks with parent(null=True)Thakte hobe
PROTECT - cant delete parent if has child 
DO_NOTHING - ignore
SET_DEFAULT - default value (defalut=val)set korte hobe
#on_delete tells what to do when the parent is deleted
"""

8.ManyToManyField(Model_name)
"""
This class defines that creating object can be link with many other multiple objects
#takes one mandetory per
1.Model_name 
tells from which models objects can be link with this object
"""

9.OneToOneField(Model_name, on_delete=models.oparetion)
"""
This class defines that with only one object can be link up with it and linked object cant be link again
#tales 2 mandetory argument
1.model 
tells with which model objects can be linked
2.on_delete
same like ForeignKey...
"""

