from django.db import models

# Create your models here.
class EmpMaster(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    # id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    DATE = models.CharField(max_length=40) 
    PATIENT_NAME = models.CharField(max_length=50)
    GENDER = models.CharField(max_length=10)
    AGE = models.IntegerField()
    ROOM_NO = models.IntegerField(null=True)
    UHID_NO = models.CharField(max_length=20,null=True)
    ADMITTED_UNDER = models.CharField(max_length=50,null=True)
    DEPARTMENT = models.CharField(max_length=50,null=True)
    EST_TIME= models.CharField(max_length=50,null=True)
    COMPLAINTS = models.CharField(max_length=400,null=True)
    
    CLOSURE= models.CharField(max_length=40,null=True)
    STATUS = models.CharField(max_length=10,null=True)
    DATE_RESOLVED = models.CharField(max_length=40,null=True)
    REMARKS = models.CharField(max_length=400,null=True)
    COMMENTS = models.CharField(max_length=400,null=True)
