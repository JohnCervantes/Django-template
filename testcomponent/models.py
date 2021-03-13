from django.db import models

# Create your models here.


class Customer(models.Model):
    """ Customer Model """
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    # profile_pic = models.ImageField(null=True, blank=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        """ Name of object"""
        return self.name


class Tag(models.Model):
    """ Tag models """
    TAGS = (
        ('Sports', 'Sports'),
        ('Summer', 'Summer'),
        ('Kitchen', 'Kitchen')
    )
    name = models.CharField(max_length=200, null=True, choices=TAGS)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    """ Product model """
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    """ Order model """
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(
        Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self) -> str:
        return self.customer.name
