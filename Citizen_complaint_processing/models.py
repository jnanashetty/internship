from django.db import models

# Create your models here.
class admin(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class user_info(models.Model):
    fname=models.CharField(max_length=100)
    sname=models.CharField(max_length=100)
    email_id=models.EmailField(max_length=50, error_messages={"invalid":"This is an invalid email ID","blank":"This field cannot be left blank"},unique=True)
    password=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pin=models.IntegerField()
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    phone=models.BigIntegerField()

class complaints(models.Model):
    department=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    date_of_occurence=models.DateField(format("%d-%m-%Y"))
    complaint_desc=models.TextField()
    status=models.BooleanField(default=False)
    user_id=models.ForeignKey(user_info,on_delete=models.CASCADE)