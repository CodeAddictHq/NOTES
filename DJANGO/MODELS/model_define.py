# So model is basically a db file which contains tables
# define a model 
from django.db import models
class Model_Name(models.Model):
    field_name = models.ModelField(att1, att2....)

#a model table contains a lot of columns and rows, rows can be unlimited but columns is what we define 
"""
we have to inherit the class called Model from django.db.models to make our model work
model module has so many class which we call field , a field defines what type of data a column gonna to store
(this are bassically class defined in mldels module)
"""
