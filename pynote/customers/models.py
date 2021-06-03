from django.db import models


class Service(models.Model):
    name = models.CharField("Name", max_length=255)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address =  models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
