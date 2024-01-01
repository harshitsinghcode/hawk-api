from django.db import models


class Company(models.Model):
    comany_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100, choices=(('IT','IT'), 
                                                   ('NON IT', 'NON IT'),
                                                   ("Mobile Phones", "Mobile Phones")
                                                   ))
    added_data=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' - '+self.location

#employee model

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=(
        ('Manager','manager'),
        ('SDE','SDE'),
        ('Project Lead','PL')
    ))
    
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    
    
