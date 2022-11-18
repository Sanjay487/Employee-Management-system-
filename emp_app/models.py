from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Department, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Role, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    
class Employees(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    joining_date = models.DateField()
    salary = models.IntegerField()
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    
    def __str__(self):
        return "%s  %s , %s" %(self.first_name, self.last_name, self.phone)