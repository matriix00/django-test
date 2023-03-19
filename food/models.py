from email.mime import image
from unicodedata import name
from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Food(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200,null=True)
    image=models.CharField(max_length=200,null=True)
    no_of_items=models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_show_url(self):
        return reverse("food.show",kwargs={"id":self.id})

    def get_all_url(self):
        return reverse("food.home")
    #1
    def get_delete_url(self):
        return reverse("food.delete",kwargs={"id":self.id})
    #1
    def get_edit_url(self):
        return reverse("food.update",kwargs={"pk":self.id})