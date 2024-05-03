from django.db import models


class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    manager_name = models.CharField(max_length=150)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.manager_name

    class Meta:
        db_table = 'manager'


class Packages(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=150)
    short_description = models.CharField(max_length=500)
    full_description = models.CharField(max_length=2000)
    area_covers = models.CharField(max_length=1000)
    package_image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.package_name

    class Meta:
        db_table = 'packages'













# Create your models here.
